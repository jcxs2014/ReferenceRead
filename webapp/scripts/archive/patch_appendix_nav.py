#!/usr/bin/env python3
"""patch_appendix_nav.py — 给 97_quality_check / 98_vocabulary / 99_final_summary 补导航头。

问题：97/98 是孤立节点（无「上一章/下一章」，Obsidian Graph 悬空）。
方案（每篇）：
    97_quality_check:   上一章 = 本篇最后正文文件（编号<97 中最大），下一章 = 98_vocabulary
    98_vocabulary:      上一章 = 97_quality_check，下一章 = 99_final_summary
    99_final_summary:   已有导航跳过；缺失则补 上一章 = 98_vocabulary

导航头用反引号格式（与其它章节一致，后续 apply_wikilinks.py 统一转 wikilink）。
幂等：已有 上一章/下一章 任一行的文件跳过。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
CAT_DIRS = ["01_cosmic-ray-propagation", "02_cosmic-ray-origins", "03_stellar-nucleosynthesis"]


def find_file(la: Path, prefix: str | int) -> Path | None:
    """按编号前缀找真实文件名（97 → 97_quality_check.md）。"""
    pfx = f"{prefix:02d}" if isinstance(prefix, int) else prefix
    for f in la.glob(f"{pfx}_*.md"):
        return f
    return None


def insert_nav_after_quote_block(text: str, nav_lines: list[str]) -> str:
    """把导航行插入到文件开头引用块（> 行）之后；无引用块则插在 H1 标题后。"""
    lines = text.splitlines()
    # 找引用块结束位置（连续的 > 行之后）
    idx = 0
    seen_quote = False
    for i, l in enumerate(lines):
        if l.startswith(">"):
            seen_quote = True
            idx = i + 1
        elif seen_quote:
            break  # 引用块结束
    # 无引用块：H1 标题后
    if idx == 0:
        for i, l in enumerate(lines):
            if l.startswith("# "):
                idx = i + 1
                break
    block = "\n".join(nav_lines)
    new_lines = lines[:idx] + [block, ""] + lines[idx:]
    out = "\n".join(new_lines)
    # 清理重复空行
    while "\n\n\n" in out:
        out = out.replace("\n\n\n", "\n\n")
    return out


def main() -> int:
    changed = 0
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
            # 最后正文文件
            body_nums = []
            for f in la.glob("*.md"):
                m = re.match(r"(\d{2})_", f.name)
                if m and int(m.group(1)) < 97:
                    body_nums.append(int(m.group(1)))
            last_body = max(body_nums) if body_nums else None

            # 三个附录文件
            for prefix, prev_ref, next_ref in [
                (97, last_body, 98),
                (98, 97, 99),
                (99, 98, None),
            ]:
                target = find_file(la, prefix)
                if not target:
                    continue
                text = target.read_text(encoding="utf-8")
                if "上一章" in text or "下一章" in text:
                    continue  # 已有导航（含已 wikilink 化的）

                nav_lines = []
                if prev_ref is not None:
                    pf = find_file(la, prev_ref)
                    if pf:
                        nav_lines.append(f"> 上一章：`{pf.name}`")
                if next_ref is not None:
                    nf = find_file(la, next_ref)
                    if nf:
                        nav_lines.append(f"> 下一章：`{nf.name}`")
                if not nav_lines:
                    continue
                new_text = insert_nav_after_quote_block(text, nav_lines)
                if new_text != text:
                    target.write_text(new_text, encoding="utf-8")
                    changed += 1
                    print(f"[OK] {cat}/{d.name}/{target.name}: {' / '.join(l[2:] for l in nav_lines)}")
    print(f"共补 {changed} 个文件导航头")
    return 0


if __name__ == "__main__":
    sys.exit(main())