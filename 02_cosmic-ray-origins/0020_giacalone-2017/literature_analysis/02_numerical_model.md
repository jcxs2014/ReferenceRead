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

---

## 2.7 运动学流体解（Appendix A 核心）

**[FACT]** 原文 Appendix A 给出球状爆震波的**恒定速度解**：

$$U(r,t) = V_{\text{sh}}\left[1 - \frac{1}{2}\left(1 + \tanh\!\left(\frac{V_{\text{sh}} t - r}{3\,\Delta_{S}}\right)\right)\right]$$

其中 $\Delta_{S} = 5\,c/\omega_{p}$ 为等离子体皮肤深度（skin depth），$\omega_{p} = \sqrt{4\pi n_{0}e^{2}/m_{p}}$ 为等离子体频率。

**[FACT]** 速度分布特征：
- 上游（$r \gg V_{\text{sh}}t$）：$U \to 0$（静止气体）
- 下游（$r \ll V_{\text{sh}}t$）：$U \to (3/4)V_{\text{sh}}$（理想强激波跳跃比 $r = 4$）
- 激波面（$r \approx V_{\text{sh}}t$）：$U$ 从 0 跳到 $(3/4)V_{\text{sh}}$，过渡区尺度 $\sim 3\Delta_{S}$

**[INTERPRETATION]** 该解的假设：
- 恒定激波速度 $V_{\text{sh}} = 2000$\ km/s（Table 1）
- 强激波极限（$r = 4$），即 Mach 数足够大
- 理想单原子气体（$\gamma_{\text{gas}} = 5/3$）
- 忽略宇宙线反压（即不考虑非线性 DSA 中的 CR pressure 反馈）

**[CRITIQUE]** 上述假设与真实 SNR 存在 3 个量级差异：
- **Sedov 减速**：真实 SNR 符合 $V_{\text{sh}} \propto t^{-3/5}$（绝热相），不是常数
- **激波半径**：真实 SNR $R_{\text{sh}} \sim 10$\ pc 对应 $R_{\text{sh}}/r_{g0} \sim 4 \times 10^{9}$，本文模拟 $R_{\text{sh}}/r_{g0} = 5 \times 10^{5}$–$5 \times 10^{6}$，差距 3–4 个数量级
- **能量分配**：20% 入射能量通量 → 超热粒子（Giacalone et al. 1997），本文模拟无此注入微观机制

## 2.8 Kolmogorov 湍流场的构造

**[FACT]** 湍流磁场构造方法：
- **分解**：$\mathbf{B}(\mathbf{r},t) = \mathbf{B}_{0} + \delta\mathbf{B}(\mathbf{r},t)$
- **波模**：大量平面波叠加，波矢各向同性分布，偏振与相位随机
- **振幅谱**：单个波模振幅由 Kolmogorov 谱决定
- **谱指数**：$g = -2/3$（Giacalone & Jokipii 1999 定义）
- **波长范围**：$\lambda_{\min} = 0.5\,r_{g0}$ 到 $\lambda_{\max} = 10^{6}\,r_{g0}$
- **波模对数间距**：$\Delta k_{n} = 0.05\,k_{n}$

**[FACT]** 湍流方差 $s^{2}$ 定义：

$$s^{2} = \frac{\langle \delta B^{2} \rangle}{B_{0}^{2}}$$

- $s^{2} = 1$（Run 1–4）：等能量平均场与涨落场
- $s^{2} = 0.3$（Run 5）：涨落场较弱

**[INTERPRETATION]** Kolmogorov 谱的能量按波数分布为 $\mathcal{E}(k) \propto k^{-5/3}$；原文 $g = -2/3$ 是**单极化波模的磁能谱密度**指数，与体积平均的 $-5/3$ 一致（$d n / d k \propto k^{2}$ 的相空间因子被吸收进 $g$ 定义）。

## 2.9 Maxwell 方程组求解

**[FACT]** 激波穿越湍流时，磁场由 Maxwell 方程决定：

$$\nabla \times \mathbf{E} = -\frac{1}{c}\frac{\partial \mathbf{B}}{\partial t}, \qquad \nabla \times \mathbf{B} = \frac{4\pi}{c}\mathbf{J} + \frac{1}{c}\frac{\partial \mathbf{E}}{\partial t}$$

- 使用**运动学电流** $\mathbf{J} = n e \mathbf{U}$（$\mathbf{U}$ 为等离子体流速）
- 给出**有闭合形式**的湍流磁场解析解（原文强调 "closed-form analytic solutions"）
- 求解条件：需在上游某点（$r \gg R_{\text{sh}}$）已知 $\mathbf{B}$

**[FACT]** 动生电场：$\mathbf{E} = -\mathbf{U} \times \mathbf{B}/c$（非相对论、无粒子反馈）

**[CRITIQUE]** Maxwell 方程求解的关键简化：
- **无自生波**：粒子不激发 Alfvén 波（Bell 1978; Lee 1983; Bell 2004 中的不稳定性被忽略）
- **下游无湍流增强**：Giacalone & Jokipii (2007); Guo et al. (2012) 指出的下游湍流未被考虑
- **准静态**：上游磁场在流体参照系中静态，故时间序列在激波到达前为常数（Fig. 1 上图所示）

## 2.10 粒子释放策略（$t_{0} = \xi^{1/3} t_{\text{max}}$）

**[FACT]** 粒子释放公式：

$$t_{0} = \xi^{1/3}\,t_{\text{max}}, \qquad \xi \sim U(0,1)$$

**[FACT]** 立方根推导（原文注 2）：
- 在 $[0, t]$ 时段穿越激波的粒子总数：

$$N(t) = \int_{0}^{t} 4\pi R_{\text{sh}}^{2}\,n_{0}\,V_{\text{sh}}\,dt^{\prime} = 4\pi n_{0} V_{\text{sh}}^{3} t^{3}$$

- 释放时刻 $t_{0}$ 使得 $[0, t_{0}]$ 与 $[0, t_{\text{max}}]$ 的释放粒子数比 $\propto t_{0}^{3}/t_{\text{max}}^{3}$；
- 要求均匀释放 ⇒ 令 $\xi = t_{0}^{3}/t_{\text{max}}^{3}$，得 $t_{0} = \xi^{1/3} t_{\text{max}}$

**[FACT]** 初始条件：
- 位置：$r_{0} = V_{\text{sh}} t_{0}$（在激波面上均匀释放）
- 速度：$w_{0} = V_{\text{sh}}$（在**当地等离子体静止系**中）
- 速度方向：各向同性
- 数密度 $n_{0}$：源粒子密度（并非环境气体密度；可能对应镜面反射离子密度的一部分）

**[INTERPRETATION]** 该释放策略保证**稳态源通量** $n_{0}V_{\text{sh}}$ 恒定（与激波面积无关），因此不同 $t_{0}$ 释放的粒子对最终分布函数的贡献相同。这是一个**稳态假设**，与真实 SNR 的非稳态演化（deceleration phase）不同。

## 2.11 参数空间详解（Table 1 逐条）

**[FACT]** 原文 Table 1 共 7 次模拟：

| Run | $L_{c}/r_{g0}$ | $V_{\text{sh}} t_{\text{max}}/L_{c}$ | $s^{2}$ | Realizations | 用途 |
|-----|---------------|---------------------------------------|--------|--------------|------|
| 1 | $10^{4}$ | 5 | 1 | Ensemble | Fig. 3 |
| 2 | $10^{5}$ | 5 | 1 | Ensemble | Fig. 3, 4, 5, 7 |
| 3 | $10^{5}$ | 5 | 1 | Single | Fig. 5, 9 |
| 4 | $10^{6}$ | 5 | 1 | Ensemble | Fig. 3 |
| 5 | $10^{5}$ | 5 | 0.3 | Ensemble | Fig. 8 |
| 6 | $10^{4}$ | 50 | 1 | Single | Fig. 9 |
| 7 | $10^{6}$ | 0.5 | 1 | Single | Fig. 9 |

**[FACT]** 通用参数：$V_{\text{sh}} = 2000$\ km/s，$r = 4$（强激波），最大激波半径 $R_{\text{sh}}(t_{\text{max}}) = 5 L_{c}$。

**[INTERPRETATION]** 参数设计意图：
- Run 1–4：固定 $V_{\text{sh}} t_{\text{max}}/L_{c} = 5$、$s^{2} = 1$，扫 $L_{c}/r_{g0}$ —— 揭示湍流尺度对能谱的影响
- Run 5：扫 $s^{2}$ —— 揭示湍流强度对注入效率的影响
- Run 6、7：不同 $L_{c}/R_{\text{sh}}$ 下的 single realization —— Fig. 9 揭示局域 vs 非局域注入

**[CRITIQUE]** 仅 7 次模拟的参数空间**覆盖有限**：
- 未扫 $V_{\text{sh}} t_{\text{max}}/L_{c}$（除了 Run 6 和 7）
- 仅两种 $s^{2}$ 值（1 与 0.3），缺少中间值与高方差值
- Run 6、7 仅 single realization —— 统计意义受限

## 2.12 数值积分与能量守恒

**[FACT]** 求解器：Burlisch-Stoer 方法（Press et al. 1986），自适应步长。

**[FACT]** 能量守恒精度：$< 10^{-5}$%。

**[FACT]** 计算量：数百万粒子的轨迹积分。

**[FACT]** 时间步长限制：$\Delta t < \omega_{0}^{-1}$，其中 $\omega_{0} = eB_{0}/(m_{p}c)$ 为回旋频率。

**[CRITIQUE]** $L_{c}/r_{g0}$ 上限为 $10^{6}$，受计算资源限制（"We are not currently capable of simulating a realistic SNR blast wave"）。真实 SNR 需 $R_{\text{sh}}/r_{g0} \sim 4 \times 10^{9}$，即需要 $L_{c}/r_{g0} \sim 10^{9}$——**本文结果的外推**因此带有不确定性。

## 2.13 与 Caprioli 2014 的对比矩阵

| 维度 | Giacalone 2017（本文） | Caprioli & Spitkovsky 2014 |
|------|-----------------------|----------------------------|
| 方法 | Test-particle + 运动学流体 | Hybrid（离子粒子 + 电子流体） |
| 几何 | 球面 | 平面（7 个 $\theta$ 值） |
| 湍流 | 预设 Kolmogorov | 自发自放大湍流 |
| 注入 | 忽略微观物理 | 自洽处理 cross-shock potential、离子反射 |
| 反馈 | 无粒子-场反馈 | 有粒子-场反馈（MHD 自洽） |
| 粒子数 | 数百万 | 千万–亿 |
| 加速时间 | 长（$V_{\text{sh}}t/L_{c} = 5$） | 短（受计算限制） |
| 覆盖参数 | $L_{c}$、$s^{2}$ | $\theta_{Bn}$ |
| 结论 | 几何各向异性、场线连接时间机制 | $\theta$ 依赖的定量加速效率 |

**[INTERPRETATION]** 两篇论文**互补**：本文给出几何直觉与长时演化，Caprioli 给出微观物理与定量曲线。本文 §5.3 也明确提及这种互补关系。
