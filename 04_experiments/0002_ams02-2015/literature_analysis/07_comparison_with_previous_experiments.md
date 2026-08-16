---
title: "§7 Comparison with Previous Experiments"
paper: "ams02-2015"
section: 7
nav_prev: "06_statistical_power.md"
nav_next: "08_conclusions.md"
---

上一章：`06_statistical_power.md`
下一章：`08_conclusions.md` — 结论

# §7 Comparison with Previous Experiments — 与前代实验对比

## 7.1 本节核心内容

AMS-02 数据与 ATIC-2、BESS-Polar II、CREAM、PAMELA（均 2000 年后实验）的质子流强测量总体**一致**，但 AMS-02 的**精度量级**（统计 + 系统误差 <5%）远超其他实验（多数 10%–30%）。正是这一精度差异使 AMS-02 能单独给出 $\gamma(R)$ 变硬的证据——单实验内排除单幂律。

## 7.2 原文内容

- **Fig.3(b)**（原文 p.6）：AMS-02 质子流强（动能刻度）× $E_K^{2.7}$ vs 四个 2000 年后实验
- 前代实验（原文 Ref. [3]–[6]）：
  - **ATIC-2**（p.6 脚注 [3]）：A.D. Panov et al.，2009–2014；气球实验，能量覆盖 ~50 GeV – ~TeV
  - **BESS-Polar II**（脚注 [4]）：2007-12 至 2008-01，25 天南极气球飞行；统计与系统误差合并
  - **CREAM**（脚注 [5]）：Y.S. Yoon et al.，Astrophys. J. 728, 122 (2011)；3 次气球实验累计
  - **PAMELA**（脚注 [6]）：O. Adriani et al.，Astrophys. J. 765, 91 (2013) 与 Science 332, 69 (2011)；轨道实验，能量覆盖 ~2 GeV – ~200 GeV

- **前人观测**（原文 Introduction，p.2）：
  - ATIC-2、CREAM、PAMELA 均显示质子流强偏离单幂律
  - 不同实验报告的偏离形态**不一致**（原文："different variations of the flux with energy"）
  - 催生多源、多机制、多传播模型（Ref. [7] 综述）

## 7.3 关键公式

无。对比图以**数据点叠加**形式呈现（原文 Fig.3(b)）。

## 7.4 关键参数

| 实验 | 平台 | 能量范围 | 精度 | 观测时间 |
|---|---|---|---|---|
| AMS-02（本文） | ISS 轨道 | 1 GV – 1.8 TV | 系统 <5% | 30 个月 |
| ATIC-2 | 气球 | ~50 GeV – ~TeV | ~10%–20% | 一次飞行 |
| BESS-Polar II | 气球 | ~1 GeV – ~10 GeV | ~5%–10% | 25 天 |
| CREAM | 气球 | ~10 GeV – ~TeV | ~10%–30% | 3 次飞行 |
| PAMELA | 卫星 | ~2 GeV – ~200 GeV | ~3%–5% | 多年 |

## 7.5 图表分析

**Fig.3(b) 对比**（原文 p.6）：
- AMS-02 数据在动能 1–1800 GeV 范围
- 其他实验在**重叠能量段**与 AMS-02 数据总体一致
- AMS-02 数据点**误差条显著更小**，且密度更高
- **关键观察**：
  - AMS-02 在 <100 GeV 与 PAMELA 数据**几乎重合**（PAMELA 轨道数据精度接近但覆盖范围较窄）
  - AMS-02 在 >100 GeV 显著超越 CREAM（CREAM 误差条 10–30%）
  - AMS-02 在 ~TeV 端填补了 CREAM/ATIC 与 PAMELA 之间的**精度空白**

## 7.6 作者的逻辑

1. 前代实验显示单幂律偏离，但**形态不一致**
2. AMS-02 以**单一实验**跨越 1 GV–1.8 TV，精度 <5%
3. 与其他实验总体一致（验证无系统偏差）
4. 但精度量级显著超越——因此 AMS-02 的 $\gamma(R)$ 变硬是**可信的新观测**

## 7.7 我的理解

**与库内文献 hess-2016 对比**：HESS 测量银河系中心 PeV 质子加速证据（VHE γ 射线），与本文构成**互补**——AMS-02 是**直接宇宙线测量**（能量至 ~1.8 TV，即 ~1.8 TeV 动能），HESS 是**间接 γ 射线推断**（至数十 TeV γ 能量 → ~1 PeV 母体质子能量）。两者共同覆盖 1 GV – 1 PeV 的质子能谱区间。

**历史脉络**：
- 1960s–1990s：气球/卫星实验（Cosinus、BESS、PAMELA 前代）给出粗略幂律
- 2000–2014：ATIC-2、CREAM、PAMELA 显示变硬迹象
- **2015（本文）**：AMS-02 以 300 M 事件 + <5% 系统误差，**首次明确**给出变硬证据

> [FACT] 原文 Ref. [27]（Lafferty & Wyatt 1995）被用于所有数据点的 $\tilde{R}$ 校正——这保证与其他实验的动能-刚性转换一致。

## 7.8 潜在问题与值得关注的地方

- [FACT] 原文图 Fig.3(b) 中 AMS-02 数据在**动能刻度**展示——动能 $E_K = \sqrt{\tilde{R}^2 + M_p^2} - M_p$，在低动能端（<100 GeV）动能 ≈ 刚性，但在高动能端（>TeV）两者差异显著。
- [CRITIQUE] ATIC-2 与 CREAM 的**系统误差结构**未在本文中详细讨论——仅定性说"不同实验报告的偏离形态不一致"。
- [FACT] 原文脚注 [3] 引出的 ATIC-2 引用（D. Maurin, F. Melot, R. Taillet, A&A 569, A32 (2014)）是**重新提取的 ATIC 数据**——原 ATIC 质子分析（Panov 2009）已不再作为独立分析，而是被 Maurin 2014 重新处理。
- [FACT] 原文脚注 [4] 说明 BESS-Polar II 的**统计与系统误差合并**——因此其误差条不可分解为两个独立分量。
- [CRITIQUE] **太阳调制**在不同实验观测年份不同（ATIC-2 ~2008，PAMELA ~2006–2009，BESS-Polar II 2007–2008，AMS-02 2011–2013），对低刚性端对比有潜在影响——本文未在 Fig.3(b) 中做太阳调制校正对比。
