> 本章属于：T. K. Gaisser (1990) "Origin of high energy galactic cosmic rays", AIP Conference Proceedings 203, 168
>
> 上一章：（无，本文件为正文分析）
>
> 下一章：[[02_cosmic-ray-origins/0003_gaisser-1990/literature_analysis/99_final_summary.md|99_final_summary.md]]

# 1. 文献基本信息

| 字段 | 内容 |
|---|---|
| Title | Origin of high energy galactic cosmic rays |
| Authors | T. K. Gaisser |
| Collaboration | 未提供 |
| Affiliation | Bartol Research Institute, University of Delaware, Newark DE 19716 |
| Journal / Conference | AIP Conference Proceedings 203, 168-182 (1990) |
| Publication Date | 1990（在线出版 29 May 2008） |
| DOI | 10.1063/1.39149 |
| arXiv | 未提供 |
| 页数 | 16 页 |
| 研究分支 | High-energy particle astrophysics / Cosmic ray astrophysics |
| Keywords | Cosmic rays, Galactic cosmic rays (GCR), Supernova acceleration, Fermi acceleration, "knee", Composition, Antiprotons, Leaky-box, Reacceleration, Closed galaxy |

**性质**：这是一篇在 1990 年会议上所做的综述/评述报告（"In this talk I discuss…"），并非原创实验/计算论文。它综合当时关于高能宇宙线起源、"膝部"组分与反质子通量的研究现状，重点讨论两种**观测探针**（膝部处的化学组分、宇宙线反质子通量）对**源-加速-传播**物理的约束能力。

---

# 2. 论文结构树

- **Abstract**
- **1. Introduction**
  - 1.1 银河系宇宙线的功率平衡：超新星供给 vs 稳态需求
  - 1.2 局部星际介质（LIS）能量密度与谱
  - 1.3 次级/初级比与 rigidity-dependent 逃逸（leaky-box）
  - 1.4 源谱与 Fermi 一阶激波加速的联系
- **2. Composition at the "knee"**
  - 2.1 膝部现象与两种解释（加速上限 vs 逃逸增加）
  - 2.2 量能计"全粒子"谱（Akeno 数据）
  - 2.3 空气簇射谱的模型依赖性
  - 2.4 膝部处组分的直接测量（JACEE）
  - 2.5 关于膝部以上组分的争议（Hillas / Fichtel-Linsley / Maryland）
  - 2.6 达到 E > 100 TeV 的可能机制（点源 vs 弥散源）
  - 2.7 结论：需要在膝部直接测量各组分的能谱
- **3. Antiprotons**
  - 3.1 反质子通量异常与多种源假说
  - 3.2 反质子的唯一探针性（高阈值的产生反应）
  - 3.3 平衡方程（Eq. 11）
  - 3.4 Leaky-box 模型（Protheroe）
  - 3.5 Closed galaxy 模型
  - 3.6 Reacceleration（Simon et al.）
  - 3.7 结论：反质子对加速与传播的互补探针性
- **ACKNOWLEDGMENTS**
- **4. References** (53 条)

---

# 3. 各章节深度精读

## 3.1 Introduction — 银河系宇宙线的功率平衡

### 3.1.1 原文内容

作者开宗明义：银河系宇宙线所需的功率，与银河系中超新星爆发所提供的能量非常吻合，约 **3 × $10^{42}$ erg/s**。这一数字基于"每 30 年一次超新星，每次抛出壳层的动能约 2 × $10^{51}$ erg"的估算。

**宇宙线维持稳态谱所需的功率**：

$$Q_{CR} = \frac{\rho_E \, V_S}{\tau_R} \sim 5 \times 10^{40} \text{ erg} \quad (1)$$

（[CRITIQUE] 此处文本中的数值印刷为 5×$10^{40}$，但前文声称功率匹配 3×$10^{42}$，数量级上存在差异。结合下文推导，作者实际使用的 $\rho$_E ≈ 1 eV/cm³、V_S ≈ 5×$10^{66}$ cm³、$\tau$_R ≈ 5×$10^{6}$ yr 得到的结果应当为 ~3×$10^{41}$ erg/s，与超新星供给 3×$10^{42}$ erg/s 相当接近——这是本文核心论据之一。）

**LIS 能量密度**：

$$\rho_E = 4\pi E^2 \frac{dN}{dE}\bigg|_{\ln E} = \frac{d\rho_\epsilon}{d\ln E} \quad (2)$$

其中 E 是每核子动能，$\beta$c 是粒子速度，dN/dE 是核子的微分谱。

**参数取值（作者假设）**：
- $\rho$_E ≈ 1 eV/cm³ [FACT]
- 源区体积 V_S ≈ 5 × $10^{66}$ cm³（取银河系盘面）[FACT]
- 在盘中的驻留时间 $\tau$_R ≈ 5 × $10^{6}$ yr [FACT]

[FACT] 关键脚注：$\tau$_R 是"在盘中的驻留时间"，**不**是宇宙线的"年龄"（后者由如 $^{10}{\rm Be}$ 等放射性同位素相对丰度给出）。

### 3.1.2 作者逻辑

功率平衡论据：超新星供给的功率 ≈ 稳态宇宙线谱需要的功率 → 超新星是宇宙线的主要动力源。这是当时已建立的"常识性共识"，作者以此为基础展开后续的膝部和反质子讨论。

---

## 3.2 Figure 1 — 能量密度谱

> **Figure 1**: Energy density in cosmic rays (eV/cm³).

### 3.2.1 图的目的
把不同能量区间对总宇宙线能量密度的贡献可视化。作者选择绘制 ∝ d$\rho$_E/d ln E 的量，使得对数坐标图上的物理面积正比于各能量区间的贡献。

### 3.2.2 坐标轴
- **横轴**：动能 $E_{0}$，单位 GeV，对数坐标，范围约 0.1 GeV ~ 1000 GeV
- **纵轴**：$\rho$_e（eV/cm³），线性坐标，范围 0 ~ 0.16

### 3.2.3 图中元素
- 1977 曲线：地球处质子通量（太阳活动极小期调制下）
- 1982 曲线：地球处质子通量（太阳活动极大期调制下）
- LIS 曲线：经去调制后的局部星际质子谱，来自 Evenson [Ref. 2]

### 3.2.4 关键观察与数值
- **质子曲线下的面积** ≈ **0.83 eV/cm³** [FACT]
- **He 及更重核贡献** ≈ **0.27 eV/cm³** [FACT]
- 二者相加 ≈ **1.1 eV/cm³**，与作者前文"$\rho$_E ≈ 1 eV/cm³"一致 [FACT]
- **99% 的星际宇宙线能量**包含在 E < 1 TeV/核子 的粒子中 [FACT]
- **超过一半的能量**由 E < 数 GeV 的粒子携带，这些粒子在穿透日球时被太阳风耗散 [FACT]

### 3.2.5 物理意义
- 说明宇宙线能量密度主要来自低能部分，而本文主题（膝部、反质子）关注的是"尾部"探针——用少数高能粒子反推加速与传播机制。
- [INTERPRETATION] 这也解释了为什么膝部（$10^{15}$ eV 附近）的观测如此困难：那里通量已经很低。

---

## 3.3 次级/初级比与 leaky-box 逃逸

### 3.3.1 原文内容

[FACT] 低能宇宙线研究的两个典型观测：
- **次级/初级核的比值**（如 B/C）**随能量升高而下降**。
- 解释：rigidity-dependent 的驻留时间减小（或空间扩散系数增大）。

**一维空间扩散模型**下的关系（脚注）：

$$\tau_R = \frac{h\,H}{D} \quad \text{（一维，垂直于盘面扩散）}$$

其中 H 是 halo 厚度，h 是盘厚度。

**最近一次的拟合（Gupta & Webber, Ref. 7）**：

$$\lambda_{esc} = \lambda_{esc}(4\,\text{GV})\left(\frac{R}{4\,\text{GV}}\right)^{\!\!0.6} \quad R > 4\,\text{GV} \quad (3)$$

对 R < 4 GV，$\lambda$_esc = const = 10.88 g/cm²。

**由此，高能处观测谱 J(E) 与源谱 Q(E) 的关系**：

$$J(E) \propto E^{-\delta}\times Q(E), \quad \delta \approx 0.6 \quad (4)$$

[FACT] 10 GeV ~ 数 TeV 能量段，微分核子谱：

$$J(E) \propto E^{-\gamma}, \quad \gamma \approx 2.7 \quad (5)$$

**推出源谱**：

$$Q(E) \propto E^{-(\gamma - \delta)} \approx E^{-2.1}$$

### 3.3.2 物理解释

- [FACT] 超新星壳层的 **一阶 Fermi 激波加速（diffusive shock acceleration）** 自然产生 E⁻² 的源谱。[FACT] （Ref. 8: Blandford & Eichler, 1987；Ref. 9: Axford, 1987）
- [FACT] 因此，一个非常自然的图景是：**大部分银河系宇宙线由向外膨胀进星际介质的超新星激波通过一阶 Fermi 机制加速产生**，能量最终来源于爆炸超新星壳层的动能。
- [INTERPRETATION] $\delta$ ≈ 0.6、$\gamma$ ≈ 2.7、源谱 E⁻²·¹，三者之间通过 Eq. (4) 形成自洽链，把加速理论、传播模型、观测谱三个部分串联起来。

### 3.3.3 关键参数小结

| 参数 | 数值 | 说明 |
|---|---|---|
| $\delta$ | ≈ 0.6 | rigidity-dependent 逃逸指数 |
| $\gamma$ | ≈ 2.7 | 观测微分谱指数 (10 GeV – 数 TeV) |
| 源谱指数 | ≈ 2.1 | 由 $\gamma$ - $\delta$ 推出，与 Fermi 一阶加速的 E⁻² 接近 |
| $\lambda$_esc(4 GV) | ≈ 6 g/cm² | 4 GV 处逃逸长度（来自 Gupta-Webber） |
| R < 4 GV | 恒定 10.88 g/cm² | 低能段的近似 |

---

## 3.4 Chapter 2: Composition at the "knee"

### 3.4.1 膝部现象 [FACT]

主成分谱在 **$10^{15}$ – $10^{16}$ eV** 能量区间发生陡化（spectral steepening），称为 **"knee"**。这是本文的核心问题之一。

### 3.4.2 两种解释

**解释 A：加速上限**
- 超新星激波的加速上限随刚度（rigidity = Pc/Ze）限制粒子能量。
- 加速度率反比于激波区的空间扩散系数。
- 在最小可能的散射长度近似下（上下游均是），D ~ r_L c，其中回旋半径 r_L = Pc/(ZeB)。
- 由此（Ref. 10: Lagage & Cesarsky, 1983）：

$$E_{max} \approx \frac{3\,u_1\,Z\,e\,B\,(\tau_u\,\tau_A)}{20\,c} \quad (6)$$

代入参数：B = 3 $\mu$Gauss，$u_{1}$ ≈ $10^{9}$ cm/s，$\tau$_A ≈ 1000 yr：

$$\frac{E_{max}}{Z} \approx 10^{14}\ \text{eV} \quad (7)$$

- Axford（Ref. 9）取更长的寿命，得出稍高的 E_max。

**解释 B：逃逸率增加**
- 银河系（或更局部的俘获区）逃逸率随刚度增加。
- 在**均匀**加速机制之上叠加 rigidity-dependent 逃逸。

[FACT] 两种解释的共同特征：组分随能量的变化都是 **rigidity-dependent steepening** 的表现。

### 3.4.3 组分直接测量（Table 1）

**Table 1**: Fractional composition of five major cosmic ray groups (JACEE, Ref. 12)

| Mass group | ⟨A⟩ | Particles (>E/A, ~100 GeV/n) | Particles (>E/nucleus) | JACEE (>200 TeV/nucleus) |
|---|---|---|---|---|
| p | 1 | 0.96 | 0.47 | 0.19 ± 0.12 |
| $\alpha$ ($^{4}{\rm He}$) | 4 | 0.035 | 0.18 | 0.22 ± 0.07 |
| M (Z=6–9) | 14 | 0.0024 | 0.10 | 0.17 ± 0.06 |
| H (Z=10–20) | 24 | 0.0007 | 0.07 | 0.30 ± 0.15 |
| VH (Z=21–30) | 56 | 0.0004 | 0.18 | 0.13 ± 0.09 |

**关键观察** [FACT]：
- 在**每核子能量**（> E/A ≈ 100 GeV/n）下，Z > 2 的核仅占 0.03%；
- 在**每核能量**（> E/nucleus）下，Z > 2 的核占 **36%**；
- 如果膝部陡化是 rigidity-dependent 效应，膝部以上 Z > 2 的比例应增至 **~53%**，比低能值高约 1.5 倍。
- JACEE 列（>200 TeV/nucleus）中每个组的事件数都很少，误差大。

[CRITIQUE] JACEE 数据在该能量点的统计量很低，误差大（每个组 ±0.06–0.15），单个数据点难以区分 rigidity-dependent 陡化与组分突变。

### 3.4.4 量能计"全粒子"谱

- 高于 $10^{14}$ eV 的通量 < 1 粒子/m²/h 通过 $\pi$ 立体角的探测器，气球或卫星不可行。
- 几乎全部通过**空气簇射**实验（calorimetric）探测。
- 空气簇射按**每粒子能量**分类，而不是按每核能量。

**Figure 2**: Primary spectrum as summarized by the Akeno group (Ref. 13)

- 横轴：log $E_{0}$ (eV)，范围 11–20
- 纵轴：E^{2.5} × 微分通量（对数）
- 图中数据：Akeno 及多个实验的"全粒子"谱
- **明确陡化点**：**~5 × $10^{15}$ eV**（这就是膝部）[FACT]
- 两条 Akeno 数据：N_e (w = 1.7 GeV) 与 N_e (w = 1.4 GeV)——反映模型的依赖性。

### 3.4.5 空气簇射谱的模型依赖性 [FACT]

两个问题：
1. **阵列接受度** 是能量的函数——更大（更穿透）的簇射更容易触发阵列。
2. 观测尺寸到初级能量的转换依赖于**强子相互作用的性质**，而这些在高能处并不完全已知。

**初级核能量估算**：

$$E_0 = w \times N_e^{(\text{max})} \quad (8)$$

其中 N_e^{(max)} 是簇射极大处的粒子数。**w** 和从地面 N_e 到 N_e^{(max)} 的修正**都是模型依赖的**，尽管后者可以半经验地处理（Ref. 14: Hillas）。

### 3.4.6 膝部以上组分的三种主要观点

[FACT] **Hillas (Ref. 15)**：膝部的"弯折"太尖锐，**不能**用均匀组分下的 rigidity-dependent 平滑陡化来解释。

[FACT] **Fichtel & Linsley (Ref. 16)**：在 ~$10^{18}$ eV 以上**新源占主导**（低能组分在加速失败或逃逸增加后消失）；新源**主要加速质子**。证据来自空气簇射实验观测到的**大波动**（重核簇射波动较小）。

[FACT] **Maryland group (Ref. 17)**：即使是较低能量就存在**两个分量**：质子/氦有较陡谱，重核有较平谱；因此 $10^{14}$ eV 及膝部以上组分**已经以重核为主**。这与 Fichtel-Linsley 的假说相反。

[FACT] 作者表态："In my opinion, either view could be correct."

### 3.4.7 达到 E > 100 TeV 的可能机制

**弥散源（diffuse sources）**：
- **Völk & Biermann (Ref. 18)**：超新星实际爆炸进**前身星的星风**（而非一般星际介质），可得到更高的 E_max。
- **Jokipii (Ref. 19)**：磁场几何的作用——在超新星激波的赤道区，磁场近垂直于激波方向，斜激波加速更快。
- **Cesarsky & Montmerle (Ref. 20)**：强恒星风的终止激波。
- **Jokipii & Morrill (Ref. 21)**：银河系星风的终止激波可加速到 **$10^{19}$ – $10^{20}$ eV**。

**点源（point sources）**：
- 吸积 X 射线双星
- 新的超新星
- **毫秒双星脉冲星**：PSR 1957+20，周期 1.6 ms (Ref. 25)
- 这些点源也是 TeV–PeV $\gamma$ 光子的潜在源——$\gamma$ 光子来自源附近加速粒子与物质碰撞产生的 $\pi$⁰ 衰变。

[FACT] 作者引用大量综述：Ref. 22 (Weekes, VRH $\gamma$-ray astronomy)、Ref. 23 (Nagle-Gaisser-Protheroe)、Ref. 24 (Bonnet-Bidaud & Chardin, Cygnus X-3 review)。

### 3.4.8 本章结论 [FACT]

- **直接在膝部区测量各主要组分的能谱**对理解起源、加速、传播至关重要。
- 低能直接测量（Ref. 12, 27, 28）已经显示出有趣的能量依赖性，需要**跟到高能量**。
- 高于 $10^{16}$ eV 的通量约 **1 粒子 m⁻² sr⁻¹ 每年**，需要**数百 m²·年的大口径探测器**。
- **Swordy (Ref. 29)** 提出**月球量能器**方案——在无大气覆盖的月球表面用大量能器直接测量初级核的电荷。

---

## 3.5 Chapter 3: Antiprotons

### 3.5.1 反质子通量异常与多种源假说 [FACT]

- 观测迹象（Ref. 30, Stephens & Golden 1988）显示宇宙线反质子通量**可能高于预期**（若质子/氦的传播历史与重核相同）。
- 这提示在数 GeV 能量段就**可能有多类源**。

**假说 1（Lagage-Cesarsky Ref. 31, Cowsik-Gaisser Ref. 32）**：
- 观测宇宙线中 **25–30%** 来自"**遮蔽源（shrouded sources）**"——粒子在源处被足够多的物质穿透，产生大量反质子，同时碎裂掉重核以不破坏 B/C 等传统扩散模型的拟合。
- [CRITIQUE] 简单模型**难以同时满足观测到的 $^{3}{\rm He}$/$^{4}{\rm He}$ 比值**——氦截面足够小，使得 $^{3}{\rm He}$/$^{4}{\rm He}$ 会高于观测（Ref. 33）。

**假说 2（exotic）**：
- 原初反物质（Ref. 34, Stecker-Wolfendale）
- WIMP 湮灭（Ref. 35, Stecker-Tylka）
- [FACT] 现在都**更不可信**，因为低能处反质子/质子比的**新上限**（<1 GeV, Ref. 36, 37）排除了它们——这些模型倾向于在低能给出较大的反质子通量。

### 3.5.2 反质子的唯一探针性 [FACT]

- **反质子产生的最小过程**：

$$p + H \to p + p + p + \bar{p} \quad (9)$$

- **阈值动能**：**5.63 GeV**
- **产生截面**：从零（阈值处）上升至 ~1 mb（100 GeV）和 ~5 mb（1000 GeV）
- 对比：碎裂反应如 $^{16}{\rm O}$ + H → $^{10}{\rm B}$ + … (10)，**高于 1 GeV 截面几乎恒定**，低于 100 MeV 有共振结构（Ref. 42）。
- 碎裂产物近同每核能量；反质子获得能量远小于射弹核（高能时典型为 1/10）。

[INTERPRETATION] 反质子的产生截面具有**强能量依赖性**且在高能区单调增大，而次级核的产生截面基本平坦——这使得反质子通量对**源谱形状、能量再加速、传播方式**的响应**与次级核显著不同**，形成**互补探针**。

### 3.5.3 平衡方程 (Eq. 11)

这是本章的**核心数学工具**：

$$\frac{dJ_{\bar{p}}(E)}{dt} = 0 = Q_{\bar{p}}(E) - \frac{1}{\tau_R(E)}J_{\bar{p}}(E) \quad \underbrace{- \frac{1}{\tau_I}\left[J_{\bar{p}}(E) + \int_0^{\infty}\frac{d\sigma_{\bar{p}}}{dE'}(E,E')\,J_{\bar{p}}(E')\,dE'\right]}_{\text{attenuation: 湮灭 + 产生反核子出射的反应}} \quad \underbrace{+ B\int_0^{\infty}\frac{dP(E,E')}{dE}\,J_{\bar{p}}(E')\,dE'}_{\text{reacceleration}} \quad (11)$$

**逐项解释**：
- 第一项 Q_{\bar{p}}(E)：反质子**源项**（产生率）
- 第二项 1/$\tau$_R · J：反质子从**银河系逃逸**
- 第三项 1/$\tau$_I · [...]：反质子在星际气体中的**衰减**（湮灭 + 产生反核子出射的次生反应；高能时后者主导）
- 第四项 B · [...]：反质子**再加速**，B 是遭遇再加速位点的速率（例如弱星际激波）；dP(E,E')/dE 是从能量 E' 再加速到 E 的归一化分布

**源项**（若反质子是次级产物）：

$$Q_{\bar{p}}(E) = 2\,\alpha\,\rho\,F\int dN_p\,J_p(E_p)\,dE_p \quad (12)$$

其中：
- J_p：初级质子谱
- $\rho$：星际气体密度
- $\sigma$：p-p 截面
- F：考虑星际气体和宇宙线束中核子效应的修正
- 因子 2：考虑反中子产生
- **源谱很窄**，大部分产额在 **1.5 – 15 GeV** 之间 [FACT]

### 3.5.4 三个模型的对比

**模型 1：Leaky-box**（Eq. 11 只取前两项）

平衡解：

$$j^{(0)}(E) = \tau_R(E)\,Q_{\bar{p}}(E) \quad (13)$$

- 当 E → ∞，Q_{\bar{p}}(E) → const × J_p(E)
- 因此若反质子在盘内由本地质子谱产生，**p̄/p 比在高能随 $\tau$_R(E) 下降而下降**（$\tau$_R 在反质子的能量处求值，而不是在产生它的更高能量处）[FACT]
- 图中**最低实线**：Protheroe 的计算（Ref. 43）
  - 逃逸长度 <10 GV 时比 Eq. (3) 低约 50%
- 若部分反质子在**源附近的物质**中由初级质子产生，驱动谱可能更硬（如 E⁻²·¹），给 p̄/p 比贡献一个**渐近常数**。

**模型 2：Closed galaxy**（Eq. 11 第三项重要）

- 一部分宇宙线是"老组分"（old component），驻留时间 $\tau$_R → ∞
- 老组分产生的反质子通量用 $\tau$_R → $\tau$_I 代替
- 此时 p̄/p 比**最终趋于常数**（因为 $\tau$_I = const）
- 但只在**非常高能量**才发生——当"年轻组分"的 $\tau$_R 下降得足够小，变得可忽略之后
- 图中**最上面一条曲线**（Ref. 43, 44, 45）

**模型 3：Reacceleration**（Eq. 11 第四项）

- 由 **Simon, Heinbach, Koch (1987, Ref. 48)** 讨论弱再加速对次级反质子产生的影响
- 图中**中间曲线**
- 当再加速是小效应时的迭代解（略去衰减项）：

$$J_{\bar{p}}^{(1)}(E) = J_{\bar{p}}^{(0)}(E)\left[1 + B\,\tau_R(E)\int_0^E \frac{dP(E,E')}{dE}\frac{J_{\bar{p}}^{(0)}(E')}{J_{\bar{p}}^{(0)}(E)}\,dE'\right] \quad (14)$$

- **再加速总是增大能量**（Simon et al. 假设）时：
  - 未扰动解 J⁽⁰⁾(E) 在 E_c ≈ **2 GeV** 处有特征最大值
  - E > E_c 时 J⁽⁰⁾(E) 下降，斜率反转
  - 再加速的净效果是把注入谱 J⁽⁰⁾(E) 向更高能量平移
  - 因为观测质子通量随能量下降，**高能处 p̄/p 比增大**（图中中间曲线）
  - 极高能处增大趋于零（因 $\tau$_R(E) 的能量依赖性）
  - **低能处 p̄/p 反而低于 leaky-box** 结果
- 若同时存在加速和减速，注入谱会向高低能两端展宽
- 再加速对次级核（如 B）的效果：次级核的注入谱总是随能量下降的，因此再加速项总是**给次级核谱增加**，低能增加多、高能增加少
- 若用 leaky-box 模型的 $\tau$_R(E) 作为输入，次级/初级比会比观测**更陡**；通过调整 $\delta$（Eq. 3 中的 $\delta$），使 $\tau$_R(E) 下降更慢来修正（Ref. 51）

### 3.5.5 Figure 3 — 反质子通量与模型

> **Figure 3**: Summary of antiproton data and models from Ref. 37. Other data shown is from Refs. 36a, 39, 40, 41.

- **横轴**：动能，GeV，对数坐标，范围 ~1–1000
- **纵轴**：J(E)，对数坐标，范围 $10^{-4}$ – $10^{-1}$
- **数据点**：
  - Ahlen et al. (1988)
  - Bogomolov et al. (1981)
  - Buffington et al. (1981)
  - Golden et al. (1978, 1984)
  - This work (1988) —— 指 Ref. 37 (Streitmatter et al.)
- **模型曲线**：
  - **下曲线**：leaky-box（Protheroe, Ref. 43），逃逸长度 <10 GV 时比 Eq. (3) 低约 50%
  - **中曲线**：再加速（Simon et al., Ref. 48）
  - **上曲线**：closed galaxy（Ref. 43）

[FACT] 作者引用：**Webber & Potgieter (Ref. 50)** 认为，当使用正确的 grammage、正确的星际初级谱并适当考虑核子效应后，**6–12 GeV 段反质子通量**可能**仅仅比最简 leaky-box 模型高不到 2 倍**。

### 3.5.6 本章结论 [FACT]

- **反质子是加速与传播的独特探针**：
  - 高阈值（5.63 GeV）
  - 产生截面强能量依赖性，向高能单调上升
  - 注入谱**相对尖锐峰值**（1.5–15 GeV 区间）
- 与次级核的信息**互补**
- 结合 He/H 同位素测量、正电子和电子通量（Ref. 52, 53）的测量，可以获得**更完整的宇宙线起源图景**

---

# 4. 公式汇总表

| 编号 | 公式 | 含义 |
|---|---|---|
| (1) | Q_CR = $\rho$_E V_S / $\tau$_R ~ 5×$10^{40}$ erg | 稳态宇宙线功率（文本印刷如此） |
| (2) | $\rho$_E = 4$\pi$ E² dN/dE = d$\rho$_$\epsilon$/d ln E | LIS 能量密度 |
| (3) | $\lambda$_esc = $\lambda$_esc(4 GV)(R/4 GV)^0.6 (R > 4 GV); 10.88 (R < 4 GV) | rigidity-dependent 逃逸长度 |
| (4) | J(E) ∝ E^(-$\delta$) × Q(E), $\delta$ ≈ 0.6 | 观测谱-源谱关系 |
| (5) | J(E) ∝ E^(-$\gamma$), $\gamma$ ≈ 2.7 (10 GeV – 数 TeV) | 观测微分谱 |
| (6) | E_max ≈ 3 $u_{1}$ Z e B ($\tau$_u $\tau$_A)/(20 c) | 最小散射长度下的加速上限 |
| (7) | E_max/Z ≈ $10^{14}$ eV (B=3$\mu$G, $u_{1}$=$10^{9}$ cm/s, $\tau$_A=$10^{3}$ yr) | 代入 ISM 参数后的 E_max |
| (8) | $E_{0}$ = w × N_e^(max) | 空气簇射初级能量估算 |
| (9) | p + H → p + p + p + p̄ | 反质子最小产生过程，阈值 5.63 GeV |
| (10) | $^{16}{\rm O}$ + H → $^{10}{\rm B}$ + … | 碎裂反应，>1 GeV 截面近似恒定 |
| (11) | 反质子平衡方程（源-逃逸-衰减-再加速） | 反质子通量的完整动力学方程 |
| (12) | Q_p̄(E) = 2$\alpha$$\rho$F ∫ dN_p J_p(E_p) dE_p | 反质子源项 |
| (13) | j⁽⁰⁾(E) = $\tau$_R(E) Q_p̄(E) | leaky-box 平衡解 |
| (14) | J_p̄⁽¹⁾(E) 迭代解，含再加速修正 | 小再加速效应下的反质子通量修正 |

---

# 5. 关键数值参数一览表

| 参数 | 数值 | 出处 |
|---|---|---|
| 超新星发生率 | 每 30 年 1 次 | 脚注 |
| 每次超新星壳层动能 | 2 × $10^{51}$ erg | 脚注 |
| 银河系宇宙线供给功率 | ~3 × $10^{42}$ erg/s | 脚注 |
| 稳态宇宙线功率 | ~5 × $10^{40}$ erg（或推论 ~3 × $10^{41}$ erg/s） | Eq. (1) |
| LIS 能量密度 $\rho$_E | ~1 eV/cm³ | 本文 |
| 源区体积 V_S | 5 × $10^{66}$ cm³ | 本文 |
| 在盘中的驻留时间 $\tau$_R | 5 × $10^{6}$ yr | 本文 |
| 逃逸指数 $\delta$ | ≈ 0.6 | Eq. (4) |
| 观测微分谱 $\gamma$ | ≈ 2.7 | Eq. (5) |
| 源谱指数 | ≈ 2.1 | 由 $\gamma$ - $\delta$ 推出 |
| 质子曲线积分面积 | 0.83 eV/cm³ | Fig. 1 |
| He+重核贡献 | 0.27 eV/cm³ | Fig. 1 |
| 膝部陡化范围 | $10^{15}$ – $10^{16}$ eV | 本文 |
| E_max/Z（超新星激波） | ~$10^{14}$ eV | Eq. (7) |
| 星际磁场 B | 3 $\mu$Gauss | 本文 |
| 激波速度 $u_{1}$ | $10^{9}$ cm/s | 本文 |
| 加速寿命 $\tau$_A | 1000 yr | 本文 |
| 反质子产生阈值 | 5.63 GeV | 本文 |
| 反质子截面 | ~1 mb @ 100 GeV; ~5 mb @ 1000 GeV | 本文 |
| 反质子源谱产额主要区间 | 1.5 – 15 GeV | 本文 |
| 未扰动反质子谱特征峰值 | E_c ≈ 2 GeV | 本文 |
| 膝部以上 Z > 2 比例（rigidity 陡化预测） | ~53%（比低能 36% 高 1.5 倍） | 本文 |
| >$10^{16}$ eV 通量 | ~1 m⁻² sr⁻¹ yr⁻¹ | 本文 |
| PSR 1957+20 周期 | 1.6 ms | Ref. 25 |
| 再加速所需 $\delta$ 调整 | $\tau$_R(E) 下降更慢 | Ref. 51 |

---

# 6. 关键参考文献分类与作用

| 编号 | 文献 | 在本文中的作用 |
|---|---|---|
| 1 | Ginzburg & Syrovatskii, 1964 | 超新星供给功率的经典参考 |
| 2 | Evenson, 1988 | LIS 质子谱（Fig. 1 曲线） |
| 7 | Gupta & Webber, 1989 | 逃逸长度拟合（Eq. 3） |
| 8 | Blandford & Eichler, 1987 | 激波加速理论综述 |
| 9 | Axford, 1987 | 膝部作为加速上限的解释者 |
| 10 | Lagage & Cesarsky, 1983 | Eq. (6) 加速上限公式 |
| 12 | Burnett et al. (JACEE), 1990 | 膝部能量段组分直接测量（Table 1） |
| 13 | Nagano et al. (Akeno), 1984 | 全粒子谱（Fig. 2） |
| 15 | Hillas, 1984 | 膝部不能由平滑 rigidity 陡化解释 |
| 16 | Fichtel & Linsley, 1986 | 高能新源（以质子为主） |
| 17 | Freudenreich et al. (Maryland), 1989 | 双分量：重核主导 |
| 18 | Völk & Biermann, 1988 | 前身星星风中的超新星加速 |
| 21 | Jokipii & Morrill, 1987 | 银河星风终止激波加速到 $10^{19}$–$10^{20}$ eV |
| 29 | Swordy, 1990 | 月球量能器方案 |
| 30 | Stephens & Golden, 1988 | 反质子通量异常的观测证据 |
| 31, 32 | Lagage-Cesarsky 1985; Cowsik-Gaisser 1982 | 遮蔽源模型 |
| 34 | Stecker & Wolfendale, 1984 | 原初反物质 |
| 35 | Stecker & Tylka, 1989 | WIMP 湮灭反质子 |
| 36, 37 | Ahlen 1988; Streitmatter 1989 | 低能 p̄/p 上限（Fig. 3） |
| 43 | Protheroe, 1981 | leaky-box 反质子计算（Fig. 3 下曲线） |
| 44 | Peters & Westergaard, 1977 | closed galaxy 模型 |
| 45 | Steigman, 1977 | 次级反质子作为探针 |
| 46 | Wandel et al., 1987 | 分布再加速 |
| 47 | Cesarsky, 1987 | 星际介质中传播的综述 |
| 48 | Simon et al., 1987 | 弱再加速对 p̄ 的影响（Fig. 3 中曲线） |
| 50 | Webber & Potgieter, 1989 | 6–12 GeV 段 p̄/p 比仅高出 2 倍 |

---

# 7. 作者论证链重建

```
超新星供给功率 ≈ 宇宙线稳态功率
     ↓
大部分宇宙线由超新星激波通过一阶 Fermi 加速产生（源谱 E⁻²，观测谱 E⁻²·⁷，$\delta$ ≈ 0.6）
     ↓
膝部（$10^{15}$–$10^{16}$ eV）陡化 → 两种解释：
  A) 超新星激波加速上限（rigidity-dependent, E_max/Z ~ $10^{14}$ eV）
  B) 银河系 rigidity-dependent 逃逸率增加
     ↓
膝部以上组分直接测量（JACEE, Table 1）是判别关键 → 但统计量不足
     ↓
空气簇射实验（Fig. 2, Akeno）揭示陡化但模型依赖（w, N_e(max) 修正）
     ↓
膝部以上组分三种观点：Hillas（新成分）/ Fichtel-Linsley（新质子源）/ Maryland（重核主导）
     ↓
替代高能机制：Völk-Biermann 星风空腔 / Jokipii 磁场几何 / 星风终止激波 / 点源
     ↓
反质子：高阈值 5.63 GeV、强能量依赖截面 → 独特探针
     ↓
平衡方程 (11) → 三模型对比：leaky-box / closed galaxy / reacceleration
     ↓
Fig. 3 显示当前数据与 leaky-box 大致吻合
     ↓
结论：膝部组分直接测量 + 反质子精确能谱 → 互补探针宇宙线起源-加速-传播
```

---

# 8. 隐含信息与文献未明确说明之处

- **[Information Not Explicitly Provided]** 反质子最小产生过程的 Q-value 具体计算未展开（仅给出阈值 5.63 GeV）。
- **[Information Not Explicitly Provided]** 超新星供给功率 3×$10^{42}$ erg/s 与 Eq. (1) 中 5×$10^{40}$ erg 的**数量级差异未解释**——可能是 Eq. (1) 印刷错误或单位不同（例如漏了 s⁻¹）。
- **[Information Not Explicitly Provided]** "shrouded sources" 模型中遮蔽层的具体质量厚度（g/cm²）未给出。
- **[隐含]** 作者默认读者熟悉 B/C 比、leaky-box、closed galaxy、分布再加速等标准宇宙线传播框架。
- **[隐含]** Fig. 3 中的"this work (1988)"对应 Ref. 37 (Streitmatter et al.)，作者本人是合作者。
- **[隐含]** 对太阳调制效应的讨论仅在低能反质子（<1 GeV）处轻触一笔，主要依赖 Perko (49)、Webber-Potgieter (50)。