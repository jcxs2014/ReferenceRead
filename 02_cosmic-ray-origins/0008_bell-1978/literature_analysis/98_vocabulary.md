---
# 98. Vocabulary — Bell (1978) 学术词汇表

## A. 逻辑连接词（基于 Bell 1978 原文）

| 词汇/短语 | 原文例句 | 逻辑功能 |
|---|---|---|
| initially | 'Initially I consider a parallel shock, in which the direction of propagation is along the magnetic field lines' | 引入首批假设（§1） |
| however | 'The shock front itself is the region in which the mean plasma velocity changes' | 转折，引入变化（§2 开头） |
| since | 'Since this is much larger than the thickness of the shock front, this thickness is usually thought to be of the order of, or less than, the gyroradius of a thermal proton' | 因果，解释几何（§1） |
| consequently | 'Consequently Alfvén waves have been detected upstream of the Earth's bow shock' | 因果，解释观测（§1） |
| in the case of | 'In the case of a thermal proton (Boyd & Sanderson 1969), as is observed to be the case for the Earth's bow shock (Formisano 1974)' | 条件举例（§1） |
| for very energetic particles | 'For very energetic particles ($v \gg c$)' | 条件，引出极限（§2） |
| it is assumed | 'it is assumed that the upstream Alfvén waves consist entirely of waves which are moving away from the shock' | 引入简化假设（§2） |
| in summary | 'As a numerical factor, close to unity, is needed in equation (9) to correct for the assumption that all particles have the same energy after $l$ cycles' | 解释数值修正（§2 脚注） |

## B. 领域术语（Bell 1978 核心概念）

### 0.1 DSA 通用概念

- **diffusive shock acceleration (DSA)**：
  - 定义：粒子通过激波压缩下的扩散-对流机制被反复加热的加速过程。Blandford & Eichler 1987 综述中正式命名，本文为奠基论文之一。
  - 原文语境：本文未用此术语，但实质上推导了 DSA 的解析谱指数（$\mu = (2u_2+u_1)/(u_1-u_2)$）。

- **first-order Fermi acceleration**：
  - 定义：粒子每次穿越激波时获得 $\Delta E/E \sim (u_1-u_2)/c$ 量级的能量（一阶），与 second-order Fermi（$\sim (v/c)^2$）的关键区别。
  - 原文语境：'It is similar to those proposed by Jokipii (1966) and Fisk (1971)...It differs from them in that the fast particles themselves generate the waves responsible for their confinement near the shock'（§1）

- **test-particle approximation**：
  - 定义：假设宇宙线能量密度远小于热能、湍流、磁场能量密度——CR 对激波结构无反馈。
  - 原文语境：本文 §2 全程在 test-particle 极限下推导谱指数。后续 Malkov 1987、Drury 1994 引入 non-linear DSA（NLDSA）超越此近似。

- **streaming instability**：
  - 定义：高能粒子相对周围等离子体超 Alfvénic 流速时激发 Alfvén 波的不稳定性。
  - 原文语境：本文 §3 把 streaming instability 作为粒子激发散射场的物理机制。

- **self-confinement**：
  - 定义：粒子通过自身激发的 Alfvén 波约束在激波附近。
  - 原文语境：本文核心创新——区别于前人外加散射场模型。本文 §3.5 跨章节分析中明确称为「自洽三件套」核心。

### 0.2 几何与运动学

- **parallel shock**：
  - 定义：激波传播方向与上游磁场平行。
  - 原文语境：本文假设 'a parallel shock, in which the direction of propagation is along the magnetic field lines'（§1）。

- **shock compression ratio**：
  - 定义：$u_1/u_2 = \chi$，激波前/后流体速度比。强激波极限 $\chi = 4$（单原子气体、$\gamma = 5/3$）。
  - 原文语境：$\mu = (2u_2+u_1)/(u_1-u_2)$，强激波 $\chi = 4$ → $\mu = 2$。

- **upstream / downstream**：
  - 定义：激波前为 upstream（粒子流向激波），激波后为 downstream（粒子被扫走）。本文以 $x=0$ 为激波，$x>0$ 为下游。
  - 原文语境：§2 Fig.1 详细几何示意。

- **gyroradius**：
  - 定义：粒子在磁场中回旋半径，$r_L = p/(eB)$，$p$ 为动量。
  - 原文语境：'this thickness is usually thought to be of the order of, or less than, the gyroradius of a thermal proton'（§1 中假设的物理基础）。

### 0.3 散射与波

- **Alfvén wave scattering**：
  - 定义：粒子被 Alfvén 波扰动磁场散射，改变运动方向。
  - 原文语境：本文 §1 引述 'Alfvén waves...scattered the energetic particles, reduce their streaming to roughly the Alfvén speed'（来自 Greenstadt 1975 地球弓激波观测）。

- **Alfvén speed**：
  - 定义：$v_A = B/\sqrt{\mu_0 \rho}$，电磁波在等离子体中的特征速度。
  - 原文语境：作为 streaming instability 与上游波速修正的关键参数（§2 末、§3.4）。

- **resonant wave-particle interaction**：
  - 定义：粒子的回旋半径与 Alfvén 波波长匹配（$\lambda \approx r_L$）时最有效的能量交换。
  - 原文语境：本文 §3.1 描述 'the wavelength of Alfvén waves excited by the streaming particles is approximately equal to the particle gyroradius'。

### 0.4 谱与观测

- **spectral index**：
  - 定义：幂律谱 $N(E) \propto E^{-\mu}$ 中的 $\mu$。微分谱指数对应 $dN/dE$，积分谱指数对应 $N(>E)$。
  - 原文语境：本文核心结果 $\mu = 2$–$2.5$，与银河宇宙线观测 $\mu \approx 2.5$ 吻合。

- **critical energy** ($E_{\rm crit}$)：
  - 定义：加速机制能够达到的能量上限。超过 $E_{\rm crit}$，谱指数变陡（弯曲）。
  - 原文语境：本文 §3.4 给出 $E_{\rm crit} \sim 3.5 \times 10^{12}$ eV（典型年轻 SNR 参数）。

- **cosmic ray residence time**：
  - 定义：CR 在银河系内被束缚的平均时间，$\sim 10^7$ 年。
  - 原文语境：本文未明确讨论，但 SNR 累积贡献需求中暗示（§4 跨章节分析）。

### 0.5 方程量

- **escape probability** ($\eta$)：
  - 定义：粒子每次穿越激波后从下游区逃逸的概率。$\eta = 4u_2/v$（本文核心，本文方程 3）。
  - 原文语境：'the probability $\eta$ of particle escape at downstream = $4u_2/v$'（§2）。

- **diffusion coefficient** ($D$)：
  - 定义：粒子在散射介质中的扩散率。$D \propto v/(\mathcal{F})$ 与波振幅成反比（本文方程 14）。
  - 原文语境：本文核心自洽方程的一个变量。

- **Alfvén wave energy density** ($\mathcal{F}$)：
  - 定义：单位体积内 Alfvén 波能量与磁场能量比。
  - 原文语境：本文方程 15 的核心变量，粒子驱动 + 阻尼竞争。

## C. 关键长难句分析

**§1 第 2 段（事实复合句）**：
> 'Particles which have energies high enough for their gyroradii to be much larger than the thickness of the shock front will tend to be of the order of, or less than, the gyroradius of a thermal proton (Boyd & Sanderson 1969), as is observed to be the case for the Earth's bow shock (Formisano 1974).'

- 句型：主句 + 'as is observed to be the case for...' 状语从句
- 逻辑：电离热质子（Boyd-Sanderson）作为地球弓激波（Formisano）的解释 → 类比到天体激波
- 关键洞察：本文的物理假设（粒子可穿越激波）建立在已被实验验证的电离物理基础上

**§2 中心句（机制定义）**：
> 'The energy $E_l$ of a particle which has performed $k$ cycles, passing from upstream to downstream and back to upstream, performs a further cycle and has its energy increased to $E_{k+1}$'

- 句型：关系从句嵌套（which has performed...passing...）
- 物理：循环式的能量累积是 DSA 机制的核心，几何必然 → 幂律

**§3 关键物理论断**：
> 'A critical energy $E_{\rm crit} \sim 3.5 \times 10^{12}$ eV is identified, above which the spectral index steepens'

- 物理含义：超出 $E_{\rm crit}$ 后，因波阻尼与粒子驱动失衡，谱形态改变
- 与 Bell 2004 Bell instability 的衔接：Bell 2004 通过完全非线性分析修正了阈值，但概念框架已在本文建立

## D. 引用文献（本文依赖的内部 B 类术语定义出处）

- **Bell 1978b, 1978c**（MNRAS 182 后续 Part II, III）：非线效应、垂直激波
- **Wentzel 1974**：上游 Alfvén 波激发的早期理论
- **Skilling 1975a, b, c**：粒子-波相互作用、波阻尼
- **Kulsrud & Cesarsky 1971**：中性粒子-波耦合
- **Chin & Wentzel 1972**：声波损失
- **Jokipii 1966**：超热粒子加速的物理类比
- **Fisk 1971**：行星际激波中的物理图像
- **Greenstadt 1975**：地球弓激波上游湍流观测
- **Formisano 1974**：地球弓激波数据
- **Boyd & Sanderson 1969**：电离热质子物理

