#!/usr/bin/env python3
"""build_citations.py — 从各篇 00_overview.md 的「篇间导航」小节提取库内引用。

语义（附 19 重定义）：
    citations = 本篇引用了库内其他论文中的哪些（库内引用），而非参考文献列表。

数据源：各篇 00_overview.md 末尾「## 篇间导航」小节的
    [`0004_blasi-2013`](../../../02_cosmic-ray-origins/0004_blasi-2013/...) 链接。

流程：
    1. 遍历 21 篇 overview，提取导航小节全部库内 stem
    2. 写入各篇 frontmatter 的 citations 字段（幂等：只替换 citations 键）
    3. 调用 build_registry.py 重建 registry（citations 进入 registry）

用法：
    python3 webapp/build_citations.py [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT_DIRS = ["01_cosmic-ray-propagation", "02_cosmic-ray-origins", "03_stellar-nucleosynthesis"]

# 从「篇间导航」小节提取 [`stem`](相对路径) 链接
NAV_LINK_RE = re.compile(r"\[`([0-9]{4}_[a-z0-9\-]+)`\]", re.IGNORECASE)


def parse_frontmatter(text: str) -> dict:
    """极简 frontmatter 解析（仅读键值）。"""
    fm = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return fm
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def collect_nav_stems(overview_text: str) -> list[str]:
    """从 overview 文本（含 frontmatter）提取篇间导航小节的库内 stem，保持出现顺序。"""
    body = overview_text
    parts = overview_text.split("---", 2)
    if len(parts) >= 3:
        body = parts[2]
    # 导航小节：从 ## 篇间导航 到文件结尾（或下一个 ##，但导航一般在末尾）
    m = re.search(r"##\s*篇间导航(.*)$", body, re.S)
    if not m:
        return []
    section = m.group(1)
    stems = []
    seen = set()
    for link in NAV_LINK_RE.findall(section):
        s = link.lower()
        if s not in seen:
            seen.add(s)
            stems.append(s)
    return stems


def update_citations_in_frontmatter(overview_path: Path, new_citations: list[str]) -> bool:
    """替换 frontmatter 里的 citations（YAML block 或 inline），返回是否改动。"""
    text = overview_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        print(f"[WARN] {overview_path.name} — 无 frontmatter，跳过", file=sys.stderr)
        return False
    # frontmatter 起止
    end = None
    for i in range(1, min(len(lines), 2000)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        print(f"[WARN] {overview_path.name} — frontmatter 未闭合", file=sys.stderr)
        return False

    new_block = "citations: " + json.dumps(new_citations, ensure_ascii=False)
    # 找到旧 citations 行区间（支持 inline 或多行 block）
    cit_start = cit_end = None
    for i in range(1, end):
        if lines[i].strip().startswith("citations:"):
            cit_start = i
            cit_end = i + 1
            # 多行 block 形式：- item 缩进行
            while cit_end < end and (lines[cit_end].strip().startswith("- ") or
                                     lines[cit_end].strip() == "-"):
                cit_end += 1
            break
    if cit_start is None:
        # 没有 citations：在 --- 前插入
        new_lines = lines[:end] + [new_block] + lines[end:]
    else:
        new_lines = lines[:cit_start] + [new_block] + lines[cit_end:]

    out = "\n".join(new_lines)
    if out == text:
        return False
    overview_path.write_text(out, encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="只统计不写入")
    args = ap.parse_args()

    total_edges = 0
    changed = 0
    for cat in CAT_DIRS:
        cat_path = ROOT / cat
        if not cat_path.exists():
            continue
        for d in sorted(cat_path.iterdir()):
            if not d.is_dir():
                continue
            overview = d / "literature_analysis" / "00_overview.md"
            if not overview.exists():
                continue
            stems = collect_nav_stems(overview.read_text(encoding="utf-8"))
            total_edges += len(stems)
            if args.dry_run:
                print(f"[DRY] {d.name}: {len(stems)} 条 citations — {stems}")
            else:
                if update_citations_in_frontmatter(overview, stems):
                    changed += 1
                    print(f"[OK]  {d.name}: {len(stems)} 条 → frontmatter")

    if args.dry_run:
        print(f"\n[dry] 总计 {total_edges} 条库内引用（21 篇提取完成）")
        return 0

    print(f"\n[OK] 更新 {changed} 篇 frontmatter，共 {total_edges} 条库内引用")
    if changed:
        # 重建 registry（citations 进 registry）
        import subprocess
        r = subprocess.run(
            [sys.executable, str(ROOT / "webapp" / "build_registry.py")],
            cwd=ROOT, capture_output=True, text=True, timeout=120)
        if r.returncode != 0:
            print(r.stderr[-500:], file=sys.stderr)
            return r.returncode
        print("[OK] registry 已重建")
    return 0


if __name__ == "__main__":
    sys.exit(main())