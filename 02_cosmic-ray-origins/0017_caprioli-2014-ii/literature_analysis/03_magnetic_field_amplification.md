---
title: "§3 MAGNETIC FIELD AMPLIFICATION"
paper: "Caprioli & Spitkovsky 2014, ApJ 794, 46"
outline_ref: "§3 MAGNETIC FIELD AMPLIFICATION"
---
> 上一章：[[02_cosmic-ray-origins/0017_caprioli-2014-ii/literature_analysis/02_hybrid_simulations.md|02_hybrid_simulations]]
> 下一章：[[02_cosmic-ray-origins/0017_caprioli-2014-ii/literature_analysis/04_turbulence_spectrum.md|04_turbulence_spectrum]]

#### 3.1 [FACT] 问题陈述与测量方法

- **[FACT]** 粒子加速中最重要的问题之一：**CR 诱导的不稳定性**如何有效放大初始磁场
- **[FACT]** §3 考察**不同强度激波**（$M$ 直至 100）的磁场放大；所有激波为**平行**，跟踪至 $t=200\omega_c^{-1}$
- **[FACT]** 案例对应：$M=100$（Run C）；$M=80$（Run D）；$M = 10, 20, 30, 50$（Run E）
- **[FACT]** 测量：图 5 上方面板——激波前**总磁场剖线** $B_{\rm tot}(x)$，在**横向 200 $c/\omega_p$** 与**时间 180–200 $\omega_c^{-1}$** 平均，位置相对于激波面 $x=x_{\rm sh}$
- **[FACT]** 激波面定位：跟磁场强度峰值（与离子密度峰值相关），并在数十个 $\omega_c^{-1}$ 时间平均；追踪速度剖线最大梯度结果相近
- **[FACT]** **时间与空间平均的必要性**：去除细丝化不均匀性引起的涨落；即使在大横向盒子中激波位置沿 $y$ 也有显著变化

#### 3.2 [FACT] 主要结果：MFA 随 $M$ 增强

- **[FACT]** **最重要的结果**：激波 precursor 中磁场放大**随 $M$ 增大而增大**
- **[FACT]** 图 5 下方面板：对激波前 $x = 10\,M_A c/\omega_p$ 距离内的平均 $B_{\rm tot}/B_0$ 作为 $M_A$ 的函数；积分区间按 $M$ 成正比选取（因强激波 precursor 长度更大）

#### 3.3 [FACT] 与共振流不稳定性预言的对比

- **[FACT]** 将模拟结果与**共振流不稳定性**（resonant streaming instability）预言（Skilling 1975a；Bell 1978；Achterberg 1983）对比
- **[FACT]** 求解**不随时间变化的** Alfvén 模式输运方程（弱 CR 修正激波，Lagage & Cesarsky 1983；Amato & Blasi 2006）：
$$P_w = \frac{P_{\rm cr}(x)}{M_A^{\sim 2}} \qquad (1)$$
其中 $P_w$, $P_{\rm cr}$ 为磁压与 CR 压，$M_A^\sim = (1 + 1/r) M_A$ 为激波参考系下的阿尔芬马赫（因强激波 $r \approx 4$，$M_A^\sim \approx 1.25 M_A$）
- **[FACT]** 横向自生分量 $B_\perp = \sqrt{B_y^2 + B_z^2}$；若各向同性，$B_\perp^2 = \tfrac{2}{3} B_{\rm tot}^2$，故 $P_w \simeq B_{\rm tot}^2/(12\pi)$
- **[FACT]** 将压以激波系流体速度 $\tilde{u}$ 归一化，引入激波处 CR 压 $\epsilon_{\rm CR} \equiv P_{\rm cr}(x_{\rm sh})/\tilde{u}^2$，最终得到：
$$\frac{B_{\rm tot}}{B_0} \simeq \sqrt{3\,\epsilon_{\rm CR}}\, M_{\rm sh} \qquad (2)$$
- **[FACT]** $\epsilon_{\rm CR}$ 通过测量**上游 precursor 内流体减速**推导，与 CR 加速效率直接相关；在所考虑 $M$ 范围内 $t = 200\omega_c^{-1}$ 时为 **10%–15%**（见 Part I 图 3）
- **[FACT]** **关键验证**：代入 $\epsilon_{\rm CR} = 0.15$ 到 (2) 式，与模拟得出的放大因子**拟合良好**（图 5 虚线）

#### 3.4 [FACT] 向真实 SNR 的外推

- **[FACT]** (2) 式向更高 $M$ 外推，与"若 CR 加速有效，CR 诱导不稳定性可解释年轻 SNR 激波阵面处**有效磁场放大**"的假说一致
- **[FACT]** 具体示例：$v_{\rm sh} \sim 4000$ km/s，$B_0 = 3$ G，$n = 1$ cm$^{-3}$ → $M_A \sim 600$ → **$B_{\rm tot}/B_0 \sim 20$**（$\epsilon_{\rm CR} = 0.2$）
- **[FACT]** 注意：高 $M$ 激波有强细丝结构（图 3），物理条件沿 $y$ 显著变化；但本分析**预期在局部仍成立**

## 关键参数

| 参数 | 值 | 出处 |
|------|-----|------|
| 积分区间（激波前） | $10\,M_A\, c/\omega_p$ | §3 |
| 平均时间窗口 | 180–200 $\omega_c^{-1}$ | §3 |
| 横向平均 | 200 $c/\omega_p$ | §3 |
| $\epsilon_{\rm CR}$ | 10%–15%（$t = 200\omega_c^{-1}$） | §3 |
| $M_A^\sim \approx$ | $1.25 M_A$（$r \approx 4$） | (1) |
| 模拟与 (2) 拟合 | $\epsilon_{\rm CR} = 0.15$ 拟合优 | §3 |
| SNR 外推 $B_{\rm tot}/B_0$ | $\sim 20$（$v_{\rm sh}=4000$ km/s，$\epsilon_{\rm CR}=0.2$） | §3 |

## 我的理解 / Interpretation

**[INTERPRETATION]** §3 是本文**定量核心**：建立 (2) 式这一**标度律**。其重要性在于：$\epsilon_{\rm CR}$ 由 Part I 自洽给出（10%–15%），代入 (2) 即可预测任意 $M$ 下的放大因子——为唯象/非线性 DSA 模型提供**自洽的 $B_{\rm tot}(M)$ 输入**。对 SNR 的外推给出与 X 射线观测一致的量级，是**从微物理到宏观现象的可证伪链条**。
