---
title: "3. Arrival Direction & LSS Correlation"
paper: "Telescope Array Collaboration 2023, Amaterasu event"
outline_ref: "§Comparison with previous events; Possible sources of the cosmic ray"
original_sections: ["§Direction and LSS analysis; §Comparison with Auger and other events"]
---

> 上一章：[[02_cosmic-ray-origins/0015_telescope-array-2023/literature_analysis/02_energy_reconstruction.md|02_energy_reconstruction]]
> 下一章：[[02_cosmic-ray-origins/0015_telescope-array-2023/literature_analysis/04_source_distance.md|04_source_distance]]

## 3.1 [FACT] 到达方向

Table 1 给出的观测到达方向（经度/赤道坐标）：

| 坐标系统 | 值 |
|---------|-----|
| 赤经 (R.A.) | $255.9 \pm 0.6°$ |
| 赤纬 (Dec.) | $16.1 \pm 0.5°$ |
| 天顶角 | $38.6 \pm 0.4°$ |
| 方位角（从东逆时针） | $206.8 \pm 0.6°$ |

**相对银河系**：方向接近银河系盘面（$\sim 5°$ 距离），银河系磁场（GMF）足以显著偏转 $244$ EeV 粒子（尤其若为重核）。

## 3.2 [FACT] Figure 2 — GMF 反推

论文使用 **两个银河系磁场模型** 和 **四种初级粒子** 进行反推：

| GMF 模型 | 来源 |
|---------|------|
| JF2012 | Jansson & Farrar 2012 |
| PT2011 | Pshirkov et al. 2011 |

| 粒子 | 反推方向 | 特征 |
|------|---------|------|
| 质子 (P) | 红色符号 | 偏转较小 |
| 碳 (C) | 紫色符号 | 中等偏转 |
| 硅 (Si) | 绿色符号 | 较大偏转 |
| 铁 (Fe) | 蓝色符号 | 偏转最大 |

**偏转大小**（论文正文）：
- 铁核：$\lesssim 20°$
- 质子：$\lesssim 1°$

## 3.3 [FACT] PKS 1717+177 — 唯一接近的 $\gamma$ 射线源

| 字段 | 内容 |
|------|------|
| 类型 | Flaring 活动星系 |
| 距离 | $\sim 600$ Mpc ($z = 0.137$) |
| 与反推方向夹角 | $\lesssim 2.5°$（质子假设） |
| 历史意义 | 已被提议为 CR 候选源（Farrar & Gruzinov 2009） |
| **结论** | **被排除**——距离远超 $244$ EeV 粒子的平均传播距离 $\sim 30$ Mpc |

## 3.4 [FACT] NGC 6946 — "烟花星系"

| 字段 | 内容 |
|------|------|
| 类型 | 星暴星系 |
| 距离 | $7.7$ Mpc（Eldridge & Xiao 2019） |
| 关联条件 | **仅**在 JF2012 GMF + 铁核假设下反推方向接近 |
| 限制 | **未在 $\gamma$ 射线波段被探测到**——不太可能是强 UHECR 源 |
| **结论** | 作为候选源**可能性低** |

## 3.5 [FACT] 局部空洞 (Local Void)

到达方向与 **Local Void** 位置（围绕 R.A. = $279.5°$, Dec. = $18.0°$）一致——这是 Local Group 与附近 LSS 纤维状结构之间的空洞（Tully et al. 2008）。

**空洞内已知星系极少**，且这些星系均非预期的 UHECR 加速场所。

## 3.6 [FACT] Figure 3 — TA 其他 $> 100$ EeV 事件

| 参数 | 值 |
|------|-----|
| 事件数 | $28$ 个（$2008.5$–$2021.11$） |
| 暴露 | $1.6 \times 10^4$ km$^2$ sr yr |
| 方向分布 | **各向同性**，无聚集 |
| 与 Amaterasu 的聚集 | **未发现** |
| TA hot spot（R.A. $146.7°$, Dec. $43.2°$） | 来自 $> 57$ EeV 事件的 $3.4\sigma$ 过量；Amaterasu 来自**不同方向** |

## 3.7 [FACT] 与 LSS 流量分布的对比

Figure 2 色度图展示了从**局部 LSS 不均匀源密度分布**计算的相对预期流量，对 $244$ EeV 铁核做了能量衰减修正，并用银河系随机磁场涂抹（turbulent smearing）。

**关键结论**：
- 到达方向**位于最低流量区域**（空洞）
- 反推方向即使考虑 GMF 偏转，仍不与高流量区域重叠
- 只有 JF2012 + 铁核反推方向接近 LSS 有星系区域

## 3.8 [INTERPRETATION] 我的理解

方向分析的核心矛盾：

> **$244$ EeV 粒子的到达方向指向局部空洞，即使考虑银河系磁场偏转后，仍无法与任何已知天体对应。**

这带来三种可能：
1. 银河系磁场比 JF2012/PT2011 模型更强（反推偏转更大）
2. 粒子来自极近距离（$< 10$ Mpc）的未知源
3. 粒子物理不完整的理解（超越标准模型的新物理）