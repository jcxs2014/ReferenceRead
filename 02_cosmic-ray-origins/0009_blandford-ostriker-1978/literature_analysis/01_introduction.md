> 本章属于：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/00_overview.md|Particle Acceleration by Astrophysical Shocks（Blandford & Ostriker 1978）]]
>
> 下一章：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/02_strong_shock_acceleration.md|02_strong_shock_acceleration]]
>
> 总览：`00_overview.md`

# 1. Introduction — 引言与问题提出

## 1.1 本节核心内容

Blandford & Ostriker（以下简称 BO）在本篇中提出了一个**新型宇宙线加速机制**——**强激波处 Alfvén 波散射驱动的 Fermi 一阶加速**。核心创新点是：此前所有激波加速方案都是"二阶"过程（粒子在激波两侧的随机散射，平均能量增益极小），而 BO 指出，由于激波两侧流体汇聚，粒子被 Alfvén 波反复散射回激波面，实际上构成**一阶 Fermi 过程**——平均能量增益正比于 $u/c$（而非 $(u/c)^2$），效率高出 $c/u \sim 100$ 倍。

## 1.2 原文内容

### 研究背景

BO 开篇即指出：**银河系超新星产生的激波**是理想的宇宙线加速场所。关键数值参数：

- 超新星能量：$E_{\rm SN} = 10^{51}$ erg
- ISM 氢密度：$n_0 \approx 1 \text{ cm}^{-3}$
- 标准 Sedov 解冷却时标：$t_{\rm cool} \approx 10^{5.9} \text{ yr}$
- 冷却时冲击速度：$u_{\rm cool} \approx 120 \text{ km s}^{-1}$
- 冷却体积：$V_{\rm cool} \approx 10^{63.4} \text{ cm}^3$

这些数值引用于 Cox & Smith (1974)、McKee & Ostriker (1977)、Spitzer (1978)。

### 能量守恒论证

BO 给出一个简洁的**能量可行性论证**：

$$\text{若每次穿越激波能量增益 } \varepsilon \sim 10^{-1}, \text{ 则总注入能量}$$
$$\varepsilon V_{\rm cool} w_{\rm cr} \sim 10^{50} \text{ erg SN}^{-1}$$

其中宇宙线能量密度 $w_{\rm cr} \sim 10^{-12} \text{ erg cm}^{-3}$。这个量级**恰好满足**已知的宇宙线能量需求，说明超新星激波加速在能量学上是可行的。

### 历史背景

BO 指出此前多个激波加速机制已被研究：

| 作者 | 年份 | 机制 |
|---|---|---|
| Wentzel | 1964 | 激波处粒子反射 |
| Hudson | 1965 | 类似 |
| Jokipii | 1966 | 随机散射 |
| Fisk | 1971 | 流体力学模型 |
| Burn | 1976 | 激波压缩 |

> **分析 / Interpretation**：所有这些方案本质上是"二阶 Fermi 型"——能量增益 $\propto (u/c)^2$，效率太低。BO 的核心贡献是绕过了这个效率瓶颈。

### 观测基础

BO 列举支持"幂律谱是宇宙线加速普适产物"的观测：

- 直接测量：Wentzel (1974) 在地球附近测得 $f \propto p^{-s} d^3x$，$4 < s < 5$
- 银河系射电：Webster (1974)
- 超新星遗迹：Woltjer (1972)
- 河外射电源：De Young (1976)

> **分析 / Interpretation**：如此广泛的观测一致性说明需要一个**普适机制**，而强激波 Fermi 加速正是这样的候选。

## 1.3 关键公式

本节前半部分（引言）不涉及核心公式推导，但给出关键背景量：

$$v_A = 13\left(\frac{B}{10^{-6} \text{ G}}\right)\left(\frac{n}{1}\right)^{-1/2} \text{ km s}^{-1} \approx 50 \text{ km s}^{-1}$$

其中 $v_A$ 为 Alfvén 速度，$B \approx 3 \mu\text{G}$ 为 ISM 磁场，$n \approx 1 \text{ cm}^{-3}$ 为质子数密度。

### 绝热不变量守恒（垂直激波特例）

对于激波面垂直于磁场的特例（$u_- \tan\theta_- > c$，磁场无法通过变换消除），绝热不变量 $p_\perp^2/B$ 近似守恒，穿过激波后平均动量平方变化：

$$\left\langle \frac{\Delta(p^2)}{p^2} \right\rangle = \frac{1}{3}(1+2r)r^{-2/3} - 1$$

其中 $r$ 为压缩比。

## 1.4 关键参数

| 参数 | 值 | 物理意义 |
|---|---|---|
| $E_{\rm SN}$ | $10^{51}$ erg | 超新星能量 |
| $n_0$ | $1 \text{ cm}^{-3}$ | ISM 密度 |
| $v_A$ | $50 \text{ km s}^{-1}$ | Alfvén 速度 |
| $w_{\rm cr}$ | $10^{-12} \text{ erg cm}^{-3}$ | 宇宙线能量密度 |
| $V_{\rm cool}$ | $10^{63.4} \text{ cm}^3$ | 超新星冷却体积 |
| $\varepsilon$ | $\sim 10^{-1}$ | 单次穿越能量增益 |
| $s$ | $4-5$ | 观测幂律谱指数 |
| $q$ | $3r/(r-1)$ | 理论预测谱指数（§II） |

## 1.5 作者的逻辑

```
超新星产生大体积强激波（背景）
→ 宇宙线能量密度已知 ~ $10^{-12}$ erg/cm$^{3}$（观测）
→ 若激波穿越时平均增益 ~ $10^{-1}$，能量注入恰好满足需求（可行性）
→ 但此前所有机制都是二阶的，效率不够（问题）
→ 激波两侧的流体汇聚提供一阶加速可能（解决方案）
→ 观测显示幂律谱在多种环境中存在（需普适机制）
```

## 1.6 我的理解

BO 这篇短文的价值不在于数学复杂——它的公式推导只有一页——而在于**物理洞察的清晰度**：一阶 Fermi 加速的图像简单到只用两页就讲清楚。它绕过了此前所有"如何在激波处高效加速粒子"的困境，只用了三件事：(1) Alfvén 波散射使粒子在激波两侧反复穿越；(2) 两侧流体汇聚（速度差 $u_- - u_+$）使每次穿越平均获得动能；(3) 逃逸时间自动与加速时间可比，天然给出幂律分布。

> **分析 / Interpretation**：这篇论文与 Bell 1978 独立发现了同一机制（Bell 在 MNRAS 179, 573 中独立推导）。BO 这篇更侧重物理图像，Bell 那篇则提供了完整数学处理。两者并列为 DSA 的奠基之作。

## 1.7 潜在问题与值得关注的地方

1. **Alfvén 波源的自洽性问题**：BO 假设激波附近存在足够强的湍流使粒子各向同性化，但激波自身能否产生这种湍流？BO 在 §III 中提到，宇宙线本身的 streaming instability 可以自激发 Alfvén 波（Kulsrud & Pearce 1969），形成自洽回路——但这一机制在 §II 中只是作为假设引入。

2. **长度尺度排序假设**：$\delta \ll r_L \ll L \ll H$。BO 承认这个排序的假设是必要的，如果湍流强度变化或扩散系数过小，可能打破排序、影响加速效率。

3. **谱指数偏低**：理想强激波 $r=4$ 给出 $s=4$，观测是 $4.5$。BO 用"激波逐渐变为 Alfvénic 时效率降低"来解释，但这需要额外计算。