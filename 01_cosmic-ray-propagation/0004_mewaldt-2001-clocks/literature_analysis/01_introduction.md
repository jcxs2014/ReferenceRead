---
title: "1. Introduction"
paper: "Mewaldt et al. 2001, Radioactive Clocks and Cosmic-Ray Transport in the Galaxy"
outline_ref: "§1 Introduction"
original_sections: ["§1. Introduction (全文 L21–75, 55 行, 3 段)"]
---
> 本章属于：[[01_cosmic-ray-propagation/0004_mewaldt-2001-clocks/literature_analysis/00_overview.md|Radioactive Clocks and Cosmic-ray Transport in the Galaxy]]
> 上一章：[[01_cosmic-ray-propagation/0004_mewaldt-2001-clocks/literature_analysis/00_overview.md|00_overview]]
> 下一章：[[01_cosmic-ray-propagation/0004_mewaldt-2001-clocks/literature_analysis/02_acceleration_delay_clocks.md|02_acceleration_delay_clocks]]

## 1.1 [FACT] 上下文：宇宙线的能量源与加速机制共识

在 2001 年这篇综述发表之时，宇宙线研究领域已经形成了两条基本共识：

**(a) 能量源**：维持银河系宇宙线能量密度（约 $3 \times 10^{40}$ erg s$^{-1}$）所需的唯一能量源是**超新星（SN）爆发**。银河系 SN 爆发频率约 1 次 / (100 年)，每次释放动能 $\sim 10^{51}$ erg，转化为宇宙线的效率约 10%，恰能补上持续损失。

**(b) 加速机制**：大部分宇宙线的能量来自**激波加速**（shock acceleration，即 DSA——扩散激波加速），与日球层中大多数高能粒子的加速机制相同。这一机制在 1970 年代末即由 Bell、Krymsky、Piacentini & Rudak、Axford–Bell 独立提出，到 2001 年已成为标准图像。

## 1.2 [FACT] 仍未解答的四个核心问题

尽管能量源和加速机制已确立，Mewaldt 将"起源之谜"归纳为四个仍然悬而未决的问题（§1 第一段）：

| # | 问题 | 物理含义 |
|---|------|---------|
| Q1 | **加速物质的来源**：新鲜超新星抛射物？"老的"星际物质？还是二者混合？ | 决定宇宙线成分是否保留源天体的核合成特征 |
| Q2 | **一次性还是分布式加速**：单次 SN 激波一次到位？还是在其寿命中被一系列 SN 激波逐步加速？ | 一次性意味着 SN 必须加速自己的抛射物；分布式意味着宇宙线可以在银河系内"游荡"多代 |
| Q3 | **宇宙线填充的体积**：是否包含银河系晕（halo）以及圆盘（disk）？ | 直接决定晕尺度 $L$ 与平均密度 $\rho$ 的约束 |

## 1.3 [FACT] 放射性同位素作为宇宙线"时钟"的物理基础

上述问题都与**时间尺度**直接相关。Mewaldt 指出三类过程各自有独立的时间尺度：

1. **核合成到加速的时间延迟** $\Delta t_{\rm nuc \to acc}$（从同位素衰变读取）
2. **加速过程本身的时间尺度** $\Delta t_{\rm acc}$
3. **宇宙线在银河系内储存的寿命** $\tau_{\rm esc}$（从放射性衰变读取）

放射性同位素是测量这些时间尺度的直接探针。Mewaldt 将宇宙线同位素按物理意义分为四类：

| 类别 | 代表同位素 | 物理用途 |
|------|-----------|---------|
| 稳定初级核 | 绝大多数初级核 | 作为分母（初级/次级比中的"初级"） |
| 长寿命初级放射性核 | $^{232}$Th、$^{238}$U、$^{237}$Np、$^{248}$Cm | 约束极长寿命尺度（$\sim 10^9$ 年），但统计量极低 |
| 电子俘获初级核（Fe 区） | $^{59}$Ni、$^{57}$Co、$^{56}$Ni | 约束核合成到加速的延迟（见 §2） |
| **β 衰变次级放射性核** | $^{10}$Be、$^{26}$Al、$^{36}$Cl、$^{54}$Mn | **约束宇宙线储存寿命 $\tau_{\rm esc}$**（见 §4） |
| 电子俘获核（作为密度计） | $^{7}$Be、$^{37}$Ar、$^{44}$Ti、$^{49}$V、$^{51}$Cr、$^{55}$Fe、$^{57}$Co | 探测能量变化过程与再加速（见 §3） |

## 1.4 [FACT] ACE/CRIS 仪器——本综述的数据基础

1997 年发射的 **Advanced Composition Explorer (ACE)** 携带 **Cosmic Ray Isotope Spectrometer (CRIS)**，是本综述几乎所有新测量结果的数据来源。CRIS 的关键性能参数：

- **质量分辨率**：$m / \Delta m = 0.1$–$0.25$ amu（对 $2 \le Z \le 30$），足以分辨同位素
- **几何因子**：$\sim 250$ cm$^2$ sr，足以测量稀有核种
- 这些性能使得 **四个 β 衰变时钟**（$^{10}$Be、$^{26}$Al、$^{36}$Cl、$^{54}$Mn）的统计精度达到前所未有的水平

## 1.5 [INTERPRETATION] 综述结构

Mewaldt 的综述结构清晰，围绕三类"时钟"数据展开：

- **§2**：加速时间延迟时钟（$^{59}$Ni 电子俘获）—— 回答 Q1（物质来源）与 Q2（一次性 vs 分布式）
- **§3**：电子俘获核作为传输过程探针（$^{51}$Cr 等）—— 探测再加速
- **§4**：β 衰变时钟（$^{10}$Be 等四种）—— 回答 Q3（晕尺度与密度）
- **§5**：总结

本论文的核心贡献不是提出新模型，而是**对 ACE/CRIS 测量结果的第一次系统综合**，并明确指出了这些结果对当时主流模型的约束。
