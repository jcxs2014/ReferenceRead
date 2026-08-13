#!/usr/bin/env python3
"""Extract B-class terminology from all 21 98_vocabulary.md files and merge into a unified glossary."""
import re
from pathlib import Path
from collections import OrderedDict

BASE = Path("/Users/jcxs2014/Sites/HermesLocal/papers")
OUT = BASE / "background" / "05_glossary.md"


def parse_98_vocabulary(md: Path):
    """Return list of (term, definition, section_ref) tuples from the B section."""
    text = md.read_text(encoding="utf-8", errors="ignore")

    # Locate ## B section (or similar)
    b_start = re.search(r"^## \s*B\.", text, re.MULTILINE)
    if not b_start:
        # Try alt headings
        b_start = re.search(r"^## \s*B\b", text, re.MULTILINE)
    if not b_start:
        return []

    # Find end: next ## C or end of file
    b_end = re.search(r"^## \s*C\.", text[b_start.end():], re.MULTILINE)
    section = text[b_start.end():b_start.end() + (b_end.start() if b_end else len(text))]

    # Try to parse table rows: | term | def | section |
    rows = re.findall(r"\|(.+?)\|(.+?)\|(.+?)\|", section)
    if rows:
        result = []
        for r in rows:
            term = r[0].strip().strip("*`_").strip()
            defn = r[1].strip().strip("*`_").strip()
            sect = r[2].strip().strip("*`_").strip() if len(r) > 2 else ""
            if not term or term.startswith("---"):
                continue
            result.append((term, defn, sect))
        return result

    # Fallback: bullet lists - term: def
    bullets = re.findall(r"[-*]\s*\*?\*?\s*([^\*]+?)\*?\*?\s*[-–—:：]\s*(.+)", section)
    return [(t.strip(), d.strip(), "") for t, d in bullets]


def main():
    glossary = OrderedDict()  # term -> [(paper, def, sect)]
    total_entries = 0

    for md in sorted(BASE.rglob("98_vocabulary.md")):
        if "/.git/" in str(md):
            continue
        paper_dir = md.parent.parent.name  # e.g., "0001_b2fh-1957"
        rows = parse_98_vocabulary(md)
        for term, defn, sect in rows:
            if term in glossary:
                glossary[term].append((paper_dir, defn, sect))
            else:
                glossary[term] = [(paper_dir, defn, sect)]
            total_entries += 1

    # Count terms appearing in multiple papers
    multi = [(t, entries) for t, entries in glossary.items() if len(entries) > 1]
    single = [(t, entries) for t, entries in glossary.items() if len(entries) == 1]
    multi.sort(key=lambda x: -len(x[1]))

    lines = [
        "# 05. 全库术语表 (Glossary)",
        "",
        f"> 从 21 篇 `98_vocabulary.md` 的 B 类术语提取汇总。",
        f"> 去重前：{total_entries} 条引用；去重后：{len(glossary)} 个独立术语。",
        f"> 跨篇复用：{len(multi)} 个术语在多篇论文中独立出现。",
        "",
        "---",
        "",
        "## 1. 跨篇复用术语（多论文中出现）",
        "",
        "| 术语 | 出现论文 | 释义合并 |",
        "|---|---|---|",
    ]

    for term, entries in multi:
        papers = "; ".join(e[0] for e in entries[:5])
        if len(entries) > 5:
            papers += f" 等 {len(entries)} 篇"
        # Merge definitions: pick the longest
        defs = sorted({e[1] for e in entries if e[1]}, key=len, reverse=True)
        def_merged = defs[0] if defs else ""
        lines.append(f"| `{term}` | {papers} | {def_merged} |")

    lines += [
        "",
        "---",
        "",
        "## 2. 单篇术语（按首字母分组）",
        "",
        "| 术语 | 论文来源 | 释义 |",
        "|---|---|---|",
    ]

    # Group by first letter
    by_letter = OrderedDict()
    for term, entries in sorted(single):
        first = term[0].upper() if term else "?"
        by_letter.setdefault(first, []).append((term, entries))

    for letter, group in sorted(by_letter.items()):
        lines.append(f"### {letter}")
        lines.append("")
        for term, entries in group:
            paper = entries[0][0]
            defn = entries[0][1]
            lines.append(f"| `{term}` | {paper} | {defn} |")
        lines.append("")

    # Section counts
    lines += [
        "---",
        "",
        "## 3. 术语密度统计",
        "",
        "| 论文 | B 类术语数 |",
        "|---|---|",
    ]

    # Count per paper (from glossary reverse)
    per_paper = {}
    for term, entries in glossary.items():
        for e in entries:
            per_paper[e[0]] = per_paper.get(e[0], 0) + 1

    for paper, n in sorted(per_paper.items()):
        lines.append(f"| {paper} | {n} |")

    lines += [
        "",
        f"*（由 `scripts/gen_glossary.py` 自动生成）*",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}: {len(glossary)} terms, {len(multi)} cross-paper, {total_entries} raw entries")


if __name__ == "__main__":
    main()
