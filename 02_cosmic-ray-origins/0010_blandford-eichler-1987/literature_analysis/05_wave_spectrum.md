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

## 5.10 波谱与 DSA 参数依赖的深入分析（从 fulltext 补充）

### 5.10.1 波谱指数对 DSA 谱指数的影响

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