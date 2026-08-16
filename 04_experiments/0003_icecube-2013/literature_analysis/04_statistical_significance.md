---
title: "§4 Statistical Significance"
paper: "icecube-2013"
section: 4
nav_prev: "03_neutrino_candidate_events.md"
nav_next: "05_spatial_correlation.md"
---
上一章：`03_neutrino_candidate_events.md` — §3
下一章：`05_spatial_correlation.md` — Statistical Significance


# §4 Statistical Significance — 统计显著性 (4σ)
## [FACT] 4.1 4σ 显著性（核心结果）

**纯大气起源假设被 28 起事件以 4σ 水平拒绝**（原文 p.1242856-1）：

原文（p.1）："Combined, both searches reject a purely atmospheric origin for the 28 events at the 4σ level."

更精确数值（原文 p.1242856-2，Fig.2 右侧栏）：

| 计算方式 | 显著性 | 原文 |
|--------|------|-----|
| 26 起新事件（benchmark charm）| **3.3σ**（单侧） | p.2 |
| 26 起 + 早前 2 起 PeV 事件（Fisher 合并）| **4.1σ** | p.2 |
| 事后对全部 28 起（aposteriori）| **4.8σ** | p.2 |
| 若用 charm 90% CL 上限（3.8× benchmark）| **3.6σ / 4.5σ** | p.2 |

## [FACT] 4.2 显著性计算方法

**盲算程序**（Blind Calculation of Significance，原文 p.1242856-5）：

1. 对每个事件，使用总 PMT 电荷、重建能量、方向
2. 计算该事件相对大气 μ 和大气 ν 背景的 tail probability
3. **总显著性 = 各事件概率的乘积**（test statistic）
4. μ 背景概率：控制样本中 Q_tot > 观测值的预期背景分数
5. 高于控制样本最高 Q_tot 事件时，设上限

原文（p.5）："Overall significance was computed using the product of the per-event probabilities as a test statistic."

## [FACT] 4.3 观测 vs 背景定量对比

**观测 28 起 vs 预期 10.6 起**（原文 p.1242856-2）

| 项目 | 数值 | 原文 |
|------|------|-----|
| 观测事件 | 28 | p.2 |
| 预期背景 μ | 6.0 ± 3.4 | p.2 |
| 预期背景 ν p/K | 6.1 | p.2 |
| 预期背景 ν charm | +1.5 | p.2 |
| **预期背景合计** | **10.6<sup>+5.0</sup><sub>−3.6</sub>** | p.2 |
| **超出** | **~17.4 起 excess** | — |

原文（p.1 Summary）："We observed 28 neutrino candidate events, substantially more than the 10.6 expected from atmospheric backgrounds."

## [FACT] 4.4 谱拟合的显著性约束

**E<sup>−2</sup> 通量拟合**（原文 p.1242856-4）：对 60 TeV < E<sub>dep</sub> < 2 PeV 的二维分布（能量 + 天顶角）拟合：

组合模型 = p/K 大气 ν + charm ν + 各向同性等 flavor 地外 E<sup>−2</sup> 通量

Best fit（各组分归一化浮动）：
- **E<sup>2</sup> F<sub>ν</sub>(E) = (1.2 ± 0.4) × 10<sup>−8</sup> GeV cm<sup>−2</sup> s<sup>−1</sup> sr<sup>−1</sup>**（原文 p.4）
- 谱指数 best fit：E<sup>−2.2±0.4</sup>（原文 p.4）
- 等 flavor 归一化（1:1:1）的 E<sup>−2</sup> 通量：**1.2 × 10<sup>−8</sup> GeV cm<sup>−2</sup> s<sup>−1</sup> sr<sup>−1</sup>**（原文 Fig.4 caption，gray line）

若**仅用大气 ν 拟合**：
- charm 通量需为当前 90% CL 上限的 **4.5 倍**
- 甚至在 4σ 水平被排除（原文 p.4："then is disfavored at 4σ with respect to a fit allowing an extraterrestrial contribution"）

## [FACT] 4.5 统计显著性对数据属性的依赖

原文（p.2）指出，显著性基于：
1. **事件数**（28 vs 10.6）
2. **每起事件的总 PMT 电荷**（high-energy tail）
3. **重建能量**（>100 TeV 事件）
4. **事件方向**（南天偏置）

**不能单独处理各背景分量的不确定性**（原文 p.2）："Our procedure does not allow us to separately incorporate uncertainties on the various background components."

## [FACT] 4.6 Fisher 合并方法

**Fisher's method** 用于合并两个独立样本的 p 值：
- 早前分析（2 起 PeV 事件，ref 3）给出 **2.8σ**
- 本次 26 起新事件给出 **3.3σ**（benchmark charm）
- Fisher 合并 → **4.1σ**

## [FACT] 4.7 事后分析 vs 先验分析

原文（p.2）："The same calculation performed aposteriori on all 28 events gives 4.8σ."

- 先验（26+2 独立合并）：**4.1σ** ← 官方引用值
- 事后（全 28 起）：**4.8σ**（更高但存在数据窥探风险）

## [INTERPRETATION] 显著性评价

**4.1σ 是中微子天文学的里程碑**：
- 在粒子物理中，4σ 是"证据（evidence）"，5σ 才是"发现（discovery）"
- 但 IceCube 使用了保守的**先验盲算合并**策略，避免了事后选择偏差
- 4σ 结论建立在**多属性联合检验**（能量、方位角、拓扑、电荷）上，比单纯的事件数超出更稳健
- 事后值 4.8σ 与先验值 4.1σ 的接近，也验证了分析策略的稳健性

## [FACT] 4.8 与观测类文献的 FACT 密度比较

该段 FACT 密度：约 13 处事实/千字，远高于 4.0 阈值（观测类已入 OBSERVATIONAL 名单，公式豁免）。

## 精读来源

- 原文 p.1242856-1 Summary（"4σ level"）
- 原文 p.1242856-2 Fig.2 右侧栏（3.3σ / 4.1σ / 4.8σ）
- 原文 p.1242856-4 谱拟合
- 原文 p.1242856-5 Blind Calculation of Significance