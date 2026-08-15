---
title: "2. Observational Data — 能谱、成分与银道面各向异性"
paper: "Hillas 1984, The Origin of Ultra-High-Energy Cosmic Rays"
outline_ref: "§2 OBSERVATIONAL DATA"
original_sections: ["§2.1 Energy Spectrum (L127–217)", "§2.2 Anisotropy (L219–340)"]
---

> 上一章：[[02_cosmic-ray-origins/0011_hillas-1984/literature_analysis/01_why_bother.md|01_why_bother]]
> 下一章：[[02_cosmic-ray-origins/0011_hillas-1984/literature_analysis/03_acceleration_mechanisms.md|03_acceleration_mechanisms]]

## 2.1 [FACT] 探测手段与实验

能量 $> 10^{15}$ eV 的粒子通过大气簇射（extensive air showers）间接探测：粒子撞击大气产生次级粒子雨，由地面阵列或荧光望远镜观测。1984 年时运行的主要实验：

| 实验 | 地点 | 面积 | 特点 |
|------|------|------|------|
| Volcano Ranch | 美国 | $\sim 8$ km$^2$ | 早期大型地面阵列 |
| Haverah Park | 英国 | $\sim 15$ km$^2$ | 中纬度，统计优 |
| Sydney | 澳大利亚 | $\sim 5$ km$^2$ | 南天覆盖 |
| Yakutsk | 俄罗斯 | 多方法 | 高纬度 |
| Chacaltaya | 玻利维亚 | $\sim 1$ km$^2$ | 高海拔 |

## 2.2 [FACT] Figure 3：能谱

Hillas 汇总了当时所有数据，给出微分通量 $J(E)$（粒子数 · cm$^{-2}$ · s$^{-1}$ · sr$^{-1}$ · eV$^{-1}$，乘以 $E^{3}$ 后作图以显示谱指数变化）：

| 能量段 | 谱指数 $\gamma$ | 特征 |
|--------|----------------|------|
| $< 5 \times 10^{15}$ eV | $\sim 2.7$ | 银河系宇宙线主流，"膝"以下 |
| $5 \times 10^{15}$–$10^{19}$ eV | $\sim 3.0$–$3.1$ | "膝"（knee）之后，平滑 |
| $> 10^{19}$ eV | 更陡（$\sim 3.3$）或平坦 | "踝"（ankle）附近，争议大 |

**膝（knee）**在 $E \sim 5 \times 10^{15}$ eV，Hillas 讨论两种解释：

- **泄漏模型**：不同原子序数 $Z$ 的核各自有"膝"在 $E_{\rm knee} \propto Z$——质子最先泄漏，重核依次
- **加速截止**：SNR 加速上限在 $\sim 10^{15}$ eV，膝之后是河外成分

**踝（ankle）**在 $E \sim 10^{18}$–$10^{19}$ eV 附近，解释更加困难——Yakutsk 数据暗示谱可能"变平"甚至反转，但其他实验（Sydney）未见。

## 2.3 [FACT] 初级粒子成分

- 在 $< 10^{15}$ eV 可直接测量（气球/卫星实验）：约 90% 质子、9% α、1% 重核
- **在 $10^{15}$–$10^{19}$ eV**：仅靠 $X_{\max}$（簇射最大发展深度）与 $\mu/N_{\rm ch}$ 比间接推断
- 不同实验结论不一致：有些暗示重核主导（$\langle A \rangle > 10$），有些暗示质子主导
- Hillas 指出：**成分的模糊性直接影响轨迹分析**（重核 $r_L \propto 1/Z$，偏转更大）

## 2.4 [FACT] Figure 4：各向异性相位与幅度

**Figure 4**（Haverah Park 数据）：各向异性相位（小时角）与能量关系：

| 能量段 | 相位（时角） | 含义 |
|--------|------------|------|
| $< 10^{14}$ eV | $\sim 3$–$4$ h | 稳定银河系各向异性（对流+梯度） |
| $5 \times 10^{17}$–$10^{18}$ eV | 快速变化 | 成分转变或新源开启 |
| $> 10^{18}$ eV | 新相位 | 与银河系平面的偏离增大 |

**关键数值**：Haverah Park 报告的各向异性幅度 $A \approx 0.06\%$——很小，但统计显著。多实验（Haverah Park、Yakutsk、Chacaltaya）的相位比对验证了**非随机性**。

## 2.5 [FACT] 泄漏模型的各向异性约束

泄漏模型预言：$J(E) \propto E^{-\gamma}$，$\gamma = 1 + t_A / t_E$（$t_A$ 加速时间、$t_E$ 逃逸时间）。若 $Q(E) \propto E^{-\gamma_0}$，银河系内粒子数 $N(E) = Q(E) \cdot T(E)$。

**Hillas 对泄漏模型的评价**：虽然能解释膝以下谱，但**在膝以上的数据越来越不一致**——特别是 Yakutsk 的高能数据与 Sydney/Haverah Park 存在显著张力。

## 2.6 [FACT] 南向过量的解释

Hillas 提到 $< 10^{19}$ eV 存在 **南向过量**（Sydney 数据），被解释为：

- 银河系内宇宙线的**密度梯度**（$\sim 15\%$ kpc$^{-1}$，指向 Orion 方向）
- 或者我们居住在**磁场"空洞"**中（位于银道面以北）

这**偏向银河系内起源**。

## 2.7 [INTERPRETATION] 我的理解

Hillas 的观测综述揭示了 1984 年时的**核心张力**：

1. 成分不确定 → 无法确定偏转大小 → 无法做源定位
2. 能谱在膝以上"平滑过渡"到河外？还是存在新的加速阶段？
3. 各向异性数据在小尺度上偏向银河系内，但在大尺度上（$> 10^{19}$ eV）指向银河系外（Virgo 方向）

## 2.8 [CRITIQUE] 潜在问题

1. Hillas 引用的数据来自 1980 年代早期实验，统计量有限（$\sim 500$ km$^2$·yr），能量分辨约 30%
2. 不同实验的"能量标定"存在系统偏差（Figure 3 阴影带）
3. 各向异性 $0.06\%$ 的量级极小，对银河系内源模型要求精细的密度梯度
