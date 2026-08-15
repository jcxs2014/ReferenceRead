> 本章属于：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/00_overview.md|Particle Acceleration by Astrophysical Shocks（Blandford & Ostriker 1978）]]
>
> 上一章：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/01_introduction.md|01_introduction]]
>
> 下一章：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/03_cosmic_ray_application.md|03_cosmic_ray_application]]
>
> 总览：`00_overview.md`

# 2. Acceleration by a Strong Shock — 强激波加速（核心推导）

## 2.1 本节核心内容

这是 BO 论文的核心——§II 给出**完整的数学推导**，证明激波处 Alfvén 波散射粒子产生幂律动量分布，且指数由压缩比 $r$ 唯一确定。推导结构：

1. 建立坐标系与假设
2. 写出扩散-对流方程
3. 在激波两侧求解，应用连接条件
4. 得到幂律解 $f(p) \propto p^{-q}$，$q = 3r/(r-1)$
5. 讨论瞬态建立时间和绝热冷却修正

## 2.2 原文内容

### 几何设置

BO 考虑一个强激波，密度跳跃比为 $r$：

$$r = \frac{u_-}{u_+} = \frac{\tan\theta_+}{\tan\theta_-}$$

其中下标 $-$ 和 $+$ 分别表示激波上游（$x < 0$）和下游（$x > 0$），$u_\pm$ 为激波系中流体速度，$\theta_\pm$ 为磁场与激波法线的夹角。

### 关键假设

BO 明确列出四个长度尺度的排序：

$$\delta \ll r_L \ll L \ll H$$

- $\delta$：激波厚度（电离 Larmor 半径量级）
- $r_L$：宇宙线 Larmor 半径
- $L \sim D/u_-$：扩散长度（$D$ 为扩散系数）
- $H$：后激波流体尺度（如 SNR 半径）

第一个不等式通常成立；第二个对弱湍流不可违反；第三个若被违反会降低加速效率。

> **分析 / Interpretation**：这个排序的物理意义是——粒子在激波厚度尺度内做无碰撞扩散，扩散范围远小于源尺度（所以可以处理为一维问题），但又远大于激波厚度本身（所以激波本身不是点源）。

### 湍流假设

BO 假设激波附近存在波速 $w \ll u$ 的波湍流，散射粒子在方位角 $\phi$ 上的速率满足：

$$\left\langle \frac{\Delta\phi^2}{\Delta t} \right\rangle = \nu$$

该散射倾向于使分布函数在背景介质参考系中各向同性化。

## 2.3 关键公式

### 公式（1a）：扩散-对流方程

这是全篇核心方程——描述激波附近各向同性部分 $f(p,x)$ 的演化：

$$K_\pm(u \pm V) \frac{\partial f}{\partial x} - V \cdot \nabla (D_\parallel \hat{n}\hat{n} \cdot \nabla f) = K_\pm(u_\pm - w_-) \delta(x) [f_+ - f_-]$$

> **分析 / Interpretation**：左边是扩散-对流项，右边是源项（激波厚度视为 $\delta$ 函数）。$D_\parallel$ 是沿磁场方向的扩散系数，$u$ 是粒子速度，$V$ 是流体速度。

### 公式（1b）：沿磁场扩散系数

$$D_\parallel = \frac{v^2}{4} \int_0^\pi \sin^3\phi \, d\phi \, \langle\Delta\phi^2/\Delta t\rangle^{-1}$$

即粒子扩散系数由散射率 $\nu$ 决定：散射越强（$\nu$ 越大），扩散越慢（$D_\parallel$ 越小）。

### 公式（1c）：粒子能量通量连续性

$$-u \frac{\partial f}{\partial \ln p} - K_\pm \nabla f \to 0 \quad (u_- / u_+)$$

其中 $\kappa = D_\parallel \cos^2\theta$。在稳态解中，通量 $uf - \kappa\nabla f$ 在激波两侧必须分别守恒（连续性条件）。

### 激波两侧解的构造

下游（$x > 0$）：当 $f \to 0$ 时，解渐近趋于 $f = f_+$。

上游（$x < 0$）：

$$f = f_- + (f_+ - f_-) \exp\left[-\int_{-\infty}^x \frac{u_-\, dx'}{\kappa(x')} \right]$$

> **分析 / Interpretation**：上游解呈现指数衰减，衰减长度正是扩散长度 $L \sim \kappa / u_-$。粒子密度从激波面 $x=0$ 处向上游指数衰减——这正是 DSA 的"加速区"。

### 公式（2）：幂律解

应用连接条件（$f$ 连续，能量通量 $uf - \kappa\nabla f$ 连续）得到：

$$\frac{df_+}{d\ln p} = \frac{(f_+ - f_-) u_-}{(u_+ - u_-) p}$$

解为：

$$f_+(p) = \frac{n \, p_0^{\,q}}{4\pi(q-3)} \, \theta(p - p_0) \, p^{-q}$$

其中**谱指数**：

$$\boxed{q = \frac{3r}{r-1}}$$

这是全篇最重要的公式。对理想强激波 $r = 4$：

$$q = \frac{3 \times 4}{4 - 1} = 4$$

> **分析 / Interpretation**：$r = 4$ 是理想强激波（绝热指数 $\gamma = 5/3$）的压缩比。$q = 4$ 意味着动量谱 $f \propto p^{-4}$，对应积分粒子能谱 $\propto E^{-3}$——与观测的 $4 < s < 5$ 大致一致但略偏低。

### 低能注入修正

如果上游入射谱 $f_- \propto p^{-s}$ 且 $s < q$，则下游谱 $f_+ = [q/(q-1)] f_- p^{-s}$——即入射谱形状被保留。若 $s > q$，则低能粒子被加速成 $f_+ \propto p^{-q}$ 的 DSA 谱。

### 平均能量增益

对非相对论粒子：
$$\langle \Delta E \rangle / E = \frac{3}{5 - 2r}, \quad r < 2.5$$

对超相对论粒子：
$$\langle \Delta E \rangle / E = \frac{3}{4 - r}, \quad r < 4$$

> **分析 / Interpretation**：当 $r \to 4$ 时非相对论增益分母趋于 $-3$（负值），说明对于超强激波，非相对论粒子被加热而非加速。只有超相对论粒子在 $r < 4$ 时有正增益——这限制了 DSA 适用的能量范围。

### 瞬态建立时间

$$t_{\rm est} \sim \frac{r^2}{\nu} \cdot \frac{1}{u_-^2}$$

由上游散射率 $\nu$ 决定。$t_{\rm est}$ 越长，稳态加速越慢。

### 绝热冷却修正

如果激波后介质在时间 $\tau \sim H^2/(K_+ u_+)$ 内膨胀回未激波密度，粒子会绝热冷却：

$$f_+(p) \to f_+(p) \cdot r^{-s/3}$$

但谱形不变——绝热冷却不改变幂律指数。

## 2.4 关键参数

| 参数 | 公式 | 值（典型） |
|---|---|---|
| 压缩比 $r$ | $u_-/u_+$ | $4$（强激波）|
| 谱指数 $q$ | $3r/(r-1)$ | $4$（$r=4$ 时）|
| 扩散长度 $L$ | $D/u_-$ | $\sim 10^{18}$ cm |
| 建立时间 | $r^2/(\nu u_-^2)$ | 取决于 $\nu$ |
| 平均能量增益 | $3/(5-2r)$（非相对论）| $-1$（$r=4$，无效）|
| 平均能量增益 | $3/(4-r)$（超相对论）| $3$（$r=4$ 发散）|

## 2.5 图表分析

本文无插图（§II 全文为推导，无 Figure）。

## 2.6 作者的逻辑

```
强激波几何（$r$，$u_-$，$u_+$）
→ 假设存在 Alfvén 波散射（$\nu$）
→ 写出扩散-对流方程（公式 1a）
→ 求解：上游指数衰减，下游常数（公式 1c 解）
→ 应用激波面连接条件（$f$ 连续 + 能量通量连续）
→ 得到 df+/dlnp 与 (f+−f−) 的关系
→ 幂律解：q = 3r/(r−1)
→ 讨论：瞬态时间、绝热冷却修正
```

## 2.7 我的理解

### 公式（2）的深刻含义

$q = 3r/(r-1)$ 这个简单表达式包含了 DSA 的物理本质：

- 分子 $3r$ 来自压缩比和三维空间的因子
- 分母 $r-1$ 来自"逃逸率"——粒子穿越激波的净速率
- 当 $r = 1$（无激波），$q \to \infty$（无加速）
- 当 $r \to \infty$，$q \to 3$（极限情况）

> **分析 / Interpretation**：这个关系是**普适的**——不依赖于散射的具体机制（Alfvén 波、磁湍流等），只依赖压缩比和几何。这解释了为什么在 SNR、AGN jet、星系团等多种环境中观测到的宇宙线谱指数大致一致。

### 与 Fermi (1949) 一阶机制的对应

BO 指出，这个一阶过程的本质是**激波面两侧流体的汇聚**。粒子在激波两侧被 Alfvén 波散射，反复穿越激波面，相当于在两个相对运动的"镜子"间被反射。每次穿越获得的能量增益正比于 $u_- - u_+$——一阶量。

这与 Fermi 1949 的"运动磁云"类比完全一致，但**效率更高**：因为粒子无法逃逸（扩散被激波汇聚困住），加速持续进行直到粒子能量足够大使其 Larmor 半径超过激波尺度。

## 2.8 潜在问题与值得关注的地方

1. **湍流假设的自洽性**：BO 假设 $\nu$ 足够大使粒子各向同性化，但 $\nu$ 的具体值由 Alfvén 波振幅决定。如果 Alfvén 波由宇宙线 streaming 自激发（见 §III），则需要证明自激发增长率快于加速率。

2. **谱指数与观测的偏差**：$q = 4$（$r = 4$ 时）比观测的 $s \approx 4.5$ 偏小。BO 用激波逐渐变为 Alfvénic 导致效率降低来解释，但这需要详细计算（"will be described elsewhere"）。

3. **公式的普适性**：$q = 3r/(r-1)$ 在**各向同性散射假设下**成立。如果散射是各向异性的（如 Alfvén 波只散射特定 $\phi$），谱指数会偏离。

4. **无磁场方向的依赖**：BO 的推导假设可以忽略磁场方向 $\theta$ 的影响（通过坐标变换到 $u \parallel B$ 的参考系）。对于倾斜激波（$\theta_- \neq 0$），这一假设可能不完全成立。