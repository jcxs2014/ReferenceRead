---
title: '08. Abundance Evolution in the Galaxy and Origin of the r Process'
authors: J. J. Cowan, C. Sneden, J. E. Lawler et al.
year: '2021'
journal: Rev. Mod. Phys. 93, 015002 (2021)
doi: 10.1103/RevModPhys.93.015002
arxiv: arXiv:2101.10655
category: 恒星核合成
chapter: §VIII
status: completed
read_date: '2026-08-15'
lastread: '2026-08-15'
path: 03_stellar-nucleosynthesis/0016_cowan-2021/literature_analysis/08_abundance_evolution_in_galaxy.md
---

> 本章属于：[[03_stellar-nucleosynthesis/0016_cowan-2021/literature_analysis/00_overview.md|Origin of the Elements: A Status Report (Cowan et al. 2021)]]
> 原文位置: fulltext.txt 行 3260–3800（约 5 页正文）
> 上一章: [07_electromagnetic_signatures_of_r_process.md](07_electromagnetic_signatures_of_r_process.md)
> 下一章: [09_final_remarks_and_conclusions.md](09_final_remarks_and_conclusions.md)

# §VIII. Abundance Evolution in the Galaxy and Origin of the r Process — 精读笔记

## §VIII.1 本节核心内容

§VIII 是 Cowan 2021 的**银河系化学演化（GCE）章**，把 §VI 的天体物理 site 与 §II 的观测丰度联系起来。分四子节：

- **§VIII.A r 过程 site 的总结与权衡**——NSM, MRSN, collapsar 等 site 在 GCE 中的角色
- **§VIII.B r 过程事件的稀有性与化学演化模型**——早期 vs 晚期 r 过程增强的解释
- **§VIII.C 观测约束的连接**——把 r 过程模式与 GCE 模型的具体预测对比
- **§VIII.D 长寿命放射性与 cosmochronometry**——U/Th 在恒星年龄测量中的应用

§VIII 的核心命题：**r 过程 site 的判定需要"天体物理 + 化学演化 + 宇宙学"的联合论证**——单一线索（如 VMP 谱学或 kilonova）都不充分。

## §VIII.2 原文内容（FACT 摘录）

### §VIII.A — Possible r-process sites

> **[FACT]** "In Sec. VI we presented possible astrophysical sites and the related abundance predictions. This section addresses some of the additional features like their occurrence frequency and its consequences for galactic chemical evolution."（行 3264–3267）

> **[FACT]** **r 过程 site 的"分层"组合**（行 3280+）：
> - **Main r process**：NSM（主要） + MRSN（少数，可能 ~10-20%）
> - **Weak r process**：CCSN + NSM 高 $Y_e$ ejecta
> - **i process**：超低金属丰度 AGB（待定）

### §VIII.B — Rarity and chemical evolution

> **[FACT]** **早期银河系 r 过程增强星证据**：
> - [Fe/H] < -2 的星中 ~5% 是 r-II（[Eu/Fe] > +1）
> - [Fe/H] < -3 的星中 ~30% 显示出某种 r 过程增强
> - 暗示早期 r 过程事件虽然稀疏，但产量丰富

> **[FACT]** **化学演化模型**（行 3488+）：
> - **Homogeneous GCE** (Argast et al. 2004; Matteucci et al. 2014): 标准均匀混合模型
> - **Inhomogeneous GCE** (van de Voort et al. 2020): 考虑 ejecta 在 ISM 中的局部富集
> - **Chemodynamical models**: 用 AREPO 等代码的 3D 流体力学模型

> **[FACT]** **NSM 延迟时间分布**：合并时间 $t_{delay}$ 服从 $P(t) \propto t^{-1}$（Dominik et al. 2012）——首次 NSM 出现在 massive star 形成后 ~10-100 Myr。

### §VIII.C — Connecting observational constraints

> **[FACT]** **VMP 星 r 过程模式 vs 模型预测**：
> - 早期（z > 1）r 过程主要由 NSM 提供（少数高产事件）
> - 后期（z < 0.5）r 过程仍由 NSM 主导（事件率 ~$10^{-4}$/yr/galaxy）
> - 早期 NSM 事件率可能比当代高 10-100×（取决于双中子星形成时间）

> **[FACT]** **元素比诊断**：
> - [Eu/Ba] vs [Fe/H]: 早期高，晚期下降至 solar
> - [Eu/Mg]: 反映 r 过程 / $\alpha$ 元素（CCSN）的相对贡献
> - [Th/Eu]: cosmochronometry

### §VIII.D — Long-lived radioactivities

> **[FACT]** **U/Th 在恒星中的应用**（行 3694+）：
> - HE 1523-0901: 测得 Th + U + Os + Ir 多 r-clock → 年龄 13.0 ± 2.5 Gyr（Frebel et al. 2007）
> - CS 31082-001: 测得 Th/Eu → 年龄 ~12.5 Gyr（Hill et al. 2002）
> - r 过程 cosmochronometry 给出与宇宙年龄一致的恒星年龄（~13.8 Gyr）

> **[FACT]** **Actinide boost**（行 3700+）：某些 r-II 星的 actinide/U 比例是 solar 的 ~2×（"actinide boost"）——暗示 r 过程 yields 的多样性（不同 NSM 的 $Y_e$ 分布不同）。

## §VIII.3 关键公式

### GCE 基本方程

**均匀 GCE**：
$$\frac{dY_i}{dt} = \mathcal{R}_{CCSN,i}(t) + \mathcal{R}_{NSM,i}(t) - \text{astration}(t) \cdot Y_i$$

其中 $\mathcal{R}_{CCSN,i}, \mathcal{R}_{NSM,i}$ 是 CCSN 和 NSM 的产额率。

**Inhomogeneous GCE**：在 3D 流体力学中跟踪每个网格的丰度演化。

### Cosmochronometry

**Th/U 比与年龄**（简化）：
$$\left(\frac{\text{Th}}{\text{U}}\right)_{observed} = \left(\frac{\text{Th}}{\text{U}}\right)_{initial} \cdot \frac{e^{-\lambda_{Th} t}}{e^{-\lambda_U t}}$$

其中 $\lambda_{Th} = \ln 2 / T_{1/2,Th}$, $\lambda_U = \ln 2 / T_{1/2,U}$。

**简化年龄公式**：
$$t = \frac{1}{\lambda_U - \lambda_{Th}} \ln\left[\frac{(\text{Th/U})_0}{(\text{Th/U})_t}\right]$$

其中 $(\text{Th/U})_0$ 是 r 过程初始产量比，$(\text{Th/U})_t$ 是观测值。

### NSM 事件率

**Standard NSM rate**：
$$\mathcal{R}_{NSM} \sim 10^{-4} \text{ yr}^{-1} \text{ galaxy}^{-1}$$

早期（z > 1）可能高 10-100×（依赖 SFR 历史）。

## §VIII.4 关键参数 / 数据点

| 观测 / 模型 | 关键参数 | 数值 | 意义 |
|---|---|---|---|
| r-II star 比例 | [Fe/H] < -2 中 ~5% | ~5% | 早期 r 过程高产 |
| r-II star 比例 | [Fe/H] < -3 中 ~30% | ~30% | 早期 r 过程主导 |
| NSM 事件率 | 当代银河系 | ~$10^{-4}$ yr$^{-1}$ | 主要 rate |
| NSM 延迟时间 | $P(t) \propto t^{-1}$ | 10–100 Myr | 早期富集时标 |
| HE 1523-0901 | r-clock 年龄 | 13.0 ± 2.5 Gyr | cosmochronometry |
| CS 31082-001 | Th/Eu 年龄 | ~12.5 Gyr | cosmochronometry |
| Actinide boost star 比例 | ~30% r-II | ~30% | r 过程多样性 |

## §VIII.5 图表分析

### Figure 13 — [Eu/Fe] vs [Fe/H] 银河系演化趋势

**1. 图的目的**：展示银河系 r 过程增强星的丰度趋势，作为 GCE 模型的约束。

**2. 坐标轴**：
- 横轴：[Fe/H]，从 -4 到 0
- 纵轴：[Eu/Fe]，从 -1 到 +2

**3. 图中元素**：
- 散点：观测星
- 颜色：按 [Ba/Eu] 分类（r-I, r-II, mixed）
- 灰色阴影：GCE 模型预测区域

**4. 关键观察**：
- [Fe/H] < -2：高散布，[Eu/Fe] 上限 +1.5
- [Fe/H] > -1：下降至 solar [Eu/Fe] ≈ 0
- r-II 星集中于 [Fe/H] < -1.5

**5. 数值信息**：
- scatter 在低金属丰度端 ~ ± 1 dex
- 趋势下降斜率 ≈ -0.3 to -0.5 dex / dex

**6. 作者的解释**：下降反映 Ia 超新星 Fe 增丰赶上 r 过程 Eu 增丰。

**7. 与正文的关系**：§VIII.C 的核心图。

**8. 物理意义**：r 过程早期高产 + 后期稳态 + Ia SN 追赶 = 当前观测到的趋势。

**9. 需要注意的问题**：
- 低金属丰度端的 scatter 受样本偏差影响
- GCE 模型依赖初始产量假设

### Figure 14 — NSM 事件延迟时间分布

**1. 图的目的**：NSM 合并的延迟时间分布。

**2. 坐标轴**：横轴为时间（Myr），纵轴为概率密度（对数）。

**3. 图中元素**：
- 灰色：模拟预测范围
- 黑色：Dominik 2012 拟合 $P(t) \propto t^{-1}$
- 数据点：双中子星系统观测

**4. 关键观察**：
- 最小延迟 ~10 Myr（最快 massive binary 演化）
- 中位延迟 ~100 Myr–1 Gyr
- 尾部到 ~10 Gyr

**5. 数值信息**：
- LIGO/Virgo O3 估计合并率 ~320 Gpc$^{-3}$ yr$^{-1}$

**6. 作者的解释**：NSM 延迟时间与早期 r 过程富集时标匹配。

**7. 与正文的关系**：§VIII.B 的核心图。

**8. 物理意义**：NSM 延迟时间决定 r 过程在银河系历史中的"开启时间"。

**9. 需要注意的问题**：
- 不同双星演化模型给出不同的 $P(t)$（t$^{-1}$ vs t$^{-1.5}$ 等）

## §VIII.6 作者的逻辑

§VIII 的逻辑结构是**"site + 化学演化"**：

1. **§VIII.A site 总结**——把 §VI 的天体物理 site 总结
2. **§VIII.B 稀有性与化学演化**——把 site 性质（事件率、产量）转化为 GCE 预测
3. **§VIII.C 观测对比**——把 GCE 预测与 VMP 星观测对比
4. **§VIII.D cosmochronometry**——给 GCE 提供独立的"时间校验"

这种"site → 模型 → 观测 → 校验"的逻辑链，是 RMP 综述把多章节融合的标准方式。

## §VIII.7 我的理解 [INTERPRETATION]

### "分层 r 过程"假说
> [INTERPRETATION]

当代主流观点（截至 2021）：

| 核素 / 元素 | 主要 site | 证据 |
|---|---|---|
| Eu, Os, Ir, Pt, Au, Th, U | Main r (NSM + MRSN) | r-II 星 + cosmochronometry |
| Sr, Y, Zr (第一峰) | Weak r (CCSN + NSM 高 Y_e) | 早期低 [Ba/Eu] 星 |
| Ba, La, Ce, Nd (第二峰) | Main r + s 过程混合 | 经典 r/s 区分困难 |
| Ra, Th (轻锕系) | i process（超低 Z AGB）? | 极少数星 |

Cowan 2021 §VIII 倾向"分层 r 过程"假说——多种 site 协同产生不同元素段。

### 早期 NSM 事件率问题
> [INTERPRETATION]

VMP r-II 星的丰度模式要求 ~$10^{-3}$–$10^{-4}$/yr/galaxy 的 r 过程事件率在 [Fe/H] < -2 时（约 ~12 Gyr ago）。当代 NSM 率是 ~$10^{-4}$/yr/galaxy——意味着要么早期 SFR 高（NSM 形成多），要么有额外 site（MRSN/collapsar）补充。

Cowan 2021 §VIII.B 未做量化。

### Actinde boost 的物理意义
> [INTERPRETATION]

某些 r-II 星（如 CS 31082-001）的 U/Th 比例是 solar 的 2×——"actinide boost"。可能机制：
1. **NSM 的 $Y_e$ 多样性**：某些 NSM 极低 $Y_e$ 产生更多 actinides
2. **不同 site 混合**：main r + minor r process 的组合

这种 boost 是 NSM ejecta $Y_e$ 分布的"指纹"，对核合成的非唯一解提示重要。

## §VIII.8 潜在问题与值得关注的地方 [CRITIQUE]

### §VIII.8.1 优点
> [CRITIQUE]
1. **site + GCE 的整合**：把天体物理与化学演化无缝连接
2. **多模型对比**：均匀 / 非均匀 GCE 模型都给
3. **独立时间校验**：cosmochronometry 与 GCE 独立

### §VIII.8.2 局限
> [CRITIQUE]
1. **早期 SFR 历史**：依赖 SFR(z) 假设，未充分讨论不确定度
2. **GCE 模型参数空间**：参数拟合的简化解 vs 全参数扫描
3. **Actinide boost 的系统研究**：仅有少数星有 actinide 测量
4. **i process 的物理来源**：未深入讨论超低金属 AGB 的物理
5. **化学动力学模拟**：3D 代码（AREPO）的初始条件依赖

### §VIII.8.3 与其他章节的张力
> [CRITIQUE]
- §VIII.A → §VI：site 列表的重申
- §VIII.B → §II.A：VMP 星观测的连接
- §VIII.D → §II.D：cosmochronometry 在 §II 已介绍，§VIII 深入应用

## §VIII.9 关键术语

- **GCE** (Galactic Chemical Evolution): 银河系化学演化
- **homogeneous GCE**: 均匀混合模型
- **inhomogeneous GCE**: 非均匀混合模型（局部富集）
- **chemodynamical model**: 化学-动力学耦合模型
- **cosmochronometer**: 长寿命放射性核素
- **NSM delay time distribution**: NSM 合并的延迟时间分布 $P(t)$
- **actinide boost**: 锕系元素相对太阳系丰度的增强
- **early enrichment**: 早期银河系富集
- **astration**: 物质被恒星吸收-再抛射的循环
- **AREPO**: 3D 流体动力学 + 化学演化代码
- **r-II star**: r 过程增强星（[Eu/Fe] > +1）

## §VIII.10 引用页码索引

| 主题 | 原文页码 | fulltext 行号 |
|---|---|---|
| §VIII 起始（"ABUNDANCE EVOLUTION..."） | 015002-54 | 行 3260 |
| §VIII.A site 总结 | 015002-54 | 行 3264+ |
| §VIII.B 稀有性与化学演化 | 015002-55 | 行 3488+ |
| Inhomogeneous GCE | 015002-55 | 行 3488+ |
| §VIII.C 观测约束 | 015002-57 | 行 3547+ |
| §VIII.D cosmochronometry | 015002-58 | 行 3694+ |
| HE 1523-0901 / CS 31082-001 | 015002-58 | 行 3700+ |
| Actinide boost | 015002-58 | 行 3700+ |
| Fig. 13 ([Eu/Fe] vs [Fe/H]) | 015002-55 | 行 3400+ |
| Fig. 14 (NSM 延迟时间) | 015002-56 | 行 3450+ |