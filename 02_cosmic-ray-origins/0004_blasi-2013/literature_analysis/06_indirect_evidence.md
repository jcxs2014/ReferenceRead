---
chapter: 6
title: Indirect evidence for CR acceleration in SNRs
pages: "Blasi 2013, §6 (pp. 47–58)"
sections:
  - "6.1 Escape"
  - "6.2 Spectra"
  - "6.3 Gamma ray emission from isolated SNRs"
  - "6.4 SNRs near molecular clouds"
related_chapters:
  prev: 05_superbubble
  next: 07_h_alpha
status: done
---

> 本章属于：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/00_overview.md|The Origin of Galactic Cosmic Rays（Blasi, 2013, arXiv:1311.7346）]]
>
> 上一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/05_superbubble.md|05_superbubble]]
>
> 下一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/07_h_alpha.md|07_h_alpha]]

# 6 Indirect evidence for CR acceleration in SNRs — SNR 范式的实证检验

[FACT] §6 是全文的**实证检验枢纽**，从四个角度对 SNR 范式进行交叉验证：**CR 逃逸机制**（§6.1）→ **逃逸谱的硬软冲突**（§6.2）→ **孤立 SNR 的多波段建模**（§6.3，两个案例 RX J1713 与 Tycho）→ **源-分子云复合系统的传播与 $\pi^0$ 鼓包**（§6.4，IC 443、W44、W28）。

[INTERPRETATION] §6 的逻辑链条是：**多波段辐射是 CR 加速的直接证据**（§6 引言：同步辐射 $\nu$ ≃ 3.7 MHz · B$_\mu$ · E$^2$(GeV)）→ **K$_{ep}$ 的 1–2 个量级差异**（NLDSA 预言 ~$10^{-3}$–$10^{-4}$ vs 地球观测 ~$10^{-2}$）→ **逃逸机制与逃逸谱形状**（§6.1，$N_{\rm esc}\propto p^{-4}$）→ **逃逸谱在最高能段的 concavity 与 bump**（§6.2，Figure 10）→ **各向异性冲突**（$D(E)\propto E^{0.7}$ vs 观测）→ **两个孤立 SNR 的对比**（§6.3）→ **$\pi^0$ 鼓包的确凿性**（§6.4）。作者刻意避免\"最终结论\"，而是给出\"每个观测都对 SNR 范式施加不同方向的约束\"——这正是 §8 中\"circumstantial evidence\"的实证基础。

---

## 6 引言 — SNR 作为 CR 加速位点的辐射证据

[FACT] 作者开篇直述（原文）：\"There is no doubt that SNRs are sites of cosmic ray acceleration. The subject of the debate is whether all CRs are accelerated in SNRs, and which SNRs or which phases of a SNR may possibly allow for CR acceleration up to the energy of the knee. This confidence is based on direct observation of the radiation produced by CRs while being accelerated inside the sources.\"

[FACT] 射电同步辐射频率关系（原文 Eq. 附近）：$\nu \simeq 3.7\,\mathrm{MHz}\cdot B_\mu \cdot E(\mathrm{GeV})^2$。

[FACT] **磁场放大对射电诊断的双重影响**：
- 若 $B$ 放大到 ~100 $\mu$G：GHz 射电对应 $E \sim 1$–2 GeV 电子；未放大则 ~10–20 GeV
- X 射线 1 keV 同步辐射对应 $E \sim 20$–30 TeV（100 $\mu$G 场下）
- **谱的凹性**（concavity）：NLDSA 强动力学反作用下 GeV 段比 ~10 GeV 段更陡 → 可能在射电-$\gamma$ 谱中可见

[FACT] **K$_{ep}$ 差异**：NLDSA 要求 $K_{ep} \sim 10^{-3}$–$10^{-4}$；地球测量 $K_{ep} \sim 10^{-2}$ ——存在 1–2 个量级差异。

[FACT] K$_{ep}$ 测量差异的物理根源（原文）：\"The value of $K_{ep}$ as inferred from multiwavelength studies in the sources reflects the instantaneous ratio ... while the value of $K_{ep}$ as measured at Earth is the result of the integration over time of the escape flux and the overlap of potentially different numerous sources.\" ——**瞬时比值 vs 时积分值**的差异是 SNR 范式\"simple nature\"背后的\"complexity\"。

[FACT] §6 引言的**双重遗留问题**预告：逃逸机制（§6.1）与谱的硬软冲突（§6.2），二者都被明确标为\"most uncertain aspects\"。

---

### 6.1 Escape

> **CR 从 SNR 的逃逸机制**

[FACT] 三种逃逸机制（原文逐一列举）：
1. **激波减速**（Sedov-Taylor 相 $R_{\rm sh}\propto t^{2/5}$，$V_{\rm sh}\propto t^{-3/5}$；扩散前沿 $\propto t^{1/2}$ 展开）→ 返回概率降低
2. **激波破裂**（shock broken）→ 粒子可通过环境缺口逃逸
3. **自散射中心失效**：CR 通过 streaming 不稳定性自激的散射中心，在远离激波处因粒子密度下降而失效

[FACT] 作者引述 Drury (2011) 作为该问题的系统综述。

[FACT] **标准逃逸边界模型**：在 $z_0$ 处 $f(p,z_0)=0$ 的边界条件（原文 Eq. 101）：

$$
f(z,p) = f_0(p)\,\frac{\exp(uz/D(p)) - \exp(uz_0/D(p))}{1 - \exp(uz_0/D(p))} \quad \text{(Eq. 101)}
$$

[FACT] **逃逸通量**（原文 Eq. 102）：

$$
F(z_0,p) = -D(p)\,\frac{\partial f}{\partial z}\bigg|_{z=z_0} = -\frac{u_1 f_0(p)}{1-\exp(u_1 z_0/D(p))}\,\exp\!\left(\frac{u_1 z_0}{D(p)}\right)
$$

$F<0$ 表示粒子从系统逃逸；谱峰在 $D(p^*)/u_1 \simeq z_0$ 处 ——**逃逸谱在动量 $p^*$ 处集中**。

[FACT] **Sedov 阶段时间积分**（原文 Eq. 103、104）：

$$
d\epsilon = 4\pi p^2\,dp\cdot pc\cdot N_{\rm esc}(p) = \xi_{\rm esc}\,\tfrac{1}{2}\rho V_{\rm sh}^3\cdot 4\pi R_{\rm sh}^2\,dt \quad \text{(Eq. 103)}
$$

$$
N_{\rm esc}(p) \propto p^{-4}\,\xi_{\rm esc}(t) \quad \text{(Eq. 104)}
$$

**决定性结论**（原文原话）：\"this $p^{-4}$ has nothing to do with the standard result of the DSA in the test-particle regime, neither it depends on the detailed evolution in time of the maximum momentum. It solely depends on having assumed that particles escape the SNR during the adiabatic (self-similar) phase.\"

[FACT] 若 $\xi_{\rm esc}$ 随时间下降（现实），逃逸谱**硬于** $p^{-4}$。

[CRITIQUE] §6.1 的 $N_{\rm esc}(p)\propto p^{-4}$ 结果值得**强调**：它与注入谱斜率无关，只要求\"自相似阶段逃逸\"。这为理解\"地球处观测谱为何是 $E^{-2.7}$（比 $p^{-4}$ 软 0.7 个指数）\"提供自然路径——只要 $\xi_{\rm esc}$ 随时间下降即可。

---

### 6.2 Spectra

> **逃逸谱的硬软冲突**

[FACT] §6.2 引言（原文）：\"The spectrum of CRs injected by a SNR into the ISM during the few tens thousands years of its evolution is extremely complex to calculate since it requires the knowledge of the instantaneous spectrum of accelerated particles at any time, of the temporal evolution of the maximum energy, of the mechanism that leads to particle escape ... and the entire calculation depends on the type of SN and the environment in which it explodes.\"

[FACT] Caprioli et al. (2010) 典型 NLDSA 逃逸谱（Figure 10，$n_0=0.1\,\mathrm{cm^{-3}}$, $T_0=10^5\,\mathrm{K}$, $\xi_{\rm inj}=3.9$）：
- **实线**：总谱（逃逸+演化末逃逸之和）
- **虚线**：任一时刻的逃逸谱（位于 $R_{\rm sh}$ 的 $\epsilon=0.15$ 边界）
- **点划线**：演化末逃逸的粒子谱（最大能量更低）
- 最高能段呈**\"bump-like\"**结构，由硬逃逸通量主导

[FACT] **问题 (1)**：此谱**硬于**多数 SNR 的 $\gamma$ 射线观测（Caprioli 2011）。

[FACT] **问题 (2)**：若在地球处匹配观测谱，需 $D(E)\propto E^{0.7}$（Berezhko & Völk 2007），导致**CR 各向异性远超观测**（Ptuskin 2006；Blasi & Amato 2012b）。

[FACT] 作者**明确声明**（原文）：\"It is worth noticing that this discrepancy is not a consequence of the non-linear theory of DSA, in that the predictions of the test particle theory are also plagued by the same problem.\"

[FACT] **可能的软化机制（一）**：快速移动散射中心（Bell 1978a；Ptuskin et al. 2010；Caprioli 2012）。谱指数（原文 Eq. 105）：

$$
\alpha = \frac{\tilde{r}+2}{\tilde{r}-1}, \quad \tilde{r} = \frac{u_1 \pm v_{W,1}}{u_2 \pm v_{W,2}} \quad \text{(Eq. 105)}
$$

取决于上游波的螺旋度（helicity）——可能软化也可能硬化。

[FACT] **可能的软化机制（二）**：垂直激波几何（Schure & Bell 2013）：下游粒子返回概率降低 → 更陡谱。

[FACT] 作者**悲观总结**（原文）：\"It is rather disappointing that both these effects rely on details of the theory, and one is left to wander if observations may actually allow us to find the correct explanation for this rather serious discrepancy between theory and observational evidence.\"

[CRITIQUE] $D(E)\propto E^{0.7}$ 与各向异性冲突的论证在 Blasi 的**多篇后续论文**中被深化（Blasi & Amato 2012b），本文仅给出定性说明。

---

### 6.3 Gamma ray emission from isolated SNRs

> **孤立 SNR 的 $\gamma$ 射线发射**

[FACT] 章节定位（原文）：\"The purpose of this section is however not that of listing the individual SNRs that have been detected in gamma rays, but rather to choose a few cases of SNRs that are sufficiently isolated so as to be modeled as individual sources, and use them to illustrate the type of information that we can gather by comparing observations with theory.\"

[FACT] **RX J1713.7–3946**（核心坍缩型，首个 TeV SNR）：
- 首个明确探测到 TeV $\gamma$ 射线的 SNR（Aharonian et al. 2004, 2006, 2007），Fermi-LAT 在 GeV 段探测到（Abdo et al. 2011）
- **强子起源要求** ~160 $\mu$G 解释 X 射线边缘和 $\gamma$ 谱
- 若电子与质子同温，将预测强热 X 射线——**未探测到**
- **Ellison et al. (2010)** 结论：即使慢速 Coulomb 散射也可使电子升温至 >1 keV，激发氧线；未探测到 → 气体密度上限过严 → $\pi$ 产生不足 → **轻子起源**
- Fermi-LAT 硬 $\gamma$ 谱**与 $\pi$ 衰变不兼容**
- **ICS 解释的问题**（Morlino et al. 2009）：需要 IR 辐射场密度高 **25 倍**；需要 ~10 $\mu$G 弱场，与 X 射线边缘不兼容
- **Fukui et al. (2012)**：气体分布与 TeV 发射空间关联 → 支持强子起源
- 作者结论：RX J1713.7–3946 是\"环境复杂性主导\"的典型案例，需 CTA 进一步澄清

[FACT] **Tycho SNR**（Ia 型，1572 年，~3 kpc）：
- 圆对称形态（均匀 ISM）；全 X 射线窄边缘
- Fermi-LAT（Giordano et al. 2012，GeV）+ VERITAS（Acciari et al. 2011，TeV）$\gamma$ 谱**只与强子起源兼容**（Morlino & Caprioli 2012）
- X 射线边缘要求 $B \sim 300\,\mu$G → 加速质子最大能量 ~500 TeV
- **Berezhko et al. (2013)**：陡化归因于**环境效应**（两个组分：均匀介质 + 密集团块，后者 $p_{\max}$ 更低）
- **Morlino & Caprioli (2012)**：陡化归因于 **NLDSA + 波以 Alfven 速度运动**（放大场中的 Alfven 速度）——即 §6.2 中 $v_W\neq 0$ 机制的具体实现
- 作者**偏向** Morlino & Caprioli 的方案：\"the shape of the spectrum is related ... to the strength of the amplified magnetic field\"（Figure 11，多波段+X 射线形态）

[INTERPRETATION] Tycho vs RX J1713 的对比是本文的**\"双案例教学\"**：Tycho 支持强子 + 高 B + 有限 $p_{\max}$ + 磁化强度自洽耦合；RX J1713 暴露\"谱 vs 环境\"的复杂性。作者**明确立场**：偏向 Morlino & Caprioli 的解释——但承认\"one is left to wander\"。

[CRITIQUE] Berezhko 的方案需要 **ad hoc 密度涨落**（不可移植到其他 SNR）；Morlino & Caprioli 的方案与 X 射线边缘磁化强度**自洽耦合**——这是两种解释的**本质差异**。

---

### 6.4 SNRs near molecular clouds

> **邻近分子云的 SNR 与 $\pi^0$ 鼓包**

[FACT] 章节定位：分子云作为**强子相互作用的靶标**，用于检验 CR 质子加速——同时是研究 CR 在源附近传播和逃逸的\"实验室\"。

[FACT] **$\pi^0$ 鼓包的首次探测**：AGILE（Giuliani et al. 2011, 2010, 2011）与 Fermi-LAT（Abdo et al. 2010a; Ackermann et al. 2013）首次明确探测到 $\pi$ 鼓包，证实 $pp\to\pi^0\to 2\gamma$。典型对象：**IC 443、W44**（Figure 12）。

[FACT] **SNR-MC 的两类关联**：
1. **激波直接传播到分子云内**：$n\sim 10^3\,\mathrm{cm^{-3}}$、截面 $\sigma\sim 10^{-14}\,\mathrm{cm^2}$ → $\lambda\sim 10^{11}\,\mathrm{cm}$ ——SNR 激波撞击分子云时可能从**碰撞less 变为碰撞型**
2. **分子云被邻近 SNR 逃逸 CR 照亮**（在距离 $R_{\rm MC}$ 处）

[FACT] 第一类的证据：分子云加热来自**脉泽发射**（Hewitt et al. 2009），证实热分子气体存在。

[FACT] 第二类——**低能截止条件**（原文）：$[D(E)\cdot\tau_{\rm SNR}]^{1/2} \simeq R_{\rm MC}$；$\pi$ 产生截面 $\propto 1/E_\pi$ → 低能 $\gamma$ 谱 $\sim E_\gamma^{-1}$ 是低能截止的特征。

[FACT] **W28 的两云对比**（Giuliani et al. 2010）：**两个不同距离的云**表现出不同 CR 通量，较远的云低能截止出现在更高能量——**符合传播时延图像**。

[FACT] 源附近 <几十 pc 范围，源 CR 主导银河系 CR 通量（Blasi & Amato 2012a）→ 该范围内的 $D(E)$ 由**自散射**主导，可能**不同于**银河系平均值。

[FACT] 主导 B 场方向时，CR 扩散各向异性 → 在 $L_c\sim 50$–$100\,\mathrm{pc}$（相干尺度）以内沿 B 方向**拉长**（Nava & Gabici 2013；Giacinti et al. 2013）。

[FACT] 若 MC 位于 SNR 的磁通管上，可被 CR 照亮；否则**几乎无 $\gamma$ 发射**。

[FACT] Malkov et al. (2013) 给出源附近 CR 传播的自洽解（含平行/垂直扩散）。

[INTERPRETATION] §6.4 从 §6.1/§6.2 的\"理论逃逸机制\"进入**\"传播+传播方向\"**的实证：W28 的两云对比是**\"传播时延\"的第一手证据**，将逃逸问题从理论抽象拉入可观测物理。

**关键数值汇总**：

| 物理量 | 数值 |
|--------|------|
| $\nu_{\rm sync}$ (GeV $e^-$) | 3.7 MHz · B$_\mu$ · E$^2$(GeV) |
| X 射线边缘厚度 | $\sim 10^{-2}$ pc |
| Tycho 推断 B | ~300 $\mu$G |
| Tycho 加速 $p_{\max}$ | ~500 TeV |
| RX J1713 强子模型要求 B | ~160 $\mu$G |
| RX J1713 ICS 模型要求 B | ~10 $\mu$G |
| RX J1713 ICS 所需 IR 密度 | 预期值 25 倍 |
| $K_{ep}$（NLDSA 预言） | $\sim 10^{-3}$–$10^{-4}$ |
| $K_{ep}$（地球观测） | $\sim 10^{-2}$ |
| 磁相干尺度 $L_c$ | 50–100 pc |
| 分子云密度 $n$ | $10^3\,\mathrm{cm^{-3}}$ |
| 分子云碰撞长度 $\lambda$ | $10^{11}\,\mathrm{cm}$ |
| W28 两云相对 CR 通量差异 | 与距离成反相关 |

---

参见 `09_figures_tables.md`（Figure 10 逃逸谱、Figure 11 Tycho 多波段、Figure 12 IC 443/W44 $\pi$ 鼓包）。

---

## 元数据

```yaml
chapter: 6
title: Indirect evidence for CR acceleration in SNRs
pages: "Blasi 2013, §6 (pp. 47–58)"
subsections:
  - "6.1 Escape"
  - "6.2 Spectra"
  - "6.3 Gamma ray emission from isolated SNRs"
  - "6.4 SNRs near molecular clouds"
key_formulas:
  - "f(z,p) (Eq. 101, escape boundary)"
  - "F(z_0,p) = -u_1 f_0(p) / [1 - exp(u_1 z_0/D(p))] · exp(u_1 z_0/D(p)) (Eq. 102)"
  - "N_esc(p) ∝ p^-4 ξ_esc(t) (Eq. 104, Sedov phase)"
  - "α = (r̃+2)/(r̃-1), r̃ = (u_1 ± v_W,1)/(u_2 ± v_W,2) (Eq. 105)"
keywords:
  - CR escape
  - K_ep discrepancy
  - spectral concavity
  - RX J1713.7-3946
  - Tycho SNR
  - pion bump
  - molecular cloud
  - W28 low-energy cutoff
  - Blasi & Amato 2012b
references_internal:
  prev_chapter: 05_superbubble
  next_chapter: 07_h_alpha
```

**引用出处**：Blasi, "The Origin of Galactic Cosmic Rays," *arXiv:1311.7346* (2013), §6（pp. 47–58），全部公式编号（Eq. 101–105）沿用原文。