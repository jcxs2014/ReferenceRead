---
chapter: 5
title: Open questions and future directions
pages: "188–194"
sections:
  - "5.1 Plasma physics and cosmic ray transport challenges"
  - "5.2 Astrophysical challenges"
  - "5.3 Concluding remarks"
related_chapters:
  prev: 04_observational_signatures
  next: 98_vocabulary
status: done
---

> 本章属于：Cosmic ray feedback in galaxies and galaxy clusters (Ruszkowski & Pfrommer 2023)
>
> 上一章：`04_observational_signatures.md`
>
> 下一章：`98_vocabulary.md`

# 5. Open questions and future directions — CR 反馈领域的前景与挑战

## 5.1 本节核心内容

[FACT] §5 Open questions and future directions 覆盖 pp. 188–194（约 7 页），是全文的**收尾 + 展望章节**。三个子节依次覆盖：

1. §5.1 Plasma physics and cosmic ray transport challenges（等离子体物理 + CR 传输理论挑战）
2. §5.2 Astrophysical challenges（天体物理挑战）
3. §5.3 Concluding remarks（结论）

[FACT] §5.1 本身包含 4 个子子节：
- 5.1.1 Plasma physics challenges
- 5.1.2 Building a self-consistent cosmic ray transport theory
- 5.1.3 Incorporating complete theory of CR transport in MHD simulations
- 5.1.4 Cosmic ray transport and non-thermal signatures in the Milky Way and other galaxies

[FACT] §5.2 本身包含 6 个子子节：
- 5.2.1 Effective CR transport near sources
- 5.2.2 Interactions of low-energy CRs with molecular clouds
- 5.2.3 Launching galactic winds
- 5.2.4 Impact of CRs on the CGM
- 5.2.5 CRs and AGN jet feedback
- 5.2.6 Impact of CRs on the reionization of the Universe

[INTERPRETATION] §5 的**结构镜像**了 §2–§4 的组织逻辑：§5.1 对应 §2 Physics（理论挑战），§5.2 对应 §3 Astrophysical systems（应用挑战），然后 §5.3 是全局收束。每一节都按照"从微观到宏观、从基础物理到天体物理应用"的顺序排列，**与正文的章节结构一一对应**。

## 5.2 原文内容

### 5.2.1 §5 开篇 (p. 188)

[FACT] 论文开篇总结过去十年 CR 反馈领域取得的**两大进展**：

- **理论进展**：CR 传输的首原理建模、galactic wind launching 中的应用、AGN feedback 中的应用
- **观测进展**：LOFAR、MeerKAT、Jansky VLA、Fermi、H.E.S.S.、VERITAS、Voyager 等观测台的数据，以及 SKA、CTA、JWST 等新/未来任务

[FACT] 论文指出，要"consolidate our picture of how CRs dynamically impact the formation and evolution of galaxies and galaxy clusters"，仍需解决以下 open problems。这些问题的列出**镜像了全文的章节顺序**——先从 plasma physics 开始，再逐步过渡到从小尺度 ISM 模拟到宇宙学结构形成模拟。

### 5.2.2 §5.1 Plasma physics and cosmic ray transport challenges (pp. 188–190)

[FACT] §5.1.1 **Plasma physics challenges**：

[FACT] 论文指出用首原理 PIC 代码模拟 CR 驱动不稳定性的**巨大数值挑战**：

- **时空尺度分离**：$n_{\text{cr}}/n_i \sim 10^{-9}$（CR–热背景数密度比），$v_A/c = \omega_{i,0}/\omega_i \sim 10^{-4}$（Alfvén 速度与光速之比，ISM 中）
- 需要**fluid-PIC 代码**可靠模拟 Landau damping（Lemmerz et al. 2023）
- 目的：(i) 研究背景等离子体密度/磁场不均匀性对不稳定增长率、微观 CR–波散射率、CR 传输描述的影响；(ii) 理解 CR 驱动不稳定性与波阻尼（非线性 Landau damping + ion-neutral damping）的非线性饱和机制

[FACT] **Extended MHD 模型**（含 Landau closures）的方向：

- Fluid-PIC 模拟的 coarse graining 来推导有效 CR 散射率和传输系数
- 采用 magnetic fusion plasma 的算法，纳入 weakly collisional 介质的**分布函数各向异性**
- 各向异性激发微尺度不稳定性，为粒子传输提供额外散射

[FACT] §5.1.2 **Building a self-consistent cosmic ray transport theory**：

[FACT] 论文指出**观测与理论之间的张力**：

> AMS-02 观测的主/次 CR 谱（Fig. 37）可以被 leaky box 模型 + 经验幂律 $D \propto R^{1/3}$ 成功描述（§4.1.2），但当前微观物理理论（包括 streaming instability 的 self-confinement 和 extrinsic turbulence 的 MHD fast mode cascade）与观测不一致（Kempski & Quataert 2022）。

[FACT] 可能的解决方向：
- **组合机制**：CR self-confinement + CR 在 extrinsic turbulent modes 上的散射，可能重现主要 CR 谱趋势和 B/C 比
- **理论扩展**：纳入新的 CR 驱动不稳定性（Shalaby et al. 2021, 2023）
- **Turbulent intermittency + 小尺度场反转**：可能使 CR 传输从 Brownian motion 变为**非 Brownian**，直至磁场相干尺度（Kempski et al. 2023；Lemoine 2023）

[FACT] §5.1.3 **Incorporating complete theory of CR transport in MHD simulations**：

[FACT] 关键下一步：发展**完整的 CR 传输理论**，改进 CR 流体模型中的动力学物理建模，需要：
- 纳入所有相关 CR 驱动不稳定性
- 对 CR 动量谱和提供 CR 散射的 plasma waves 分别进行谱描述
- 计算效率足以应用于 3D ISM 模拟和整个星系模拟

[FACT] §5.1.4 **CR transport and non-thermal signatures in the Milky Way and other galaxies**：

[FACT] 改进后的 CR 流体理论将支持：
- 自洽的**谱分辨 CR 流体模拟**（spectral CR hydrodynamics），使用 two-moment CR transport
- 在银河系和河外星系中解释 local CR 数据（H、He、B、C、O、电子）和非热发射（射电 + γ 射线）
- 与观测对照（FIR–radio、FIR–γ 射线相关性、individual non-thermal spectra）揭示理论弱点
- **Fermi bubbles 的 leptonic vs. hadronic 起源**问题的解决
- 为 SKA 射电望远镜和 CTA γ 射线观测台做出可靠预测
- 量化恒星形成星系对 isotropic extra-galactic γ 射线背景的贡献
- **校准 calorimetric fraction**：CR 能量中辐射损失部分 vs. 可用于反馈的部分

### 5.2.3 §5.2 Astrophysical challenges (pp. 190–194)

[FACT] §5.2.1 **Effective CR transport near sources**：

[FACT] CR 在 SNR 附近的传输被认为高度空间和时间变化：
- Schroer et al. (2022) 理论和 Jacobs et al. (2023) 观测暗示 CR 在 SN 附近**传输严重抑制**
- 后果：(i) 显著抑制 ISM 密度概率分布函数的高密度端；(ii) 通过增大 local CR 压力梯度、增加 Jeans mass 抑制 local fragmentation；(iii) 改变恒星形成率和星系形态（Semenov et al. 2021）
- 相反，ion-neutral damping 在冷/密环境中增强 CR 传输速度（Armillotta et al. 2022）

[FACT] 核心挑战：**阐明 CR 如何从 injection site（紧密 confined）迁移到更大尺度的 ISM/星系尺度（传输更快）**。

[FACT] §5.2.2 **Interactions of low-energy CRs with molecular clouds**：

[FACT] 关键挑战：建立能预测**低能 CR 穿透分子云**的能量依赖行为的自洽理论。

[FACT] 当前模型**系统性地低估**了 CR 电离率（即使假设 free-streaming CR 深度穿透分子云）。模型无法自洽地连接低能（$2–10$ MeV）质子谱与 GeV 以上的 CR 质子谱。

[FACT] 可能解决方案：
- 改进 CR 传输模型
- 考虑分子云**内部**低能 CR 源（如原恒星喷流激波）
- 研究 ambipolar diffusion 率和尘埃形成

[FACT] §5.2.3 **Launching galactic winds**：

[FACT] **Ion-neutral damping 对 wind launching 的影响**：
- Kulsrud & Pearce (1969)；Blasi (2018) 指出 ion-neutral 摩擦导致 Alfvén waves 强阻尼
- 在 $n \gtrsim 10^{-2}$ cm$^{-3}$（冷/温中性相 ISM）中，ion-neutral damping 主导，导致快速 CR 扩散和均匀的 CR 压力分布（Armillotta et al. 2021）
- 在盘以上低密度区域（温电离/热相），ion-neutral damping 减弱，CR 散射率增加，宏观传输速度降低，**CR–气体动量转移增大**

[FACT] 关键 open question：这种 dynamical re-coupling 是否与观测到的**低水平 CR anisotropy** 一致？

[FACT] **CR bottlenecks**：
- Streaming CRs 使声波不稳定 → 形成 shocks → 产生密度不连续和 peaks（CR bottlenecks）
- 结果：CR 呈 staircase-like 分布，只在 stair jumps 处对气体施加强力并加热
- 即使在 isothermal 情况下，分层大气中的 adiabatic 声波在 CR streaming 主导区也是不稳定的（Tsung et al. 2022；Quataert et al. 2022a；Huang et al. 2022）
- 关键工作：**扩展到 3D 分层大气 + 辐射冷却**的 CR bottleneck 模拟

[FACT] **CR 与辐射流体动力学耦合**：
- 下一代全星系模型需要**同时耦合** two-moment CR hydrodynamics + radiation hydrodynamics
- 需要包括非平衡冷却、光电子加热、辐射转移、SN 能量注入
- 分辨率需足够支持小尺度 dynamo 增长磁场
- 目标：**用首原理反馈取代经验反馈参数化**，特别是矮星系 cosmological simulations

[FACT] §5.2.4 **Impact of CRs on the CGM**：

[FACT] CR 在 CGM 中的压力支撑**强烈依赖 CR 传输物理**：
- **慢传输**：盘内 CR 压力梯度显著，可驱动外流，但 catastrophic inelastic CR energy losses 限制 wind driving
- **快传输**：CR 在盘中停留时间不足，无法有效加速风

[FACT] 因此存在一个**最优 CR 传输速度范围**，能同时最大化 CR 对 wind driving 的影响和 CGM 中的 CR 压力支撑（Ruszkowski et al. 2017b；Hopkins et al. 2021b）。

[FACT] 模型与观测的张力：
- 慢 CR 传输模式下，γ 射线发射可能超过观测上限
- X 射线属性：CR 反馈模型接近 stellar mass vs. soft X-ray luminosity 关系，但在低 SFR 区间**低估 X 射线发射**
- 如果 CR 提供显著 CGM 压力支撑，热气体将更冷、密度分布更平滑，金属发射/吸收线特征将不同

[FACT] 解决方向：
- (i) 研究 SN 附近 CR 扩散抑制的影响（可能协调 CR 和气体分布的 anti-correlation，降低 γ 射线光度）
- (ii) 系统研究磁场放大数值方法对 CR streaming loss 的影响
- (iii) 建立 CGM 条件下 CR 散射率的自洽理论
- (iv) 用改进的 CR 流体模型进行 cosmological simulations

[FACT] §5.2.5 **Cosmic rays and AGN jet feedback**：

[FACT] AGN 相对论喷流加速的 CR 质子成分：
- CR 从 radio bubbles 逃逸并 streaming 到 ICM
- 通过激发/阻尼 Alfvén waves 加热等离子体
- 能量沉积可能抵消 cool core 星系团的辐射损失

[FACT] 关键 challenge：**识别不同加热机制（CR、turbulent mixing、shock/sound wave dissipation）的相对重要性**，以及 cool core/non-cool core 二态性的物理原因。

[FACT] CR jet feedback 模型需要与**多波段观测约束**对照：射电、毫米波 SZ emission、Hα、X 射线、γ 射线。

[FACT] §5.2.6 **Impact of CRs on the reionization of the Universe**：

[FACT] 一个尚未被充分探索的方向：**CR 对宇宙再电离的潜在影响**。

[FACT] 物理图像：$z \sim 20–40$ 时的第一代（Population III）恒星形成中，引力坍缩产生 strong collisionless shocks，加速 CR，CR 电离中性气体 → 产生自由电子 → 催化分子氢（H₂）形成 → 加速冷却 → 促进下一代恒星形成（Jasche et al. 2007）。

[FACT] 论文指出，近期在谱分辨和空间分辨 CR 流体模拟方面的进展使**重新审视这些早期结果**成为可能。

### 5.2.4 §5.3 Concluding remarks (p. 194)

[FACT] 论文最后总结：
- 过去十年 CR 反馈领域取得"extraordinary progress"
- 这些进展**同时引发了更多问题**，为后续研究开辟了道路
- 预期该领域在未来十年将更加活跃

[FACT] **Acknowledgements** 感谢 referee Ellen Zweibel、Timon Thomas、Mohamad Shalaby、Lukas Platz、Vladimir Lenok、David Maurin、Tom Abel、Andrea Botteon、Hsiao-Wen Chen、Martin Lemoine。

[FACT] **Funding**：MR 由 NASA grants 80NSSC20K1541, 80NSSC20K1583 和 NSF AST-1715140, AST-2009227 支持；CP 由 ERC-AdG grant PICOGAL-101019746 支持。

## 5.3 关键公式

$$
\boxed{\frac{n_{\text{cr}}}{n_i} \sim 10^{-9}}
\quad \text{（§5.1.1, CR–热背景数密度比，ISM）}
$$

$$
\boxed{\frac{v_A}{c} = \frac{\omega_{i,0}}{\omega_i} \sim 10^{-4}}
\quad \text{（§5.1.1, Alfvén 速度与光速比，ISM）}
$$

$$
\boxed{D \propto R^{1/3} \;\;\text{（phenomenological, leaky box）}}
\quad \text{vs.}
\quad \boxed{D_{\text{microphysical}} \neq R^{1/3} \;\;\text{（当前理论预测）}}
\quad \text{（§5.1.2 的核心张力）}
$$

$$
\boxed{\text{Optimal CR transport speed} \;\sim\; \mathcal{D}^*}
\quad \text{（§5.2.4, 同时最大化 wind driving + CGM pressure support）}
$$

$$
\boxed{z_{\text{reion}} \sim 20–40}
\quad \text{（§5.2.6, CR 对再电离影响的关键红移区间）}
$$

## 5.4 关键参数

| 参数 | 数值 | 单位 | 出处 |
|------|------|------|------|
| CR–热背景数密度比 | $\sim 10^{-9}$ | — | §5.1.1 |
| Alfvén 速度/光速 | $\sim 10^{-4}$ | — | §5.1.1 |
| CR 谱（AMS）指数 | $1/3$ | — | §5.1.2 |
| 低能 CR 谱区间 | $2–10$ | MeV | §5.2.2 |
| Ion-neutral damping 主导密度 | $\gtrsim 10^{-2}$ | cm$^{-3}$ | §5.2.3 |
| 再电离关键红移 | $z \sim 20–40$ | — | §5.2.6 |
| 未来十年预期活跃领域 | — | — | §5.3 |

## 5.5 图表分析

§5 未直接引入新的 Figure 或 Table。论文在这一节主要进行**定性总结 + 展望**，不涉及新的观测数据展示。

[FACT] §5.1.2 中提到 AMS-02 数据（Fig. 37, §4.1）作为观测参考，但 §5 本身未新引入图表。

[FACT] §5.2.6 中引用 Jasche et al. (2007) 的 Population III 恒星形成 CR 模型，但 §5 本身未新引入相关图表。

## 5.6 作者的逻辑

```
§5 开篇 [总结] 十年进展（理论 + 观测）
  → §5.1 [物理挑战] PIC 模拟尺度分离 → CR 传输理论与观测张力 → MHD 实现挑战 → 应用至 Milky Way
    → §5.2 [天体物理挑战] 源附近 CR 传输 → 低能 CR 与分子云 → 银河风启动 → CGM → AGN 喷流 → 再电离
      → §5.3 [结论] 进展 + 新问题 + 未来展望
```

[INTERPRETATION] §5 的逻辑是"从**基础物理**到**天体物理应用**再到**宇宙学尺度**"：

1. §5.1 讨论"我们目前无法从首原理解释 CR 传输理论"——这是**底层问题**
2. §5.2 讨论"由于 §5.1 的问题，我们在以下六个天体物理场景中无法做出可靠预测"
3. §5.2.6 将讨论扩展到**宇宙学尺度**（再电离）
4. §5.3 收束，强调"进展 = 新问题"

[INTERPRETATION] §5 的结构与 §2–§4 完全镜像，这体现作者刻意让读者"顺着 §1 → §5 读一遍，再顺着 §5 反向重读一遍来发现所有 open problems"的阅读策略。

## 5.7 我的理解

### 5.7.1 [INTERPRETATION] §5 的"核心张力"——微观理论与宏观观测的脱节

§5.1.2 揭示的**根本矛盾**：

```
宏观观测（AMS B/C 比, D ∝ R^{1/3}）
        ↑  无法解释
微观理论（streaming instability + extrinsic turbulence）
```

这一脱节意味着：
- 当前 CR 反馈模型中的**扩散系数参数化**（$D = D_0 \times (E/E_0)^{1/3}$）是**经验性的**，不是从首原理推导的
- 因此 §3 Astrophysical systems 中所有涉及 CR 扩散的数值模拟结论，其**绝对数值**依赖这个经验参数化
- 未来如果微观理论给出不同的 $D(E)$ 依赖，§3 的许多结论需要重新校准

[CRITIQUE] 这是全篇论文中**最关键的未解决理论问题**——它直接影响 CR 反馈在星系演化中的定量重要性判断。

### 5.7.2 [CRITIQUE] PIC 模拟的尺度分离问题

[CRITIQUE] §5.1.1 给出的 $n_{\text{cr}}/n_i \sim 10^{-9}$ 和 $v_A/c \sim 10^{-4}$ 意味着 PIC 模拟需要：

- 空间分辨率：足够分辨 CR 回旋半径 $\sim 10^3$–$10^4$ km（ISM 中）
- 时间分辨率：足够分辨 Alfvén 波周期
- 粒子数：至少 $\sim 10^9$ 个粒子来正确采样 CR 分布

[CRITIQUE] 这些要求使**全 3D PIC 模拟**在可预见的未来仍不可行。论文提出的 fluid-PIC + extended MHD 路线是务实的，但仍需要解决 Landau damping 的**closure**问题——目前 magnetic fusion 中的 Landau closure 假设弱碰撞，但 astrophysical 等离子体中 collisionality 更低，可能需要更复杂的 closure。

### 5.7.3 [CRITIQUE] "Optimal CR transport speed" 的物理论证

[CRITIQUE] §5.2.4 指出存在"optimal CR transport speed"，同时最大化 wind driving 和 CGM pressure support。这个"optimal"的物理来源是：

| CR 传输速度 | 风驱动效应 | CGM 压力支撑 |
|-------------|-----------|--------------|
| 慢 | 盘内 CR 停留时间长 → 风驱动强；但 inelastic loss 多 | CR 积累在盘附近 → CGM 支撑弱 |
| 快 | CR 逃逸快 → 风驱动弱 | CR 充满 CGM → 支撑强 |
| **最优** | **折中** | **折中** |

[CRITIQUE] 这个"optimal"依赖于 §2.4 中给出的 CR 冷却时标（pp 碰撞）与 §2.3 中给出的扩散系数的**竞争**。但这两个参数都是**经验性**的（见 §5.7.1 的讨论），因此"optimal"的具体数值也带有相同的经验性。

### 5.7.4 [INTERPRETATION] CR 在宇宙再电离中的角色

[INTERPRETATION] §5.2.6 提出的 CR 在再电离中的作用，是论文中**最具前瞻性**的 open question：

1. $z \sim 20–40$ 时，第一代恒星形成的激波可以加速 CR 到 GeV–TeV 能量
2. CR 电离中性气体 → 产生自由电子 → 催化 H₂ 形成（通过 $e^- + \text{H}_2^+ \to \text{H} + \text{H}$ 和 $e^- + \text{H}_2 \to \text{H} + \text{H}^-$ 等反应）
3. H₂ 增多 → 冷却加速 → 下一代恒星形成

[CRITIQUE] Jasche et al. (2007) 的早期结果使用简化的 CR 谱和传输模型。论文指出近期谱分辨 CR 流体模拟的进展使**重新审视**这些结果成为可能。如果 CR 确实在再电离中起重要作用，这将是 CR 反馈理论从"星系/星系团尺度"扩展到**宇宙学尺度**的重大突破。

### 5.7.5 [CRITIQUE] §5 的"问题清单"性质

[CRITIQUE] §5 本质上是**open questions 的清单**，而非"解决方案的路线图"。每节列出问题但没有给出明确的优先级或时间线。对于研究者而言，需要结合文献进一步判断哪些是"最近可解"、哪些是"远期目标"：

| 可解性 | 问题 | 预计时间 |
|--------|------|----------|
| **近期（1–3 年）** | Fluid-PIC 代码发展、Landau closure 改进、CR bottleneck 3D 模拟 | 近年 |
| **中期（3–5 年）** | 谱分辨 CR 流体模型（Girichidis et al. 2023）、CGM CR 观测约束 | 近几年 |
| **远期（5–10 年）** | 再电离中的 CR 作用、AGN–CR 耦合定量模型、全 3D PIC | 十余年 |

## 5.8 潜在问题与值得关注的地方

### 5.8.1 [CRITIQUE] §5.1.2 中 B/C 比与微观理论的**张力程度**

[CRITIQUE] 论文引用 Kempski & Quataert (2022) 说"当前微观理论与观测不一致"，但没有给出定量比较：$D_{\text{theory}}$ 与 $D_{\text{AMS}}$ 的偏离是 20%、50% 还是数量级差异？这种定量信息对判断问题严重性至关重要。

### 5.8.2 [CRITIQUE] "Extended MHD" 模型的适用边界

[CRITIQUE] §5.1.1 提到 extended MHD + Landau closures 从 magnetic fusion 借鉴。但 fusion plasma 的参数空间（$\beta \sim 0.01–1$，$T \sim$ keV–MeV）与 astrophysical plasma（$\beta \sim 0.01–10^6$，$T \sim$ eV–keV）有本质不同。Extended MHD 在 astrophysical 极端参数下的适用性**未经充分验证**。

### 5.8.3 [CRITIQUE] 矮星系中 CR 反馈的定量结论

[CRITIQUE] §3.3 提到 Girichidis et al. (2023) 发现矮星系中 mass loading factor 可下降 4 倍。但 §5.2 未进一步讨论矮星系在 CR 反馈中的**特殊地位**：

- 矮星系的 CR 冷却时标更短（$n \sim 1$ cm$^{-3}$ → $t_{\text{pp}} \sim 10^6$ yr）
- 矮星系的磁通量管几何可能不同
- 矮星系的 ion-neutral friction 更强（中性气体比例高）

这些差异使矮星系成为测试 CR 反馈理论的**关键实验室**，但 §5 未明确指出。

### 5.8.4 [CRITIQUE] §5.2.6 再电离方向与全篇的联系

[CRITIQUE] §5.2.6 提出的 CR 在再电离中的作用与 §2–§4 的 CR 反馈主线联系较弱：

- §2 Physics：CR 加速和传输机制可以推广到 $z \sim 20–40$ 的激波环境
- §3 Astrophysical systems：CR 电离低能效应（§3.1）与再电离中的 H₂ 催化直接相关
- §4 Observational signatures：再电离 CR 的直接观测目前不可行，但 21-cm signal 和 JWST 对 Pop III 星系的观测可能间接约束

[CRITIQUE] 论文在这里提出再电离方向，但没有说明"这一方向如何与 §2–§4 中已经建立的 CR 传输理论、扩散系数经验参数化、观测约束形成一致的图景"。这是 §5.2.6 的一个**论述不足**之处。

### 5.8.5 §5 与全篇的接口

[INTERPRETATION] §5 的每一个 open problem 都对应 §1–§4 中的某个**已确立结果**：

| §5 Open Problem | 对应的 §2–§4 内容 |
|-----------------|-------------------|
| §5.1.1 PIC 模拟尺度分离 | §2.1 中的 streaming instability 线性增长率 |
| §5.1.2 微观理论与观测张力 | §4.1 B/C 比 + §2.5 Kolmogorov 扩散 |
| §5.2.1 CR 源附近传输 | §3.2 CR 驱动风模型 |
| §5.2.3 CR bottleneck | §3.2 Eq. 62 风方程 |
| §5.2.4 CGM CR 压力支撑 | §3.4 冷气体 + §4.4 CGM 观测 |
| §5.2.5 AGN jet feedback | §3.5 AGN 加热机制 |
| §5.2.6 再电离 | §3.1 CR 电离低能效应 |

---

## 元数据

```yaml
chapter: 5
pages: "188–194"
subsections: ["5.1", "5.2", "5.3"]
key_formulas:
  - "n_cr / n_i ~ 10^{-9} [PIC 尺度分离]"
  - "v_A / c ~ 10^{-4} [PIC 尺度分离]"
  - "D ∝ R^{1/3} [phenomenological, leaky box]"
  - "z_reion ~ 20–40 [CR 对再电离的影响]"
keywords:
  - PIC simulation
  - fluid-PIC
  - extended MHD
  - Landau closure
  - CR bottleneck
  - CR self-confinement
  - non-Brownian transport
  - optimal CR transport speed
  - reionization
references_internal:
  prev_chapter: 04_observational_signatures
  next_chapter: 98_vocabulary
```

**引用页码**：全文引用基于 *A&A Reviews 31:4 (2023)*，pp. 188–194。
