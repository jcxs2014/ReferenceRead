---
title: "§5 THE ROLE OF NRH MODES"
paper: "Caprioli & Spitkovsky 2014, ApJ 794, 46"
outline_ref: "§5 THE ROLE OF NRH MODES"
---
> 上一章：[[02_cosmic-ray-origins/0017_caprioli-2014-ii/literature_analysis/04_turbulence_spectrum.md|04_turbulence_spectrum]]
> 下一章：[[02_cosmic-ray-origins/0017_caprioli-2014-ii/literature_analysis/06_conclusions.md|06_conclusions]]

#### 5.1 [FACT] NRH 不稳定性的理论背景

- **[FACT]** §4 中放大水平与谱都与**共振流不稳定性**一致——但存在一个**短波长不稳定性**：**非共振混合（NRH）不稳定性**（Bell 2004, 2005），预言其增长快于共振
- **[FACT]** 不同"流"不稳定性可通过**线性化**对齐背景磁场的圆极化波的色散关系获得（Krall & Trivelpiece 1973），包含电子回返电流抵消正 CR 电流（Amato & Blasi 2009 详细动力学推导）
- **[FACT]** **左旋**（与质子同向）→ 共振支；**右旋**（与电子同向）→ 非共振（NRH）支

#### 5.2 [FACT] 增长率与最不稳定波数（准线性）

- **[FACT]** 动量 $p$、速度 $v_{\rm CR}$ 的离子上游传播电流贡献的最大增长率（Amato & Blasi 2009 公式 28）：
$$\Gamma_{\rm res}(p) \simeq \frac{m v_{\rm CR}}{2\pi} \cdot \frac{\epsilon_{\rm CR}(p)\,v_{\rm CR}}{c}, \qquad \Gamma_{\rm nrh}(p) \simeq \epsilon_{\rm CR}(p) \frac{v_{\rm CR}}{2 v_A} \qquad (9)$$
其中 $\epsilon_{\rm CR}(p) \equiv n_{\rm CR}(>p)/n$ 为能量 $>p$ 的 CR 密度归一化
- **[FACT]** $v_{\rm CR}$ 为**随上游流体运动的波所见** CR 整体速度：
  - 扩散 CR（激波系各向同性）：$v_{\rm CR} \simeq v_{\rm sh}$
  - **逃逸 CR**（自由流动）：$v_{\rm CR} \sim 2E_{\max}/m$（相对论 CR：$v_{\rm CR} \sim c$）
- **[FACT]** 最不稳定波数：$K_{\rm res} \sim 1/r_L(p)$；$K_{\rm nrh} \sim \epsilon_{\rm CR}/v_A$
- **[FACT]** NRH 增长率严格依赖**所有流 CR 的电流**；共振只由 $p \gtrsim 1/K_{\rm res}$ 的 CR 驱动
- **[FACT]** $K_{\rm nrh} r_L(p) = \epsilon_{\rm CR} M^2 \ll 1$（$M \equiv v_{\rm CR}/v_A$ 为 CR 电流有效阿尔芬马赫）——NRH 模式波长远小于驱动离子回旋半径

#### 5.3 [FACT] NRH 与共振增长率的比值与机制切换判据

- **[FACT]** 增长率比（Amato & Blasi 2009）：
$$W(p) \equiv \frac{\Gamma_{\rm nrh}}{\Gamma_{\rm res}} = M \,\epsilon_{\rm CR}(p)\,\frac{v_{\rm CR} p}{m v_A} \simeq M\,\epsilon_{\rm CR}(mv_{\rm CR}) \qquad (10)$$
（假设 $f(p) \propto p^{-4}$ 的 $\epsilon_{\rm CR}(p) \propto 1/p$）
- **[FACT]** 扩散 CR：$M \sim M_A$，$\epsilon_{\rm CR}(mv_{\rm sh}) \sim 10^{-3}$（Part I）
- **[FACT]** **判据**：$\Gamma_{\rm nrh} > \Gamma_{\rm res} \Leftrightarrow M_A W / \epsilon_{\rm CR} \gtrsim 30$，即 **$M_A \gtrsim 30$ 时 NRH 增长快于共振**（Amato & Blasi 2009）

#### 5.4 [FACT] NRH 非线性色散关系与饱和机制（Riquelme & Spitkovsky 2009）

- **[FACT]** Riquelme & Spitkovsky (2009) 导出 NRH 非线性色散关系，可求 $\Gamma/b$ 与 $\Gamma$ 对任意放大因子 $b$ 的依赖
- **[FACT]** 从他们附录 A 式 (A12) 的虚部得到 $b$ 的微分方程；代回实部得（$v_A \ll c$ 极限）：
$$\frac{\Gamma^2}{v_A^2} = \frac{k(2K_0 - k)K_0^2\,(2b^2 + 1)}{b+1}\cdot\frac{\epsilon_{\rm CR}}{M_0^2}\cdot\frac{c^2}{v_A^2} \qquad (11)$$
其中下标 0 为初始量（$b=1$），$\Gamma(k)$ 为 $k$ 模式增长率，$K_0$ 为最快增长模式
- **[FACT]** $b \gg 1$ 时 $v_A^2 \simeq v_{A,0}^2 (b^2+1)$
- **[FACT]** 最快模式增长率：
$$\Gamma(b) \simeq v_{A,0} K_0\sqrt{\frac{2b^2+1}{M_0^2}}\left(1 - \frac{2}{M_0^2}\right) \qquad (12)$$
适用于 $1 \ll 2b^2 \ll M_0^2$
- **[FACT]** 积分 $\dot{b}(t) = \Gamma(b)$（$b(0) \simeq 1$）：
$$b(t) \simeq \frac{e^{\Gamma_0 t}\sqrt{M_0^2 - M_0\sqrt{M_0^2-2}}}{1 - e^{2\Gamma_0 t}\sqrt{M_0^2-1} + M_0\sqrt{M_0^2-2}} \qquad (13)$$
- **[FACT]** **最大放大**：$b_{\max} \simeq M_0/\sqrt{2}$（此时 $\Gamma(b_{\max}) \simeq 0$）
- **[FACT]** 达到时间 $\Gamma_0 t_{\max} \simeq \ln(\sqrt{2} M_0)$
- **[FACT]** 上述与 PIC/hybrid 受控离子束模拟（Riquelme & Spitkovsky 2009；Gargatè et al. 2010）高度一致：饱和时 $b_{\max} \sim M_0$；指数阶段持续 $t \sim 3$–$5\,\Gamma_0^{-1}$；几倍 $t_{\max}$ 后饱和

#### 5.5 [FACT] SNR 中的物理含义

- **[FACT]** 对 ISM 中相对论 CR，$b_{\max} \sim c/v_A \sim 20$–$30$——SNR 逃逸粒子在**各向同性化之前**可**预先放大 ISM 磁场超过一个量级**（Bell et al. 2013）
- **[FACT]** $\epsilon_{\rm CR} M_0 \gg 1$ 是 NRH 非线性增长的必要条件 → 给出与 CR 密度**无关的** $b$ 上限：$b \lesssim 3 M_0$

#### 5.6 [FACT] 两个区域的划分与自由逃逸边界

- **[FACT]** 真实激波 precursor 存在**两个区域**：
  - **(1) 远上游**：电流由**自由流动**离子提供（$E \gtrsim E_{\max}$），激发短波长 NRH 模式
  - **(2) CR precursor**：电流由**扩散 CR** 维持（$v_{\rm CR} \sim v_{\rm sh}$）
- **[FACT]** 两区域分界由 $b \simeq b_{\rm crit}$ 标记 → **自由逃逸边界**（free-escape boundary）（Caprioli et al. 2010 及文内引用）
- **[FACT]** 动力学修改仅发生在 precursor（CR 有效磁化，可对入射流体施压）；逃逸粒子仍可带走能量，使激波表现得**部分辐射**（Caprioli et al. 2009a）

#### 5.7 §5.1 [FACT] 自由逃逸边界的具体确定

- **[FACT]** 周期性盒子与真实 precursor 关键差异：**CR 电流非固定**，由自生湍流中散射决定
- **[FACT]** 最不稳定模式 $K_0$ 无法偏转电流离子（右旋 + 短波长，$K_0 r_L(v_{\rm CR}) \simeq \epsilon_{\rm CR} M^2 \ll 1$）
- **[FACT]** 非线性下最快波数减小：$K(b) \simeq K_0/b^2$（Riquelme & Spitkovsky 2009）→ $K(b) r_L(b) \sim b^{-3}$
- **[FACT]** 存在临界放大 $b_{\rm crit} \sim 3\sqrt{\epsilon_{\rm CR}} M_0$：NRH 波长变得与驱动离子回旋半径相当，$K(b) r_L(b) \sim 1$
- **[FACT]** 非线性阶段：右旋 NRH 模式**波长逐渐增大**，最终与驱动离子共振 → 离子被散射，电流被破坏

#### 5.8 [FACT] 模拟验证

- **[FACT]** 在长时间全局模拟中通过**偏振**区分共振与 NRH 模式（Gargatè & Spitkovsky 2012）
- **[FACT]** $M \lesssim 30$ 时 NRH 预期不显著：**$M=20$ 上游偏振主要为左旋**（共振/Alfvén）；$F(k)$ 可由共振流不稳定性解释（图 6）
- **[FACT]** $M=80$（Run D）上游**以右旋为主**（NRH）
- **[FACT]** $M=80$ 远上游 $F(k)$ 在小于 $r_L(E_{\max} \sim 100 E_{\rm sh})$ 的波长处有峰值（图 7）——随接近激波，该峰值**向长波长迁移**，最终匹配 $E_{\max}$ 共振波数
- **[FACT]** Run D 中逃逸 CR 密度 $\epsilon_{\rm CR}(E \gtrsim E_{\max}) \sim 10^{-4}$，对它们 $M_0 \sim M_A E_{\max}/E_{\rm sh}$ → 最快模式增长率 $\Gamma_0 \sim 0.07\,\omega_c$
- **[FACT]** Run D 足够长足够大以使最快模式饱和：$t_{\rm sat} \sim \ln(M)/\Gamma_0 \sim 100\,\omega_c^{-1}$，$L_{\rm sat} = v_{\rm sh} t_{\rm sat} \sim 8000\,c/\omega_p$
- **[FACT]** 估计 $b \simeq 3.7$——与图 7 中 precursor 与远上游边界处（$x \sim 2\times10^4\,c/\omega_p$）**放大量级一致**

#### 5.9 [FACT] 低 $M$ 下的自由逃逸边界

- **[FACT]** 低 $M$ 激波中，场放大通常在线性区，共振与 NRH 增长率几乎相同 → 逃逸离子电流更易被破坏，激波 precursor 延伸约一个最大能量离子扩散长度
- **[FACT]** 完整粒子扩散与扩散系数参数化 → 留给 Paper III

#### 5.10 [FACT] 结论的谨慎性

- **[FACT]** 主要发现基于 **2D** 有限横向尺寸模拟（至 $M=80$）；Run C（$M=100$，大横向）显示细丝化对强激波重要——1D 描述**可能无法捕捉**磁湍流的增长与饱和
- **[FACT]** 但细丝化**增强**了磁湍流产生（上下游均然）（CS13）→ 有限横向尺寸**给出磁场放大的下限**
- **[FACT]** 对 §4.1 仅含共振不稳定性的输运方程在高 $M$ 的适用性：方程 (4)–(8) 在 **precursor** 内仍适用；完整上游输运方程**还应包含逃逸 CR 电流与波长迁移**——但 (5) 式仍捕获了量级正确的增长率，对图 5 总放大因子拟合良好

## 关键参数

| 参数 | 值 | 出处 |
|------|-----|------|
| 机制切换 $M_A$ | $\gtrsim 30$ | (10) |
| $\epsilon_{\rm CR}(mv_{\rm sh})$ | $\sim 10^{-3}$ | Part I |
| $K_{\rm nrh} r_L(p)$ | $= \epsilon_{\rm CR} M^2 \ll 1$ | §5.2 |
| $K(b) \simeq K_0/b^2$ | NRH 非线性 | R&S2009 |
| $b_{\max}$ | $\simeq M_0/\sqrt{2}$ | (13) |
| $\Gamma_0 t_{\max}$ | $\simeq \ln(\sqrt{2} M_0)$ | (13) |
| $b_{\rm crit}$ | $\sim 3\sqrt{\epsilon_{\rm CR}} M_0$ | §5.1 |
| Run D 逃逸 CR $\epsilon_{\rm CR}$ | $\sim 10^{-4}$ | §5 |
| Run D $\Gamma_0$ | $\sim 0.07\,\omega_c$ | §5 |
| Run D $t_{\rm sat}$, $L_{\rm sat}$ | $\sim 100\,\omega_c^{-1}$, $\sim 8000\,c/\omega_p$ | §5 |
| Run D 边界 $b$ 实测 | $\simeq 3.7$ | §5 |
| ISM 相对论 CR $b_{\max}$ | $\sim c/v_A \sim 20$–$30$ | §5 |

## 我的理解 / Interpretation

**[INTERPRETATION]** §5 是本文**最具理论贡献**的部分：将 Riquelme & Spitkovsky 2009 的 NRH 非线性色散关系引入全局激波模拟，定量解释（1）$M \gtrsim 30$ 时放大水平高于共振预言，（2）$F(k)$ 峰值偏离共振波数，（3）自由逃逸边界位置。三个关键物理量（$b_{\max} \sim M_0/\sqrt{2}$、$b_{\rm crit} \sim 3\sqrt{\epsilon_{\rm CR}}M_0$、$K(b) \propto b^{-2}$）共同构成一个**自洽的自由逃逸边界模型**，为唯象 DSA 提供了可闭合的输入。
