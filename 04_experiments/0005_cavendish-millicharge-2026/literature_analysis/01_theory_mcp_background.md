# 1. mCP 背景与 Cavendish 信号物理

> 本章属于：Cavendish Tests of Millicharged Particles
>
> 上一章：`00_overview.md`
>
> 下一章：`02_recasting_cavendish.md`

## 1.1 本节核心内容

论文首先建立 **millicharged particles (mCPs)** 的动机与参数空间，然后给出两个关键物理推导：**(i)** 带电导体壳内部的 mCPs 会积累并产生可测电压；**(ii)** 该信号在弱耦合与强耦合 regime 下形式不同，分别对应 Debye 屏蔽与电学捕获。

## 1.2 原文内容（详细复述）

**[FACT]** mCPs 被定义为携带有效电荷 $eq_\chi \ll 1$ 的新粒子（$e$ 为元电荷，$q_\chi$ 为无量纲电荷）。它们在标准模型（SM）扩展中地位基础——最简单的扩展即为引入带小电荷的新粒子。

**[FACT]** 加速器产生实验 [8–16]、超新星 SN1987A [17]、离子阱 [18]、物质电中性 [19–21]、暗物质直接探测 [22–24] 均已对 mCPs 设限，但"令人惊讶地"仍有相当参数空间——在 GeV 尺度质量下 $q_\chi \sim 10^{-4}$ 仍未被排除。

**[FACT]** 关键机制：在宽广的参数空间内，mCPs 与地球物质发生快速散射并**热化到室温 $T \approx 300$ K**（对应 $\sim 25$ meV），从而在地球上形成**大 overdensity**。mCP 热化条件在 Fig. 1 的上方灰色实线以上——即 $m_\chi q_\chi^2 \gtrsim$ 某阈值。

**[FACT]** 本文核心思路：在一篇 companion paper [30]（Berlin et al. 2026）中，作者证明了固定电压的带电壳（如 Van de Graaff 加速器）可作为 mCPs 的有效**积聚器（accumulator）**，把局部密度提升多达 **12 个量级**。本文则演示 Cavendish 实验本身既是 quasistatic accumulator 又是探测器。

**[FACT]** Cavendish 实验基本结构：自 18 世纪末以来的库仑定律检验，核心是测量**带电导体壳内部的电场**。高斯定理完美时壳内无电场；任何非零电场意味着库仑定律破缺（如光子有质量、或新物理），或存在穿透壳体的物理电荷。

**[FACT]** 具体实现：一组同心壳，外层壳以频率 $\nu_0$ 和电压 $\phi_0$ 相对地做准静态振荡，内层两壳之间的电势差被测量。最敏感的一次（Ref. [37]）将壳内电压差限制在 $< 10^{-12}$ V。

**[FACT]** 自 20 世纪以来，Cavendish 实验常被重新解释为**光子质量** $m_\gamma$ 的测量——$m_\gamma \neq 0$ 使高斯定理变为 $\nabla \cdot \mathbf{E} = \rho - m_\gamma^2 \phi$，等价于壳内等效电荷密度 $\rho_{\rm eff} = -m_\gamma^2 \phi_0$。

**[FACT]** 关键区分：导体壳对普通 SM 离子是屏障（work function $\sim$ few eV，$q > 300\,\mathrm{K}/\mathrm{few\,eV} \sim 10^{-2}$ 的粒子无法通过金属表面），但对更小的 $q_\chi \lesssim 10^{-2}$ 的 mCPs，壳几乎透明。因此**壳屏蔽 SM 离子的同时仍允许 mCPs 穿过**。

## 1.3 关键公式

**公式 1（弱耦合 regime，Debye 屏蔽）**：

$$\rho_{\rm weak} \simeq \epsilon_{\rm weak}\, m_D^2\, \phi_0$$

其中：
- $m_D = \sqrt{eq_\chi n_\chi / T}$ 为 mCP 对光子 Debye 质量的贡献
- $n_\chi$ 为 mCP 数密度
- $\epsilon_{\rm weak} \lesssim 1$ 为效率因子（反映 mCPs 在一个振荡周期内未完全穿过的可能性）
- 物理意义：$\rho_{\rm weak} m_D$ 在 Gauss 定律中扮演光子质量的角色

**公式 2（强耦合 regime，电学捕获）**：

$$\rho_{\rm strong} \sim \frac{2}{\pi} \epsilon_{\rm strong}\, eq_\chi n_\chi \frac{V_E\, t_{\rm osc}}{R_0}$$

其中：
- $t_{\rm osc} = \frac{1}{2\nu_0}$ 为半振荡时间
- $\epsilon_{\rm strong} \lesssim 1$ 为效率因子（要求 mCPs 在振荡时间内扩散进入壳体、散射并电学束缚）
- 强耦合 regime：$q_\chi \gtrsim T/(e\phi_0)$

**公式 3（积聚速度 $V_E$）**：

$$V_E \simeq \frac{eq_\chi E_0}{m_\chi / \tau_{\rm air}} \left/ \max\left(\tau_{\rm air} E,\, \frac{v_{\rm th}}{2R_0}\right)\right.$$

其中：
- $E_0 = \phi_0 / R_0$ 为壳体表面电场
- $\tau_{\rm air}$ 为 mCP-大气原子动量交换时间
- $v_{\rm th} = \sqrt{3T/m_\chi}$ 为 mCP 热速度
- $\beta_E$ 为镜像电荷修正因子（户外 $\sim 1$，室内因地面屏蔽可降至 $\sim q_\chi\phi_0/(2T) \ll 1$）

## 1.4 关键参数

| 参数 | 值 | 单位 | 意义 |
|---|---|---|---|
| $T$ | 300 | K | 室温 |
| $q_\chi$ | $10^{-6}$–$10^{-2}$ | 无量纲 | mCP 电荷 |
| $m_\chi$ | $1$ MeV–$1$ GeV | GeV | mCP 质量 |
| $n_\chi$ | $10^{-1}$–$10^{6}$ | cm⁻³ | 环境 mCP 数密度 |
| $q_\chi$ 加速器限 | $10^{-4}$ | 无量纲 | GeV 尺度尚未排除 |
| 积聚提升 | $10^{12}$ | 无量纲 | accumulator 密度增强上限 |

## 1.5 图表分析

本章无独立图表；核心物理推导在 §IV 通过 Fig. 1 展现。Fig. 1 中的两条灰色/黑色虚线（热化线、能量损失线）由本章 §I 的散射/热化物理决定。

## 1.6 作者的逻辑

**问题** → mCPs 参数空间仍有较大未被排除区域（$q_\chi \sim 10^{-4}$）→ **方法** → 利用 Cavendish 实验的准静态带电壳结构 → **物理** → mCPs 穿透导体壳、在内壳电场中积聚 → **结果** → 积聚电荷产生可测壳内电压 → **下一步** → §IV 重新解读历史实验并提取约束。

## 1.7 我的理解（INTERPRETATION）

**[INTERPRETATION]** 核心洞察在于把**库仑定律检验**（100+ 年历史技术）重新解释为**暗物质/新物理探测器**：传统的重新解释是把壳内电场归因于光子质量；本文进一步指出它**必然同时探测 mCPs**——因为导体壳对 mCPs 几乎透明、对 SM 离子不透明这一"选择性透过"性质。

**[INTERPRETATION]** 强耦合积聚机制的"12 个量级提升"是本论文与 companion paper [30] 的核心创新：静电壳通过**拖曳-散射-电学束缚**循环把 mCPs 从远处拉到壳内——这本质上是一个**静电力场驱动的 Maxwell's Demon**。

**[INTERPRETATION]** $\epsilon_{\rm strong}$ 和 $\epsilon_{\rm weak}$ 两个效率因子的引入使理论推导对**扩散时间 vs 振荡周期**的比值敏感——这正是 §IV–§V 中"频率选择"的物理依据。

## 1.8 潜在问题与值得关注的地方（CRITIQUE）

**[CRITIQUE]** 公式 2 假设"mCPs 连续分布"，且要求积聚总电荷 $> q_\chi^{-1} R_0^{-3} \sim 10^2$——对极小 $n_\chi$ 或极小 $q_\chi$ 的参数空间，离散化效应可能显著，使连续假设失效。

**[CRITIQUE]** $\epsilon_{\rm strong}$ 因子具体取值依赖于 mCPs 与壳体材料的散射截面——论文在 Supplemental Material [41] 讨论，但**正文未给具体函数形式**，读者无法独立复现极限曲线。

**[CRITIQUE]** 公式 3 中 $\tau_{\rm air}$（mCP-大气动量交换时间）来自 Ref. [26, 30]——该值对 $m_\chi$ 与 $q_\chi$ 有强依赖，尤其对 $m_\chi < 1$ MeV 的极端轻质量区，散射截面可能被原子电子屏蔽效应大幅压低，使公式可靠性下降（§IV 作者也承认这一点）。