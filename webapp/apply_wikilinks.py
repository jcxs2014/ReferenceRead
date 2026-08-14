#!/usr/bin/env python3
"""apply_wikilinks.py — V2.2 补丁：Obsidian 图谱链接化。

改动 A：分章导航头 → 完整路径 wikilink（~150 文件）
    > 上一章：`00_overview.md`
    → > 上一章：[[0001_strong-.../literature_analysis/00_overview|00_overview]]
    21 篇各有同名 00_overview.md，必须带 vault 内完整路径，短链接会歧义。

改动 B：frontmatter citations → wikilink（21 文件）
    - 0004_blasi-2013  →  - [[0004_blasi-2013]]
    stem 目录名 vault 内唯一，短链接不歧义。

幂等：已有 [[ ]] 的行/项跳过。仅改源 md，不碰 registry/webapp（由 build 层处理）。
用法：python3 webapp/apply_wikilinks.py [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT_DIRS = ["01_cosmic-ray-propagation", "02_cosmic-ray-origins", "03_stellar-nucleosynthesis"]
NAV_RE = re.compile(r"^(>\s*(?:上一章|下一章)[：:])\s*`([^`]+\.md)`\s*$")
CIT_INLINE_RE = re.compile(r"^citations:\s*\[(.*?)\]\s*$")


def nav_link_target(paper_dir: str, fname: str, cat_dir: str) -> str:
    """拼库内完整路径 wikilink（相对 vault 根 papers/，须含分类目录前缀）。

    vault 根 = ROOT（papers/），实际路径形如
        01_cosmic-ray-propagation/0001_strong-.../literature_analysis/00_overview.md
    缺分类前缀会悬空（Obsidian 按文件名解析，同名 21 篇会歧义）。
    """
    return f"{cat_dir}/{paper_dir}/literature_analysis/{fname}"


def convert_nav_line(line: str, paper_dir: str, cat_dir: str) -> str:
    m = NAV_RE.match(line)
    if not m:
        return line
    prefix, fname = m.group(1), m.group(2)
    if "[[" in line:
        return line  # 幂等：已是 wikilink
    target = nav_link_target(paper_dir, fname, cat_dir)
    return f"{prefix}[[{target}|{fname}]]"


def stem_to_cat(stem: str) -> str | None:
    """查论文 stem 所属分类目录（vault 根 = ROOT）。"""
    for cat in CAT_DIRS:
        if (ROOT / cat / stem).is_dir():
            return cat
    return None


def convert_citations_block(text: str, paper_dir: str, cat_dir: str) -> tuple[str, bool]:
    """把 frontmatter 的 citations 列表项转 wikilink（指向目标篇 overview 文件）。

    Obsidian wikilink 只认**文件**，不能链接目录名——`[[0004_blasi-2013]]`
    是目录会悬空。改为指向该篇入口文件：
        [[0004_blasi-2013/literature_analysis/00_overview|0004_blasi-2013]]
    """
    lines = text.splitlines()
    out = []
    in_cit = False
    changed = False
    for ln in lines:
        # 进入 citations 块
        if re.match(r"^citations:\s*$", ln):
            in_cit = True
            out.append(ln)
            continue
        if in_cit:
            # block 项
            m = re.match(r"^(\s*)-\s*(.+?)\s*$", ln)
            if m and not ln.strip().startswith("- [["):
                indent, val = m.group(1), m.group(2).strip().strip("'\" ")
                # 幂等：已是 wikilink（含带引号 '[[...]]' 格式）直接保留
                if val.startswith("[[") and val.endswith("]]"):
                    out.append(ln)
                    continue
                stem = val.split("|")[0]
                tgt_cat = stem_to_cat(stem) or cat_dir
                out.append(f"{indent}- [[{tgt_cat}/{stem}/literature_analysis/00_overview|{stem}]]")
                changed = True
                continue
            if m and ln.strip().startswith("- [["):
                out.append(ln)  # 已是 wikilink
                continue
            # 退出块（空行/---/新键）
            if ln.strip() == "" or ln.strip() == "---" or ":" in ln:
                in_cit = False
        # inline 形态 citations: [...] → block 形态
        m = CIT_INLINE_RE.match(ln)
        if m:
            vals = [v.strip().strip("'\" ") for v in m.group(1).split(",") if v.strip()]
            vals = [re.sub(r"^\[\[(.*)\]\]$", r"\1", v).split("|")[0] for v in vals]
            out.append("citations:")
            for v in vals:
                tgt_cat = stem_to_cat(v) or cat_dir
                out.append(f"- [[{tgt_cat}/{v}/literature_analysis/00_overview|{v}]]")
            changed = True
            continue
        out.append(ln)
    result = "\n".join(out)
    return result, changed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    nav_changed = 0
    cit_changed = 0
    repaired = 0
    for cat in CAT_DIRS:
        cat_path = ROOT / cat
        if not cat_path.exists():
            continue
        for d in sorted(cat_path.iterdir()):
            if not d.is_dir():
                continue
            la = d / "literature_analysis"
            if not la.is_dir():
                continue
            # 真实文件（按编号索引）——用于修复旧重命名遗留的陈旧引用
            actual_by_num = {}
            for f in la.glob("*.md"):
                mm = re.match(r"(\d{2})_", f.name)
                if mm:
                    actual_by_num[mm.group(1)] = f.name
            for f in sorted(la.glob("*.md")):
                text = f.read_text(encoding="utf-8")

                # 修复陈旧引用：`NN_旧名.md` → `NN_真实名.md`（编号对齐，幂等）
                def fix_ref(m):
                    num = m.group(1)
                    if num in actual_by_num and m.group(0) != f"`{actual_by_num[num]}`":
                        nonlocal repaired
                        repaired += 1
                        return f"`{actual_by_num[num]}`"
                    return m.group(0)
                text = re.sub(r"`(\d{2})_[^`]+\.md`", fix_ref, text)

                # 改动 A：导航头（正文所有行）
                new_lines = [convert_nav_line(ln, d.name, cat) for ln in text.splitlines()]
                text_new = "\n".join(new_lines)
                if text_new != text:
                    nav_changed += 1
                    text = text_new

                # 改动 B：frontmatter citations（仅 00_overview.md 有）
                if f.name == "00_overview.md":
                    text_new, chg = convert_citations_block(text, d.name, cat)
                    if chg:
                        cit_changed += 1
                        text = text_new

                if text != f.read_text(encoding="utf-8"):
                    if args.dry_run:
                        print(f"[DRY] {cat}/{d.name}/{f.name}")
                    else:
                        f.write_text(text, encoding="utf-8")

    print(f"陈旧引用修复（编号对齐）: {repaired} 处")
    print(f"导航头 wikilink 化: {nav_changed} 文件")
    print(f"citations wikilink 化: {cit_changed} 文件" + ("（dry-run）" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())