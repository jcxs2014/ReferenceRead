> 上一章：[[05_conclusions]]
> 下一章：[[A2_appendix_dsa_theory]]
---
title: "Appendix A — Numerical Model (Plasma Velocity & Fields)"
section: 'Appendix A'
---

## A.1 Spherical Shock: Plasma Velocity

**[FACT]** 球状激波从原点径向向外以恒定 $V_{\text{sh}}$ 运动。假设：
- $V_{\text{sh}}$ 远大于声速和 Alfvén 速度
- 强激波 → 密度跃迁比 $r=4$（理想单调气体）
- 环境气体静止

**[FACT]** 激波上游（$r > V_{\text{sh}}t$）：
$$\mathbf{U} = 0$$

**[FACT]** 激波下游（$r < R_{\text{sh}}$）：
$$\mathbf{U}(r,t) = U(r,t)\,\hat{r}$$
采用特殊函数形式：
$$U(r,t) = V_{\text{sh}}\left[1 - \frac{1}{2}\left(1 + \tanh\left(\frac{V_{\text{sh}}t - r}{3\,\Delta_S}\right)\right)\right]$$

**[FACT]** 该形式允许 Maxwell 方程对含湍流磁场的下游磁场给出**精确解析解**。

**[FACT]** 极限行为：
- $r \ll V_{\text{sh}}t$：$U \to (3/4)V_{\text{sh}}$（下游速度，由 $r=4$ 强激波条件）
- $r \gg V_{\text{sh}}t$：$U \to 0$

**[FACT]** 过渡区尺度 $\Delta_S = 5\,c/\omega_p$（$c/\omega_p$ 为等离子体皮肤深度）——假设远小于粒子回旋半径。

**[FACT]** 模型局限：
- 原点必须有**等离子体和磁场源**才能使 $r < (3/4)V_{\text{sh}}t$ 处的解成立——**模型实际适用 $r > (3/4)R_{\text{sh}}$**
- 下游 $\nabla \cdot \mathbf{U} \neq 0$ → 粒子冷却时标 $\sim R_{\text{sh}}^2/V_{\text{sh}}$

## A.2 Spherical Shock: Electric and Magnetic Field

**[FACT]** 磁场构造：
- 上游：均匀平均 $\mathbf{B}_0 = B_0\hat{z}$ + Kolmogorov 湍流
- 下游：由 Maxwell 方程 $\nabla \times \mathbf{B} = (4\pi/c)\mathbf{J}$ 通过流的 $\nabla \times \mathbf{U}$ 项推导

**[FACT]** 湍流谱：
- **三维 Kolmogorov**
- 谱指数 $g = -(5/3)+1 = -2/3$（Giacalone & Jokipii 1999 定义：$\int k^{g+1}dk$ 为总方差）
- 波模对数间距 $\Delta k_n = 0.05\,k_n$
- 波长范围 $\lambda_{\min} = 0.5\,r_{g0}$ 到 $\lambda_{\max} = 10^6\,r_{g0}$
- 湍流方差 $s^2 = \langle \delta B^2\rangle/B_0^2$：本文用 $s^2=0.3$ 和 $s^2=1$

**[FACT]** 电场：理想 MHD 近似
$$\mathbf{E} = -\frac{1}{c}\,\mathbf{U} \times \mathbf{B}$$

**[FACT]** 因下游流速度恒定（$(3/4)V_{\text{sh}}$），解只在 $r > (3/4)V_{\text{sh}}t$ 有效——原点附近的源问题需另行处理。

## A.3 与 Caprioli 2014 方法对比

| 要素 | Giacalone 2017（本文） | Caprioli & Spitkovsky 2014 |
|---|---|---|
| 粒子处理 | 测试粒子 | 动力学离子（hybrid） |
| 场处理 | 运动学预设 + Maxwell | 自洽 MHD |
| 几何 | 三维球面 | 2D/3D 平面 |
| 注入物理 | 忽略 cross-shock potential | 自洽恢复 |
| 加速率公式 | γ(θ) 解析（Appendix B） | 模拟直接测量 |
| 适用 | 几何效应、长时间演化 | 微观注入、定量效率 |

**[INTERPRETATION]** 两种方法**互补**：本文给出几何直觉与长时间演化图像，Caprioli 给出微观注入机制与定量效率。
