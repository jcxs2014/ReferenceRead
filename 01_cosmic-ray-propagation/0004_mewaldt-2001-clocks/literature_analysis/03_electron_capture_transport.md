---
title: "3. Electron-Capture Nuclei as Probes of Transport — 51Cr/49V 与再加速"
paper: "Mewaldt et al. 2001, Radioactive Clocks and Cosmic-Ray Transport in the Galaxy"
outline_ref: "§3 Electron-Capture Nuclei as Probes of Cosmic Ray Transport Processes"
original_sections: ["§3 (L156–213, 57 行)"]
---
> 本章属于：[[01_cosmic-ray-propagation/0004_mewaldt-2001-clocks/literature_analysis/00_overview.md|Radioactive Clocks and Cosmic-ray Transport in the Galaxy]]
> 上一章：[[01_cosmic-ray-propagation/0004_mewaldt-2001-clocks/literature_analysis/00_overview.md|00_overview]]
> 下一章：[[01_cosmic-ray-propagation/0004_mewaldt-2001-clocks/literature_analysis/04_beta_decay_clocks.md|04_beta_decay_clocks]]

## 3.1 [FACT] 物理动机：单次加速 vs 系列加速

**单次激波加速的理论极限**（Gaisser, 1990）：
在单个 SN 激波的 $\sim 10^4$ 年寿命内，理论上可将原子序数为 $Z$ 的宇宙线加速到 $\sim 10^{14} Z$ MeV 的能量。对于铁（$Z=26$），即 $\sim 2.6 \times 10^{15}$ MeV —— 足以覆盖大部分观测到的宇宙线能量范围。

但 Mewaldt 指出，**"大部分宇宙线可能从一系列 SN 激波中逐步获得能量"**（分布式加速 / re-acceleration）。区分这两种情形的直接手段是**电子俘获核**。

## 3.2 [FACT] 电子俘获核的能量依赖性

- **[FACT]** ACE/CRIS 与 Ulysses、Voyager、ISEE-3 四个平台**跨仪器交叉检验**：Connell & Simpson (1999) 用 Ulysses+Voyager 的 $^{49}$V/$^{51}$V 比与 LBM 比较；Webber (2000a,b) 用 ACE+Ulysses 与蒙特卡洛扩散模型比较——多平台一致观测到能量依赖的信号（原文 p.31, p.32，行 174–198）。

电子俘获衰变要求宇宙线原子核携带至少一个电子。对于高能宇宙线（裸核），EC 衰变被完全抑制；只有当宇宙线减速到足够低的能量（$\lesssim 200$ MeV/核子）时，EC 衰变才变得有效。

因此，如果宇宙线在低能区"停留"过（即曾经被减速后又被再加速到高能），EC 核就会出现比预期更多的衰变。Mewaldt 列出的候选核素（实验室半衰期 28 天–67 年）：

$$^{7}\text{Be},\; ^{37}\text{Ar},\; ^{44}\text{Ti},\; ^{49}\text{V},\; ^{51}\text{Cr},\; ^{55}\text{Fe},\; ^{57}\text{Co}$$

## 3.3 [FACT] 关键观测：51Cr 在低能区的亏损

**Niebur et al. (2000)** 利用 CRIS 大收集能力，在多个能量区间测量了 $^{51}$Cr 和 $^{51}$V 的丰度（Figure 3）：

- **$^{51}$Cr（母核）** 在低能区出现**明显亏损**
- **$^{51}$V（子核）** 在低能区出现**对应过剩**
- **$^{51}$Cr + $^{51}$V 之和**与稳定次级核的比较是**能量无关的**

这后一点非常关键：它排除了"Fe 碎裂截面存在非预期的能量依赖性"这一替代解释，**确认了观测到的能量依赖确实是 $^{51}$Cr 的 EC 衰变所致**。

类似的结果也见于 $^{49}$V/$^{49}$Ti 母-子核组合（Niebur et al. 2000）。

## 3.4 [CRITIQUE] 是否需要再加速？

不同作者对相同数据的解释存在分歧：

| 作者 | 数据 | 是否需要再加速？ |
|------|------|----------------|
| Connell & Simpson (1999) | Ulysses + Voyager 的 $^{49}$V/$^{51}$V 比，与 LBM 比较 | **是**，需要再加速 |
| Soutoul et al. (1998) | 同上 | **是** |
| **Mewaldt 立场（基于 Niebur 2000）** | ACE/CRIS 的 $^{51}$Cr + $^{51}$V 能谱 | **否**，仅用 EC 的能量依赖性即可解释 |
| Webber (2000a) | ACE 的 $^{51}$V/$^{49}$V 比，与 LBM 比较 | **否**，LBM 无需再加速即可拟合 |
| Webber (2000b) | ACE + Ulysses 的蒙特卡洛扩散模型 | $^{51}$V/$^{51}$Cr 偏向再加速，$^{49}$Ti/$^{49}$V 不偏向 |

## 3.5 [FACT] 不确定性的根本来源

Mewaldt 在 §3 末尾明确表态："**从电子俘获核的观测中得出明确结论仍然为时过早**"，理由是其丰度同时依赖于：

1. **电子俘获与剥离截面的能量依赖性**
2. **碎裂截面**（铁族的碎裂）
3. **宇宙线加速历史与可能的再加速**
4. **星际物质中的不均匀性**（Raisbeck et al. 1975；Letaw et al. 1984）
5. **宇宙线进入日球层时的能量变化**（太阳调制）

这五个因素中每一个的不确定性都会显著影响最终结论。Mewaldt 预计这些数据的解释将在未来几年成为"激烈争论的主题"。

## 3.6 [INTERPRETATION] §3 对本论文定位的意义

§3 在方法论上的价值在于：**确立了电子俘获核作为宇宙线"能量历史探针"的工具地位**，但**明确承认目前数据的精度尚不足以在"再加速 vs 无再加速"之间做出最终判决**。这一定调与 §4 中 β 衰变时钟的定量结论形成鲜明对比。
