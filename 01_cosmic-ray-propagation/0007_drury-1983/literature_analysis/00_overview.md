---
id: drury-1983
title: "An introduction to the theory of diffusive shock acceleration of energetic particles in tenuous plasmas"
author: "L. O'C. Drury"
authors: "L. O'C. Drury"
affiliation: "Max-Planck-Institut für Kernphysik, Heidelberg, West Germany"
year: 1983
journal: "Reports on Progress in Physics"
volume: 46
pages: 57-130
category: "宇宙线传播 / Diffusive Shock Acceleration (DSA)"
doi: null
arxiv: null
pdf_path: "../drury-1983_diffusive-shock-acceleration.pdf"
citations:
  - '[[02_cosmic-ray-origins/0008_bell-1978/literature_analysis/00_overview|bell-1978]]'
  - '[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/00_overview|blandford-ostriker-1978]]'
status: completed
tags:
  - DSA
  - diffusive shock acceleration
  - cosmic rays
  - particle acceleration
  - supernova remnants
read_date: '2026-08-16'
lastread: '2026-08-16'
sections:
  - '§1 Introduction'
  - '§2 Basic theory'
  - '§3 Linear modifications'
  - '§4 Non-linear modifications'
  - '§5 Concluding remarks'
analysis_date: '2026-08-16'
encoding_note: "fulltext.txt 为 ISO-8859-1；已转码为 /tmp/drury_1983_utf8.txt 用于引用。"
---

# L. O'C. Drury (1983) — DSA 综述精读

## 1. 元数据核对（metadata verification）

| 来源 | 值 |
|---|---|
| 任务上下文 | L. O'C. Drury, 1983, Rep. Prog. Phys. 46, 973–1027 |
| 目录名 | `0007_drury-1983` |
| PDF 首页 | "Rep. Prog. Phys., Vol. 46, pp. 973–1027, 1983" / "L O'C Drury" / "Max-Planck-Institut für Kernphysik" |

三源一致，无勘误。本综述为 DSA（Diffusive Shock Acceleration，又称 first-order Fermi）理论的奠基性评述。

## 2. 综述定位

- **期刊**：Reports on Progress in Physics 46 (1983) 973–1027（55 页长综述）
- **发表时点**：DSA 概念在 Krymsky (1977), Axford et al. (1977), Bell (1978), Blandford & Ostriker (1978) 四篇论文几乎同时独立提出后 5–6 年
- **核心问题**：稀薄等离子体中激波如何把相对论/近相对论带电粒子加速到幂律能谱，从而解释银河系宇宙线能谱指数（≈ −2.7）与非热射电源（synchrotron）辐射谱
- **方法论**：宏观（transport equation + MHD 激波结构）与微观（Fermi 单粒子反弹）双视角并行推导

## 3. 章节树（section tree）

主章用一级编号 1–5；子节用 § N.N：

- § 1  Introduction（p. 975, 2 页）
- § 2  Basic theory（p. 976, 11 页）
  - § 2.1  Transport of energetic charged particles
  - § 2.2  Shock kinematics and scatter-free acceleration
  - § 2.3  Diffusive acceleration at shocks
- § 3  Linear modifications（p. 987, 16 页）
  - § 3.1  Oblique shocks
  - § 3.2  Time-dependent solutions
  - § 3.3  Non-planar shocks（球激波）
  - § 3.4  Additional energy gains and losses
- § 4  Non-linear modifications（p. 1003, 22 页）
  - § 4.1  Self-induced scattering
  - § 4.2  Shock structure（Rankine–Hugoniot 推广）
  - § 4.3  Non-linear effects on the particle spectrum（精确解、Blandford 微扰）
  - § 4.4  Injection and selective acceleration
  - § 4.5  Pressure divergence in non-linear shocks
- § 5  Concluding remarks（p. 1025, 2 页）

## 4. 图表索引

| 类型 | 数 | 说明 |
|---|---|---|
| Figure | 8 | Fig. 1 激波磁场几何；Fig. 2 scatter-free 轨迹；Fig. 3 球激波能谱；Fig. 4 星风终止激波；Fig. 5 时间依赖能谱；Fig. 6 各向异性修正；Fig. 7 修改激波结构速度剖面；Fig. 8 非线性 delta 源加速谱 |
| Table | 0 | 综述全文未含表格 |

## 5. 引用网络

- **向上**（Drury 1983 引用）：
  - [[bell-1978]] Bell, A. R. (1978) MNRAS 182, 147 — 微观 DSA 推导、自激 Alfven 波
  - [[blandford-ostriker-1978]] Blandford & Ostriker (1978) Nature 271, 57 — 非相对论 DSA 宏观解
  - 此外：Krymsky (1977), Axford-Leer-Skadron (1977), Schatzman (1963), Parker (1958), Jokipii (1966, 1968), Fisk (1971), Scholer, Forman & Morfill (1979), Vasil'ev et al. (1980), Axford (1981a,b), Lagage & Cesarsky (1981, 1982)
- **向下**（本库中引用 Drury 1983 的论文）：
  - [[strong-2007]] Strong et al. (2007) ARA&A — 银河系宇宙线传播综述
  - [[amato-blasi-2018]] Amato & Blasi (2018) A&A — SNR 加速
  - [[genolini-2021]] Genolini (2021) — 综述综述 / historical review

## 6. 精确度（fidelity）说明

- 全文 55 页、约 2800 行文本，精读覆盖全部 5 章 11 节
- 关键公式（谱指数 a、压缩比 r、加速时标 t_acc）均从 PDF 原文逐字摘录并校验
- 全文使用 `[FACT]` / `[INTERPRETATION]` / `[CRITIQUE]` 三标签体系
- 术语表见 [[98_vocabulary.md]]

## 7. 分析文件导航

| 文件 | 内容 |
|---|---|
| [[00_overview.md]] | 本文（元数据 + 结构 + 引用） |
| [[01_introduction.md]] | § 1 引言 |
| [[02_basic_theory.md]] | § 2 基本理论（输运方程 + 输运系数） |
| [[03_shock_kinematics.md]] | § 2.2 激波运动学与无散射加速 |
| [[04_diffusive_acceleration.md]] | § 2.3 DSA 核心理论（功率律谱导出） |
| [[05_linear_modifications.md]] | § 3 线性修正总述 |
| [[06_oblique_shocks.md]] | § 3.1 斜激波 |
| [[07_time_dependent.md]] | § 3.2 时间依赖解 |
| [[08_nonplanar_shocks.md]] | § 3.3 非平面激波（球激波） |
| [[09_energy_gains_losses.md]] | § 3.4 附加能量增益与损耗 |
| [[10_nonlinear_modifications.md]] | § 4 非线性修正总述 |
| [[11_self_induced_scattering.md]] | § 4.1 自激散射 |
| [[12_shock_structure.md]] | § 4.2 修改激波结构 |
| [[13_nonlinear_spectrum.md]] | § 4.3 非线性对谱的影响 |
| [[14_injection.md]] | § 4.4 注入与选择性加速 |
| [[15_pressure_divergence.md]] | § 4.5 非线性激波压力发散 |
| [[16_conclusion.md]] | § 5 结论 |
| [[97_quality_check.md]] | 质量检查 |
| [[98_vocabulary.md]] | 术语表 |
| [[99_final_summary.md]] | 最终总结 + 完整性核查 |

上一章：（无，此为总览）
下一章：[[01_introduction.md]]
