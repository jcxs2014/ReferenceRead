> 上一章：[[01_introduction]]
> 下一章：[[03_results]]
---
title: "§2 Numerical Model — Giacalone 2017"
section: '2. NUMERICAL MODEL'
---

## 2.1 方法总览

**[FACT]** 本文采用**测试粒子（test-particle）+ 运动学流体**（kinematically defined plasma flow）方法：
- **粒子**：大量测试质子，遵循洛伦兹方程
- **场**：由**预设**的等离子体流 + Maxwell 方程 + Kolmogorov 湍流确定——**不**自洽求解 MHD，也**不**包括 shock 微观结构（如 cross-shock potential）

**[FACT]** 与 Caprioli 2014 的 hybrid/PIC 方法对比：
- **本文**：不处理注入物理细节（cross-shock potential, ion reflection）
- **Caprioli 2014**：自洽 hybrid 恢复注入与 $p^{-4}$ 谱
- **本文优势**：三维球面几何、大范围参数空间、长时间模拟

## 2.2 运动方程

**[FACT]** 洛伦兹方程（cgs 单位）：
$$\frac{d\mathbf{p}}{dt} = q\left[\mathbf{E}(\mathbf{r},t) + \frac{\mathbf{v}}{c} \times \mathbf{B}(\mathbf{r},t)\right]$$
其中 $\mathbf{p}$ 动量、$\mathbf{v}$ 速度、$q=e$ 质子电荷、$c$ 光速。

**[FACT]** 数值方案：**Burlisch-Stoer 方法**（Press et al. 1986, *Numerical Recipes*）——**自适应步长**，能量守恒精度 $>10^{-5}$%。

**[FACT]** 关键优势：**$\mathbf{E}$, $\mathbf{B}$ 是三坐标函数**——**不允许 ignorable coordinate**，粒子可自由脱离场线。对比 Jokipii 1993; Giacalone 1994; Jones 1998 中至少一个坐标被假定可忽略。

## 2.3 初始条件

**[FACT]** 粒子释放时刻：
$$t_0 = \xi\, t_{\text{max}}^{1/3}$$
其中 $\xi$ 为 $[0,1]$ 均匀随机数。立方根来自**常数源通量** $n_0 V_{\text{sh}}$ 及球面面积 $\propto (V_{\text{sh}} t)^2$ 的假设。

**[FACT]** 分布函数确定：由 $t_{\text{max}}$ 时刻粒子位置与**等离子体静止系**速度给出。

## 2.4 参数空间（Table 1 总结）

| Run | $L_c/r_{g0}$ | $V_{\text{sh}} t_{\text{max}}/L_c$ | $s^2$ | Realizations | 图 |
|---|---|---|---|---|---|
| 1 | $10^4$ | 5 | 1 | Ensemble | Fig. 3 |
| 2 | $10^5$ | 5 | 1 | Ensemble | Figs 3,4,5,7 |
| 3 | $10^5$ | 5 | 1 | Single | Figs 5, 9 |
| 4 | — | — | — | Single | — |
| 5 | $10^5$ | 5 | 0.3 | Ensemble | Fig. 8 |
| 6 | — | — | — | — | — |

三个关键长度尺度：
1. $r_{g0}$：以 $V_{\text{sh}}$ 在 $B_0$ 中运动的粒子回旋半径
2. $R_{\text{sh}} = V_{\text{sh}} t$：激波半径
3. $L_c$：湍流相干尺度

## 2.5 物理常数与假设

**[FACT]**
- 理想单调气体，强激波跃迁比 $r=4$
- 环境未冲击气体静止
- 湍流：**三维 Kolmogorov**，谱指数 $g = -(5/3)+1 = -2/3$（Giacalone & Jokipii 1999 定义）
- 波模对数间距 $\Delta k_n = 0.05\,k_n$
- 波长范围：$0.5\,r_{g0}$ 到 $10^6\,r_{g0}$
- 内激波速度 $(3/4)V_{\text{sh}}$
- 过渡区 $\Delta_S = 5\,c/\omega_p$（等离子体皮肤深度）

## 2.6 局限

**[CRITIQUE]**
- **非自洽**：场由运动学给出，粒子不反馈到场
- **忽略 shock 微观结构**：无 cross-shock potential（图 4 中 5–500$E_R$ 的 bump-like 特征因此出现，但自洽 hybrid 中不出现）
- **测试粒子**：无粒子-粒子相互作用，无波产生
- **恒定 $V_{\text{sh}}$**：真实 SNR 符合 Sedov 解（减速）

**[INTERPRETATION]** 这些局限在 §4 中被明确承认，本文**聚焦几何效应**，而非自洽注入细节——Caprioli 2014 的 hybrid 结果补充后者。
