#!/usr/bin/env python3
"""update_counts.py — 用 _meta.py 里的全局篇数/文件数更新 background/ 静态文案。

用法:
    python3 scripts/update_counts.py        # dry-run（只打印 diff）
    python3 scripts/update_counts.py --write  # 实际写入
"""
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent  # scripts/ → 仓库根
META = BASE / "scripts" / "_meta.py"

def load_meta():
    ns = {"PAPER_COUNT": None, "FILE_COUNT": None, "TOPIC_COUNTS": {}}
    if not META.exists():
        print(f"[WARN] {META} not found — run gen_index.py first")
        return ns
    # Minimal eval guard: only allow literals
    code = META.read_text(encoding="utf-8")
    allowed = {"True": True, "False": False, "None": None}
    for line in code.splitlines():
        if line.startswith("PAPER_COUNT"):
            ns["PAPER_COUNT"] = int(line.split("=")[1].strip())
        elif line.startswith("FILE_COUNT"):
            ns["FILE_COUNT"] = int(line.split("=")[1].strip())
        elif line.startswith("TOPIC_COUNTS"):
            # TOPIC_COUNTS = {...} — safe literal eval
            expr = line.split("=", 1)[1].strip()
            try:
                ns["TOPIC_COUNTS"] = eval(expr, {"__builtins__": {}}, allowed)
            except Exception as e:
                print(f"[WARN] TOPIC_COUNTS parse failed: {e}")
    return ns

# (file_pattern, find_pattern, replacement_fn) — fn gets (match_obj, meta) → replacement
REPLACEMENTS = [
    # background/00_home.md — main summary line
    (
        "background/00_home.md",
        r"本知识库涵盖 \*\*宇宙线传播与起源\*\*（\d+ 篇）、\*\*恒星核合成与丰度\*\*（\d+ 篇）、\*\*实验与观测\*\*（\d+ 篇）共 \d+ 篇学术论文",
        lambda m, meta: (
            f"本知识库涵盖 **宇宙线传播与起源**（{meta['TOPIC_COUNTS'].get('01. 宇宙线传播', (0,0))[0]} 篇）、"
            f"**恒星核合成与丰度**（{meta['TOPIC_COUNTS'].get('03. 恒星核合成与元素丰度', (0,0))[0]} 篇）、"
            f"**实验与观测**（{meta['TOPIC_COUNTS'].get('04. 实验与观测', (0,0))[0]} 篇）"
            f"共 {meta['PAPER_COUNT']} 篇学术论文"
        ),
    ),
    # background/00_home.md — key_values table row (capture whole |cell|)
    (
        "background/00_home.md",
        r"(\| \[00_key_values\.md.*?\]\]) \| \d+ 篇论文.*?\|",
        lambda m, meta: m.group(1) + f" | {meta['PAPER_COUNT']} 篇论文核心数值与公式汇总 |",
    ),
    # background/00_home.md — section heading for experiments
    (
        "background/00_home.md",
        r"论文 · 实验与观测（\d+ 篇）",
        lambda m, meta: f"论文 · 实验与观测（{meta['TOPIC_COUNTS'].get('04. 实验与观测', (0,0))[0]} 篇）",
    ),
    # background/04_critique_index.md — table + inline stats
    (
        "background/04_critique_index.md",
        r"自动从 \d+ 篇 `literature_analysis/\*\.md` 提取",
        lambda m, meta: f"自动从 {meta['PAPER_COUNT']} 篇 `literature_analysis/*.md` 提取",
    ),
    (
        "background/04_critique_index.md",
        r"已完成精读的 \d+ 篇",
        lambda m, meta: f"已完成精读的 {meta['PAPER_COUNT']} 篇",
    ),
    # background/05_glossary.md
    (
        "background/05_glossary.md",
        r"从 \d+ 篇 `98_vocabulary\.md`",
        lambda m, meta: f"从 {meta['PAPER_COUNT']} 篇 `98_vocabulary.md`",
    ),
    # background/06_controversy_evolution.md
    (
        "background/06_controversy_evolution.md",
        r"本库 \d+ 篇文献发表区间",
        lambda m, meta: f"本库 {meta['PAPER_COUNT']} 篇文献发表区间",
    ),
    (
        "background/06_controversy_evolution.md",
        r"\+ \d+ 篇文献年份结构化生成",
        lambda m, meta: f"+ {meta['PAPER_COUNT']} 篇文献年份结构化生成",
    ),
    # background/README.md — readme header
    (
        "background/README.md",
        r"基于 \d+ 篇文献精读的系统整理",
        lambda m, meta: f"基于 {meta['PAPER_COUNT']} 篇文献精读的系统整理",
    ),
    # background/README.md — table rows (全库 N 篇)
    (
        "background/README.md",
        r"全库 \d+ 篇",
        lambda m, meta: f"全库 {meta['PAPER_COUNT']} 篇",
    ),
    # background/README.md — 篇数 column in table
    (
        "background/README.md",
        r"(?<= \| )(\d+ 篇)(?= \| )",
        lambda m, meta: f"{meta['PAPER_COUNT']} 篇",
    ),
]

def process_file(path: Path, meta: dict, dry: bool = True) -> list:
    if not path.exists():
        return [f"  [SKIP] {path} — not found"]
    orig = path.read_text(encoding="utf-8")
    text = orig
    changes = []
    for entry in REPLACEMENTS:
        file_rel_pat, pattern, repl_fn = entry
        def _make_repl(m, _repl_fn=repl_fn):
            new = _repl_fn(m, meta)
            if new != m.group():
                changes.append(f"    {m.group()!r} → {new!r}")
            return new
        text, n = re.subn(pattern, _make_repl, text, count=1)
    if not changes:
        return []
    if not dry:
        path.write_text(text, encoding="utf-8")
    return changes

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="实际写入（默认 dry-run）")
    args = ap.parse_args()
    dry = not args.write

    meta = load_meta()
    print(f"Loaded: PAPER_COUNT={meta['PAPER_COUNT']}, FILE_COUNT={meta['FILE_COUNT']}")

    all_changes = {}
    for file_rel, pattern, _ in REPLACEMENTS:
        path = BASE / file_rel
        changes = process_file(path, meta, dry=dry)
        if changes:
            all_changes[file_rel] = changes

    if not all_changes:
        print("全部是最新的，无需更新。" if dry else "全部已写入。")
        return

    print(f"\n{'[DRY-RUN] — 以下将更改:' if dry else '[WRITE] — 更改:'}")
    for file_rel, changes in all_changes.items():
        print(f"  {file_rel}:")
        for c in changes:
            print(c)

    if not dry:
        print("\n已写入。")
        # Rebuild webapp so audit picks up the new static text
        print("\n请重新运行: python3 webapp/scripts/build_webapp.py --include-papers")

if __name__ == "__main__":
    sys.exit(main())
