---
title: '06. Astrophysical Sites and Their Ejecta Composition'
authors: J. J. Cowan, C. Sneden, J. E. Lawler et al.
year: '2021'
journal: Rev. Mod. Phys. 93, 015002 (2021)
category: 恒星核合成
chapter: §VI
status: completed
read_date: '2026-08-15'
path: 03_stellar-nucleosynthesis/0016_cowan-2021/literature_analysis/06_astrophysical_sites_and_their_ejecta.md
---

# §VI. Astrophysical Sites and Their Ejecta Composition — 精读笔记

## §VI.1 本节核心内容

§VI 覆盖 r 过程的天体物理场所，分两子节：

- **§VI.A 大质量恒星相关的 r 过程 site**——CCSN neutrino wind、electron-capture SN、neutrino-induced r process in He shell、MRSN、collapsars/hypernovae/long GRB
- **§VI.B 双中子星并合（NSM）与中子星–黑洞并合（NSBH）**

§VI 的核心命题：**r 过程 site 分为"主要 site"（NSM，2017 后确认）与"次要 site"（CCSN, MRSN, collapsar 等仍有争议）**。

## §VI.2 原文内容（FACT 摘录）

### §VI.A — Massive star related sites

> **[FACT]** **CCSN neutrino wind**（行 2374+）：$Y_e \sim 0.45-0.5$，只能产生 weak r process。

> **[FACT]** **Electron-capture SN**（行 2425+）：8-10 M☉ 的 ONeMg 核坍缩。$Y_e$ 仍偏高。

> **[FACT]** **Neutrino-induced r process in He shell**（行 2445+）：$^4$He($\nu, \nu' n$)$^3$H 等反应产生自由中子——触发 weak r process。

> **[FACT]** **Magnetorotational SN**（MRSN, 行 2500+）：MHD jet 喷出中子化物质。$Y_e$ 可低至 ~0.1，可合成 main r process。

> **[FACT]** **Collapsars / Hypernovae / Long GRBs**（行 2540+）：黑洞 + 吸积盘 + 喷流。

### §VI.B — Neutron-star mergers (NSM)

> **[FACT]** **NSM ejecta 机制**：
> 1. **Dynamical ejecta**（prompt, ms timescale）：$Y_e \sim 0.04-0.4$；总质量 ~$10^{-3}$–$10^{-2}$ M☉
> 2. **Wind ejecta**（secular, s timescale）：$Y_e \sim 0.2-0.4$；总质量 ~$10^{-2}$ M☉
> 3. **Viscous ejecta**：吸积盘黏滞扩散；$Y_e \sim 0.2-0.3$

> **[FACT]** **GW170817 + AT2017gfo 拟合**：总 ejecta ~0.04-0.05 M☉；dynamical 30-50%（lanthanide-rich 红）；wind 50-70%（lanthanide-poor 蓝）。

> **[FACT]** **NSM 事件率**：$\mathcal{R} \sim 320^{+490}_{-240}$ Gpc⁻³ yr⁻¹（Abbott et al. 2020）。

> **[FACT]** **NSBH mergers**（行 2900+）：潮汐撕裂 ejecta 较少（~$10^{-3}$ M☉），$Y_e$ 可低至 ~0.05。

## §VI.3 关键公式

### Neutrino wind $Y_e$

$$Y_e \approx \frac{\lambda_{\nu_e n} + \lambda_{\bar\nu_e p}}{\lambda_{\nu_e n} + \lambda_{\bar\nu_e p} + \lambda_{\nu_e p} + \lambda_{\bar\nu_e n}}$$

### NSM ejecta 质量

$$M_{tidal} \sim 10^{-3} M_\odot \left(\frac{M_{BH}}{M_{NS}}\right)^{1/3} \left(\frac{R_{NS}}{12 \text{ km}}\right)^4$$

$$v_{ej} \sim 0.2-0.3 c$$

### $Y_e$ 与丰度峰关系

- $Y_e < 0.25$：含锕系 + 三峰齐全
- $0.25 < Y_e < 0.4$：仅前两峰
- $Y_e > 0.45$：仅 weak s + first peak

## §VI.4 关键参数 / Site 对比

| Site | $Y_e$ | ejecta 质量 | 主要产物 | 事件率 |
|---|---|---|---|---|
| CCSN neutrino wind | 0.45–0.5 | ~$10^{-2}$ M☉ | weak r, s | ~$10^{-2}$/yr/galaxy |
| MRSN jet | 0.1–0.3 | ~$10^{-3}$–$10^{-2}$ M☉ | main r | ~$10^{-4}$/yr/galaxy? |
| Collapsar jet | 0.1–0.4 | ~$10^{-3}$ M☉ | main r | ~$10^{-5}$/yr/galaxy? |
| NSM dynamical | 0.04–0.4 | ~$10^{-3}$–$10^{-2}$ M☉ | main r (red) | ~$10^{-4}$/yr/galaxy |
| NSM wind | 0.2–0.4 | ~$10^{-2}$ M☉ | weak r (blue) | 同上 |
| NSBH tidal | 0.05–0.25 | ~$10^{-3}$ M☉ | main r | ~$10^{-5}$/yr/galaxy |

## §VI.5 图表分析

### Figure 10 — NSM ejecta $Y_e$ 分布与丰度模式

**1. 图的目的**：展示 NSM 不同 ejecta 通道的 $Y_e$ 分布及其丰度模式。

**2. 坐标轴**：横轴 $Y_e$，纵轴 ejecta mass fraction。

**3. 图中元素**：
- 多峰分布：peak at $Y_e \sim 0.04$（极中子化）, peak at $Y_e \sim 0.25$（中等）, peak at $Y_e \sim 0.4$（弱中子化）
- 不同颜色对应不同 ejecta 通道

**4. 关键观察**：
- 极低 $Y_e$ (< 0.1)：合成 actinides + 三峰
- 中等 $Y_e$ (0.2-0.3)：main r process 第一/二峰
- 高 $Y_e$ (0.3-0.4)：weak r process 第一峰

**5. 数值信息**：基于多个 GW170817 模拟的合并统计。

**6. 作者的解释**：NSM 的多通道 ejecta 自然解释了 kilonova 的"蓝+红"双成分。

**7. 与正文的关系**：§VI.B 核心图。

**8. 物理意义**：$Y_e$ 分布是 NSM 模拟的"指纹"——不同 EOS / 中子星质量给出不同 $Y_e$ 分布。

**9. 需要注意的问题**：
- 2D/3D vs 1D 球对称：1D 低估 dynamical 占比
- 中微子 flavor oscillations 在 NSM ejecta 中的处理仍简化

### Figure 11 — 不同 site 的 $N_n/N_{seed}$ 与丰度峰关系

**1. 图的目的**：横坐标 $N_n/N_{seed}$，纵坐标 final abundance peak 位置。

**2. 坐标轴**：log-log 标度。

**3. 图中元素**：
- 直线：$\langle A_{final}\rangle \propto N_n/N_{seed}$
- 散点：各 site 典型参数

**4. 关键观察**：
- $N_n/N_{seed} \sim 100$：到达第三峰（A ≈ 195）
- $N_n/N_{seed} \sim 10$：仅到达第二峰
- $N_n/N_{seed} \sim 1$：仅到达第一峰

**5. 数值信息**：每个 site 在图上有特征"区域"。

**6. 作者的解释**：$N_n/N_{seed}$ 是 site 区分的核心物理量。

**7. 与正文的关系**：§VI 综合图。

**8. 物理意义**：连接 §III.C 与 §VI.A/B。

**9. 需要注意的问题**：
- $N_n/N_{seed}$ 取决于 ejecta 具体动力学参数

## §VI.6 作者的逻辑

§VI 逻辑是**"按 site 分类，从次要到主要"**：

1. **§VI.A massive stars**：曾经的候选（CCSN 风是 1970s-2000s 主流假设），但当代认识是次要
2. **§VI.B NSM**：2017 后确认的主要 site

## §VI.7 我的理解 [INTERPRETATION]

### r 过程 site 问题的当代共识
> [INTERPRETATION]

截至 2021 年：
- **Main r process（重核）**：NSM（确认），可能 + MRSN
- **Weak r process（轻核）**：CCSN wind + NSM 高 $Y_e$ ejecta
- **i process（中间）**：超低金属丰度 AGB

### NSM 与早期银河系 r 过程的矛盾
> [INTERPRETATION]

NSM 事件率 ~$10^{-4}$/yr/galaxy，但早期银河系 r 过程增强星已显示成熟 r 过程模式。两种解释：
1. 早期 NSM 率高
2. 其他 r 过程 site 补充

### 多个 r 过程 site 的核合成模式混合
> [INTERPRETATION]

当代：60-90% NSM + 10-30% 其他 site。

## §VI.8 潜在问题与值得关注的地方 [CRITIQUE]

### §VI.8.1 优点
> [CRITIQUE]
1. Site 覆盖全面
2. $Y_e$ 维度强调
3. NSM 多通道论述

### §VI.8.2 局限
> [CRITIQUE]
1. 早期银河系 r 过程来源未深入
2. 核合成产物的 ISM 混合机制未详细
3. 二维/三维 vs 一维 NSM 模拟维度影响未量化
4. 中微子振荡对 $Y_e$ 影响
5. MRSN 事件率范围太大（$10^{-4}$–$10^{-6}$/yr/galaxy）

## §VI.9 关键术语

- **CCSN** (Core-Collapse Supernova)
- **MRSN** (Magnetorotational Supernova)
- **NSM** (Neutron-Star Merger)
- **NSBH** (Neutron-Star–Black-Hole merger)
- **$Y_e$** (electron fraction)
- **dynamical ejecta**
- **wind ejecta**
- **viscous ejecta**
- **neutrino-driven wind**
- **collapsar**
- **hypernova**
- **EOS** (Equation of State)
- **neutrino oscillation**

## §VI.10 引用页码索引

| 主题 | 原文页码 | fulltext 行号 |
|---|---|---|
| §VI 起始 | 015002-37 | 行 2221 |
| §VI.A.1 CCSN neutrino wind | 015002-37 | 行 2374+ |
| §VI.A.2 Electron-capture SN | 015002-37 | 行 2425+ |
| §VI.A.3 Neutrino-induced r in He | 015002-37 | 行 2445+ |
| §VI.A.5 MRSN with jets | 015002-37 | 行 2500+ |
| §VI.A.6 Collapsars / hypernovae | 015002-37 | 行 2540+ |
| §VI.B NSM dynamical + wind | 015002-39 | 行 2600+ |
| NSBH mergers | 015002-39 | 行 2700+ |
| GW170817 拟合参数 | 015002-39 | 行 2620+ |
| Fig. 10 ($Y_e$ 分布) | 015002-40 | 行 2750+ |
| Fig. 11 ($N_n/N_{seed}$ 关系) | 015002-41 | 行 2850+ |