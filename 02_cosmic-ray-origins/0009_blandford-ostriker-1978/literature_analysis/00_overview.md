---
title: Particle acceleration by astrophysical shocks
authors: R. D. Blandford (Caltech), J. P. Ostriker (Princeton)
year: '1978'
journal: The Astrophysical Journal 221, L29-L32 (1978)
pages: 'L29'
doi: 10.1086/182658
arxiv: —（预印本时代前）
category: 宇宙线起源
status: completed
read_date: '2026-08-14'
lastread: '2026-08-14'
tags: []
citations: []
path: 02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/00_overview.md
---
> 状态：**精读完成**（2026-08-15）
> ★ **DSA 奠基论文**（与 Bell 1978 同期独立提出，共同构成 diffusive shock acceleration 的双源头）

# 00. Overview — Blandford & Ostriker (1978) 精读笔记

## 基本信息

| 字段 | 内容 |
|---|---|
| **Title** | Particle acceleration by astrophysical shocks |
| **Authors** | R. D. Blandford (Caltech), J. P. Ostriker (Princeton) |
| **Journal** | The Astrophysical Journal 221, L29-L32 (1978) |
| **DOI** | 10.1086/182658 |
| **arXiv** | —（预印本时代前） |
| **Year** | 1978（Received 1977 Dec 12; accepted 1978 Jan 6） |
| **Pages** | L29-L32（4 pages，简报格式） |
| **Citations** | ~2000+（Google Scholar，2024） |

## [FACT] 论文结构

### Abstract（摘要）
> "A new mechanism is proposed for acceleration of a power-law distribution of cosmic rays with approximately the observed slope. High-energy particles in the vicinity of a shock are scattered by Alfvén waves carried by the converging fluid flow leading to a first-order acceleration process in which the escape time is automatically comparable to the acceleration time. Shocks from supernova explosions propagating through the interstellar medium can account for the acceleration of galactic cosmic rays."

**三个关键词**：first-order acceleration；escape time ≈ acceleration time；SNR 银河宇宙线。

### Section III: Acceleration of Cosmic Rays（pp.L30-L32）

**物理图像**：激波携带的汇聚流场中的 Alfvén 波散射高能粒子 → 一阶加速过程（first-order）。

**与 Bell 1978 的等价性**：两篇论文独立得出相同结论——强激波的压缩比决定幂律谱指数。BO 1978 在简报中给出了定性论述，未给出显式公式（Bell 给出了方程 12 的显式推导）。

**SNR 中的应用**：
- SNR 激波中的加速时间：$t_{\rm acc} \sim \kappa / u_s^2$（$\kappa$ = 扩散系数）
- 逃逸时间与加速时间自动可比拟 → 稳态幂律分布自然形成
- 能量上限：SNR 激波条件下可达 $\sim 10^{14}$ eV（1978 年估计，今日修正为 $\sim 10^{15}$ eV）

**自洽性条件**：波增长的特征时间 $R/u_s$（$R$ = SNR 半径，$u_s$ = 激波速度）须小于 SNR 年龄。

## [INTERPRETATION] 与 Bell 1978 的对比

| 维度 | Bell 1978 | BO 1978 |
|---|---|---|
| 物理图像 | 粒子在激波间反复穿越获得能量 | 汇聚流场中 Alfvén 波散射 |
| 数学深度 | 完整方程推导（方程 1-23） | 定性论述为主 |
| 核心公式 | $\mu = 2.5$（$\chi=3$ 或含波速） | 定性"first-order" |
| 能量上限 | $E_{\rm crit} \sim 3.5\times10^{12}$ eV（中性阻尼） | $\sim 10^{14}$ eV |
| 自洽性 | 显式讨论波-粒子耦合 | 讨论 SNR 自洽条件 |

两篇论文**物理等价**，均从"激波压缩→各向异性粒子分布→与波散射→能量增益"的基本图像出发。

## [CRITIQUE] 批判性分析

### 优点
1. **"First-order"命名的历史价值**：将两篇独立论文的机制统一命名为 first-order Fermi acceleration，建立了至今沿用的术语体系
2. **SNR 应用的具体化**：明确将机制与银河宇宙线起源联系起来，是现代 SNR 范式的直接先驱
3. **逃逸时间 ≈ 加速时间的洞察**：加速和逃逸时间自动可比，是 DSA 能产生稳态幂律分布的关键

### 局限（1978 年时点）
1. **数学推导不如 Bell 完整**：简报格式（L29-L32）限制了深度；完整理论见 Blandford (in preparation)（但似乎未单独发表）
2. **能量上限保守**：$10^{14}$ eV 远低于现代认知的 PeVatron 能量尺度（$10^{15}$-$10^{16}$ eV）
3. **非线性效应未考虑**：test-particle 极限，不讨论 CR 反馈对激波结构的修改

### 历史地位
- **1978年两篇奠基文章共同构成 DSA 的双子峰**：Bell (MNRAS) + BO (ApJ)
- 1987 年 Blandford & Eichler 正式命名为 "diffusive shock acceleration (DSA)"

## 前序阅读 / 关联论文

| 关系 | 论文 | 说明 |
|---|---|---|
| 同期独立 | **Bell 1978** | MNRAS 182, 147——同机制独立推导（数学更完整） |
| 综述命名 | **Blandford & Eichler 1987** | Phys. Rep. 154, 1——正式命名 DSA，系统综述 |
| 理论基础 | Skilling 1975a,b,c | 被引为 Alfvén 波散射理论基础 |
| 应用 | Gaisser 1990 | DSA 在膝部 CR 的应用 |
| 波产生 | Kulsrud & Pearce 1969 | CR streaming 激发 Alfvén 波 |
| 银河 CR 论证 | Kulsrud & Zweibel 1975 | 被引为 adiabatic decompression 问题 |

## 关键词

`first-order Fermi acceleration` `diffusive shock acceleration` `SNR acceleration` `Alfvén wave scattering` `cosmic ray origin` `escape time` `acceleration time` `supernova remnants`
