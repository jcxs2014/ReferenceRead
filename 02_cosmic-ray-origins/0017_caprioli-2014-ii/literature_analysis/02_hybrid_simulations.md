---
title: "§2 HYBRID SIMULATIONS"
paper: "Caprioli & Spitkovsky 2014, ApJ 794, 46"
outline_ref: "§2 HYBRID SIMULATIONS"
---
> 上一章：[[02_cosmic-ray-origins/0017_caprioli-2014-ii/literature_analysis/01_introduction.md|01_introduction]]
> 下一章：[[02_cosmic-ray-origins/0017_caprioli-2014-ii/literature_analysis/03_magnetic_field_amplification.md|03_magnetic_field_amplification]]

#### 2.1 [FACT] 数值方法（dHybrid）与无量纲化

- **[FACT]** 代码：**dHybrid**（Gargatè et al. 2007）——非相对论、大规模并行、hybrid（离子动力学 + 电子为中和流体，多方状态方程）；即使 2D 也保留三个方向的离子动量与电磁场分量
- **[FACT]** **长度单位**：离子皮层深度 $c/\omega_p$，其中 $\omega_p = \sqrt{4\pi n e^2/m}$（$m$, $e$, $n$ 为离子质量、电荷、数密度）
- **[FACT]** **时间单位**：$\omega_c^{-1} = mc/eB_0$，$B_0$ 为背景磁场 $|B_0|$
- **[FACT]** **速度单位**：阿尔芬速度 $v_A = B/\sqrt{4\pi m n} = c\,\omega_c/\omega_p$
- **[FACT]** **激波强度**：阿尔芬马赫数 $M_A = v_{\rm sh}/v_A$，$v_{\rm sh} = -v_{{\rm sh},x}$；能量尺度 $E_{\rm sh} = \tfrac{1}{2} m v_{\rm sh}^2$
- **[FACT]** 离子初始热分布 $\sim v_A$（故声马赫 $M_s \approx M_A$）；电子初始与离子热平衡；本文直接以 $M = M_A \simeq M_s$ 表示激波强度
- **[FACT]** 激波产生机制：主等离子体流（沿 $-x$）与反射壁（$x=0$）产生的对流流碰撞；激波在图中向右传播

#### 2.2 [FACT] 参数空间与 Trade-off

| Run | $M$ | $L_x (c/\omega_p)$ | $L_y (c/\omega_p)$ | $t_{\max}(\omega_c^{-1})$ | $\Delta t(\omega_c^{-1})$ |
|-----|-----|-----|-----|-----|-----|
| A | 20 | $5\times10^4$ | 1000 | 1000 | $5\times10^{-4}$ |
| B | 20 | $10^5$ | 100 | 2500 | $5\times10^{-4}$ |
| C | 100 | $3\times10^4$ | 2000 | 200 | $10^{-4}$ |
| D | 80 | $4\times10^5$ | 200 | 500 | $2.5\times10^{-4}$ |
| E | $10\to50$ | $2\times10^4$ | 500 | 200 | $10^{-2}/M$ |

- **[FACT]** 使用**非常大盒子**以正确计入最高能离子的扩散长度，并跟踪直至 $M = 100$ 的强激波
- **[FACT]** **Trade-off 约束**：hybrid 模拟能量守恒所需的时间步 $\Delta t \propto 1/v_{\rm typ}$——高能粒子速度越大，$\Delta t$ 越小；因此盒子尺寸（纵、横）、激波强度与物理时间之间存在不可兼得
- **[FACT]** 本文采取**分离探索各极限**的策略（在 §6 明确讨论）：无法在同一 run 中同时满足（1）长时间演化 +（2）大横向尺寸 +（3）高 $M$

#### 2.3 §2.1 强激波长期演化（Run A/B，$M=20$ 平行激波）

- **[FACT]** **Run A**：$(L_x, L_y) = (5\times10^4, 10^3) \,[c/\omega_p]^2$，$t_{\max} = 1000\,\omega_c^{-1}$——大横向尺寸，完整捕捉**细丝化不稳定性**（CS13）
- **[FACT]** **Run B**：$(L_x, L_y) = (10^5, 10^2) \,[c/\omega_p]^2$，$t_{\max} = 2500\,\omega_c^{-1}$——小横向尺寸，**长时间演化**，研究非热尾发展
- **[FACT]** 图 1（Run A，$t=1000\omega_c^{-1}$）：密度、磁场各分量、本地阿尔芬速度；显示预期 $r \approx 4$ 密度跃变（$x_{\rm sh} \sim 6000\,c/\omega_p$），以及细丝化不稳定的标志性特征：**上游空腔化、激波面波纹（触发 Richtmyer-Meshkov）、下游湍流结构**
- **[FACT]** 图 2（Run B，$t$ 至 $2000\omega_c^{-1}$）：下游离子动量谱随时间演化；非热幂律尾范围随时间增长；$f(p) \propto p^{-4}$（$f(E) \propto E^{-1.5}$），与强激波 DSA 预言完美吻合，跨越**超过两个能量量级**

#### 2.4 §2.2 高马赫数区（Run C，$M=100$；Run D，$M=80$）

- **[FACT]** 背景：SNR 激波 $M$ 可达数百至千；Part I 显示 $M \gtrsim 10$ 时加速效率恒为 10%–15%；但 **MFA 在大 $M$ 下更显著**——故需要探测高 $M$ 区
- **[FACT]** **Run C**（$M=100$）图 3：渐近压缩 $r\approx 4$ 在 $x \sim 5000\,c/\omega_p$ 处达到；非磁化（高 $M_A$）激波由 **Weibel 不稳定性**触发（Kato & Takabe 2010）；加速离子的存在会在上游放大磁场，最终影响激波跃迁性质
- **[FACT]** **上游细丝化（filamentation）**是**高 $M$ 激波的普适特征**：在 $x \sim 8000\,c/\omega_p$ 处明显的空腔与细丝；热等离子体和磁场被推出空腔、堆积于密集细丝，**局部 $B$ 可达 $20\,B_0$**
- **[FACT]** 横向平均后 $|B| > B_0$ 的区域在激波前显著延伸；在 $5000\lesssim x \lesssim 8000\,c/\omega_p$ 处为极端的 CR precursor——能量粒子相对热和磁分量的能量**不成比例大**，将剧烈改变激波流体动力学
- **[FACT]** 可能的物理解释：CR precursor 中的**声学不稳定性**（Drury & Falle 1986），声波失稳形成弱"shocklets"显著加热上游
- **[FACT]** **Run D**（$M=80$，小横向）图 4：可解析下游热离子回旋半径，但不完全计入上游强细丝化；在 precursor 中 $B_{\rm tot}/B_0 \sim 5$–$10$（平均），峰值 $15$–$20\,B_0$；跟踪至 $t = 500\omega_c^{-1}$

#### 2.5 [FACT] 凹谱（concave spectrum）与 Part I 一致性

- **[FACT]** 高 $M$ 下，粒子谱虽呈 DSA 幂律尾，但因 CR 修正激波的非线性效应**肉眼可见地 concave**（Malkov & Drury 2001）；但由于非相对论，(气体+CR) 流体绝热指数仍为 $5/3$，总压缩比和子激波压缩比仅小偏离 $r=4$，故在最多两个能量量级内，偏离幂律几乎不可察觉

## 关键参数

| 参数 | 值 | 出处 |
|------|-----|------|
| $c/\omega_p$（长度单位） | 离子皮层深度 | §2 |
| $\omega_c^{-1}$（时间单位） | 离子回旋时间 | §2 |
| $v_A$（速度单位） | 阿尔芬速度 | §2 |
| $M_A = v_{\rm sh}/v_A$ | 阿尔芬马赫数 | §2 |
| $E_{\rm sh}$ | $\tfrac{1}{2} m v_{\rm sh}^2$ | §2 |
| Run A 盒 | $(5\times10^4, 1000)$ | Table 1 |
| Run B 盒 | $(10^5, 100)$ | Table 1 |
| Run C 盒 | $(3\times10^4, 2000)$，$t_{\max}=200$ | Table 1 |
| Run D 盒 | $(4\times10^5, 200)$，$t_{\max}=500$ | Table 1 |
| Run E 盒 | $(2\times10^4, 500)$，$t_{\max}=200$ | Table 1 |
| $M$ 范围 | 10, 20, 30, 50, 80, 100 | §2, §3 |
| 最大局部放大 $M=100$ | $\sim 20\,B_0$ | §2.2 |
| 平均放大 $M=80$ 在 precursor | $5$–$10\,B_0$ | §2.2 |

## 我的理解 / Interpretation

**[INTERPRETATION]** §2 是"实验平台"部分。关键点是 **dHybrid 的 trade-off 约束**：三个目标（长时间 + 大横向 + 高 $M$）不可同时满足。这一约束贯穿全文——作者明确承认结论来自**不同 run 的组合**，因此对饱和/非线性阶段的定量推断需要谨慎。§6 结论 5 也呼应此点。
