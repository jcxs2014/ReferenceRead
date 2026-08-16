#!/usr/bin/env python3
"""build_registry.py — 读 55 个 frontmatter，生成 registry.json。

遍历：
  - 4 个分类目录下所有 NNNN_*/literature_analysis/00_overview.md（55 篇）
  - background/*.md（7 篇，排除 README.md 与 00_home.md）

对每条：
  1. 解析 YAML frontmatter
  2. 统计 quality = literature_analysis/*.md 文件数（排除 overview / vocabulary / summary）
  3. 从 background/00_key_values.md 按标题匹配提取 key_values（仅限 overview 类条目）
输出 registry.json，用 python3 -m json.tool 验证。

仅用 Python 3.11 stdlib + PyYAML。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
KEY_VALUES_FILE = ROOT / "background" / "00_key_values.md"

CATEGORY_MAP = {
    "01_cosmic-ray-propagation": "宇宙线传播",
    "02_cosmic-ray-origins": "宇宙线起源",
    "03_stellar-nucleosynthesis": "恒星核合成",
    "04_experiments": "实验与观测",
}

# background 中需要生成 registry 条目的文件（7 篇；不含 README.md 与 00_home.md）
BACKGROUND_FILES = {
    "00_key_values.md",
    "01_cosmic_rays.md",
    "02_nucleosynthesis.md",
    "03_astrophysics.md",
    "04_critique_index.md",
    "05_glossary.md",
    "06_controversy_evolution.md",
}


# ---------------------------------------------------------------------------
# YAML frontmatter 提取
# ---------------------------------------------------------------------------

def parse_frontmatter(path: Path):
    """返回 (fm_dict | None, body_str)。失败时 (None, None)。"""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[ERR] {path} — read: {e}", file=sys.stderr)
        return None, None
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, None
    end = None
    for i in range(1, min(len(lines), 1000)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, None
    try:
        fm = yaml.safe_load("\n".join(lines[1:end])) or {}
    except Exception as e:
        print(f"[ERR] {path} — yaml parse: {e}", file=sys.stderr)
        return None, None
    body = "\n".join(lines[end + 1 :]).lstrip("\n")
    return fm, body


# ---------------------------------------------------------------------------
# quality 统计
# ---------------------------------------------------------------------------

def count_quality(overview_path: Path) -> int:
    la_dir = overview_path.parent
    if not la_dir.exists():
        return 0
    count = 0
    for f in la_dir.iterdir():
        if not f.is_file() or not f.suffix == ".md":
            continue
        name = f.name
        # 排除 overview / vocabulary / summary
        if any(k in name for k in ("overview", "vocabulary", "summary")):
            continue
        count += 1
    return count


# ---------------------------------------------------------------------------
# key_values 提取（从 background/00_key_values.md）
# ---------------------------------------------------------------------------

# 各 overview 的 ### 1.x 小节标题（子标题里常带作者/年份） → 对应的 overview 目录名
def build_kv_by_section_index(text: str) -> dict[str, list[dict]]:
    """把 00_key_values.md 按 ### N.x 小节索引，返回 {小节标题: [行字典]}。"""
    sections: dict[str, list[dict]] = {}
    current = None
    for line in text.splitlines():
        m = re.match(r"^###\s+[\d.]+\s+(.+)$", line)
        if m:
            current = m.group(1).strip()
            sections[current] = []
            continue
        if current and line.startswith("|") and "|" in line[1:]:
            # 解析 markdown 表格行
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            # 分隔行跳过
            if len(cells) >= 4 and not re.match(r"^[\s:|:-]+$", line.strip()):
                section = sections.setdefault(current, [])
                # 只收集数值行（物理量、数值、来源、章节）
                if len(cells) >= 4:
                    section.append({
                        "quantity": cells[0],
                        "value": cells[1] if len(cells) > 1 else "",
                        "uncertainty": cells[2] if len(cells) > 2 else "",
                        "source": cells[3] if len(cells) > 3 else "",
                        "section": cells[4] if len(cells) > 4 else "",
                    })
    return sections


def match_kv_for_paper(kv_index: dict[str, list[dict]], path: Path) -> list[dict]:
    """按 overview 路径 / 文件 stem 匹配对应的小节，返回合并后的 key_values。"""
    rel = path.relative_to(ROOT).as_posix()
    parent_dir = path.parent.parent.name  # 0001_b2fh-1957
    # 从 parent_dir 提取作者/年份/关键词
    tokens = set(parent_dir.replace("-", " ").replace("_", " ").split())
    tokens.add(parent_dir)

    matched: list[dict] = []
    for section_title, rows in kv_index.items():
        # 在 section title 中查找是否有 tokens 里任一（长度 >= 3 才匹配，避免噪声）
        score = 0
        for t in tokens:
            if len(t) >= 3 and t.lower() in section_title.lower():
                score += 1
        # 也允许年份匹配
        for t in tokens:
            if re.fullmatch(r"\d{4}", t) and t in section_title:
                score += 2
        if score >= 1:
            matched.extend(rows)

    # 截到前 8 条
    return matched[:8]


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def _strip_citation(v):
    """从 Obsidian wikilink 提取论文 stem。

    V2.2 目标形态二种：
        [[0004_blasi-2013]]                                          （短格式）
        [[02_cosmic-ray-origins/0004_.../literature_analysis/00_overview|0004_blasi-2013]]
    后者路径倒数第 3 段（论文目录名）即 stem。
    """
    s = str(v).strip()
    if s.startswith("[[") and s.endswith("]]"):
        s = s[2:-2]
    target = s.split("|")[0].strip()
    parts = target.split("/")
    if len(parts) >= 3 and "literature_analysis" in parts:
        return parts[-3]
    return target


def main() -> None:
    ap = argparse.ArgumentParser(description="Build registry.json from frontmatter.")
    ap.add_argument("--dry-run", action="store_true", help="只打印，不写入")
    args = ap.parse_args()

    entries: list[dict] = []

    # 1) overview 文件（21 篇）
    overview_files: list[Path] = []
    for prefix in CATEGORY_MAP:
        d = ROOT / prefix
        if not d.exists():
            print(f"[WARN] dir not found: {d}", file=sys.stderr)
            continue
        overview_files.extend(sorted(d.rglob("00_overview.md")))
    overview_files = sorted(set(overview_files))

    # 加载 key_values
    kv_index: dict[str, list[dict]] = {}
    if KEY_VALUES_FILE.exists():
        try:
            kv_index = build_kv_by_section_index(KEY_VALUES_FILE.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[WARN] key_values load failed: {e}", file=sys.stderr)

    for p in overview_files:
        fm, _ = parse_frontmatter(p)
        if fm is None:
            print(f"[WARN] {p.relative_to(ROOT)} — 无 frontmatter", file=sys.stderr)
            continue
        fm = dict(fm)
        fm["path"] = str(p.relative_to(ROOT))
        fm["quality"] = count_quality(p)
        fm["key_values"] = match_kv_for_paper(kv_index, p)
        if isinstance(fm.get("citations"), list):  # V2.2: strip wikilink
            fm["citations"] = [_strip_citation(c) for c in fm["citations"]]
        entries.append(fm)

    # 2) background 文件
    bg_dir = ROOT / "background"
    if bg_dir.exists():
        for name in sorted(BACKGROUND_FILES):
            p = bg_dir / name
            if not p.exists():
                continue
            fm, _ = parse_frontmatter(p)
            if fm is None:
                # 若没有 frontmatter 也保留骨架（背景文件应已由 build_fm.py 写入）
                fm = {}
            fm = dict(fm)
            fm["path"] = str(p.relative_to(ROOT))
            fm["quality"] = None  # 背景文件无 lit_analysis 计数
            fm["key_values"] = (
                list(kv_index.values())[0] if name == "00_key_values.md" else []
            )
            entries.append(fm)

    # 输出
    out_path = ROOT / "webapp" / "registry.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        print(f"[DRY] 共收集 {len(entries)} 条")
        for e in entries:
            print(f"  - {e.get('path','?')}: title={e.get('title','?')}  quality={e.get('quality')}  kv={len(e.get('key_values',[]))}")
        print(f"[DRY] 将写入 {out_path}")
    else:
        # 序列化前：所有字段转 str（防 year 是 int 时 .strip() 报错）
        safe = []
        for e in entries:
            e2 = dict(e)
            if isinstance(e2.get("year"), int):
                e2["year"] = str(e2["year"])
            safe.append(e2)
        out_path.write_text(
            json.dumps(safe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"[OK] 已写入 {out_path}，共 {len(entries)} 条")

    # 输出 JSON 到 stdout（供 python3 -m json.tool 验证）
    print("\n=== JSON (stdout) ===")
    print(json.dumps(entries, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
