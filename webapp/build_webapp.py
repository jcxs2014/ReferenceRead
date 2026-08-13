#!/usr/bin/env python3
"""Build the interactive webapp from background/*.md and optionally all 21 papers' literature_analysis."""
import argparse
import json
import re
import html as html_mod
import base64
import sys
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # papers/
TOOLS = HERE       # webapp/
DOCROOT = ROOT / "background"
OUT = HERE / "interactive.html"   # built artifact lives in webapp/ alongside shell + scripts
SHELL = HERE / "shell.html"
INDEX = ROOT / "INDEX.md"

PAPER_INFO = {
    "01_cosmic-ray-propagation": {"label": "宇宙线传播"},
    "02_cosmic-ray-origins":     {"label": "宇宙线起源与 UHECR"},
    "03_stellar-nucleosynthesis":{"label": "恒星核合成与丰度"},
}


def _fmt_authors(raw: str) -> str:
    """Compact author list: keep full names, join last-two with ' &'."""
    parts = [p.strip() for p in re.split(r",\s*", raw) if p.strip()]
    if not parts:
        return raw
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return parts[0] + " & " + parts[1]
    return parts[0] + " et al."


def _build_citation_map() -> dict:
    """Parse INDEX.md to auto-generate citation labels from real author/titles.
    Returns {stem: "Authors (Year)"}."""
    if not INDEX.exists():
        return {}
    text = INDEX.read_text(encoding="utf-8")
    # Entry block: ### `stem` ... | **Authors** | ... | **Title** | ...
    entries = {}
    # Split on ### `stem` boundaries
    for block in re.split(r"(?=\n### `[^`]+`\n)", text):
        stem_m = re.search(r"`([^`]+)`", block)
        if not stem_m:
            continue
        stem = stem_m.group(1).strip()

        auth_m = re.search(r"\*\*Authors?\*\*\s*[|]\s*(.+?)\s*(?:\n|$)", block, re.IGNORECASE)
        yr_m   = re.search(r"(\d{4})[_-]?\w*-(\d{4})\b", stem)

        authors = auth_m.group(1).strip() if auth_m else ""
        year    = yr_m.group(2) if yr_m else "?"
        label   = f"{_fmt_authors(authors)} ({year})" if authors else stem
        entries[stem] = label
    return entries


CITATION = _build_citation_map()
# Fallback for any stems not in INDEX (should be few/none)
_FALLBACK = {
    "0001_strong-moskalenko-ptuskin-2007": "Strong, Moskalenko & Ptuskin (2007)",
    "0001_bhattacharjee-sigl-2000":         "Bhattacharjee & Sigl (2000)",
    "0002_al-dargazelli-1996":               "Al-Dargazelli, Wolfendale, Smialkowski & Wdowczyk (1996)",
    "0003_gaisser-1990":                     "Gaisser (1990)",
    "0004_blasi-2013":                       "Blasi (2013)",
    "0005_amato-2014":                       "Amato (2014)",
    "0006_grenier-2015":                     "Grenier, Black & Strong (2015)",
    "0007_biermann-1996":                    "Biermann (1996)",
    "0001_b2fh-1957":                        "B²FH (1957)",
    "0002_trimble-1975":                     "Trimble (1975)",
    "0003_fowler-1984":                      "Fowler (1984)",
    "0004_wallerstein-1997":                 "Wallerstein et al. (1997)",
    "0005_champagne-wiescher-1992":          "Champagne & Wiescher (1992)",
    "0006_anders-grevesse":                  "Anders & Grevesse (1989)",
    "0007_grevesse-sauval-1998":             "Grevesse & Sauval (1998)",
    "0008_lodders-2003":                     "Lodders (2003)",
    "0009_asplund-2009-solar-composition":   "Asplund et al. (2009)",
    "0010_gies-lambert-1992":                "Gies & Lambert (1992)",
    "0011_kewley-2001-starburst":            "Kewley, Dopita, Sutherland, Heisler & Trevena (2001)",
    "0012_dieterich-2014-h-burning-limit":   "Dieterich, Henry, Jao, Winters, Hosey, Riedel & Subasavage (2014)",
    "0013_bertone-hooper-2018":              "Bertone & Hooper (2018)",
}
for k, v in _FALLBACK.items():
    if k not in CITATION:
        CITATION[k] = v


def slug(s):
    s = html_mod.unescape(s).lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", s).strip("-")
    return s[:80]


def convert_doc(path: Path, doc_id: str = ""):
    tmp = path.with_suffix(".fragment.html")
    args = [sys.executable, str(TOOLS / "md2doc_html.py"), str(path), str(tmp)]
    if doc_id:
        args.append(doc_id)
    r = subprocess.run(args, capture_output=True, text=True, cwd=str(TOOLS))
    if r.returncode != 0:
        raise RuntimeError(f"md2doc_html failed on {path}:\n{r.stderr}")
    try:
        content = tmp.read_text(encoding="utf-8")
    finally:
        tmp.unlink(missing_ok=True)
    return content


def _deduplicate_headings(html_body: str, parent_id: str) -> tuple:
    """Ensure all heading ids in html_body are globally unique within this doc.
    Returns (deduped_html, list_of_toc_entries)."""
    # Find all heading ids and their info
    heading_pattern = re.compile(r"<h([2-6])([^>]*)id=\"([^\"]+)\"([^>]*)>(.*?)</h", re.DOTALL)
    seen = {}   # id -> count for suffix
    new_html = html_body
    toc_entries = []

    for m in heading_pattern.finditer(html_body):
        level = int(m.group(1))
        hid   = m.group(3)
        raw   = re.sub(r"<[^>]+>", "", m.group(5)).strip()
        title = html_mod.unescape(raw)

        # Deduplicate: append -1, -2, ... for repeats
        if hid in seen:
            seen[hid] += 1
            new_hid = f"{hid}-{seen[hid]}"
            # Patch the id attribute in the HTML
            old_tag = m.group(0)
            new_tag = old_tag.replace(f'id="{hid}"', f'id="{new_hid}"')
            new_html = new_html.replace(old_tag, new_tag, 1)
            hid = new_hid
        else:
            seen[hid] = 0

        toc_entries.append({"level": level, "id": hid, "title": title,
                           "parent_id": parent_id, "parent_label": ""})

    return new_html, toc_entries


def build(include_papers=False, out=None):
    """Build the interactive HTML. `out` defaults to webapp/interactive.html."""
    if out is None:
        out = OUT
    docs        = []
    all_toc     = []
    papers_json = []

    bg_files = [
        ("00_key_values.md",      "全库关键数值速查表"),
        ("01_cosmic_rays.md",     "宇宙线（传播与起源）"),
        ("02_nucleosynthesis.md", "恒星核合成"),
        ("03_astrophysics.md",    "太阳丰度与天体物理"),
        ("04_critique_index.md",  "CRITIQUE 观点汇总"),
        ("05_glossary.md",        "全库术语表"),
    ]

    # ── Background docs ──────────────────────────────────────────
    for fname, title in bg_files:
        path   = DOCROOT / fname
        if not path.exists():
            continue
        doc_id = slug(title)
        html   = convert_doc(path, doc_id)
        # Dedup headings within this single file
        html, tocs = _deduplicate_headings(html, doc_id)
        b64    = base64.b64encode(html.encode("utf-8")).decode("ascii")
        docs.append({"id": doc_id, "slug": doc_id, "title": title,
                     "category": "背景知识", "b64": b64})
        for t in tocs:
            t["parent_id"] = doc_id
            all_toc.append(t)

    # ── Paper docs ───────────────────────────────────────────────
    if include_papers:
        for cat_dir in sorted(ROOT.glob("0[0-9]_*")):
            if not cat_dir.is_dir():
                continue
            cat_label = PAPER_INFO.get(cat_dir.name, {"label": cat_dir.name})["label"]
            for paper_dir in sorted(cat_dir.iterdir()):
                if not paper_dir.is_dir():
                    continue
                lit = paper_dir / "literature_analysis"
                if not lit.is_dir():
                    continue
                stem       = paper_dir.name
                title      = CITATION.get(stem, stem.replace("_", " "))
                paper_slug = f"paper-{slug(stem)}"

                # Collect raw HTML parts
                paper_parts = []
                for f in sorted(lit.iterdir()):
                    if f.suffix != ".md" or f.name == "99_final_summary.md":
                        continue
                    paper_parts.append(convert_doc(f, paper_slug))
                final_summary = lit / "99_final_summary.md"
                if final_summary.exists():
                    paper_parts.append(convert_doc(final_summary, paper_slug))

                paper_html = f'<div class="paper-preface"><h3>{html_mod.escape(title)}</h3></div>\n'
                paper_html += "\n".join(paper_parts)

                # Dedup headings across all combined fragments (H1 fix)
                paper_html, tocs = _deduplicate_headings(paper_html, paper_slug)

                b64 = base64.b64encode(paper_html.encode("utf-8")).decode("ascii")
                docs.append({"id": paper_slug, "slug": paper_slug,
                             "title": f"论文 · {title}",
                             "category": cat_label, "b64": b64})

                for t in tocs:
                    t["parent_id"]   = paper_slug
                    t["parent_label"] = title
                    all_toc.append(t)

                stem_yr = re.match(r"\d{4}_.+?-(\d{4})", stem)
                year    = int(stem_yr.group(1)) if stem_yr else 0
                papers_json.append({
                    "slug":     paper_slug,
                    "label":    title,
                    "year":     year,
                    "stem":     stem,
                    "category": cat_label,
                })

    # ── Inject & write ───────────────────────────────────────────
    shell = SHELL.read_text(encoding="utf-8")
    shell = shell.replace("__DOCS_JSON__",   json.dumps(docs,        ensure_ascii=False, indent=2))
    shell = shell.replace("__TOC_JSON__",     json.dumps(all_toc,     ensure_ascii=False, indent=2))
    shell = shell.replace("__PAPERS_JSON__",  json.dumps(papers_json, ensure_ascii=False, indent=2))

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(shell, encoding="utf-8")
    print(f"Wrote {out} ({len(shell)} chars)")
    print(f"  docs: {len(docs)}, toc items: {len(all_toc)}, papers: {len(papers_json)}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--include-papers", action="store_true",
                    help="include all 21 papers' literature_analysis")
    ap.add_argument("--out", type=Path, default=OUT,
                    help="output HTML path (default: webapp/interactive.html)")
    args = ap.parse_args()
    build(args.include_papers, out=args.out)
