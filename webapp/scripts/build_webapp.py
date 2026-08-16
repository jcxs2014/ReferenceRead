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

HERE = Path(__file__).resolve().parent       # webapp/scripts/
ROOT = HERE.parent.parent                     # papers/
TOOLS = HERE                                  # scripts/（md2doc_html.py 所在）
DOCROOT = ROOT / "background"
WEBAPP = HERE.parent                          # webapp/（产物/模板所在）
OUT = WEBAPP / "interactive.html"             # 构建产物
SHELL = WEBAPP / "shell.html"                 # 骨架模板
INDEX = ROOT / "INDEX.md"

PAPER_INFO = {
    "01_cosmic-ray-propagation": {"label": "宇宙线传播"},
    "02_cosmic-ray-origins":     {"label": "宇宙线起源与 UHECR"},
    "03_stellar-nucleosynthesis":{"label": "恒星核合成与丰度"},
    "04_experiments":          {"label": "实验与观测"},
}

# Load registry for enriched paper metadata (status, read_date, tags, citations)
REGISTRY_FILE = WEBAPP / "registry.json"
_registry: dict = {}
if REGISTRY_FILE.exists():
    for e in json.loads(REGISTRY_FILE.read_text(encoding="utf-8")):
        if e.get("category") == "背景知识":
            continue
        # stem is the directory name, e.g. "0001_strong-moskalenko-ptuskin-2007"
        # path like: 01_cosmic-ray-propagation/0001_.../literature_analysis/00_overview.md
        parts = e["path"].replace("/00_overview.md", "").split("/")
        stem = parts[-2] if len(parts) >= 2 else parts[-1]
        _registry[stem] = e


def _paper_reg(stem: str) -> dict:
    """Return registry entry for a paper stem, or empty dict."""
    return _registry.get(stem, {})


def _clean_author(raw) -> str:
    """Strip markdown bold, parenthetical notes, institution info, and all asterisks.
    Accepts str or list (from YAML multi-author format)."""
    if isinstance(raw, list):
        raw = ", ".join(str(x) for x in raw)
    s = str(raw).strip()
    # Remove ALL asterisk runs (markdown bold remaining on individual names)
    s = re.sub(r'\*+', '', s).strip()
    # Remove superscript ordinals (¹²³ etc.) that INDEX.md uses as author footnotes
    s = re.sub(r'[\u00b0\u00b2\u00b3\u00b9\u00ba\u2070-\u2079]', '', s).strip()
    # Remove (corresponding author) and similar notes
    s = re.sub(r'\s*\(corresponding author\)', '', s, flags=re.IGNORECASE).strip()
    # Remove institution notes in parentheses: English or Chinese (any position)
    s = re.sub(r'\s*[\uff08(][^)\uff09]*(?:University|Institute|Observatory|Laboratory|Laboratoire|College|University of|GRAPPA|蒙纳士|大学|学院|天文台)[^)\uff09]*[\uff09)]', '', s, flags=re.IGNORECASE).strip()
    # Remove any remaining trailing parenthetical notes
    s = re.sub(r'\s*[\uff08(][^)\uff09]*[\uff09)]\s*$', '', s).strip()
    return s

def _title_case(s: str) -> str:
    """Title-case a space-separated name, preserving lowercase after first letter."""
    return " ".join(w[0].upper() + w[1:].lower() if len(w) > 1 else w.upper()
                    for w in s.split())

def _fmt_authors(raw: str) -> str:
    """Compact author list: handle comma, semicolon, and Chinese separators."""
    s = _clean_author(raw)
    # Split on comma, semicolon, Chinese semicolon, or Chinese comma
    parts = [p.strip() for p in re.split(r"[;,；、]\s*", s) if p.strip()]
    if not parts:
        return raw
    # Normalize ALL-CAPS names (journal convention) to Title Case
    parts = [_title_case(p) for p in parts]
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
    entries = {}
    for block in re.split(r"(?=\n### `[^`]+`\n)", text):
        stem_m = re.search(r"`([^`]+)`", block)
        if not stem_m:
            continue
        stem = stem_m.group(1).strip()

        auth_m = re.search(r"作者\s*[|]\s*([^|\n]+)", block)
        yr_m = re.search(r"\b(19\d{2}|20\d{2})\b", block)
        yr_in_stem_m = re.search(r"(?<=[-_])(\d{4})(?=[-_]|$)", stem)

        authors = auth_m.group(1).strip() if auth_m else ""
        year = (yr_m.group(1) if yr_m else
                yr_in_stem_m.group(1) if yr_in_stem_m else "?")
        label = f"{_fmt_authors(authors)} ({year})" if authors else stem
        entries[stem] = label

    return entries


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

CITATION = _build_citation_map()
# Merge FALLBACK entries — fills in years and author corrections for stems where
# INDEX.md lacks a year or the author field has parsing issues (Anders/Grevesse, etc.)
for k, v in _FALLBACK.items():
    if k not in CITATION or "?" in CITATION[k]:
        CITATION[k] = v


def slug(s):
    s = html_mod.unescape(s).lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", s).strip("-")
    return s[:80]


def convert_doc(path: Path, doc_id: str = ""):
    tmp = path.with_suffix(".fragment.html")
    args = [sys.executable, str(TOOLS / "md2doc_html.py"), str(path), str(tmp), "--reset-anchors"]
    if doc_id:
        args.append(doc_id)
    r = subprocess.run(args, capture_output=True, text=True, cwd=str(TOOLS))
    if r.returncode != 0:
        raise RuntimeError(f"md2doc_html failed on {path}:\n{r.stderr}")
    try:
        content = tmp.read_text(encoding="utf-8")
    finally:
        # 临时 fragment 清理失败不中断构建（.gitignore 已忽略 *.fragment.html，
        # 残留可在构建后统一清理；2026-08-16 保护层曾拦截批量 unlink 致构建中断）
        try:
            tmp.unlink(missing_ok=True)
        except Exception:
            pass
    return content


def _deduplicate_headings(html_body: str, parent_id: str) -> tuple:
    """Ensure all heading ids are unique within a doc; extract TOC entries.
    md2doc resets its counter per fragment, so cross-fragment collisions (same
    bare anchor appearing in multiple fragments) are resolved here.
    Strategy: strip any existing -N suffix, re-suffix all bare anchors 1..N.
    This avoids collisions between bare anchors and md2doc's own -N suffixes."""
    heading_pattern = re.compile(r"<h([2-6])([^>]*)id=\"([^\"]+)\"([^>]*)>(.*?)</h", re.DOTALL)
    toc_entries = []

    # Pass 1: collect (bare, full_id, level, title, old_tag, tag_start, tag_end)
    matches = list(heading_pattern.finditer(html_body))
    bare_counter = {}   # bare -> count across all fragments
    items = []
    for m in matches:
        full_id = m.group(3)
        level   = int(m.group(1))
        raw     = re.sub(r"<[^>]+>", "", m.group(5)).strip()
        title   = html_mod.unescape(raw)
        # 从标题重建裸 anchor（与 md2doc_html 同规则），供跨 fragment 去重。
        # 不依赖 full_id 剥离 -N 后缀：旧逻辑 `re.sub(r'-\d+$','',full_id)` 会误剥
        # 真实数字 anchor（`### 1`→"doc"、`### $^{1}$`→"doc-1"），Pass 2 重编号时碰撞
        # （全库术语表 doc-1/doc-2 重复断言失败）；对同篇多分章同名标题（跨 fragment）
        # 也无法正确合并去重（ruszkowski 多分章 `### 1. 图的目的` 碰撞）。
        title_anchor = re.sub(r"[^\w\u4e00-\u9fff0-9-]+", "-", title).strip("-").lower()
        if not title_anchor:
            title_anchor = f"h{level}"
        prefix = full_id.split("-doc-")[0] if "-doc-" in full_id else ""
        bare   = f"{prefix}-doc-{title_anchor}" if prefix else title_anchor
        items.append({
            "bare": bare, "full_id": full_id, "level": level,
            "title": title, "old_tag": m.group(0),
            "tag_start": m.start(), "tag_end": m.end(),
        })
        bare_counter[bare] = bare_counter.get(bare, 0) + 1

    # Pass 2: assign new suffixes only for bare anchors that appear > once
    seen_count = {}
    result = []
    last_end = 0
    for it in items:
        if bare_counter[it["bare"]] > 1:
            seen_count[it["bare"]] = seen_count.get(it["bare"], 0) + 1
            new_id = f"{it['bare']}-{seen_count[it['bare']]}"
        else:
            new_id = it["bare"]
        toc_entries.append({"level": it["level"], "id": new_id, "title": it["title"],
                           "parent_id": parent_id, "parent_label": ""})
        new_tag = it["old_tag"].replace(f'id="{it["full_id"]}"', f'id="{new_id}"')
        result.append(html_body[last_end:it["tag_start"]])
        result.append(new_tag)
        last_end = it["tag_end"]

    result.append(html_body[last_end:])
    deduped = "".join(result)

    # Assert final uniqueness
    ids = [m.group(3) for m in heading_pattern.finditer(deduped)]
    assert len(ids) == len(set(ids)), \
        f"Duplicate heading ids in {parent_id}: {[h for h in ids if ids.count(h) > 1]}"

    return deduped, toc_entries


def build(include_papers=False, out=None):
    """Build the interactive HTML. `out` defaults to webapp/interactive.html."""
    if out is None:
        out = OUT
    docs        = []
    all_toc     = []
    papers_json = []

    bg_files = [
        ("00_home.md",             "知识库首页"),
        ("00_key_values.md",      "全库关键数值速查表"),
        ("01_cosmic_rays.md",     "宇宙线（传播与起源）"),
        ("02_nucleosynthesis.md", "恒星核合成"),
        ("03_astrophysics.md",    "太阳丰度与天体物理"),
        ("04_critique_index.md",  "CRITIQUE 观点汇总"),
        ("05_glossary.md",        "全库术语表"),
        ("06_controversy_evolution.md", "争议演化时间线"),
        ("07_experimental_panorama.md", "实验观测全景"),
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
        docs.append({"id": doc_id, "slug": doc_id, "title": title,
                     "category": "背景知识", "html": html, "file": fname})
        for t in tocs:
            t["parent_id"] = doc_id
            all_toc.append(t)

    # ── Paper docs ───────────────────────────────────────────────
    if include_papers:
        for cat_dir in sorted(ROOT.glob("[0-9][0-9]_*/")):
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
                reg        = _paper_reg(stem)
                raw_title  = reg.get("title", "") or CITATION.get(stem, "")
                # Strip markdown emphasis from title
                title      = re.sub(r'\*+([^*])\*+', r'\1', raw_title).strip()
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

                docs.append({"id": paper_slug, "slug": paper_slug,
                             "title": f"论文 · {title}",
                             "category": cat_label, "html": paper_html})

                for t in tocs:
                    t["parent_id"]   = paper_slug
                    t["parent_label"] = title
                    all_toc.append(t)

                stem_yr = re.match(r"\d{4}_.+?-(\d{4})", stem)
                reg     = _paper_reg(stem)
                reg_yr  = reg.get("year")
                try: reg_yr_i = int(str(reg_yr).strip())
                except (TypeError, ValueError): reg_yr_i = 0
                year    = reg_yr_i or (int(stem_yr.group(1)) if stem_yr else 0)
                papers_json.append({
                    "slug":     paper_slug,
                    "label":    _fmt_authors(reg.get("authors", "")) + f" ({year})" if reg.get("authors") else title,
                    "year":     year,
                    "stem":     stem,
                    "category": cat_label,
                    "status":   reg.get("status", "completed"),
                    "read_date": reg.get("read_date", ""),
                    "tags":     reg.get("tags", []),
                    "citations": reg.get("citations", []),
                })

    # ── Inject & write ───────────────────────────────────────────
    shell = SHELL.read_text(encoding="utf-8")
    shell = shell.replace("__DOCS_JSON__",   json.dumps(docs,        ensure_ascii=False, indent=2))
    shell = shell.replace("__TOC_JSON__",     json.dumps(all_toc,     ensure_ascii=False, indent=2))
    shell = shell.replace("__PAPERS_JSON__",  json.dumps(papers_json, ensure_ascii=False, indent=2))
    # 倒排索引（build_search_index.py → search_index.json）
    search_idx_path = WEBAPP / "search_index.json"
    if search_idx_path.exists():
        search_idx = json.loads(search_idx_path.read_text(encoding="utf-8"))
        # 只注入 index 字段（含 count/total_entries 冗余）
        shell = shell.replace(
            "__SEARCH_INDEX_JSON__",
            json.dumps(search_idx.get("index", {}), ensure_ascii=False, indent=2),
        )
    else:
        shell = shell.replace("__SEARCH_INDEX_JSON__", "{}")
    # 术语表（05_glossary.md → glossary.json，运行时 hover 用）
    gloss_path = WEBAPP / "glossary.json"
    if gloss_path.exists():
        gloss = json.loads(gloss_path.read_text(encoding="utf-8"))
    else:
        gloss = []
        print("[WARN] glossary.json 不存在 — 先跑 build_glossary.py", file=sys.stderr)
    shell = shell.replace("__GLOSS_JSON__", json.dumps(gloss, ensure_ascii=False, indent=2))
    # KaTeX 离线：替换 CDN 为本地 third-party/katex（interactive.html 在 webapp/ 根，third-party 用相对路径即可）
    shell = shell.replace("__WEBAPP_ROOT__", "")

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
