# 4. The non-linear theory of diffusive shock acceleration

> 本章属于：The Origin of Galactic Cosmic Rays（Blasi, 2013, arXiv:1311.7346）
>
> 上一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/03_test_particle_dsa.md|03_test_particle_dsa.md]]
>
> 下一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/05_superbubble.md|05_superbubble.md]]

## 4.1 本节核心内容

- 建立"为什么要 NLDSA"的三条主线：加速粒子对激波的动量反馈、CR 诱导的不稳定性（磁化放大）、放大磁场对激波的反向作用。
- 用稳态守恒方程推导**precursor + subshock** 结构，得到 R_sub < 4 < R_tot。
- 谱的凹性（concave）：低能段更陡（接近 R_sub），高能段更硬（接近 R_tot），转折在 ~GeV/c。
- 磁场放大四种机制的系统对比：共振 streaming 不稳定性、Bell 非共振小尺度模、filamentation 不稳定性、大尺度 firehose 不稳定性。
- 放大磁场的动力学反作用（$\Lambda_{\rm B}$, W）使谱更趋幂律。

## 4.2 原文内容（要点摘录）

### §4 引言：三条需要 NLDSA 的理由

- [FACT] 加速粒子对激波的动量反馈：$\xi_{\rm CR}$ ~ 10% → CR 压力改变压缩比 r，谱变为刚度依赖。
- [FACT] CR 诱导等离子体不稳定性：磁化放大既是 X 射线窄边缘的原因，也是缩短加速时间的必要条件。
- [FACT] 放大磁场动力学反作用：~100–1000 µG 的磁场压力虽仅为 $\rho$v$^{2}$_s 的 $10^{-2}$–$10^{-3}$，但可远大于上游热压，进而影响 r。

### §4.1 Dynamical reaction of accelerated particles

- [FACT] 两种效应：(1) CR 压力在上游造成 **precursor**（流体减速）；(2) 最高能粒子逃逸使激波 **radiative-like**，R_tot > 7 潜在可能。
- [FACT] 守恒方程（Eq. 53–60）：质量 $\rho$u = const；动量 $\rho$u$^{2}$ + P_g + P_c = const；能量 $\rho$$\epsilon$ + P_g + E_c = const（含 CR 能量通量）。
- [FACT] CR 能量方程（Eq. 64）：∂E_c/∂t + ∇·($\gamma_{\rm c}$/($\gamma_{\rm c}$−1)·uP_c) = ∇·(D̄∇E_c) + u∇P_c，其中 D̄ 是能量加权平均扩散系数。
- [FACT] 准稳态下子激波压缩比 R_sub 用 $M_{1}$ 表达（Eq. 68）；总压缩比 R_tot = $u_{0}$/$u_{1}$（Eq. 69）用 R_sub、R_0 表达。
- [FACT] CR 诱导 precursor 的深度：$\xi_{\rm CR}$(z) ≈ P_c(z)/($\rho_{0}$$u_{0}^{2}$) ≈ 1 − u(z)/$u_{0}$（Eq. 70）。
- [FACT] **谱的凹性**（concavity）："particles with low momentum experience a compression factor closer to R_sub < 4, while higher momentum particles trace a compression factor closer to R_tot > 4."
- [FACT] 三种计算 NLDSA 的方法：有限差分（Berezhko & Völk；Zirakashvili & Ptuskin）；Monte Carlo（Ellison & Eichler；Knerr；Vladimirov）；半解析（Malkov；Blasi 2002；Amato & Blasi）。

### §4.2 Magnetic field amplification

- [FACT] X 射线窄边缘观测：电子同步辐射给出 E_e ≈ 8(E_$\gamma$/100 eV)^½ · B$^{-1}$/$^{2}$_100 TeV。
- [FACT] Bohm 极限下加速时间（Eq. 71）：$\tau_{\rm acc}$ ≈ $3.3\times10^{7}$ E_TeV · B$^{-1}$_100 · V$^{-2}$_sh,8 s。
- [FACT] 同步辐射损失时间（Eq. 72）：$\tau_{\rm syn}$ = $4\times10^{10}$ B$^{-2}$_100 · E$^{-1}$_TeV s。
- [FACT] 最大电子能量（Eq. 73）：E_e,max ≈ 34 B$^{-1}$/$^{2}$_100 · V_sh,8 TeV。
- [FACT] 最大光子能量（Eq. 74）：E_$\gamma$,max ≈ 1.7 V$^{2}$_sh,8 keV —— **与 B 无关**（Bohm 假设下）。
- [FACT] 特征宽度（Eq. 75）：√(D·$\tau_{\rm syn}$) ≈ $3.7\times10^{-2}$ B$^{-3}$/$^{2}$_100 pc → 观测到的 ~$10^{-2}$ pc 窄边缘需要 B~几百 µG。
- [FACT] 磁化放大两种起源：(i) 激波波纹（shock corrugation，Giacalone & Jokipii 2007，Sano 2012）——下游；(ii) CR streaming 不稳定性——**上游**（"qualitatively, extremely important difference"）。
- [FACT] 若 D(E) 取 ISM 值（$3\times10^{28}$ (E/10 GeV)^$\delta$ cm$^{2}$/s），$\tau_{\rm acc}$ 远超自由膨胀期（Eq. 76）。
- [FACT] Bohm 假设、B=100 µG、T_s=300 yr：E_max ≈ $3\times10^{5}$ GeV · B_100 · (T_s/300 yr) · (V_sh/1000 km/s)$^{2}$（Eq. 78）。"All parameters have to be chosen in the most optimistic way so as to maximize E_max."
- [FACT] 共振 streaming 不稳定性增长速率（Zweibel 1979；Achterberg 1983，Eq. 79/87）：
  $\omega_{\rm I}$(k) = ($\pi$/8)·$\Omega$*_p·(V_sh/v_A)·[n_CR(p>pres(k))/n_i]
- [FACT] 共振不稳定性适用条件（Eq. 86, 88）：n_CR/n_i ≪ v_A$^{2}$/(V_sh c)，即 $\xi_{\rm CR}$ ≪ $8\times10^{-4}$ · (V_sh/$5\times10^{8}$ cm/s)$^{-3}$ —— **对 $\xi_{\rm CR}$ ~ 10% 完全不成立**。
- [FACT] **CR modified regime**（$\xi_{\rm CR}$ 大，Eq. 89）：$\omega_{\rm I}$ ≈ $\omega_{\rm R}$ = [ ($\pi$/8)$\Omega$*_p k V_sh n_CR(p>pres)/n_i ]^½，相位速度 v_$\phi$ ≫ v_A。
- [FACT] 此条件下 $F_{0}$ ≤ 1（Eq. 90）：$F_{0}$(k) = ($\pi$/6)^½ ($\xi_{\rm CR}$/$\Lambda$)^½ (c/V_sh)^½，即"efficient CR acceleration ... reduces the growth of the waves and limits the value of the self-generated magnetic field to the same order of magnitude as the pre-existing magnetic field."
- [FACT] **Bell 非共振小尺度模**（Bell 2004, 2005）：$\xi_{\rm CR}$ 大时，右手极化模在 k r_L,0 > 1 出现非共振分支，增长率 ∝ k^½，峰值在 k* r_L,0 = 3 $\xi_{\rm CR}$ $\gamma_{\rm min}$ / $\Lambda$ · (V_sh/v_A)$^{2}$ · (V_sh/c) > 1（Eq. 92），比共振模快 (k* r_L,0)^½ 倍。
- [FACT] Bell 模**不能共振散射**（尺度 << 任何加速粒子的 r_L），但非线性演化可形成 flux tubes 结构（Reville & Bell 2012）。
- [FACT] Zirakashvili 等 (2008) 数值：小尺度模下最大能量 ~$10^{5}$ GeV，因为在高能端 D(p) ∝ p$^{2}$（小偏角制）。
- [FACT] **Filamentation 不稳定性**（§4.2.3）：CR 逃逸电流导致 filament 形成，J×B 力排斥等离子体，形成更大截面的磁通管。Reville & Bell (2012)、Caprioli & Spitkovsky (2013) 表明这可能在 p_max 尺度产生放大磁场，是自洽的"self-confinement"机制。
- [FACT] Bell et al. (2013) 估算：在 V_sh ~ 5000 km/s（Tycho 类 SNR），此机制允许达到 ~200 TeV —— **距膝点差一个量级**。
- [FACT] **大尺度非共振 firehose 模**（§4.2.4）：$\Gamma_{\rm FH}$(k) ≈ $\xi_{\rm CR}^{\rm ½}$ · V_sh$^{2}$ k / c（Eq. 93）；对于 k ≪ 1/r_L,max，$\Gamma_{\rm FH}$·$\tau_{\rm adv}$(p_max) ≪ $\xi_{\rm CR}^{\rm ½}$ < 1，时间不够。

### §4.3 放大磁场的动力学反作用

- [FACT] 磁动量方程增加 P_w 项（Eq. 95）：$\rho$u$^{2}$ + P_g + P_c + P_w = const。
- [FACT] Alfvén 波通量（Eq. 98）：F_w = $\Sigma$ ($\delta$B$^{2}$_i)/(4$\pi$) · (u + H c_i v_A) + P_w u，H = ±1 为波螺旋度。
- [FACT] R_tot–R_sub 关系（Eq. 99）：R_tot^($\gamma_{\rm g}$+1) = $M_{0}^{2}$ R_sub^$\gamma_{\rm g}$ / [2 · ($\gamma_{\rm g}$+1 − R_sub($\gamma_{\rm g}$−1))/(1+$\Lambda_{\rm B}$)]，$\Lambda_{\rm B}$ = W [1 + R_sub(2/$\gamma_{\rm g}$ − 1)]，W = P_w,1/P_g,1。
- [FACT] W ≪ 1 时磁动力学反作用可忽略；W ≳ 1 时**压缩比被减小**，谱更幂律化。
- [FACT] X 射线边缘反推 B 给出 W ~ 1–10（若该场归因于 CR 诱导）→ 磁反作用重要且已显著改善谱的凹性。

### §4.4 磁化放大机制的批判总结

- [FACT] "Is this the same magnetic field that is responsible for particle acceleration up to the knee?"——**核心问题**。
- [FACT] 共振不稳定性增长过慢（$\delta$B~B）；Bell 非共振模增长快但尺度太小；下游放大不影响上游散射；filamentation 有希望但尚需验证。
- [FACT] 混合 PIC / hybrid 模拟正在填补这一空白（Gargaté & Spitkovsky 2012；Caprioli & Spitkovsky 2013）。

## 4.3 关键公式汇总

| 编号 | 公式 | 含义 |
|------|------|------|
| 53 | ∂$\rho$/∂t + ∇($\rho$u) = 0 | 质量守恒 |
| 55 | ∇($\rho$u$^{2}$+P_g+P_c) = 0 | 含 CR 的动量守恒 |
| 60 | ∇(½$\rho$u$^{3}$ + $\gamma_{\rm g}$/($\gamma_{\rm g}$−1)·uP_g) = −u∇P_c | 含 CR 能量守恒 |
| 62, 63 | E_c, P_c 的定义 | CR 能量/压力 |
| 66 | CR 能量输运方程 | 含扩散项、做功项 |
| 68 | R_sub($M_{1}$) | 子激波压缩比 |
| 69 | R_tot(R_sub, $M_{0}$) | 总压缩比 |
| 70 | $\xi_{\rm CR}$(z) ≈ 1 − u(z)/$u_{0}$ | precursor 深度 |
| 71 | $\tau_{\rm acc}$ (Bohm) | 加速时间（磁化放大情形） |
| 73 | E_e,max ≈ 34 B$^{-1}$/$^{2}$_100 V_sh,8 TeV | 最大电子能量 |
| 74 | E_$\gamma$,max ≈ 1.7 V$^{2}$_sh,8 keV | 最大同步辐射光子能量 |
| 78 | E_max ≈ $3\times10^{5}$ GeV·B_100·(T_s/300 yr)·(V_sh/1000)$^{2}$ | SNR 最大能量上限估计 |
| 81 | $F_{0}$(k) = ($\pi$/4)·$\xi_{\rm CR}$·(V_sh/v_A)·(1/$\Lambda$) | 共振 streaming 功率谱 |
| 86, 88 | $\xi_{\rm CR}$ ≪ $8\times10^{-4}$(V_sh/$5\times10^{8}$)$^{-3}$ | 共振不稳定性适用条件 |
| 87 | $\omega_{\rm I}$(k) = ($\pi$/8)$\Omega$*_p(V_sh/v_A)(n_CR/n_i) | 低 $\xi_{\rm CR}$ 共振增长率 |
| 89 | $\omega_{\rm I}$ ≈ $\omega_{\rm R}$ = [($\pi$/8)$\Omega$*_p k V_sh n_CR/n_i]^½ | 高 $\xi_{\rm CR}$ 增长率 |
| 90 | $F_{0}$(k) = ($\pi$/6)^½ ($\xi_{\rm CR}$/$\Lambda$)^½ (c/V_sh)^½ | 高 $\xi_{\rm CR}$ 情况下的 $F_{0}$ |
| 92 | k* r_L,0 = 3 $\xi_{\rm CR}$ $\gamma_{\rm min}$/$\Lambda$ · (V_sh/v_A)$^{2}$ · (V_sh/c) | Bell 非共振模峰值尺度 |
| 93 | $\Gamma_{\rm FH}$(k) ≈ $\xi_{\rm CR}^{\rm ½}$ · V_sh$^{2}$ k/c | 大尺度 firehose 增长率 |
| 95 | ∇($\rho$u$^{2}$ + P_g + P_c + P_w) = 0 | 含波动的动量守恒 |
| 99 | R_tot^($\gamma$+1) 与 R_sub 关系 | 磁反作用下的压缩比 |
| 100 | $\Lambda_{\rm B}$ = W[1 + R_sub(2/$\gamma$ − 1)] | 磁动力学反作用参量 |

## 4.4 关键数值

| 物理量 | 数值 |
|--------|------|
| 年轻 SNR X 射线窄边缘厚度 | ~$10^{-2}$ pc |
| 推断磁场强度 | ~300–1000 µG（ISM 背景 ~1–6 µG）|
| Bohm 极限 E_max（典型） | $~3\times10^{5}$ GeV |
| Bell 非共振模峰值 k* r_L,0 | ~$10^{4}$ |
| Bell 非共振模可及能量 | ~$10^{5}$ GeV（Zirakashvili 等）|
| Filamentation 可及能量 | ~200 TeV（Tycho 参数）|
| 放大场相对热压 W = P_w/P_g | ~1–10 |
| W ≪ 1 磁反作用可忽略；W ≳ 1 重要 |
| 谱凹性转折动量 | ~few GeV/c |

## 4.5 图表分析

参见 `09_figures_tables.md`（Figure 7 激波示意图、Figure 8 粒子谱、Figure 9 色散关系）。

## 4.6 作者的逻辑

- 三条**"必须 NLDSA"**的理由构成一个自洽链条：10% 效率必然产生动力学反作用 → 上游散射要求自洽的磁化放大 → 磁化放大反过来减小压缩比 → 谱凹性变弱。
- §4.2 的四个小节（4.2.1–4.2.4）是按"由经典到前沿"排列的**磁化放大机制谱系**。
- [INTERPRETATION] 作者对 Bell 非共振模持**温和乐观**态度："promising results ... from numerical investigations of the filamentation instability ... might represent a breakthrough."

## 4.7 我的理解

- [CRITIQUE] 作者对共振不稳定性在 $\xi_{\rm CR}$ ~ 10% 时失效的论证（§4.2.1）是**决定性**的：如果这一论证正确，那么传统 "$\delta$B/B ~ 1 饱和" 的教科书结论在 SNR 强加速情形下不适用。
- [CRITIQUE] 但是 §4.2.3 filamentation 的估计（~200 TeV for Tycho）距膝点仍差一个量级——作者坦承"SNRs with even larger velocity (therefore much younger) may be responsible for acceleration of PeV CRs"，但没有证明这些"超年轻 SNR"的能量学足以支撑总通量。
- [INTERPRETATION] §4.3 的磁动力学反作用是**"软化"谱凹性的关键物理**——它解释了为何实际观测到的 $\gamma$ 射线谱比纯 NLDSA 预言更软（但作者也指出，即使加上这一机制，仍需引入散射中心速度假设才能完全解释 Tycho）。
- [CRITIQUE] 作者没有处理 **turbulent heating / wave damping** 对 precursor 和谱凹性的影响——这是 Berezhko & Ellison (1999) 的经典结果，但本文仅在 §4.1 中一笔带过。

## 4.8 潜在问题与值得关注的地方

- **潜在不一致性**：Eq. 74（E_$\gamma$,max 与 B 无关）只在 Bohm 假设下成立，作者明确指出"not a general result"——但后文多次使用 Bohm 假设进行能量估计。
- **信息缺失**：磁化放大的**时间演化**（随 SNR 演化）未讨论；不同 SNR 演化阶段（自由膨胀期 vs Sedov 期 vs 压强驱动期）对应的磁化状态可能不同。
- [CRITIQUE] §4.4 结尾的批判总结写得相当克制——作者承认所有机制都不完美，但没有给出"最可能"的方案。这是综述的诚实，但留给读者的是"问题仍在"的印象。
- [CRITIQUE] Bell 2004 非共振模的右手极化/电子主导物理虽然正确，但 §4.2.3 中 filamentation 与它之间的关系被简化为"可能的非线性发展"——实际数值模拟表明二者的耦合远更复杂。