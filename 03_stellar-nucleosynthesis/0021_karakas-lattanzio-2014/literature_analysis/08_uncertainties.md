# 8. Major Uncertainties（§4 主要不确定性）

**上一章**: [07_pies_superagb_fates.md](07_pies_superagb_fates.md) · **下一章**: [09_yield_tables.md](09_yield_tables.md)

## 8.1 Convection and the third dredge-up

### 8.1.1 对流边界判定
[FACT] 1D 恒星模型对流边界由 **Schwarzschild 判据** 判定；但实际恒星内部有混合层（convective overshoot、semiconvection）需要额外参数化。

[FACT] 对流超射（overshoot）的实现在不同恒星演化代码中差异巨大，直接影响：
- He 核心尺寸；
- ¹³C 袋深度与质量；
- λ（TDU 效率）；
- s-过程产额（对 Sr、Ba、Pb 特别敏感）。

### 8.1.2 对流引起的结构变化
[FACT] 对流边界附近的核反应区结构变化会反馈到 AGB 演化时标与产额。

## 8.2 Mass Loss（质量损失）

[FACT] AGB 质量损失率 $\dot{M}$ 决定恒星在包络耗尽前经历多少次 TDU。

[FACT] 参数化：
- Reimers (1975): $\dot{M} \propto L R / M$
- Blocker (1995): 用于 O 富星
- Vassiliadis & Wood (1994): Vw 关系（依赖包络质量）

[FACT] Spitzer 卫星观测揭示：低金属度下 C 富 AGB 的质量损失并不一定小于高 Z 值（因 C 富包络尘埃驱动更强）。

## 8.3 关键系统不确定性

| 参数 | 影响 | 当前状态 |
|-----|------|---------|
| 对流边界 (overshoot) | λ, ¹³C 袋, s-过程产额 | 未校准 |
| 半对流（semiconvection） | He 核尺寸 | 时标不确定 |
| 呼吸脉冲（breathing pulses） | He 核尺寸 | 观测不支持（Renzini & Fusi Pecci 1988） |
| 质量损失率 | TDU 次数 | 依赖经验公式 |
| ¹²C(α,γ)¹⁶O 反应率 | intershell C/O | 实验约束差 |

[CRITIQUE] 本文明确指出 §6 中的展望：对流与质量损失是所有 AGB 产额系统误差的两大主导源。

## 8.4 关键方程（LaTeX）

[FACT] **Schwarzschild 对流判据**：原文 p.16
$$ \nabla_{\rm rad} \;>\; \nabla_{\rm ad} \qquad \Longleftrightarrow \qquad \text{convective unstable} $$

[FACT] **Ledoux 判据**（加入 $\nabla_\mu$ 分子重量梯度）：原文 p.16
$$ \nabla_{\rm rad} \;>\; \nabla_{\rm ad} + \varphi\,\nabla_\mu \qquad \Longleftrightarrow \qquad \text{Ledoux unstable} $$

[FACT] **Reimers 质量损失率**（RGB/AGB 经典参数化）：原文 p.27
$$ \dot{M}_{\rm Reimers} \;\approx\; 4\times 10^{-13}\,\eta_R\,\frac{L\,R}{M}\;\Big[\frac{M_\odot}{\mathrm{yr}}\Big] \qquad (\eta_R \simeq 0.4\text{--}1.0) $$

[FACT] **Vassiliadis–Wood (1994) 关系**（$L/L_\odot$ 依赖包络质量）：原文 p.27
$$ \dot{M}_{\rm VW} \;=\; 4\times 10^{-13}\,L\,R\,\Big(\frac{M_{\rm env}}{M_0}\Big)^{-0.5} $$

[FACT] **Blocker (1995) 关系**（用于 O-富 AGB）：原文 p.27
$$ \dot{M}_{\rm Blocker} \;=\; 6\times 10^{-14}\,\frac{L\,R}{M}\Big(\frac{X_{\rm H}}{0.70}\Big)^2 $$

[FACT] **对流超射长度参数化**（指数衰减）：原文 p.16
$$ P_{\rm overshoot}(d) \;=\; P_0\,\exp\!\Big(-\frac{2d}{\alpha_{\rm ov}\,H_P}\Big) $$

[FACT] **semiconvection 扩散系数**：原文 p.8
$$ D_{\rm sc} \;\propto\; \frac{\nabla_{\rm rad} - \nabla_{\rm ad}}{|\nabla_\mu|} $$

## 8.5 不确定性量化公式

**[FACT] Blockler 质量损失率公式**（本文 §8.1 / O-富 AGB）：

$$\dot{M}_{\rm Blocker} = 6 \times 10^{-14}\,\frac{L\,R}{M}\left(\frac{X_{\rm H}}{0.70}\right)^{2}$$

$L$ (L$_\odot$)、$R$ ($R_\odot$)、$M$ ($M_\odot$)。本文 §8.1 据此给出 O-富 AGB 风的高质量损失率上限。

**[FACT] 对流超射长度参数化**（本文 §8.1 / 指数衰减）：

$$P_{\rm overshoot}(d) = P_0\,\exp(-2d/(\alpha_{\rm ov}\,H_P))$$

$\alpha_{\rm ov}$ 为超射参数，$H_P$ 为压强标高。本文 §8.1 用 $\alpha_{\rm ov} \in [0.0, 0.25]$ 测试对流边界对 TDU 深度的影响。

**[FACT] 反应率—核合成产额灵敏度公式**（本文 §8.2）：

$$\Delta \log Y_i = \sum_{j} \frac{\partial \log Y_i}{\partial \log \langle\sigma v\rangle_j}\,\Delta \log \langle\sigma v\rangle_j$$

灵敏度矩阵——本文 §8.2 用此量化 ${}^{22}\mathrm{Ne}(\alpha, n)$、${}^{13}\mathrm{C}(\alpha, n)$ 等关键反应率 30% 不确定性对 s-过程产额的影响。

**[FACT] TDU 深度参数化**（本文 §8.3）：

$$\lambda = \Delta M_{\rm dredge}/\Delta M_{\rm H}$$

TDU 效率 $\lambda$ 定义为每个 TP 周期 dredge-up 质量与 H 包络质量之比。本文 §8.3 用 $\lambda \in [0.5, 0.9]$ 测试低/中质量 AGB 的 s-过程产额散布。

**[FACT] 不确定性总传递链**（本文 §8.4）：

$$\sigma_{\rm tot}(\log Y_i) = \sqrt{\sum_k (\partial_k \log Y_i)^2 \sigma_k^2}$$

各不确定性源（反应率、质量损失、对流、初始丰度）独立贡献的均方根合成。本文 §8.4 给出对 $Y_i$ 的 1-σ 不确定性上限（典型 0.3-0.5 dex）。
