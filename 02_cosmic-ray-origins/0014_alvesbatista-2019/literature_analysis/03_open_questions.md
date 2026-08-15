---
title: §3 Open Questions
paper: alvesbatista-2019
section: 3
pages: '8-20'
source_file: fulltext.txt (UTF-8 copy)
source_lines: '416-1280'
parent: alvesbatista-2019
created: 2026-08-15
tags: [open questions, Hillas, source identification, BSM, LIV, magnetic fields, hadronic interactions]
---

> 本章属于：[Open Questions in Cosmic-Ray Research at Ultrahigh Energies]
>
> 上一章：`02_status_ultrahigh_energy.md`
>
> 下一章：`04_conclusions_and_perspectives.md`

# 3. Open Questions

## 3.1 本节核心内容

§3 是全篇的**主旨章节**——系统梳理 UHECR 领域的 7 大类开放问题：

1. **§3.1 Precision Measurements of Spectrum and Mass-Composition**（3.1.1 Energy resolution；3.1.2 Composition at UHE）
2. **§3.2 Astrophysics**：
   - 3.2.1 Origin of the Bulk of UHECRs（Hillas 判据、能量预算、各类候选源）
   - 3.2.2 Galactic to Extragalactic Transition（knee / second knee / ankle）
   - 3.2.3 Source Identification Beyond the Ankle（catalog cross-correlation、joint modeling）
   - 3.2.4 Steady and Transient Sources（$t_{prop}/t_{emiss}$ 判据）
   - 3.2.5 Origin of the End of the Cosmic-Ray Spectrum（GZK vs 最大能量）
   - 3.2.6 Magnetic Fields（GMF、EGMF 对偏转的影响）
3. **§3.3 Other Open Questions**：
   - 3.3.1 Hadronic Interactions at Ultrahigh Energies
   - 3.3.2 Physics Beyond the Standard Model（LIV、muon excess 的 BSM 解释）

[FACT] 本章是全篇信息密度最高、参考文献最密集的章节，**几乎每一句都有引用**——这是综述类章节的典型特征。

## 3.2 原文内容

### 3.2.1 §3.1 Precision Measurements of Spectrum and Mass-Composition（页 8-9）

**3.1.1 能量分辨率的重要性**：

[FACT] 作者用 Figure 8（Brämmel et al. 2013）演示"spillover"效应：对于 30% 能量分辨率的探测器，在 $E_{thresh}=10^{19.63}$ eV 阈值下，58% 的"事件"其实是来自 $E_{true}<E_{thresh}$ 的 spillover——被当作 isotropic background 稀释 signal。

[FACT] 关键结论：把阈值从 $10^{19.63}$ 提升到 $10^{19.83}$ eV，30% 分辨率的探测器可以达到与 10% 分辨率探测器在 $10^{19.63}$ eV 相同的"signal purity"，但代价是曝光量要加倍（flux 在提升阈值处下降约 2×）。

**3.1.2 成分在 UHE 的演化**：

[FACT] 成分演化（Figure 5 揭示的交替主导模式）可能是：
- **Peters cycle**（Peters 1961）：源端最大能量依赖 rigidity $R=E/Z$；
- **Photonuclear spallation**：传播过程中的光核碎裂，导致按 $E/A$ 标度。

[FACT] p/He 最大值比 $\approx 4$——**倾向于 spallation 情景**。但 Peters cycle + spallation 的叠加**未被排除**。

[FACT]  rigidity 演化：$\frac{1}{R} = \sum_i f_i Z_i/E$，Figure 9 显示 rigidity 随能量增大而增大——因此磁场偏转随能量减小，**"mass increase is slow enough to not outrun the energy increase"**。

### 3.2.2 §3.2.1 Origin of the Bulk of UHECRs（页 10-13）

**Hillas 判据**：

[FACT] Hillas (1984) 的最小约束：粒子能被束缚在加速区内的条件是 Larmor 半径 $r_L$ 小于加速器尺寸 $R$，给出：
$$E_{max} = eBR$$
$$R = l \cdot \delta$$
其中 $l$ 是源 comoving 尺寸，$\delta$ 是流的 Lorentz factor（AGN jets $\delta\sim10$–50；GRB $\delta\sim10$–1000）。

[FACT] Shock 加速公式（Equation 1）：
$$E_{max} = \eta \beta_{sh} eBR$$
其中 $\eta$ 表征加速效率（Bohm limit $\eta=1$）。

[FACT] Hillas 判据**不是充分条件**——还需能量预算约束。Figure 11 展示"luminosity-density diagram"：
- 黑实线：Auger 最佳拟合的 UHECR 产率 $\dot{\mathcal{E}}_{UHE}\approx 5\times10^{44}$ erg Mpc$^{-3}$ yr$^{-1}$（Aab et al. 2017d）；
- 橙虚线：源数密度下限（来自 Abreu et al. 2013 的无聚类分析）；
- 对角线：能量预算约束 $L_{CR}=L_{\lambda}$（以及 $0.1\times$、$10\times$ 的虚线）。

[FACT] **候选源分类**：
- GRB（高光度、低光度）、超新星、jetted AGN、TDE（Swift J1644+57）、starburst galaxies、galaxy clusters、pulsars/magnetars。
- **Wolf-Rayet 星风**在 Hillas 图上不满足 $10^{20}$ eV 约束。
- **Blazar**（指向地球喷流的 AGN）不满足数密度约束。
- **Radio galaxies**（包括 Cen A）是最长期、最有力的候选者。
- **TDE**：理论上可能满足能量预算，但 Swift 数据暗示实际率不足。

### 3.2.3 §3.2.2 Galactic to Extragalactic Transition（页 13-14）

[FACT] 宇宙线谱在 $10^{15}$–$10^{18}$ eV 有三个断点（Figure 12）：
- **Knee** $\sim 3$ PeV
- **Second knee / iron knee** $\sim 100$ PeV
- **Ankle** $\sim 10^{18.6}$ eV

**Knee 的两种起源**：
- **传播起源**：PeV CR 的 Larmor 半径在 $\sim\mu$G GMF 中达到 $1$ pc，与 SNR 驱动湍流的最大尺度 $l_{max}$ 相当，散射变得低效——谱变陡。
- **最大能量起源**：SNR 的 Hillas 最大能量：
$$E_{max} = \eta\beta_{sh}eBR \approx 10 \cdot \eta\beta_{sh} B_{3\mu G} R_{10\,pc} \text{ TeV}$$

[FACT] Bell 机制（Bell 1978）：CR 加速粒子驱动磁流体不稳定性，放大上游磁场——观测上已有证据。

[FACT] KASCADE-Grande 报告"second knee"在 $100$ PeV（Apel et al. 2011）——若 knee 是质子，则 $100$ PeV 的 iron knee 与 rigidity 标度一致。

[FACT] 已知银河系 PeVatron：Sgr A\*（Abramowski et al. 2016），但其 CR 光度在 PeV 能段偏低。

**Ankle 与 extragalactic component**：

[FACT] EeV 能量的 extragalactic protons 通过 Bethe-Heitler 与 CMB 作用产生 pair-production：
$$p + \gamma_{\rm CMB} \to p + e^+e^-$$
时间尺度为 Gyr 量级。这些 pair 触发电磁级联，贡献 diffuse gamma-ray background。Fermi-LAT 的 gamma-ray background 约束偏好**负演化（negative evolution）**：UHECR 源在 extragalactic 空间的 filling factor 很小。

### 3.2.4 §3.2.3 Source Identification Beyond the Ankle（页 14-15）

[FACT] Auger 发现的大尺度各向异性与 2MASS 的近红外 extragalactic matter 分布一致（Aab et al. 2017b）——这是"first observational evidence for UHECRs beyond the ankle originating from extragalactic sources"。

[FACT] 小尺度 cross-correlation：
- 与 2MASS / Swift-BAT X-ray：$3$–$4\sigma$ 的 $10$–$15\%$ 事件相关性；
- 与 starburst galaxies 和 jetted AGN（radio+gamma）：类似。

[FACT] **Auger + TA 联合分析**（Aab et al. 2014d; Biteau et al. 2018）：通过匹配共同赤纬带的 flux，提供共同天空视图。

[FACT] **Electromagnetic counterpart 下限**（Equation 4）：
$$L_{\rm photon} > 3\times10^{44} \text{ erg s}^{-1} \left(\frac{E/Z}{10^{18.5}\text{ V}}\right)^2 \left(\frac{\epsilon}{100}\right)^{2/\eta}$$
假设 electron 与磁场等分（equipartition）。对应的最小可测流量 $S_{min}\approx 2\times10^{-12}$ erg cm$^{-2}$ s$^{-1}$——**与 Fermi-LAT / WISE 全天空巡天灵敏度相当**。

[FACT] 两个阻碍：(1) 银河系平面的 foreground；(2) 缺乏全天空光谱巡天（redshift 信息）。

### 3.2.5 §3.2.4 Steady and Transient Sources（页 15-16）

[FACT] 区分判据：$t_{prop}/t_{emiss}$
- $t_{prop}/t_{emiss}<1$：steady source
- $t_{prop}/t_{emiss}>1$：transient source

[FACT] AGN jet 活动时间尺度 $\sim 300$ Myr（Wykes et al. 2013）；UHECR 的 ballistic propagation 时间（10 Mpc 距离）$\sim 30$ Myr——因此 $t_{prop}<t_{emiss}$，**AGN 是 steady source**。

[FACT] GRB 的 VHE gamma-ray 发射时间尺度 $<1000$ s（GRB 130427A）——因此 **GRB 是 transient source**。

[FACT] **"Magnetic horizon"**：低能端，CR 的扩散球最终不再与邻近源的扩散球重叠——这一现象称为 magnetic horizon，导致所有源的稳态发射在低能端**都不可达到**。

[FACT] 高能端，能量损失缩短 $t_{emiss}$，使 $t_{prop}/t_{emiss}>1$——因此**源类可能在有限能量范围内实现稳态，低于或高于这个范围只有 transient**。

### 3.2.6 §3.2.5 Origin of the End of the Cosmic-Ray Spectrum（页 16-17）

[FACT] UHECR 谱的截止是"established unambiguously recently"——但起源仍有争议。

[FACT] Figure 13：用 CRPropa 模拟不同单一初级成分（p, He, N, Si, Fe）的传播，源演化按 SFR（Robertson et al. 2015）或 AGN density（Ahlers et al. 2005）。
- 引入最大能量作为自由参数后，无论源端成分如何都能拟合 Earth 上的谱；
- 但"pure GZK scenarios"（最大能量足够高）的拟合**同时预测的成分与 Auger/TA 观测不符**。

[FACT] 关键模型（Fang et al. 2013; Aab et al. 2017d; Wittkowski 2018）：
- 最大 rigidity $\sim 10^{18.8}$ V
- 中等质量核素主导
- 源谱较硬 $\gamma \sim 1.6$
- 流强抑制 = 传播效应 + 源端最大能量 的组合。

### 3.2.7 §3.2.6 Magnetic Fields（页 18-19）

[FACT] EGMF 的不确定性：
- void 场：$10^{-17}$ G（Neronov & Vovk 2010，来自 gamma-ray-induced cascades）；
- 但 EGMF 的整体空间分布缺乏观测约束。

[FACT] 宇宙学模拟的不同结论：
- Sigl et al. (2003a,b) 与 Dolag et al. (2005) 结论冲突；
- Dolag：$E>40$ EeV 偏转很小；Sigl：UHECR astronomy 前景不利；
- Hackstein et al. (2016, 2018) 考虑 astrophysical + primordial seed，确认 Dolag 结论。

[FACT] Farrar & Sutherland (2017) 在 JF12 GMF 模型下的 backtracking：
- $R<10$ EV 偏转大（$\sim90°$）；
- $R>20$ EV 不同 GMF 模型给出一致偏转，**允许对 arrival directions 做 GMF 修正**（除银盘附近 $|b|<19.5°$）。

[FACT] 利用 UHECR 约束 EGMF：Yüksel et al. (2012) 论证：Auger 观测到的 Cen A 相关若成立，暗示 $B\sim 20$ nG 的 EGMF。

[FACT] Figure 14：CRPropa 模拟，p（黑）、N（蓝，$7\le A\le 19$）、Fe（红，$40\le A\le 56$）三种初级成分注入，按 SFR 演化、纯幂律谱至 $10^{22}$ eV，分别拟合 Auger（上）和 TA（下）数据。

### 3.2.8 §3.3 Other Open Questions

**3.3.1 Hadronic Interactions**：

[FACT] 核心困难：
- p-p 截面和次级粒子多重度在 LHC 数据下**温和上升**；
- 从 pp/p-pbar 到 pi-p、K-p 再到核-核的外推**在软/硬过程过渡区域几乎无法理解**（Regge parameterization for soft, QCD-improved parton model for hard）；
- p-Pb、Pb-Pb 的数据**不能以所需精度**转移到轻核；
- 建议在 LHC 做 p-O 测量——是"key measurement for improving air shower predictions"。

[FACT] 高多重度 pp 事件表现出"heavy ion collision"特征（QGP-like collectivity）——这会影响强子相互作用模型的构建。

**3.3.2 Physics Beyond the Standard Model**：

[FACT] UHECR 与 $\gamma\sim$ GeV 背景作用时的质心能量（Equation 5）：
$$\sqrt{s} \approx \sqrt{2E\epsilon} \approx 40\sqrt{\epsilon_{\rm GeV}}\sqrt{E_{10^{18}{\rm eV}}} \text{ TeV}$$
因此 UHECR 传播**不能探测 Lorentz-invariant 的 BSM 物理**，但可以探测 Lorentz boost 下的 Lorentz 破缺。

[FACT] **Lorentz-Invariance Violation**（Equation 6）——dimension-5 CPT-odd operator（Myers & Pospelov 2003）：
$$\mathcal{L}_{\rm LIV} = -\frac{\xi}{2M_{Pl}}u^\mu F_{\mu\nu}(u\cdot\partial)u_\alpha\tilde{F}^{\alpha\nu}+\frac{\xi_1}{2M_{Pl}}\bar\psi\gamma_\mu u^\mu(1+\xi_2\gamma_5)(u\cdot\partial)\psi$$

[FACT] 色散关系修正（Equation 7）：
$$E_{\pm}^2 = m^2 + p^2\left(1\pm\frac{\xi_\pm\,p}{M_{Pl}^n}\right)$$
其中 $n=d-4$，$M_{Pl}$ 是 Planck mass。

[FACT] 关键能量尺度（Equation 8）：
$$E_{cr} = E_{Pl}\left(\frac{m^2}{M_{Pl}^n}|\xi|\right)^{1/(n+2)}$$

[FACT] **Muon excess 的 BSM 解释**：
- KASCADE-Grande 在 $>10^{16}$ eV 看到 muon 过量（Apel et al. 2017）；
- Auger 也看到 $\sim1.5\times$ 过量（Aab et al. 2016a）；
- $f_0$（neutral pion branching ratio）决定 hadronic channel 的能量份额——若 $f_0$ 减小，muon 数增加；
- Farrar & Allen (2013a,b)：若 chiral symmetry 在某 $\sqrt{s}$ 恢复，pion 可能变重、产生被抑制，能量流入 baryon-antibaryon 通道；
- Anchordoqui et al. (2017)：可能产生 deconfined quark-gluon fireball；
- 若 high-energy neutral pion 稳定或衰变率降低（LIV 效应），能量也流入 hadronic channel。

## 3.3 关键公式

**Hillas 判据**（Equation 1）：
$$E_{max} = \eta\,\beta_{sh}\,eBR$$

**SNR Hillas 最大能量**（Equation 3）：
$$E_{max} = \eta\beta_{sh}eBR \approx 10\,\eta\beta_{sh}B_{3\mu G}R_{10\,pc}\text{ TeV}$$

**Photon luminosity 下限**（Equation 4）：
$$L_{\rm photon}>3\times10^{44}\text{ erg s}^{-1}\left(\frac{E/Z}{10^{18.5}\text{ V}}\right)^2\left(\frac{\epsilon}{100}\right)^{2/\eta}$$

**UHECR 与 background photon 的质心能量**（Equation 5）：
$$\sqrt{s}\approx\sqrt{2E\epsilon}\approx 40\sqrt{\epsilon_{\rm GeV}}\sqrt{E_{10^{18}\text{eV}}}\text{ TeV}$$

**CPT-odd dimension-5 LIV operator**（Equation 6）：
$$\mathcal{L}_{\rm LIV}=-\frac{\xi}{2M_{Pl}}u^\mu F_{\mu\nu}(u\cdot\partial)u_\alpha\tilde{F}^{\alpha\nu}+\frac{\xi_1}{2M_{Pl}}\bar\psi\gamma_\mu u^\mu(1+\xi_2\gamma_5)(u\cdot\partial)\psi$$

**LIV 修正色散关系**（Equation 7）：
$$E_\pm^2=m^2+p^2\left(1\pm\frac{\xi_\pm\,p}{M_{Pl}^n}\right)$$

**LIV 临界能量**（Equation 8）：
$$E_{cr}=E_{Pl}\left(\frac{m^2}{M_{Pl}^n}|\xi|\right)^{1/(n+2)}$$

**Peters cycle rigidity**：
$$R=E/Z, \qquad \frac{1}{R}=\sum_i f_i Z_i/E$$

**Bethe-Heitler pair production**：
$$p+\gamma_{\rm CMB}\to p+e^+e^-$$

**Muons in shower**（branching ratio $f_0$）：
$$E_{had}(n)\propto(1-f_0)^n$$

**Cosmogenic photon flux 上限（Auger）**：
$$\Phi_{\gamma}>10^{18}\text{eV} < 0.1\%$$

## 3.4 关键参数

| 参数 | 数值 | 来源/章节 |
|---|---|---|
| AGN jets $\delta$ | $10$–$50$ | §3.2.1 |
| GRB $\delta$ | $10$–$1000$ | §3.2.1 |
| UHECR 产率 | $\sim 5\times10^{44}$ erg Mpc$^{-3}$ yr$^{-1}$ | Aab et al. 2017d |
| 早期 UHECR 产率估计 | $\sim 5\times10^{43}$ erg s$^{-1}$ yr$^{-1}$ | Waxman 1995b 等 |
| AGN jet 活动 timescale | $\sim 300$ Myr | §3.2.4 |
| 10 Mpc ballistic 传播时间 | $\sim 30$ Myr | §3.2.4 |
| EGMF void 场下限 | $10^{-17}$ G | Neronov & Vovk 2010 |
| Farrar-Sutherland backtracking 上限 | $R>20$ EV（除银盘外） | §3.2.6 |
| EGMF Cen A 约束 | $\sim 20$ nG | Yüksel et al. 2012 |
| Knee 能量 | $\sim 3$ PeV | §3.2.2 |
| Second knee | $\sim 100$ PeV | KASCADE-Grande |
| SNR Hillas max | $\sim 10$ TeV（无放大） | Equation 3 |
| 最大 rigidity（拟合） | $\sim 10^{18.8}$ V | §3.2.5 |
| 最佳拟合源谱指数 | $\gamma\sim 1.6$ | §3.2.5 |
| EGMF deflection（$E>50$ EeV 质子） | $<2°$ 在 $\sim1/4$ 天空 | §3.2.6 |
| UHECR 传播 $\sqrt{s}$ | $\sim 40$ TeV（$\epsilon$=GeV, $E=10^{18}$ eV） | Equation 5 |
| Auger muon excess | $\sim 1.5\times$ | Aab et al. 2016a |

## 3.5 图表分析

### Figure 8 — *Effect of spillover*

**图的目的**：演示能量分辨率对 source-correlated events 稀释的影响。

**关键数值**：30% 分辨率、$E_{thresh}=10^{19.63}$ eV 时，58% 的"events"是 spillover background。

**物理意义**：[INTERPRETATION] 这直接说明为什么 UHECR 领域需要"更精确的能量分辨率"——否则 anisotropy 信号被大量低能 isotropic 事件稀释。

**注意**：[CRITIQUE] 这是简化模型（单一 threshold），实际探测器可能有更复杂的 energy response。

---

### Figure 9 — *UHECR rigidity evolution*

**图的目的**：用 Auger composition fractions（Bellido 2018, Aab et al. 2014b）计算平均 rigidity 随能量的演化。

**关键观察**：rigidity 随能量增大——因此 angular deflection 随能量减小。

**注意**：[CRITIQUE] 用 $X_{max}$ 推断的 "average logarithmic mass" **不是** rigidity，因为 $A/Z\approx 2$（除质子外 $A/Z=1$）——这个差异在强各向异性搜索中至关重要。

---

### Figure 10 — *Hillas diagram*

**图的目的**：在 $\log R$–$\log B$ 平面上展示各类源满足 Hillas 判据的可行性。

**图中元素**：
- 实线：fast shock $\beta_{sh}=1$ 的 p（红）和 Fe（蓝）$10^{20}$ eV 约束；
- 虚线：slow shock $\beta_{sh}=0.01$。

**关键观察**：normal galaxies、supernovae、Wolf-Rayet stars **不满足** Hillas 判据；其他源类均满足。

**注意**：[CRITIQUE] Hillas 判据是**必要非充分条件**——满足 Hillas 不保证能加速到 $10^{20}$ eV（还需能量损失、加速时间等约束）。

---

### Figure 11 — *Luminosity vs. number density*

**图的目的**：对比各类源的"辐射光度 vs 源数密度"，与 UHECR 能量预算（黑线）和数密度下限（橙线）比较。

**关键观察**：
- HL GRB：roughly consistent with energy budget（偏低）；
- LL GRB：数密度更大，但 true rate 不确定；
- Radio galaxies（FRI/FRII）：可能满足；
- Cen A：长期候选者。

**注意**：[CRITIQUE] 横纵坐标的"luminosity"是**辐射光度**（IR/radio/X/gamma），不是 CR 光度；两者之间的换算（$\epsilon_{CR}$）是未知参数。

---

### Figure 12 — *Spectral breaks schematic*

**图的目的**：展示 knee / second knee / ankle 三个断点的位置与可能的物理解释。

**关键数值**：knee $\sim 3$ PeV，second knee $\sim 100$ PeV，ankle $\sim 10^{18.6}$ eV。

---

### Figure 13 — *Propagation fits (pure primary beams)*

**图的目的**：用 CRPropa 模拟纯 p/He/N/Si/Fe 注入，测试能否拟合 Auger 数据。

**关键观察**：引入最大能量自由参数后，单一初级成分**都能**拟合谱——但纯 GZK 情景（最大能量足够高）预言的成分与数据不符。

---

### Figure 14 — *Mixed composition CRPropa fits*

**图的目的**：三种初级束（p、N、Fe）分别拟合 Auger 和 TA 数据。

**关键观察**：两种实验可分别被相似的注入成分拟合——但 Auger 拟合偏好更重的成分，TA 偏好更轻——**与 §2.3 的观测差异一致**。

---

### Figure 15 — *EGMF volume filling factors*

**图的目的**：展示不同 EGMF 模型（Alves Batista 2017, Das 2008, Dolag 2005, Hackstein 2018, Kotera & Lemoine 2008a, Sigl 2003b）的宇宙学 filling factor。

**关键观察**：不同模型在 filling factor 上跨越 3 个数量级——**反映 EGMF 不确定度的巨大范围**。

---

### Figure 16 — *Experiments timeline*

**图的目的**：展示 UHECR 与 UHE neutrino 实验的暴露量随时间演化（地面 & 空间；现有、升级、提议）。

**关键实验**：Auger 升级、TA×4、POEMMA、GRAND（10k & 200k）、ARA-37、ARIANNA、Trinity、K-EUSO、TUS。

---

### Figure 17 — *Cosmogenic neutrino sensitivities*

**图的目的**：对比 cosmogenic neutrino 预言与 IceCube/Auger 上限及下一代实验灵敏度。

**关键观察**：IceCube 上限 $\sim 3\times10^{-8}$ GeV cm$^{-2}$ s$^{-1}$ sr$^{-1}$ at EeV；POEMMA / GRAND 可将灵敏度推进 $\sim 1$ 个数量级。

## 3.6 作者的逻辑

[INTERPRETATION] §3 的论证结构呈现**由"测量精度"到"物理图像"到"BSM 前沿"的递进**：

```
§3.1 Precision Measurements（测量基础）
  → 能量分辨率、成分精度 → "数据能说什么"
  →
§3.2 Astrophysics（物理图像）
  → 源类（Hillas + 能量预算 + 数密度约束）
  → 过渡区（Galactic → extragalactic）
  → 源识别（catalog、EM counterpart）
  → 稳态 vs 瞬变
  → cutoff 起源
  → 磁场
  →
§3.3 Other（BSM + hadronic 相互作用）
  → 强子模型的极限
  → LIV 与 muon excess 的新物理可能
```

**核心逻辑转折**：

[FACT] 作者反复强调一个"三角关系"：**观测约束 ⇄ 强子模型系统误差 ⇄ BSM 新物理**——任何一项的突破都可能改变其他两项的解读。例如 muon excess 可能是强子模型缺陷，也可能是 LIV 效应。

**§3.2 内部的关键逻辑**：

1. 从 Hillas 判据（§3.2.1）的"必要非充分条件"出发，逐层增加约束（能量预算、数密度、数密度下限），**逐步淘汰候选源**。
2. 用"steady vs transient"（§3.2.4）区分源的观测特征。
3. 用"cutoff origin"（§3.2.5）检验 GZK 假说与源端最大能量假说。

## 3.7 我的理解

[INTERPRETATION]

1. **Hillas 判据在 §3 的地位**：它是 UHECR 源讨论的**起点也是终点**——每一个候选源都被"先 Hillas、再能量预算、再数密度"三层筛过滤。这反映出 UHECR 源问题的"几何约束 + 能量约束 + 统计约束"的三重结构。

2. **Negative source evolution 的反复出现**：§2.4 的 cosmogenic 拟合、§3.2.2 的 Fermi-LAT gamma-ray background 约束、§3.2.5 的 CRPropa 拟合——三条独立线索都指向"UHECR 源在局部宇宙富集"（local overdensity 或 cosmic variance）。这是一个**跨子领域的隐性共识**。

3. **"Correlation ≠ Causation"**（§3.2.3）——作者明确提醒：即使 $5\sigma$ 的 anisotropy 与 catalog 相关，也可能有隐藏变量造成伪相关。要"identification"，需要全天空覆盖 + redshift 演化约束 + 源模型 completeness——**这是 2025 年后多信使时代的"gold standard"**。

4. **Muon excess 的双重解读**：§3.3.2 把 muon excess 同时作为"强子模型缺陷"（Standard Model 内）和"新物理信号"（BSM）的候选——这是**同一现象的两种极端解读**，反映 UHECR 领域"数据驱动新物理"的独特地位。

5. **Equation 4 的巧妙性**：Hillas 判据 + equipartition 假设 → 最小可测 electromagnetic flux → 与 Fermi-LAT/WISE 巡天灵敏度对比。这是一个"用 Hillas 判据反过来约束 electromagnetic 观测"的方法学创新。

[CRITIQUE]

6. **§3.2.1 的"能量预算"论证对 AGN 的偏好**：能量预算 $\sim 5\times10^{44}$ erg Mpc$^{-3}$ yr$^{-1}$ 的推导基于 Aab et al. 2017d 的 best-fit，但该 fit 本身依赖 strong 假设（mixed composition、SFR evolution）。**若 best-fit 改变，能量预算也会变**。

7. **§3.3.2 的 LIV 讨论的"边缘性"**：dimension-5 CPT-odd operator 是最保守的 LIV 模型，但方程 (6) 只考虑了 photon 和 electron——对 hadronic 过程的 LIV 影响几乎没有讨论。**这是 §3.3.2 的一个缺口**。

8. **"Pure GZK"假说的"救活"空间**：作者承认"引入最大能量自由参数后都能拟合"——这意味着**GZK cutoff 的观测特征无法单独区分"纯 GZK"vs"最大能量 + GZK"**，需要成分的独立约束。

9. **Equation 3 对 SNR 的"最大能量 = TeV"**的结论——与 Bell 机制增强磁场后的 PeV 可能性有张力。作者承认"SNR 是否真的能达到 3 PeV 仍是开放问题"——这是**Galactic UHECR 研究的根本瓶颈**。

10. **EGMF 的不确定性**（§3.2.6）：**10$^{-17}$ G 到 10$^{-9}$ G** 的跨度（跨越 8 个数量级）意味着**所有 UHECR 偏转计算都带有一个巨大的系统误差**。这是"能否做 UHECR astronomy"的最关键不确定度。

## 3.8 潜在问题与值得关注的地方

[CRITIQUE]

1. **Hillas 判据的"必要性 vs 充分性"平衡**：§3.2.1 用 Hillas + 能量预算 + 数密度三约束层层筛选源类，但在"AGN"小节用了大量篇幅，"GRB"和"TDE"则篇幅相对少——这是否反映了**作者团队（Auger 主导）对 AGN 的偏好**？

2. **"Local overdensity"假设的风险**：§2.4 与 §3.2.2 都暗示 UHECR 源可能在局部富集。若这是真的，则**所有基于均匀源分布的 cosmogenic neutrino 预言都可能高估了一个数量级**。

3. **Equation 4 的 equipartition 假设**：$L_{CR}=L_{\lambda}$ 是一个"标准假设"，但**实际可能偏离 100 倍**。Figure 11 的 $0.1\times$ 和 $10\times$ 虚线正是为了反映这个不确定度。

4. **Steady vs Transient 的判据边界**：$t_{prop}/t_{emiss}=1$ 是"临界"，但**在临界附近源的观测特征（各向异性模式、time variability）有怎样的区别**？作者没有详细讨论。

5. **Muon excess 的"新物理 vs 强子模型"歧义**：[CRITIQUE] §3.3.2 把 muon excess 同时当作"模型缺陷信号"和"BSM 候选信号"，但没有提供**实验上区分这两种解释的方案**——这是本文的一个方法论缺口。

6. **Equation 5 的"40 TeV"**：UHECR 传播的 $\sqrt{s}\sim 40$ TeV（当 $\epsilon\sim$GeV、$E\sim 10^{18}$ eV 时）——**正好接近 LHC 的能量**。这意味着 UHECR 传播**可以被 LHC 数据直接检验**（至少在 SM 内）——这一交叉验证的潜力值得注意。

7. **方程 (6) 中 CPT-odd 的选择**：§3.3.2 只讨论 CPT-odd 的 LIV——CPT-even 的 LIV 可能有不同的实验信号（如 photon dispersion 的 helicity-independent 项）。选择 CPT-odd 可能因为**它是最易被实验约束的 LIV 形式**，但读者应意识到这是**刻意选择而非完整覆盖**。

8. **LIV 临界能量（Equation 8）**：$E_{cr}$ 的表达式含 $M_{Pl}^n$——对于 dimension-5 算符（$n=1$），$E_{cr}$ 可达 $10^{19}$ eV 量级（若 $\xi\sim 1$），与 UHECR 能量相当——**这就是为什么 UHECR 是 LIV 的天然实验室**。

9. **Bethe-Heitler 与 GZK 的能量尺度差异**：§3.2.2 的 Bethe-Heitler（pair production）在 EeV 起作用，而 §3.2.5 的 GZK（photopion）在 $\sim 5\times10^{19}$ eV 起作用——**两者是 UHECR 传播的两个不同能量区间，需要不同的传播模型处理**。

10. **KASCADE-Grande 的"second knee"报告**（Apel et al. 2011）：这是**全篇唯一被引用的地面实验膝点数据**——KASCADE-Grande 已停止运行，其数据是否被更新分析验证，是读者应关注的后续。

---

## Frontmatter 元数据

```yaml
chapter: 3
chapter_title: Open Questions
paper_id: alvesbatista-2019
pages_covered: '8-20'
source_file: /tmp/batch4_utf8/0014_alvesbatista-2019_fulltext.txt
source_line_range: '416-1280'
figures_referenced: [Figure 8, Figure 9, Figure 10, Figure 11, Figure 12, Figure 13, Figure 14, Figure 15, Figure 16, Figure 17]
tables_referenced: []
equations:
  - 'Eq 1: E_max = η·β_sh·eBR (Hillas shock)'
  - 'Eq 3: E_max ≈ 10·η·β_sh·B_{3μG}·R_{10pc} TeV (SNR)'
  - 'Eq 4: L_photon > 3×10^44 erg/s (EM counterpart bound)'
  - 'Eq 5: √s ≈ √(2Eε) (BSM CM energy)'
  - 'Eq 6: L_LIV = CPT-odd dim-5 operator'
  - 'Eq 7: $E_{\pm}^2 = m^2 + p^2\left(1\pm\frac{\xi_\pm\,p}{M_{Pl}^n}\right)$ (LIV dispersion)'
  - 'Eq 8: $E_{cr} = E_{Pl} (m^2|M|/M_{Pl}^n)^{1/(n+2)}$'
key_topics:
  - Spillover effect (energy resolution)
  - Peters cycle vs spallation
  - Rigidity evolution (R=E/Z)
  - Hillas criterion (necessary, not sufficient)
  - Source energy budget (5×10^44 erg/Mpc$^{3}$/yr)
  - Steady vs transient sources (t_prop/t_emiss)
  - GZK cutoff origin (pure GZK vs max energy)
  - EGMF constraints (10^-17 to 10^-9 G)
  - Hadronic interaction uncertainties
  - Muon excess (BSM vs hadronic model)
  - Lorentz-invariance violation
  - LIV dispersion relations
key_references:
  - Hillas 1984
  - Aab et al. 2017d (combined fit)
  - Abreu et al. 2013 (source density)
  - Aab et al. 2017b (dipole/2MASS)
  - Biteau et al. 2018 (Auger-TA joint)
  - Farrar & Sutherland 2017 (GMF backtracking)
  - Yüksel et al. 2012 (EGMF Cen A)
  - Fang et al. 2013 (rigidity max)
  - Aab et al. 2016a (muon excess)
  - Apel et al. 2017 (KASCADE-Grande muon)
  - Myers & Pospelov 2003 (LIV operator)
  - Anchordoqui et al. 2017 (QGP fireball)
cross_references:
  - '02_status_ultrahigh_energy.md (§2.3 Composition, §2.5 Hadronic)'
  - '04_conclusions_and_perspectives.md (§4 Action Items)'
next_chapter: 04_conclusions_and_perspectives.md
```

---

**页码引用**：本节对应原文页 8-20（fulltext UTF-8 行 416-1280），Frontiers in Astronomy and Space Sciences 6:23 (2019)。