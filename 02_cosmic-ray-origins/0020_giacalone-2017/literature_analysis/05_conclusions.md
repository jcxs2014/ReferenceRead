> 上一章：[[04_implications]]
> 下一章：[[A1_appendix_numerical_model]]
---
title: "§5 Conclusions — Giacalone 2017"
section: '5. CONCLUSIONS'
---

## 5.1 主要结论

**[FACT]** 论文结尾 §5 总结了以下核心结论：

1. **球面几何的关键效应**：激波表面 $\theta_{Bn}$ 的变化导致**沿球面**的加速率显著变化

2. **加速位置**：
$$\dot{E}\big|_{\theta=90°} \gg \dot{E}\big|_{\theta=0°}$$
最高能粒子初始在**赤道/准垂直**区被加速

3. **聚集位置**：
> "the highest intensities of particles, accelerated by the shock, are at the poles of the blast wave"
粒子最终聚集到**极区**

4. **聚集机制**：
> "The particles collect at the poles as they approximately adhere to magnetic field lines that move poleward from their initial encounter with the shock at the equator"
场线随激波膨胀向极移动 + 粒子沿场线漂移

5. **Lc/Rsh 决定注入性质**：
- $L_c/R_{\text{sh}} \sim 1$：注入非局地化，准垂直/准平行效率相近
- $L_c/R_{\text{sh}} \gg 1$：注入局地化，由局部 $\theta_{Bn}$ 决定

6. **应用**：SNR 全球 X 射线不对称、CME/SEP 强度与 $\theta_{Bn}$ 弱依赖、TS 钝头 ACR 分布

## 5.2 公式回顾

- **注入阈值**（§1）：
$$E_{\text{inj}}(\theta=90°) = \frac{E_R}{2\left(1 + \kappa_\parallel/(A^2\kappa_\perp)\right)}$$
$$E_{\text{inj}}(\theta=0°) = 9\,E_R$$

- **加速率**（Appendix B）：
$$\gamma(\theta) \propto \frac{1}{\cos^2\theta + \delta\sin^2\theta}, \quad \delta = \kappa_\perp/\kappa_\parallel$$

- **球状爆震波流**（Appendix A）：
$$U(r,t) = V_{\text{sh}}\left[1 - \frac{1}{2}\left(1 + \tanh\left(\frac{V_{\text{sh}} t - r}{3\,\Delta_S}\right)\right)\right]$$

## 5.3 与库内文献的对话

| 库内文献 | 本文结论如何与它对话 |
|---|---|
| **Bell 1978** | 平面 DSA → 本文加入几何各向异性 γ(θ) |
| **Blandford & Ostriker 1978** | 早期 DSA 框架 → 本文推广到球面 |
| **Caprioli 2014** | 提供 θ 依赖的加速效率定量曲线 → 本文提供**几何直觉**（why θ 影响加速）|
| **Blasi 2013** | 非线性 DSA 综述 → 本文补充几何层面 |

## 5.4 未来方向（隐含）

**[INTERPRETATION]** 本文**没有**明确列出 future work，但从全文可推断：
1. **Sedov 减速相**：本文恒定 $V_{\text{sh}}$，真实 SNR 减速需处理
2. **自洽 MHD**：本文场运动学预设，粒子不反馈
3. **Parker 螺旋磁场**：§4 明确假设不适用
4. **注入微观物理**：本文忽略 cross-shock potential，Caprioli 2014 hybrid 结果可补充
