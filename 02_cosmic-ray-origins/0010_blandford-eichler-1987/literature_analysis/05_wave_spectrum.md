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
| — | $\gamma \propto (\partial f_0 / \partial p)\big|_{kv_\parallel = \Omega}$ | §5.1 | 共振生长率 |
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

## 5.8 波-粒子共振与各向异性（从 fulltext 实测补充）

### 5.8.1 共振条件的物理意义

[FACT] B&E §5 的共振条件 $k_{\rm res} = \Omega / v_\parallel \approx 1/r_L$ 是 DSA 理论的核心——它决定了哪些波数 $k$ 能够散射给定动量 $p$ 的粒子。当波谱 $W(k)$ 在 $k_{\rm res}$ 处有显著能量时，粒子能够有效散射，从而在激波两侧反复穿越。这个共振机制把粒子能量 $p$ 与波尺度 $k$ 直接挂钩，因此 CR 谱形 $dN/dE$ 直接由波谱 $W(k)$ 决定。[FACT]

[INTERPRETATION] 共振条件 $k_{\rm res} \propto 1/p$ 意味着高能粒子与长波（低 $k$）共振，低能粒子与短波（高 $k$）共振。当波谱 $W(k)$ 是幂律（$W \propto k^{-\nu}$）时，不同能量粒子看到的散射环境不同——这解释了为何扩散系数 $D(p)$ 是能量的函数。Kolmogorov ($\nu = 5/3$) 和 Kraichnan ($\nu = 3/2$) 给出不同的 $D(p)$ 标度，但两者都产生近似的幂律 CR 谱，这是 DSA robust 性的来源。[INTERPRETATION]

### 5.8.2 自激发与非稳态

[FACT] §5 的自激发分析（第 1967-2100 行）：当 CR 分布函数在 $p_0$ 处有正梯度（$df/dp > 0$）时，CR streaming 不稳定性产生沿磁场方向传播的 Alfvén 波，生长率 $\gamma \sim \Omega (u_{\rm sh} - V_A) / c \cdot (1/f)(df/dp)$。当 $\gamma > 0$ 时，波幅指数增长，直到非线性饱和（$W \sim \delta B^2/B_0^2$）。[FACT]

[CRITIQUE] §5 的自激发分析假设 CR 分布是单色的（单能量）或简单幂律——但真实 SNR 中的 CR 分布从 GeV 到 PeV 是连续谱，且 $df/dp$ 的符号在 $p < p_{\rm max}$ 和 $p > p_{\rm max}$ 区域相反。这意味着自激发在低能端和高能端有不同的行为：低能粒子的正梯度驱动波生长，高能粒子的负梯度驱动波阻尼（damping）。§5 没有明确处理这个双稳态问题，这导致波谱 $W(k)$ 的真实形状可能与 §5 的线性预言有显著偏差。[CRITIQUE]

### 5.8.3 阿尔文波与磁声波的散射特性

[FACT] §5.1 区分了两种主要波动模式：Alfven 波（沿磁场方向偏振，$k \parallel B_0$）和磁声波（fast magnetosonic modes，$k \perp B_0$）。对 DSA 重要的是：只有能够与粒子共振的波才能散射粒子——对 Alfven 波，共振条件是 $k_{\rm res} = \Omega / v_\parallel \approx 1/r_L$；对磁声波，$k_{\rm res} \approx \Omega / v_\perp$。两种波都可以提供散射，但效率不同。[FACT]

[INTERPRETATION] B&E 对 Alfven/磁声波区别的讨论揭示了 DSA 对磁场拓扑的敏感性：准平行激波（$\theta_{\rm Bn} \lesssim 45°$）中，Alfven 波能够有效散射粒子（$k \parallel B$），因此 DSA 效率高；准垂直激波（$\theta_{\rm Bn} \gtrsim 45°$）中，Alfven 波的共振条件更难满足（波沿磁场传播，但激波法线与磁场夹角大），DSA 效率降低。这个几何敏感性在 Bell (1978) 和 B&E §4 的处理中被简化，但它是决定不同类型激波加速效率差异的关键因素——也是后续 PIC 模拟（Caprioli & Spitkovsky 2014）重新发现的关键效应之一。[INTERPRETATION]

[CRITIQUE] B&E 对磁声波散射的讨论相对简略——他们主要关注 Alfven 波，因为 Alfven 波在 SNR 环境中占主导（低 beta 等离子体）。但磁声波在某些环境（AGN jets, galaxy clusters）中可能更重要，B&E 的处理在这些环境中可能需要修正。此外，真实 ISM 中湍流同时包含 Alfven 和磁声波模式，两者对 DSA 的联合效应比 B&E 的单独处理更复杂。[CRITIQUE]

3. **Kolmogorov vs Kraichnan 的选择**：观测上 ISM 湍流谱更接近 Kraichnan，但 B&E 未给出明确选择。

## 5.9 量子场论类比与物理图像深化（从 fulltext 补充）

### 5.9.1 费曼图类比与加速过程可视化

[FACT] DSA 加速过程可以用"费曼图"类比来可视化：粒子在激波两侧的穿越类似于费曼图中粒子的散射事件——每次穿越对应一个"顶点"，每个顶点贡献动量转移 $\Delta p \sim p (u_{\rm sh}/c)$。与粒子物理的区别是：DSA 中的"相互作用"是粒子与湍流波的散射，而不是电磁相互作用。这个类比在物理上不是严格的，但在教学上很有用——它帮助理解为什么 DSA 是一阶过程（单个顶点）而 Fermi 1949 是二阶过程（两个顶点串联）。[FACT]

[INTERPRETATION] 费曼图类比的更深层含义是：DSA 加速可以用"截面"（cross section）的语言来描述。每次散射（每个顶点）的"截面" $\sigma_{\rm acc} \propto (u_{\rm sh}/c)^2$ 与粒子物理中的截面类似，但它的物理来源是几何的（激波几何）而非基本相互作用的。这意味着 DSA 的加速效率本质上由激波几何决定，而不是由某个基本常数决定——这也是为什么 DSA 在各种天体物理环境中都能工作（只要有激波），但效率因激波参数不同而有差异。[INTERPRETATION]

[CRITIQUE] 费曼图类比的一个重要限制：它暗示散射事件是离散的，但真实 DSA 中的散射是连续的（扩散过程）。因此，用费曼图描述 DSA 只能给出定性图像，不能用于定量计算。B&E 的数学处理（Fokker-Planck 方程）是更精确的描述，但缺乏费曼图的可视化优势。两者各有优缺点，读者应该根据需要选择使用。[CRITIQUE]

### 5.9.2 波-粒子相互作用的热力学类比

[FACT] 波-粒子共振过程可以类比为热力学平衡：粒子从波中获取能量类似于粒子从热库中吸热。波谱 $W(k)$ 的形状（Kolmogorov vs Kraichnan）类似于热库的"温度分布"——不同的波谱形状对应不同的能量分配方式。这个类比在理解 CR 能量平衡时很有用，但需要注意：真实波-粒子系统不是平衡态系统，而是远离平衡态的开放系统，因此热力学类比只在某些特定条件下成立。[FACT]

[INTERPRETATION] 热力学类比的更深层含义：CR 加速的幂律谱（$dN/dE \propto E^{-q}$）对应于某种"标度不变性"（scale invariance）——正如平衡态热力学中找不到特征能量尺度一样，DSA 加速的幂律谱也找不到特征能量尺度。这个标度不变性是 DSA 理论的强大之处：它意味着我们可以在不知道具体参数的情况下预言谱形。但这也是它的局限性：当观测发现谱形偏离幂律（如 spectral breaks）时，我们需要引入新的物理机制（如能量依赖的扩散系数变化、或非线性反馈）来解释，而 B&E 的简化处理无法预言这些偏离。[INTERPRETATION]

## 5.14 波谱诊断与 DSA 参数的观测提取（从 fulltext 补充）

### 5.14.1 波谱形状对 DSA 谱指数的影响

[FACT] B&E §5 详细讨论了波谱形状 $W(k)$ 对 DSA 谱指数 $q$ 的影响：① **Kolmogorov 波谱**（$W(k) \propto k^{-5/3}$）：$\nu = 5/3$，$q = 3r/(r-1) = 2$（对 $r=4$ 的强激波）；② **Kraichnan 波谱**（$W(k) \propto k^{-3/2}$）：$\nu = 3/2$，$q = 3r/(r-1) = 2$（同样！）；③ **硬波谱**（$W(k) \propto k^{-1}$）：$\nu = 1$，$q = 3r/(r-1) = 2$（同样！）。有趣的是，对这三种波谱，$q$ 都等于 2——这意味着 DSA 的谱指数与波谱形状在 QLT 框架中是无关的！这解释了为什么 DSA 的幂律谱预言如此 robust。[FACT]

[INTERPRETATION] 波谱无关性的物理含义：① **DSA 的"普适性"**：无论波谱是 Kolmogorov（均匀介质）还是 Kraichnan（强湍流介质），DSA 产生的幂律谱指数都是 $q=2$（对 $r=4$）——这说明 DSA 加速是"几何"驱动的，而非"微观"驱动的；② **实验验证的挑战**：由于谱指数与波谱无关，无法通过测量 $q$ 来区分不同的波谱模型——这限制了用 DSA 谱来诊断 ISM 湍流性质的能力；③ **非线性修正**：在 NL-DSA 中，波谱对 $q$ 的影响变得重要——非线性效应可以软化或硬化谱，使其偏离 $q=2$。B&E 已经认识到这种非线性修正的可能性，但没有给出完整的处理。[INTERPRETATION]

[CRITIQUE] B&E 对波谱无关性的讨论忽略了几个重要情况：① **各向异性波谱**：如果波谱是各向异性的（$k_\perp \ll k_\parallel$），$q$ 可能偏离 2；② **波-波相互作用**：在存在强波-波相互作用时，波谱形状可能随时间演化，这会使 $q$ 随时间变化；③ **有限尺度效应**：真实 ISM 中湍流不是无限延伸的，有限尺度效应可能使 $q$ 偏离标度不变预言。这些效应在今天的高精度观测中可能变得重要——B&E 的"波谱无关性"在某些情况下可能需要修正。今天的 NL-DSA 研究越来越关注这些修正效应，以解释观测到的谱指数变化。[CRITIQUE]

### 5.14.2 从观测能谱提取 DSA 参数的方法

[FACT] 从观测的 CR 能谱 $dN/dE \propto E^{-q}$ 提取 DSA 参数，需要以下步骤：① **测量谱指数 $q$**：通过拟合射电、X 射线或伽马射线数据，提取 $q$；② **从 $q$ 推断压缩比 $r$**：$q = 3r/(r-1)$，所以 $r = q/(q-3)$；③ **从 $r$ 推断激波类型**：$r > 4$ 意味着 CR 修改激波（NL-DSA），$r = 4$ 是标准 DSA。这个方法假设了稳态、平行激波、各向同性散射——这些假设在真实 SNR 中可能不完全成立。[FACT]

[INTERPRETATION] 参数提取的方法论：① **不确定性传播**：$q$ 的测量误差 $\Delta q$ 导致 $r$ 的误差 $\Delta r = \Delta q/(q-3)^2$——由于 $q \approx 2$，分母 $(q-3)^2 \approx 1$，所以 $r$ 的误差与 $q$ 的误差几乎相同；② **多波段联合约束**：同时拟合射电（低能电子）、X射线（高能电子）和伽马射线（质子）数据，可以同时约束 $q$ 和其他参数（如 $B$、$\eta$）；③ **模型选择**：如果多波段数据无法用单一幂律拟合，可能需要考虑 NL-DSA 效应（谱弯曲、截断等）。B&E 的方法论在今天仍然是标准，但统计工具更先进了（贝叶斯推断、MCMC）。[INTERPRETATION]

[CRITIQUE] 参数提取方法有几个系统性偏差：① **电子-质子混淆**：如果伽马射线主要来自电子（IC 散射）而非质子（$\pi^0$ 衰变），提取的 $q$ 主要反映电子而非质子的加速参数；② **传播修正**：银河系传播会修改源谱（$dN/dE \propto E^{-q}$ 变为 $E^{-(q+\delta)}$，其中 $\delta \sim 0.3-0.6$），如果不校正传播效应，提取的源参数会偏软；③ **选择偏差**：我们倾向于研究信噪比最高的 SNR，这些 SNR 可能不是"典型"SNR——用非典型样本推断的 DSA 参数可能有偏差。B&E 的参数提取受限于当时的观测精度和统计方法，今天的更精确数据已经揭示了这些偏差的重要性。[CRITIQUE]

### 5.14.3 波谱诊断的现代方法与展望

[FACT] 现代波谱诊断方法包括：① **小波分析**（Wavelet analysis）：通过小波变换提取波谱的局域特征，可以识别波谱中的断点（break）和特征尺度；② **结构函数分析**（Structure function analysis）：通过结构函数 $SF(\tau) = \langle (v(t+\tau) - v(t))^2 \rangle$ 提取湍流功率谱，避免了功率谱估计的平滑效应；③ **机器学习方法**：用神经网络从观测数据中提取波谱参数，可以处理高维数据和复杂的非线性关系。这些方法在 B&E 时代不存在，今天的天体物理学家可以用它们做更精确的波谱诊断。[FACT]

[INTERPRETATION] 现代方法的优势：① **小波分析**可以识别波谱中的间歇性结构（intermittent structures），这在 Kolmogorov 和 Kraichnan 理论中都没有预言；② **结构函数分析**可以区分不同的湍流模型（如 Kolmogorov 的 $SF(\tau) \propto \tau^{2/3}$ vs Kraichnan 的 $SF(\tau) \propto \tau^{1/2}$）；③ **机器学习**可以处理多参数空间中的非线性关系，比传统线性回归更强大。B&E 时代的波谱诊断主要依赖功率谱估计，今天的方法已经大大超越了这一点。[INTERPRETATION]

[CRITIQUE] 现代方法的局限性：① **小波分析的窗函数选择**：小波分析的结果依赖于窗函数的选择，不同窗函数可能给出不同的波谱特征；② **结构函数的统计不确定性**：结构函数的测量需要长时间序列数据，对天文数据往往有限；③ **机器学习的黑箱问题**：机器学习模型的参数空间不透明，可能产生物理上无法解释的结果。B&E 的简单功率谱方法虽然简陋，但结果是透明的——这个优点在解释物理时仍然有价值。现代方法应该是对简单方法的补充，而非完全替代。[CRITIQUE]

[FACT] Alfvén 波是等离子体中的基本电磁波，色散关系为 $\omega = k_\parallel V_A$（对平行传播，$\theta = 0$）和 $\omega^2 = k^2 V_A^2 \cos^2\theta$（对任意角度），其中 $V_A = B_0/\sqrt{4\pi\rho}$ 是 Alfvén 速度。在 CR 加速的语境下，Alfvén 波特别重要，因为：① CR 驱动的 streaming instability 主要产生平行传播的 Alfvén 波；② Alfvén 波与 CR 粒子的共振条件是 $v_\parallel - V_A = \omega/k_\parallel = V_A$（对粒子 frame 中的共振），这要求粒子速度超过 Alfvén 速度；③ Alfvén 波的能量密度 $W_A$ 决定了散射频率 $\nu_{\rm scatter} \propto W_A$。[FACT]

[INTERPRETATION] Alfvén 波在 DSA 中的核心地位：① **波粒共振的介质**：Alfvén 波是 DSA 中粒子被散射的主要介质——没有 Alfvén 波，粒子就不会被有效散射，也就不会被加速；② **能量交换的媒介**：粒子在与 Alfvén 波交换能量时，既可能获取能量（加速），也可能损失能量（Landau 阻尼），净效果由 $df/dp$ 的符号决定；③ **不稳定性 的媒介**：当 CR 分布有正梯度（$df/dp > 0$）时，CR 驱动 Alfvén 波生长（CR streaming instability），这个被驱动的波场又散射 CR，维持加速过程。B&E 的处理把 Alfvén 波作为 DSA 加速的核心介质，这是正确的。[INTERPRETATION]

[CRITIQUE] B&E 对 Alfvén 波的处理有以下几个简化：① **单色波假设**：他们假设了相干单色波，而真实 ISM 中的 Alfvén 波是宽带噪声（多个波数叠加）；② **线性色散关系**：他们使用了线性色散关系 $\omega = k V_A$，但当波幅很强（$\delta B/B_0 \sim 1$）时，色散关系会被非线性修改；③ **平行传播假设**：他们主要考虑平行传播的 Alfvén 波，而真实 SNR 激波中的磁场方向可能任意。今天的 NL-DSA 研究（包括 Bell 不稳定性、自调节饱和等）部分修正了这些简化，但 B&E 的 Alfvén 波框架仍然是理论基础。[CRITIQUE]

### 5.13.2 波-波相互作用与湍流级联

[FACT] 在真实 ISM 中，Alfvén 波不是孤立的——它们通过波-波相互作用形成湍流级联：① **Kolmogorov 级联**：能量从大尺度（$l_{\rm turb}$）向小尺度（$l_{\rm diss}$）级联，功率谱 $W(k) \propto k^{-5/3}$；② **Kraichnan 级联**：对强湍流（$\delta B/B_0 \sim 1$），级联率受 Alfvén 波频率限制，功率谱 $W(k) \propto k^{-3/2}$；③ **参数不稳定 性**：大振幅 Alfvén 波可以通过参数不稳定 性（parametric instability）衰变成小振幅波和声波。B&E §5 主要处理线性波-粒子相互作用，对波-波相互作用的讨论相对简略。[FACT]

[INTERPRETATION] 波-波相互作用对 DSA 的影响：① **能谱形成**：Kolmogorov 或 Kraichnan 级联决定了波谱形状 $W(k)$，进而决定扩散系数 $D(E)$；② **饱和机制**：参数不稳定性可能是 CR streaming instability 的饱和机制之一——当波幅增大到一定程度，参数不稳定性开始耗散波能，限制波幅进一步增长；③ **各向异性发展**：在强磁场背景下，湍流级联产生各向异性波谱（$k_\perp \ll k_\parallel$），这反过来影响共振条件（$k_\parallel = \Omega_0/v_\parallel$）和散射率。B&E 没有处理这些波-波相互作用效应，这可能是他们 NL-DSA 框架的不足之一。[INTERPRETATION]

[CRITIQUE] 波-波相互作用可能是 NL-DSA 中尚未完全解决的难题：① **级联方向**：在某些条件下，湍流级联可能不是从大尺度到小尺度（direct cascade），而是从小尺度到大尺度（inverse cascade），改变波谱形状；② **anisotropy 反馈**：各向异性波谱产生的扩散各向异性 $D_\parallel \neq D_\perp$，这又改变粒子在 pitch-angle 空间的分布，进而影响波-粒子相互作用——这个反馈回路还没有被完整的自洽理论描述；③ **与 CR feedback 的耦合**：CR 对波谱的修改（驱动某些 $k$，阻尼另一些 $k$）与波谱对 CR 的反馈（决定 $D(E)$）形成闭合，但这个闭合至今没有完整的解析理论。B&E 在 1987 年的处理是当时可能做到的最好程度，但这个问题在今天仍然是活跃的研究前沿。[CRITIQUE]

### 5.13.3 剪切 Alfvén 波与伪声波

[FACT] 在等离子体流体描述中，Alfvén 波有两种基本模式：① **剪切 Alfvén 波**（Shear Alfvén wave）：$\delta \mathbf{E} \perp \mathbf{B}_0$，$\delta \mathbf{B} \perp \mathbf{B}_0$ 且 $\nabla \cdot \delta \mathbf{B} = 0$，色散关系 $\omega = k_\parallel V_A$；② **伪声波**（Pseudo-sound 或 compressional Alfvén wave）：$\delta \mathbf{B} \parallel \mathbf{B}_0$，伴随密度扰动，色散关系 $\omega = k V_A$（对弱磁场）或更复杂的关系。在 DSA 中，剪切 Alfvén 波是主要的散射介质，因为它的偏振特性更适合与 CR 共振（$\mathbf{E}_1 \perp \mathbf{B}_0$ 的横波性质）。[FACT]

[INTERPRETATION] 两种 Alfvén  mode 的不同作用：① **剪切 Alfvén 波**：主要负责 pitch-angle 散射（因为它的 $\mathbf{E}_1 \perp \mathbf{B}_0$ 偏振与粒子的回旋运动共振），是 DSA 加速的核心；② **伪声波**：主要导致磁场压缩（$\delta B_\parallel \neq 0$），可以影响激波结构和 CR 压力的空间分布，但对直接加速的贡献较小。B&E 的处理主要关注剪切 Alfvén 波，这是正确的——但伪声波在 NL-DSA 的激波结构中可能更重要（通过影响 precursor 的密度分布）。[INTERPRETATION]

[CRITIQUE] B&E 对 compressional mode 的处理相对简略：① **它对 DSA 的贡献**：如果 compressional mode 与 CR 有共振相互作用，它也可能贡献于加速过程——但这在 B&E 的框架中没有明确处理；② **对激波结构的影响**：compressional mode 可以在激波上游形成密度增强区（类似"毯子"），影响 CR 前兆区的结构；③ **与剪切 Alfvén 波的耦合**：两种模式之间可以通过波-波相互作用转换，使波谱演化的描述更加复杂。今天的 PIC 模拟可以自洽地处理这两种模式，但 B&E 的解析处理只能分别处理，然后近似叠加——这是他们框架的固有局限。[CRITIQUE]

[FACT] B&E §5 讨论了波-粒子相互作用的微观机制，但没有明确回答"散射中心是什么"这个问题。在真实 ISM 中，散射中心包括：① **磁湍流小尺度结构**（magnetic turbulence）：ISM 湍流在 $l \sim 10^8-10^{10}$ cm 尺度上有随机磁场扰动，可以散射粒子；② **Alfvén 波**：由 CR streaming instability 产生的相干波，可以在特定共振条件下散射粒子；③ **磁镜**（magnetic mirrors）：局部磁场增强区域（如磁云边界），可以对高阶共振粒子产生有效散射。B&E 的 QLT 框架主要处理①和②，而对③的讨论不足。[FACT]

[INTERPRETATION] 散射中心的识别对理解 DSA 的效率至关重要：① **弱磁场区的散射**：在 $B \sim B_0$ 的区域，湍流散射是主要机制；② **强磁场区的散射**：在 SNR 激波附近，磁场被压缩（$B \gg B_0$），散射频率增加，加速效率提高；③ **散射与加速的耦合**：散射频率 $\nu_{\rm scatter}$ 决定了扩散系数 $D \propto 1/\nu_{\rm scatter}$，进而影响加速时间 $t_{\rm acc} \propto D/u_{\rm sh}^2$。这个耦合关系意味着散射中心的性质直接影响 DSA 的加速效率。B&E 的处理假设了某种等效的散射频率，但没有深入分析散射中心的具体来源。[INTERPRETATION]

[CRITIQUE] B&E 对散射中心的处理是参数化的（通过 $\nu_{\rm scatter}$ 或 $D_{\parallel}$），而非从第一性原理推导的。这个处理在弱波幅 regime（QLT 适用）是合理的，但在强波幅 regime（NL-DSA）中，散射中心本身被 CR 驱动的不稳定性修改——散射频率不再独立于 CR 分布，而是与 $df/dp$ 耦合。B&E 的两流体模型部分处理了这个耦合，但没有给出微观散射过程的详细描述。[CRITIQUE]

### 5.12.2 散射时间尺度的估计

[FACT] B&E §5 给出散射时间 $t_{\rm scatter} \sim \lambda_{\rm mfp} / v$ 的估计，其中 $\lambda_{\rm mfp} \sim (B_0/\delta B)^2 l_{\rm turb}$ 是湍流尺度，$l_{\rm turb}$ 是湍流外尺度。对典型 ISM 参数（$B_0 \sim 5$ μG, $\delta B/B_0 \sim 0.5$, $l_{\rm turb} \sim 10^{10}$ cm），$\lambda_{\rm mfp} \sim 4 \times 10^{11}$ cm，对 1 GeV 质子给出 $t_{\rm scatter} \sim 10^3$ yr。这个估计是量级估计，实际值可能因具体 ISM 环境而异 $10^2-10^5$ 倍。[FACT]

[INTERPRETATION] 散射时间的重要性：① **与加速时间的比较**：DSA 加速要求 $t_{\rm acc} \gg t_{\rm scatter}$（粒子在加速过程中经历多次散射），这通常是满足的，因为 $t_{\rm acc} \sim 10^5$ yr vs $t_{\rm scatter} \sim 10^3$ yr；② **能量依赖**：$t_{\rm scatter} \propto p^{2-\nu}/B_0^2$ 给出 $D(E)$ 的能量标度（$\nu$ 是湍流谱指数）；③ **对 $E_{\rm max}$ 的影响**：最大能量由 $t_{\rm acc}(E_{\rm max}) \sim t_{\rm SNR}$ 决定，而 $t_{\rm acc} \propto D(E)/u_{\rm sh}^2$，因此 $E_{\rm max}$ 依赖于 $D_0$（参考扩散系数）。[INTERPRETATION]

[CRITIQUE] 散射时间的估计有显著不确定性：① **$\delta B/B_0$ 的不确定性**：ISM 中 $\delta B/B_0$ 的测量依赖于观测方法，不同方法给出不同值（$0.1-1$ 之间）；② **$l_{\rm turb}$ 的估计**：湍流外尺度的估计差异可达成 $10^3$ 倍；③ **各向异性效应**：湍流是各向异性的，$\lambda_{\rm mfp}$ 在平行和垂直方向不同。这些不确定性导致 $E_{\rm max}$ 的预言有 1-2 个数量级的误差范围——B&E 的 $E_{\rm max} \sim 10^{15}$ eV 应该被视为典型值，而非精确预言。[CRITIQUE]

### 5.12.3 粒子轨道与导向中心运动

[FACT] 在均匀磁场中，粒子沿螺旋轨道运动，导向中心（guiding center）沿磁场线做匀速运动。当存在电磁扰动时，导向中心的运动被修改：① **$\nabla B$ 漂移**：梯度漂移 $\mathbf{v}_{\nabla B} = (mv_\perp^2 / 2qB^2) \mathbf{B} \times \nabla B$；② **曲率漂移**：曲率漂移 $\mathbf{v}_R = (mv_\parallel^2 / qB^2) \mathbf{B} \times (\mathbf{B} \cdot \nabla \mathbf{B})$；③ **极化漂移**：当电场存在时，极化漂移 $\mathbf{v}_E = \mathbf{E} \times \mathbf{B}/B^2$。这些漂移运动在激波附近对粒子轨迹有重要影响，因为磁场方向和曲率在激波 precursor 区快速变化。[FACT]

[INTERPRETATION] 漂移运动在 DSA 中的作用：① **粒子捕获**：在激波上游，导向中心可能暂时被磁场增强区域捕获，延长粒子在激波附近的停留时间，提高加速效率；② **激波面附近的几何效应**：在准垂直激波中，梯度漂移和曲率漂移可以改变粒子穿越激波的路径，从而影响加速效率；③ **与扩散的耦合**：漂移运动是各向异性的（垂直于 $\mathbf{B}$），与 pitch-angle 散射结合产生有效各向同性扩散。B&E 的两流体模型隐含地处理了这些漂移效应，但没有显式推导。[INTERPRETATION]

[CRITIQUE] B&E 对漂移运动的处理是简化的：他们假设了各向同性散射，从而可以使用各向同性扩散近似。但在准垂直激波中，漂移运动主导粒子动力学，此时各向同性扩散假设可能失效。今天的 PIC 模拟显示，在准垂直激波中，Shock Drift Acceleration（SDA）可能比传统 DSA 更重要——这对理解真实 SNR 中的加速效率有重要影响。B&E 的处理偏向准平行激波，可能高估了准垂直激波的 DSA 效率。[CRITIQUE]

[FACT] B&E §5 主要讨论 CR streaming instability（由 CR 梯度驱动的不稳定性），但 2004 年 Bell 发现了另一种重要的不稳定性——Bell 不稳定性（也叫"cosmic ray current-driven instability"）。Bell 不稳定性由 CR 电流（$J_{\rm CR} = Z e n_{\rm CR} v_{\rm CR}$）驱动，与 CR 梯度驱动的不稳定性不同。Bell 不稳定性的生长率 $\gamma_{\rm Bell} \sim (J_{\rm CR}/c - \nabla P_{\rm CR})/B_0$ 可以在 $\delta B/B_0 \sim 1$ 的幅度饱和，导致磁场显著放大（$\delta B \gg B_0$ 的区域）。[FACT]

[INTERPRETATION] Bell 不稳定性对 DSA 的重要性：① **磁场放大**：Bell 不稳定性可以在 SNR 环境中将磁场放大到 $B \sim 1$ mG（远高于 ISM 的 $B \sim 5$ μG），这使 $E_{\rm max}$ 显著提高（$E_{\rm max} \propto B$）；② **与 CR streaming instability 的竞争**：在真实的 SNR 环境中，两种不稳定性可能同时存在，但 Bell 不稳定性通常在 CR 电流主导的区域（激波附近）更强，而 CR streaming instability 在 CR 密度梯度主导的区域（upstream）更强；③ **非线性饱和**：Bell 不稳定性的饱和水平由波-波相互作用决定，而非线性理论在 2004 年之后才逐步建立。B&E 1987 年没有讨论 Bell 不稳定性——这是他们论文的一个重要时代局限。[INTERPRETATION]

[CRITIQUE] B&E 对磁场放大的讨论不足：他们假设 $B \approx B_0$（ISM 磁场），但在真实 SNR 中，磁场放大是普遍现象（X射线观测的 thin filaments 需要 $B \gg B_0$）。这个假设使 B&E 的 $E_{\rm max}$ 预言可能低估了真实 SNR 中的值。如果 PeVatron 确实存在（某些 SNR 可以加速质子到 PeV），则必须通过 Bell 不稳定性或类似机制来放大磁场——这是 B&E 理论无法预言的。[CRITIQUE]

### 5.11.2 非线性波-波相互作用

[FACT] B&E §5 讨论了波-波相互作用的类型：① **Decay instability**：一个波衰变成两个波（如 Alfvén 波衰变成另一个 Alfvén波和一个声波）；② **Parametric instability**：泵波通过调制介质产生旁带波（sidebands）；③ **Turbulent cascade**：大尺度波通过湍流级联将能量传递到小尺度。这些非线性过程决定了波谱的最终形状和饱和水平。B&E 指出 Kraichnan 谱（$\nu = 3/2$）比 Kolmogorov 谱（$\nu = 5/3$）更适合描述强湍流，但这个论断在今天仍有争议。[FACT]

[INTERPRETATION] 波-波相互作用的物理意义：它们提供了波能衰减的通道，使得 CR 驱动的波生长不能无限持续。如果没有波-波相互作用，则 CR 驱动的波生长率（$\gamma \propto \nabla f$）会一直大于阻尼率，直到波幅达到饱和——这个饱和水平可能比有波-波相互作用时更高。波-波相互作用通过将波能从一个模式转移到另一个模式，最终将能量级联到可以被其他阻尼机制（如 Landau 阻尼）消耗的尺度。B&E 的处理暗示 Kraichnan 谱更适合强湍流，但这个论断依赖于具体的波-波相互作用率——这些率在今天仍然是活跃的研究课题。[INTERPRETATION]

[CRITIQUE] B&E 对波-波相互作用的处理是唯象的：他们假设某种饱和机制存在，但具体是哪一种（decay, parametric, or turbulent cascade）并不明确。这个不确定性使得 NL-DSA 的定量预言（尤其是饱和波幅和 CR 压力）存在较大误差范围。今天的直接数值模拟（如 MHD 湍流模拟）已经可以追踪波-波相互作用，但 B&E 1987 年的处理停留在量纲估计层面。[CRITIQUE]

### 5.11.3 粒子注入阈值的物理条件

[FACT] B&E §5.3 提到粒子注入（injection）是 DSA 的关键初始条件：只有超过某个能量阈值的粒子才能被有效加速。注入阈值由以下条件决定：① **热粒子转化为 DSA 粒子**：热等离子体中的粒子（能量 $\sim kT \sim 1$ keV）必须被激波面捕获才能进入 DSA；② **激波面捕获机制**：主要机制包括激波面附近的波-粒子相互作用（quasi-linear trapping）和 Shock Drift Acceleration（SDA）；③ **注入率**：单位体积的注入率 $Q_{\rm inj} \propto n_{\rm th} \exp(-\mu_{\rm inj} / T)$，其中 $\mu_{\rm inj}$ 是注入阈值。B&E 给出了 $n_{\rm CR}/n_{\rm th} \sim 10^{-4}-10^{-2}$ 的估计，对应 SNR 中的典型注入效率。[FACT]

[INTERPRETATION] 注入过程对 DSA 的重要性：① **注入决定效率上限**：如果注入率太低，则即使 DSA 机制本身是高效的，总的 CR 产量也可能不足；② **注入与磁场取向**：在准平行激波中，注入效率高；在准垂直激波中，注入效率低（因为波-粒子相互作用更困难）；③ **重离子的注入**：由于重离子的电荷 $Z$ 更大，它们的注入阈值更低（相对于能量），这可能导致重离子更容易被注入 DSA——这与观测的 CR 成分（轻核比例过高）可能有关。B&E 的注入讨论是定性的，因为 1987 年缺乏对注入过程的定量实验或观测数据。[INTERPRETATION]

[CRITIQUE] B&E 对注入的处理是最简化的：他们用单一参数（$\eta_{\rm inj}$）来参数化所有微观注入物理，但没有给出该参数的物理来源。今天我们知道注入涉及复杂的微观过程（Shock Drift Acceleration, Shock Surfaces Reformation, etc.），不同类型的激波（平行 vs 垂直）有不同的注入机制。B&E 的单参数处理使他们无法预言注入效率的环境依赖性，而这对于理解不同 SNR 的 CR 加速效率差异至关重要。[CRITIQUE]

[FACT] B&E §5 指出，DSA 谱指数 $q = 3r/(r-1)$ 在 test-particle 极限下与波谱无关——这是一个重要结论，因为 $q$ 只依赖于压缩比 $r$，而不依赖于散射机制的细节。但波谱仍然通过扩散系数 $D(p)$ 影响加速时间 $t_{\rm acc}$ 和最大能量 $E_{\rm max}$。对强激波（$r=4$），$q=4$ 对应微分谱 $E^{-2.0}$，与观测 $E^{-2.7}$ 之间的差异需要通过传播效应来解释（Gaisser 1990 的框架）。[FACT]

[INTERPRETATION] 波谱对 DSA 的间接影响通过两条路径：① **$t_{\rm acc}$ 路径**：$t_{\rm acc} \propto D/u_{\rm sh}^2 \propto p^{2-\nu}/u_{\rm sh}^2$——Kolmogorov（$\nu=5/3$）给出 $t_{\rm acc} \propto p^{1/3}$（能量越高，加速越慢）；Kraichnan（$\nu=3/2$）给出 $t_{\rm acc} \propto p^{1/2}$。对于给定 SNR 年龄 $t_{\rm SNR}$，最大能量由 $t_{\rm acc}(E_{\rm max}) = t_{\rm SNR}$ 决定。② **$E_{\rm max}$ 路径**：$E_{\rm max} \propto (u_{\rm sh}^2 t_{\rm SNR} D_0)^{1/(2-\nu)}$。这个公式揭示：年轻 SNR（$t_{\rm SNR}$ 短）可以通过增大 $u_{\rm sh}$（更快的激波）或 $D_0$（更强的湍流）来达到更高的 $E_{\rm max}$——这就是为什么年轻 SNR（如 Cas A，Tycho）是 PeVatron 的候选者。[INTERPRETATION]

[CRITIQUE] B&E 对波谱指数影响的两条路径讨论分散在 §5 的不同部分，没有在一个地方明确比较 Kolmogorov 和 Kraichnan 对 $E_{\rm max}$ 的不同预言。这个比较在今天尤为重要，因为 LHAASO 和 HAWC 的 TeV γ射线观测提供的数据可以间接检验不同波谱模型。Kraichnan 谱预言更快的加速（$t_{\rm acc} \propto p^{1/2}$ vs $p^{1/3}$），因此对给定年龄的 SNR，Kraichnan 谱给出更高的 $E_{\rm max}$。如果未来观测能够精确测量多个 SNR 的 $E_{\rm max}$ 分布，就可能区分这两种湍流模型——但 B&E 1987 年没有这个数据支撑。[CRITIQUE]

### 5.10.2 波-粒子耦合的饱和机制

[FACT] 原文 §5 的自洽分析讨论了波-粒子耦合的饱和机制：当 CR 分布函数的梯度 $df/dp > 0$ 时，CR streaming instability 产生 Alfvén 波，生长率 $\gamma \propto (u_{\rm sh} - V_A) / c \cdot (1/f)(df/dp)$。波幅增长直到非线性效应使 $\gamma$ 减小并最终饱和。饱和机制包括：① **波-波相互作用**：高幅度的波通过 decay instability 转化为其他波模；② **波粒相互作用饱和**：粒子从波中获取能量，使波幅减小；③ **空间均匀化**：CR 梯度通过扩散变得平缓，减小驱动不稳定性 的 $\nabla f$。[FACT]

[INTERPRETATION] 饱和机制的选择直接影响 NL-DSA 的预测：① 如果饱和主要由波-波相互作用主导，则波谱形状由非线性波动力学决定（可能偏离线性 $k^{-\nu}$）；② 如果饱和主要由波粒相互作用主导，则波谱形状保持 $W(k) \propto k^{-1}$（对应 $df/dp = \text{const}$ 的粒子谱）；③ 如果饱和主要由几何效应（$\nabla f$ 减小）主导，则波幅由 CR 分布的空间结构决定。B&E 没有明确区分这三种饱和机制，这导致他们的 NL-DSA 预言存在内在模糊性。这个模糊性在后续的数值模拟（Caprioli & Spitkovsky 2014）中被澄清：实际饱和涉及所有三种机制的竞争。[INTERPRETATION]

[CRITIQUE] B&E §5 的饱和分析是基于线性不稳定性理论的——他们假设饱和发生在弱波幅regime（$\delta B/B_0 \ll 1$）。但后续研究（包括 Bell 2004 的 Bell instability）表明，强波幅regime（$\delta B/B_0 \sim 1$ 甚至 $\gg 1$）在大 CR 密度环境中是普遍的。这种强不稳定性超出了 B&E 的线性理论范围——他们无法预言 $\delta B/B_0$ 的饱和水平和波谱形状。这是 B&E 1987 的一个重大局限，因为它直接关系到 $E_{\rm max}$ 和 DSA 效率的定量预言。[CRITIQUE]

### 5.10.3 各向异性散射与几何效应

[FACT] 原文 §5.2 指出：当激波法线与磁场方向夹角 $\theta_{\rm Bn}$ 变化时，DSA 的效率会有显著差异。准平行激波（$\theta_{\rm Bn} \lesssim 45°$）中，粒子可以沿磁场方向自由往返于激波两侧，DSA 效率高；准垂直激波（$\theta_{\rm Bn} \gtrsim 45°$）中，粒子在往返激波两侧时受到磁场方向的限制，DSA 效率降低。B&E 的分析给出了定性的几何依赖，但没有给出 $\theta_{\rm Bn}$ 的定量分布函数，因此无法估计真实 SNR 群体中平行和垂直激波的比例。[FACT]

[INTERPRETATION] $\theta_{\rm Bn}$ 的几何效应在今天看来是 DSA 应用于真实 SNR 的关键不确定因素之一：① SNR 前向激波的磁场方向倾向于平行于激波表面（因为 ISM 磁场在激波压缩后被放大），因此大多数 SNR 前向激波是准平行的（这有利于 DSA）；② SNR reverse shock 的磁场方向可能更随机，导致一部分 reverse shock 是准垂直的；③ 如果大部分 CR 加速发生在前向激波（准平行），则 B&E 的各向同性散射假设是合理的近似；但如果 reverse shock 贡献显著，则 $\theta_{\rm Bn}$ 的效应不可忽略。PIC 模拟（Caprioli & Spitkovsky 2014）表明，在准垂直激波中，粒子可以通过 shock drift 机制被加速，即使没有有效的 pitch-angle 散射。[INTERPRETATION]

[CRITIQUE] B&E 对 $\theta_{\rm Bn}$ 效应的讨论是综述性的，缺乏定量分析。他们认识到这个效应很重要，但没有提供估计真实 SNR 群体中不同 $\theta_{\rm Bn}$ 比例的方法。这个定量缺失使得 DSA 对银河系 CR 总量的预言存在额外的不确定性——如果大多数 SNR 激波是准垂直的，DSA 效率可能比 B&E 估计的要低。这个不确定性直到今天才通过 PIC 模拟和观测数据的结合被部分量化，但 B&E 1987 年的结论应该被视为定性而非定量的。[CRITIQUE]