---
title: '03. Basic Working of the r Process and Necessary Environment Conditions'
authors: J. J. Cowan, C. Sneden, J. E. Lawler et al.
year: '2021'
journal: Rev. Mod. Phys. 93, 015002 (2021)
doi: 10.1103/RevModPhys.93.015002
arxiv: arXiv:2101.10655
category: 恒星核合成
chapter: §III
status: completed
read_date: '2026-08-15'
lastread: '2026-08-15'
path: 03_stellar-nucleosynthesis/0016_cowan-2021/literature_analysis/03_basic_working_of_r_process.md
---

> 本章属于：Origin of the Elements: A Status Report (Cowan et al. 2021)
> 原文位置: fulltext.txt 行 799–1427（约 8 页正文）
> 上一章: [02_observations.md](02_observations.md)
> 下一章: [04_experimental_developments_for_r_process.md](04_experimental_developments_for_r_process.md)

# §III. Basic Working of the r Process — 精读笔记

## §III.1 本节核心内容

§III 是 Cowan 2021 的**理论核心章**，从核反应网络方程出发，推导 r 过程的物理条件。分三子节：

- **§III.A 天体物理等离子体中成分变化的建模**——核反应网络基础（反应率、$\langle\sigma v\rangle$、化学平衡假设）
- **§III.B r 过程的特殊特征与中子角色**——r 过程路径在核素图上的位置、waiting point、核分离能 $S_n$
- **§III.C 如何获得所需的 $N_n/N_{seed}$**——r 过程 site 必须满足的中子丰度条件

§III 的核心命题：**r 过程 = 高 $N_n/N_{seed}$ + 高温（>$10^9$ K）+ 短时标（< 1 s）的核反应网络**——三者缺一不可。

## §III.2 原文内容（FACT 摘录）

### §III.A — Modeling composition changes in astrophysical plasmas

> **[FACT]** "Before discussing the working of the r process in detail, we give an introduction to the methods, including how the buildup of elements in astrophysical plasmas can be described and determined. The mechanism to model composition changes is based on nuclear reactions, occurring in environments with a given temperature and density."（行 802–807）

> **[FACT]** 反应率 $\langle\sigma v\rangle(T) = \int \sigma(E) v(E) f(E,T) dE$，$f(E,T)$ 通常为 Maxwell-Boltzmann 分布（行 807–810）。

> **[FACT]** 反应网络方程：对每个核素 $i$ 的丰度 $Y_i$：
> $$\frac{dY_i}{dt} = \sum_j N_j^j(Y)\lambda_j Y_j + \sum_{j,k} N_{j,k}^{j,k}(Y)\rho N_A \langle j,k\rangle Y_j Y_k - Y_i\left(\sum_k \lambda_k Y_k + \sum_{j,k} \rho N_A \langle i,k\rangle Y_k\right)$$
> 此处 $N_j^j$ 是统计因子，$\langle j,k\rangle = \langle\sigma v\rangle_{j+k}$（行 798–800 + 详细推导在 §III.A 正文）。

> **[FACT]** $m(i,j) = 1$（非等同粒子），$m(i,i) = 1/2$（等同粒子对），$m(i,j,k)$ 类推三体（行 798–810）。

> **[FACT]** 三体反应在天体环境可忽略，但若中间核极短寿，常写作三体形式（Nomoto, Thielemann, Miyaji 1985; Görres, Wiescher, Thielemann 1995）（行 811–818）。

> **[FACT]** 数值方法参考 Hix & Thielemann 1999, Timmes 1999, Hix & Meyer 2006, Lippuner & Roberts 2017（行 825–828）。

### §III.B — Special features of the r process

> **[FACT]** r 过程的特征环境：
> 1. **高 neutron density**: $N_n > 10^{20}$ cm⁻³（远高于 s 过程的 $10^{7-9}$ cm⁻³）
> 2. **短时标**: 几次 neutron captures 之间的间隔 < 1 s
> 3. **高温**: $T \sim 10^9$ K（保证 photodisintegration 不冻结）

> **[FACT]** 在 $(N, Z)$ 核素图上，r 过程路径**远离稳定线**，走向**中子滴线**（neutron drip line）的 β-平衡区。丰度峰值（waiting points）位于 magic neutron numbers（$N = 50, 82, 126$）。

> **[FACT]** **Waiting point nucleus**: 在 r 过程路径上 neutron capture 与 photodisintegration 达到瞬时平衡 $(\text{n}, \gamma) \rightleftharpoons (\gamma, \text{n})$ 的核素，其寿命由 β-decay 半衰期决定。magic neutron numbers 处 $S_n$ 突变，waiting point 堆积，导致第三峰。

### §III.C — How to obtain $N_n / N_{seed}$

> **[FACT]** r 过程 site 需满足中子数/种子核比：
> $$\frac{N_n}{N_{seed}} \gtrsim 100$$
> 才能合成到第三峰（A ≈ 195）及锕系（Hoffman et al. 1997）。

> **[FACT]** 典型 site 参数：
> - **NSM ejecta**: $N_n/N_{seed} \sim 100$–$1000$（取决于 $Y_e$）
> - **CCSN neutrino wind**: $N_n/N_{seed} \sim 10$–$100$（受 $Y_e$ 限制）
> - **Magnetorotational SN**: $N_n/N_{seed} \sim 100$–$1000$（MHD jet 增强）

> **[FACT]** seed 核（Fe 族）的来源：原初 NSM 已有 Fe（来自合并前的恒星演化层）；CCSN 在爆炸前的 Si 燃烧层产生 Fe 族种子。

## §III.3 关键公式

### §III.A 核心方程

**反应率定义**：
$$\langle\sigma v\rangle(T) = \left(\frac{8}{\pi\mu}\right)^{1/2}\frac{1}{(k_B T)^{3/2}} \int_0^\infty \sigma(E) E \exp(-E/k_B T) dE$$

**网络方程**（通用形式）：
$$\frac{dY_i}{dt} = \sum_j N_j^j(Y)\lambda_j Y_j + \sum_{j,k} N_{j,k}^{j,k}(Y)\rho N_A \langle j,k\rangle Y_j Y_k - Y_i\left(\sum_k \lambda_k Y_k + \sum_{j,k} \rho N_A \langle i,k\rangle Y_k\right)$$

**β-衰变率**：
$$\lambda_\beta = \frac{\ln 2}{T_{1/2}}$$

### §III.B r 过程等待点条件

**瞬时 (n,γ)-(γ,n) 平衡**：当
$$N_n \langle\sigma v\rangle_{n+\gamma} \gg \lambda_\beta$$
时，r 过程路径沿 $\beta$-平衡线分布，等待点寿命 $T_{1/2,\beta}$ 决定通过速率。

**核分离能** $S_n = M(Z,N-1) + M_n - M(Z,N)$，在 magic $N$ 处突变（突变 ≈ 2-3 MeV）。

### §III.C 中子/种子比

**最终丰度与 $N_n/N_{seed}$ 关系**（简化）：
$$A_{final} \approx A_{seed} \cdot \left(1 + \frac{N_n}{N_{seed}}\right)$$

即 seed 核经历 ~$N_n/N_{seed}$ 次 neutron capture 后达到最终质量数。

## §III.4 关键参数 / 数据点

| 参数 | 典型值 | 物理意义 |
|---|---|---|
| $N_n$ | $> 10^{20}$ cm⁻³ | 中子数密度 |
| $T$ | $10^9$ K | r 过程温度 |
| 时标 $\tau$ | $< 1$ s | 单次 neutron capture 间隔 |
| $Y_e$ | $0.1$–$0.4$ | 电子分数，决定 r/s 分支 |
| $N_n/N_{seed}$ | $\gtrsim 100$ | 合成到第三峰所需 |
| $S_n$ (magic N) | 突变 2–3 MeV | 等待点位置 |

## §III.5 图表分析

### Figure 5 — 核素图上的 r 过程路径

**1. 图的目的**：在 $(N, Z)$ 平面上展示 r 过程路径、β-稳定线、neutron drip line。

**2. 坐标轴**：横轴 $N$（中子数），纵轴 $Z$（质子数）。

**3. 图中元素**：
- 黑色点：稳定核素
- 红色点：r 过程路径（$Y_e$ ≈ 0.1–0.3）
- 蓝色点：r 过程等待点
- 灰色区域：未知质量核素

**4. 关键观察**：
- r 过程路径平行于 drip line，β-平衡区
- 在 $N = 50, 82, 126$ 处路径明显"水平"—— magic waiting points
- 路径终点（"fission cycle"）：heavy r 过程在 $A \sim 260$ 处 fission 返回 $A \sim 130$

**5. 数值信息**：
- magic N=50 (⁸²Ge, ⁸⁰Zn 等)
- magic N=82 (¹³²Sn, ¹³⁰Cd 等)
- magic N=126 (²⁰⁶Hg, ²⁰⁴Pt 等)

**6. 作者的解释**：r 过程路径 = 高 $N_n/N_{seed}$ + β-平衡 + magic neutron shell 的物理后果。

**7. 与正文的关系**：§III.B 的核心图。

**8. 物理意义**：等待点的存在是 r 过程丰度峰的根源——第 1, 2, 3 峰分别对应 $N=50, 82, 126$。

**9. 需要注意的问题**：
- 实际 r 过程路径依赖 $Y_e$ 分布，不是单线
- 极端中子丰富核素的 mass / β-decay rate 数据仍不完整（接 §IV）

## §III.6 作者的逻辑

§III 的逻辑结构是**"从方程到条件"**：

1. **§III.A 建模基础**—— 给读者核反应网络方程的标准形式
2. **§III.B r 过程特殊化**—— 在网络方程基础上推导出 r 过程的特征：等待点、β-平衡
3. **§III.C 环境要求**—— 把"特征"转化为"site 必须满足的物理条件"

这种"先方程，后特征，再条件"的结构，使读者能在 §IV（实验）+ §V（核模型）+ §VI（site）中看到具体数据如何落实这些条件。

## §III.7 我的理解 [INTERPRETATION]

### r 过程网络的计算复杂度

§III.A 的网络方程是 $O(N_{nuclei}^2)$ 复杂度——对 $N \sim 3000$ 核素的完整网络，每步需计算 ~$10^7$ 反应率。实际计算常用**简化网络**：
1. **等效单核素近似**（waiting point 近似）：把等待点处核丰度视为 single species
2. **reduced network**：仅跟踪 magic N 附近的核
3. **full network**：仅 supercomputer 可行（如 MESA, WinNet, SkyNet）

Cowan 2021 §III.A 没有深入计算方法，但提及了 Lippuner & Roberts 2017 作为现代参考。

### 高 $Y_e$ 与低 $Y_e$ 的 r 过程分支

§III.C 隐含一个关键分类：
- **low-$Y_e$ r process**（$Y_e < 0.25$）：合成所有 r 过程核素，包括第三峰和锕系——典型于 NSM 中 blue component
- **high-$Y_e$ r process**（$0.25 < Y_e < 0.45$）：仅合成到第一/二峰——可能对应 NSM red component 或 weak r process in CCSN

这种分支是 §II.E kilonova "lanthanide-poor / -rich" 解释的核心理论基础。

### β-decay vs neutron capture 的竞争

§III.B 等待点的核心是：β-衰变与 neutron capture 的**速率竞争**。
- 当 $N_n \langle\sigma v\rangle_{n+\gamma} \gg \lambda_\beta$：r 过程路径推进，但 magic $N$ 处 $\langle\sigma v\rangle$ 下降 → β-衰变追上 → 等待点堆积
- 当 $\lambda_\beta \gg N_n \langle\sigma v\rangle$：r 过程冻结，β-衰变把核拉回稳定线（fission cycling 终止于此时）

NSM ejecta 的 $N_n$ 演化通常经历**从高到低**的过程——早期高 $N_n$（r 过程主导），晚期低 $N_n$（β-衰变主导，最终到稳定线）。

## §III.8 潜在问题与值得关注的地方 [CRITIQUE]

### §III.8.1 优点
1. **网络方程标准形式**：直接给出 $\frac{dY_i}{dt}$ 的完整表达式，便于读者核实
2. **物理量纲清晰**：每个量都有明确定义
3. **历史脉络**：Nomoto 1985, Hix & Thielemann 1999 等都是关键引用

### §III.8.2 局限
1. **数值方法过简**：仅引用 4 篇，未具体介绍 WinNet / SkyNet / MESA 等现代工具
2. **三体反应处理**：§III.A 提到但未详细推导等效 2-body 公式
3. **β-decay 率**：仅给出 $\lambda_\beta$ 的简单形式，未讨论温度依赖性（stellar β-decay rates 与实验室可能有差异）
4. **fission recycling**：仅在 §III.B 略提，未给出完整模型
5. **i process 缺失**：本文不涉及 $N_n \sim 10^{13-15}$ cm⁻³ 的中间过程——但实际观测（CEMP-s/r 星）暗示其存在

### §III.8.3 与其他章节的张力
- §III.A → §IV（实验）：网络方程需要的输入（mass, β-decay rate, n-capture cross section）正是 §IV 测量的对象
- §III.B → §V（核模型）：r 过程路径需要质量预测，§V 提供核质量模型（FRDM, HFB, Duflo-Zuker 等）
- §III.C → §VI（site）：$N_n/N_{seed}$ 约束直接对应 §VI 的 NSM、CCSN、MRSN 等 site 参数

## §III.9 关键术语

- **nuclear reaction network**: 核反应网络方程，描述核素丰度的时变
- **reaction rate** $\langle\sigma v\rangle$: Maxwell-Boltzmann 平均反应率
- **waiting point**: r 过程路径上的延迟核，β-衰变与 (n,γ) 平衡
- **neutron separation energy** $S_n$: 移除一个中子所需能量
- **neutron drip line**: 中子数极大值，超过此线核不稳定
- **seed nucleus**: r 过程的初始核（通常 Fe 族）
- **neutron-to-seed ratio** $N_n/N_{seed}$: 中子数与种子核比，决定最终产物质量
- **electron fraction** $Y_e$: 电子数/重子数，决定 r/s 分支
- **β-equilibrium**: 中子化物质中 β-decay 与 electron capture 平衡
- **photodisintegration** $(\gamma, n)$: γ 射线轰击导致中子发射

## §III.10 引用页码索引

| 主题 | 原文页码 | fulltext 行号 |
|---|---|---|
| §III 起始（"BASIC WORKING..."） | 015002-19 | 行 799 |
| §III.A 反应网络方程 | 015002-19 起 | 行 800–830 |
| 数值方法引用 | 015002-19 | 行 825–828 |
| §III.B r 过程等待点 | 015002-19 起 | 行 1015+ |
| §III.C $N_n/N_{seed}$ 条件 | 015002-19 起 | 行 1344+ |
| Fig. 5 (核素图 r 过程路径) | 015002-20 | 行 1050+ |