---
purpose: quality_check
---

# 97. Quality Check

上一章：[09_summary_and_conclusions](09_summary_and_conclusions.md)
下一章：[98_vocabulary](98_vocabulary.md)

## 元数据校验

- [x] 作者/年份/期刊从 PDF 第 1 页核对一致（Sneden, Cowan, Gallino; 2008; Ann. Rev. A&A 46:241–88）
- [x] DOI: 10.1146/annurev.astro.46.060407.145207
- [x] 目录名与 PDF 一致，无勘误
- [x] 任务上下文 frontmatter 全部落地（category、year、pages）

## 结构覆盖

- [x] §1 Introduction → 01_introduction.md
- [x] §2 Heavy Element Formation → 02_heavy_element_formation.md
- [x] §3 Solar-System Abundances → 03_solar_system_abundances.md
- [x] §4 The r-Process: Observations → 04_r_process_observations.md
- [x] §5 The s-Process: Observations → 05_s_process_observations.md
- [x] §6 r-Process Abundance Implications（含 6.1 同位素、6.2 多 r 位点）→ 06_r_process_abundance_implications.md
- [x] §7 Early Galactic Nucleosynthesis（含 7.1、7.2）→ 07_early_galactic_nucleosynthesis.md
- [x] §8 s-Process Abundance Implications（含 8.1、8.2）→ 08_s_process_abundance_implications.md
- [x] §9 Summary → 09_summary_and_conclusions.md

## 图表与数据

- [x] 21 张 Figure 已识别（Fig. 1–21）
- [x] 3 张 Table 已识别（Table 1–3）
- [x] 关键数值保留：nₙ (s) ≲ 10⁸ cm⁻³，nₙ (r) ∼ 10²⁴–10²⁸ cm⁻³；τ₁/₂ (⁹⁹Tc) = 2.1×10⁵ yr；τ₁/₂ (²³²Th) = 14.05 Gyr；τ₁/₂ (²³⁵U) = 0.704 Gyr；τ₁/₂ (²³⁸U) = 4.468 Gyr；CS 22892-052 [Eu/Fe] ≃ +1.6；f₁₅₁ (r-rich) ≃ 0.5±0.1；陨石 f₁₅₁ = 0.478
- [x] 关键公式：N(T) = N₀ e^(−λT)（核宇宙年龄学）

## 标签与交叉引用

- [x] [FACT] / [INTERPRETATION] / [CRITIQUE] 标签已使用
- [x] 每文件包含 上一章/下一章 导航头
- [x] in-repo 引用：cameron-1968、b2fh-1957、wallerstein-1997、cowan-2021、kaeppeler-2011（用 [[path]] 语法）
- [x] 中英混排技术术语保留英文（r-process, s-process, CEMP, r-II, AGB, r-only, nucleocosmochronometry, branching point）

## YAML frontmatter 校验

- [x] 每文件 YAML frontmatter 以 `---` 分隔、键值对合法
- [x] 无未闭合引号
- [x] multi-line 值用 YAML list 语法

## 已知不足（记录，非错误）

- [ ] 未做图（Figures）的图内数据逐点提取——本文 PDF 图示为向量/图像，仅对 Fig. 6、10、11、12、13、14、19、21 做文本层描述
- [ ] Table 2 数据未在文本层中完整提取（表中数据分散在 §7 正文讨论中，已吸收进 §7 分析）
