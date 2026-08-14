#!/usr/bin/env python3
"""
quality_matrix.py — 扫描 38 篇论文的 literature_analysis 目录，
生成「READING_INSTRUCTIONS 章节覆盖率矩阵」。

支持三种精读格式（OR 正则匹配）：
  (A) CHECKLIST 标准格式: ## 2. / ## 3. / ## X.n
  (B) FACT 三段式: ## [FACT] / ## [INTERPRETATION] / ## [CRITIQUE]
  (C) 老论文格式: ## 0.x

用法:
    python3 scripts/quality_matrix.py [--check] [--verbose]

输出:
    - 每篇: 8 项 required items 的覆盖状态
    - 汇总: 每项 required 的库级覆盖率
    - --check 模式: 非全部覆盖则 exit 1
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # scripts/ → 仓库根
PAPERS_ROOT = ROOT                               # 论文目录直接位于仓库根下

OUTFORMAT = "{:<55} {:>5} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7}  {:>5}"
HEADER    = OUTFORMAT.format(
    "论文", "元信息", "结构", "章节", "图表", "公式", "数值", "实验", "Figure", "Table", "总计"
)

# OR patterns: 支持三种精读格式
CHECKLIST = [
    # (A) CHECKLIST 标准: ## 2. / ## 3. / ## X.n
    # (B) FACT 三段式: ## [FACT] 等
    # (C) 老格式: ## 0.x
    ("metadata",      r"## 2\.|## \[FACT\]|## 0\.[1-9]",                      "元信息"),
    ("structure",    r"## 3\.|## \[INTERPRETATION\]|## 0\.[1-9]",              "结构"),
    ("chapter",     r"## (?:4\.|X\.\d|\d+\.\d+|\[CRITIQUE\])",        "章节(4/X.n)"),
    ("figure",       r"## Figure \d+",                                        "Figure"),
    ("table",        r"## Table \d+",                                          "Table"),
    ("formula",      r"## 7\.|## Formula|\$\$[\s\S]+?\$\$|\$[^\$]+\$",    "公式"),
    ("numerical",    r"## 8\.|## 数值|\d+\.\d+\s*[×x]\s*\d+",          "数值信息"),
    ("experimental", r"## 9\.|## 实验|## 观测|measurement|data",                 "实验/数据"),
]

def score_file(text: str) -> dict[str, bool]:
    return {
        item_id: bool(re.search(pattern, text))
        for item_id, pattern, _ in CHECKLIST
    }

def score_chapter_sections(text: str) -> int:
    """X.1-X.8 / 0.x 章节子节覆盖数量（0-8）。"""
    return len(re.findall(r"## X\.\d|## \d+\.\d+", text))

def detect_format(text: str) -> str:
    """检测论文使用哪种精读格式。"""
    if re.search(r"## \[FACT\]|## \[INTERPRETATION\]|## \[CRITIQUE\]", text):
        return "FACT"
    if re.search(r"## 0\.[1-9]", text):
        return "老格式"
    if re.search(r"## 2\.|## 3\.|## 4\.", text):
        return "CHECKLIST"
    return "unknown"

def scan_paper(paper_dir: Path) -> dict:
    """返回 {item_id: bool, chapter_sections: int}。"""
    la_dir = paper_dir / "literature_analysis"
    files = sorted(la_dir.glob("*.md")) if la_dir.exists() else []

    combined = "\n".join(f.read_text(encoding="utf-8") for f in files)
    result = score_file(combined)
    result["chapter_sections"] = score_chapter_sections(combined)
    result["total_files"] = len(files)
    result["fmt"] = detect_format(combined)
    return result

def paper_summary(row: dict) -> int:
    """已覆盖的必需项数量（不含 chapter_sections 软指标）。"""
    required = [k for k, _, _ in CHECKLIST]
    return sum(row[k] for k in required)

def is_paper_stem(stem_name: str) -> bool:
    """按目录名前缀判断是否论文（01_/02_/03_ = 论文，排除 background/ 等）。"""
    return bool(re.match(r"0[123]_", stem_name))

def find_all_papers() -> list[Path]:
    """递归找出所有 literature_analysis/00_overview.md 所在目录（论文根）。"""
    return list(PAPERS_ROOT.rglob("literature_analysis/00_overview.md"))

def build_matrix() -> list[tuple[str, dict]]:
    """返回 [(stem, result_dict)] 列表。"""
    papers = []
    for overview_path in sorted(find_all_papers()):
        paper_root = overview_path.parent.parent  # literature_analysis/ → 论文根
        if not is_paper_stem(paper_root.parent.name):  # paper_root.parent = category dir (01_/02_/03_)
            continue
        result = scan_paper(paper_root)
        papers.append((paper_root.name, result))
    return papers

def print_matrix(papers: list[tuple[str, dict]], verbose: bool = False) -> None:
    print()
    print(HEADER)
    print("-" * len(HEADER))

    col_keys = [k for k, _, _ in CHECKLIST]
    totals: dict[str, int] = {k: 0 for k, _, _ in CHECKLIST}
    total_cs = 0

    for stem, row in papers:
        cols = [("✓" if row[k] else "○") for k in col_keys]
        cs = row["chapter_sections"]
        cols.append(f"{cs}/8" if cs > 0 else "○")
        total = paper_summary(row)
        line = OUTFORMAT.format(stem, *cols, f"{total}/{len(col_keys)}")
        print(line)

        for k in col_keys:
            totals[k] += int(row[k])
        total_cs += row["chapter_sections"]

    print("-" * len(HEADER))
    n = len(papers)
    cov = OUTFORMAT.format(
        f"覆盖率 ({n} 篇)",
        *[f"{totals[k]*100//n}%" for k in col_keys],
        f"{total_cs*100//(n*8)}%",
        f"{sum(totals[k] for k in col_keys)*100//(n*len(col_keys))}%"
    )
    print(cov)

    if verbose:
        print()
        for item_id, _, label in CHECKLIST:
            missing = [s for s, r in papers if not r[item_id]]
            if missing:
                print(f"  ⚠ {label}: {len(missing)} 篇缺失 — {', '.join(missing[:3])}{' ...' if len(missing)>3 else ''}")

        # 按格式分组统计
        formats: dict[str, int] = {}
        for _, row in papers:
            fmt = row.get("fmt", "unknown")
            formats[fmt] = formats.get(fmt, 0) + 1
        print(f"  格式分布: {formats}")

def check_all_covered(papers: list[tuple[str, dict]]) -> bool:
    """所有论文的所有必需项均覆盖返回 True（exit 0），否则 False（exit 1）。"""
    col_keys = [k for k, _, _ in CHECKLIST]
    for stem, row in papers:
        if not all(row[k] for k in col_keys):
            return False
    return True

def main() -> int:
    check_mode = "--check" in sys.argv
    verbose = "--verbose" in sys.argv

    papers = build_matrix()
    print_matrix(papers, verbose=verbose)

    if check_mode:
        if check_all_covered(papers):
            print("\n[PASS] 所有论文元信息、结构、图表、公式、数值、实验 section 全部覆盖 ✅")
            return 0
        else:
            print("\n[FAIL] 部分论文缺少必需 section，覆盖率未达 100% ❌")
            return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
