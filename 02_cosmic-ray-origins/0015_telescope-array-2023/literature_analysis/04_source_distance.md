---
title: "4. Source Distance — GZK 能量损失长度与源距离约束"
paper: "Telescope Array Collaboration 2023, Amaterasu event"
outline_ref: "§Supplementary Text: Expected cosmic ray sources (distance calculation)"
original_sections: ["§Methods: Distance to closest UHECR source"]
---

> 上一章：[[02_cosmic-ray-origins/0015_telescope-array-2023/literature_analysis/03_direction_and_lss.md|03_direction_and_lss]]
> 下一章：[[02_cosmic-ray-origins/0015_telescope-array-2023/literature_analysis/05_discussion_and_conclusions.md|05_discussion_and_conclusions]]

## 4.1 [FACT] 源距离计算方法

TA 合作组通过**积分能量损失长度**估计最近的 UHECR 源距离：

$$D_0 = \int_{E_{\rm obs}}^{E_0} \frac{dE}{-\left(\frac{dE}{dx}\right)_{\rm loss}}$$

其中 $E_{\rm obs} = 244$ EeV 是观测能量，$E_0 = 10^3$ EeV（$1000$ EeV）是假设的注入能量上限。

**使用软件**：TransportCR（Kalashev & Kido 2015）计算能量损失长度；用 SimProp（Aloisio et al. 2017）交叉验证（结果差异 $\sim 10\%$）。

## 4.2 [FACT] 铁核与质子的源距离

| 初级粒子 | $D_0$（统计误差） | $D_0$（含系统误差） | 95% C.L. 上限 |
|---------|-------------------|-------------------|--------------|
| **铁核** ($Z = 26$) | $10.3^{+5.3}_{-3.0}$ Mpc | $10.3^{+25.2}_{-4.5}$ Mpc | $< 25.5$ Mpc |
| **质子** ($Z = 1$) | $27.0^{+3.8}_{-3.0}$ Mpc | $27.0^{+7.6}_{-4.9}$ Mpc | $< 36.0$ Mpc |

**含系统误差时铁核的上方误差大幅扩大**（$+25.2$ Mpc）——因为系统误差（$-10\%$ 能量）对应注入能量更低，从而允许更远距离。

## 4.3 [FACT] 注入能量敏感性

若假设更高注入能量 $E_0 = 10^4$ EeV（$10,000$ EeV）：

| 初级粒子 | $D_0$（统计误差） |
|---------|-------------------|
| 铁核 | $13.1^{+5.3}_{-3.0}$ Mpc（**仅微幅变化**） |
| 质子 | $61.9^{+3.8}_{-3.0}$ Mpc（**大幅变化**） |

**物理解释**：
- 铁核的能量损失主要由光核反应 $A + \gamma \to A' + N$ 主导，损失长度几乎与能量无关（在 $10^3$–$10^4$ EeV 范围内）
- 质子在 $> 10^3$ EeV 时 $\Delta$ 共振截面随能量变化，导致注入能量从 $10^3$ 到 $10^4$ EeV 时距离显著变化

## 4.4 [FACT] 质子方案被 disfavored 的原因

TA 合作组明确指出：**质子方案不太可能被支持**，理由：

1. **Auger 与 TA 成分测量不一致**：Auger 在最高能量端观测到成分变重，而 TA 倾向较轻——但即使如此，铁核的距离约束更严格
2. **方向分析**：铁核的磁场偏转更小（$r_L \propto 1/Z$），反推方向更接近观测方向，但仍不与 LSS 重叠
3. **能量损失**：质子在 $244$ EeV 的损失长度较短（$\sim 10$ Mpc），更严格限制源必须极近

## 4.5 [FACT] 最近源的可能候选

若铁核假设（$D_0 \sim 10$ Mpc）：

| 候选 | 距离 | 特征 |
|------|------|------|
| 银河系内源 | $< 30$ kpc | 违反 Hillas 判据（$BL$ 要求无法满足 $244$ EeV 加速） |
| M87（室女座 A） | $\sim 16.4$ Mpc | AGN，但方向不匹配 |
| Cen A（NGC 5128） | $3.9$ Mpc | 最近 AGN；方向**不匹配**（位于南天 Dec. $\sim -43°$） |
| 局部星系群 | $\sim 0.5$–$5$ Mpc | 无已知 UHECR 候选源 |

**关键**：在 $10$–$30$ Mpc 范围内，**没有已知天体**能同时在方向和 Hillas 判据上满足 $244$ EeV 加速。

## 4.6 [FACT] Hillas 判据的约束

Hillas 判据要求（Hillas 1984）：

$$B_\mu \cdot L_{\rm pc} > 2 \frac{E_{15}}{Z \beta}$$

对于 $E = 244$ EeV = $244 \times 10^{15}$ eV：

$$B_\mu \cdot L_{\rm pc} > 2 \times 244 / (Z \beta) = 488 / (Z \beta)$$

| 天体类型 | $B$ ($\mu$G) | $L$ (pc) | $BL$ | 能否加速 $Z=1$? |
|---------|-------------|---------|------|----------------|
| SNR | $100$ | $3$ | $300$ | **否**（需 $488$） |
| AGN hotspot | $10^4$ | $10^6$ | $10^{10}$ | 是 |
| GRB | $10^{10}$ | $10^8$ | $10^{18}$ | 是 |
| 银河系中心 | $\sim 3000$ | $\sim 1$ | $\sim 3000$ | 是（边缘） |

## 4.7 [INTERPRETATION] 我的理解

源距离分析的核心结论：

> **Amaterasu 事件的源必须在 $10$–$30$ Mpc 内，但在此距离范围内无已知对应天体——除非是银河系内源（违反 Hillas 判据）或尚未发现的新类型加速源。**

这个"距离-方向"双重约束使得 Amaterasu 事件的解释变得非常困难：
- 河外源：方向不匹配
- 银河系内源：Hillas 判据不满足
- 新物理（暗物质衰变、弦理论等）：可能性极低，但论文未完全排除