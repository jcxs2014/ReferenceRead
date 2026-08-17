#!/usr/bin/env python3
"""Generate 97_quality_check.md for each paper by mechanically counting sections, figures, tables, formulas, and [CRITIQUE] tags across all analysis files."""
import re
import sys
from pathlib import Path

BASE = Path("/Users/jcxs2014/Sites/HermesLocal/papers")


def collect_papers():
    """Return list of (rel_dir, lit_path) for each paper."""
    papers = []
    for cat in sorted(BASE.glob("0[0-9]_*")):
        if not cat.is_dir():
            continue
        for d in sorted(cat.iterdir()):
            lit = d / "literature_analysis"
            if lit.is_dir():
                rel = str(lit.relative_to(BASE))
                papers.append((rel, lit))
    return papers


def count_patterns(text: str) -> dict:
    """Count occurrences of figures, tables, formulas, and CRITIQUE tags."""
    # 公式统计（2026-08-17 修复）：精读文档用 Markdown 数学 $...$/$$...$$，
    # 旧正则只匹配 LaTeX 旧式 \[...\]/\(...\)/\tag{} → 恒为 0。
    # 现三种写法都统计：block $$...$$（可跨行）+ inline $...$（单行，
    # 排除 $$ 边界，用 (?<!\$) 与 (?!\$) 防误匹配）+ 旧式 \[...\]/\(...\)/\tag{}
    block_formulas = len(re.findall(r"\$\$[^$]+\$\$", text))
    inline_formulas = len(re.findall(r"(?<!\$)\$[^$\n]+\$(?!\$)", text))
    legacy_formulas = len(re.findall(r"\\\[.*?\\\]|\\\(.*?\\\)|\\\tag\{", text, re.DOTALL))
    return {
        "figures": len(re.findall(r"\bFigure\b", text, re.IGNORECASE)),
        "tables": len(re.findall(r"\bTable\b", text, re.IGNORECASE)),
        "formulas": block_formulas + inline_formulas + legacy_formulas,
        "block_formulas": block_formulas,
        "inline_formulas": inline_formulas,
        "critique": len(re.findall(r"\[CRITIQUE\]", text)),
        "interpretation": len(re.findall(r"\[INTERPRETATION\]", text)),
        "fact": len(re.findall(r"\[FACT\]", text)),
    }


def count_sections(text: str) -> dict:
    """Count heading levels."""
    h1 = len(re.findall(r"^# ", text, re.MULTILINE))
    h2 = len(re.findall(r"^## ", text, re.MULTILINE))
    h3 = len(re.findall(r"^### ", text, re.MULTILINE))
    return {"h1": h1, "h2": h2, "h3": h3}


def build_check(rel_dir: str, lit_path: Path) -> str:
    md_files = sorted(lit_path.glob("*.md"))
    total_text = "\n".join(f.read_text(encoding="utf-8", errors="ignore") for f in md_files)

    counts = count_patterns(total_text)
    sections = count_sections(total_text)

    has_overview = (lit_path / "00_overview.md").exists()
    has_summary = (lit_path / "99_final_summary.md").exists()
    has_vocab = (lit_path / "98_vocabulary.md").exists()
    body_files = sorted(lit_path.glob("[0-1][0-9]_*.md"))
    total_lines = sum(
        len(f.read_text(encoding="utf-8", errors="ignore").splitlines())
        for f in md_files
    )

    paper_name = lit_path.parent.name

    # Completeness score: 0-10 based on coverage signals
    score = 0
    if has_overview: score += 1
    if has_summary: score += 1
    if has_vocab: score += 1
    if len(body_files) >= 3: score += 2
    elif len(body_files) >= 1: score += 1
    if counts["figures"] + counts["tables"] >= 5: score += 2
    if counts["critique"] >= 3: score += 2
    if counts["formulas"] >= 1: score += 1

    out = [
        f"# 97. Quality Check — 完成度自查",
        f"",
        f"> 文献：`{paper_name}`",
        f"> 自动生成：统计 `literature_analysis/` 下所有 Markdown 文件。",
        f"",
        f"## 文件清单",
        f"",
        f"| 组件 | 状态 |",
        f"|---|---|",
        f"| 00_overview.md | {'✅' if has_overview else '⚠️ 缺失'} |",
        f"| 99_final_summary.md | {'✅' if has_summary else '⚠️ 缺失'} |",
        f"| 98_vocabulary.md | {'✅' if has_vocab else '⚠️ 缺失'} |",
        f"| 正文章节文件 | {len(body_files)} 个（{'✅' if len(body_files) >= 1 else '⚠️ 缺失'}） |",
        f"| **合计** | **{len(md_files)} 个分析文件，{total_lines} 行** |",
        f"",
        f"## 覆盖统计",
        f"",
        f"| 项目 | 数量 | 说明 |",
        f"|---|---|---|",
        f"| §1 标题数 | {sections['h1']} | 主章节数 |",
        f"| §2 标题数 | {sections['h2']} | 分节数 |",
        f"| §3 标题数 | {sections['h3']} | 子分节数 |",
        f"| 图 (Figure) | {counts['figures']} | `[FACT]/[INTERPRETATION]/[CRITIQUE]` 中的图表引用 |",
        f"| 表 (Table) | {counts['tables']} | 同上 |",
        f"| 公式 | {counts['formulas']} | LaTeX 行内/独立公式计数 |",
        f"| [FACT] | {counts['fact']} | 事实陈述 |",
        f"| [INTERPRETATION] | {counts['interpretation']} | 解读 |",
        f"| [CRITIQUE] | {counts['critique']} | 批判 |",
        f"",
        f"## 完成度评分",
        f"",
        f"| 维度 | 得分 | 满分 |",
        f"|---|---|---|",
        f"| 元数据 (00_overview) | {'1' if has_overview else '0'} | 1 |",
        f"| 总结 (99_final_summary) | {'1' if has_summary else '0'} | 1 |",
        f"| 词汇表 (98_vocabulary) | {'1' if has_vocab else '0'} | 1 |",
        f"| 正文覆盖 | {min(len(body_files), 2)} | 2 |",
        f"| 图表完整性 | {'2' if counts['figures'] + counts['tables'] >= 5 else '1' if counts['figures'] + counts['tables'] > 0 else '0'} | 2 |",
        f"| 批判性分析 | {'2' if counts['critique'] >= 3 else '1' if counts['critique'] > 0 else '0'} | 2 |",
        f"| 公式完整性 | {'1' if counts['formulas'] >= 1 else '0'} | 1 |",
        f"| **总分** | **{score} / 10** | |",
        f"",
        f"## 建议",
        f"",
        f"- " + ("无" if score >= 9 else (
            f"该论文精读**基本完整**（{score}/10）。"
            if score >= 7 else (
            f"该论文精读**部分覆盖**（{score}/10）。可考虑补充正文分章、批判观点或公式整理。"
            if score >= 4 else
            f"该论文精读**覆盖较薄**（{score}/10）。建议按 READING_INSTRUCTIONS.md 重新精读并补充章节。"
        )
        )),
        f"",
        f"*（本页由 `scripts/gen_quality_check.py` 自动生成）*",
        f"",
    ]
    return "\n".join(out), score


def main():
    papers = collect_papers()
    added = 0
    updated = 0
    total_score = 0

    for rel_dir, lit_path in papers:
        path = lit_path / "97_quality_check.md"
        text, score = build_check(rel_dir, lit_path)
        total_score += score
        if path.exists():
            old = path.read_text(encoding="utf-8")
            if old != text:
                path.write_text(text, encoding="utf-8")
                updated += 1
        else:
            path.write_text(text, encoding="utf-8")
            added += 1

    avg = total_score / len(papers) if papers else 0
    print(f"Generated/updated: +{added}, ~{updated} (total {len(papers)})")
    print(f"Average score: {avg:.1f} / 10")


if __name__ == "__main__":
    main()
