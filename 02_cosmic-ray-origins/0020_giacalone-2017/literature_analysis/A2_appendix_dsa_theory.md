> 上一章：[[A1_appendix_numerical_model]]
> 下一章：[[97_quality_check]]
---
title: "Appendix B — DSA Theory"
section: 'Appendix B'
---

## B.1 背景：Bell 1978 DSA 加速率

**[FACT]** Bell 1978 给出 DSA 加速率的一般形式：
$$\gamma^{-1} = \frac{3}{u_1 - u_2}\left(\frac{\kappa_{x1}}{u_1} + \frac{\kappa_{x2}}{u_2}\right)$$
其中：
- $u_1, u_2$：激波上游/下游流体速度（激波静止系）
- $\kappa_{x1}, \kappa_{x2}$：激波法向扩散系数（上/下游）
- $\rho = u_1/u_2$：压缩比（强激波 $\rho=4$）

**[FACT]** 空间扩散张量分解（Giacalone & Jokipii 1999）：
$$\kappa_{ij} = \kappa_\perp\,d_{ij} + (\kappa_\parallel - \kappa_\perp)\,\hat{b}_i\,\hat{b}_j$$
其中 $\hat{\mathbf{b}} = \mathbf{B}/B$。

**[FACT]** 激波法向扩散系数 $\kappa_{xx}$：
$$\kappa_{xx} = \kappa_\parallel \cos^2\theta + \kappa_\perp \sin^2\theta$$
其中 $\theta$ 是 $\mathbf{B}$ 与激波法向夹角。

**[FACT]** 简化假设：$\kappa_{xx2} \approx \kappa_{xx1}$（下游湍流增强补偿）

**[FACT]** 由此得到：
$$\gamma \propto \frac{\rho\,u_1^2}{\kappa_\parallel \cos^2\theta + \kappa_\perp \sin^2\theta}$$

## B.2 关键表达式（Fig. 6(c) 所用）

**[FACT]** 令 $\delta = \kappa_\perp/\kappa_\parallel \ll 1$，$g_\parallel$ 为 $\theta=0°$ 时加速率：
$$\gamma(\theta) = \frac{g_\parallel}{\cos^2\theta + \delta\,\sin^2\theta}$$

**[FACT]** 极限行为：
- $\theta \to 0°$（平行）：$\gamma \to g_\parallel$（最小）
- $\theta \to 90°$（垂直）：$\gamma \to g_\parallel / \delta \gg g_\parallel$（最大）
- $\delta$ 越小，准垂直优势越大

**[FACT]** Fig. 6(c) 中两个 $\delta$ 值：
- $\delta = 0.01$（$s^2=1$，强湍流）
- $\delta = 0.001$（$s^2=0.3$，弱湍流）

## B.3 数值代入

**[FACT]** Giacalone & Jokipii 1999 的扩散系数标度：
$$\kappa_\parallel \sim \frac{1}{3}\,r_{g0}\,V_{\text{sh}}, \quad \kappa_\perp \sim \delta\,\kappa_\parallel$$

**[FACT]** 本文假设 $\delta$ 与能量无关（Giacalone & Jokipii 1999 数值模拟支持）。

## B.4 与 Caprioli 2014 的定量联系

**[FACT]** Caprioli 2014 通过 PIC/hybrid 模拟直接测量 $\epsilon(\theta, M)$：
- 准平行（$\theta \lesssim 45°$）：$\epsilon \sim 10\%$–$20\%$
- 准垂直（$\theta \gtrsim 45°$）：$\epsilon$ 急剧下降至 $\lesssim 1\%$

**[FACT]** 本文 γ(θ) 与 Caprioli 结果的**定性一致**：加速率在准垂直最高，但在本文几何中粒子能到达极区是因为**场线-激波连接时间**长。

**[INTERPRETATION]** 两者看似矛盾实则互补：
- **Caprioli**：在**固定** θ 平面激波中测加速效率——准垂直效率低（注入难）
- **本文**：在**球面演化**几何中，粒子**初始在赤道（准垂直）快速加速**，然后随场线漂移到极区**积累**——**积累时间**取代了**注入难度**成为极区高强的原因
