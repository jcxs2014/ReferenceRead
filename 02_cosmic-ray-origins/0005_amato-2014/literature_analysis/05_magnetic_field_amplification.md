# 5. 磁场放大（MFA）— 非线性 DSA 的核心

> 本章属于：The origin of galactic cosmic rays (Blasi 2013 §4.2-4.4 & Amato 2014 §3.1, §7)
>
> 上一章：[[02_cosmic-ray-origins/0005_amato-2014/literature_analysis/04_nl_dsa.md|04_nl_dsa.md]]
>
> 下一章：[[02_cosmic-ray-origins/0005_amato-2014/literature_analysis/06_escape_spectra.md|06_escape_spectra.md]]

## 5.1 观测证据

**[FACT]** **所有**年轻 SNR 都观测到亮窄 X 射线边缘（thin X-ray rims）→ 同步辐射。

**[FACT]** X 射线边缘厚度量级 **~$10^{-2}$ pc** → 要求局部 B ~ **100–1000 μG**（对比 ISM 的 1–6 μG）→ 放大因子 ~10–100。

**[FACT]** Blasi §4.2 给出关键量级：
- 100 eV X 光子同步辐射要求电子能量 E_e ≈ 8 (E_γ/100 eV)^{1/2} $B_{100}$^{-1/2} TeV；
- 同步损失时间（Blasi 式 (72)）：$\tau_{syn} = 4\times 10^{10} B_{100}^{-2} E_{TeV}^{-1}$ s；
- 同步加速时间（Blasi 式 (71)）：$\tau_{acc} \approx 3.3\times 10^7 E_{TeV} B_{100}^{-1} V_{sh,8}^{-2}$ s；
- 最大电子能量（Blasi 式 (73)）：$E_{e,max} \approx 34\, B_{100}^{-1/2}\, V_{sh,8}$ TeV；
- 最大同步光子能量（Blasi 式 (74)）：$E_{\gamma,max} \approx 1.7\, V_{sh,8}^2$ keV（与 B 无关——Bohm 扩散下）；
- 边缘厚度（Blasi 式 (75)）：$\sqrt{D\tau_{syn}} \approx 3.7\times 10^{-2} B_{100}^{-3/2}$ pc。

**[FACT]** Amato §4.5 独立推导：$\sqrt{D\tau_{syn}} \approx 0.04\, B_{-4}^{-3/2}$（B₋₄ 单位为 100 μG）→ 一致。

## 5.2 两种根本不同的 MFA 机制（Blasi §4.4 首）

**[FACT]** 两大候选机制：

| 机制 | 位置 | 依赖 | 对加速的影响 |
|---|---|---|---|
| **Shock corrugation / Richtmyer-Meshkov**（Giacalone & Jokipii 2007；Sano 2012） | 下游 | 密度不均匀 δρ/ρ ~ 1 | 上游散射不变；只对**垂直激波**几何加速有帮助 |
| **加速粒子 streaming 不稳定**（Blasi 主流观点） | **上游** | CR 电流 | 上游 δB 增大 → 加速时间缩短 → PeVatron 可能 |

**[FACT]** 关键区分：只有**上游**放大能显著缩短加速时间；下游放大对 PeVatron 没有帮助。

## 5.3 共振 streaming 不稳定性（Blasi §4.2.1 & Amato §7）

### 5.3.1 中性条件与色散关系

**[FACT]** 上游等离子体（CR 为质子，背景 n_i 离子 + n_e 电子）满足：
- 电荷中性：$n_{CR} + n_i = n_e$（Blasi 式 (82)）
- 电流为零：$n_i v_i = n_e v_e$（Blasi 式 (83)）→ $v_e = V_{sh}\,n_i/(n_{CR}+n_i) \approx V_{sh}(1 - n_{CR}/n_i)$（Blasi 式 (84)）

**[FACT]** 全色散关系（Blasi 式 (85)）：
$$\frac{c^2 k^2}{\omega^2} = 1 + \sum_\alpha \frac{4\pi^2 q_\alpha^2}{\omega} \int dp \int d\mu\, p^2 v(p)(1-\mu^2)\, \frac{1}{\omega - k v \mu \pm \Omega_\alpha}\left[\frac{\partial f_{0,\alpha}}{\partial p} + \frac{1}{p}\left(\frac{v k}{\omega} - \mu\right)\frac{\partial f_{0,\alpha}}{\partial \mu}\right]$$

### 5.3.2 弱流极限（Zweibel 1979; Achterberg 1983）

**[FACT]** 条件（Blasi 式 (86)）：$n_{CR}/n_i \ll v_A^2/V_{sh}^2$ → 对应 ξ_CR ≪ $10^{-3}$

**[FACT]** 增长率为共振 Alfvén 波（Blasi 式 (87)）：
$$\omega_I(k) = \frac{\pi}{8}\, \Omega_p^*\, \frac{V_{sh}}{v_A}\, \frac{n_{CR}(p > p_{res}(k))}{n_i}$$

**[FACT]** 波功率谱在激波处（Blasi 式 (81)）：
$$F_0(k) = \frac{\pi}{4}\, \xi_{CR}\, \frac{V_{sh}}{v_A}\, \frac{1}{\Lambda}$$

典型参数（ξ_CR=0.1, V_sh=5000 km/s, v_A=3 km/s, Λ~10）→ **$F_{0}$ ≫ 1**，即弱流极限给出极强的放大。

### 5.3.3 强流极限（"CR modified regime"）

**[FACT]** 实际 SNR 中 ξ_CR ~ 10% ≫ $10^{-3}$ → 弱流条件**不成立**。此时（Blasi 式 (89)）：
$$\omega_I \approx \omega_R = \left(\frac{\pi}{8}\, \Omega_p^*\, k V_{sh}\, \frac{n_{CR}(p > p_{res})}{n_i}\right)^{1/2} \propto k \quad (k\,r_{L,0} \le 1)$$

**[FACT]** 强流极限下的波功率谱（Blasi 式 (90)）：
$$F_0(k) = \left(\frac{\pi}{6}\right)^{1/2}\left(\frac{\xi_{CR}}{\Lambda}\right)^{1/2}\left(\frac{c}{V_{sh}}\right)^{1/2} \lesssim 1$$

**[FACT]** Amato §7 独立推导相同结果（式 (29)、(30)），指出**相速度 Re(ω)/k ≈ 2% V_sh**——这是散射中心速度的关键修正，见下。

**[CRITIQUE]** **强流区的关键物理事实**：CR 效率越高，共振 Alfvén 波的放大**越弱**（$F_{0}$ ≲ 1）。这是过去数十年文献普遍误用弱流增长率（式 (87) / Amato 式 (16)）导致的系统性高估。Amato §7 专门揭露这一错误。

### 5.3.4 色散关系图示（Blasi Fig.9 / Amato Fig.11）

**[FACT]** Blasi Fig.9（Amato & Blasi 2009）：V_sh = $10^{9}$ cm/s, $B_{0}$ = 1 μG, n = 1 cm⁻³, ξ_CR = 10%, p_max = $10^{5}$ m_p c。上图左手极化、下图右手极化；实线 Re(ω)、虚线 Im(ω)。显示非共振模式在 k*r_L,0 ~ $10^{4}$ 处达到最大增长率。

**[FACT]** Amato Fig.11（完全同源）：展示弱流（点线，式 (16)/(26)）与强流（点划线，式 (29)）增长率的巨大差异；说明"标准"增长率高估了强流区。

## 5.4 非共振短波模式：Bell 模式（Blasi §4.2.2 & Amato §7）

**[FACT]** Bell (2004, 2005) 发现：当 ξ_CR 超过式 (91) 的阈值时，右旋模式在 k*r_L,0 > 1（**比所有加速粒子的回旋半径更小**）出现**非共振支**，增长率随 k^{1/2} 增加，达到最大（Blasi 式 (92)）：
$$k^* r_{L,0} = 3\, \xi_{CR}\, \gamma_{min}\, \frac{1}{\Lambda}\left(\frac{V_{sh}}{v_A}\right)^2 \frac{V_{sh}}{c}$$

**[FACT]** 特点：
- **电流驱动**，电流是 CR 电流导致的背景等离子体**返回电流**（电子相对离子漂移）；
- 生长极快（V_sh ~ $10^{4}$ km/s 时 ~$10^{4}$ 倍快于共振模式）；
- **几乎纯增长**（Re(ω) ≪ Im(ω)）；
- 尺度 < r_L,0 → **不能直接与加速粒子共振**（"散射在最小偏角制"，D(p) ∝ p²）。

**[FACT]** Zirakashvili et al. (2008) 数值：仅用 Bell 模式时 E_max ~ $10^{5}$ GeV（比膝低 1 个量级）。

**[CRITIQUE]** Bell 模式虽能解释 X 射线边缘的 ~100 μG 磁场，但**不能直接解决 PeVatron 散射问题**（尺度不匹配）。

## 5.5 丝状不稳定性（Filamentation）— 新的希望（Blasi §4.2.3）

**[FACT]** Bell (2004)、Riquelme & Spitkovsky (2009) 的 PIC 模拟显示：小尺度非共振模式在非线性发展中**向大尺度反级联**（inverse cascade）。

**[FACT]** Reville & Bell (2012)、Caprioli & Spitkovsky (2013)：逃逸 CR 电流诱导**丝状结构**，等离子体被 J×B 力挤出丝内部，丝相互吸引合并 → 放大发生在**接近逃逸粒子回旋半径**的尺度上。

**[FACT]** Bell et al. (2013)：若这一机制成立，年轻 SNR（V_sh ~ 5000 km/s，如 Tycho）可达 **~200 TeV**——比膝低 ~1 个量级；可能需要**更快的 SNR** 才能到 PeV。

**[CRITIQUE]** 该机制若仅由逃逸粒子驱动，则要求极年轻 SNR（V_sh 高），而这些 SNR 抛射物质少、加速粒子总量不足——**能量学**上难以支撑银河系 CR 总通量。

## 5.6 大尺度非共振模式：火管（Firehose）不稳定性（Blasi §4.2.4）

**[FACT]** 增长率为（Blasi 式 (93)）：
$$\Gamma_{FH}(k) \simeq \xi_{CR}^{1/2}\, \frac{V_{sh}^2 k}{c}$$

**[FACT]** 因 k ≪ 1/r_L,max，则 $\Gamma_{FH}\tau_{adv}(p_{max}) \ll \xi_{CR}^{1/2} < 1$ → **无足够时间增长**。

**[FACT]** 逃逸粒子分布的各向异性若比扩散近似更极端，可增强此机制——**目前不确定**。

## 5.7 放大磁场的动力学反作用（Blasi §4.3）

**[FACT]** 动量守恒含磁压（Blasi 式 (95)）：
$$\frac{\partial}{\partial z}\left(\rho u^2 + P_g + P_c + P_w\right) = 0$$

**[FACT]** 含波的总压缩比（Blasi 式 (98)）：
$$R_{tot}^{\gamma_g+1} = M_0^2 R_{sub}^{\gamma_g} \frac{\gamma_g+1 - R_{sub}(\gamma_g-1)}{1+\Lambda_B}$$

其中 $\Lambda_B = \frac{W}{1 + R_{sub}(2/\gamma_g - 1)}$，$W = P_{w,1}/P_{g,1}$ 是亚激波上游的**波压/热压**之比。

**[FACT]** 物理：W ≪ 1 → 磁压反作用可忽略；W ≳ 1 → **总压缩比下降** → 谱更"平"（接近幂律）；X 射线边缘暗示 W ~ 1–10。

**[FACT]** 反直觉结果：**放大磁场的动力学反作用使 NLDSA 的谱更简单**（更接近幂律），而非更复杂。

## 5.8 关于 MFA 的总评（Blasi §4.4）

**[FACT]** Blasi 的谨慎结论：
- X 射线边缘证实了放大；
- 但放大**是否与 PeV 加速所需的散射机制相同**尚不确切；
- 各种机制各有缺陷：
  - 共振 Alfvén 波（强流区）：放大被限制在 δB ~ $B_{0}$；
  - Bell 模式：尺度太小，不能直接散射 PeV 粒子；
  - 冲击畸变：只影响下游，帮助有限；
  - 火管：时间不够；
  - 丝状：需要年轻 SNR，能量学困难；
- **PeVatron 问题仍然开放**。