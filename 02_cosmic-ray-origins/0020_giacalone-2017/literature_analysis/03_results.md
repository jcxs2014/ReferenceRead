> 上一章：[[02_numerical_model]]
> 下一章：[[04_implications]]
---
title: "§3 Results — Giacalone 2017"
section: '3. RESULTS'
---

## 3.1 背景场（Fig. 1, 2）

**[FACT] Fig. 1**：磁场强度随时间在某固定位置的变化。显示：
- 激波到达前：$|\mathbf{B}|$ 在均值 $B_0$ 附近振荡（湍流贡献）
- 激波通过后：磁场跃升（压缩）+ 下游湍流增强

**[FACT] Fig. 2**：$x$-$z$ 平面上磁场线投影。$L_c/V_{\text{sh}}t$ 从顶到底由大变小（$3 \to 0.3$）。
- **$L_c > R_{\text{sh}}$（顶三图）**：场线几乎直线，贯穿球面——磁场线漂移**非局地化**，粒子沿场线跨越整个球面
- **$L_c < R_{\text{sh}}$（底三图）**：场线弯曲复杂，局域 $\theta_{Bn}$ 涨落剧烈——**注入局地化**

**[FACT] 核心观察**：激波法向与磁场夹角沿激波面前后**变化巨大**（"varies considerably along the shock front"）——这是本文全部结果的几何根源。

## 3.2 能谱对比：球状 vs 平面（Fig. 3, 4）

**[FACT] Fig. 3**：$L_c/r_{g0} = 10^4$（Run 1, 黑直方）与 $10^5$（Run 2, 蓝），对比平面激波（绿）。
- 球面 & 平面在低能区一致
- 球面出现**bump-like feature**在 $E_R$ 附近，延伸到 $\sim 5 E_R$——单圈回旋（single gyro-orbit）效应
- 高于 $50$–$100\,E_R$：谱变陡——有限加速时间 + **局域加速率沿球面变化**

**[FACT] Fig. 4**：球状（$L_c/r_{g0}=10^5$）vs 平面 DSA 理论 $\kappa p^{-4}$。球面谱在高能端**更陡**于 $p^{-4}$，原因：
1. 上游粒子贡献（理论只含下游）
2. **加速率随 $\theta_{Bn}$ 变化**（非均匀减速谱）

**[FACT] 能谱形状随 $\theta_{Bn}$ 定性说明**（Jokipii 1982, 1987）：
$$\dot{E}\big|_{\theta=90°} \gg \dot{E}\big|_{\theta=0°}$$
加速在准垂直区最快，准平行区最慢。

## 3.3 粒子通量沿球面分布（Fig. 5）

**[FACT] Fig. 5**：粒子通量 $E>1000\,E_R$，归一化 $n_0 V_{\text{sh}}$，色标编码。
- **Ensemble 平均（左）**：明显**极区增强**——粒子"收集"在两极
- **Single realization（右）**：极区增强依然存在，但叠加随机局部增强（"patchy"）

**[FACT] 极区增强的物理机制**（本文核心结果之一）：
> "The particles 'collect' at the poles as they approximately adhere to magnetic field lines that move poleward from their initial encounter with the shock at the equator, as the shock expands. The field lines at the poles have been connected to the shock the longest."

**链条**：
1. 粒子初始在赤道（准垂直）被快速注入/加速
2. 磁场线压缩使粒子**沿激波面漂移**（$E \times B$ drift 与动生电场同向）
3. 随着激波向外膨胀，每条场线与激波的交点**平均向极区移动**
4. 粒子随之聚集到极区——**场线-激波连接时间最长**

## 3.4 加速率随 θ 变化（Fig. 6）

**[FACT] Fig. 6(a)(b)**：不同时刻的球状激波，标注场线-激波交点随时间向极移动。

**[FACT] Fig. 6(c)**：加速率 $\gamma(\theta)$ 解析式（Appendix B 导出）：
$$\gamma \propto \frac{1}{\cos^2\theta + \delta \sin^2\theta}$$
其中 $\delta = \kappa_\perp/\kappa_\parallel \ll 1$。

**图示**：
- $\theta \to 90°$：$\gamma \to \text{最大}$
- $\theta \to 0°$：$\gamma \to \delta \times$ 最大值（最小）
- 两个 $\delta$ 值（$\delta=0.01, 0.001$）曲线显示 $\delta$ 越小，$\theta=90°$ 处加速率优势越明显

## 3.5 能谱按最终/初始极角分类（Fig. 7, 8, 9）

**[FACT] Fig. 7**（$s^2=1$, Run 2）：
- **上图**（按末极角）：
  - 蓝：赤道末态（$\cos\theta_f \in (-0.1, 0.1)$）
  - 红：极区末态（$\cos\theta_f \in (0.8, 1)$）
  - **极区粒子数（积分）远大于赤道**——尽管单粒子能量未必更高
- **下图**（按初极角）：
  - 蓝：初在赤道
  - 红：初在极区
  - **最高能量粒子来自赤道初始位置**

**[FACT] Fig. 8**（$s^2=0.3$, Run 5）：
- 低能粒子（$E < 500\,E_R$）**极区主导**（比 $s^2=1$ 更明显）
- 原因：低湍流方差 → 低 $\kappa_\perp$ → 准垂直注入效率低（"fewer particles injected at quasi-perpendicular shock"）
- 但加速率在准垂直仍最高（$\propto 1/\kappa_\perp$）

**[FACT] Fig. 9**：能谱按**初始位置相对局部磁场**分类（$\cos\theta_{L,0}$，局部 $B$ 与 $\hat{n}$ 夹角）。
- 显示：即使按**局部** $\theta_{Bn}$ 分类，**准垂直初始粒子最终仍聚集到极区**——再次印证"场线连接时间"机制

## 3.6 关键数值总结

| 量 | 数值 |
|---|---|
| 能量守恒精度 | $< 10^{-5}\%$ |
| 单圈回旋特征能量 | $\sim E_R$ 到 $5\,E_R$ |
| 幂律区上限 | $50$–$100\,E_R$ |
| 低湍流方差 s² | 0.3 |
| 高湍流方差 s² | 1 |
| $L_c/r_{g0}$ | $10^4$, $10^5$ |
| 湍流波长范围 | $0.5\,r_{g0}$ 到 $10^6\,r_{g0}$ |
| 内激波流速度 | $(3/4)V_{\text{sh}}$ |
| 冷却时标（下游膨胀） | $\sim R_{\text{sh}}/V_{\text{sh}}$ |

## 3.7 核心结果一句话

**[FACT] 三合一**：
1. **加速位置**：准垂直（赤道）区加速**最快**
2. **最终聚集**：粒子收集到极区，极区**通量最高**
3. **机制**：场线随激波膨胀向极移动 + 粒子沿场线漂移
