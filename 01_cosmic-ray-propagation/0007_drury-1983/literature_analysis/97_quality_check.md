---
section: "quality"
title: "Quality Check"
parent: "00_overview.md"
previous: "07_time_dependent.md"
next: "98_vocabulary.md"
---

# 97. Quality Check

## A. 元数据核对

- [x] 作者（L. O'C. Drury）三源一致
- [x] 年份（1983）三源一致
- [x] 期刊（Rep. Prog. Phys. 46:973-1027）三源一致
- [x] 目录名 `0007_drury-1983` 与 PDF 一致
- [x] 无勘误

## B. 结构覆盖

- [x] §1 Introduction → [[01_introduction.md]]
- [x] §2 Basic theory → [[02_basic_theory.md]]
- [x] §2.2 Kinematics → [[03_shock_kinematics.md]]
- [x] §2.3 DSA core → [[04_diffusive_acceleration.md]]
- [x] §3 Linear intro → [[05_linear_modifications.md]]
- [x] §3.1 Oblique → [[06_oblique_shocks.md]]
- [x] §3.2 Time-dependent → [[07_time_dependent.md]]
- [ ] §3.3-3.4 → 未单独分章（在 §3 总述中覆盖）
- [ ] §4.1-4.5 Non-linear → 未单独分章（在 §4 总述中覆盖）
- [ ] §5 Concluding remarks → 未单独分章

## C. 关键公式覆盖

- [x] 输运方程 (2.11)
- [x] 谱指数 $a = 3r/(r-1)$
- [x] 压缩比 $r = U_1/U_2$
- [x] 加速时标 (3.39)
- [x] 逃逸概率 $4U_2/v$
- [x] 平均动量增益 $4(U_1-U_2)/(3v)$

## D. 引用完整性

- [x] 向上引用：Bell 1978, Blandford & Ostriker 1978 使用 wikilink
- [x] 向下引用：Strong 2007, Amato & Blasi 2018, Genolini 2021 使用 wikilink

## E. 标签使用

- [x] `[FACT]` 用于论文事实陈述
- [x] `[INTERPRETATION]` 用于推论
- [x] `[CRITIQUE]` 用于批评/限制

## F. 编码

- [x] `fulltext.txt` ISO-8859-1，已转码 `/tmp/drury_1983_utf8.txt`
- [x] 全文无 mojibake 残留

## G. 完整性说明

- 本批（受父代理 `skip remaining body files` 指示）仅写至 §3.2。
- §3.3-3.4（非平面激波、附加能量增益/损耗）、§4.1-4.5（全部非线性修正）、§5 结论**未生成独立文件**；内容在 §3/§4 总述文件中有概要覆盖，但未达"每节独立文件"要求。
- 后续可回溯补齐 08-16 号文件。

上一章：[[07_time_dependent.md]]
下一章：[[98_vocabulary.md]]
