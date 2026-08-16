---
chapter: 1
title: "INTRODUCTION"
pages: "241-243 (PDF p2)"
---

# 1. INTRODUCTION

上一章：[00_overview](00_overview.md)
下一章：[02_heavy_element_formation](02_heavy_element_formation.md)

## 1.1 元素分类语言

[FACT] 文中建立一套恒星核合成的术语分类体系（沿用 B²FH 传统）：
- **α elements**（Z 为偶数、主要同位素为 ⁴He 倍数）：C, O, Mg, Si, S, Ca（非正式含 Ti，主同位素 ⁴⁸Ti）。
- **proton-capture**（Z ≤ 13 且丰度受 H 燃烧显著影响）：C, N, O, F, Na, Mg, Al。
- **Fe-peak**：21 ≤ Z ≤ 30（Ti、Cu 是否算入存疑）。
- **neutron-capture (n-capture)**：Z > 30，共有 54 种稳定或长寿命（τ₁/₂ > 10⁶ yr）n-capture 元素，仅 30 个较轻元素，但在太阳物质中数密度占比仅约 10⁻⁶%。

## 1.2 综述目标

[FACT] 低金属度银晕（metal-poor halo）中 n-capture 元素含量呈现巨大的星间散布（scatter）：既体现在 n-capture 元素总量对轻元素的比值，也体现在 n-capture 元素彼此之间的比值。
[FACT] 数种"well-defined"丰度分布已经浮现，揭示了特征性的 r-process 与 s-process 合成模式。
[FACT] 本文综述这些金属贫星的丰度观测，与太阳系统值对比、与理论预测对照、用于识别引发特定异常的天体类型，并探讨早期银河系核合成的时间尺度与性质。

## 1.3 观测门槛

[FACT] n-capture 元素观测的核心难点：太阳物质中这些元素数密度极低（≈10⁻⁶%），即便在 n-capture 富集星中也需要高分辨光谱（R ≳ 60,000）配合精确原子数据（跃迁几率、超精细与同位素结构）才能定量测量。

## 1.4 逻辑结构

[FACT] 极低金属晕星（ultralow-metallicity）三例：HE 0107-5240（[Fe/H]≃−5.3, Christlieb et al. 2002）；HE 1327-2326（[Fe/H]≃−5.5, Frebel et al. 2005）；HE 0557-4840（[Fe/H]≃−4.8, Norris et al. 2007）。三者均极 C-rich（[C/Fe] > +1.5）；HE 1327-2326 中 Sr 超丰（[Sr/Fe]≃+1），Sr 来源可能为超新星或 r-process 而非 s-process。由于其它 n-capture 元素均未探测，本文不再深入讨论（原文§1，p.242）。
[FACT] 综述坐标：VandenBerg, Bolte & Stetson (1996) 球团年龄；McWilliam (1997) 丰度与化学演化；Wallerstein & Knapp (1998) C-rich 星；Freeman & Bland-Hawthorn (2002) 恒星族；Bromm & Larson (2004) 早期银河与恒星形成；Gratton, Sneden & Carretta (2004) 球团丰度；Beers & Christlieb (2005) 银河晕巡天（原文§1，p.242）。
[FACT] 观测窗口：n-capture 元素观测主要限于冷巨星（T_eff < 5000 K，log g < 3），高温主序星光谱线过弱导致目前观测集中于红巨星支与 AGB 下方区域。
[FACT] 化学演化探针：n-capture 元素对恒星参数（T_eff、log g、[Fe/H]）高度敏感——一个 dex 的 T_eff 误差可带来 n-capture 元素 [X/Fe] 数 dex 的误差；因此精确恒星大气参数是后续所有定量分析的前提。
[FACT] 本文 9 章路线图：§2 核合成机制 → §3 太阳系统丰度 → §4 r-process 观测 → §5 s-process 观测 → §6 r-process 丰度含义 → §7 早期银河核合成 → §8 s-process 丰度含义 → §9 结论（原文§1，p.242）。

[INTERPRETATION] 本节的核心功能是"划定战场"：把元素周期表的后半段标成 n-capture 领域，指出这个领域虽小（仅 10⁻⁶%）却包含 54 种元素，是恒星核合成研究中信息密度最高的区域，也是银河系化学演化最敏感的探针。极低金属度（[Fe/H] < −5）三例说明，即使在银河形成最早期，个别星已经显示 C-rich + Sr 超丰的核合成印记。

## 1.5 关键定量公式（贯穿全综述）

> 本节列出全文反复使用的核心公式，详尽推导与适用条件见 §3、§4、§5、§7 的对应章节。

**[FACT] 等值宽度—丰度反演公式**（标准曲线生长法，本文 §3.3 详述）：

$$\log\frac{N_i}{N_H} = \log\frac{W_\lambda}{\lambda} - \log(gf) + \log(\Gamma) - \Theta_{\rm exc} + C$$

其中 $W_\lambda$ 为等值宽度（mÅ），$\lambda$ 为波长（Å），$gf$ 为振子强度，$\Gamma$ 为阻尼展宽常数，$\Theta_{\rm exc} = 5040/T_{\rm exc}$（K）为激发温度倒数，$C$ 为电离平衡 + 恒星大气模型常数（依元素、谱线、模型而变）。这是本文所有 n-capture 元素丰度测定的起点。

**[FACT] 太阳系 n-capture 残差标度**（B²FH 经典，沿用至本文 §3）：

$$N_s \cdot \sigma_s = N_r \cdot \sigma_r + N_p$$

其中 $N_s, N_r, N_p$ 分别为 s-only、r-only、p-only 同位素太阳系丰度，$\sigma_s, \sigma_r$ 为 s、r 过程的中子照射量。该式由 B²FH (1957) 引入，是分离 s/r 残差的基础——本文 §3 Table 1 列出 12 个 s-only 同位素的 $\sigma_s$。

**[FACT] r-only 归一比**（本文 §3、§4 多次引用）：

$$R_r(i) = \log(N_{\odot,i}/N_{\odot,i}^{\rm s-only})$$

对纯 r 同位素 $i$（如 $^{138}$La、$^{180}$Ta 除外的大多数重 n-capture），$R_r(i)$ 反映 r-process 核合成相对产额。

**[FACT] s-only 归一比**（本文 §3、§5 多次引用）：

$$R_s(i) = \log(N_{\odot,i}/N_{\odot,i}^{\rm r-only})$$

对纯 s 同位素（$^{86}$Sr、$^{96}$Mo、$^{142}$Nd 等），$R_s(i)$ 反映 s-process 核合成相对产额。

**[FACT] Th/Eu 核宇宙年表公式**（本文 §7.2 核心公式）：

$$\Delta t = \frac{\log(\mathrm{Th/Eu})_{\rm now} - \log(\mathrm{Th/Eu})_0}{\log(e)\,\lambda_{\rm Th}}$$

其中 $\lambda_{\rm Th} = \ln 2 / t_{1/2}(\mathrm{Th}) = 1/14.05\,\mathrm{Gyr}^{-1}$ 为 Th-232 衰变常数。本文 §7 用此公式估算 r-process 现场年龄——典型金属贫星 $\log(\mathrm{Th/Eu}) \approx -0.4$ 给出 $\Delta t \approx 10$–$15$ Gyr。

**[FACT] 金属度标度**（贯穿全文）：

$$[\mathrm{X/Fe}] = \log(N_{\rm X}/N_{\rm Fe})_{\rm star} - \log(N_{\rm X}/N_{\rm Fe})_{\odot}$$

本文所有"[X/Fe]"值均按此定义（原文§1，p.242）。

[INTERPRETATION] 这 6 个公式不是"装饰"——它们贯穿全文 §3、§4、§5、§6、§7、§8，是判定任何金属贫星丰度分布是否"well-defined"的量化基础。形式上的简洁不等于内容上的简单：每个公式背后都有一段独立的物理推导与适用条件讨论（详见后续章节）。

上一章：[00_overview](00_overview.md)
下一章：[02_heavy_element_formation](02_heavy_element_formation.md)
