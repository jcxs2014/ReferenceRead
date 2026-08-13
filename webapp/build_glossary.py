#!/usr/bin/env python3
"""build_glossary.py — 解析 background/05_glossary.md → webapp/glossary.json。

输入格式（三列多对多表格）:
    | `术语（中文/英文）` | 0001_bhattacharjee-sigl-2000; ...; 0005_amato-2014 等 11 篇 | 中文释义 |

输出:
    [{ "term": "术语", "def": "释义", "papers": ["stem", ...], "cross_paper": true }]

仅用 Python 3.11 stdlib（含 PyYAML）。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY_FILE = ROOT / "background" / "05_glossary.md"
OUT_FILE = ROOT / "webapp" / "glossary.json"

ROW_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*$")


def parse_glossary(text: str) -> list[dict]:
    entries: list[dict] = []
    in_table = False
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("|---") or line.startswith("| ----"):
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        m = ROW_RE.match(line)
        if not m:
            continue
        term_raw, papers_raw, def_raw = m.group(1), m.group(2), m.group(3)
        # 术语：去掉反引号内多余空白，保留原始形态（可能含中文/英文/括号说明）
        term = term_raw.strip()
        if not term or term.startswith("术语") or def_raw.startswith("释义"):
            continue
        # 出现论文：`stem; stem 等 N 篇` → stem 列表
        papers: list[str] = []
        for seg in re.split(r"[;；]", papers_raw):
            seg = seg.strip()
            m_stem = re.match(r"([0-9]{4}_[A-Za-z0-9\-]+)", seg)
            if m_stem:
                papers.append(m_stem.group(1))
        # 跨篇判断：原始文本含"等 N 篇"或 ≥2 个 stem
        cross = bool(re.search(r"等\s*\d+\s*篇", papers_raw)) or len(papers) >= 2
        entries.append({
            "term": term,
            "def": def_raw.strip(),
            "papers": papers,
            "cross_paper": cross,
        })
    return entries


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="只打印统计不写文件")
    args = ap.parse_args()

    text = GLOSSARY_FILE.read_text(encoding="utf-8")
    entries = parse_glossary(text)

    # 去重（同一术语可能跨节重复）
    seen: dict[str, dict] = {}
    for e in entries:
        key = e["term"]
        if key in seen:
            prev = seen[key]
            prev["papers"] = sorted(set(prev["papers"]) | set(e["papers"]))
            prev["cross_paper"] = prev["cross_paper"] or e["cross_paper"]
            prev["def"] = prev["def"] or e["def"]
        else:
            seen[key] = e
    merged = sorted(seen.values(), key=lambda x: x["term"])

    if args.dry_run:
        cross = sum(1 for e in merged if e["cross_paper"])
        no_def = sum(1 for e in merged if not e["def"])
        no_papers = sum(1 for e in merged if not e["papers"])
        print(f"总术语: {len(merged)}（去重后）")
        print(f"  跨篇复用: {cross}")
        print(f"  缺释义: {no_def}，缺论文: {no_papers}")
        sample = [e for e in merged if e["cross_paper"]][:3]
        for e in sample:
            print(f"  · {e['term']} — {e['def'][:30]} ({len(e['papers'])} 篇)")
        return 0

    OUT_FILE.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] 已写入 {OUT_FILE}，共 {len(merged)} 条")
    return 0


if __name__ == "__main__":
    sys.exit(main())