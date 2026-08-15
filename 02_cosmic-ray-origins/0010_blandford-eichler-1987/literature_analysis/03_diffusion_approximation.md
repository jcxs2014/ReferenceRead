> 本章属于：Particle Acceleration at Astrophysical Shocks: A Theory of Cosmic Ray Origin（Blandford & Eichler 1987）
>
> 上一章：`02_observational_background.md`
>
> 下一章：`04_test_particle_approximation.md`
>
> 总览：`00_overview.md`

# 3. The Diffusion Approximation — 扩散近似理论

## 3.1 本节核心内容

§3 是 DSA 理论的**数学基础**——从 Vlasov 方程出发，推导出描述粒子在磁流体力学湍流中运动的传输方程。覆盖六个子节：

| 子节 | 主题 | 关键产出 |
|---|---|---|
| §3.1 | 分布函数 | 六维相空间分布函数 $f(\mathbf{x},\mathbf{p},t)$ |
| §3.2 | Fermi 加速 | 二阶 Fermi 机制的局限 |
| §3.3 | 动量空间扩散 | Fokker-Planck 方程 |
| §3.4 | 方位角散射与空间输运 | Alfvén 波共振散射理论 |
| §3.5 | 对流-扩散方程 | 完整传输方程 |
| §3.6 | 流体极限 | 宇宙线流体方程 |

## 3.2 §3.1 分布函数（原文核心内容）

宇宙线能量通过**一系列小增量**累积，可以视为在动量空间中扩散和/或被对流。同时存在空间扩散。因此用**六维相空间分布函数** $f(\mathbf{x},\mathbf{p},t)$ 描述粒子，其中 $f \, d^3x \, d^3p$ 为 $d^3x \, d^3p$ 中的粒子数。$f$ 是 Lorentz 不变的，满足相对论性 Vlasov 方程：

$$\frac{\partial f}{\partial t} + \mathbf{v} \cdot \frac{\partial f}{\partial \mathbf{x}} + \frac{\mathbf{F}}{m} \cdot \frac{\partial f}{\partial \mathbf{p}} = 0$$

其中 $\mathbf{v}$ 是粒子速度，$\mathbf{F} = d\mathbf{p}/dt$ 是电磁力。当 $\mathbf{F}$ 为电磁力时，第三项可改写为 $\mathbf{F} \cdot (\partial f / \partial \mathbf{p})$。

B&E 的目标是将此 Vlasov 方程转化为**Boltzmann 方程**（含碰撞项），再进一步转化为**传输方程**。

## 3.3 §3.2 Fermi 加速

B&E 从 Fermi (1949) 原始理论开始回顾：

### 幂律谱的通用论证

Fermi 指出：若宇宙线持续注入加速区，且**能量增益率与能量成正比**（$\dot{E} = E/\tau_{\rm acc}$），同时逃逸是**能量无关的 Poisson 过程**（逃逸率 $1/\tau_{\rm esc}$），则稳态粒子分布为幂律：

$$\frac{dN}{dE} \propto E^{-\gamma}$$

其中：

$$\gamma = 1 + \frac{\tau_{\rm acc}}{\tau_{\rm esc}}$$

### 赌徒类比

Fermi 用赌徒类比：赌徒以概率 $(1-p)$ 赢分额 $f$，以概率 $p$ 输光。最终赢家人数分布：

$$N(w) \propto w^{-(1 + p/f)}$$

### 二阶 Fermi 机制

Fermi 原始方案中，宇宙线与**星际云**碰撞获得能量：

$$\Delta E / E \sim (u/c)^2$$

其中 $u$ 为云速度。

**二阶 Fermi 的三个问题**：

1. **效率低**：加速率 $\propto (u/c)^2$——对 $u \sim 10^{-3}c$，$\tau_{\rm acc} \sim (c/u)^2 \sim 10^6$ 碰撞次
2. **谱指数无物理约束**：需要 $\tau_{\rm acc} / \tau_{\rm esc} \sim 7$，无物理理由
3. **离子化损失**：$T < 100$ MeV 时加速无法克服离子化损失

> **分析 / Interpretation**：这三个问题是 DSA 试图解决的核心困难。DSA 将二阶升级为**一阶**——能量增益率从 $(u/c)^2$ 提升到 $u/c$，效率提升 $\sim c/u \sim 1000$ 倍。

### 现代变体

Fermi 机制的现代变体用**磁流体力学波**替代"星际云"，但核心困难仍在——除非波的运动有系统性的方向偏好（这正是 DSA 激波两侧汇聚流提供的）。

## 3.4 §3.3 动量空间扩散（Fokker-Planck 方程）

单次碰撞的动量变化很小，可以用**Fokker-Planck 形式**处理。假设过程是 Markov 过程：

$$f(\mathbf{p}, \mathbf{x} + \mathbf{v}\Delta t, t + \Delta t) = \int d(\Delta \mathbf{p}) \, \phi(\mathbf{p} - \Delta \mathbf{p}, \Delta \mathbf{p}) \, f(\mathbf{p} - \Delta \mathbf{p}, \mathbf{x}, t)$$

Taylor 展开得到 Fokker-Planck 方程：

$$\frac{\partial f}{\partial t} + \mathbf{v} \cdot \frac{\partial f}{\partial \mathbf{x}} = \frac{\partial}{\partial p_i} \left\langle \frac{\Delta p_i}{\Delta t} \right\rangle + \frac{1}{2} \frac{\partial^2}{\partial p_i \partial p_j} \left\langle \frac{\Delta p_i \Delta p_j}{\Delta t} \right\rangle$$

**细致平衡原理**下（散射体反作用可忽略），$q(\mathbf{p}, -\Delta \mathbf{p}) = q(\mathbf{p}, \Delta \mathbf{p})$，方程简化为：

$$\frac{\partial f}{\partial t} + \mathbf{v} \cdot \frac{\partial f}{\partial \mathbf{x}} = \frac{1}{p^2} \frac{\partial}{\partial p} \left( p^2 D_{pp} \frac{\partial f}{\partial p} \right)$$

其中**动量空间扩散系数**：

$$D_{pp} = \frac{1}{2} \left\langle \frac{(\Delta p)^2}{\Delta t} \right\rangle$$

**最简单情况**——各向同性散射、各向同性散射体分布、散射体速度 $V \ll c$：

$$D_{pp} = \frac{p^2 V^2}{6 L v}$$

其中 $L$ 是碰撞平均自由程，$v$ 是粒子速度。

> **分析 / Interpretation**：$D_{pp} \propto p^2$ 意味着能量增益率 $\dot{E} \propto E$——这正是幂律谱的成因。对于相对论粒子这成立，对非相对论粒子不成立。

## 3.5 §3.4 方位角散射与空间输运

### 逃逸时间形式

最简单形式：在传输方程右侧加 $f/\tau_{\rm esc}$ 项。加速区被视为"漏箱"（leaky box）。对银河系 CR，此近似意外地好。

**稳态解**：

$$S(E) = \frac{f(E)}{\tau_{\rm esc}} + \frac{1}{p^2} \frac{d}{dp}\left(p^2 D_{pp} \frac{df}{dp}\right)$$

### Alfvén 波散射

粒子被**Alfvén 波**散射——不可压缩横向磁流体模式，由场张力 $B^2/4\pi$ 驱动，以 Alfvén 速度传播：

$$V_A = \frac{B}{\sqrt{4\pi\rho}}$$

**共振条件**：粒子 Larmor 半径 $\sim$ 波波长时发生共振散射。粒子速度远大于 $V_A$ 时，粒子看到的波几乎是**静磁场**扰动。

Larmor 半径：$r_L = pc / ZeB$

**散射率推导**：在波的参考系中，电场消失。粒子绕磁力线做回旋运动，波的磁场 $\mathbf{B}_1$ 改变粒子动量：

$$\frac{dp_\perp}{dt} = Ze \, \mathbf{v}_\perp \times \mathbf{B}_1$$

最低阶扰动下：

$$\Delta p_\perp = Ze v(1-\mu^2)^{1/2} B_1 \cos[(k v_\parallel - \Omega)t + \phi]$$

只有**共振波** $k v_\parallel \approx \Omega$（$\Omega = ZeB/\gamma mc$ 为回旋频率）才能强烈相互作用。

**方位角扩散系数**（准线性理论）：

$$D_{\mu\mu} = \frac{\pi \Omega^2 (1-\mu^2)}{2} \frac{W(k = \Omega/v_\parallel)}{B^2}$$

其中 $W(k)$ 是波能量密度谱。

**关键结果**——粒子分布函数的 Fokker-Planck 方程：

$$\frac{\partial f}{\partial t} + v\mu \frac{\partial f}{\partial x} = \frac{1}{p^2} \frac{\partial}{\partial p}\left(p^2 D_{pp} \frac{\partial f}{\partial p}\right) + \frac{1}{\mu^2} \frac{\partial}{\partial \mu}\left((1-\mu^2) D_{\mu\mu} \frac{\partial f}{\partial \mu}\right)$$

### 空间扩散系数

平行于场的扩散系数：

$$D_\parallel \sim \frac{v^2}{3\nu} \propto \frac{1}{W(k_{\rm res})}$$

即与共振波湍流水平**反比**——湍流越强，扩散越慢。

垂直于场的扩散：

$$D_\perp \sim D_\parallel \left(\frac{\delta B}{B}\right)^2$$

**磁场线漂移**（gradient B drift）给出非对角项：

$$D_\perp = -\frac{v^2}{3\Omega}$$

**磁场线游荡**（field line wandering）：两条起始靠近的磁力线以分离速率 $ds/dz = (8\pi k W_k / B^2) k$ 分开。

### 散射的困难——$\mu \to 0$ 的"盲区"

当粒子方位角接近 $90°$（$\mu \to 0$），共振 $k$ 趋于无穷大，准线性理论失效。**非线性效应**（粒子镜像效应 + 共振展宽）允许粒子通过 $\mu = 0$——这对激波穿越至关重要。

> **分析 / Interpretation**：§3.4 建立了完整的双向扩散理论——动量空间（§3.3）和位置空间（§3.4）——为 §3.5 的完整传输方程奠定基础。关键假设是准线性理论（小振幅、随机相位、$k \parallel B$），这些在真实激波中可能全部违反。

## 3.6 §3.5 对流-扩散方程

（将在下一分章与 §4 一起深入处理，此处只概述框架）

完整传输方程形式：

$$\frac{\partial f}{\partial t} + (\mathbf{V} + \mathbf{v}) \cdot \nabla f = \frac{1}{p^2}\frac{\partial}{\partial p}\left(p^2 D_{pp} \frac{\partial f}{\partial p}\right) + \frac{1}{p^2} \frac{\partial}{\partial \mu}\left((1-\mu^2) D_{\mu\mu} \frac{\partial f}{\partial \mu}\right) + \nabla \cdot (D_\parallel \nabla_\parallel f + D_\perp \nabla_\perp f)$$

这是 DSA 理论的核心方程。§4 将在**测试粒子近似**下求解它。

## 3.7 §3.6 流体极限

当扩散系数 $D_\parallel \to \infty$（各向同性极限），宇宙线可视为**流体**：

$$n_{\rm cr} = \int f \, d^3p$$
$$p_{\rm cr} = \frac{1}{3} \int p v f \, d^3p$$

得到宇宙线流体方程组，可与背景 MHD 方程耦合——这是 §6 非线性理论的基础。

## 3.8 关键公式速查

| 编号 | 公式 | 出处 | 物理意义 |
|---|---|---|---|
| 3.1 | Vlasov 方程 | §3.1 | 相空间分布的基本演化方程 |
| 3.2 | $dN/dE \propto E^{-\gamma}$，$\gamma = 1 + \tau_{\rm acc}/\tau_{\rm esc}$ | §3.2 | 幂律谱通用条件 |
| — | $D_{pp} = p^2 V^2 / (6Lv)$ | §3.3 | 动量空间扩散系数 |
| — | Fokker-Planck 方程 | §3.3 | 动量空间传输方程 |
| 3.12 | $V_A = B / \sqrt{4\pi\rho}$ | §3.4 | Alfvén 速度 |
| 3.13 | $dp_\perp/dt = Ze\mathbf{v}_\perp \times \mathbf{B}_1$ | §3.4 | 波场中的动量变化 |
| 3.16 | $D_{\mu\mu} = \pi\Omega^2(1-\mu^2) W(k)/2B^2$ | §3.4 | 方位角扩散系数（准线性）|
| 3.18 | Fokker-Planck with $D_{\mu\mu}$ | §3.4 | 方位角 Fokker-Planck |
| 3.20 | $D_\perp \sim D_\parallel (\delta B/B)^2$ | §3.4 | 垂直扩散系数 |
| 3.21 | $ds/dz = (8\pi k W_k / B^2)k$ | §3.4 | 磁场线游荡速率 |

## 3.9 作者的逻辑

```
Vlasov 方程（六维相空间）
→ Fermi 原始机制：二阶，三个问题
→ Fokker-Planck 方程：动量空间扩散
→ Alfvén 波散射：方位角扩散（准线性理论）
→ 空间扩散：平行/垂直/非对角
→ 完整传输方程
→ 流体极限
```

## 3.10 潜在问题与值得关注的地方

1. **准线性理论的局限**：小振幅、随机相位、$k \parallel B$ 三个假设在强激波中可能全部违反。§5 的"非线性计算"试图解决此问题。

2. **$\mu = 0$ 盲区**：准线性理论在 $\mu \to 0$ 时失效——需要非线性效应。这对激波穿越至关重要。

3. **$D_{pp} \propto p^2$ 与谱指数**：这个比例关系直接导致幂律谱。若偏离，谱形会改变。

4. **动量空间扩散 vs 逃逸时间**：B&E 指出逃逸时间近似（leaky box）意外地好——但只有在注入谱接近 $E^{-2}$ 时才成立。