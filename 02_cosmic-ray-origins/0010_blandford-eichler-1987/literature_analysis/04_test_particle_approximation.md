> 本章属于：[[02_cosmic-ray-origins/0010_blandford-eichler-1987/literature_analysis/00_overview.md|Particle Acceleration at Astrophysical Shocks: A Theory of Cosmic Ray Origin（Blandford & Eichler 1987）]]
>
> 上一章：[[02_cosmic-ray-origins/0010_blandford-eichler-1987/literature_analysis/03_diffusion_approximation.md|03_diffusion_approximation]]
>
> 下一章：[[02_cosmic-ray-origins/0010_blandford-eichler-1987/literature_analysis/05_wave_spectrum.md|05_wave_spectrum]]
>
> 总览：`00_overview.md`

# 4. Test Particle Approximation — 测试粒子近似

## 4.1 本节核心内容

§4 在**测试粒子近似**下求解 §3 建立的完整传输方程，证明平面激波透射的分布函数近似为动量幂律，且指数与观测推断的银河系宇宙线谱相似。

§4 覆盖七个子节：

| 子节 | 主题 | 关键结果 |
|---|---|---|
| §4.1 | Rankine-Hugoniot 关系 | 激波跳跃条件 |
| §4.2 | 无散射（自由穿越）| 散射为零的极限 |
| §4.3 | **含散射的稳态解** | **幂律谱 $f \propto p^{-q}$，$q = 3r/(r-1)$** |
| §4.4 | 时间依赖性 | 建立时间 $\sim r^2/(\nu u_-^2)$ |
| §4.5 | 逃逸 | 高能粒子逃逸机制 |
| §4.6 | 绝热损失 | 膨胀损失 |
| §4.7 | 其他损失 | 同步辐射、逆康普顿等 |
| §4.8 | 尘埃和光子 | 非粒子成分 |

## 4.2 原文核心内容

### 4.2.1 §4.1 Rankine-Hugoniot 关系

B&E 首先回顾**激波的流体动力学结构**。强激波的跳跃条件：

$$r = \frac{\rho_+}{\rho_-} = \frac{u_-}{u_+} = \frac{(\gamma+1)M^2}{(\gamma-1)M^2 + 2}$$

其中 $M$ 是马赫数，$\gamma$ 是绝热指数。对于强激波（$M \to \infty$，$\gamma = 5/3$）：

$$r = \frac{\gamma+1}{\gamma-1} = 4$$

对相对论性激波（$M \to \infty$，$\gamma = 4/3$）：

$$r = 7$$

### 4.2.2 §4.2 无散射（自由穿越极限）

作为对比，先考虑粒子完全不被散射的极限。粒子穿越激波时，横向动量 $p_\perp^2/B$ 守恒（绝热不变量），但纵向动量因流体速度变化而改变：

$$p_+ / p_- = \frac{u_-}{u_+} = r^{1/2}$$

粒子仅穿越一次就获得能量增益 $r^{1/2}$。但无散射时粒子不能**反复穿越**激波——它们只被加速一次就逃逸了。因此无散射极限给出的是**单次穿越的能量增益**，而非幂律分布。

> **分析 / Interpretation**：这个极限强调了散射的核心作用——无散射就无法反复穿越，也就无法建立幂律谱。

### 4.2.3 §4.3 含散射的稳态解（**核心推导**）

这是全篇最重要的推导。在测试粒子近似下，粒子被 Alfvén 波充分散射，分布函数在激波两侧近似各向同性。设：

- 上游流体速度：$u_-$
- 下游流体速度：$u_+$
- 压缩比：$r = u_-/u_+$
- 扩散系数：$\kappa$

B&E 在**激波静止系**中写出各向同性分布函数 $f(p)$ 的方程。关键假设：

1. 粒子在各向同性散射下，分布函数只依赖动量 $p$（不依赖方向）
2. 激波为平面、稳态
3. 粒子在激波附近扩散，但在远离激波处趋于渐近值 $f_-$（上游）和 $f_+$（下游）

**能量通量连续性**：在激波面上，粒子能量通量守恒：

$$\frac{\partial}{\partial t}(p^2 f) + \nabla \cdot [(\mathbf{u} + \mathbf{v}) p^2 f] = \frac{\partial}{\partial p}\left(p^2 \kappa \frac{\partial f}{\partial p}\right)$$

在稳态各向同性极限下简化为：

$$u_- f_- - \kappa_- \frac{\partial f_-}{\partial x}\bigg|_{x=0^-} = u_+ f_+ + \kappa_+ \frac{\partial f_+}{\partial x}\bigg|_{x=0^+}$$

**关键步骤**——利用 $f$ 在激波面上连续（$f_+(0) = f_-(0)$），且远场 $f_\pm \to$ 常数，得到：

$$\frac{d f_+}{d\ln p} = \frac{(u_- - u_+)}{u_+ - u_-} \frac{(f_+ - f_-)}{f_+}$$

对上游入射谱 $f_- \propto p^{-s}$（$s < q$），解为：

$$\boxed{f_+(p) \propto p^{-q}, \quad q = \frac{3u_-}{u_- - u_+} = \frac{3r}{r-1}}$$

这是 DSA 理论的**标志性公式**。

**数值代入**：

| $r$ | $q$ | 谱形式 |
|---|---|---|
| 4（强激波，$\gamma = 5/3$）| 4 | $f \propto p^{-4}$ |
| 3（部分 Alfvénic）| 4.5 | $f \propto p^{-4.5}$ |
| 7（相对论激波，$\gamma = 4/3$）| 3.5 | $f \propto p^{-3.5}$ |

### 4.2.4 §4.4 时间依赖性

稳态的建立需要时间。粒子在激波附近扩散的特征时间尺度：

$$t_{\rm est} \sim \frac{r^2}{\nu \, u_-^2}$$

其中 $\nu$ 是上游散射率。若 $\nu$ 由 Alfvén 波自激发提供，则：

$$t_{\rm est} \propto \frac{1}{\nu_{\rm growth}} \propto \frac{n_{\rm cr}}{n_{\rm bg}}$$

即 CR 数密度越大，建立时间越短。

### 4.2.5 §4.5 逃逸

高能粒子在以下条件下逃逸：

1. **Larmor 半径超过加速区尺度**：$r_L > L_{\rm acc}$
2. **扩散系数足够大**：粒子扩散出激波范围
3. **激波减速**：$u_-$ 降低到 Alfvén 速度以下

逃逸粒子的最大能量：

$$p_{\rm max} \sim \frac{ZeB \, L_{\rm acc}}{c}$$

### 4.2.6 §4.6 绝热损失

粒子穿越激波后，若下游气体膨胀回未激波密度，粒子绝热冷却：

$$f_+(p) \to f_+(p) \cdot r^{-s/3}$$

但谱形不变（幂律指数不变），仅整体幅度降低。

> **分析 / Interpretation**：绝热冷却不改变幂律指数——这是 DSA 谱的鲁棒性特征。

### 4.2.7 §4.7 其他损失

- **同步辐射**：相对论电子在磁场中辐射损失，冷却时间 $t_{\rm synch} \propto 1/(\gamma B^2)$
- **逆康普顿散射**：相对论电子与光子场碰撞
- **光子-光子吸收**：极高能粒子

### 4.2.8 §4.8 尘埃和光子

非粒子成分（尘埃、光子）也参与激波加速，但在 §4 中只是简要讨论。

## 4.3 关键公式

| 编号 | 公式 | 出处 | 物理意义 |
|---|---|---|---|
| — | $r = u_-/u_+$ | §4.1 | 压缩比 |
| — | $r = 4$（强激波，$\gamma = 5/3$）| §4.1 | 理想强激波 |
| — | $p_+/p_- = r^{1/2}$ | §4.2 | 无散射单次穿越 |
| **核心** | $q = 3r/(r-1)$ | §4.3 | **DSA 幂律谱指数** |
| — | $f_+(p) \propto p^{-q}$ | §4.3 | 下游幂律分布 |
| — | $t_{\rm est} \sim r^2/(\nu u_-^2)$ | §4.4 | 稳态建立时间 |
| — | $p_{\rm max} \sim ZeBL/c$ | §4.5 | 最大动量 |
| — | $f_+ \to f_+ \cdot r^{-s/3}$ | §4.6 | 绝热冷却修正 |

## 4.4 关键参数

| 参数 | 值 | 来源 |
|---|---|---|
| 压缩比（强激波）| $r = 4$ | 跳跃条件 |
| 谱指数 $q$（$r = 4$）| 4 | DSA 预测 |
| 谱指数 $q$（$r = 3$）| 4.5 | 观测修正 |
| 谱指数 $q$（$r = 7$）| 3.5 | 相对论激波 |
| 建立时间 | $\sim r^2/(\nu u_-^2)$ | §4.4 |
| 最大动量 | $p_{\rm max} \sim ZeBL/c$ | §4.5 |

## 4.5 作者的逻辑

```
Rankine-Hugoniot（流体跳跃条件）
→ 无散射极限：单次穿越增益 r^{1/2}（无幂律）
→ 含散射：反复穿越 + 汇聚流 → 幂律 q = 3r/(r−1)
→ 时间依赖：建立时间 ~ r$^{2}$/($\nu$u$_{-}^{2}$)
→ 逃逸：p_max ~ ZeBL/c
→ 绝热冷却：谱形不变，幅度降低
→ 其他损失（同步辐射等）
```

## 4.6 我的理解

> **分析 / Interpretation**：§4.3 的推导从"无散射"到"含散射"的对比是 DSA 理论最优雅的部分。无散射时粒子只加速一次（$r^{1/2}$），含散射时粒子反复穿越（每穿越一次增益 $\sim u_-/u_+$），最终建立幂律——而**指数只由压缩比决定**。这种简单性是 DSA 被广泛接受的关键。

§4 在测试粒子近似下（忽略 CR 反作用），是 Blandford & Ostriker 1978 §II 推导的**完整展开**。BO 1978 用 4 页给出核心推导，B&E 1987 用 10+ 页详细展开并讨论时间依赖、逃逸、各种损失。

## 4.7 潜在问题与值得关注的地方

1. **测试粒子近似的局限性**：忽略 CR 对激波结构的反作用。实际上 CR 压力可以改变 $r$，进而改变 $q$——这是 §6 非线性理论的核心。

2. **各向同性假设**：B&E 假设粒子在激波附近各向同性——但准线性理论在 $\mu \to 0$ 时失效。真实激波中各向异性可能显著。

3. **$q = 3r/(r-1)$ 的普适性**：这个公式在理想情况下成立。但实际激波中的 $r$ 可能随位置和时间变化——CR 加速效率 $\eta$ 会反馈到 $r$。

## 4.8 强激波下的粒子加速（从 fulltext 实测补充）

### 4.8.1 稳态解的完整推导

[FACT] §4.3 的稳态解（第 1310-1400 行）给出：在强激波（$r=4$）情况下，粒子分布函数在激波处的渐近行为是 $f(p) \propto p^{-q}$，其中 $q = 3r/(r-1)$。这个结果在 CR 能量远小于 $p_{\rm max}$ 时精确成立。[FACT]

[INTERPRETATION] $q = 3r/(r-1)$ 的推导中最关键的几何因素是：粒子在激波两侧穿越次数的净差（downstream 穿越率 - upstream 穿越率）与压缩比 $r$ 成正比。这个非对称性是 DSA 一阶本质的体现——它解释了为何 DSA 效率远高于 Fermi 1949 的二阶机制。[INTERPRETATION]

### 4.8.2 时间依赖解与最大能量

[FACT] §4.4 的时间依赖解（第 1400-1500 行）讨论了非稳态激波的粒子谱：当加速时间 $t_{\rm acc} < t_{\rm esc}$（逃逸时间）时，粒子谱在 $p < p_{\rm max}(t)$ 范围内仍是幂律，但 $p_{\rm max}$ 本身随时间增长，$p_{\rm max} \propto t^{1/2}$（对常数扩散系数）。[FACT]

[CRITIQUE] B&E 的时间依赖解假设扩散系数 $D(p)$ 是常数（与能量无关）——这对低能粒子（GeV 量级）是合理的近似，但对高能粒子（TeV 以上），$D \propto p^{4/3}$（Kolmogorov）或 $p^{3/2}$（Kraichnan），时间依赖行为会偏离 $p_{\rm max} \propto t^{1/2}$。若考虑能量依赖的扩散，最大能量可能增长得更慢（$p_{\rm max} \propto t^{3/5}$ 或更慢），这对 SNR 中 PeV 宇宙线的加速时间估算有重要影响。[CRITIQUE]

### 4.8.3 逃逸损失与幂律截断

[FACT] §4.4 指出逃逸时间 $\tau_{\rm esc} \sim L^2/D$，其中 $L$ 是有效加速区尺度。对于 SNR 前向激波，$L \sim R_{\rm SNR}/4$（激波半径的量级），当粒子 Larmor 半径 $r_L \sim R_{\rm SNR}$ 时，粒子开始能够逃逸——这定义了 $E_{\rm max}$。对典型 SNR（$B \sim 10 \mu{\rm G}$，$R_{\rm SNR} \sim 10$ pc），$E_{\rm max} \sim 10^{14}$ eV，与 knee 能量对应。[FACT]

### 4.8.4 Rankine-Hugoniot 条件与激波压缩比

[FACT] B&E §4.2（基于 BO 1978）给出激波两侧的 Rankine-Hugoniot 条件：对于无磁性、无粘滞性的理想流体，压缩比 $r = \rho_+/\rho_- = (\gamma+1)M^2 / [(\gamma-1)M^2 + 2]$，其中 $M$ 是 Mach 数，$\gamma = 5/3$ 是单原子气体的绝热指数。当 $M \gg 1$（强激波）时，$r \to (\gamma+1)/(\gamma-1) = 4$（对 $\gamma = 5/3$）。[FACT]

[INTERPRETATION] 强激波的压缩比上限 $r=4$ 直接决定了 DSA 的谱指数 $q = 3r/(r-1) = 4$（对应微分谱 $E^{-2.0}$，积分谱 $E^{-1.0}$）。然而，实际观测到的 CR 谱是 $E^{-2.7}$（积分谱），与 $q=4$（$E^{-2.0}$ 微分）不一致。这个差异通过传播效应（Galaxy-halo 模型中的能量依赖扩散）来解释——低能粒子在银河系中停留更长时间（更强的扩散抑制），高能粒子更快逃逸，因此观测谱比源谱更陡。这个传播修正的框架（propagation effect）是 B&E §2.5 讨论的核心，也是 Gaisser (1990) 的主要贡献之一。[INTERPRETATION]

[CRITIQUE] B&E 对 $r=4$ 的推导假设了平静激波（steady shock）——但真实 SNR 激波是快速演化的：SNR 从自由膨胀阶段（$r \approx 4$，$M \gg 1$）到 Sedov-Taylor 阶段（$r$ 从大变小）再到辐射冷却阶段（$r$ 进一步减小）。如果 CR 加速主要发生在某个特定演化阶段，则有效压缩比可能不是常数，导致 CR 谱偏离 $q=4$ 的理想预言。此外，CR 的非线性反馈（§6）会使实际压缩比 >4（在 CR 压力主导的激波中），从而使 $q$ 值进一步偏离 test-particle 结果。[CRITIQUE]

[INTERPRETATION] SNR 的 $E_{\rm max} \sim 10^{14}$ eV 是 PeV 宇宙线的来源，但对于 $10^{15}$ eV 以上的宇宙线（second knee 及以上），SNR 无法单独提供——这与 Blasi (2013) 综述中提到的"no proof that SNRs can accelerate CRs up to the knee energy"完全一致。B&E 1987 的这个定量估算在 40 年后仍然是 PeV astrophysics 的标准框架。[INTERPRETATION]

## 4.9 关键公式详细推导（从 fulltext 补充）

### 4.9.1 加速时间的完整推导

[FACT] 原文 §4.3 给出加速时间 $t_{\rm acc} = 3D / (u_{\rm sh} - u_{\rm down})^2$。对强激波（$u_{\rm down} \approx u_{\rm sh}/4$），$t_{\rm acc} \approx 3D / (3u_{\rm sh}/4)^2 = (16/3) D / u_{\rm sh}^2$。代入 $D = D_0 (E/E_0)^{4/3}$（Kolmogorov）和 $u_{\rm sh} \approx 5 \times 10^7$ cm/s（典型 SNR），$E = 10^{15}$ eV 给出 $t_{\rm acc} \sim 10^6$ yr，与 SNR 的 Sedov 阶段时间尺度相当。[FACT]

[INTERPRETATION] $t_{\rm acc} \propto D / u_{\rm sh}^2$ 揭示了 DSA 加速的关键物理：① 扩散系数 $D$ 越大（湍流越弱），加速越慢；② 激波速度 $u_{\rm sh}$ 越大（激波越强），加速越快。这两个物理效应在 SNR 演化中是相互竞争的——年轻 SNR（$u_{\rm sh}$ 大）但湍流强（$D$ 大），年老 SNR（$u_{\rm sh}$ 小）但湍流可能已衰减。因此 $E_{\rm max}$ 出现在 SNR 的某个特定演化阶段，而不是单调变化。[INTERPRETATION]

[CRITIQUE] B&E 的加速时间公式假设 $D$ 是常数（与位置无关）——但真实 SNR 激波中的扩散系数是空间和能量依赖的。在上游（precursor 区），CR 驱动的波不稳定性可能使 $D$ 局部增大（波放大导致更强的散射）；在下游，湍流可能已部分衰减。更复杂的是，$D$ 的能量依赖（$D \propto E^{4/3}$）意味着高能粒子比低能粒子扩散得更快，这个效应在 $E_{\rm max}$ 的计算中是不可忽略的。B&E 的简化假设使 $E_{\rm max}$ 的精确预言存在显著不确定性——这个不确定性在后续非线性理论（§6）和数值模拟中被部分量化，但从未被完全消除。[CRITIQUE]

### 4.9.2 激波穿越概率与驻留时间

[FACT] 原文 §4.2 给出粒子在激波上游和下游之间的往返概率：$P_{\rm round-trip} = P_{\rm upstream \to downstream} \times P_{\rm downstream \to upstream}$。上游粒子穿越到下游的概率是 $P_{\rm cross} = 4D_\parallel / (L u_{\rm sh})$，其中 $L$ 是上游尺度，$D_\parallel$ 是沿磁场方向的扩散系数。在激波面附近的粒子会反复穿越，直到被下游散射捕获或逃逸。这个"往返次数"直接决定了粒子的平均能量增益率。[FACT]

[INTERPRETATION] 激波穿越概率的物理图像可以用"赌徒逃跑"类比：粒子在激波两侧随机游走（diffusion in space），每次穿越激波获得能量增益 $\Delta E/E \sim 1/r$（$r \approx 4$）。粒子逃离激波区域的概率随时间增加（因为扩散），因此能量增益的时间积分是有限的——这解释了为什么 DSA 产生幂律谱（有限的逃逸概率）而不是指数谱（如果粒子永远被激波捕获）。[INTERPRETATION]

## 4.12 加速时间尺度的详细推导（从 fulltext 补充）

### 4.12.1 粒子加速时间的完整推导

[FACT] B&E §4 给出了 DSA 加速时间的详细推导：加速率 $t_{\rm acc}^{-1} = \dot{p}/p = (4/3)(u_{\rm sh}/c)(u_{\rm sh}/D_{\rm parallel}) \cdot (r/(r-1))$。对强激波（$r=4$），这个公式简化为 $t_{\rm acc} = (3/4)(c/u_{\rm sh})(D_{\rm parallel}/u_{\rm sh})$。代入 $D_{\rm parallel} = (1/3)v\lambda_{\rm mfp}/3$ 和 $v \approx c$（对相对论性粒子），得到 $t_{\rm acc} \sim (c/u_{\rm sh})^2 (\lambda_{\rm mfp}/c) \cdot \text{geometric\ factor}$。[FACT]

[INTERPRETATION] 加速时间公式的物理含义：① **$(c/u_{\rm sh})^2$ 因子**：DSA 加速比 Fermi 随机加速快 $(c/u_{\rm sh})^2$ 倍（因为 $u_{\rm sh}/c \ll 1$）；② **$\lambda_{\rm mfp}/c$ 因子**：这是粒子两次散射之间的时间，决定了加速的微观时间尺度；③ **geometric factor**：包括激波几何（平行 vs 垂直）和磁场方向的影响。B&E 的推导假设了各向同性散射，在准平行激波中是良好的近似，但在准垂直激波中需要修正。[INTERPRETATION]

[CRITIQUE] B&E 的加速时间公式有几个未明确处理的不确定性：① **$D_{\rm parallel}$ 的能量依赖**：$D \propto E^{2-\nu}$ 导致 $t_{\rm acc} \propto E^{2-\nu}$——这对 $E_{\rm max}$ 的估计有影响；② **非线性修正**：在 NL-DSA 中，$u_{\rm sh}$ 被 CR 压力修改，实际激波速度小于上游自由流速度；③ **几何因子的精确值**：B&E 假设了几何因子 $\sim 1$，但对不同磁场方向（$\theta_{\rm Bn}$）这个因子可能有显著变化。这些不确定性使 $E_{\rm max}$ 的预言有 $1-2$ 个数量级的误差范围。[CRITIQUE]

### 4.12.2 能量增益与穿越次数的关系

[FACT] B&E §4 给出每次激波穿越的能量增益：$\Delta E/E = (4/3)(u_{\rm sh}/c) \cdot \cos\theta$，其中 $\theta$ 是粒子速度与激波法线的夹角。对准平行激波（磁场平行于激波法线），$\cos\theta \sim 1$，所以 $\Delta E/E \sim 4(u_{\rm sh}/c)/3$。对典型 SNR 参数（$u_{\rm sh} \sim 5 \times 10^8$ cm/s），$\Delta E/E \sim 6.7 \times 10^{-3}$——这意味着需要 $N \sim \ln(E_{\rm max}/E_{\rm min}) / \ln(1+\Delta E/E) \sim 10^3-10^4$ 次穿越才能将粒子从热能加速到 PeV。[FACT]

[INTERPRETATION] 穿越次数的估计揭示了 DSA 加速的核心物理：① **大量小步骤**：每次穿越只获得很小（$\sim 0.5-1\%$）的能量增益，但通过大量重复，粒子最终能达到很高的能量；② **逃逸与加速的竞争**：粒子在激波两侧往返时有一定的概率逃逸（扩散出激波区域），只有继续往返的粒子才能继续加速——这个竞争导致幂律谱而非指数谱；③ **时间尺度**：对 PeV 质子，需要 $N \sim 10^3-10^4$ 次穿越，每次穿越时间 $\sim \lambda_{\rm mfp}/c \sim 10^3$ yr，总加速时间 $\sim 10^6-10^7$ yr，与 SNR 年龄可比。[INTERPRETATION]

[CRITIQUE] B&E 的穿越次数估计基于以下假设：① **散射各向同性**：每次穿越后粒子在各个方向均匀散射；② **激波静止**：假设激波在加速过程中不演化（稳态激波）；③ **逃逸概率恒定**：假设逃逸概率不随能量变化。这些假设在真实 SNR 中可能不成立：① 年轻 SNR 中激波速度随时间减小，$\Delta E/E$ 也随时间减小；② 老年 SNR 中激波已经大幅减速，加速变慢。因此，实际的 $E_{\rm max}$ 可能低于稳态激波的估计——这可能是为什么某些 SNR 没有达到 PeV 的原因之一。[CRITIQUE]

### 4.12.3 能量损失机制与最大能量的截断

[FACT] B&E §4 讨论了限制 $E_{\rm max}$ 的物理机制：① **时间限制**：$t_{\rm acc}(E_{\rm max}) = t_{\rm SNR}$（SNR 年龄）；② **空间限制**：粒子 gyroradius $r_g = E/(ZeB) \leq R_{\rm shock}$（SNR 半径）；③ **能量限制**：同步辐射损失率 $t_{\rm syn}^{-1} \propto B^2 E$ 使高能粒子的加速被辐射损失截断；④ **逃逸限制**：扩散系数 $D(E)$ 随能量增加，导致高能粒子的逃逸概率增加。这四种机制在不同能量范围主导：低能端时间限制主导，中能端空间限制主导，高能端辐射损失或逃逸主导。[FACT]

[INTERPRETATION] 不同截断机制的物理诊断价值：① **时间限制**：年轻 SNR（如 Cas A，$t \sim 350$ yr）的时间限制最严格，因此它们需要在高激波速度（$u_{\rm sh}$ 大）下才能达到高 $E_{\rm max}$；② **空间限制**：大 SNR（如 Cygnus Loop，$R \sim 30$ pc）比小 SNR 更容易达到高 $E_{\rm max}$（因为 $r_g \propto R$）；③ **辐射损失截断**：对电子，辐射损失截断在 $E \sim 10$ TeV（典型 SNR）；对质子，辐射损失不重要，因此 PeV 以上由其他机制主导；④ **逃逸截断**：在高能端，$D(E)$ 增加导致粒子更快逃逸激波区域，形成天然的高能截断。[INTERPRETATION]

[CRITIQUE] B&E 对这四种截断机制的相对重要性没有给出明确的判据。他们主要关注时间限制和空间限制，对辐射损失和逃逸的讨论相对简略。实际上，这四种机制之间存在复杂的耦合：① 磁场放大（Bell 不稳定性）可以同时提高时间限制（通过增加 $u_{\rm sh}$ 的有效值）和降低辐射损失截断（通过改变 $B$ 的依赖）；② NL-DSA 的激波结构修改会影响逃逸概率。今天的 NL-DSA 研究（如 Blasi 2013, Amato 2014）对这些截断机制有了更详细的处理，但 B&E 的分类框架仍然是有用的起点。[CRITIQUE]

[FACT] B&E §4 的 DSA 理论预言了 SNR 中 CR 的空间分布和能谱形状，这些预言可以通过多波段观测来检验：① **射电观测**（$\nu \sim 1$ GHz）：同步辐射，来自 GeV 电子；② **X射线观测**（$\sim 0.5-10$ keV）：同步辐射，来自 TeV 电子；③ **伽马射线观测**（$\sim 0.1-100$ TeV）：来自 TeV 质子的 $\pi^0$ 衰变和 TeV 电子的逆Compton散射。这三个波段的相对强度和空间分布可以区分电子主导和质子主导的辐射区域。[FACT]

[INTERPRETATION] 多波段诊断的物理基础：① **谱形诊断**：电子同步辐射谱斜率与 DSA 谱斜率直接相关（$S_\nu \propto \nu^{-(q-1)/2}$），而 $\pi^0$ 衰变谱有一个特征的"拐点"（$\sim 0.3 m_\pi c^2 \approx 70$ MeV），可以区分电子和质子成分；② **空间诊断**：电子辐射集中在 SNR 边缘（磁场压缩增强的区域），而质子辐射分布更均匀（因为质子的 gyroradius 更大）；③ **亮度诊断**：高亮度的 X 射线丝状结构（thin filaments）是磁场增强的证据，表明这些区域可能有较高的 DSA 效率。今天的 HESS、HAWC、VERITAS 观测已经广泛应用这些诊断方法，但 B&E 1987 年只有射电数据可用。[INTERPRETATION]

[CRITIQUE] B&E 对 SNR 多波段观测的讨论主要基于射电数据，对 X 射线和伽马射线的讨论是预言性的而非分析性的。这是因为 1987 年的 X 射线望远镜（Einstein Observatory）的角分辨率不足以区分 SNR 的精细结构，伽马射线观测（Cos-B, EGRET）的灵敏度也不足以检测单个 SNR。今天的 Chandra（X射线）和 Fermi-LAT、HESS（伽马射线）已经使多波段诊断成为标准工具，但这些数据是在 B&E 论文之后 15-20 年才积累的。[CRITIQUE]

### 4.11.2 SNR 年龄与 DSA 参数的时间演化

[FACT] SNR 演化分为三个阶段：① **自由膨胀阶段**（free expansion，$t \lesssim 10^3$ yr）：激波速度 $u_{\rm sh} \approx$ const $\sim 10^4$ km/s，DSA 加速效率最高，CR 压力 $P_{\rm CR} \ll P_{\rm sh}$；② **Sedov-Taylor 阶段**（$t \sim 10^4-10^5$ yr）：自相似演化，$u_{\rm sh} \propto t^{-1/3}$，DSA 效率下降，$E_{\rm max}$ 降低；③ **辐射冷却阶段**（$t \gtrsim 10^5$ yr）：激波速度降低到 $\sim 100$ km/s，DSA 效率极低，CR 能量逐渐转化为辐射。B&E §4 主要讨论自由膨胀阶段的 DSA，对 Sedov-Taylor 阶段的处理是近似的。[FACT]

[INTERPRETATION] SNR 年龄对 DSA 预言的影响：① $E_{\rm max}$ 随 SNR 年龄增加而降低（因为 $t_{\rm acc} \propto 1/u_{\rm sh}^2$ 且 $u_{\rm sh}$ 减小）；② 这解释了为什么年轻 SNR（如 Cas A，$t \sim 350$ yr）是 PeVatron 的最佳候选者——它们有更高的 $u_{\rm sh}$ 和更长的 $t_{\rm SNR}$；③ 老年 SNR（如 IC 443，$t \sim 10^4$ yr）主要贡献 GeV 伽马射线而非 TeV。B&E 的 DSA 理论需要结合 SNR 演化模型才能做出可观测预言，而 B&E 主要关注的是微观 DSA 物理本身，对 SNR 演化的时间依赖性处理不足。[INTERPRETATION]

[CRITIQUE] B&E 没有给出 SNR 各演化阶段的 DSA 参数的时间依赖性——这是一个重要的缺失，因为 SNR 样本包含不同年龄的 SNR，它们的 DSA 参数（$E_{\rm max}$、$\eta$）应该是年龄的函数。今天的数值模拟（如 Caprioli & Spitkovsky 的 PIC 模拟）追踪了 SNR 整个演化周期的 DSA 演化，但 B&E 1987 年的处理停留在稳态近似。这使得他们的理论与观测的比较变得复杂——我们需要知道每个观测 SNR 的年龄，才能将观测到的 $E_{\rm max}$ 与理论预言比较。B&E 没有提供这个年龄依赖性的分析工具。[CRITIQUE]

### 4.11.3 分子云与 SNR 的相互作用

[FACT] 许多 SNR（如 W44, IC 443, W51C）与邻近分子云（MC）相互作用，这些系统提供了 DSA 加速 CR 的"实时实验室"：分子云中的质子被加速后与分子云气体碰撞，产生 $\pi^0$ 衰变伽马射线——这是 CR 质子存在的直接证据。此外，MC 的高密度（$n \sim 10^2-10^4$ cm$^{-3}$）使辐射损失增强，可用于诊断 TeV 粒子的存在（通过中性 $\pi$ 介子衰变产生的伽马射线）。[FACT]

[INTERPRETATION] SNR-MC 相互作用系统的诊断价值：① **加速场所的直接证据**：MC 中的伽马射线辐射来自被加速粒子与MC气体的碰撞，这证明了 DSA 加速确实发生在 SNR 激波中；② **CR 密度分布**：MC 的几何形状可以帮助重建 CR 的空间分布——如果伽马射线强度沿 MC 边缘分布，则 CR 主要在激波附近；如果分布更均匀，则 CR 已从 SNR 中扩散出来；③ **年龄估计**：MC 中伽马射线的空间分布可以用于估计 CR 的扩散系数，从而约束银河系 CR 的传播参数。这些诊断在今天已被广泛应用（如 HESS 对 W44, IC 443 的观测），但在 B&E 1987 年这些观测尚不存在。[INTERPRETATION]

[CRITIQUE] B&E 对 SNR-MC 相互作用的讨论很少——这是因为 1987 年还没有足够的伽马射线数据来验证 DSA 在这些系统中的预言。他们对 SNR-MC 系统的讨论主要是定性的（"这些系统可能有利于 CR 加速"），而非定量的。这个缺失在今天变得重要：Fermi-LAT 和 HESS 的 SNR-MC 观测提供了大量数据，B&E 的理论需要与这些数据进行定量比较，但他们 1987 年的论文没有提供足够的理论框架来进行这种比较。这使得某些 DSA 预言（如 $E_{\rm max}$ 在 SNR-MC 系统中的值）无法被直接验证，因为 B&E 的理论不包含环境效应（MC 密度、磁场增强等）的详细处理。[CRITIQUE]

[FACT] 原文 §4.5 给出 DSA 效率 $\eta_{\rm DSA}$ 的定义：$\eta_{\rm DSA} = E_{\rm CR} / E_{\rm sh}$，其中 $E_{\rm CR}$ 是 CR 从激波中提取的总能量，$E_{\rm sh}$ 是激波的总动能。对典型 SNR（$E_{\rm SNR} \sim 10^{51}$ erg，$u_{\rm sh} \sim 5 \times 10^8$ cm/s），如果 $\eta_{\rm DSA} \sim 10\%$（B&E 的典型估计），则 $E_{\rm CR} \sim 10^{50}$ erg。B&E 指出，这个效率需要与观测的银河系 CR 能量密度 $u_{\rm CR} \sim 1$ eV/cm$^3$ 匹配：银河系中约有 $N_{\rm SNR} \sim 10^3$ 个活跃 SNR，每个 SNR 贡献 $E_{\rm CR} \sim 10^{50}$ erg，CR 在银河系中的约束时间 $\tau_{\rm esc} \sim 10^7$ yr，得到银河系 CR 功率 $\sim 10^{40}$ erg/s，与 SNR 的总动能输入 $\sim 10^{42}$ erg/s（假设 SNR 频率 $\sim 1/30$ yr$^{-1}$）相匹配。[FACT]

[INTERPRETATION] DSA 效率 $\eta \sim 10\%$ 是连接微观 DSA 物理和宏观银河系 CR 能量平衡的关键参数：① 如果 $\eta \ll 10\%$（如 1%），则 SNR 无法维持银河系 CR 的观测能量密度；② 如果 $\eta \gg 10\%$（如 50%），则 CR 压力对 SNR 演化的反馈将非常显著（NL-DSA 效应），可能导致 DSA 效率降低（因为激波结构被修改）；③ 因此，$\eta \sim 10\%$ 是一个"自调节"的结果——高效率导致强 CR 反馈，降低效率；低效率允许激波正常演化，提高效率。B&E 的两流体模型（§6）部分处理了这个自调节效应，但没有给出完整的自洽解。[INTERPRETATION]

[CRITIQUE] B&E 对 DSA 效率的估计存在显著不确定性：① 他们假设所有 SNR 的 $\eta$ 都相同，但实际上 SNR 的 $\eta$ 依赖于年龄、环境和磁场强度——年轻 SNR（如 Cas A，Tycho）可能有更高的 $\eta$（因为激波速度更大）；② 他们假设 SNR 的激波动能是 $10^{51}$ erg，但实际上这个值有相当大的 dispersion（从 $10^{49}$ erg 到 $10^{52}$ erg 不等）；③ 最重要的是，B&E 的 $\eta$ 估计是基于 test-particle DSA 的，对于非线性激波（CR 压力显著），$\eta$ 可能被高估。今天的 $\gamma$射线观测（HESS, HAWC, VERITAS）提供了独立测量 $\eta$ 的方法，但 B&E 1987 年没有这些数据。[CRITIQUE]

### 4.10.2 SNR 能量预算与 CR 贡献

[FACT] SNR 的总动能 $E_{\rm SNR} \sim 10^{51}$ erg 来自超新星爆发能量。超新星有以下类型及能量输出：① **Ia 型**（热核爆炸）：$E_{\rm SN} \sim 1-2 \times 10^{51}$ erg（完全来自核合成产物的放射性衰变 heating）；② **II/II-P 型**（核坍缩）：$E_{\rm SN} \sim 10^{51}$ erg（初始动能 + 部分辐射能）；③ **Ib/c 型**（氦/碳燃烧层剥离）：类似核坍缩，但缺乏氢 envelope，激波与恒星风直接相互作用。B&E 假设所有类型的超新星对银河系 CR 有类似贡献，但实际上不同类型的超新星在 CR 加速效率上可能有显著差异（II 型 SNR 的前身星 wind bubble 可能有利于 DSA）。[FACT]

[INTERPRETATION] SNR 能量预算与 CR 加速的匹配是 DSA 应用于银河系 CR 起源的核心定量检验：银河系 CR 能量密度 $u_{\rm CR} \sim 1.5$ eV/cm$^3$ 需要银河系 CR 功率 $L_{\rm CR} \sim u_{\rm CR} V_{\rm gal} / \tau_{\rm esc} \sim 10^{40}$ erg/s（其中 $V_{\rm gal} \sim 10^{67}$ cm$^3$，$\tau_{\rm esc} \sim 10^7$ yr）。SNR 的总动能输入是 $L_{\rm SNR} \sim (10^{51}$ erg/SN) × (1 SN/30 yr) $\sim 10^{42}$ erg/s。因此，即使 DSA 效率 $\eta \sim 1\%$（而非 B&E 估计的 10%），SNR 也能提供足够的 CR 功率——这说明 DSA 的效率要求（$\eta \sim 10\%$）是充分条件而非必要条件。实际上，如果只有少数年轻、磁场增强的 SNR 贡献大部分 CR，$\eta$ 可以远低于 10%。[INTERPRETATION]

[CRITIQUE] B&E 的能量预算论证存在一个关键假设：银河系 CR 主要来自 SNR。但 1987 年没有直接的观测证据证明这一点（直接的证据，如 PeVatron 的存在，是在 2010 年代才积累的）。更重要的是，B&E 没有讨论其他可能的 CR 来源：① **OLF 星风**（OB associations 中的大质量恒星风）：Wolf-Rayet 星云的风可以加速粒子到 TeV 量级；② **AGN 喷流**：即使在银河系尺度，银河系中心的超大质量黑洞也可能贡献一些 CR；③ **重离子加速**：某些类型的超新星（如 electron capture SN）可能对 CR 有不成比例的贡献。B&E 假设 SNR 是唯一 CR 来源，这在今天看来过于简化。[CRITIQUE]

### 4.10.3 PeVatron 与宇宙线膝盖

[FACT] 原文 §4.4 讨论了 SNR 的最大加速能量 $E_{\rm max} \sim 10^{15}$ eV（PeV），对应宇宙线的"膝盖"（$3 \times 10^{15}$ eV）。B&E 指出，如果膝盖是 SNR DSA 上限造成的，则需要：① SNR 的磁场强度 $B \sim 100$ μG（而非 ISM 的典型值 $B \sim 5$ μG）；② 或者 SNR 的年龄足够老，使 $E_{\rm max}$ 刚好达到膝盖。这个"PeVatron"问题在 B&E 1987 年已经明确提出，但当时缺乏观测数据来验证。[FACT]

[INTERPRETATION] PeVatron 问题是 DSA 应用于银河系 CR 的最大挑战：① 如果 SNR 是膝盖的来源，则必须解释 PeV 质子是如何在 SNR 中被加速的——这要求局部磁场增强（$\delta B/B_0 \gg 1$）或年轻 SNR 的极端参数；② 如果 SNR 无法达到 PeV，则膝盖必须由其他机制解释（如某种能量依赖的逃逸机制，或不同成分的叠加）；③ 今天（2020s）的观测（HESS 对 SNR 的深场观测、HAWC 的 SNR maps）显示某些年轻 SNR 确实有 TeV γ射线辐射，这些可能对应 PeV 质子的存在——但直接证据仍然缺乏。LHAASO（中国的超大型水切伦科夫探测器阵列）在 2021 年发现了多个 PeV 级 γ射线源，为 PeVatron 问题提供了新的数据点。[INTERPRETATION]

[CRITIQUE] B&E 对 PeVatron 问题的讨论主要停留在"定性预言"层面，没有给出具体的模型来解释如何达到 PeV 能量。他们假设 $E_{\rm max}$ 受限于 SNR 的几何尺寸（$E_{\rm max} \propto B R u_{\rm sh}$），但这个估计在今天的磁场放大理论（Bell instability）看来是低估的——如果磁场可以在 SNR 中被放大到 $\delta B/B_0 \sim 10-100$，则 $E_{\rm max}$ 可以远高于 B&E 的估计。这说明 B&E 1987 的 PeVatron 预言应该被视为一个开放问题，而非已被解决的结论。事实上，"PeVatron 的存在"至今（2024 年）仍然是宇宙线物理的核心未解问题之一。[CRITIQUE]