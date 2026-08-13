#!/usr/bin/env python3
"""Build the interactive webapp from background/*.md and optionally all 21 papers' literature_analysis/."""
import argparse
import json
import re
import html as html_mod
import base64
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
ROOT = (HERE.parent).parent
TOOLS = HERE
DOCROOT = HERE.parent
OUT = DOCROOT / "background-interactive.html"
SHELL = TOOLS / "shell.html"

PAPER_INFO = {
    "01_cosmic-ray-propagation": {"label": "宇宙线传播"},
    "02_cosmic-ray-origins": {"label": "宇宙线起源与 UHECR"},
    "03_stellar-nucleosynthesis": {"label": "恒星核合成与丰度"},
}

# Mapping from folder-stem to a clean citation label
CITATION = {
    "0001_strong-moskalenko-ptuskin-2007": "Strong, Moskalenko & Ptuskin (2007)",
    "0001_bhattacharjee-sigl-2000": "Bhattacharjee & Sigl (2000)",
    "0002_al-dargazelli-1996": "Al-Dargazelli, Wamrschmidt & Gaisser (1996)",
    "0003_gaisser-1990": "Gaisser, Halzen & Hooper (1990)",
    "0004_blasi-2013": "Blasi (2013)",
    "0005_amato-2014": "Amato (2014)",
    "0006_grenier-2015": "Grenier, Black & Strong (2015)",
    "0007_biermann-1996": "Biermann (1996)",
    "0001_b2fh-1957": "B²FH (1957)",
    "0002_trimble-1975": "Trimble (1975)",
    "0003_fowler-1984": "Fowler (1984)",
    "0004_wallerstein-1997": "Wallerstein et al. (1997)",
    "0005_champagne-wiescher-1992": "Champagne & Wiescher (1992)",
    "0006_anders-grevesse": "Anders & Grevesse (1989)",
    "0007_grevesse-sauval-1998": "Grevesse & Sauval (1998)",
    "0008_lodders-2003": "Lodders (2003)",
    "0009_asplund-2009-solar-composition": "Asplund et al. (2009)",
    "0010_gies-lambert-1992": "Gies & Lambert (1992)",
    "0011_kewley-2001-starburst": "Kewley & Echle (2001)",
    "0012_dieterich-2014-h-burning-limit": "Dieterich, Boyett & Pinsonneault (2014)",
    "0013_bertone-hooper-2018": "Bertone & Hooper (2018)",
}

def slug(s):
    s = html_mod.unescape(s).lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", s).strip("-")
    return s[:80]

def slug_title(title):
    title = re.sub(r"^[1-9]\d*[\.\)]+\s*", "", title)
    title = re.sub(r"^##?\s*", "", title)
    return title

def convert_doc(path: Path):
    tmp = path.with_suffix(".fragment.html")
    r = subprocess.run(
        [sys.executable, str(TOOLS / "md2doc_html.py"), str(path), str(tmp)],
        capture_output=True, text=True, cwd=str(TOOLS)
    )
    if r.returncode != 0:
        raise RuntimeError(f"md2doc_html failed on {path}:\n{r.stderr}")
    return tmp.read_text(encoding="utf-8")

def extract_toc(html_body):
    toc = []
    for m in re.finditer(r'<h([1-4])\s+id="([^"]+)">([^<]+)</h\1>', html_body):
        level = int(m.group(1))
        toc.append({"level": level, "id": m.group(2), "title": html_mod.unescape(m.group(3).strip())})
    return toc

def get_years():
    """Return dict {stem: year} for paper-ref matching."""
    years = {}
    for cat, papers in PAPER_INFO.items():
        for p in papers.values():
            years[p["stem"]] = p["year"]
    return years

def build(include_papers=False):
    docs = []
    all_toc = []
    papers_json = []

    # 1. Background documents
    bg_files = [
        ("00_key_values.md", "全库关键数值速查表"),
        ("01_cosmic_rays.md", "宇宙线（传播与起源）"),
        ("02_nucleosynthesis.md", "恒星核合成"),
        ("03_astrophysics.md", "太阳丰度与天体物理"),
        ("04_critique_index.md", "CRITIQUE 观点汇总"),
        ("05_glossary.md", "全库术语表"),
    ]

    # 2. Paper documents (if --include-papers)
    paper_docs = []
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
                stem = paper_dir.name
                title = CITATION.get(stem, stem.replace("_", " "))
                # Collect files in order
                files = sorted(lit.iterdir())
                paper_parts = []
                for f in files:
                    if f.suffix != ".md" or f.name == "99_final_summary.md":
                        continue
                    content = convert_doc(f)
                    paper_parts.append(content)
                # 99_final_summary at end (only overview part)
                final_summary = lit / "99_final_summary.md"
                if final_summary.exists():
                    paper_parts.append(convert_doc(final_summary))

                # Build paper HTML
                paper_html = f'<div class="paper-preface"><h3>{html_mod.escape(title)}</h3></div>\n'
                paper_html += "\n".join(paper_parts)

                paper_slug = f"paper-{slug(stem)}"
                b64 = base64.b64encode(paper_html.encode("utf-8")).decode("ascii")
                docs.append({"id": paper_slug, "slug": paper_slug, "title": f"论文 · {title}", "category": cat_label, "b64": b64})

                # TOC
                for t in extract_toc(paper_html):
                    t["parent_id"] = paper_slug
                    t["parent_label"] = title
                    all_toc.append(t)

                # Papers index
                stem_year_match = re.match(r"\d{4}_(.+?)-(\d{4})", stem)
                year = stem_year_match.group(2) if stem_year_match else ""
                papers_json.append({
                    "slug": paper_slug,
                    "label": title,
                    "year": int(year) if year else 0,
                    "stem": stem,
                    "category": cat_label,
                })

    # Background docs
    for fname, title in bg_files:
        path = DOCROOT / fname
        if not path.exists():
            continue
        html = convert_doc(path)
        doc_id = slug(title)
        b64 = base64.b64encode(html.encode("utf-8")).decode("ascii")
        docs.append({"id": doc_id, "slug": doc_id, "title": title, "category": "背景知识", "b64": b64})
        for t in extract_toc(html):
            t["parent_id"] = doc_id
            all_toc.append(t)

    shell = SHELL.read_text(encoding="utf-8")
    shell = shell.replace("__DOCS_JSON__", json.dumps(docs, ensure_ascii=False, indent=2))
    shell = shell.replace("__TOC_JSON__", json.dumps(all_toc, ensure_ascii=False, indent=2))
    shell = shell.replace("__PAPERS_JSON__", json.dumps(papers_json, ensure_ascii=False, indent=2))

    OUT.write_text(shell, encoding="utf-8")

    print(f"Wrote {OUT} ({len(shell)} chars)")
    print(f"  docs: {len(docs)}, toc items: {len(all_toc)}, papers: {len(papers_json)}")

if __name__ == "__main__":
    import sys
    ap = argparse.ArgumentParser()
    ap.add_argument("--include-papers", action="store_true", help="include all 21 papers' literature_analysis")
    args = ap.parse_args()
    build(args.include_papers)
