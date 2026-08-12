# 01. Theoretical Background — 第1–2章精读

> 本章属于：Cosmic-ray propagation and interactions in the Galaxy (Strong, Moskalenko & Ptuskin, 2007)
>
> 上一章：`00_overview.md`
>
> 下一章：`02_confrontation_with_data.md`

---

## 1. Introduction（引言）

### 1.1 本节核心内容

作者阐述宇宙线在 Astrophysics 中的独特地位：宇宙线是少数可直接采样的星际物质（其余为陨石和星尘），提供了几百万年尺度内星际介质的元素和同位素样本。

### 1.2 原文内容

#### 宇宙线的独特地位

[FACT] "Cosmic rays are almost unique in astrophysics in that they can be directly sampled, not just observed via electromagnetic radiation."

宇宙线作为直接的星际物质样品，其价值是其他电磁辐射观测无法替代的。

#### 综述文献导览

作者列举了大量历史文献，包括：

- Annual Reviews 相关文章（1952–1989 年约 15 篇），涵盖重核 (1)、集体输运效应 (2)、成分 (3) 和传播 (4)
- 基本教科书：Ginzburg & Syrovatskii 的《The Origin of Cosmic Rays》(9) 是现代宇宙线研究的奠基之作；其更新版 (8) 是基础参考
- 其他重要书籍：Hillas (11)、Gaisser (12)、Stanev (13)（高能）、Schlickeiser (14)（理论）、Diehl et al. (15)（实验数据概览，截至 2001 年）
- 高能（>10¹⁵ eV）宇宙线：作者明确排除，引用 (16–18) 和 (25–27)
- 相互作用：(19)；实验与天体物理：(20)；传播与成分：(21–24)

#### 两种研究方法

[FACT] 作者区分了两种研究宇宙线传播的途径：

1. **粒子观点**：关注粒子谱、相互作用、与观测的直接比较
2. **ISM 气体观点**：将宇宙线视为无质量无碰撞的相对论性气体，考虑其压强和能量，与其他 ISM 成分一起处理

[FACT] "Both ways of looking at the problem are valid up to a point, but for consistency a unified approach would be desirable and to our knowledge has never been attempted." 统一方法尚未尝试，最接近的是 (32, 33)。

> **分析 / Interpretation**：这一区分非常重要。本文主要从粒子观点出发（因为目标是与观测比较），但作者意识到与 ISM 动力学的自洽耦合是未来的方向。

#### 观测进展

[FACT] 该领域最近的重大进展是：
- 同位素成分和元素谱的高质量测量
- 伽马射线望远镜（卫星和地面）的观测

文中给出了直接测量（Figs. 1–13）和间接伽马射线测量（Figs. 14, 16）的概览图。

#### 本文范围声明

[FACT] 明确排除的内容：
- 宇宙线起源（"we will, for the most part, sidestep this problem"，遵循 Cesarsky 1980）
- 超新星遗迹作为宇宙线源（文献可追溯至最近的 H.E.S.S. TeV γ-ray 结果 (34)）
- 太阳调制
- 星系团
- 外银河宇宙线
- 能量高于 10¹⁵ eV 的宇宙线

[FACT] 主要关注银河系自身，但提及来自外星系的信息（通过同步辐射）。

#### 低能端的补充说明

[FACT] MeV 粒子虽非相对论性但也是非热平衡的，必须纳入讨论，尤其因为它们对星际介质的加热和电离很重要 (28)。例如，附近的超新星遗迹产生的宇宙线可能抑制分子云中的恒星形成 (29)。

---

## 2. Cosmic-ray Propagation: Theory（传播理论）

### 2.1 Basics and Approaches（基本概念与途径）

#### 2.1.1 本节核心内容

介绍为什么次级核素是研究传播的良好探针：初级核素已知，因此次级产生函数可以精确计算，然后通过"传播"与观测比较。

#### 2.1.2 关键历史脉络

[FACT] 自意识到宇宙线充满银河系以来，核相互作用就意味着成分信息包含传播信息 (44)。1970 年代锂、铍、硼同位素的卫星测量是历史性事件 (45)。

[FACT] "The simple observation that the observed composition of CR is different from that of solar, in that rare solar-system nuclei like Boron are abundant in CR, proves the importance of propagation." 硼在太阳系中稀少但在宇宙线中丰富，这直接证明了传播中碎裂的重要性。

[FACT] 经典的"几 g cm⁻²"穿透物质厚度是宇宙线物理学最广为人知的事实之一。

[FACT] 作者认为："the diffusion model with possible inclusion of convection provides the most adequate description of CR transport in the Galaxy at energies below about 10¹⁷ eV."

---

### 2.2 Propagation Equation（传播方程）

#### 2.2.1 本节核心内容

给出宇宙线传播的完整偏微分方程，即核心方程 (1)。

#### 2.2.2 关键公式

$$\frac{\partial\psi(\vec{r}, p, t)}{\partial t} = q(\vec{r}, p, t) + \nabla \cdot (D_{xx} \nabla\psi - \vec{V}\psi) + \frac{\partial}{\partial p} p^2 D_{pp} \frac{\partial}{\partial p} \frac{1}{p^2}\psi - \frac{\partial}{\partial p}\left[\dot{p}\psi - \frac{p}{3}(\nabla \cdot \vec{V})\psi\right] - \frac{1}{\tau_f}\psi - \frac{1}{\tau_r}\psi$$

**各项物理含义**：

| 项 | 符号 | 物理意义 |
|---|---|---|
| **源项** | $q(\vec{r}, p, t)$ | 初级（injection）、碎裂（spallation）和衰变贡献之和 |
| **空间扩散** | $D_{xx}$ | 空间扩散系数，一般依赖于 $(\vec{r}, \beta, p/Z)$ |
| **对流** | $\vec{V}$ | 银河风（对流）速度 |
| **动量空间扩散（再加速）** | $D_{pp}$ | 随机加速，与 $D_{xx}$ 通过 $D_{pp} \propto p^2 D_{xx}$ 关联 |
| **能量损失/增益** | $\dot{p} = dp/dt$ | 包含辐射损失（同步辐射、逆康普顿）、电离损失、绝热损失等 |
| **绝热项** | $\frac{p}{3}(\nabla \cdot \vec{V})\psi$ | 非均匀流中的绝热能量变化，冻结在磁场中的不均匀性散射 CR |
| **碎裂** | $\tau_f$ | 由总碎裂截面和 $n(\vec{r})$ 决定 |
| **放射性衰变** | $\tau_r$ | 放射性衰变时间尺度 |

[FACT] $\psi(\vec{r}, p, t)$ 是单位总动量 $p$ 的 CR 密度，$\psi(p)dp = 4\pi p^2 f(\vec{p})dp$。

#### 2.2.3 关于源项 $q(\vec{r}, p, t)$ 的详细说明

[FACT] CR 源通常假设集中在银河盘附近，径向分布类似超新星遗迹。

[FACT] 碎裂部分依赖于所有母核物种及其能量依赖截面，以及气体密度 $n(\vec{r})$。

[FACT] 假设碎裂产物与母核具有相同的每核子动能。

[FACT] K-电子俘获和电子剥离可通过 $\tau_f$ 和 $q$ 纳入。

#### 2.2.4 关于扩散系数 $D_{xx}$

[FACT] $D_{xx}$ 一般依赖于 $(\vec{r}, \beta, p/Z)$，其中 $\beta = v/c$，$Z$ 是电荷，$p/Z$ 决定给定磁场中的回转半径。

[FACT] $D_{xx}$ 可以是各向同性的，或更真实地说是各向异性的。

[FACT] $D_{pp}$ 通过 $D_{pp} D_{xx} \propto p^2$ 与 $D_{xx}$ 关联（§2.5 详细描述）。

[FACT] CR 自身可能影响 $D_{xx}$（例如在波阻尼模型中）。

#### 2.2.5 边界条件

[FACT] 通常假设在"晕边界"（粒子逃逸到星际空间处）$\psi = 0$，但这显然只是近似（因为星际通量不为零），可在具有物理边界处理模型中放宽。

[FACT] 方程 (1) 是含时的；通常求稳态解（设 $\partial\psi/\partial t = 0$，或跟随时间依赖至达到稳态）。

[FACT] $q$ 的时间依赖性被忽略，除非研究附近新源或源的随机性效应。

#### 2.2.6 数值求解策略

[FACT] "Starting with the solution for the heaviest primaries and using this to compute the spallation source for their products, the complete system can be solved including secondaries, tertiaries etc." 从最重初级核开始，逐步向下求解。

[FACT] 源丰度通过迭代确定，与数据比较。对于源丰度很小的核素，源值被次级和截面不确定性掩盖，难以确定。

> **分析 / Interpretation**：方程 (1) 是本综述的**核心方程**。文中所有数值模型（GALPROP 等）和解析模型都是对此方程在不同近似下的求解。理解后续所有讨论的钥匙就是这 8 个物理过程（源、扩散、对流、再加速、能量损失、绝热变化、碎裂、衰变）。

---

### 2.3 Diffusion（扩散）

#### 2.3.1 本节核心内容

从微观（准线性理论）和宏观（经验模型）两个层面解释扩散系数的起源和数值。

#### 2.3.2 经验值

[FACT] 从 CR 数据拟合得到的典型值：
$$D_{xx} \sim (3-5) \times 10^{28} \text{ cm}^2 \text{s}^{-1} \quad \text{at energy} \sim 1 \text{ GeV/n}$$

[FACT] 扩散系数随磁刚度按 $R^{0.3} - R^{0.6}$ 增加（不同经验模型版本）。

#### 2.3.3 微观理论：准线性理论

[FACT] 在微观层面上，扩散源于粒子在随机 MHD 波和不连续性上的散射。带电粒子在具有小随机涨落 $\delta B \ll B$ 的磁场中运动的有效"碰撞积分"来自等离子体湍流的准线性理论 (51)。

[FACT] 波-粒子相互作用是共振性质的：
$$k_\parallel = \pm s / (r_g \mu)$$
其中 $\mu$ 是粒子投掷角，整数 $s = 0, 1, 2...$ 对应不同阶的回旋共振。

[FACT] 一阶共振 $s = 1$ 对各向同性和一维随机 MHD 波分布最重要。

[FACT] 空间扩散在局部是强各向异性的，主要沿磁力线。但在大尺度 ($L \sim 100$ pc) 磁场涨落（随机场强度为平均场的数倍）下，全局扩散趋于各向同性。

#### 2.3.4 扩散系数估计

[FACT] 从理论估计：
$$D_{xx} \approx (\delta B_{res}/B)^{-2} v r_g / 3$$

其中 $\delta B_{res}$ 是共振波数 $k_{res} = 1/r_g$ 处的随机场幅度。

[FACT] 星际湍流能谱：
$$w(k)dk \sim k^{-2+a}dk, \quad a = 1/3 \quad \text{在} \quad 1/(10^{20}\text{cm}) < k < 1/(10^8\text{cm})$$

[FACT] $\delta B \approx 5 \mu G$（主尺度），估计 $D_{xx} \approx 2 \times 10^{27} \beta R^{1/3}_{GV} \text{ cm}^2 \text{s}^{-1}$，适用于 $R < 10^8$ GV，与经验模型（含分布式再加速版本）一致。

[FACT] $D_{xx} \sim R^{1/3}$ 的标度由指数 $a = 1/3$（Kolmogorov 谱）决定。

#### 2.3.5 Kolmogorov vs. Kraichnan 谱

| 谱类型 | 指数 $a$ | 扩散标度 | 对应 |
|---|---|---|---|
| **Kolmogorov** | $1/3$ | $D_{xx} \sim R^{1/3}$ | 低能区，经验模型（含再加速） |
| **Kraichnan** | $1/2$ | $D_{xx} \sim R^{1/2}$ | 高能极限，"plain diffusion"模型 |

[FACT] 理论上 (55)，Kolmogorov 谱可能只适用于沿磁场方向强烈伸长的 Alfvénic 结构，这些结构不能提供显著的散射。更各向同性的快磁声波部分，具有 Kraichnan 型指数 $a = 1/2$，可能存在于星际介质中 (56)。

> **分析 / Interpretation**：这一部分是本文理论核心的微观基础。$a = 1/3$ 还是 $a = 1/2$ 不仅决定了 $D_{xx}(R)$ 的依赖关系，还决定了能否同时拟合次级/初级比和 CR 各向异性（见 §3.5）。

---

### 2.4 Convection（对流/银河风）

#### 2.4.1 本节核心内容

讨论银河风是否存在及其对宇宙线传播的影响，包括对流和绝热能量损失。

#### 2.4.2 模型分类

[FACT] 两种模型已被研究：
- **1-zone 模型**：对流和扩散处处存在
- **2-zone 模型**：距盘面某距离以内只有扩散，以外是扩散+对流

#### 2.4.3 检验

[FACT] 对一维扩散/对流模型，次级/初级比的能量依赖是一个良好的诊断：

[FACT] 纯对流传输没有能量依赖性（除反应率的 $\beta$ 依赖外），这与观测矛盾。

[FACT] 如果扩散率在低能降低，任何对流最终会占主导，使次级/初级比在低能变平——这被观测到但对 B/C 拟合很差 (67)。

[FACT] 放射性同位素约束风速度 $< 10$ km s⁻¹ kpc⁻¹（线性增加风）。

[FACT] 拟合 B/C 需要约 $15$ km s⁻¹ 的恒定速度风（即使存在再加速 (68)），相比之下 (69) 的风模型为 $30$ km s⁻¹；后者意味着扩散系数的能量依赖可能与 CR 各向异性冲突。

#### 2.4.4 自洽模型

[FACT] (33) 研究了 CR 和热气驱动的银河风自洽两区模型：
- $|z| < 1$ kpc：完全扩散
- 以外：扩散-对流
- CR 到达对流区后不返回，因此对流区充当随能量和银心距变化的晕边界

[FACT] (70) 构造了 CR 驱动的风，各向异性扩散的自洽模型，外区对流速度高达 $100$ km s⁻¹，但与放射性核素不冲突（因为该约束仅适用于内区）。

> **分析 / Interpretation**：作者总体上对银河风模型持保留态度——缺乏直接观测证据，且参数选择面临多种约束的竞争。2-zone 自洽模型是当前最有前景的版本。

---

### 2.5 Reacceleration（再加速）

#### 2.5.1 本节核心内容

描述动量空间扩散的物理（随机加速），与扩散的关系，以及对观测数据的解释。

#### 2.5.2 关键公式

[FACT] 动量空间扩散系数：
$$D_{pp} = \frac{p^2 V_a^2}{9 D_{xx}}$$
其中 $V_a$ 是 Alfvén 速度，作为弱扰动在磁场中传播的特征速度。

#### 2.5.3 能否作为主加速机制？

[FACT] "Distributed acceleration in the entire Galactic volume cannot serve as the main mechanism of acceleration of CR at least in the energy range 1–100 GeV/n." 因为更高能粒子在系统中停留时间更长，次级核丰度随能量增加而增加，与观测矛盾。

[FACT] 该论证在低能区不成立——分布加速可能很强，可以解释次级/初级比在约 1 GeV/n 处的峰值。

[FACT] 再加速的术语用于区分源区的主加速过程。

#### 2.5.4 与观测的比较

[FACT] (71, 46) 表明：如果 $D_{xx} \sim R^a$（$a \sim 0.3$，对应 Kolmogorov 谱）且 Alfvén 速度 $V_a \sim 30$ km s⁻¹（接近 ISM 中的实际值），则可以解释次级核丰度的能量依赖。

#### 2.5.5 K-俘获同位素检验

[FACT] 再加速的额外检验来自次级 K-俘获同位素：³⁷Ar, ⁴⁴Ti, ⁴⁹V, ⁵¹Cr 等，在低能时通过电子俘获快速衰变。

[FACT] 电子轨道存在的概率强烈依赖于能量，因此这些同位素及其衰变产物的丰度是能量的强函数，对能量变化敏感。

[FACT] ⁴⁹V 和 ⁵¹Cr 在 CR 中能量依赖衰变的首次测量 (73) 被用来检验分布再加速速率 (74)，但需要核产生截面的精细化。

#### 2.5.6 波阻尼效应

[FACT] 再加速中粒子能量的增益伴随着 MHD 湍流的能量损失。计算表明 (75)，在小尺度（$< 10^{13}$ cm）的 Kraichnan 非线性级联可能受到 CR 耗散的显著影响，甚至终止级联。

[FACT] 结果：扩散系数刚度依赖的自洽变化，$D_{xx}$ 在小刚度处急剧上升。该机制解释了高能扩散标度 $D_{xx} \sim R^{0.5}$，并为初级/次级比的能量依赖提供了解释。

#### 2.5.7 源区效应

[FACT] 在源区（小体积填充因子的高速度 SNR 激波区域），两个效应可产生平坦能谱的次级成分 (76, 77)：
1. 平源谱（$\sim E^{-2}$）的初级核碎裂产生次级
2. SNR 激波直接加速 ISM 中的背景次级核

[FACT] 计算表明这些效应在 $>100$ GeV/n 可能产生高于标准次级陡谱的平坦成分。

> **分析 / Interpretation**：再加速是本综述的一个关键主题，它解决了"为何次级/初级比在低能下降比纯 $\beta$ 依赖更快"这一难题，且与 Kolmogorov 谱（$a \sim 0.3$）一致。然而 K-俘获同位素的直接证据仍因截面不确定性而不明确。

---

### 2.6 Galactic Structure（银河系结构）

#### 2.6.1 本节核心内容

概述影响 CR 传播的银河系结构要素：气体、磁场、辐射场和太阳本地环境。

#### 2.6.2 气体分布

[FACT] 原子氢从 21 cm 巡天已知，分子氢较不确定（需要 CO 示踪，转换因子难以确定，且可能随位置变化）。

[FACT] CR-气体相互作用是确定银河系分子氢含量的最佳方法之一（见伽马射线章节）。

#### 2.6.3 磁场

[FACT] 大尺度场：几个 $\mu$G，沿旋臂排列，但细节尚无共识 (79)。

[FACT] 近期分析给出大尺度银河磁场的双对称模型，在臂间边界反转 (80)。

[FACT] 通过同步辐射、CR 和 $\gamma$ 射线数据的联合分析，确认几个 $\mu$G 的强度，向银河系内部增加 (81)。

[FACT] $>10^{15}$ eV 的全球拓扑重要，影响 CR 各向异性和点源搜索——作者排除。

#### 2.6.4 星际辐射场 (ISRF)

[FACT] 来自所有类型恒星，经星际尘埃吸收和再发射加工，覆盖远红外到紫外。

[FACT] ISRF 的计算很困难，但现在有了关于恒星含量和尘埃的更多信息来改进模型 (85)。

#### 2.6.5 太阳本地环境

[FACT] 本地泡可能对放射性核素有影响（§3.2）。

[FACT] "the Sun left the local bubble about $10^5$ years ago after spending several million years inside, and we now live in the CLIC (collection of local interstellar clouds) with HI density about $0.2$ cm⁻³ and $35$ pc extent." (86, 87, 134)

[FACT] 该问题对 CR 传播的影响尚未被探讨。

---

### 2.7 Interactions（相互作用）

#### 2.7.1 本节核心内容

简要概述与 CR 传播相关的核相互作用和能量损失过程。

#### 2.7.2 关键文献

作者将主要过程及其参考文献汇集在系列论文中：

| 过程 | 参考文献 |
|---|---|
| 核和电子的能量损失 | (67) |
| 轫致辐射和同步辐射 | (81) |
| 逆康普顿（各向异性散射） | (88) |
| $\pi$ 衰变产生 $\gamma$ 射线、电子、正电子 | (39) |
| 用现代粒子物理代码研究 $\pi$ 产生 | (89, 90) |
| 碎裂截面测量和模型 | J. Connell in (91); (92, 93, 94) |
| 放射性过程和 K-俘获 | (95, 96, 97, 73, 98) |

[FACT] 用现代粒子物理代码 (89, 90) 的详细 $\pi$ 产生研究给出谱指数比旧处理硬 0.05，且几个 GeV 处 $\gamma$ 射线产额略高。

> **分析 / Interpretation**：这些是 GALPROP 等传播代码的输入物理过程。碎裂截面的准确性直接影响次级/初级比的计算精度，是本领域的一个长期不确定因素。

---

### 2.8 Weighted Slabs and Leaky Boxes（加权板与泄漏盒）

#### 2.8.1 本节核心内容

解释泄漏盒和加权板形式是如何作为扩散模型的近似获得的，以及它们的适用条件和局限。

#### 2.8.2 泄漏盒模型

[FACT] 在泄漏盒模型中，扩散和对流项被泄漏项近似，具有某特征逃逸时间 $\tau_{esc}$。

[FACT] 泄漏盒方程在以下两种情况下可作为扩散模型的正确近似：
1. 快速 CR 扩散 + 晕边界反射（有逃逸概率）的模型 (9)
2. 平坦晕模型（$z_h \ll R$）中薄源盘和薄气体盘（$z_{gas} \ll z_h$）的盘内 CR 密度公式 (10)，在考虑稳定核时形式上等价于泄漏盒公式

[FACT] 核碎裂实际由逃逸长度（g cm⁻²）决定，而非逃逸时间：
$$x = v \rho \tau_{esc}$$
其中 $\rho$ 是包含 CR 晕体积的星际气体平均密度。

#### 2.8.3 加权板方法

[FACT] 加权板方法 (99, 9) 将问题拆分为天体物理部分和核部分：
- 核碎裂在板模型中求解：CR 束穿越厚度 $x$ 的星际气体
- 对所有 $x$ 值用天体物理传播模型导出的分布函数 $G(x)$ 加权积分

[FACT] 标准加权板在以下情况失效：低能 CR（核截面强能量依赖、强能量损失、能量依赖扩散），以及扩散系数依赖核物种时误差显著。

[FACT] 经修改 (102) 后，在扩散系数可分离依赖能量（或刚度）和位置且无对流的特殊情况下变得严格。

[FACT] 泄漏盒模型的 $G(x)$ 是指数分布：
$$G(x) \propto \exp(-x/X)$$
平均 grammage 等于逃逸长度 $X$。

#### 2.8.4 截断问题

[FACT] 在指数路径长度分布下，在小路径长度（$1$ GeV/n 附近低于几个 g cm⁻²）处存在截断的讨论已持续数十年 (1, 101, 105, 106)。

[FACT] 在云状星际介质的 CR 扩散和核碎裂一致理论中，如果部分 CR 源位于巨分子云内部，则截断自然发生 (107)。

#### 2.8.5 放射性核素

[FACT] 对放射性核素，经典方法是计算"存活分数"——观测丰度与无衰变情况下的预期丰度之比。

[FACT] "The surviving fraction can better be related to physical parameters (108)." 存活分数可以转化为物理量（如扩散系数），而非直接使用泄漏盒"气体密度"。

---

### 2.9 Explicit Models（显式模型）

#### 2.9.1 本节核心内容

综述各种显式解析解方法的进展和局限。

#### 2.9.2 关键模型一览

| 方法 | 引用 | 特点 | 局限 |
|---|---|---|---|
| 显式解（先驱工作） | (10), (109, 65) | 2D 扩散-对流，含源分布 | 许多限制性近似（无能量损失、简单气体模型） |
| 半经验 2D 模型 | (110, 68) | 含能量损失和再加速，Green 函数形式 | 气体为盘内常数密度 |
| 含时显式解 | (111) | 推广气体分布 | 无能量损失 |
| 多源模型 | (112) | Green 函数 | 无能量损失，有缺陷被指出 (111) |
| 3D 解析传播 | (114, 115) | 含能量损失和再加速，通过 PLD | 无法正确处理电离损失 |
| 精细空间时间变化 | (116) | 无能量损失 Green 函数 | 对离散源效应的研究有用 |
| 完全数值（GALPROP） | §2.10 | 三维数值 | 高能粒子轨迹计算未纳入 |

#### 2.9.3 蒙特卡罗方法的前景

[FACT] 蒙特卡罗方法可显式包含场线扩散（对银河系垂直方向传播很重要）等效应。

[FACT] 但仍是挑战：GeV 粒子平均自由程 $\sim 1$ pc，在 $4$ kpc 晕高度的银河系中需要 $\sim(4000/1)^2 \approx 10^7$ 次散射才能离开银河系——即使现在的超级计算机也难以获得足够统计量。

[FACT] "we expect numerical solution of the propagation equations to remain an important approach for the foreseeable future."

---

### 2.10 GALPROP（GALPROP 代码详解）

#### 2.10.1 本节核心内容

详细描述 GALPROP 代码的设计目标、功能和局限。

#### 2.10.2 设计目标

GALPROP (67) 的创建目标：

1. 同时预测所有相关观测：CR 核、电子和正电子、$\gamma$ 射线和同步辐射
2. 克服解析和半解析方法的局限，利用计算能力进展
3. 纳入银河系结构和源分布的最新信息
4. 提供公开可用的代码作为进一步扩展的基础

[FACT] 第一点最重要："all data relate to the same system, the Galaxy, and one cannot for example allow a model which fits secondary/primary ratios while not fitting $\gamma$-rays or not being compatible with the known interstellar gas distribution."

[FACT] 作者坦承："to find one model satisfying all of them is a challenge, which in fact has not been met up to now."

#### 2.10.3 技术细节

[FACT] 传播方程 (1) 在空间网格上数值求解，2D（轴对称）或完整 3D。

[FACT] 边界（半径和高度）及网格间距用户可调。

[FACT] 动量网格（用动量而非动能，因为方程 (1) 中的自然量是动量）。

[FACT] 方程 (1) 中所有过程的参数可在输入中控制。

[FACT] CR 源分布可自由选择，通常表示 SNR。源谱形状和同位素成分（相对质子）是输入参数。

[FACT] 星际气体分布基于最新 HI 和 CO 巡天，ISRF 基于详细计算，截面基于广泛汇编和参数化 (92)。

[FACT] 求解从最重初级核（如 ⁶⁴Ni）开始，逐步向下计算碎裂源项，直至质子、次级电子/正电子和反质子。⁽¹⁰B 通过 ¹⁰Be 衰变通道产生，重要，需要第二次迭代⁾。

[FACT] GALPROP 包含 K-俘获和电子剥离过程：H-原子视为单独物种（因为寿命不同）。H-原子只有 1 个 K-壳电子，因此 K-俘获半衰期需乘 2。

[FACT] 质子、氦和电子的实验数据归一化由用户提供（其他同位素由源成分和传播决定）。

[FACT] $\gamma$ 射线和同步辐射使用星际气体数据（$\pi$ 衰变和轫致辐射）和 ISRF 模型（逆康普顿）计算。

[FACT] 输出：所有物种在选定网格上的谱，以及 $\gamma$ 射线和同步辐射全天图，标准天文格式。

[FACT] 近期扩展：非线性波阻尼 (75) 和暗物质包。

#### 2.10.4 计算资源与局限

[FACT] "The computing resources required by GALPROP are moderate by today's standards."

[FACT] 已知局限：
- 仅能量低于 $10^{15}$ eV（无轨迹计算）
- 均匀的源丰度（无 superbubble 增强）
- 仅 $>10$ pc 尺度（无 clumpy ISM，受计算能力限制）
- 同步辐射中 B-场视为随机（规则分量影响射电辐射结构）

#### 2.10.5 GALPROP 的地位

[FACT] GALPROP 被 NASA 的 GLAST（即费米）$\gamma$ 射线天文台采纳为弥散银河 $\gamma$ 射线辐射的标准，AMS、ACE、HEAT 和 Pamela 合作组也在使用。

> **分析 / Interpretation**：GALPROP 是本综述作者的旗舰工具，也是该领域的标准传播代码。理解 GALPROP 对于理解本文的所有数值结果和后续研究至关重要。GALPROP 的局限（如均匀源丰度、无小尺度结构）也是当前传播建模需要改进的方向。

---

### 2.11 Numerical versus Analytical（数值法 vs. 解析法——作者观点）

[FACT] 作者明确表达倾向于数值方法的观点，反驳了三种认为解析方法有优势的常见主张：

1. **物理洞察**：简单情况解析解确实有用，但复杂公式最终也可能无洞察；数值模型非常直观（显式生成全银河系分布）
2. **等价于完整解**：只在限制条件下成立（涉及能量损失和空间变化密度）；电子/正电子本就在解析方法之外
3. **更快、更易计算**：现代计算机使速度问题不再相关

[FACT] 引述 Wallace (1981) 的论断：
> "It is unclear whether one would wish to go much beyond the generalizations discussed above for an analytically soluble diffusion model. The added insight from any analytic solution over a purely numerical approach is quickly cancelled by the growing complexity of the formulae."

[FACT] 宇宙线空中簇射计算中，解析法在至少 40 年前就让位于数值法。

---

### 2.12 Self-consistent Models（自洽模型）

[FACT] 少数尝试将 CR 作为 ISM 动力学的一个相对论性气体成分进行自洽描述。

[FACT] (32, 33) 建立了含 CR 驱动风的磁化 ISM 3D 模型，声称与 CR 次级/初级比一致。

[FACT] 这种风被提出作为 CR 梯度问题的可能解释 (70)。

[FACT] Parker 不稳定性近期用各向异性扩散 (120) 重新分析 (119)，随后有 CR 驱动银河发电机模型 (121)，使用 Zeus-3D MHD 代码扩展 (30) 含 CR 传播和源。

[FACT] 在湍流动力学作用产生的磁场中研究 CR 传播 (31) 提供了全新视角。

[FACT] 扩展到包含 CR 谱、次级、$\gamma$ 射线等（与观测的完整比较）"would be very desirable but has not yet been attempted."

[FACT] 另一种自洽性：将 CR 对扩散系数的影响纳入 (75)。

---

> 下一章：`02_confrontation_with_data.md`
