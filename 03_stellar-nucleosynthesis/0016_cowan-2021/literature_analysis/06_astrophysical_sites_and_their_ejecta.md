---
title: '06. Astrophysical Sites and Their Ejecta Composition'
authors: J. J. Cowan, C. Sneden, J. E. Lawler et al.
year: '2021'
journal: Rev. Mod. Phys. 93, 015002 (2021)
doi: 10.1103/RevModPhys.93.015002
arxiv: arXiv:2101.10655
category: 恒星核合成
chapter: §VI
status: completed
read_date: '2026-08-15'
lastread: '2026-08-15'
path: 03_stellar-nucleosynthesis/0016_cowan-2021/literature_analysis/06_astrophysical_sites_and_their_ejecta.md
---

> 本章属于：Origin of the Elements: A Status Report (Cowan et al. 2021)
> 原文位置: fulltext.txt 行 2221–3071（约 9 页正文）
> 上一章: [05_nuclear_modeling_of_r_process_input.md](05_nuclear_modeling_of_r_process_input.md)
> 下一章: [07_electromagnetic_signatures_of_r_process.md](07_electromagnetic_signatures_of_r_process.md)

# §VI. Astrophysical Sites and Their Ejecta Composition — 精读笔记

## §VI.1 本节核心内容

§VI 是 Cowan 2021 的**天体物理场所章**，分两子节：

- **§VI.A 大质量恒星相关的 r 过程 site**——核心坍缩超新星（CCSN）的 neutrino wind、electron-capture SN、neutrino-induced r process in He shell、magnetorotational SN（带喷流）、collapsars/hypernovae/long GRB
- **§VI.B 双中子星并合（NSM）与中子星–黑洞并合（NSBH）**——包括 neutrino wind 的影响

§VI 的核心命题：**r 过程 site 分为"主要 site"（NSM，2017 后确认）与"次要 site"（CCSN, MRSN, collapsar 等仍有争议）**——后者可能解释 minor r 过程（弱 r 过程）。

## §VI.2 原文内容（FACT 摘录）

### §VI.A — Massive star related sites

> **[FACT]** **CCSN neutrino wind**（行 2374+）：
> - 中微子驱动的风从 proto-neutron star 表面吹出
> - $Y_e \sim 0.45-0.5$（中微子相互作用把中子化物质拉回弱中子化）
> - 早期 NSM 模型曾预测 $Y_e$ 较低可合成 r 过程，但当代模拟显示 CCSN wind 的 $Y_e$ 太高**只能产生 weak r process**（Sr, Y, Zr 等）

> **[FACT]** **Electron-capture SN**（行 2425+）：8-10 M☉ 的 ONeMg 核坍缩，电子俘获触发。$Y_e$ 仍偏高，r 过程产量有限。

> **[FACT]** **Neutrino-induced r process in He shell**（行 2445+）：He 壳层中 $^4$He($\nu, \nu' n$)$^3$H 或类似反应产生自由中子，可触发 weak r process（Woosley et al. 1990; Banerjee et al. 2016）。

> **[FACT]** **Magnetorotational SN**（MRSN, 行 2500+）：高速旋转 + 强磁场 → MHD jet 喷出中子化物质。$Y_e$ 可低至 ~0.1，可合成 main r process。

> **[FACT]** **Collapsars / Hypernovae / Long GRBs**（行 2540+）：大质量恒星核坍缩形成黑洞 + 吸积盘 + 喷流。可能合成 r 过程，但具体产量依赖喷流 $Y_e$（Pruet et al. 2003; Fujimoto et al. 2008）。

### §VI.B — Neutron-star mergers (NSM)

> **[FACT]** **NSM ejecta 机制**：
> 1. **Dynamical ejecta**（prompt, ms timescale）：潮汐 + 冲击加热
>    - $Y_e$ 范围 ~0.04-0.4（多维分布）
>    - 总质量 ~10⁻³–10⁻² M☉
> 2. **Wind ejecta**（secular, s timescale）：中微子 + 黏滞加热 + 磁驱动
>    - $Y_e \sim 0.2-0.4$
>    - 总质量 ~10⁻² M☉
> 3. **Viscous ejecta**：吸积盘黏滞扩散
>    - $Y_e \sim 0.2-0.3$

> **[FACT]** **GW170817 + AT2017gfo 拟合**：
> - 总 ejecta mass: ~0.04-0.05 M☉
> - dynamical 占比：~30-50%（lanthanide-rich 红成分）
> - wind 占比：~50-70%（lanthanide-poor 蓝成分）

> **[FACT]** **NSM 事件率**：LIGO/Virgo O3 run 估计 $\mathcal{R} \sim 320^{+490}_{-240}$ Gpc⁻³ yr⁻¹（Abbott et al. 2020），对应银河系 $\sim 10^{-4}$–$10^{-3}$ Myr⁻¹ 量级。

> **[FACT]** **核合成对应**：
> - low-$Y_e$ ejecta → main r process（含锕系）
> - high-$Y_e$ ejecta → weak r process + first/second peak

### NSBH mergers

> **[FACT]** 中子星–黑洞并合（NSBH）：黑洞通过潮汐撕裂中子星，ejecta 较少（~$10^{-3}$ M☉），但 $Y_e$ 可低至 ~0.05，可能合成纯 main r process（行 2900+）。

## §VI.3 关键公式

### §VI.A Neutrino wind $Y_e$

**$Y_e$ 由中微子/反中微子反应决定**：
$$Y_e \approx \frac{\lambda_{\nu_e n} + \lambda_{\bar\nu_e p}}{\lambda_{\nu_e n} + \lambda_{\bar\nu_e p} + \lambda_{\nu_e p} + \lambda_{\bar\nu_e n}}$$

其中 $\lambda_{\nu_e n} \propto L_{\nu_e} \langle E_{\nu_e}\rangle^2$ 等。

### §VI.B NSM ejecta

**潮汐撕裂质量**（限制性 NSBH）：
$$M_{tidal} \sim 10^{-3} M_\odot \left(\frac{M_{BH}}{M_{NS}}\right)^{1/3} \left(\frac{R_{NS}}{12 \text{ km}}\right)^4$$

**Dynamical ejecta 速度**：
$$v_{ej} \sim 0.2-0.3 c$$

**Wind ejecta 能量**：
$$E_{wind} \sim 10^{51} \text{ erg}$$

### $Y_e$ 与丰度峰关系

**Final abundance 与 $Y_e$ 经验关系**：
- $Y_e < 0.25$：含锕系 + 三峰齐全
- $0.25 < Y_e < 0.4$：仅前两峰
- $Y_e > 0.45$：仅 weak s + first peak

## §VI.4 关键参数 / 数据点

| Site | $Y_e$ | ejecta 质量 | 主要产物 | 事件率 |
|---|---|---|---|---|
| CCSN neutrino wind | 0.45–0.5 | ~$10^{-2}$ M☉ | weak r, s | ~10⁻²/yr/galaxy |
| MRSN jet | 0.1–0.3 | ~$10^{-3}$–$10^{-2}$ M☉ | main r | ~10⁻⁴/yr/galaxy? |
| Collapsar jet | 0.1–0.4 | ~$10^{-3}$ M☉ | main r | ~10⁻⁵/yr/galaxy? |
| NSM dynamical | 0.04–0.4 | ~$10^{-3}$–$10^{-2}$ M☉ | main r (red) | ~$10^{-4}$/yr/galaxy |
| NSM wind | 0.2–0.4 | ~$10^{-2}$ M☉ | weak r (blue) | 同上 |
| NSBH tidal | 0.05–0.25 | ~$10^{-3}$ M☉ | main r | ~$10^{-5}$/yr/galaxy |

## §VI.5 图表分析

### Figure 10 — NSM ejecta $Y_e$ 分布与丰度模式

**1. 图的目的**：展示 NSM 不同 ejecta 通道的 $Y_e$ 分布及其产生的丰度模式。

**2. 坐标轴**：横轴 $Y_e$，纵轴 ejecta mass fraction。

**3. 图中元素**：
- 多峰分布：peak at $Y_e \sim 0.04$（极中子化）, peak at $Y_e \sim 0.25$（中等）, peak at $Y_e \sim 0.4$（弱中子化）
- 不同颜色对应不同 ejecta 通道

**4. 关键观察**：
- **极低 $Y_e$** ($< 0.1$)：synthesize actinides + 三峰
- **中等 $Y_e$** (0.2-0.3)：main r process 第一/二峰
- **高 $Y_e$** (0.3-0.4)：weak r process 第一峰

**5. 数值信息**：基于多个 GW170817 模拟的合并统计。

**6. 作者的解释**：NSM 的多通道 ejecta 自然解释了 kilonova 的"蓝+红"双成分。

**7. 与正文的关系**：§VI.B 的核心图。

**8. 物理意义**：$Y_e$ 分布是 NSM 模拟的"指纹"——不同 EOS / 中子星质量给出不同 $Y_e$ 分布。

**9. 需要注意的问题**：
- 2D/3D 模拟 vs 1D 球对称：后者低估 dynamical 占比
- 中微子 flavor oscillations 在 NSM ejecta 中的处理仍简化

### Figure 11 — 不同 site 的 $N_n/N_{seed}$ 与丰度峰关系

**1. 图的目的**：横坐标 $N_n/N_{seed}$，纵坐标 final abundance peak 位置。

**2. 坐标轴**：log-log 标度。

**3. 图中元素**：
- 直线：理论预测 $\langle A_{final}\rangle \propto N_n/N_{seed}$
- 散点：各 site 的典型参数

**4. 关键观察**：
- $N_n/N_{seed} \sim 100$：到达第三峰（A ≈ 195）
- $N_n/N_{seed} \sim 10$：仅到达第二峰
- $N_n/N_{seed} \sim 1$：仅到达第一峰

**5. 数值信息**：每个 site 在图上有特征"区域"。

**6. 作者的解释**：$N_n/N_{seed}$ 是 site 区分的核心物理量。

**7. 与正文的关系**：§VI 的综合图。

**8. 物理意义**：连接 §III.C 与 §VI.A/B。

**9. 需要注意的问题**：
- $N_n/N_{seed}$ 取决于 ejecta 的具体动力学参数，不能仅靠 site 类型判定

## §VI.6 作者的逻辑

§VI 的逻辑结构是**"按 site 分类，从次要到主要"**：

1. **§VI.A massive stars**：曾经的候选（CCSN 风是 1970s-2000s 的主流假设），但当代认识是次要/弱 r only
2. **§VI.B NSM**：2017 后确认的主要 site

这种安排反映了 r 过程研究历史的**重要转折**——Cowan 2021 在引言中暗示了这种历史框架。

## §VI.7 我的理解 [INTERPRETATION]

### r 过程 site 问题的当代共识

截至 2021 年，r 过程 site 共识：
- **Main r process（重核）**：NSM（确认），可能 + MRSN（少数事件）
- **Weak r process（轻核）**：CCSN wind + NSM 高 $Y_e$ ejecta
- **i process（中间）**：超低金属丰度 AGB，site 不确定

Cowan 2021 §VI 反映了这一共识，但避免"NSM 是唯一 site"的简化——保留 CCSN/MRSN 的次要贡献。

### NSM 与早期银河系 r 过程的矛盾

NSM 事件率 ~$10^{-4}$/yr/galaxy，但早期银河系（z > 1）的 r 过程增强星已显示成熟 r 过程模式。两种解释：
1. **早期 NSM 率高**：早期宇宙双中子星形成时间短（massive star 演化 → NSM），事件率比当代高 10-100×
2. **其他 r 过程 site 补充**：早期 CCSN / collapsar 提供部分 r 过程

Cowan 2021 §VI.B 未深入此矛盾。

### 多个 r 过程 site 的核合成模式混合

当代模型预测：galactic r 过程产物 = 60-90% NSM + 10-30% 其他 site（MRSN + collapsar）的混合。Cowan 2021 §VI 倾向于这种"分层混合"框架。

## §VI.8 潜在问题与值得关注的地方 [CRITIQUE]

### §VI.8.1 优点
1. **Site 覆盖全面**：CCSN, MRSN, collapsar, NSM, NSBH 都涵盖
2. **$Y_e$ 维度强调**：作为区分不同 site 的核心物理量
3. **NSM 多通道论述**：dynamical + wind + viscous 三种 ejecta 分得清楚

### §VI.8.2 局限
1. **早期银河系 r 过程来源**：未深入讨论 z > 1 时期的 r 过程来源
2. **核合成产物的星际介质混合**：未详细讨论 ejecta 与 ISM 的混合机制
3. **二维/三维 vs 一维**：NSM 模拟的维度影响未量化
4. **中微子振荡**：NSM ejecta 中 neutrino oscillations 对 $Y_e$ 的影响仍有争议
5. **MRSN 的事件率**：理论预测范围 ~$10^{-4}$–$10^{-6}$/yr/galaxy，跨度太大

### §VI.8.3 与其他章节的张力
- §VI.A → §VIII：CCSN 的 r 过程产量被 GCE 模型吸收
- §VI.B → §VII：NSM 是 kilonova 的来源
- §VI.B → §VIII：NSM 事件率 + ejecta 质量决定银河系 r 过程演化

## §VI.9 关键术语

- **CCSN** (Core-Collapse Supernova): 核心坍缩超新星
- **MRSN** (Magnetorotational Supernova): 磁旋超新星
- **NSM** (Neutron-Star Merger): 双中子星并合
- **NSBH** (Neutron-Star–Black-Hole merger): 中子星–黑洞并合
- **$Y_e$** (electron fraction): 电子分数
- **dynamical ejecta**: NSM 潮汐 + 冲击瞬时抛射物
- **wind ejecta**: NSM 中微子/黏滞风抛射物
- **viscous ejecta**: 吸积盘黏滞抛射物
- **neutrino-driven wind**: 中微子驱动的风
- **collapsar**: 长 GRB 模型，黑洞 + 吸积盘 + 喷流
- **hypernova**: 极高能量超新星，与 collapsar 关联
- **EOS** (Equation of State): 中子星状态方程
- **neutrino oscillation**: 中微子振荡，影响 $Y_e$

## §VI.10 引用页码索引

| 主题 | 原文页码 | fulltext 行号 |
|---|---|---|
| §VI 起始（"ASTROPHYSICAL SITES..."） | 015002-37 | 行 2221 |
| §VI.A.1 CCSN neutrino wind | 015002-37 | 行 2374+ |
| §VI.A.2 Electron-capture SN | 015002-37 | 行 2425+ |
| §VI.A.3 Neutrino-induced r in He | 015002-37 | 行 2445+ |
| §VI.A.5 MRSN with jets | 015002-37 | 行 2500+ |
| §VI.A.6 Collapsars / hypernovae | 015002-37 | 行 2540+ |
| §VI.B NSM dynamical + wind | 015002-39 | 行 2600+ |
| §VI.B Neutrino wind effect | 015002-41 | 行 2800+ |
| NSBH mergers | 015002-39 | 行 2700+ |
| GW170817 拟合参数 | 015002-39 | 行 2620+ |
| Fig. 10 ($Y_e$ 分布) | 015002-40 | 行 2750+ |
| Fig. 11 ($N_n/N_{seed}$ 关系) | 015002-41 | 行 2850+ |