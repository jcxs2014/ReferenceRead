# 7. $\gamma$ 射线观测与 SNR（Isolated SNRs & SNR-MC 复合体）

> 本章属于：[[02_cosmic-ray-origins/0005_amato-2014/literature_analysis/00_overview.md|The origin of galactic cosmic rays (Blasi 2013 §6.3-6.4 & Amato 2014 §4.6)]]
>
> 上一章：[[02_cosmic-ray-origins/0005_amato-2014/literature_analysis/06_escape_spectra.md|06_escape_spectra.md]]
>
> 下一章：[[02_cosmic-ray-origins/0005_amato-2014/literature_analysis/08_superbubble_ha.md|08_superbubble_ha.md]]

## 7.1 观测史与关键实验

**[FACT]** 主要 $\gamma$ 射线实验：
- **HESS**（地面 Cherenkov，TeV）：RXJ1713.7-3946 首个 SNR TeV 探测（Aharonian 2004, 2006, 2007）
- **Fermi-LAT**（空间，GeV）：RXJ1713.7-3946（Abdo 2011），W44（Abdo 2010a），IC443（Abdo 2010c），W28（Abdo 2010a），W51C（Abdo 2009），Tycho（Giordano 2012）
- **AGILE**：W44（Giuliani 2010, 2011）
- **VERITAS**（地面 Cherenkov，TeV）：Tycho（Acciari 2011）
- **Multi-messenger 突破**：Ackermann et al. 2013（Science 339:807）首次确认 **$\pi^{0}$ 鼓包**（pi bump）在 IC443 和 W44

## 7.2 RXJ1713.7-3946 的"反复横跳"

**[FACT]** 该 SNR（核心塌缩型）的解读历经多次反转：

1. **2004–2009**：HESS 发现 TeV $\gamma$ 射线 + Chandra 亮窄 X 射线边缘（B ~ 160 $\mu$G） → 早期倾向**强子起源**（Morlino et al. 2009）；
2. **Ellison et al. 2010**：精细热 X 射线分析 → 若电子与质子同温则应有强热发射，未观测到 → 暗示电子温度低；但即使慢速库仑散射也会激发氧线，未观测到 → 气体密度上限很低 → $\pi^{0}$ 产率不足 → **转向轻子**；
3. **Fermi-LAT (Abdo 2011)**：MeV-GeV 谱**过硬**，无法用 $\pi^{0}$ 衰变解释 → 确认轻子起源更可能；
4. **Fukui et al. 2012**：$H_{2}$ 分布与 TeV $\gamma$ 射线空间相关 → 又暗示强子起源。

**[FACT]** 轻子起源（ICS）面临的困难：
- 所需 IR 光密度比预期高 ~25 倍（Morlino 2009）；
- 需要弱 B ~ 10 $\mu$G，与 X 射线边缘矛盾。

**[CRITIQUE]** RXJ1713.7-3946 是典型的"**环境复杂性**"案例：观测本身不足以唯一判定强子/轻子起源，未来需 CTA 高分辨率 $\gamma$ 射线观测。

## 7.3 Tycho SNR（Type Ia，~3 kpc）

**[FACT]** Tycho 是**最有利的强子候选**：
- 几何规则（近乎完美的圆）→ 均匀 ISM；
- 亮窄 X 射线边缘 → B ~ **300 $\mu$G**；
- Fermi-LAT（GeV，Giordano 2012）+ VERITAS（TeV，Acciari 2011）→ 多频模型 → **推断质子最大能量 ~500 TeV**（Morlino & Caprioli 2012）；
- Berezhko et al. 2013 也主张强子起源，但用**不均匀密度团块**解释陡谱。

**[FACT]** Blasi Fig.11（Morlino & Caprioli 2012）左：Tycho 空间积分 SED；右：X 射线 1 keV 边缘亮度轮廓（Cassam-Chenaï 2007），模型经 Chandra PSF 卷积拟合。

**[FACT]** 但：**$\gamma$ 射线谱陡峭**，需要**修正** NLDSA 谱（式 (104) 散射中心速度）才能解释。

**[INTERPRETATION]** Tycho 是"**最接近膝区**"的 SNR，但目前只能到 **500 TeV**——仍差一个量级。

## 7.4 SNR 与分子云（MC）— $\pi^{0}$ 鼓包的"smoking gun"

**[FACT]** **Ackermann et al. (2013, Science 339:807)** 首次直接探测到 IC443 和 W44 中的 $\pi^{0}$ 衰变特征鼓包（~70 MeV）。

**[FACT]** Blasi Fig.12：IC443（左）与 W44（右）的 $\gamma$ 射线谱，$\pi^{0}$ 鼓包明显。

**[FACT]** 其他 MC-SNR 复合体（Fermi-LAT 探测）：W28（G6.4-0.1）、W51C、IC443、W44。

**[FACT]** 关键特征（Blasi）：
- 这些是**中年龄 SNR**（~$10^{4}$ yr），加速已不活跃 → 谱陡峭；
- $\gamma$ 射线亮度来自**高靶密度**，而非高 CR 通量；
- $\gamma$ 射线谱陡峭 → 推断 CR 谱在所有能量 > few GeV 上都比 E$^{-2}$ 陡（$\gamma_{\rm e}$ ~ 2.5–3）。

**[FACT]** Blasi 区分两类 SNR-MC 复合体：
1. 激波**直接冲击 MC**（n ~ $10^{3}$ cm$^{-3}$，分子碰撞长度 $\lambda$ ~ $10^{11}$ cm，激波可能退化为**有碰撞**激波）；
2. SNR 与 MC 分离，CR **扩散**到 MC 后被照射。

**[FACT]** 情形 2 中的**低能截断**现象：CR 谱在 [D(E)·$\tau_{\rm SNR}$]^{1/2} ~ R_MC 处有低能截断 → 高能粒子先到达 MC。

**[FACT]** 该截断在 $\gamma$ 射线谱中表现为低能端近似 ∝ E_$\gamma$^{-1} 的谱（$\pi$ 产额截面 ∝ 1/E）。

**[FACT]** W28（Giuliani 2010）：**两个云**距 SNR 不同距离，观测到不同 CR 照射强度，且较远云的低能截断在**更高能量**——**与传播理论预测完美一致**。

## 7.5 CR 各向异性传播（Blasi §6.4 尾 & Malkov 2013）

**[FACT]** 在源附近（~几十 pc 内），CR 密度主导银河系背景 → 扩散性质**自产生**于源本身产生的湍流，可能与银河系整体扩散不同。

**[FACT]** **平行扩散主导**时，CR 分布沿背景磁场**伸长**（Nava & Gabici 2013; Giacinti 2013），尺度 ~50–100 pc（相干长度 L_c）。

**[FACT]** 若 MC 与 SNR **沿同一磁力管**相连，被照射；否则几乎无 $\gamma$ 射线——这为**未来观测**提供了明确的"开/关"判据。

**[INTERPRETATION]** 该图像比"各向同性扩散"更复杂，但对**高分辨率 $\gamma$ 射线 + 磁场取向**观测敏感。

## 7.6 Amato §4 的总评

**[FACT]** Amato 明确列出 SNR 的"成功"与"张力"：

**成功**（6 项）：
1. R > 4（Tycho、SN1006）✓
2. 下游温度低于 RH 预期（RCW86 H$\alpha$）✓
3. 凹谱（少数 SNR 射电）✓
4. 空间发射轮廓（SN1006 X 射线 → $\xi$ ~ 30%；Tycho → $\xi$ ~ 10%）✓
5. 放大磁场（X 射线窄边缘 ~0.01 pc → B ~ 100 $\mu$G）✓
6. $\gamma$ 射线强子示踪（W44、IC443 $\pi^{0}$ 鼓包）✓

**张力**（1 项，但严重）：
- **粒子谱**：所有测到的 SNR 推断谱都比 E$^{-2}$ **更陡**（Amato §4.7 直言"discrepancy is clearly very serious"）。

**[CRITIQUE]** Amato 在此处的"张力"列举本身是一种批判性评估，但其框架存在问题：6项"成功"大多来自间接推断（X射线→B场、γ射线→强子成分），缺乏直接CR proton加速的观测证据。更根本的问题是：若所有SNR的γ射线谱都比E$^{-2}$更陡，而NLDSA+MFA在某些条件下确实预测更陡谱，那这究竟是"成功"（符合修正理论）还是"失败"（NLDSA预测的谱斜率与特定SNR条件一一对应，而非普遍更陡）？Amato的叙述没有区分这两种解读——这是一个科学方法论层面的模糊地带。[CRITIQUE]

**[INTERPRETATION]** 值得注意的是：W44和IC443的π⁰鼓包"成功"实际上依赖于假设——若γ射线来自强子相互作用（p+p→π⁰→2γ），则需要知道目标气体密度分布（而气体密度本身存在巨大不确定性）。因此"强子示踪成功"的置信度取决于气体模型，而不是纯粹的观测结果。精确的强子/轻子成分区分仍是CR天体物理的核心未解问题——ctao和高分辨率VHE γ射线观测将是关键。[INTERPRETATION]