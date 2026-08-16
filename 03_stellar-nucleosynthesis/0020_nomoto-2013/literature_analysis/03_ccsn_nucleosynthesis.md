# 3. Explosive Nucleosynthesis in Core-Collapse Supernovae — Nomoto et al. (2013) §3 精读

> 本章属于：[[03_stellar-nucleosynthesis/0020_nomoto-2013/literature_analysis/00_overview.md|Nucleosynthesis in Stars and the Chemical Enrichment of Galaxies]]
>
> 上一章：[[03_stellar-nucleosynthesis/0020_nomoto-2013/literature_analysis/02_agb_stars.md|02_agb_stars]]
>
> 下一章：[[03_stellar-nucleosynthesis/0020_nomoto-2013/literature_analysis/04_massive_stars.md|04_massive_stars]]

---

> 重点章节（本任务核心坍缩 SN 产额表）——§3 给出产额表的**物理机制**（爆炸区核合成）；§4 给出**产额表本身**。

## 3.1 Neutron-Proton Ratio Near the Mass Cut

[FACT] 超新星产额的关键分界线是 **mass cut** $M_{\text{cut}}$：质量 $<M_{\text{cut}}$ 的部分被吸入 BH/NS，$>M_{\text{cut}}$ 的部分被抛射。$M_{\text{cut}}$ 的位置决定抛射物中 Fe-峰元素 vs. α 元素的比例——是 EMP 星 [α/Fe] 比值的最主要参数。

[FACT] **中子-质子比 $Y_e$**（电子分数）：决定 Fe-峰元素合成中 NSE 的走向。
- 爆炸区深处（靠近 NS）：$Y_e \approx 0.42–0.46$（中子富集）→ 合成 Ni/Co/Cr/Mn 等**奇 Z 元素**（odd-Z 元素）——**Mn 是 SN 中 odd-Z 元素的关键诊断**
- 外层：$Y_e \approx 0.49–0.50$ → 主要合成 Si/S/Ar/Fe 等偶 Z 元素

[FACT] **Mn 的唯一天然来源**：CC-SN 中 $Y_e < 0.49$ 的区域。[Mn/Fe] 几乎完全追踪 CC-SN 爆炸的**深处产额贡献**（§7.1.4）。

## 3.2 Mixing and Fallback Model

[FACT] **Mixing-fallback 参数化**（Woosley & Weaver 1995；Kobayashi et al. 2006）：
1. 假设存在一个**混合层** $\Delta M_{\text{mix}}$（典型 0.5–1.5 M☉），将外壳的 He/C/N 层"翻转"混合
2. 混合后的物质若动能不足以逃逸，则 fallback 回 NS

[FACT] **典型参数值**（Pop III 大质量星）：
- $M_{\text{cut}} \sim 6–10$ M☉（超新星），Hypernova 中 $M_{\text{cut}} \sim 2–6$ M☉
- 混合层 $\Delta M_{\text{mix}} \sim 0.5–1.5$ M☉
- **O/Fe 比强烈依赖 $M_{\text{cut}}$**：$M_{\text{cut}}$ 小 → 更多 O 逃逸 → [O/Fe] 高

[FACT] **EMP 星 [O/Fe]–[Mg/Fe] 双轴拟合**：这是反推 Pop III 前身星 $M_{\text{cut}}$ 与 $M_{\text{ZAMS}}$ 的标准方法（图 §13）。

## 3.3 Postshock Temperature and Explosive Nuclear Burning

[FACT] 爆炸核合成的分区由**峰值温度 $T_p$**（10⁹ K）决定，形成"温度-核素"对应图（Fig. 5）：

### 3.3.1 Complete Si burning ($T_p > 5 \times 10^9$ K)

- 达到 **NSE (Nuclear Statistical Equilibrium)**
- 主要产物：**⁵⁶Ni / ⁵⁶Fe**（$Y_e \sim 0.5$）；中子富集时 **⁵⁸Ni, ⁶⁰Zn**

### 3.3.2 Incomplete Si burning ($4 \times 10^9 < T_p < 5 \times 10^9$ K)

- 未达 NSE，"冻结"在 Fe-峰元素
- 主产物：**⁴⁴Ti, ⁵²Fe, ⁵⁴Fe, ⁵⁶Ni, ⁵⁷Ni, ⁵⁸Ni**
- ⁴⁴Ti 是观测中直接测量 SN 产额的关键核素（半衰期 ~60 yr）

### 3.3.3 Fe-peak elements and neutron excess

- 中子过剩 $\eta \equiv (N-Z)/(N+Z)$ 决定 Fe-峰丰度模式
- 中子富集区 → **odd-Z 元素** Mn, Cr, Co 富集
- 中子贫乏区 → **Ti, V, Ni** 主导

### 3.3.4 Explosive O-Ne-C burning ($3.3 \times 10^9 < T_p < 4.0 \times 10^9$ K)

- 主产物：**²⁸Si, ³²S, ³⁶Ar, ⁴⁰Ca**（经典 α 元素）
- 是**银河系 [α/Fe] 富集**的直接物理来源

[FACT] **更浅层的温度**：
- $T_p \sim 3 \times 10^9$ K：Explosive Ne burning → ²⁰Ne, ²⁴Mg
- $T_p \sim 2–3 \times 10^9$ K：Explosive C burning → ¹²C, ¹⁶O
- $T_p \lesssim 2 \times 10^9$ K：无有效核合成，仅冲击波压缩

## 3.4 Explosion Energy

[FACT] **标准爆炸能量 $E = 10^{51}$ erg ("1 foe")**。但 Pop III 与 Hypernova 的 $E$ 可跨越 $10^{50}$ 到 $10^{52}$ erg 两个数量级。

[FACT] 能量与产额的关系：$E$ 增大 → 冲击波穿透更深的内部 → $M_{\text{cut}}$ 减小 → 更多 Fe-峰元素逃逸 → [α/Fe] **下降**（因为 Fe 增长快于 α）。

[FACT] **Hypernova**（$E \sim 10^{52}$ erg, $M_{\text{ZAMS}} \sim 25–40$ M☉）：
- [O/Fe] 低（$<0.5$），[α/Fe] 平直
- **与 EMP 星中的 "plateau" 族一致**——是 Kobayashi et al. (2006) 提出的 Pop III 前身星主力候选

## [INTERPRETATION]

§3 是**产额表物理基础**的独立论证：产额表不是任意参数化，而是从 $T_p$ 分区 + $M_{\text{cut}}$ + $Y_e$ 分布三个物理量自洽推导的。这也是 Nomoto et al. (2013) 与 B²FH (1957) 的核心差别——B²FH 用稳态核反应网描述**恒星内部核合成**；本文描述**爆炸非稳态核合成**。

## [CRITIQUE]

- **Mixing-fallback 是唯象的**：真正的 3D 流体不稳定性 (convection, SASI, neutrino-driven mixing) 会改变 $M_{\text{cut}}$ 位置。Kobayashi et al. (2011) 后续已用 1D 流体不稳定性模型微调。
- **$M_{\text{cut}}$ 的不确定性**直接传导到 EMP 星拟合的质量/能量不确定性——典型误差 ±2–3 M☉ 和 ±0.5 dex in log(E)。

---
