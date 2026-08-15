# 6. Indirect evidence for CR acceleration in SNRs

> 本章属于：The Origin of Galactic Cosmic Rays（Blasi, 2013, arXiv:1311.7346）
>
> 上一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/05_superbubble.md|05_superbubble.md]]
>
> 下一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/07_h_alpha.md|07_h_alpha.md]]

## 6.1 本节核心内容

- 综合多波段观测证据（射电、X 射线、γ 射线）对 SNR CR 加速的检验。
- 关键议题：(1) CR 逃逸机制与逃逸谱形状；(2) SNR 加速谱的凹性与 γ 射线谱、各向异性的冲突；(3) 孤立 SNR（RX J1713.7–3946, Tycho）的多波段分析；(4) 邻近分子云的 SNR（π⁰ 鼓包）。

## 6.2 原文内容

### §6 引言

- [FACT] SNR 是 CR 加速位点的**直接证据**来自辐射观测。"The subject of the debate is whether all CRs are accelerated in SNRs, and which SNRs or which phases of a SNR may possibly allow for CR acceleration up to the energy of the knee."
- [FACT] 射电同步辐射：ν ≃ 3.7 MHz · B_µ · E(GeV)²。
- [FACT] 若 B 放大到 ~100 µG，GHz 射电对应 E~1–2 GeV；未放大则 ~10–20 GeV。
- [FACT] X 射线 1 keV 同步辐射对应 E~20–30 TeV（100 µG 场下）。
- [FACT] NLDSA 预言 K_ep ~ $10^{-3}$–$10^{-4}$；在地球测量值 K_ep ~ $10^{-2}$，存在 1–2 个量级的差异。
- [FACT] "The value of K_ep as inferred from multiwavelength studies in the sources reflects the instantaneous ratio ... while the value of K_ep as measured at Earth is the result of the integration over time of the escape flux."

### §6.1 Escape

- [FACT] 三种逃逸机制：(1) 激波减速使粒子不易返回；(2) 激波破裂；(3) 自散射中心随 CR 密度下降而失效。
- [FACT] Drury (2011) 综述了该问题。
- [FACT] 标准逃逸模型：在 $z_{0}$ 处 f(p, $z_{0}$)=0 的边界条件（Eq. 101, 102）。
- [FACT] 边界处逃逸通量（Eq. 102）：
$$F(z_0, p) = -D(p)\frac{\partial f}{\partial z}\bigg|_{z=z_0} = -\frac{u_1 f_0(p)}{1 - \exp(u_1 z_0/D(p))}\exp\left(\frac{u_1 z_0}{D(p)}\right)$$
- [FACT] 逃逸谱形状：在动量 p*（满足 D(p*)/$u_{1}$ ≃ $z_{0}$）处峰值 → 每个时刻的逃逸谱集中在 p* 附近。
- [FACT] Sedov 阶段时间积分（Eq. 103, 104）：**在 ξ_esc 与时间无关的假设下，逃逸谱 ∝ p⁻⁴**——与 DSA 的瞬时谱斜率无关，只依赖"逃逸发生在自相似阶段"这一前提。
- [FACT] 若 ξ_esc 随时间下降，逃逸谱硬于 p⁻⁴。

### §6.2 Spectra

- [FACT] NLDSA 计算的逃逸谱（Caprioli et al. 2010，Fig. 10）在最高能段呈**"bump-like"** 结构，由硬逃逸通量主导。
- [FACT] 问题 (1)：硬于多数 SNR 的 γ 射线观测（Caprioli 2011）。
- [FACT] 问题 (2)：若在地球处匹配观测谱，需 D(E) ∝ E^0.7，而此能量依赖导致 **CR 各向异性远超观测**（Ptuskin 2006；Blasi & Amato 2012b）。
- [FACT] 问题**并非 NLDSA 独有**：test-particle 理论同样有该问题。
- [FACT] 可能的软化机制：
  - 快速移动的散射中心（Bell 1978a；Ptuskin et al. 2010；Caprioli 2012）：谱指数
    $$\alpha = \frac{\tilde r + 2}{\tilde r - 1}, \quad \tilde r = \frac{u_1 \pm v_{W,1}}{u_2 \pm v_{W,2}} \quad (105)$$
    取决于波的螺旋度 → 可能软化或硬化。
  - 垂直激波几何（Schure & Bell 2013）：下游返回概率降低 → 更陡谱。
- [FACT] "Both these effects rely on details of the theory ... observations may actually allow us to find the correct explanation."

### §6.3 Gamma-ray emission from isolated SNRs

**RX J1713.7–3946**（核心坍缩型）：
- [FACT] 首个明确探测到 TeV γ 射线的 SNR（Aharonian et al. 2004, 2006, 2007），后被 Fermi-LAT 在 GeV 段探测到（Abdo et al. 2011）。
- [FACT] 若为强子源：需要 ~160 µG 解释 X 射线边缘和 γ 谱；若电子与质子同温，将预测强热 X 射线——未探测到。
- [FACT] Ellison et al. (2010)：即使慢速 Coulomb 散射也可使电子升温至 >1 keV，激发氧线；未探测到 → 气体密度上限过严 → π 产生不足 → Ellison 等结论为**轻子起源**。
- [FACT] Fermi-LAT 硬 γ 谱同样**与 π 衰变不兼容**。
- [FACT] 但 ICS 解释也有问题：Morlino et al. (2009) —— 需要 IR 辐射场密度高 25 倍；需要 ~10 µG 弱场，与 X 射线边缘不兼容。
- [FACT] Fukui et al. (2012)：气体分布与 TeV 发射空间关联 → 支持强子起源。
- [FACT] 作者结论：RX J1713.7–3946 是"环境复杂性主导"的典型案例，需 CTA 进一步澄清。

**Tycho SNR**（Ia 型，1572 年，~3 kpc）：
- [FACT] 圆对称形态（均匀 ISM）；全 X 射线窄边缘。
- [FACT] Fermi-LAT（Giordano et al. 2012，GeV）和 VERITAS（Acciari et al. 2011，TeV）γ 谱只与**强子起源**兼容（Morlino & Caprioli 2012）。
- [FACT] X 射线边缘要求 B ~ 300 µG → 加速质子最大能量 ~500 TeV。
- [FACT] Berezhko et al. (2013)：γ 谱的陡化归因于**环境效应**（两个组分：均匀介质 + 密集团块，后者 p_max 更低）。
- [FACT] Morlino & Caprioli (2012)：陡化归因于 **NLDSA + 波以 Alfven 速度运动**（放大场中的 Alfven 速度）——即 §6.2 中 v_W ≠ 0 机制的具体实现。
- [FACT] 两种解释的本质差异：前者需要**ad hoc 密度涨落**（不可移植到其他 SNR），后者**与 X 射线边缘磁化强度自洽耦合**。
- [FACT] 作者偏向 Morlino & Caprioli 的方案（"the shape of the spectrum is related ... to the strength of the amplified magnetic field"）。

### §6.4 SNRs near molecular clouds

- [FACT] AGILE（Giuliani et al. 2011, 2010）与 Fermi-LAT（Ackermann et al. 2013）**首次明确探测到 π 鼓包**（pion bump），证实 pp→π⁰→2γ。
- [FACT] 典型对象：IC 443、W44（Fig. 12）。
- [FACT] 分子云内密度 n=$10^{3}$ cm⁻³、几何截面 σ~$10^{-14}$ cm² → λ~$10^{11}$ cm —— **SNR 激波撞击分子云时可能从碰撞less 变为碰撞型**。
- [FACT] 分子云加热证据来自**脉泽发射**（Hewitt et al. 2009）。
- [FACT] 逃逸 CR 到达分子云的**低能截止**条件：[D(E)·τ_SNR]^½ ≃ R_MC。
- [FACT] π 产生截面 ~ 1/E_π → 低能 γ 谱 ~ E_γ⁻¹ 是低能截止的特征。
- [FACT] W28（Giuliani et al. 2010）：**两个不同距离的云**表现出不同 CR 通量，较远的云低能截止出现在更高能量——**符合传播时延图像**。
- [FACT] CR 源附近 <几十 pc 范围内，源 CR 主导银河系 CR 通量（Blasi & Amato 2012a）→ 该范围内的 D(E) 由自散射主导，可能**不同于银河系平均值**。
- [FACT] 主导 B 场方向时，CR 扩散各向异性 → 在 L_c ~ 50–100 pc（相干尺度）以内沿 B 方向拉长。
- [FACT] 若 MC 位于 SNR 的磁通管上，可被 CR 照亮；否则几乎无 γ 发射（Nava & Gabici 2013；Giacinti et al. 2013）。
- [FACT] Malkov et al. (2013) 给出源附近 CR 传播的自洽解（含平行/垂直扩散）。

## 6.3 关键公式

| 编号 | 公式 | 含义 |
|------|------|------|
| 101 | f(z,p) 边界解 | 逃逸边界条件 f($z_{0}$,p)=0 下的分布函数 |
| 102 | F($z_{0}$,p) | 逃逸通量（动量依赖的峰）|
| 103 | dε = 4πp²dp·pc·N_esc(p) = ξ_esc · ½ρV³_sh · 4πR²_sh dt | 逃逸能量守恒 |
| 104 | N_esc(p) ∝ p⁻⁴ ξ_esc(t) | Sedov 阶段积分后逃逸谱 |
| 105 | α = (r̃+2)/(r̃−1)，r̃ = ($u_{1}$ ± v_W,1)/($u_{2}$ ± v_W,2) | 含移动散射中心的谱指数 |

## 6.4 关键数值

| 物理量 | 数值 |
|--------|------|
| ν_sync (GeV e⁻) | 3.7 MHz · B_µ · E²(GeV) |
| X 射线边缘厚度 | ~$10^{-2}$ pc |
| Tycho 推断 B | ~300 µG |
| Tycho 加速 p_max | ~500 TeV |
| RX J1713 强子模型要求 B | ~160 µG |
| RX J1713 ICS 模型要求 B | ~10 µG |
| RX J1713 ICS 所需 IR 密度 | 预期值 25 倍 |
| K_ep（NLDSA 预言） | ~$10^{-3}$–$10^{-4}$ |
| K_ep（地球观测） | ~$10^{-2}$ |
| 磁相干尺度 L_c | 50–100 pc |
| 分子云密度 n | $10^{3}$ cm⁻³ |
| 分子云碰撞长度 λ | $10^{11}$ cm |
| W28 两云相对 CR 通量差异 | 与距离成反相关 |

## 6.5 图表分析

参见 `09_figures_tables.md`（Figure 10 逃逸谱、Figure 11 Tycho 多波段、Figure 12 IC 443/W44 π 鼓包）。

## 6.6 作者的逻辑

- 从**抽象的逃逸机制**（§6.1）→ 到**逃逸谱的积分形状**（§6.2）→ 到**具体 SNR 的多波段检验**（§6.3，两个案例）→ 到**源-MC 复合系统的传播**（§6.4）。
- [INTERPRETATION] 每个小节都在**测试 SNR 范式的一条腿**：§6.1 测试"谱的形状"，§6.2 测试"谱的硬软"，§6.3 测试"加速源-辐射源的耦合"，§6.4 测试"π 产生通道的确凿性"。
- [INTERPRETATION] 作者刻意避免"最终结论"，而是给出"每个观测都对 SNR 范式施加不同方向的约束"——这正是 §8 结论中"circumstantial evidence"的实证基础。

## 6.7 我的理解

- [CRITIQUE] §6.1 的 N_esc(p) ∝ p⁻⁴ 结果值得**强调**：它**与注入谱斜率无关**，只要求"自相似阶段逃逸"。这为理解"地球处观测谱为何是 E⁻²·⁷（比 p⁻⁴ 软 0.7 个指数）"提供自然路径——只要 ξ_esc 随时间下降即可。
- [CRITIQUE] §6.2 关于 D(E) ∝ E^0.7 与各向异性冲突的论证在 Blasi 的**多篇后续论文**中被深化（Blasi & Amato 2012b），本文仅给出定性说明。
- [INTERPRETATION] §6.3 中 Tycho vs RX J1713 的对比是本文的**"双案例教学"**：Tycho 支持强子（有 π 鼓包证据）+ 高 B + 有限 p_max；RX J1713 则暴露"谱 vs 环境"的复杂性。
- [CRITIQUE] 对 Tycho 的解释（Morlino & Caprioli vs Berezhko 等）作者**明确偏向**前者，但仍承认"one is left to wander"。这是综述中的**少数明确立场**之一，值得记住。

## 6.8 潜在问题与值得关注的地方

- **潜在不一致性**：K_ep ~ $10^{-3}$–$10^{-4}$（NLDSA）vs ~$10^{-2}$（地球）——作者在 2 处强调但未给出解决路径。
- **信息缺失**：CTA 展望仅在 §8 提到；2013 年之后 CTA 数据已部分到位（如 Tycho、IC 443 的 CTA 观测），本文未涉及。
- [CRITIQUE] §6.4 对 W28 低能截止的解释高度依赖"纯扩散 + 点源"图像；如果 CR 逃逸具有**定向性**（沿 B 场），则解释需修订。