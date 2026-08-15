---
title: "2. Acceleration-Time Delay Clocks — 59Ni 电子俘获时钟"
paper: "Mewaldt et al. 2001, Radioactive Clocks and Cosmic-Ray Transport in the Galaxy"
outline_ref: "§2 Acceleration-Time Delay Clocks"
original_sections: ["§2 (L83–155, 72 行)"]
---
> 本章属于：[[01_cosmic-ray-propagation/0004_mewaldt-2001-clocks/literature_analysis/00_overview.md|Radioactive Clocks and Cosmic-ray Transport in the Galaxy]]
> 上一章：[[01_cosmic-ray-propagation/0004_mewaldt-2001-clocks/literature_analysis/00_overview.md|00_overview]]
> 下一章：[[01_cosmic-ray-propagation/0004_mewaldt-2001-clocks/literature_analysis/03_electron_capture_transport.md|03_electron_capture_transport]]

## 2.1 [FACT] 物理原理：电子俘获核作为核合成–加速延迟时钟

**历史起源**：Soutoul et al. (1978) 首次提出利用 Fe 区三个电子俘获（electron-capture, EC）核作为宇宙线时钟的想法。这三个核均为爆炸性核合成的产物：

| 核 | 半衰期 | 衰变方式 |
|----|--------|---------|
| $^{56}$Ni | $\sim 6$ 天 | EC → $^{56}$Co |
| $^{57}$Co | $0.74$ 年 | EC → $^{57}$Fe |
| $^{59}$Ni | $7.6 \times 10^4$ 年 | EC → $^{59}$Co |

**关键物理**：能量 $> 500$ MeV/核子的宇宙线在其绝大部分传播时间内是**完全剥离电子的裸核**。对于裸核，电子俘获通道被阻断——它们无法俘获电子，因此不会通过 EC 衰变。只有在宇宙线减速到足够低能、重新捕获电子后，EC 衰变才会开启。

因此，如果在宇宙线中观测到某 EC 核仍然存活，就说明从核合成到加速到高能的时间延迟 $\Delta t_{\rm nuc \to acc}$ **小于**该核的半衰期；反之，如果观测到其衰变产物（EC 子核）而母核缺失，说明延迟 **大于**半衰期。

## 2.2 [FACT] 观测事实：59Co 稀缺暗示 59Ni 已衰变

**观测**（Wiedenbeck et al. 1999, Figure 1）：ACE/CRIS 测量了宇宙线中 Co 和 Ni 的质量分布。**59Co 严重匮乏**，而 $^{59}$Ni 也极稀少。

这看似矛盾——如果 $^{59}$Ni 还在，应该有 $^{59}$Ni；如果 $^{59}$Ni 已完全衰变为 $^{59}$Co，应该有 $^{59}$Co。但 $^{59}$Co 也稀缺。

**解释**：这说明 $^{59}$Ni 已经通过 EC 衰变为 $^{59}$Co，但 $^{59}$Co 又**进一步通过 EC 衰变为 $^{57}$Fe**（$^{57}$Co 半衰期 0.74 年）。最终稳定的终点是 $^{57}$Fe——它混在宇宙线中大量存在的稳定 $^{57}$Fe 中，无法分辨来源。

## 2.3 [FACT] 定量约束：从 59Co 匮乏到 10$^{5}$ 年的延迟

Wiedenbeck et al. (2000) 给出了 $^{59}$Ni/$^{59}$Co 测量对 $\Delta t_{\rm nuc \to acc}$ 的定量约束（Figure 2）：

| 假设的质量-59 核中 $^{59}$Ni 初始占比 | 要求的最小延迟 |
|------|--------------|
| $\ge 20\%$ | $\gtrsim 3 \times 10^4$ 年 |
| $\ge 40\%$ | $\gtrsim 10^5$ 年 |

**Woosley & Weaver (1995) 的理论预言**：
- 对于初始质量 $11$–$25$ $M_\odot$ 的 II 型 SN，质量-59 核中以 $^{59}$Ni 形式合成的比例从 27% 到 87% 变化
- 采用 Salpeter 初始质量函数积分后，**$\sim 68\%$ 的质量-59 核以 $^{59}$Ni 形式合成**

因此，宇宙线中的核合成产物中 $^{59}$Ni 占比约为 68%，**要求 $\Delta t_{\rm nuc \to acc} > 10^5$ 年**。

## 2.4 [FACT] 对宇宙线起源模型的关键判决

$\Delta t_{\rm nuc \to acc} > 10^5$ 年的结论对几类起源模型产生决定性影响：

**与以下模型不兼容**：
- **SN 加速自己的抛射物**（"fresh ejecta" 模型）：SN 爆发后激波在 $10^4$ 年内即可加速粒子；$10^5$ 年的延迟远超激波有效加速时间

**与以下模型兼容**：
1. **ISM 加速模型**（Olive & Schramm, 1982）：宇宙线从星际介质中加速，ISM 物质早已合成，延迟 $\gg 10^5$ 年
2. **恒星耀斑预加速模型**（Meyer, 1985）：低速种子粒子被恒星耀斑预加速后再被 SN 激波加速，种子本身来自 ISM，延迟大
3. **星际尘埃颗粒模型**（Meyer et al. 1997）：宇宙线中的难熔元素来自星际尘埃颗粒——这些颗粒年龄远超 $10^5$ 年
4. **超级气泡（super-bubble）模型**（Higdon et al. 1998）：一系列 SN 在一个超级气泡内爆发，时间跨度 $\sim 10^5$ 年；气泡早期 SN 的抛射物在气泡中"游荡"直到被后续 SN 的激波加速

## 2.5 [FACT] 在途衰变的可能性

Mewaldt 讨论了一个重要细节：$^{59}$Ni 是否可能在传播过程中**在途**（in-flight）俘获电子而衰变？

**分析**（Wiedenbeck et al. 2000）：
- CRIS 测量的平均能量 $\sim 300$ MeV/核子，对应日球层外 $\sim 400$–$500$ MeV/核子
- 在 $\ge 450$ MeV/核子时，电子附着平均自由程（mfp）为**数 $\rm g\,cm^{-2}$**，而电子剥离 mfp $< 10^{-2} \rm\,g\,cm^{-2}$
- 在平均密度 $\sim 0.3$–$0.4 \rm\,cm^{-3}$ 的星际介质中，宇宙线在此能量段不会发生显著的 $^{59}$Ni 在途 EC 衰变

**例外**：如果宇宙线曾在较低能量（$< 200$ MeV/核子，此处 EC mfp $< 1 \rm\,g\,cm^{-2}$）停留较长时间，则**显著的 $^{59}$Ni 在途衰变是可能的**。这直接关系到"宇宙线是否分步加速（再加速）"的问题，在 §3 讨论。
