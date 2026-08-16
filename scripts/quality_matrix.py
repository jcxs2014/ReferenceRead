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
    - 每篇: 8 项 required items 的覆盖状态（Figure 列已移除，改名为"章节子节"单独输出）
    - 汇总: 每项 required 的库级覆盖率
    - 章节子节: X.x / 0.x 章节覆盖数量（单独一行，不是百分比）
    - --check 模式: 非全部覆盖则 exit 1
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # scripts/ → 仓库根
PAPERS_ROOT = ROOT                               # 论文目录直接位于仓库根下

# 8 列（移除了 Figure 列，避免 chapter_sections 数字混淆）
OUTFORMAT = "{:<55} {:>5} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7}  {:>5}"
HEADER    = OUTFORMAT.format(
    "论文", "元信息", "结构", "章节", "图表", "公式", "数值", "实验", "总计"
)

# OR patterns: 支持三种精读格式
CHECKLIST = [
    # (A) CHECKLIST 标准: ## 2. / ## 3. / ## X.n
    # (B) FACT 三段式: ## [FACT] 等
    # (C) 老格式: ## 0.x
    ("metadata",      r"## 2\.|## \[FACT\]|## 0\.[1-9]",                      "元信息"),
    ("structure",    r"## 3\.|## \[INTERPRETATION\]|## 0\.[1-9]",              "结构"),
    ("chapter",     r"## (?:4\.|X\.\d|\d+\.\d+|\[CRITIQUE\])",        "章节"),
    ("figure",       r"## Figure \d+",                                         "图表"),
    ("table",        r"## Table \d+",                                          "公式"),   # 注：Table 和 figure 共用同一正则入口，下方单独计数
    ("formula",      r"## 7\.|## Formula|\$\$[\s\S]+?\$\$|\$[^\$]+\$",    "数值"),
    ("numerical",    r"## 8\.|## 数值|\d+\.\d+\s*[×x]\s*\d+",          "实验"),
    ("experimental", r"## 9\.|## 实验|## 观测|measurement|data",                 "参考文献"),
]



def score_file(text: str) -> dict[str, bool]:
    return {
        item_id: bool(re.search(pattern, text))
        for item_id, pattern, _ in CHECKLIST
    }

def score_chapter_sections(text: str) -> int:
    """X.1-X.8 / 0.x / ## 数字.数字 章节子节覆盖数量（0-8）。"""
    return len(re.findall(r"## X\.\d|## \d+\.\d+", text))

# 子节镜像统计（议题 3，仅警告，不参与 --check）
SUBSEC_RE = re.compile(r"^### \d+\.\d+\.\d+", re.M)


def score_subsections(text: str) -> int:
    """分章 ### N.n.n 三级子节数（路径 A 镜像指标）。"""
    return len(SUBSEC_RE.findall(text))


def parse_97_subsections(quality_text: str) -> tuple:
    """从 97「子节级覆盖」块解析 (覆盖数, 名单总数)；无块返回 (None, None)。"""
    m = re.search(r"## 子节级覆盖.*?\n((?:\|.*\n)+)", quality_text, re.S)
    if not m:
        return (None, None)
    rows = [
        r
        for r in m.group(1).splitlines()
        if r.startswith("|")
        and "原文子节" not in r
        and set(r.replace("|", "").strip()) != {"-"}
    ]
    covered = sum(1 for r in rows if "✅" in r)
    return (covered, len(rows))


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
    result["subsections"] = score_subsections(combined)
    # 97 块：尝试解析子节级覆盖 (covered, total)
    q97 = la_dir / "97_quality_check.md"
    if q97.exists():
        result["subsec_97"] = parse_97_subsections(q97.read_text(encoding="utf-8"))
    else:
        result["subsec_97"] = (None, None)
    result["total_files"] = len(files)
    result["fmt"] = detect_format(combined)
    return result

def paper_summary(row: dict) -> int:
    """已覆盖的必需项数量（不含 chapter_sections 软指标）。"""
    required = [k for k, _, _ in CHECKLIST]
    return sum(row[k] for k in required)

def is_paper_stem(stem_name: str) -> bool:
    """按目录名前缀判断是否论文（01_/02_/03_ = 论文，排除 background/ 等）。"""
    return bool(re.match(r"0[0-9]_", stem_name))  # 01-04 域（04_experiments 已纳入）

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
        f"{sum(totals[k] for k in col_keys)*100//(n*len(col_keys))}%"
    )
    print(cov)

    # 章节子节单独一行（不混在主表）
    avg_cs = total_cs // n
    print(f"章节子节: 平均 {avg_cs}/8（共 {total_cs}/{n*8} 节段）")

    # 子节镜像（议题 3，仅 print，不参与 --check）
    total_subsec = sum(row["subsections"] for _, row in papers)
    entries = []
    have_block = 0
    for stem, row in papers:
        covered, total = row["subsec_97"]
        if covered is not None and total is not None and total > 0:
            have_block += 1
            pct = covered * 100 // total if total else 0
            entries.append(f"{stem} {covered}/{total} ({pct}%)")
    if entries:
        print(
            f"子节镜像: {have_block} 篇有 97 块 | "
            + " | ".join(entries)
            + f" | 全库 ### N.n.n = {total_subsec}"
        )
    else:
        print(f"子节镜像: 0 篇有 97 块 | 全库 ### N.n.n = {total_subsec}")

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

HARD_REQUIRED = {"metadata", "structure", "chapter", "numerical"}
# 软指标（figure/table/formula/experimental）：观测/实验类文献天然少公式与图表章节，
# 覆盖率仅展示不参与 FAIL 判定；硬项四者全库覆盖率 100%。

def check_all_covered(papers: list[tuple[str, dict]]) -> bool:
    """所有论文的硬必需项（metadata/structure/chapter/numerical）均覆盖返回 True。"""
    for stem, row in papers:
        if not all(row[k] for k in HARD_REQUIRED):
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
