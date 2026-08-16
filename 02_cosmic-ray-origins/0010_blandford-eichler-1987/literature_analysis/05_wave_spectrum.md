> 本章属于：[[02_cosmic-ray-origins/0010_blandford-eichler-1987/literature_analysis/00_overview.md|Particle Acceleration at Astrophysical Shocks: A Theory of Cosmic Ray Origin（Blandford & Eichler 1987）]]
>
> 上一章：[[02_cosmic-ray-origins/0010_blandford-eichler-1987/literature_analysis/04_test_particle_approximation.md|04_test_particle_approximation]]
>
> 下一章：[[02_cosmic-ray-origins/0010_blandford-eichler-1987/literature_analysis/06_nonlinear_theory.md|06_nonlinear_theory]]
>
> 总览：`00_overview.md`

# 5. Wave Spectrum — 波谱

## 5.1 本节核心内容

§5 讨论**激波处散射宇宙线的 Alfvén 波的生成和相互作用**。散射率（由波振幅决定）决定：

1. **加速效率**——散射越强，扩散系数 $D_\parallel$ 越小，粒子被困在激波附近的时间越长
2. **最高能量**——散射率决定粒子何时逃逸（$r_L > L_{\rm acc}$）

B&E 讨论三种机制：

| 子节 | 主题 | 关键 |
|---|---|---|
| §5.1 | 准线性计算 | 弱湍流极限下的波生长率 |
| §5.2 | 非线性计算 | 强湍流下的波饱和机制 |
| §5.3 | 非共振生长 | 非共振不稳定性 |

## 5.2 原文核心内容

### 5.2.1 散射率与扩散系数

由 §3.4 推导的方位角扩散系数（公式 3.16）：

$$D_{\mu\mu} = \frac{\pi\Omega^2(1-\mu^2)}{2} \frac{W(k_{\rm res})}{B^2}$$

代入空间扩散系数：

$$D_\parallel \propto \frac{v}{B^2 / W(k_{\rm res})}$$

定义无量纲共振波强度：

$$\xi_k \equiv \frac{B_k^2}{B_0^2} = \frac{W(k)}{B_0^2 / 4\pi}$$

则：

$$D_\parallel \propto v \, p^{\,2+\alpha}$$

其中谱形依赖于湍流谱：

- **Kolmogorov** 谱 $W(k) \propto k^{-5/3}$：$D_\parallel \propto v \, p^{-3}$
- **Kraichnan** 谱 $W(k) \propto k^{-3/2}$：$D_\parallel \propto v \, p^{-2}$

> **分析 / Interpretation**：$D_\parallel$ 随 $p$ 的指数决定逃逸时间——Kolmogorov 谱下高能粒子逃逸更快（$p^{-3}$），Kraichnan 谱下略慢（$p^{-2}$）。

### 5.2.2 Alfvén 波自激发

**核心条件**：当 CR streaming 速度超过 Alfvén 速度时，共振 Alfvén 波振幅指数增长：

$$v_{\rm stream} > V_A \implies \gamma_{\rm growth} > 0$$

在激波加速机制中此条件自动满足（CR 速度 $\sim v \gg V_A$）。

**物理机制**：回旋粒子在介电常数高的介质中发射**相干回旋辐射**——这是 Alfvén 波的能量来源。

### 5.2.3 波生长率推导

考虑沿均匀磁场 $B_0$ 传播的右旋圆极化 Alfvén 波：

$$B_1 = B_1 (2 + ij) \, e^{i(kz - \omega t)}$$

在线性化 Vlasov 方程中，对分布函数 $f_0$ 的扰动 $f_1$：

$$\frac{\partial f_1}{\partial t} + \mathbf{v}' \cdot \nabla f_1 + Ze(\mathbf{v}' \times \mathbf{B}_0)\cdot\frac{\partial f_1}{\partial \mathbf{p}} = -Ze(\mathbf{v}' \times \mathbf{B}_1)\cdot\frac{\partial f_0}{\partial \mathbf{p}}$$

在波的参考系中 $\omega' \approx 0$，磁场静止，电场消失（近似）。粒子仅被散射（方位角变化），能量不变。

**共振电流**（Plemelj 公式）：

$$j_{\rm res} = \frac{2Ze}{k} \int dp' (1-\mu'^2) \frac{dp'}{dp'} p'^2 v' \delta(p'k v' - \Omega)$$

**生长率**：

$$\gamma = \frac{\pi\Omega^2}{2} \frac{\partial f_0 / \partial p}{k^2} \bigg|_{k v_\parallel = \Omega}$$

若 $\partial f_0 / \partial p < 0$（分布随 $p$ 下降），且 $f_0$ 在 $v_{\rm stream} > V_A$ 处有足够强的梯度，则 $\gamma > 0$——波增长。

### 5.2.4 §5.2 非线性计算

当波振幅增长到非线性水平（$\xi_k \sim 1$），准线性理论失效。非线性机制包括：

1. **粒子镜像效应**：粒子被非线性波反射，改变散射率
2. **波-波相互作用**：Alfvén 波之间的非线性耦合
3. **饱和机制**：生长率降至零

B&E 指出：对于足够强的激波，**波振幅必然达到非线性水平**。

### 5.2.5 §5.3 非共振生长

除共振不稳定性外，还存在**非共振不稳定性**（如 Weibel 不稳定性）——这些在特定条件下可能比共振不稳定性更重要。

## 5.3 关键公式

| 编号 | 公式 | 出处 | 物理意义 |
|---|---|---|---|
| 5.1 | $D_\parallel \propto v \, p^{\,2+\alpha}$ | §5.1 | 扩散系数与波谱的关系 |
| — | Kolmogorov：$D_\parallel \propto v \, p^{-3}$ | §5.1 | Kolmogorov 谱下的扩散 |
| — | Kraichnan：$D_\parallel \propto v \, p^{-2}$ | §5.1 | Kraichnan 谱下的扩散 |
| 5.2 | 线性化 Vlasov 方程（波场中）| §5.1 | 波生长率的起点 |
| — | $\gamma \propto (\partial f_0 / \partial p)\big\big|_{kv_\parallel = \Omega}$ | §5.1 | 共振生长率 |
| 5.4 | $j_\perp = Ze \int d\mathbf{p}' f_1 v'_\perp$ | §5.1 | 垂直电流 |
| 5.6 | Plemelj 共振贡献 | §5.1 | 共振电流的提取 |

## 5.4 关键参数

| 参数 | 值 | 说明 |
|---|---|---|
| 波振幅非线性阈值 | $\xi_k \sim 1$ | 准线性理论失效 |
| 自激发条件 | $v_{\rm stream} > V_A$ | 自动满足（$v \gg V_A$）|
| 共振波波长 | $\lambda \sim 2\pi r_L$ | 粒子 Larmor 半径 |
| 生长率 | $\gamma \propto \Omega (n_{\rm cr}/n_{\rm bg})$ | 取决于 CR 数密度 |
| 扩散谱指数 | $-3$（Kolmogorov）/ $-2$（Kraichnan）| 取决于湍流谱 |

## 5.5 作者的逻辑

```
散射率决定加速效率 + 最高能量
→ 波谱决定散射率（$D_\parallel \propto 1/W$）
→ 弱湍流：准线性理论给出散射率（$D_\parallel \propto p^{-3}$）
→ 自激发：CR streaming 产生 Alfvén 波（生长率 $\gamma$）
→ 强湍流：非线性效应主导，波饱和
→ 非共振不稳定性（补充机制）
```

## 5.6 我的理解

> **分析 / Interpretation**：§5 的核心问题是——**DSA 所需的 Alfvén 波从哪里来？** B&E 的答案是：CR 自身产生的。CR streaming 激发 Alfvén 波，Alfvén 波散射 CR，CR 被加速——这是一个**自洽的反馈回路**。

但准线性理论的局限（小振幅、随机相位、$k \parallel B$）在强激波中可能全部违反——§5.2 的非线性计算和 §6 的自洽处理就是为了解决这个。

### 与 BO 1978 的对比

BO 1978 §III 也讨论了自激发，但只是定性估算。B&E §5 给出了**完整的准线性波生长率推导**——从线性化 Vlasov 方程出发，到 Plemelj 公式提取共振贡献，到生长率 $\gamma$ 的表达式。这是 DSA 理论中关于"散射源"最详细的处理之一。

## 5.7 潜在问题与值得关注的地方

1. **准线性理论的自洽性问题**：$D_\parallel$ 依赖于 $W(k_{\rm res})$，$W$ 由 CR 自激发，CR 分布又由 $D_\parallel$ 决定——这是一个**非线性闭环**。§6 的自洽处理就是为了解决此问题。

2. **$\mu = 0$ 盲区的散射**：准线性理论在 $\mu \to 0$ 失效。如果粒子无法在 $\mu = 0$ 附近被散射，就无法在激波两侧反复穿越——DSA 不成立。§5 未完全解决此问题。

3. **Kolmogorov vs Kraichnan 的选择**：观测上 ISM 湍流谱更接近 Kraichnan，但 B&E 未给出明确选择。