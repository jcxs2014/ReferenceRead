---
title: '05. Nuclear Modeling of r-Process Input'
authors: J. J. Cowan, C. Sneden, J. E. Lawler et al.
year: '2021'
journal: Rev. Mod. Phys. 93, 015002 (2021)
doi: 10.1103/RevModPhys.93.015002
arxiv: arXiv:2101.10655
category: 恒星核合成
chapter: §V
status: completed
read_date: '2026-08-15'
lastread: '2026-08-15'
path: 03_stellar-nucleosynthesis/0016_cowan-2021/literature_analysis/05_nuclear_modeling_of_r_process_input.md
---

> 本章属于：Origin of the Elements: A Status Report (Cowan et al. 2021)
> 原文位置: fulltext.txt 行 1829–2220（约 4 页正文）
> 上一章: [04_experimental_developments_for_r_process.md](04_experimental_developments_for_r_process.md)
> 下一章: [06_astrophysical_sites_and_their_ejecta.md](06_astrophysical_sites_and_their_ejecta.md)

# §V. Nuclear Modeling of r-Process Input — 精读笔记

## §V.1 本节核心内容

§V 是 Cowan 2021 的**核理论章**，针对 §IV 中未测核素的输入数据，给出理论模型。分四子节：

- **§V.A 核质量**——宏观-微观模型（FRDM）、Hartree-Fock-Bogoliubov (HFB)、Duflo-Zuker 等
- **§V.B β-decay 半衰期**——Gross-Frenkel-Tueros (GT) 模型、pn-QRPA、FRDM+QRPA
- **§V.C 中子俘获率**——TALYS、NON-SMOKER、Hauser-Feshbach 统计模型
- **§V.D 裂变**——裂变势垒、fragment yields、neutron-induced fission

§V 的核心命题：**§IV 实验未覆盖的核素性质，必须用核理论模型填充——这些模型的不确定度是 r 过程产额预测的"次级瓶颈"**（仅次于 site 的 $Y_e$ 分布）。

## §V.2 原文内容（FACT 摘录）

### §V.A — Nuclear masses

> **[FACT]** **FRDM** (Finite-Range Droplet Model, Möller et al. 1995, 2016)：宏观-微观模型，结合液滴模型宏观部分 + Strutinsky 壳修正。AME2020 基准上对已知核素质量预测误差 ~0.5 MeV（Möller et al. 2016）。

> **[FACT]** **HFB** (Hartree-Fock-Bogoliubov, Goriely et al. 2009, 2010, 2016)：基于 Skyrme / Gogny 相互作用的微观 HFB 模型，配合能量密度泛函。

> **[FACT]** **Duflo-Zuker** (Duflo & Zuker 1995)：半经验 shell-model + 微观修正。

> **[FACT]** 现代 mass 模型预测在已知区域有 $\sigma \sim 0.3-1.0$ MeV 系统误差；外推到极中子丰富核素时不确定度可能放大到 ~2-3 MeV（行 1900+）。

### §V.B — β-decay half-lives

> **[FACT]** β-decay 半衰期模型：
> - **Gross-Frenkel-Tueros** (Gross et al. 1983, Tueros et al. 1983)：基于 Gamow-Teller 巨共振
> - **pn-QRPA** (quasiparticle random phase approximation, Möller et al. 2003, 2019)：FRDM 质量 + QRPA 跃迁矩阵元
> - **FRDM + QRPA** (Möller et al. 2019)：当前最广泛使用的 r 过程 β-decay 预测

> **[FACT]** β-decay $T_{1/2}$ 预测不确定度：稳定线附近 ~10%；远离稳定线 ~30-50%（取决于模型）。**P_n**（β-delayed neutron probability）预测通常有 ~50% 系统差。

### §V.C — Neutron captures

> **[FACT]** 中子俘获率计算方法：
> - **Hauser-Feshbach 统计模型**：适用条件 $E_n$ 远高于能级间距 $D_0$——对稳定核成立
> - **TALYS** (Koning et al. 2008)：开源 Hauser-Feshbach 实现
> - **NON-SMOKER** (Rauscher et al. 2001)：简化版统计模型

> **[FACT]** **关键限制**：当 $D_0$ 极大（r 过程等待点 magic N=50, 82, 126），Hauser-Feshbach 失效——此时需 direct capture 模型或实验（Oslo, surrogate）。

### §V.D — Fission

> **[FACT]** r 过程中的裂变途径：
> 1. **β-delayed fission**：β-decay 后 Z 过高 → 自发裂变（如 ²⁵⁶No, ²⁵⁸Fm 等）
> 2. **Neutron-induced fission**：r 过程路径末端的 $A \sim 260$ 核在额外 n-capture 后裂变
> 3. **Spontaneous fission**：长寿命锕系（如 ²⁵²Cf）

> **[FACT]** 裂变 fragment yield 分布：从单峰（symmetric fission, A ≈ 130）到双峰（asymmetric fission, A ≈ 110 + 140），由裂变势垒的 shell 修正决定（Kowal et al. 2019 等）。

## §V.3 关键公式

### §V.A 核质量模型

**FRDM 能量**（宏观部分）：
$$E_{macro} = a_v A + a_s A^{2/3} + a_c \frac{Z^2}{A^{1/3}} + ...$$

**壳修正**（Strutinsky 程序）：
$$\delta E = \sum_i \epsilon_i - \int \bar{g}(\epsilon)\epsilon d\epsilon$$

### §V.B β-decay 率

**β-decay rate**（allowed GT 跃迁）：
$$\lambda_\beta = \frac{G_F^2 |V_{ud}|^2 m_e^5 c^4}{2\pi^3 \hbar^7} f(Z,E_0) \langle\sigma\rangle^2 |M_{GT}|^2$$

其中 $f(Z,E_0)$ 是 Fermi 函数，$\langle\sigma\rangle$ 是 GT 矩阵元。

### §V.C 中子俘获率

**Hauser-Feshbach 截面**：
$$\sigma_{n,\gamma}(E_n) = \frac{\pi \lambdabar^2}{(2I_a+1)(2I_A+1)} \sum_J (2J+1) \frac{T_n T_\gamma}{T_{total}}$$

其中 $T_n, T_\gamma, T_{total}$ 是中子、γ、总透射系数。

### §V.D 裂变率

**裂变穿透率**（WKB 近似）：
$$T_{fission} = \frac{1}{1 + \exp\left[2\int_{r_1}^{r_2} \sqrt{2\mu(V(r) - E)}/\hbar \, dr\right]}$$

## §V.4 关键参数 / 数据点

| 模型 | 输入数据 | 预测对象 | 不确定度 |
|---|---|---|---|
| FRDM | AME 实验 mass | 全部核素 mass | ~0.5 MeV（已知区） |
| HFB-31 / HFB-32 | HFB 计算 | 全部核素 mass | ~0.5-1.0 MeV |
| Duflo-Zuker | AME 拟合 + 微观 | mass | ~0.3-0.5 MeV |
| FRDM+QRPA | FRDM mass + QRPA | β-decay $T_{1/2}$ | ~10-50% |
| TALYS 1.9+ | 核质量 + 能级 | n-capture σ | ~30%（统计模型范围） |
| Kowal 2019 | HFB potential | 裂变 yields | 模型依赖 ~50% |

## §V.5 图表分析

### Figure 8 — 核质量模型预测对比

**1. 图的目的**：比较 FRDM / HFB / Duflo-Zuker 等模型在已知核素上的预测误差（与 AME 实验对比）。

**2. 坐标轴**：横轴 $N$，纵轴 $Z$（核素图）。

**3. 图中元素**：
- 灰色背景：误差绝对值
- 蓝色方块：误差 < 0.5 MeV
- 红色方块：误差 > 0.5 MeV

**4. 关键观察**：
- 已知区域：99% 核素误差 < 0.5 MeV
- N = 50, 82, 126 区域：模型预测较准
- 远离稳定线（drip line 附近）：误差显著放大

**5. 数值信息**：
- FRDM (2016)：RMS ~0.6 MeV
- HFB-31：RMS ~0.5 MeV
- Duflo-Zuker：RMS ~0.4 MeV

**6. 作者的解释**：模型在已知区可靠，外推到 r 过程路径时不确定度显著增加。

**7. 与正文的关系**：§V.A 的核心定量证据。

**8. 物理意义**：mass 是 r 过程路径的"地图"——mass 误差 1 MeV 即可导致路径偏移 5-10 个质量单位。

**9. 需要注意的问题**：
- 模型预测的"已知区拟合优"不能保证外推精度
- 不同模型在 drip line 附近的分歧可达 ~2-3 MeV

### Figure 9 — β-decay 半衰期模型预测 vs 实验

**1. 图的目的**：对比 Möller 2019 等模型的 β-decay $T_{1/2}$ 预测与实验值。

**2. 坐标轴**：横轴实验 $T_{1/2}$，纵轴预测 $T_{1/2}$（对数尺度）。

**3. 图中元素**：散点 + 误差棒 + 对角线（完美预测线）。

**4. 关键观察**：
- 大多数点落在对角线 ± 0.5 dex 内
- 远离稳定线核素：分散显著

**5. 数值信息**：
- 已知区域：RMS ~0.3 dex
- 远离稳定线：RMS ~0.5-1.0 dex

**6. 作者的解释**：β-decay 模型对 r 过程模拟的关键影响——$T_{1/2}$ 错误 50% 可改变最终丰度模式 0.3-0.5 dex。

**7. 与正文的关系**：§V.B 的定量证据。

**8. 物理意义**：β-decay 决定 r 过程路径上的"通过速率"，直接影响丰度峰形态。

**9. 需要注意的问题**：
- 实验测量的 $T_{1/2}$ 本身有 ~5-10% 系统差
- 部分核素的 GT 跃迁矩阵元难以精确计算

## §V.6 作者的逻辑

§V 的逻辑结构是**"按网络方程的需求顺序"**：

1. **§V.A 核质量**—— 决定路径
2. **§V.B β-decay**—— 决定通过速率
3. **§V.C n-capture**—— 决定推进速率
4. **§V.D 裂变**—— 决定终点

这种顺序对应 §III.A 网络方程中各项的输入优先级：mass（路径） > β-decay（流出） > n-capture（流入） > fission（终止）。

## §V.7 我的理解 [INTERPRETATION]

### 模型选择的"工程哲学"

r 过程核数据建模有两种哲学：
1. **多模型平均**（如 REACLIB 的多模型加权平均）：减小单一模型偏差
2. **单一最佳模型**（如 FRDM+QRPA）：保持物理一致性

Cowan 2021 偏向**多模型对比**——展示 FRDM/HFB/Duflo-Zuker 的差异，让读者判断。

### 核数据缺口与 NSM 模拟的耦合

NSM ejecta 模拟高度依赖 §V 的核理论输入。一个简化的"灵敏度测试"是：
- mass 不确定度 1 MeV → 路径偏移 ~5 mass units
- β-decay $T_{1/2}$ 不确定度 50% → 最终丰度 0.3-0.5 dex
- n-capture rate 不确定度 30% → 第三峰形态 0.2 dex

### 裂变 recycling 的当代争议

§V.D 提及的"neutron-induced fission 在 r 过程末端的循环"是 NSM ejecta 模拟的核心环节：
- 若裂变循环效率高：r 过程路径 $A \sim 260$ 全部裂变为 $A \sim 130$，产生大量 second-peak 元素
- 若裂变循环效率低：r 过程路径只到 $A \sim 200$，锕系产量高

两者的丰度模式截然不同。Cowan 2021 §V.D 强调 Kowal 2019 等裂变 yield 模型仍不确定。

## §V.8 潜在问题与值得关注的地方 [CRITIQUE]

### §V.8.1 优点
1. **模型覆盖全面**：FRDM, HFB, Duflo-Zuker, QRPA, TALYS, Kowal 等都提及
2. **不确定度量化**：每个模型都给出 RMS 误差估计
3. **物理量纲清晰**：从微观模型到宏观产物的链条完整

### §V.8.2 局限
1. **FRIB 数据未整合**：2021 年 FRIB 刚开始启用，第一批 r 过程数据未发表
2. **理论-实验联合拟合**（如 Bayesian 框架）：未深入讨论
3. **机器学习 mass 模型**：2021 年前后已有 NN/ML 介入，但本文未提及
4. **裂变 yield 系统对比**：不同模型（GEF, SPY, Kowal）的对比不充分
5. **Ab-initio 方法**：如 IMSRG, coupled cluster 在 r 过程区的应用未提及

### §V.8.3 与其他章节的张力
- §V.A → §IV.B：实验测量的 mass 是 §V 的训练数据
- §V.B → §III.B：β-decay 决定 r 过程等待点的通过
- §V.D → §VI.D：裂变循环直接决定 NSM 的最终 yields

## §V.9 关键术语

- **FRDM** (Finite-Range Droplet Model): 宏观-微观核质量模型
- **HFB** (Hartree-Fock-Bogoliubov): 微观核质量模型
- **QRPA** (Quasiparticle Random Phase Approximation): 集体激发态理论
- **Hauser-Feshbach**: 复合核统计模型，用于反应率计算
- **TALYS**: 开源统计模型代码
- **GT 矩阵元** (Gamow-Teller matrix element): β-decay 跃迁矩阵元
- **Strutinsky 壳修正**: 核质量模型中的壳效应
- **β-delayed fission**: β-decay 后自发裂变
- **裂变势垒** (fission barrier): 裂变阈能，依赖核形变
- **shell correction**: 闭壳层导致的能量修正
- **AME** (Atomic Mass Evaluation): 实验核质量评估

## §V.10 引用页码索引

| 主题 | 原文页码 | fulltext 行号 |
|---|---|---|
| §V 起始（"NUCLEAR MODELING..."） | 015002-32 | 行 1829 |
| §V.A 核质量 (FRDM, HFB, DZ) | 015002-32 | 行 1900+ |
| §V.B β-decay 半衰期 | 015002-32 起 | 行 2013+ |
| §V.B.β2 β-delayed neutron | 015002-32 起 | 行 2080+ |
| §V.C 中子俘获率 | 015002-32 起 | 行 2114+ |
| §V.D 裂变 (β-delayed, neutron-induced) | 015002-32 起 | 行 2200+ |
| Fig. 8 (mass 模型对比) | 015002-33 | 行 1950+ |
| Fig. 9 (β-decay 模型对比) | 015002-34 | 行 2050+ |