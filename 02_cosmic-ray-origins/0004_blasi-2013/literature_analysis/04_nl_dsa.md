# 4. The non-linear theory of diffusive shock acceleration

> 本章属于：The Origin of Galactic Cosmic Rays（Blasi, 2013, arXiv:1311.7346）
>
> 上一章：`03_test_particle_dsa.md`
>
> 下一章：`05_superbubble.md`

[FACT] §4 是全文的**方法论核心**：从 test-particle DSA 跃升到**非线性 DSA（NLDSA）**。三个一级子节（§4.1 加速粒子对激波的动力学反馈、§4.2 磁场放大、§4.3 放大磁场对激波的反向作用）构成"加速粒子→磁场→激波"的自洽闭合。§4.2 细分为四个二级子节（§4.2.1–§4.2.4），按"共振→非共振小尺度→filamentation→非共振大尺度"递进，是四种磁化放大机制的完整谱系。

[INTERPRETATION] §4 的逻辑链条是：**加速粒子反馈激波 → precursor + 子激波结构 → 谱凹性**（§4.1）→ **放大磁场如何产生**（§4.2 四机制）→ **放大磁场如何反过来改变激波**（§4.3）。作者的核心立场：在 $\xi_{\rm CR} \sim 10\%$ 的现实加速条件下，经典线性理论（$\delta B \sim B$）失效，必须引入非线性处理才能解释观测。

---

## 4.1 Dynamical reaction of accelerated particles

[FACT] §4.1 建立加速粒子对激波的动力学反馈机制，是 NLDSA 的理论起点。两种效应同时作用：**(1)** CR 压力在上游造成 **precursor**（流体提前减速）；**(2)** 最高能粒子逃逸使激波表现出**辐射激波类似**的特征（radiative-like），R$_{\rm tot}$ 可 $>7$。

[FACT] 守恒方程组（原文 Eq. 53–60），包含 CR 的动量与能量通量：

$$
\partial_t \rho + \nabla(\rho u) = 0 \quad \text{(Eq. 53, 质量守恒)}
$$

$$
\nabla(\rho u^2 + P_g + P_c) = 0 \quad \text{(Eq. 55, 含 CR 的动量守恒)}
$$

$$
\nabla\!\left(\tfrac{1}{2}\rho u^3 + \tfrac{\gamma_g}{\gamma_g-1} u P_g\right) = -u \nabla P_c \quad \text{(Eq. 60, 含 CR 能量守恒)}
$$

$$
\nabla\!\left(E_c u + \tfrac{\gamma_c}{\gamma_c-1} u P_c\right) = \nabla\!\cdot(\bar{D}\nabla E_c) + u \nabla P_c \quad \text{(Eq. 64, CR 能量方程)}
$$

其中 $E_c$、$P_c$ 分别为 CR 能量密度与压力（Eq. 62、63），$\bar{D}$ 为能量加权平均扩散系数。

[FACT] 准稳态下**子激波压缩比** R$_{\rm sub}$ 用上游马赫数 M$_1$ 表达（Eq. 68）；**总压缩比** R$_{\rm tot} = u_0/u_1$（Eq. 69）用 R$_{\rm sub}$ 与总马赫数 M$_0$ 表达：

$$
\boxed{R_{\rm tot} = \frac{u_0}{u_1}, \quad R_{\rm sub} = R_{\rm sub}(M_1) \quad \text{(Eq. 68, 69)}}
$$

[FACT] CR 诱导 precursor 的深度：

$$
\xi_{\rm CR}(z) \approx \frac{P_c(z)}{\rho_0 u_0^2} \approx 1 - \frac{u(z)}{u_0} \quad \text{(Eq. 70)}
$$

[FACT] **谱的凹性**（concavity）——NLDSA 的决定性特征："particles with low momentum experience a compression factor closer to R$_{\rm sub}$ $< 4$, while higher momentum particles trace a compression factor closer to R$_{\rm tot}$ $> 4$." 转折动量 ~GeV/c，低能段近 R$_{\rm sub}$（更陡），高能段近 R$_{\rm tot}$（更硬）。

[FACT] 三种计算 NLDSA 的方法论：**(i)** 有限差分（Berezhko & Völk；Zirakashvili & Ptuskin）；**(ii)** Monte Carlo（Ellison & Eichler；Knerr；Vladimirov）；**(iii)** 半解析（Malkov；Blasi 2002；Amato & Blasi）。

[INTERPRETATION] §4.1 的 precursor + subshock 双结构解释了为何 SNR 观测到的 $\gamma$ 射线谱偏硬：高能粒子"看到"的压缩比大于 4，谱指数低于 test-particle 极限。

---

## 4.2 Magnetic field amplification

[FACT] §4.2 是本章最长的子节，围绕**年轻 SNR 的 X 射线窄边缘**这一观测事实，论证为什么必须存在强磁场放大。观测给出边缘厚度 $\sim 10^{-2}$ pc，推断背景磁场 $B_0 \sim 1$–$6\;\mu$G 需放大到 $B \sim 100$–$1000\;\mu$G。

[FACT] 同步辐射诊断给出最大电子能量（Eq. 73）：

$$
E_{e,\max} \approx 34\, B_{100}^{-1/2}\, V_{\rm sh,8}\; \text{TeV}
$$

最大光子能量（Eq. 74，Bohm 假设下与 B **无关**）：

$$
E_{\gamma,\max} \approx 1.7\, V_{\rm sh,8}^2\; \text{keV}
$$

特征宽度（Eq. 75）：$\sqrt{D \cdot \tau_{\rm syn}} \approx 3.7\times 10^{-2}\, B_{100}^{-3/2}$ pc。观测到 $\sim 10^{-2}$ pc 窄边缘要求 B~几百 $\mu$G。

[FACT] 加速时间（Bohm，Eq. 71）与同步辐射损失时间（Eq. 72）：

$$
\tau_{\rm acc} \approx 3.3\times 10^7\, E_{\rm TeV}\, B_{100}^{-1}\, V_{\rm sh,8}^{-2}\; \text{s}
$$

$$
\tau_{\rm syn} = 4\times 10^{10}\, B_{100}^{-2}\, E_{\rm TeV}^{-1}\; \text{s}
$$

[FACT] 若取 ISM 背景扩散系数 $D = 3\times 10^{28}\,(E/10\;\text{GeV})^\delta$ cm$^2$/s，则 $\tau_{\rm acc}$ 远超 SNR 自由膨胀期（Eq. 76）——背景场不足以支撑 DSA。

[FACT] Bohm + B=100 $\mu$G + $T_s$=300 yr 时（Eq. 78），"all parameters chosen in the most optimistic way"：

$$
E_{\max} \approx 3\times 10^5\; \text{GeV}\;\cdot\, B_{100}\cdot\!\left(\frac{T_s}{300\;\text{yr}}\right)\cdot\!\left(\frac{V_{\rm sh}}{1000\;\text{km/s}}\right)^2
$$

[FACT] 磁化放大两种起源：**(i)** 激波波纹（shock corrugation，Giacalone & Jokipii 2007；Sano 2012）——下游放大；**(ii)** CR streaming 不稳定性——**上游**放大。"Qualitatively, extremely important difference."

[FACT] §4.2 按四种机制细分为 §4.2.1 共振 streaming 不稳定性 → §4.2.2 Bell 非共振小尺度模 → §4.2.3 filamentation 不稳定性 → §4.2.4 大尺度非共振 firehose 不稳定性。按"由经典到前沿"排列。

### 4.2.1 Resonant streaming instability

> **共振 streaming 不稳定性**

[FACT] 共振 streaming 不稳定性（Zweibel 1979；Achterberg 1983，原文 Eq. 79/87）增长率：

$$
\omega_{\rm I}(k) = \frac{\pi}{8}\, \Omega^*_p\, \frac{V_{\rm sh}}{v_A}\, \frac{n_{\rm CR}(p>p_{\rm res}(k))}{n_i}
$$

共振功率谱（Eq. 81）：

$$
F_0(k) = \frac{\pi}{4}\, \xi_{\rm CR}\, \frac{V_{\rm sh}}{v_A}\, \frac{1}{\Lambda}
$$

[FACT] **适用条件**（Eq. 86、88）——共振不稳定性仅在低 $\xi_{\rm CR}$ 时成立：

$$
\frac{n_{\rm CR}}{n_i} \ll \frac{v_A^2}{V_{\rm sh}\, c} \quad \Longleftrightarrow \quad \xi_{\rm CR} \ll 8\times 10^{-4}\, \left(\frac{V_{\rm sh}}{5\times 10^8\;\text{cm/s}}\right)^{-3}
$$

[FACT] **决定性结论**：对 $\xi_{\rm CR} \sim 10\%$ 的强加速 SNR，此条件**完全不成立**。"The resonant streaming instability does not operate in the regime relevant for SNR."

[CRITIQUE] 因此传统教科书结论 $\delta B/B \sim 1$ 的饱和机制在 SNR 强加速情形下**不适用**——这正是必须引入非线性处理（§4.2.2–§4.2.4）的根本原因。

### 4.2.2 Non-resonant small-scale modes from streaming instability

> **来自 streaming 不稳定性的非共振小尺度模式**

[FACT] 当 $\xi_{\rm CR}$ 大时进入 **CR modified regime**（原文 Eq. 89），增长率：

$$
\omega_{\rm I} \approx \omega_{\rm R} = \left[\frac{\pi}{8}\, \Omega^*_p\, k\, V_{\rm sh}\, \frac{n_{\rm CR}(p>p_{\rm res})}{n_i}\right]^{1/2}
$$

相位速度 $v_\phi \gg v_A$（远离 Alfvén 波特征）。

[FACT] 此条件下 $F_0 \leq 1$（Eq. 90）：

$$
F_0(k) = \left(\frac{\pi}{6}\right)^{1/2} \left(\frac{\xi_{\rm CR}}{\Lambda}\right)^{1/2} \left(\frac{c}{V_{\rm sh}}\right)^{1/2}
$$

"Efficient CR acceleration ... reduces the growth of the waves and limits the value of the self-generated magnetic field to the same order of magnitude as the pre-existing magnetic field."

[FACT] **Bell 非共振小尺度模**（Bell 2004, 2005）：$\xi_{\rm CR}$ 大时，右手极化模在 $k\, r_{L,0} > 1$ 出现非共振分支，增长率 $\propto k^{1/2}$，峰值在：

$$
k^*\, r_{L,0} = 3\, \xi_{\rm CR}\, \gamma_{\rm min} / \Lambda \cdot \left(\frac{V_{\rm sh}}{v_A}\right)^2 \cdot \frac{V_{\rm sh}}{c} > 1 \quad \text{(Eq. 92)}
$$

比共振模快 $(k^* r_{L,0})^{1/2}$ 倍。典型值 $k^* r_{L,0} \sim 10^4$。

[FACT] Bell 模**不能共振散射**（尺度 $\ll$ 任何加速粒子的回旋半径），但非线性演化可形成 flux tubes 结构（Reville & Bell 2012）。

[FACT] Zirakashvili 等（2008）数值：小尺度模下最大能量 $\sim 10^5$ GeV，因为在高能端 D(p) $\propto p^2$（小偏角制）。

[CRITIQUE] Bell 模虽然增长快，但尺度太小无法有效散射被加速粒子——需要**非线性**机制（§4.2.3）将其重组为可散射的大尺度结构。

### 4.2.3 Filamentation instability

> **filamentation 不稳定性**

[FACT] CR 逃逸电流导致 **filament 形成**：J$\times$B 力排斥等离子体，形成更大截面的磁通管。该机制可在 $p_{\max}$ 尺度产生放大磁场，是自洽的"self-confinement"机制。

[FACT] Reville & Bell（2012）、Caprioli & Spitkovsky（2013）的数值工作表明此机制**可能**是自洽的。

[FACT] Bell 等（2013）估算：在 $V_{\rm sh} \sim 5000$ km/s（Tycho 类 SNR），filamentation 允许达到 $\sim 200$ TeV。

[FACT] **距膝点差一个量级**——但作者指出"SNRs with even larger velocity (therefore much younger) may be responsible for acceleration of PeV CRs"，即需要更年轻、更快的 SNR。

[CRITIQUE] 200 TeV 的估计距膝点（$\sim$ PeV）仍差一个量级；作者承认需要"超年轻 SNR"但**未证明**这些 SNR 的能量学足以支撑总通量。§4.2.3 与 §4.2.2 的关系被简化为"可能的非线性发展"，实际数值模拟表明二者耦合远更复杂。

[INTERPRETATION] 作者对 filamentation 持**温和乐观**态度："promising results ... from numerical investigations of the filamentation instability ... might represent a breakthrough."——这是全文四机制中最被寄予希望的一个。

### 4.2.4 Non-resonant large-scale streaming instability

> **非共振大尺度 streaming 不稳定性**

[FACT] **大尺度非共振 firehose 模**（原文 Eq. 93）增长率：

$$
\Gamma_{\rm FH}(k) \approx \xi_{\rm CR}^{1/2}\, \frac{V_{\rm sh}^2\, k}{c}
$$

[FACT] 对于 $k \ll 1/r_{L,\max}$：

$$
\Gamma_{\rm FH}\cdot \tau_{\rm adv}(p_{\max}) \ll \xi_{\rm CR}^{1/2} < 1
$$

**时间不够**——大尺度 firehose 不稳定性无法在粒子最大能量对应的时间标度内有效生长。

[FACT] 因此 §4.2.4 对"能否靠大尺度模支撑 PeV 加速"给出**否定性**结论：增长率在大尺度上太慢。

[CRITIQUE] §4.2.4 表明大尺度非共振模在物理上受**时间瓶颈**限制，无法与 §4.2.3 的 filamentation 形成互补——放大磁场的产生仍必须依赖 §4.2.2 的小尺度非共振模 + 非线性重组。

[INTERPRETATION] §4.2 的四个子节合起来给出**磁化放大机制谱系**的完整诊断：共振模（§4.2.1）在 $\xi_{\rm CR} \sim 10\%$ 下失效；Bell 非共振小尺度模（§4.2.2）增长快但尺度太小；filamentation（§4.2.3）最有希望但需验证；firehose（§4.2.4）时间不够。核心问题归结为作者自问："Is this the same magnetic field that is responsible for particle acceleration up to the knee?"

[CRITIQUE] 混合 PIC / hybrid 模拟（Gargaté & Spitkovsky 2012；Caprioli & Spitkovsky 2013）正在填补这一空白，但作者没有给出"最可能"的方案——这是综述的诚实，也意味着问题**仍未解决**。

---

## 4.3 The dynamical reaction of amplified magnetic fields on the shock

[FACT] §4.3 完成 NLDSA 的**闭合回路**：放大磁场的压力 $P_w$ 反过来改变激波结构，进而软化谱凹性。

[FACT] 磁动量方程增加 $P_w$ 项（原文 Eq. 95）：

$$
\nabla(\rho u^2 + P_g + P_c + P_w) = 0
$$

[FACT] Alfvén 波通量（Eq. 98）：

$$
F_w = \sum_i \frac{\delta B_i^2}{4\pi}(u + H\, c_i\, v_A) + P_w\, u
$$

其中 $H = \pm 1$ 为波螺旋度。

[FACT] **R$_{\rm tot}$–R$_{\rm sub}$ 关系**（Eq. 99）：

$$
R_{\rm tot}^{\gamma_g+1} = \frac{M_0^2\, R_{\rm sub}^{\gamma_g}}{2\,\bigl[\gamma_g+1 - R_{\rm sub}(\gamma_g-1)\bigr] / (1+\Lambda_{\rm B})}
$$

其中磁动力学反作用参量（Eq. 100）：

$$
\boxed{\Lambda_{\rm B} = W\!\left[1 + R_{\rm sub}\!\left(\frac{2}{\gamma_g} - 1\right)\right], \quad W = \frac{P_{w,1}}{P_{g,1}}}
$$

[FACT] $W \ll 1$ 时磁动力学反作用可忽略；$W \gtrsim 1$ 时**压缩比被减小**，谱更趋幂律化。

[FACT] 由 X 射线边缘反推 $B$，若归因于 CR 诱导，给出 $W \sim 1$–$10$ → 磁反作用**重要且显著**改善谱的凹性。

[INTERPRETATION] §4.3 的磁动力学反作用是**"软化"谱凹性的关键物理**——解释了为何实际观测的 $\gamma$ 射线谱比纯 NLDSA 预言更软。即使加上这一机制，仍需引入散射中心速度假设才能完全解释 Tycho。

[CRITIQUE] 作者没有处理 **turbulent heating / wave damping** 对 precursor 和谱凹性的影响——这是 Berezhko & Ellison (1999) 的经典结果，但本文仅在 §4.1 中一笔带过。

---

| 物理量 | 数值 |
|--------|------|
| 年轻 SNR X 射线窄边缘厚度 | $\sim 10^{-2}$ pc |
| 推断磁场强度 | $\sim 300$–$1000\;\mu$G（ISM 背景 $\sim 1$–$6\;\mu$G）|
| Bohm 极限 $E_{\max}$（典型） | $\sim 3\times 10^5$ GeV |
| Bell 非共振模峰值 $k^* r_{L,0}$ | $\sim 10^4$ |
| Bell 非共振模可及能量 | $\sim 10^5$ GeV（Zirakashvili 等）|
| Filamentation 可及能量 | $\sim 200$ TeV（Tycho 参数）|
| 放大场相对热压 $W = P_w/P_g$ | $\sim 1$–$10$ |
| $W \ll 1$ 磁反作用可忽略；$W \gtrsim 1$ 重要 | |
| 谱凹性转折动量 | $\sim$ few GeV/c |

## 图表分析

参见 `09_figures_tables.md`（Figure 7 激波示意图、Figure 8 粒子谱、Figure 9 色散关系）。

---

## 元数据

```yaml
chapter: 4
title: The non-linear theory of diffusive shock acceleration
pages: "Blasi 2013, §4"
subsections:
  - "4.1 Dynamical reaction of accelerated particles"
  - "4.2.1 Resonant streaming instability"
  - "4.2.2 Non-resonant small-scale modes from streaming instability"
  - "4.2.3 Filamentation instability"
  - "4.2.4 Non-resonant large-scale streaming instability"
  - "4.3 The dynamical reaction of amplified magnetic fields on the shock"
key_formulas:
  - "R_tot = u_0 / u_1 (Eq. 69)"
  - "xi_CR(z) ≈ 1 - u(z)/u_0 (Eq. 70, precursor)"
  - "E_gamma,max ≈ 1.7 V_sh,8^2 keV (Eq. 74, Bohm)"
  - "omega_I(k) = (pi/8) Omega*_p (V_sh/v_A) (n_CR/n_i) (Eq. 87)"
  - "xi_CR << 8e-4 (V_sh/5e8)^-3 (Eq. 86/88, 共振适用条件)"
  - "omega_I ≈ omega_R = [(pi/8) Omega*_p k V_sh n_CR/n_i]^1/2 (Eq. 89)"
  - "k* r_L,0 = 3 xi_CR gamma_min/Lambda · (V_sh/v_A)^2 · (V_sh/c) (Eq. 92)"
  - "Gamma_FH(k) ≈ xi_CR^1/2 · V_sh^2 k/c (Eq. 93)"
  - "Lambda_B = W[1 + R_sub(2/gamma_g - 1)] (Eq. 100)"
keywords:
  - NLDSA
  - precursor
  - subshock
  - spectral concavity
  - streaming instability
  - Bell instability
  - filamentation instability
  - firehose instability
  - magnetic field amplification
  - magnetic reaction
references_internal:
  prev_chapter: 03_test_particle_dsa
  next_chapter: 05_superbubble
```

**引用出处**：Blasi, "The Origin of Galactic Cosmic Rays," *arXiv:1311.7346* (2013), §4 全部公式编号（Eq. 53–100）沿用原文。