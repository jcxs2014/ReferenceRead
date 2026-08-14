#!/usr/bin/env python3
"""Generate INDEX.md from the papers/ directory structure.

Usage:
    python3 scripts/gen_index.py            # generate INDEX.md
    python3 scripts/gen_index.py --check    # check if INDEX.md is up-to-date
"""
import os
import re
import sys
import argparse
from datetime import datetime
from pathlib import Path
from collections import OrderedDict

BASE = Path("/Users/jcxs2014/Sites/HermesLocal/papers")

# Topic domain definitions (in display order)
TOPICS = [
    ("01_cosmic-ray-propagation", "01. 宇宙线传播"),
    ("02_cosmic-ray-origins", "02. 宇宙线起源"),
    ("03_stellar-nucleosynthesis", "03. 恒星核合成与元素丰度"),
]

# Author / journal / etc. extracted from each paper's 00_overview.md
# Falls back to directory name + file count if overview is missing fields.

def _fmt_title(t: str) -> str:
    """Title Case 清洗：全大写或全小写标题转为标题大小写。"""
    t = t.strip()
    if not t or t != t.upper() and t != t.lower():
        return t  # 混合大小写不处理
    # 全大写/全小写时做 Title Case（保留罗马数字等大写）
    import re as _re
    return _re.sub(r"\b([a-z])([a-z]*)\b", lambda m: m.group(1).upper() + m.group(2), t.lower())


def extract_meta(overview: Path):
    """Parse a few standard fields from 00_overview.md front-matter table."""
    meta = {"authors": "", "journal": "", "title": ""}
    if not overview.exists():
        return meta
    text = overview.read_text(encoding="utf-8", errors="ignore")
    for key in meta:
        # match "| **Key** | value |" (case-insensitive, allow markdown bold variants)
        m = re.search(rf"\|\s*\**\s*{re.escape(key)}\s*\**\s*\|\s*([^|]+?)\s*\|",
                      text, re.IGNORECASE)
        if m:
            meta[key] = m.group(1).strip().rstrip("|").strip().strip("*").strip("'").strip('"').strip()
    # bullet format fallback: "- **Key**: value"
    # 必须 IGNORECASE: frontmatter 的 "title:" 小写也命中（覆盖"Title:" 等变体）
    if not meta["authors"]:
        m = re.search(r"\*?\*?Authors?\*?\*?\s*[:：]\s*([^\n]+)", text, re.IGNORECASE)
        if m:
            # 捕获值剥首尾 ** 和 YAML 引号（防"**Title:** value"或 `title: '...: ...'`）
            meta["authors"] = m.group(1).strip().strip("*").strip("'").strip('"').strip()
    if not meta["title"]:  # title 同样有 bullet fallback（之前缺）
        m = re.search(r"\*?\*?Title?\*?\*?\s*[:：]\s*([^\n]+)", text, re.IGNORECASE)
        if m:
            meta["title"] = m.group(1).strip().strip("*").strip("'").strip('"').strip()
    # title 全大写/全小写时做 Title Case
    if meta["title"]:
        meta["title"] = _fmt_title(meta["title"])
    return meta


def collect_papers():
    """Walk each topic directory and collect (dirname, paper_path) entries."""
    papers = OrderedDict()
    for topic, _label in TOPICS:
        topic_path = BASE / topic
        if not topic_path.is_dir():
            continue
        papers[topic] = []
        for d in sorted(topic_path.iterdir()):
            if not d.is_dir() or not d.name[0].isdigit():
                continue
            lit = d / "literature_analysis"
            if not lit.is_dir():
                continue
            overview = lit / "00_overview.md"
            summary = lit / "99_final_summary.md"
            files = sorted([f.name for f in lit.glob("*.md")])
            meta = extract_meta(overview)
            papers[topic].append({
                "dir": d.name,
                "path": d,
                "lit": lit,
                "overview": overview,
                "summary": summary,
                "files": files,
                "meta": meta,
            })
    return papers


def fmt_paper_entry(p):
    """Format one paper section as markdown."""
    files_n = len(p["files"])
    files_links = "、".join(f for f in p["files"][:5])
    if len(p["files"]) > 5:
        files_links += f"、…等 {files_n} 个"

    title = p["meta"].get("title", "(标题未提取)")
    authors = p["meta"].get("authors", "(作者未提取)")
    journal = p["meta"].get("journal", "(期刊未提取)")

    lines = []
    lines.append(f"### `{p['dir']}`")
    lines.append("")
    lines.append(f"**{title}**")
    lines.append("")
    lines.append("|  |  |")
    lines.append("|---|---|")
    lines.append(f"| 作者 | {authors} |")
    lines.append(f"| 期刊 | {journal} |")
    lines.append(f"| 分析文件 | {files_n} 个（{files_links}） |")
    lit_rel = p['lit'].relative_to(BASE)
    lines.append(f"| 目录 | [`{lit_rel}/`]({lit_rel}/) |")
    lines.append(f"| 概览 | [`00_overview.md`]({lit_rel}/00_overview.md) |")
    if p["summary"].exists():
        lines.append(f"| 总结 | [`99_final_summary.md`]({lit_rel}/99_final_summary.md) |")
    lines.append("")
    return "\n".join(lines)


def render(papers):
    total_papers = sum(len(v) for v in papers.values())
    total_files = sum(len(p["files"]) for v in papers.values() for p in v)

    out = []
    out.append("# Papers Index — 文献索引")
    out.append("")
    out.append(f"> 共 **{total_papers} 篇文献**、**{total_files} 个分析文件**。按主题分类，点击链接进入分析文档。")
    out.append("")
    out.append("> 每篇分析的入口：`00_overview.md`（文献信息+结构树）→ 正文分章文件 → `98_vocabulary.md`（词汇表）→ `99_final_summary.md`（总结）")
    out.append("")
    out.append("---")
    out.append("")

    for topic, label in TOPICS:
        if topic not in papers or not papers[topic]:
            continue
        out.append(f"## {label}")
        out.append("")
        for p in papers[topic]:
            out.append(fmt_paper_entry(p))
        out.append("---")
        out.append("")

    out.append("## 统计")
    out.append("")
    out.append("| 分类 | 篇数 | 分析文件 |")
    out.append("|---|---|---|")
    for topic, label in TOPICS:
        if topic not in papers:
            continue
        n_papers = len(papers[topic])
        n_files = sum(len(p["files"]) for p in papers[topic])
        out.append(f"| {label} | {n_papers} | {n_files} |")
    out.append(f"| **合计** | **{total_papers}** | **{total_files}** |")
    out.append("")
    out.append(f"> 最后更新: {datetime.now().strftime('%Y-%m-%d')}（自动生成）")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if INDEX.md is out of date")
    args = ap.parse_args()

    papers = collect_papers()
    rendered = render(papers)

    index_path = BASE / "INDEX.md"
    if args.check:
        if index_path.exists() and index_path.read_text(encoding="utf-8") == rendered:
            print("INDEX.md is up-to-date.")
            return 0
        print("INDEX.md is OUT OF DATE. Run without --check to update.")
        return 1

    index_path.write_text(rendered, encoding="utf-8")
    total_papers = sum(len(v) for v in papers.values())
    total_files = sum(len(p["files"]) for v in papers.values() for p in v)
    print(f"Wrote INDEX.md: {total_papers} papers, {total_files} files")


if __name__ == "__main__":
    sys.exit(main())
