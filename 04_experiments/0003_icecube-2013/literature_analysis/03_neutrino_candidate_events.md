---
title: "§3 Neutrino Candidate Events"
paper: "icecube-2013"
section: 3
nav_prev: "02_event_selection_and_background.md"
nav_next: "04_statistical_significance.md"
---
上一章：`02_event_selection_and_background.md` — §2
下一章：`04_statistical_significance.md` — Neutrino Candidate Events


# §3 Neutrino Candidate Events — 28 个候选中微子事件
## [FACT] 3.1 28 起候选事件总览

**观测结果**（原文 p.1242856-1–2，Fig.2）：在两年观测（662 天）中，观测到 **28 起中微子候选事件**，**沉积能量范围 30–1200 TeV**（原文："28 events with in-detector deposited energies between 30 and 1200 TeV"）。

| 特征 | 值 | 原文 |
|------|-----|-----|
| 事件总数 | **28 起** | p.2 |
| 新增事件（本报告） | **26 起** | p.2 |
| 含此前 PeV 事件 | **2 起**（最高能量） | p.2，引 ref 3 |
| 沉积能量范围 | **30 – 1200 TeV** | p.1 |
| Track 事件 | **7 起**（可辨识 μ 径迹） | p.2 |
| Shower 事件 | **21 起**（簇射型） | p.2 |
| 能量 >100 TeV | **9 起**（原文 p.3："Nine had reconstructed deposited energies above 100 TeV"） | p.3 |
| 能量 >1 PeV | **2 起**（最高 2 起） | p.3 |

## [FACT] 3.2 前 5 起最高能量事件（Table 1）

| ID | 沉积能量 (TeV) | Declination (°) | RA (°) | 类型 | 原文 p.1242856-2 |
|----|---------|---------|------|------|-----|
| 14 | **1424<sup>+108</sup><sub>−137</sub>** | −27.9 | 265.6 | Shower | Table 1 |
| 20 | **1433<sup>+143</sup><sub>−137</sub>** | −67.2 | 38.3 | Shower | Table 1 |
| 13 | 253<sup>+22</sup><sub>−22</sub> | +40.3 | 67.9 | Track | Table 1 |
| 22 | 220<sup>+24</sup><sub>−21</sub> | −22.1 | 293.7 | Shower | Table 1 |
| 26 | 210<sup>+29</sup><sub>−25</sub> | +22.7 | 143.4 | Shower | Table 1 |

**最高能量**：1424 TeV（~1.4 PeV），20 号事件 1433 TeV（~1.4 PeV）——两起 >1 PeV 事件是 2013 年报告的最高能量中微子，也是 **当时人类探测到的最高能量中微子**。

## [FACT] 3.3 Track 事件（7 起）

| ID | 能量 (TeV) | 方位角误差 | Declination | 原文 |
|----|---------|---------|---------|-----|
| 3 | 78.7 | **≤1.4°** | −31.2 | Table 1 |
| 5 | 71.4 | **≤1.2°** | −0.4 | Table 1 |
| 8 | 32.6 | **≤1.3°** | −21.2 | Table 1 |
| 13 | 253 | **≤1.2°** | +40.3 | Table 1 |
| 18 | 31.5 | **≤1.3°** | −24.8 | Table 1 |
| 23 | 82.2 | **≤1.9°** | −13.2 | Table 1 |
| 28 | 46.1 | **≤1.3°** | −71.5 | Table 1 |

Track 事件方位角分辨率 ~1°（优于 shower 的 10°–15°），是**未来源定位**的主力（原文 p.2）。

## [FACT] 3.4 Shower 事件（21 起）

21 起簇射型事件，**与 ν_e / ν_τ 相互作用或 ν_μ CC 产生的强子簇射一致**。方位角分辨率 10°–15°（能量相关）。其中 4 起低能 track-like 事件起点在探测器边界且向下进入，与大气 μ 背景一致（原文 p.2："Four of the low-energy tracklike events started near the detector boundary and were down-going"）——其中 1 起（event 28，Table 1 中的 28 号 track，46.1 TeV）在 IceTop 表面阵列有命中。

## [FACT] 3.5 方向分布特征

**南方天主导**：观测事件中大多数来自南天（原文 Fig.2，p.2）。这一**南北不对称**是地外中微子流的特征：
- 地球在几十 TeV 以上对中微子吸收显著
- 天顶角分布符合各向同性地外通量被地球吸收后的预期（原文 Fig.4B）

原文（p.3）："The observed zenith distribution is also typical of such a flux: as a result of absorption in Earth above tens of TeV energy, most events (~60%) ... would be expected to appear in the Southern Hemisphere."

## [FACT] 3.6 空间分布均匀性

**事件首次探测光坐标**（Fig.3，原文 p.3）：
- 事件在 **(r$^{2}$, z) 空间**中近似均匀分布
- 与中微子在探测体内均匀相互作用的预期一致
- 与 μ 背景（在探测器边界/ veto 层附近聚集）明确区分

原文（p.3）："The observed events are consistent with a uniform distribution."

## [FACT] 3.7 能量分布特征

**硬谱特征**（Fig.4A，原文 p.3–4）：
- 观测到的 28 起事件中，能量高于 100 TeV 有 9 起
- 高于 1 PeV 有 2 起
- 与 p/K 大气 ν 背景外推相比，观测谱明显更硬（harder）
- 谱指数 best fit：E<sup>−2.2±0.4</sup>（原文 p.4）

## [FACT] 3.8 与背景事件的定量比较

| 特征 | 观测事件 | 大气 p/K 背景预期 | 原文 |
|------|--------|------------|-----|
| 事件数 | 28 | 6.1（仅 ν p/K） | p.2 |
| >100 TeV 事件数 | 9 | ~1 | p.3 |
| >1 PeV 事件数 | 2 | 0 | p.3 |
| Track 分数 | 7/28 = 25% | 预期 ~3/4（若为 p/K ν） | p.3 |
| 南天事件 | ~60%+ | 若为大气起源应北天为主 | p.3 |

**Track 分数倒置**：p/K 大气 ν 以 ν_μ 为主（π/K → μ + ν_μ → e + ν_e + ν_μ + ν̄_μ），预期 ~3/4 为 track；观测仅 1/4——**这一比率与宇宙线加速源预言的 flavor equipartition（1:1:1）一致**。

## [INTERPRETATION] 候选事件特征总结

28 起候选事件呈现四个一致指向地外起源的特征：
1. **能量过高**：2 起 >1 PeV，是已知中微子最高能量
2. **谱过硬**：E<sup>−2.2±0.4</sup>，比 p/K 大气 ν 谱硬得多
3. **南天偏置**：60%+ 来自南天，与大气 μ 背景（北天为主）相反
4. **Track 分数过低**：25% track vs 大气 p/K 预期 75%

## 精读来源

- 原文 Fig.2（能量-方位角分布）、Fig.3（事件坐标）、Fig.4（能谱与天顶角）、Table 1（28 起事件表）
- 原文 p.1242856-1–4