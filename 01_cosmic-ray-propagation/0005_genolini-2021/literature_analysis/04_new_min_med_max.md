> 本章属于：New minimal, median, and maximal propagation models for dark matter searches with Galactic cosmic rays（Génolini et al. 2021）
>
> 上一章：`03_statistical_method.md`
>
> 下一章：`06_summary_conclusion.md`
>
> 总览：`00_overview.md`

# 4. New MIN-MED-MAX Fluxes — 新 min/med/max 通量

## 4.1 本节核心内容

§V 呈现新 min/med/max 模型的定量结果：反质子和正电子的 astrophysical background 预测，拟合公式，以及与旧版模型的比较。

## 4.2 反质子通量

### 4.2.1 关键结果

| 量 | MIN | MED | MAX |
|---|---|---|---|
| 反质子 astrophysical background | 最低 | 中值 | 最高 |
| 相对旧版的不确定性缩小 | $\sim 6$ 倍 | — | — |

**反质子背景通量**（在 $\sim 10$ GeV，$\langle\sigma v\rangle_{bb}$ 湮灭）：

| 模型 | $\bar{p}/p$ 比率 | 备注 |
|---|---|---|
| MIN | 最低 | $L$ 小 → 停留时间短 |
| MED | 与 AMS-02 最佳拟合 | — |
| MAX | 最高 | $L$ 大 → 停留时间长 |

### 4.2.2 拟合公式

本文提供了反质子背景的**handy fitting formulae**（附录 E）：

$$\phi_{\bar{p}}^{\rm sec}(E) \approx A \left(\frac{E}{E_0}\right)^{-\alpha}$$

参数 $A, \alpha, E_0$ 对三个模型分别给出，方便 DM 搜寻直接使用。

## 4.3 正电子通量

### 4.3.1 关键结果

| 量 | MIN | MED | MAX |
|---|---|---|---|
| 正电子 astrophysical background | 最低 | 中值 | 最高 |
| 相对旧版的不确定性缩小 | $\sim 2$ 倍 | — | — |

**正电子背景通量**（在 $\sim 10$ GeV）：

正电子的 min-max 范围比反质子窄（$\sim 2$ 倍 vs $\sim 6$ 倍），因为正电子通量 $\propto L^{3/2}/K^{1/2}$，对 $L$ 的依赖较弱。

## 4.4 与旧版的比较

| 方面 | 旧版 (Cirelli 2008) | 新版 (Génolini 2021) |
|---|---|---|
| 数据 | PAMELA 等 | AMS-02 最新 |
| 扩散系数 | 简单幂律 | 含高低刚度断裂 |
| 晕大小 | 未系统约束 | 放射性同位素约束 |
| 不确定性量化 | 粗略 | 系统统计方法 |
| 反质子不确定性 | 大 | 缩小 $\sim 6$ 倍 |
| 正电子不确定性 | 大 | 缩小 $\sim 2$ 倍 |

## 4.5 关键公式

| 公式 | 出处 | 物理意义 |
|---|---|---|
| — | 反质子拟合公式（附录 E）| $\phi_{\bar{p}}^{\rm sec}(E)$ 的三模型拟合 |
| — | 正电子拟合公式（附录 E）| $\phi_{e^+}^{\rm sec}(E)$ 的三模型拟合 |

## 4.6 关键参数

| 参数 | MIN | MED | MAX | 单位 |
|---|---|---|---|---|
| 反质子背景（10 GeV）| 低 | 中 | 高 | $10^{-7}$ m⁻² s⁻¹ sr⁻¹ GeV⁻¹ |
| 正电子背景（10 GeV）| 低 | 中 | 高 | $10^{-7}$ m⁻² s⁻¹ sr⁻¹ GeV⁻¹ |

## 4.7 潜在问题与值得关注的地方

1. **拟合公式的适用范围**：本文的拟合公式在 $1-100$ GeV 范围内有效，超出此范围需谨慎。

2. **DM 信号 vs 背景的分离**：本文仅提供 astrophysical background——DM 信号计算仍需额外工作。

3. **与 Wechsler et al. 2020 的关系**：本文的参数后验直接来自 Wechsler et al. 2020 的 AMS-02 分析——这是一个独立的传播约束工作。