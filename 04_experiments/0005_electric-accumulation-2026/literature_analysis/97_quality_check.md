> 文献：`04_experiments/0005_electric-accumulation-2026`
> 精读完成度自查（每项 × 完成 / △ 部分 / × 未完成）

## 结构完整性

- [×] 00_overview.md — frontmatter 完整（title/authors/year/journal/doi/arxiv）
- [×] 论文结构树（§I–§VI + Appendix A/B）与全文章节对应
- [×] companion paper 关系说明（PRD 114, 015016 vs PRL 137, 021804）

## 精读质量

- [×] 正文 6 个正文章节（01–06）结构完整
- [×] 附录 2 个文件（06_appendix_a / 07_appendix_b）结构完整
- [×] 08_references.md 包含主要引用、公式汇总、图件说明

## 标注统计（grep 实测）

| 标签 | 数量 | 实测 |
|---|---|---|
| [FACT] | 87 | 00×5 + 01×20 + 02×16 + 03×12 + 04×9 + 05×6 + 06×7 + 07×3 + 08×8 + 97×1 |
| [INTERPRETATION] | 29 | 01×5 + 02×6 + 03×7 + 04×4 + 05×2 + 06×3 + 07×1 + 97×1 |
| [CRITIQUE] | 5 | 01×1 + 02×1 + 03×1 + 05×1 + 97×1 |
| 总行数 | 590 | wc -l *.md |

## 自审检查

- [×] 无占位符（grep XXXXX/按需/TODO/FIXME 零命中）
- [×] arxiv 字段已填（arXiv:2510.25825，companion paper）
- [×] DOI 字段已填（10.1103/physrevd.114.015016）
- [×] fulltext.txt 存在（86549 chars，18 pages）

## 关键公式验证

- [×] 密度增强公式 10¹² × (t/yr)（公式 7）
- [×] VE 表达式（公式 8）
- [×] 宇宙线 mCP population 公式（公式 5、6）
- [×] 大气电场捕获条件 qχ ≳ 10⁻⁷
