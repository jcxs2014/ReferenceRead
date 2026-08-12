# 98. Vocabulary — 学术词汇与术语

> 文献：0004_blasi-2013。本词汇表基于 `literature_analysis/` 中各分析文件提取，供中文母语读者辅助精读原文。

## A. 学术逻辑词（跨篇高频，标注逻辑功能）

> 这些词决定句子之间的逻辑关系，比专业术语更重要。下表中「单词」列给出中文逻辑词对应的**英文学术等价词**（精读英文原文时按此对应关系理解）；例句摘自本论文分析文本，均为本篇实际出现。

| 中文逻辑词 | 英文等价词 | 词性 | 逻辑功能 | 原文/分析例句 | 逻辑说明 |
|-----------|-----------|------|----------|---------------|----------|
| 因此 | 因此 | therefore / consequently | adv. | "- [FACT] 作者用 "escape time normalized to B/C at E* makes J(E) independent of H" 强调了一个**重要的不敏感性**：简单扩散模型里 CR 通量和 grammage 都按 H/D(E) 标度，因此 halo 大小可以被消去。 - [INTERPRETATION] ξ_CR ≈ 10% 的"10% 定律"是 SNR 范式的**能量锚点**，但并非直接观测——它是推导" | 因果 |
| 虽然 | 虽然 | although / though | conj. | "- **潜在不一致性**：Eq. 74（E_γ,max 与 B 无关）只在 Bohm 假设下成立，作者明确指出"not a general result"——但后文多次使用 Bohm 假设进行能量估计。 - **信息缺失**：磁化放大的**时间演化**（随 SNR 演化）未讨论；不同 SNR 演化阶段（自由膨胀期 vs Sedov 期 vs 压强驱动期）对应的磁化状态可能不同。 - [CRITIQUE] §4.4 结尾的批判总结写得相当" | 让步 |
| 即使 | 即使 | even if | conj. | "- [FACT] **中性回流（neutral return flux）**（Blasi et al. 2012）：下游电荷交换产生的热原子以高速运动，部分可穿越激波回到上游，在上游几倍电荷交换/电离路径长度内沉积能量动量。 - [FACT] 结果：上游等离子体被加热并减速 → **激波 Mach 数降低** → 压缩比 r<4（即使是强激波）。 - [FACT] 中性回流在 V_sh ≲ 3000 km/s 时重要；对更快激波，电荷交" | 让步 |
| 而 | 而 | whereas / while / and | conj. | "- [FACT] NLDSA 计算的逃逸谱（Caprioli et al. 2010，Fig. 10）在最高能段呈**"bump-like"** 结构，由硬逃逸通量主导。 - [FACT] 问题 (1)：硬于多数 SNR 的 γ 射线观测（Caprioli 2011）。 - [FACT] 问题 (2)：若在地球处匹配观测谱，需 D(E) ∝ E^0.7，而此能量依赖导致 **CR 各向异性远超观测**（Ptuskin 2006；Blas" | 对比/转折 |
| 同时 | 同时 | meanwhile / simultaneously | adv. | "- **test-particle DSA 的"谱与 D 无关"**思路：在理论建模中利用对称性/不变量简化计算。 - **NLDSA 的三种数值方法**（有限差分 / Monte Carlo / 半解析）各有适用场景——半解析适合与流体耦合，Monte Carlo 适合处理 p_max 附近的非扩散效应。 - **Balmer 线诊断**：一种**用传统光学观测约束高能物理**的范例。 - **多波段自洽拟合**（Morlino &" | 递进/顺序 |
| 进而 | 进而 | furthermore / subsequently | adv. | "- **test-particle DSA**（Skilling 1975a 传输方程）：给出 α=3r/(r−1)→4 的幂律谱，但**与 D 无关、不能给出 p_max**。 - **非线性 DSA**（Malkov & Drury 2001 框架）：自洽求解加速粒子对激波的反馈（precursor + subshock），给出**凹谱**预言。 - **等离子体不稳定性理论**：系统比较共振 streaming、Bell 非共振、" | 递进 |
| 特别是 | 特别是 | in particular / specifically | phrase | "无独立新公式。结论引用 §3–§6 的公式（特别是 Eq. 105 移动散射中心、§3.4 最大能量估计）。" | 举例 |
| 最终 | 最终 | eventually | adv. | "- 从**抽象的逃逸机制**（§6.1）→ 到**逃逸谱的积分形状**（§6.2）→ 到**具体 SNR 的多波段检验**（§6.3，两个案例）→ 到**源-MC 复合系统的传播**（§6.4）。 - [INTERPRETATION] 每个小节都在**测试 SNR 范式的一条腿**：§6.1 测试"谱的形状"，§6.2 测试"谱的硬软"，§6.3 测试"加速源-辐射源的耦合"，§6.4 测试"π 产生通道的确凿性"。 - [INTERP" | 顺序 |
| 由于 | 由于 | owing to / due to / because of | prep. | "- [FACT] 单次循环的能量增益（Bell 1978a）： $$\left\langle\frac{E'_1 - E_1}{E_1}\right\rangle_{\mu_1,\mu_2} = \frac{4}{3}\beta \quad (44)$$ 标度为 β¹ → "first order Fermi"。 - [FACT] 加速时间（Drury 1983；Lagage & Cesarsky 1983a,b）： $$\tau_{\" | 因果 |
| 即 | 即 | namely / i.e. | adv. | "- [FACT] **中性回流（neutral return flux）**（Blasi et al. 2012）：下游电荷交换产生的热原子以高速运动，部分可穿越激波回到上游，在上游几倍电荷交换/电离路径长度内沉积能量动量。 - [FACT] 结果：上游等离子体被加热并减速 → **激波 Mach 数降低** → 压缩比 r<4（即使是强激波）。 - [FACT] 中性回流在 V_sh ≲ 3000 km/s 时重要；对更快激波，电荷交" | 举例 |
| 据 | 据 | according to / based on | prep. | "- 从 Hess（1912）的宇宙线发现与 Rossi（1964）书的 50 周年回顾，引出"一个世纪后仍未完全解决"的主题。 - 给出银河系宇宙线的基本图像：质子为主（~90%）、氦核（~10%），能量密度约 1 eV/cm³。 - **全粒子能谱**：低能端 (~30 GeV 以下) 被太阳调制；膝点 knee 在 E_K = 3 × 10¹⁵ eV 处从 γ ≈ 2.7 变到 ≈ 3.1；膝点之上成分趋向重核主导，最高至 ~10¹" | 因果 |

*共 11 个逻辑词，均在本篇分析文本中实际出现。*

## B. 领域术语（本篇特有）

| 术语（中文/英文） | 中文释义 | 出现次数 | 首次出现章节 |
|------------------|----------|----------|-------------|
| SNR | 超新星遗迹 | 148 | §00 |
| 激波 | 激波 | 61 | §00 |
| 源 | （宇宙线）源 | 50 | §00 |
| 逃逸 | 逃逸 | 43 | §00 |
| γ 射线 | γ 射线 | 35 | §00 |
| DSA | 扩散激波加速 | 34 | §00 |
| 各向异性 | 各向异性 | 23 | §00 |
| 约束 | 约束/限制 | 22 | §01 |
| 银河系 | 银河系的 | 19 | §00 |
| 模型 | 模型 | 19 | §00 |
| 传播 | 传播 | 17 | §01 |
| 强子 | 强子 | 16 | §06 |
| SN | 超新星 | 15 | §02 |
| 电离 | 电离 | 15 | §01 |
| shock | 激波 | 13 | §00 |
| ISM | 星际介质 | 12 | §02 |
| 同步辐射 | 同步辐射 | 11 | §04 |
| magnetic field | 磁场 | 9 | §00 |
| 扩散系数 | 扩散系数 | 9 | §02 |
| 宇宙线 | 宇宙线 | 8 | §00 |
| 能谱 | 能谱 | 8 | §00 |
| 等离子体 | 等离子体 | 8 | §00 |
| flux | 通量 | 7 | §00 |
| escape | 逃逸 | 6 | §00 |
| Monte Carlo | 蒙特卡罗模拟 | 6 | §04 |
| 衰变 | 衰变 | 5 | §00 |
| 湍流 | 湍流 | 5 | §05 |
| UHECR | 超高能宇宙线 | 4 | §08 |
| cosmic ray | 宇宙线 | 4 | §00 |
| 暗物质 | 暗物质 | 4 | §01 |
| 截面 | 截面 | 4 | §04 |
| 河外 | 河外的 | 4 | §08 |
| pion | π 介子 | 3 | §00 |
| proton | 质子 | 3 | §01 |
| gamma-ray | γ 射线 | 3 | §00 |
| 阈值 | 阈值 | 3 | §01 |
| nucleon | 核子 | 2 | §02 |
| gamma ray | γ 射线 | 2 | §01 |
| diffusion coefficient | 扩散系数 | 2 | §03 |
| 超新星 | 超新星 | 2 | §00 |
| 超新星遗迹 | 超新星遗迹 | 2 | §00 |
| 级联 | 级联 | 2 | §09 |
| 核子 | 核子 | 2 | §09 |
| propagation | 传播 | 1 | §08 |
| positron | 正电子 | 1 | §01 |
| power law | 幂律 | 1 | §03 |
| confinement | 约束/束缚 | 1 | §04 |
| plasma | 等离子体 | 1 | §01 |
| turbulence | 湍流 | 1 | §08 |
| 脉冲星 | 脉冲星 | 1 | §01 |
| 轫致辐射 | 轫致辐射 | 1 | §09 |
| 各向同性 | 各向同性 | 1 | §09 |
| 伽马射线 | γ 射线 | 1 | §05 |
| 轻子 | 轻子 | 1 | §06 |
| 功率谱 | 功率谱 | 1 | §04 |

*共 55 个领域术语（按出现频次降序排列；仅列出在本文分析文本中实际出现者）。*

## C. 长难句摘录

### C1.

> - [FACT] "The problem of the origin of cosmic rays is a complex one: what we observe at the Earth results from the convolution of acceleration inside sources, escape from the sources and propagation in the Galaxy."
- [FACT] **证据三支柱**：
  1. γ 射线："prove that SNRs accelerate particles up to at least 50–500 TeV"（Aharonian 2013；Brandt et al. 2013a,b；Holder 2012）；Tycho 的 γ 射线最可能是 π⁰ 衰变。
  2. X 射线边缘："magnetic field amplification is taking place at SNR shocks, in virtually all young SNRs"（Völk et al. 2005；Vink 2012），场强 ~几百 µG，最可能由加速粒子诱导的不稳定性产生。
  3. Balmer 线异常宽度："evidence for anomalous width of t…

**结构复杂度**：约 530 词（中文 259 字 + 英文 271 词）；30 处停顿（逗号/分号/冒号）；多分句嵌套。

### C2.

> - [FACT] X 射线窄边缘观测：电子同步辐射给出 E_e ≈ 8(E_γ/100 eV)^½ · B⁻¹/²_100 TeV。
- [FACT] Bohm 极限下加速时间（Eq. 71）：τ_acc ≈ 3.3×10⁷ E_TeV · B⁻¹_100 · V⁻²_sh,8 s。
- [FACT] 同步辐射损失时间（Eq. 72）：τ_syn = 4×10¹⁰ B⁻²_100 · E⁻¹_TeV s。
- [FACT] 最大电子能量（Eq. 73）：E_e,max ≈ 34 B⁻¹/²_100 · V_sh,8 TeV。
- [FACT] 最大光子能量（Eq. 74）：E_γ,max ≈ 1.7 V²_sh,8 keV —— **与 B 无关**（Bohm 假设下）。
- [FACT] 特征宽度（Eq. 75）：√(D·τ_syn) ≈ 3.7×10⁻² B⁻³/²_100 pc → 观测到的 ~10⁻² pc 窄边缘需要 B~几百 µG。
- [FACT] 磁化放大两种起源：(i) 激波波纹（shock corrugation，Giacalone & Jokipii 2007，Sano 2012）——下游；(ii) CR streaming 不稳定性——**上游**（"qualitatively, extremely important difference"）。
…

**结构复杂度**：约 478 词（中文 296 字 + 英文 182 词）；40 处停顿（逗号/分号/冒号）；多分句嵌套。

### C3.

> - [FACT] "In 1962 Bruno Rossi finalized the writing of his book Cosmic Rays ... the field of CR research had become a complex combination of several fields, from Astronomy to Plasma Physics and Particle Physics."
- [FACT] "Cosmic rays are mainly charged particles that contribute an energy density in the Galaxy of about 1 eV cm⁻³. They are mainly protons ... with about 10% fraction of helium nuclei and smaller abundances of heavier elements."
- [FACT] The knee: "the prominent steepening of the spectrum at energy E_K = 3 × 10¹⁵ eV is named the knee: at this point the spectral slope of the d…

**结构复杂度**：约 364 词（中文 77 字 + 英文 287 词）；11 处停顿（逗号/分号/冒号）；多分句嵌套。

### C4.

> - [FACT] AGILE（Giuliani et al. 2011, 2010）与 Fermi-LAT（Ackermann et al. 2013）**首次明确探测到 π 鼓包**（pion bump），证实 pp→π⁰→2γ。
- [FACT] 典型对象：IC 443、W44（Fig. 12）。
- [FACT] 分子云内密度 n=10³ cm⁻³、几何截面 σ~10⁻¹⁴ cm² → λ~10¹¹ cm —— **SNR 激波撞击分子云时可能从碰撞less 变为碰撞型**。
- [FACT] 分子云加热证据来自**脉泽发射**（Hewitt et al. 2009）。
- [FACT] 逃逸 CR 到达分子云的**低能截止**条件：[D(E)·τ_SNR]^½ ≃ R_MC。
- [FACT] π 产生截面 ~ 1/E_π → 低能 γ 谱 ~ E_γ⁻¹ 是低能截止的特征。
- [FACT] W28（Giuliani et al. 2010）：**两个不同距离的云**表现出不同 CR 通量，较远的云低能截止出现在更高能量——**符合传播时延图像**。
- [FACT] CR 源附近 <几十 pc 范围内，源 CR 主导银河系 CR 通量（Blasi & Amato 2012a）→ 该范围内的 D(E) 由自散射主导，可能**不同于银河系平均值**。
- [FAC…

**结构复杂度**：约 283 词（中文 223 字 + 英文 60 词）；11 处停顿（逗号/分号/冒号）；多分句嵌套。

### C5.

> - [FACT] **中性回流（neutral return flux）**（Blasi et al. 2012）：下游电荷交换产生的热原子以高速运动，部分可穿越激波回到上游，在上游几倍电荷交换/电离路径长度内沉积能量动量。
- [FACT] 结果：上游等离子体被加热并减速 → **激波 Mach 数降低** → 压缩比 r<4（即使是强激波）。
- [FACT] 中性回流在 V_sh ≲ 3000 km/s 时重要；对更快激波，电荷交换截面急剧下降，主要变为电离。
- [FACT] 后果：低能粒子（扩散长度 < 电荷交换/电离路径长度）的谱**显著变软**；高能粒子不受影响。
- [FACT] 若激波速度 ~1000 km/s，谱可变得极陡，粒子能量含量被注入能量而非粒子质量主导 ——"for all practical purposes, corresponds to not having particle acceleration."
- [FACT] **中间 Balmer 线**：在激波前 ~几倍碰撞长度内的离子被中性回流预热，与之电荷交换产生的 Hα 线宽 ~100–300 km/s。
- [FACT] 观测证据：Ghavamian et al. (2000) 可能有初步观测到中间线。

**结构复杂度**：约 257 词（中文 225 字 + 英文 32 词）；14 处停顿（逗号/分号/冒号）；多分句嵌套。
**关键连接词**：即使, 而, 即

