> 本章属于：[[01_cosmic-ray-propagation/0005_genolini-2021/literature_analysis/00_overview.md|New minimal, median, and maximal propagation models for dark matter searches with Galactic cosmic rays（Génolini et al. 2021）]]
>
> 上一章：[[01_cosmic-ray-propagation/0005_genolini-2021/literature_analysis/01_introduction.md|01_introduction]]
>
> 下一章：[[01_cosmic-ray-propagation/0005_genolini-2021/literature_analysis/03_statistical_method.md|03_statistical_method]]
>
> 总览：`00_overview.md`

# 2. Generalities — 传播理论与 DM 通量标度

## 2.1 本节核心内容

§II 回顾银河系 CR 传播方程、暗物质源项、DM 产生反物质通量对传播参数的解析依赖关系。核心推论：反质子通量 $\propto L^2/K$，正电子通量 $\propto L^{3/2}/K^{1/2}b^{-1/2}$——晕高 $L$ 是决定 min/max 差异的关键。

## 2.2 传播方程

**CR 能量空间传输方程**（公式 1）：

$$-\frac{\partial}{\partial x}(K \frac{\partial a}{\partial x}) - \nabla \cdot (V_c a) - \frac{\partial}{\partial E}\left(\dot{E} a + \frac{\partial}{\partial E}(K_{pp} \frac{\partial a}{\partial E})\right) = Q_a^{\rm prim} + Q_a^{\rm sec} - a \nu_{\rm sink}$$

各项物理：

| 项 | 物理 | 参数 |
|---|---|---|
| $K(E)$ 空间扩散 | 磁场湍流中的粒子扩散 | $K_0$, $\delta$, $R_l$, $\delta_l$ |
| $V_c$ 平流 | 银河风 / 对流 | $V_c$ |
| $\dot{E}$ 能量损失 | 同步辐射 + 逆康普顿 | $\propto E^2$（GeV 以上）|
| $K_{pp}$ 动量扩散 | 再加速（Alfvén 波）| $V_A$（Alfvén 速度）|
| $Q_a^{\rm prim}$ 一级源 | 超新星注入 | 注入谱 |
| $Q_a^{\rm sec}$ 二级源 | 碎裂产生 | 截面 + 密度 |
| $\nu_{\rm sink}$ 汇 | 电离/碎裂损失 | — |

### 2.2.1 三种传播方案

| 方案 | 扩散系数参数化 | 再加速 | 对流 | 自由度 |
|---|---|---|---|---|
| SLIM | $K(E) = K_0 (\beta R/R_1)^\delta (1 + (R_l/R)^\delta_l)^{-1}$ | 无 | 无 | 5 参数 |
| BIG | SLIM + 高能断裂 | 无 | 有 | 7 参数 |
| QUAINT | SLIM + 低能断裂 | 有（Alfvén 波）| 有 | 9 参数 |

### 2.2.2 扩散系数细节

**完整扩散系数**（公式 A1）：

$$K(E) = K_0 \, \beta \left(\frac{R}{R_1}\right)^\delta \left[1 + \left(\frac{R_l}{R}\right)^{\delta_l}\right]^{-1} \left[1 + \left(\frac{R}{R_h}\right)^{\delta_h}\right]^{-1}$$

其中：

| 参数 | 含义 | 典型值 |
|---|---|---|
| $K_0$ | 扩散系数归一化 | $\sim 2 \times 10^{28}$ cm$^{2}$/s |
| $R_1$ | 参考刚度 | 4 GV |
| $\delta$ | 高刚度幂律指数 | $\sim 0.3-0.6$ |
| $R_l$ | 低刚度断裂刚度 | $\sim 3-10$ GV |
| $\delta_l$ | 低刚度断裂指数 | $\sim 1-2$ |
| $R_h$ | 高刚度断裂刚度 | $\sim 10^3-10^5$ GV |
| $\delta_h$ | 高刚度断裂指数 | $\sim 1-2$ |

## 2.3 暗物质源项

**湮灭源**（公式 2）：

$$Q_a(E, \mathbf{x}_s) = \frac{\langle\sigma v\rangle}{2 m^2} \rho^2(\mathbf{x}_s) \frac{dN_a}{dE}$$

其中 $\rho(\mathbf{x})$ 是暗物质质量密度剖面，本文采用 NFW 剖面：

$$\rho(r) = \rho_s \left(\frac{r}{r_s}\right)^{-1} \left(1 + \frac{r}{r_s}\right)^{-2}$$

DM 分布的特征：

| 参数 | 值 | 出处 |
|---|---|---|
| 暗晕尺度半径 $r_s$ | $\sim 20$ kpc | §2 |
| 本地 DM 密度 $\rho_\odot$ | $\sim 0.4$ GeV/cm$^{3}$ | §2 |
| 银心距离 $R_\odot$ | $\sim 8.2$ kpc | §2 |

## 2.4 DM 反质子通量的标度关系

### 2.4.1 晕大小的核心作用

**关键推论**：在 $L \ll R$ 时（即晕高远小于银心距离），反质子通量：

$$\frac{dp}{dE} \propto \frac{L^2}{K(E)} \cdot \rho_\odot^2$$

**物理含义**：通量正比于 CR 在晕中的停留时间 $\tau_{\rm res} \sim L^2/K$——晕越大，粒子停留越久，产生的反质子越多。

> **分析 / Interpretation**：这个简单关系决定了 min/med/max 的核心差异——$L$ 是首要变量。

### 2.4.2 NFW 剖面的级数展开

对于 NFW 剖面（$\gamma = 1$），通量的 $L/R$ 级数展开（公式 8）：

$$\frac{dp}{dE} = \frac{v \, R^2}{4 K(E)} Q_p(E) \sum_{l=1}^{\infty} \left(\frac{L}{R}\right)^{2l} \frac{1}{2l(2l-1)}$$

- $l=1$ 项：$\propto (L/R)^2$——本地贡献
- $l>1$ 项：$L$ 越大，更高阶项越重要——银心热点的贡献增大

## 2.5 DM 正电子通量的标度关系

### 2.5.1 能量损失主导的高能区

正电子与反质子不同——在 GeV 以上，能量损失（同步辐射 + 逆康普顿）主导传播。

**正电子传播尺度**（公式 12）：

$$\ell = \sqrt{4 K / \dot{E}} \approx 0.05 \text{ kpc} \left(\frac{K}{2\times10^{28}\text{ cm}^2/\text{s}}\right)^{1/2} \left(\frac{E}{1\text{ GeV}}\right)^{-1/2}$$

- 当 $E \gg E_1$（能量损失主导）：$\ell \to 0$，通量只依赖本地能量损失率
- 当 $E \ll E_1$（扩散主导）：$\ell \sim L$，通量依赖 $L$

### 2.5.2 正电子通量标度

$$\frac{de^+}{dE} \propto \frac{L^2}{K^{1/2} \dot{E}^{1/2}}$$

对比反质子：$\propto L^2/K$

> **分析 / Interpretation**：正电子对 $K$ 的依赖减半（$K^{1/2}$ vs $K$），因为能量损失提供了一个"截断尺度"，减弱了扩散的影响。

## 2.6 min/med/max 的关键参数

| 方案 | min | med | max | 物理含义 |
|---|---|---|---|---|
| $L$（晕高）| 最小 | 中值 | 最大 | 直接决定停留时间 |
| $K_0$ | 最大（扩散强）| 中值 | 最小（扩散弱）| $L/K$ 固定（B/C 约束）|
| $\delta$（幂律）| 依赖 $L$ | 中值 | 依赖 $L$ | 与 $L$ 有强相关性 |

**核心约束**：$L/K \sim$ 常数（B/C 比率强约束）——$L$ 增大必须伴随 $K$ 等比例增大。

## 2.7 关键公式

| 编号 | 公式 | 出处 | 物理意义 |
|---|---|---|---|
| 1 | 完整 CR 传输方程 | §II | 传播的物理框架 |
| A1 | 扩散系数完整形式 | App. A | 含高低刚度断裂 |
| 2 | DM 湮灭源项 | §II | 暗物质源 |
| — | NFW 剖面 | §II | DM 分布 |
| 4 | $L \ll R$ 时通量 $\propto \rho_\odot$ | §II | 晕高远小于银心距离 |
| 7 | $dp/dE \propto L^2/K$ | §II | **反质子通量标度** |
| 8 | NFW 级数展开 | §II | 通量的 $L/R$ 展开 |
| 10 | 正电子传播尺度 $\ell$ | §II | 能量损失 vs 扩散 |
| 15 | $de^+/dE \propto L^2/(K^{1/2}\dot{E}^{1/2})$ | §II | **正电子通量标度** |

## 2.8 关键参数

| 参数 | 值 | 出处 |
|---|---|---|
| $K_0$（扩散归一化）| $\sim 2\times10^{28}$ cm$^{2}$/s | §II |
| $R_1$（参考刚度）| 4 GV | §II |
| $\delta$（幂律指数）| $\sim 0.3-0.6$ | §II |
| $R_l$（低刚度断裂）| $\sim 3-10$ GV | §II |
| $R_h$（高刚度断裂）| $\sim 10^3-10^5$ GV | §II |
| 暗晕尺度半径 $r_s$ | $\sim 20$ kpc | §II |
| 银心距离 $R_\odot$ | $\sim 8.2$ kpc | §II |
| 本地 DM 密度 | $\sim 0.4$ GeV/cm$^{3}$ | §II |
| 正电子能量损失率 $\dot{E}$ | $\propto E^2$（GeV 以上）| §II |

## 2.9 作者的逻辑

```
CR 传输方程 → 三种传播方案（BIG/SLIM/QUAINT）
→ 扩散系数完整形式（含高低刚度断裂）
→ DM 湮灭源项（NFW 剖面）
→ 反质子通量标度：dp/dE ∝ L$^{2}$/K（晕大小 + 扩散）
→ 正电子通量标度：de$^{+}$/dE ∝ L$^{2}$/(K^{1/2}·É^{1/2})（晕大小 + 扩散 + 能量损失）
→ L/K ~ const（B/C 约束）
→ min/med/max 的差异主要由 L 决定
```

## 2.10 潜在问题与值得关注的地方

1. **$L/K \sim$ 常数的强约束**：B/C 比率对 $L/K$ 的约束如此强，以至于 min/med/max 的 $L$ 差异几乎完全由 $K$ 变化补偿——晕大小本身的不确定性才是暗物质搜寻的关键系统误差。

2. **NFW 级数展开的有效性**：展开假设 $L/R \ll 1$——当 $L \sim 10$ kpc，$R \sim 8.2$ kpc 时，$L/R \sim 1$——级数收敛性存疑。

3. **正电子的能量损失**：本文采用 $b(E) \propto E^2$（同步辐射 + 逆康普顿）——实际能量损失率依赖 ISRF（星际辐射场）密度，仍有不确定性。

4. **与 Amato-Blasi 2018 的关系**：本文采用**唯象**扩散系数参数化（固定幂律 + 断裂），而非 Amato-Blasi 的**物理**模型（自生波阻尼机制切换）。两种方法互补——唯象模型用于实际数据拟合，物理模型用于理解机制。