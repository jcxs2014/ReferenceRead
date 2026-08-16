# 7. Chemical Evolution of Galaxies — Nomoto et al. (2013) §7 精读

> 本章属于：[[03_stellar-nucleosynthesis/0020_nomoto-2013/literature_analysis/00_overview.md|Nucleosynthesis in Stars and the Chemical Enrichment of Galaxies]]
>
> 上一章：[[03_stellar-nucleosynthesis/0020_nomoto-2013/literature_analysis/06_type_ia.md|06_type_ia]]
>
> 下一章：[[03_stellar-nucleosynthesis/0020_nomoto-2013/literature_analysis/08_emp_stars.md|08_emp_stars]]

---

> 重点章节（本任务化学演化模型 GCE）——§7 是产额表的**自洽性检验**：产额表能否复现观测的银河系化学演化？

## 7.1 Solar Neighborhood

[FACT] **GCE 基本方程**（closed-box + inflow 简化）：
$$ \frac{dM_g}{dt} = \psi_{\text{in}} - \psi_{\text{SFR}} - \psi_{\text{out}} $$
$$ \frac{d(M_g Z_i)}{dt} = \psi_{\text{in}} Z_{i,\text{in}} - \psi_{\text{SFR}} Z_{i,\text{ISM}} + \int \psi(t') \tau(t') Y_i(M, Z) \, dM \, dZ $$
其中 $Y_i(M,Z)$ 来自 §4 Yields Table 2013。

### 7.1.1 α Elements

[FACT] **[α/Fe] vs [Fe/H]** 的经典演化曲线（"knee" 特征）：
- 低 [Fe/H]（早期）：只有 CC-SN 贡献 → **[α/Fe] ≈ +0.4**（平坦）
- 转折点 [Fe/H] ≈ −0.5（"knee"）：SN Ia 加入 → Fe 增加快于 α → [α/Fe] **下降**
- 高 [Fe/H]（太阳邻域）：[α/Fe] ≈ 0（相对太阳）

[FACT] 转折点位置对**银河系形成时间**敏感：knee 越早 → 银河系形成越早。

### 7.1.2 Odd-Z elements

[FACT] **Na, Al, Cu** 显示**低金属丰度下降**：
- [Na/Fe]、[Al/Fe]、[Cu/Fe] 均随 [Fe/H] 增加而上升
- Al 由 AGB 星 (3–4 M☉) 的 H 壳 CNO 燃烧贡献为主

### 7.1.3 Iron-peak elements

[FACT] **[(Cr, Mn, Co, Ni, Zn)/Fe]** 与观测平均值一致——这是 Yields Table 2013 的**关键成功**：模型不需要额外调参就能复现这些元素的演化。

### 7.1.4 Manganese

[FACT] **Mn 是 SN Ia 的特征元素**：CC-SN 中 Mn 合成很少（需要 $Y_e < 0.49$ 的深处），SN Ia 中 $M_{\text{Mn}} \approx 0.1$ M☉。
- 低 [Fe/H]：< −1.5 时 [Mn/Fe] 单调下降
- [Fe/H] > −0.5：[Mn/Fe] → 0（SN Ia 主导）

[FACT] **[Mn/Fe] 是 SN Ia 时间出现最早的诊断**——比 [α/Fe] knee 更灵敏。

### 7.1.5 Zinc

[FACT] **[Zn/Fe] 平直**：观测显示 [Zn/Fe] 在 −4 < [Fe/H] < 0 全区间**近似常数**（~0.4）。
- 传统模型预测 [Zn/Fe] 应随 [Fe/H] 升高（因为 Zn 归入 SN Ia）
- **新解释**（本文采用）：低质量 CC-SN（EC-SN, §2.3.2）和 faint SN（§4.3）是**Zn 的重要来源**

### 7.1.6 Carbon

[FACT] **C 的来源是"混合体"**：低质量 AGB (1–4 M☉) 产额 ≈ 中等质量星 (4–8 M☉) 的产额 ≈ 大质量星 (8–40 M☉) 的产额——**三种贡献相当**
- [C/Fe] 在低 [Fe/H] 处富集（AGB 延迟短于 SN Ia）

### 7.1.7 Nitrogen

[FACT] **N 主要由中等质量 AGB (4–8 M☉)** 合成（CNO 循环平衡），延迟时间 ~10⁸ 年。
- 高 [O/Fe] 星 [N/O] 常数 → "primary N"
- 低 [O/Fe] 星 [N/O] 上升 → "secondary N"

### 7.1.8 Fluorine

[FACT] **F** 是有趣的元素：一部分由 AGB 星 ($^{22}$Ne(α,γ)$^{26}$Mg 等)，一部分由 超新星
- [F/O] 在 [O/H] ≈ −4 处**反转上升**——这是 AGB 星对 F 贡献的观测证据

## 7.2 Galactic Bulge

[FACT] 银心凸起（Bulge）：快速形成（~1 Gyr），[α/Fe] 高（knee 推迟到 [Fe/H] ≈ 0），[Fe/H] 分布以 0 为中心。
- **产额约束**：Bulge 的快速形成要求 CC-SN 主导 Fe 供应；SN Ia 贡献晚。

## 7.3 Galactic Thick Disk

[FACT] 厚盘：形成早于薄盘，[α/Fe] 高（+0.3 至 +0.4），[Fe/H] 分布 −1 到 0。
- **产额约束**：与 Bulge 类似但时间略晚

## 7.4 Galactic Halo

[FACT] 晕：形成最早（~13 Gyr），[Fe/H] 分布 −5 到 −1。
- **[α/Fe] 高且分散** → 早期"泄漏盒子"化学演化（泄漏模型漏出气体）
- **产额约束**：Pop III 与 Pop II CC-SN 的相对贡献敏感

## 7.5 Globular Clusters

[FACT] 球状星团：古老的（> 10 Gyr），内部元素丰度**高度均匀**（特别是 Fe-峰元素）——这是**单个 CC-SN 污染整个气体云**的"泄漏"印记
- 但**轻元素（C, N, O, Na）存在恒星内部的"丰度反相关"**（ON 反相关）——这是 AGB 星或大质量星快速反馈的证据

## 7.6 Dwarf Spheroidal Galaxies

[FACT] 矮星系（如 Sculptor, Fornax）：低 [Fe/H] 延展（−4 到 −1），**[α/Fe] knee 推迟到 −1 到 −0.5**（vs 银河系晕的 −1.5）——**产额表的强约束**
- 推迟 knee 意味着**气体流失 (outflow)**：SN 抛出的金属被吹走，Fe 被稀释

## 7.7 Damped Lyman-α Systems (DAMPs)

[FACT] DAMPs 是高红移 (z ~ 2–3) 中性气体云的光谱探针，提供**早期化学演化的快照**
- [O/H] 分布 −3 到 −1
- **[α/Fe] 分散度大** → 单个超新星污染的印记
- **[Zn/Fe] 平直** → 支持 §7.1.5 的 EC-SN 产额解释

## 7.8 Elliptical Galaxies

[FACT] 椭圆星系：快速形成（quench 早），**[α/Fe] 高且均匀**——是"快速形成"的化学化石
- **Mg2 指数**（MgFe 比值）：随有效速率 $v_{\text{eff}}$ 上升——"Fundamental Plane" 的化学对应物

## [INTERPRETATION] §7 是产额表的总验收

- Yields Table 2013 的 8 个 (M, Z, E) 网格点**同时**解释了 8 个元素族（α, odd-Z, Fe-peak, Mn, Zn, C, N, F）的演化——这是一个**"超定"约束**（>参数个数），是产额表的定量成功。
- 与 §0017 Käppeler 2011 的 s 过程产额互补：本文 GCE 用 s 过程产额解释 Ba、Eu 分布；用 CC-SN 产额解释 α、Fe、Mn、Zn 分布。

## [CRITIQUE]

- GCE 模型对**outflow 参数**（风速度、质量损失率）非常敏感；不同的 outflow 假设给出不同的产额约束
- **inhomogeneous GCE**（Kobayashi & Nakasato 2011）比 closed-box 更符合观测，但参数更多
- **Pop III 与 Pop II 的 IMF 差异** 在 §7 中未量化——是主要系统误差来源

---
