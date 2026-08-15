> 本章属于：[[01_cosmic-ray-propagation/0002_amato-blasi-2018/literature_analysis/00_overview.md|Cosmic ray transport in the Galaxy: A review（Amato & Blasi 2018）]]
>
> 上一章：[[01_cosmic-ray-propagation/0002_amato-blasi-2018/literature_analysis/03_self_excited_alfven_waves.md|03_self_excited_alfven_waves]]
>
> 下一章：[[01_cosmic-ray-propagation/0002_amato-blasi-2018/literature_analysis/05_near_source_confinement.md|05_near_source_confinement]]
>
> 总览：`00_overview.md`

# 4. Self-Generated Transport — 自生波中的传播

## 4.1 本节核心内容

§4 是本文的理论核心——将 §3 的自激发波理论应用于银河系传播，**推导出扩散系数的刚度依赖**，解释 AMS-02/PAMELA/CREAM 观测到的能谱"断裂"。

关键结论：自激发 Alfvén 波的饱和机制导致 $D(p)$ 在 $\sim 100-1000$ GV 范围内出现**自然断裂**——与观测吻合。

## 4.2 波谱的稳态分布

### 4.2.1 波生长的稳态方程

共振 Alfvén 波的稳态谱由**生长率 = 阻尼率**条件确定：

$$\gamma_{\rm CR}^{\rm RES}(k) = \gamma_{\rm NLD}(k)$$

其中 $\gamma_{\rm NLD}$ 是非线性级联（Non-Linear Damping, NLD）阻尼率。

**NLD 机制**：Kolmogorov 湍流级联——波在 $k$ 空间中的扩散，$D_{kk} \sim k^2 \gamma_{\rm NLD}$。

### 4.2.2 饱和扩散系数的刚度依赖

波的饱和振幅 $\delta B^2/B_0^2 \propto W(k)$，则扩散系数：

$$D(p) \propto \frac{1}{W(k_{\rm res})} \propto k_{\rm res}^\alpha \propto p^\alpha$$

具体幂律取决于阻尼机制：

| 阻尼机制 | $\alpha$ | $D(p)$ 谱 | 适用能量 |
|---|---|---|---|
| NLD 主导（Kolmogorov 级联）| 2 | $D \propto p^2$ | 低能量（$< 100$ GV）|
| IND 主导（离子-中性阻尼）| 1 | $D \propto p$ | 中间能量 |
| 无自生波（背景湍流主导）| $\delta$ | $D \propto p^\delta$ | 高能量（$> 1$ TV）|

> **分析 / Interpretation**：$D(p)$ 在 $\sim 100-1000$ GV 范围内的**幂律指数变化**——这是本文最核心的物理论断。它自然解释了 AMS-02 观测到的"变平"：不是人为加的 break，而是阻尼机制切换的物理后果。

## 4.3 Aloisio & Blasi (2013) 模型

**关键模型**（本文 §4 的核心引用）：

1. **Kolmogorov 背景谱**：$W(k) \propto k^{-5/3}$
2. **自生波叠加**：共振 Alfvén 波的生长与 NLD 阻尼的平衡
3. **两个特征刚度**：
   - $K_1 \sim 100$ GV：NLD 开始主导阻尼
   - $K_2 \sim 1000$ GV：自生波完全饱和，$D \to$ 常数

**传播系数的刚度依赖**：

$$D(p) \propto \begin{cases} p^{\delta} & p < K_1 \quad \text{（背景湍流）} \\ p^2 & K_1 < p < K_2 \quad \text{（NLD 饱和）} \\ \text{const} & p > K_2 \quad \text{（完全自洽）} \end{cases}$$

### 与 AMS-02 数据的对照

Blandford-Eichler 1987 的 $q = 3r/(r-1)$ 给出的是源谱。这里的 $D(p)$ 刚度依赖是**传播阶段**的修正——两者共同决定地球上的观测谱。

**AMS-02 质子谱**（Aguilar et al. 2015a）：

观测谱在 $200-300$ GeV 处变平——与本文模型预测的 $K_1 \sim 100-200$ GV 处 $D(p)$ 从 $\propto p^2$ 过渡到 $\propto$ const 吻合。

> **分析 / Interpretation**：这是本文最有力的观测支持——一个**无需人为调节参数**的物理模型解释了 AMS-02 质子谱的变平。

## 4.4 扩散系数断裂的物理起源

**核心论点**：幂律谱中的"断裂"不应当被视为**唯象参数**，而应当对应**物理尺度的切换**。

| 物理尺度 | 对应刚度 | 观测表现 |
|---|---|---|
| NLD 开始饱和 | $K_1 \sim 100$ GV | B/C 比率变平 |
| 完全自洽饱和 | $K_2 \sim 1000$ GV | 质子谱变平 |

**与"唯象 break"模型的区别**：

- 唯象：在某个 $K$ 处人为加 break，两个幂律拼接
- 物理：$K_1$ 和 $K_2$ 由波生长率与阻尼率的竞争自洽决定

## 4.5 银河风与传播

Ptuskin et al. (1997) 提出：CR 对等离子体的动力学压力可驱动银河风。风的特征速度 $u$ 由 CR 压力梯度决定：

$$u \propto (U_{\rm CR}/\rho)^{1/2}$$

**风对传播的影响**：

- 在晕高度 $z_0 \sim 1$ kpc 处，风从扩散主导过渡到平流主导
- 特征长度 $s^*(p) \propto \sqrt{D(p)}$：在 $z > s^*$ 处平流主导
- 无需显式"自由逃逸边界"——风自然提供截断

**谱特征**：

$$I_a \propto \frac{Q_a}{D(p)^{1/2}} \quad \text{（风模型）}$$

对比标准扩散：$I_a \propto Q_a/D(p)$

> **分析 / Interpretation**：风模型将"晕高 H"从边界条件（自由逃逸边界）转变为动力学结果（风启动高度）——本文主张后者更具物理基础。

## 4.6 源附近的自生波

D'Angelo et al. (2016) 研究了 CR 源附近（$\sim$ pc 尺度）的自生波传播：

**四种 ISM 相场景**：

| 场景 | 中性密度 $n_i$ | 自生波效果 |
|---|---|---|
| 完全电离 | $n_i = 0$ | IND 不存在，自生波完全有效 |
| 部分电离 | $n_i = 0.45$ cm$^{-3}$ | IND 部分抑制 |
| 中性为主 | $n_i \gg$ | IND 完全抑制，自生波不生长 |
| 稀薄电离 | $n_i \ll$ | 接近完全电离 |

**关键结论**：自生波的效果高度依赖于 ISM 相——**中性成分的存在**（通过 IND）可以显著减弱自生波对传播的影响。

## 4.7 关键公式

| 编号 | 公式 | 出处 | 物理意义 |
|---|---|---|---|
| 8 | $\gamma_{\rm CR}^{\rm RES} = p^2 v_A J_{\rm CR}/(c B_0)$ | §3 | 波生长率（§4 用到）|
| 11 | $J_{\rm CR}^{\rm RES} = 4\pi e D p^3/c \cdot \partial\ln f/\partial p$ | §3 | 共振电流 |
| 12 | $D(p) \propto 1/W(k_{\rm res}) \propto p^\alpha$ | §4 | 扩散系数刚度依赖 |
| 18 | $\partial_t W = \gamma_{\rm CR} W - \gamma_{\rm NLD} W$ | §4 | 波谱演化方程 |
| 22 | 源区碎裂克质量 $\Lambda_{\rm src} \sim 0.15$ g/cm$^{2}$ | §4 | D'Angelo et al. 2016 |
| 23 | $s^*(p) \propto \sqrt{D(p)}$ | §4 | 风启动特征长度 |
| 24 | $I_a \propto Q_a / D(p)^{1/2}$ | §4 | 风模型通量公式 |

## 4.8 关键参数

| 参数 | 值 | 出处 |
|---|---|---|
| NLD 特征刚度 $K_1$ | $\sim 100$ GV | §4 |
| 完全饱和刚度 $K_2$ | $\sim 1000$ GV | §4 |
| 风启动高度 $z_0$ | $\sim 1$ kpc | §4 |
| 风速度 | $\sim 100$ km/s | §4 |
| 自生波饱和振幅 | $\delta B/B \sim 0.1-1$ | §4 |
| 源区碎裂克质量 | $\sim 0.15$ g/cm$^{2}$ | §4（D'Angelo 2016）|

## 4.9 作者的逻辑

```
§3 建立自生波理论（共振 + 非共振不稳定性）
→ §4 应用于传播：波生长 = 阻尼 → 饱和谱
→ 饱和谱 → D(p) 的刚度依赖（$K_{1}$、$K_{2}$ 特征刚度）
→ AMS-02 质子变平（200-300 GeV）↔ D(p) 从 p$^{2}$ 过渡到 const
→ 这不是唯象 break，而是阻尼机制切换的物理后果
→ 银河风模型：CR 压力驱动风 → 自然截断
→ 源附近：ISM 相决定自生波效果
```

## 4.10 潜在问题与值得关注的地方

1. **NLD 阻尼率的模型依赖**：本文采用的 NLD 率来自 Aloisio & Blasi (2013)，不同阻尼模型给出不同的 $D(p)$ 谱指数。

2. **IND 的 ISM 相依赖**：如果银河系 ISM 大部分中性，IND 完全抑制自生波，则本文核心论点（D(p) 断裂 = 物理起源）不成立。

3. **风模型的参数空间**：$z_0 \sim 1$ kpc 是模型假设——观测上能否约束风启动高度？

4. **与 Blandford-Eichler 1987 的关系**：B&E 1987 主要处理**源附近**的 DSA，而本文处理**银河系传播**。两者通过 Alfvén 波散射联系起来——但本文的散射是**传播阶段**的，与 B&E 的加速阶段不同。