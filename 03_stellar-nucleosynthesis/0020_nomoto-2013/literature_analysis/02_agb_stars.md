# 2. Evolution and Nucleosynthesis of AGB Stars — Nomoto et al. (2013) §2 精读

> 本章属于：[[03_stellar-nucleosynthesis/0020_nomoto-2013/literature_analysis/00_overview.md|Nucleosynthesis in Stars and the Chemical Enrichment of Galaxies]]
>
> 上一章：[[03_stellar-nucleosynthesis/0020_nomoto-2013/literature_analysis/01_introduction.md|01_introduction]]
>
> 下一章：[[03_stellar-nucleosynthesis/0020_nomoto-2013/literature_analysis/03_ccsn_nucleosynthesis.md|03_ccsn_nucleosynthesis]]

---

## 2.1 Yields Table — AGB 部分

[FACT] AGB 星产额采用 **Karakas (2010)** 模型，覆盖：
- 质量：**1.0, 1.25, 1.5, 1.75, 1.9, 2.0, 2.25, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5 M☉**
- 金属丰度：$Z = 0.0001, 0.004, 0.008, 0.02$
- 插值规则：$Z=0.0001 \le Z \le 0.001$ 用 $Z=0.0001$ 的产额；$Z \ge 0.02$ 用 $Z=0.02$ 的产额

[FACT] **产额定义**（本文严格采用）：
$$ Y_i \equiv M_{i,\text{wind}} - M_{i,\text{initial}} $$
即"恒星一生抛射中核素 $i$ 的净增加"。某些同位素（如 $^{15}$N）的产额可为 **负值**（被恒星演化破坏）。

[FACT] **负产额处理**：GCE 模型要求非负输入；本文对 $^{15}$N 若为负值则置为 0（§2.1 明述）。这体现了"模型自洽 > 物理精确"的妥协。

[FACT] 对 Z=0（Pop III AGB 星），使用 **Campbell & Lattanzio (2008)** 模型，覆盖 $M = 0.85, 1.0, 2.0, 3.0$ M☉。Na 产额人为除以 10（反应率过旧）。$M > 3.5$ M☉ 时不产金属——这一假设被本文作者自陈"可能不成立"。

[FACT] 放射性核素 $^{26}$Al 归入 $^{26}$Mg，$^{60}$Fe 归入 $^{60}$Ni（半衰期远短于 GCE 时标）。

## 2.2 C+O White Dwarfs versus Type 1.5 Supernovae

[FACT] **C+O WD**：前身星 $M \approx 8–10$ M☉。太阳丰度下，C+O 核通过超软 X 射线源 (SSS) 吸积氢，可触发 **氖点燃** 或 **热核爆发**（Type 1.5 SN）。

[FACT] **热核爆发 (WD detonation)** 阈值：
- $M_{\text{remnant}} \approx 1.01, 1.12, 1.15$ M☉ 对应 $M_{\text{ZAMS}} \approx 7, 8, 10$ M☉
- 若吸积速率 $\dot{M} \sim 10^{-7}$ M☉/yr，表面爆发；否则形成 ONeMg 核

[FACT] **Type 1.5 SN**（Miyaji 1980）：C+O WD 吸积足够质量后，Ne 点燃引爆，抛射 O/Ne/Mg——是 **[Mg/Fe] 和 [Ne/Fe] 在低金属丰度星中轻度富集**的可能来源。

## 2.3 Super AGB Stars, O+Ne+Mg White Dwarfs, and Electron-Capture Supernovae

### 2.3.1 Formation of O+Ne+Mg White Dwarfs

[FACT] 当中心 C 耗尽后形成 **O+Ne+Mg 核**。核质量不超过 **Ne 点燃的临界质量 $M_{\text{crit}} = 1.37$ M☉**，因此 Ne 燃烧永不点火。核强简并，包层成为 super-AGB 形态（带 He 壳的热脉冲）。

[FACT] **$M_{\text{up,Ne}} \approx 9 \pm 1$ M☉**（Siess 2007, 2010; Poelarends 2008; Pumo 2009; Langer 2012）：这是 O+Ne+Mg WD 的前身星**质量上界**，随金属丰度降低而减小。

[FACT] 最终命运取决于两个过程的竞争：
1. 质量损失（减少包层质量）→ 形成 O+Ne+Mg WD
2. 核增长（H/He 壳燃烧）→ 触发电子俘获

### 2.3.2 Electron-Capture Supernovae

[FACT] **EC-SN 前身星**：$M_{\text{up,Ne}} < M < 10$ M☉。核心质量增长至 $1.38$ M☉，中心密度达 $\rho_c \sim 4 \times 10^9$ g cm⁻³。

[FACT] **触发机制**（Miyaji et al. 1980; Nomoto 1987）：电子 Fermi 能量超过电子俘获阈值，引发链式反应：
$$ {}^{24}\text{Mg}(e^-, \nu) \to {}^{24}\text{Na}(e^-, \nu) \to {}^{20}\text{Ne}(e^-, \nu) \to {}^{20}\text{F}(e^-, \nu) \to {}^{20}\text{O} $$
Ye 下降 → 绝热指数 < 4/3 → 坍缩。

[FACT] **爆发能量**：$E \sim 10^{50}$ erg，是**最弱**的超新星。由中微子加热诱导，抛射少量 α 元素和 Fe 峰元素，但可能是 **Zn 和轻 p 核素**的重要来源。

[FACT] 9 M☉ EC-SN 的产额（Wanajo et al. 2009, 2011）：最大的过量出现在 **$^{60}$Zn, $^{70}$Se, $^{74}$Se, $^{78}$Kr** 等轻 p 核素——这是 p 过程的一个新候选 site（除传统 SN 外）。

## [INTERPRETATION] §2 的意义

- **AGB 星**是银河系**慢中子俘获 (s 过程) 的主要 site**（主 s 过程）；其产额表的金属丰度依赖（$^{13}$C 口袋大小）是 [Ba/Fe]、[Eu/Ba] 观测比值的决定性输入（见 §0017 Käppeler 2011）。
- **EC-SN** 是 "faint SN" 家族的一员，是解释 Damped Lyman-α 系统中 **[Zn/Fe] 平直**（不随 [Fe/H] 变化）的关键。

## [CRITIQUE]

- Z=0 AGB 模型依赖的 $M>3.5$ M☉ 无金属产出假设"可能不成立"（作者自陈），但影响平均 GCE 甚微——**个体 EMP 星的拟合仍敏感**。
- Karakas (2010) 模型对 **$^{13}$C 口袋深度**（第三挖掘深度 third dredge-up）仍不精确——直接影响 s 过程产额 20–50% 的不确定性。

---
