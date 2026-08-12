> 本章属于：Theoretical Modeling of Starburst Galaxies (Kewley, Dopita, Sutherland, Heisler & Trevena 2001, ApJ 556:121)
>
> 下一章：`99_final_summary.md`

# 0. 文献基本信息

- **Title:** Theoretical Modeling of Starburst Galaxies
- **Authors:** Lisa J. Kewley, M. A. Dopita, R. S. Sutherland, C. A. Heisler († 1999 Oct 28), J. Trevena
- **Affiliation:** Research School of Astronomy and Astrophysics, Australian National University, Weston Creek PO, ACT 2611, Australia
- **Journal:** The Astrophysical Journal (ApJ), 556:121–140
- **Publication Date:** 2001 July 20（Received 2000 Nov 11; accepted 2001 Mar 28）
- **DOI:** 10.1086/320855 [FACT]（文献未直接给出 DOI 字符串，此处为期刊标准格式）
- **arXiv:** 未提供 [FACT]
- **Research Field:** 恒星天体物理 / 星系核合成 / 星云光谱诊断
- **Keywords:** galaxies: starburst — radiation mechanisms: thermal [FACT]

## 0.1 Abstract 精读

作者用 **PEGASE v2.0**（Padova 演化轨，Clegg & Middlemass PNN 大气模型）与 **STARBURST99**（Geneva 演化轨，Schmutz/Leitherer/Gruenwald W-R 大气模型）两套恒星种群合成代码生成了星暴年轻星团的 SED，再用 **MAPPINGS III** 光电离代码（含自洽尘埃物理与化学耗竭）计算星云发射线，并与 157 个温热红外星暴星系观测比对。

核心发现：[FACT]
1. 诊断图对 **1–4 Ry** 区间的 EUV 谱指数最敏感；
2. 温热红外星暴在 1–4 Ry 区间拥有**相对较硬**的 EUV 场；
3. PEGASE 的 1–4 Ry 连续谱比 STARBURST99 更硬，差异主要来自 **W-R 星大气模型** 的不同；
4. Schmutz 大气模型更接近物理现实，但无法单独产生 1–4 Ry 的硬 EUV——**连续谱金属不透明度（continuum metal blanketing）** 可能是解法之一；
5. SNR 激波机械能贡献到光电离模型 >20%（Hβ 光度贡献约 16–20%），不足以解释差异；
6. 给出新的**星暴–AGN 理论分类线**（rectangular hyperbola 拟合公式）。

## 0.2 论文结构树

```
1. INTRODUCTION
2. THE OBSERVATIONAL COMPARISON SAMPLE
3. STELLAR POPULATION SYNTHESIS MODELS
4. STARBURST MODELING
   4.1 Instantaneous Models
   4.2 Continuous Models
   4.3 Shock Excitation from Supernovae
5. WOLF-RAYET EMISSION IN STARBURST GALAXIES
6. CONTINUUM METAL OPACITY IN STARBURST GALAXIES
7. EXTREME STARBURST CLASSIFICATION LINE
8. CONCLUSIONS
```

---

# 1. Introduction（§1）

## 1.1 研究背景与动机

[FACT] 星暴星系观测可为大质量恒星形成区的物理过程与光谱特征提供关键洞察；其物理条件类似于早期宇宙星系坍缩形成时期，可用于理解早期星系演化。

[FACT] IRAS 卫星首次发现了大量红外亮星系（Rieke & Low 1972; Lutz et al. 1996, 1998; Genzel et al. 1998; Veilleux et al. 1995, 1999）；其中许多由剧烈恒星形成主导——年轻热星光加热周围尘埃，产生大量红外辐射。

[FACT] 目前理论工具已可推导以下恒星种群参数：
- 星暴年龄
- 金属丰度
- IMF（初始质量函数）
- SFR（恒星形成率）
- 恒星大气模型

[FACT] 发射线光谱可约束电离气体与 ISM 物理参数：气体密度、温度、压力；无大量尘埃星系中，Balmer 线亮度可直接估算总恒星形成率（Kennicutt 1998）。

[FACT] 将恒星种群合成模型产生的电离 UV 辐射场与自洽的光电离模型（**MAPPINGS III**, Sutherland & Dopita 1993；或 **CLOUDY**, Ferland et al. 1998）结合，可为任何 H II 区或星暴生成理论模型。自洽处理**尘埃物理与元素耗竭**是关键。

[FACT] 星云发射线光谱对电离 EUV 辐射的硬度极其敏感；光学线比诊断图可约束 EUV 光谱形状，也可估算平均电离参数与金属丰度。

## 1.2 诊断图发展史

[FACT]
- **BPT 1981**（Baldwin, Phillips & Terlevich）——首次用发射线比值将星系分为星暴/AGN 两类（AGN 电离光谱比热星硬得多）；
- **Osterbrock & de Robertis 1985**、**Veilleux & Osterbrock 1987 (VO87)**——修订了分类方案，本文使用修订版本；
- **Dopita et al. 2000**——用 MAPPINGS III 对河外 H II 区序列进行了理论再校准，量化了丰度、电离参数、连续 vs. 瞬时星暴模型的影响。

## 1.3 与之前工作的关键区别

[FACT] Dopita et al. 2000 显示：对高面亮度孤立河外 H II 区，PEGASE 与 STARBURST99 给出的电离 EUV 谱与 H II 区发射线谱**几乎一致**（由年轻 OB 星团激发）。

[FACT] 对于**星暴星系**（星暴光度可比肩宿主星系），情况截然不同：
- 恒星形成很可能持续至少一个星系动力学时标——**连续星暴（continuous starburst）** 假设更合适；
- 因此恒星质量损失配方与演化轨的假设起更大作用；
- 对 > 几 Myr 的星暴，**W-R 星** 在决定 EUV 谱强度与形状上至关重要。

[FACT] 对 W-R 星，以下不确定假设对 EUV 谱起决定性作用：
- 恒星寿命
- 风质量损失率
- 风速度定律
- 大气不透明度

## 1.4 本文目标与研究问题

[FACT] 本文提出新的连续恒星形成假设下的理论模型网格，结合 MAPPINGS III 与 PEGASE 2 / STARBURST99，用以：
1. 用 Kewley et al. 2000, 2001 的观测数据对 EUV 电离辐射场形状施加**新的观测约束**；
2. **分离并量化** 恒星大气模型与演化轨的选择对光学诊断图的影响；
3. 找出**在 He II 电离极限以下给出最硬 EUV 谱，但 He II 以上光子较少**的模型——这类模型能最好地拟合星暴星系在诊断图上的分布；
4. 为理论家研究大质量恒星演化晚期阶段提供新的观测约束。

---

# 2. The Observational Comparison Sample（§2）

## 2.1 样本选择标准

[FACT] 285 个温热 IRAS 星系样本，来自 Strauss et al. 1992 目录，选在 δ ≤ −10°，附加标准：

| # | 标准 | 数值 |
|---|------|------|
| 1 | 60 μm 流量 | ≥ 2.5 Jy；25, 60, 100 μm 有中等或高质量探测 |
| 2 | 红移 | log L_FIR < 11 时 z < 8000 km s⁻¹；log L_FIR ≥ 11 时 z < 30000 km s⁻¹ |
| 3 | 银纬 / 赤纬 | \|b\| ≥ 15°；δ ≤ −10° |
| 4 | 温热 FIR 颜色 | 8 ≤ F60/F25 ≤ 0.5（应为 −8 ≤ F60/F25 ≤ 0.5 之误，原文如此，疑为印刷）；2 ≤ F60/F100 ≤ 0.5（同上） |

[CRITIQUE] 选择标准的第 4 项颜色不等式数值（8 ≤ F60/F25 ≤ 0.5）在原文中是明显印刷错误，实际应为 log(F60/F25) 或类似量级。参考 Veilleux & Osterbrock 与 Kewley et al. 2001 原始选择为 0.5 ≤ (F60/F25) ≤ 8。

## 2.2 光谱观测

[FACT]
- 285 个中 225 个获得了 Hβ 处 50 km s⁻¹ 分辨率光学光谱；
- S/N > 3σ；
- 使用 Mount Stromlo & Siding Springs 2.3 m 望远镜的 Double Beam Spectrograph，蓝/红两段波长；
- 观测细节见 Kewley et al. 2000, 2001。

[FACT] 225 个样本通过 VO87 图上新的理论分类线分为 AGN / Starburst / LINER：
- **157 个星暴星系** —— 是本文星暴光谱建模的主要观测比较样本。

## 2.3 星暴样本中 AGN 污染的低估计

[FACT] 作者论证本星暴样本 AGN 污染低：
1. Kewley et al. 2001 显示诊断图对 AGN 存在极敏感——即使 AGN 仅贡献 **20%** 光学发射，线比值也会被推入 AGN 区域；
2. 本样本中 D₁ ≡ F60/F25 ≤ 8（即无温热色）的星暴很少，而温热色通常标志 AGN 能量主导。

[FACT] 结论：与 Veilleux et al. 1999 与 Genzel et al. 1998 一致——ULIRG 中分类为星暴的星系缺乏能量主导的 AGN。

[INTERPRETATION] 这意味着星暴样本的发射线光谱可视为**几乎纯净的恒星形成贡献**，是建模 EUV 场形状的理想目标。

---

# 3. Stellar Population Synthesis Models（§3）

## 3.1 两套代码的差别

[FACT]

| 属性 | PEGASE 2 | STARBURST99 |
|------|----------|-------------|
| 演化轨 | **Padova** (Bressan et al. 1993) | **Geneva** (Schaller et al. 1992) |
| 大气模型（高温/T > 50000 K） | **Clegg & Middlemass 1987 PNN** | **Schmutz, Leitherer & Gruenwald 1992 W-R 扩展大气** |
| 平面-平行大气 | Lejeune, Cuisinier & Buser 1997 (基于 Kurucz 1992) | Lejeune 网格 + 可选 Schmutz 扩展大气 |
| 质量损失 | "标准"与"增强" | "标准"与"增强"（Leitherer et al. 1999）|

[FACT] 对本文使用的诊断线比值而言，STARBURST99 的"标准"与"增强"质量损失方案差异 ≤ **0.03 dex**——可忽略。

## 3.2 演化轨细节

[FACT] Padova vs Geneva 的差别：
- **混叠（overshooting）**：Padova 对 m ≥ 1 M☉ 混叠，混叠距离/压力标高比更大，下探到更低质量；Geneva 仅在 > 1.5 M☉ 时混叠；
- **不透明度**：Padova 用 Iglesias, Rogers & Wilson 1992 OPAL 不透明度；Geneva 用 Rogers & Iglesias 1992；
- **混合长度**：两套轨相近；
- **氦含量**：Padova Y = 0.28；Geneva Y = 0.30；
- Padova 在质量与时间分辨率上更高。

## 3.3 瞬时 vs 连续星暴

[FACT] 大质量星氢燃烧寿命：
$$\tau \simeq 4.5 \left(\frac{M}{40\, M_\odot}\right)^{-0.43} \text{ Myr}$$

[FACT] 因此，对任何持续 > **~6 Myr** 的星暴，对 > **~20 M☉** 的所有质量均建立出生/死亡的动态平衡，同时 W-R 星也能对 EUV 做出完整贡献。

[FACT] Figure 1 显示（Z = 1 Z☉）：
- PEGASE 年龄 0–6 Myr，STARBURST99 年龄 0–8 Myr；
- **0 Myr（零龄）** 两套代码给出**几乎相同的 EUV 谱**——因为无 W-R 星、用相同 ZAMS 与相同热星大气模型；
- **> 5 Myr** 后谱形状不再变化（与 5 Myr 曲线重合）；
- 几 Myr 后 EUV 谱出现明显差异。

## 3.4 W-R 星物理——密度参数

[FACT] W-R 大气出射 EUV 谱关键取决于被用于维持 W-R 风区电离的电离光子比例，即发射测度 $\int n^2\, dr$，正比于：
$$\left(\frac{\dot{M}_0}{v_\infty}\right)^2 R_*^{-3}$$
即 **Schmutz, Hamann & Wessolowski 1989 密度参数**，其中 $\dot{M}_0$ 质量损失率、$v_\infty$ 终端速度、$R_*$ 光球半径。

[FACT] 相同密度参数的模型具有相似的发射线等值宽度，但总光度正比于 $R_*^2$。

[FACT] 可引入 **transformed radius**：
$$R_t \equiv R_* \left(\frac{v_\infty}{v_{\text{ref}}}\right) \left(\frac{\dot{M}_0}{\dot{M}_{\text{ref}}}\right)^{2/3}$$

[FACT] 使用更大比例 EUV 光子来维持扩展大气光电离的星，表现出：
- **较低强度**与**更硬**的 EUV 谱（在 He II 电离边以下，即 1–4 Ry 区间）；
- 更强的重元素大气屏蔽。

[CRITIQUE] 这正是 PEGASE（Clegg & Middlemass PNN）与 STARBURST99（Schmutz W-R）模型产生**谱形差异**的根本原因——两类大气模型在 T > 50000 K 区间的发射测度不同，导致硬 EUV 光子比例不同。

## 3.5 大气模型的物理合理性

[FACT]
- PEGASE 中 T > 50000 K 的星（含 W-R 星）用 Clegg & Middlemass **PNN 大气**——PNN 的表面重力**远高于** W-R 星；
- STARBURST99 中强风星（含 W-R 星）用 **Schmutz W-R 大气**——含 He 不透明度，**但不含重元素不透明度**。

[FACT] 因为 STARBURST99 专为星暴设计，其对 EUV 谱的建模在理论上更精细。

[INTERPRETATION] 作者因此更偏袒 Schmutz 大气模型（物理上更适合 W-R 星），但该模型无法单独解释观测到 1–4 Ry 的硬 EUV——因此 §6 提出引入 continuum metal opacities 作为补充方案。

---

# 4. Starburst Modeling（§4）

## 4.1 MAPPINGS III 计算参数

[FACT] 计算设置：
- **几何**：平面-平行、等压模型
- **电子密度** $n_e = 350$ cm⁻³（来自 [S II] λ6716, λ6731 禁戒线比值，配合 MAPPINGS III 五级模型原子推导；Kewley et al. 2001 中给出每颗星系的电子密度）
- **电离参数** $\chi$（cm s⁻¹，尺寸化）定义在星云**内边界**（最接近激发星处）；无量纲形式 $U = \chi/c$
- $\chi$ 变化范围：**5 × 10⁶ – 3 × 10⁸ cm s⁻¹**（即 log U = −3.5 – −2.0）
- 金属丰度：PEGASE **0.01 – 3 Z☉**；STARBURST99 **0.05 – 2 Z☉**

## 4.2 尘埃物理

[FACT] MAPPINGS III 中尘埃物理的自洽处理：
- 辐射场被尘埃吸收
- 尘埃带电
- 光电加热

[FACT] 尘埃模型：
- 硅酸盐颗粒：100 ≤ a ≤ 1000 Å
- 小非晶有机颗粒：10 ≤ a ≤ 100 Å
- 尺寸分布：**Mathis, Rumpl & Nordsieck 1977 (MRN)** 幂律
- 几何：球形
- 该尺寸范围确保耗竭因子与 Jenkins 1987（通过温暖弥散云看到的恒星 UV 消光测量）相似。

[FACT] MAPPINGS III 尘埃模型给出太阳丰度下每氢原子吸收：
$$\frac{E_{B-V}}{N(H)} \simeq 5.9 \times 10^{21} \text{ cm}^{-2} \text{ mag}^{-1}$$
（Bohlin, Savage & Drake 1978）

[FACT] 光电产率使用 Draine & Sutin 1987 曲线（更保守）；光电颗粒电流用 Draine 1978 + Laor & Draine 1993 尘埃吸收数据；电子/质子碰撞用 Draine 1978 标准"sticking"系数。

## 4.3 化学丰度与耗竭因子

[FACT] 未耗竭的太阳光谱丰度采用 **Anders & Grevesse 1989**。表 1 给出每元素的 log Z☉ 与 log D（耗竭因子）：

| 元素 | log Z☉ | log D |
|------|--------|-------|
| H | 0 | 0 |
| He | 1.01 | 0 |
| C | 3.44 | −0.30 |
| N | 3.95 | −0.22 |
| O | 3.07 | −0.22 |
| Ne | 3.91 | 0 |
| Mg | 4.42 | −0.70 |
| Si | 4.45 | −1.0 |
| S | 4.79 | 0 |
| Ar | 5.44 | 0 |
| Ca | 5.64 | −2.52 |
| Fe | 4.33 | −2.0 |

[FACT] 对非太阳丰度，尘埃模型与耗竭因子**保持不变**（作者承认无其他方法估计）。

[FACT] 除 N 和 He 外，所有元素视为**初级核合成产物**。这是简化假设——在 SFR 历史不同或星系风重要的系统中可能不成立（如 LMC/SMC 中 O/Fe 比值不同于太阳，Russell & Dopita 1992）。

[FACT] **He**：除原初值外，还有初级核合成分量，经验上匹配 SMC、LMC 与太阳丰度：
$$\frac{\text{He}}{\text{H}} = 0.081 + 0.026 \left(\frac{Z}{Z_\odot}\right)$$

[FACT] **N**：经验拟合（van Zee, Haynes & Salzer 1997）N/O 在 H II 区的行为——
- 对 $Z/Z_\odot \geq 0.23$：N 为**次级**元素，
$$\log(\text{N/H}) = -4.57 + \log(Z/Z_\odot)$$
- 对 $Z/Z_\odot < 0.23$：N 为**初级**元素，
$$\log(\text{N/H}) = -3.94 + 2\log(Z/Z_\odot)$$

[CRITIQUE] N 从初级到次级的 0.23 Z☉ 转折点为经验性拟合，缺乏严格的核合成模型支持。

## 4.4 氦含量与初始参数对化学演化的影响

[FACT] Padova Y = 0.28、Geneva Y = 0.30——0.02 的差异在演化轨寿命与最终 He 产率上有可测影响。

[FACT] Padova 在更高质量处下探的混叠与更大的混叠距离，使得 Padova 演化出的 W-R 星阶段与 STARBURST99（Geneva）不同。

[INTERPRETATION] 这些差异叠加到恒星大气模型（PNN vs W-R）上，共同决定了 EUV 谱 1–4 Ry 区间的硬度。

---

# 5. Instantaneous vs Continuous Models（§4.1–4.2）

## 5.1 瞬时模型（§4.1）

[FACT] 瞬时零龄星暴——因无 W-R 星、相同 ZAMS 与相同热星大气模型，PEGASE 与 STARBURST99 给出：
- 几乎相同的 EUV 谱形状；
- 几乎相同的 MAPPINGS III 光学线比值。

[FACT] 在 VO87 诊断图（Figs 4, 5, 6）上，瞬时模型的**主要问题**：
- 许多星暴星系落在电离参数-金属丰度网格曲面"折回"（fold）上方/右方；
- 这些点位于**"禁带"区域**——任何金属丰度与电离参数组合都无法到达；
- 要进入此区域，需混入**另一种激发机制**（激波 / 幂律辐射场），或**使用更硬的 EUV 电离谱**（特别是 1–4 Ry 区间）。

[FACT] 观测证据支持连续星暴：
- 许多星暴处于合并星系对——理论上恒星形成应持续星系动力学时标；
- 一些谱显示 Hβ 低等值宽度或 Hβ 吸收线特征——直接证据显示恒星形成持续数 Myr；
- Goldader et al. 1997 发现瞬时模型对亮红外星系给出的年龄范围不现实。

## 5.2 连续模型（§4.2）

[FACT] 连续星暴：
- PEGASE **6 Myr**、STARBURST99 **8 Myr** 后达到星生/星死的动态平衡；
- 因此这两个年龄作为连续星暴模型的假设年龄。

[FACT] Figure 9–11 显示三组连续模型在 VO87 上的表现：

**(a) PEGASE 2 (Padova + Lejeune + Clegg & Middlemass PNN)**
[FACT]
- **唯一**能覆盖几乎所有星暴星系的模型；
- 谱在 1–4 Ry 区间**随 W-R 星启动变硬**（PNN 大气的直接结果）；
- 电离参数范围：6 × 10⁶ ≤ χ ≤ 6 × 10⁷；
- 金属丰度覆盖 0.2 – 3 Z☉；
- 大多数星暴一致于 **1–3 Z☉**；低丰度物体罕见。

**(b) STARBURST99 (Geneva + Lejeune + Schmutz)**
[FACT]
- Schmutz 大气在 1–3 Ry 随星团年龄几乎不变；
- 与零龄瞬时模型给出相似结果；
- W-R 星在 He II 电离极限以上（4–8 Ry）贡献可观辐射——因此可探测 **He II λ4686**（§5 讨论）；
- **仍无法**解释约一半观测点的位置——需要更硬的电离谱。

**(c) STARBURST99 (Geneva + Lejeune  alone)**
[FACT]
- 1–4 Ry 区间辐射场**更软**；
- 理论网格落在所有观测点下方/左方——**被排除**。

## 5.3 诊断图关键数值

[FACT] 连续 PEGASE 模型覆盖区域：
- log([N II]/Hα): −2 到 0
- log([O III]/Hβ): −1 到 1.5
- log([S II]/Hα): −2 到 0
- log([O I]/Hα): −3 到 −0.5

[FACT] MAPPINGS III 网格参数：
- 电离参数 χ：5×10⁶, 1×10⁷, 2×10⁷, 4×10⁷, 8×10⁷, 1.5×10⁸, 3×10⁸ cm s⁻¹
- 金属丰度（Z/Z☉）：0.05, 0.1, 0.2, 0.4/0.5, 1.0, 1.5, 2.0, 3.0

[FACT] Dopita et al. 2000 证明：
- [O III] λ5007 / [O II] λλ3726,9 是**电离参数**的好诊断；
- [N II] λ6584 / [O II] λλ3726,9 是**丰度**的最佳诊断（在 0.1–3 Z☉ 单调）。

[FACT] 因本文光谱未覆盖 [O II]，Figures 7, 8（瞬时）与 12, 13（连续）专门提供给天文界使用。

---

# 6. Shock Excitation from Supernovae（§4.3）

## 6.1 激波激发的基本影响

[FACT] 纯光电离模型未包含 SN 激波机械能。激波主要效应：将理论网格在 VO87 上**向上并略微向右**移动。

## 6.2 激波/光电离贡献比值（关键公式 1）

[FACT] SN 与恒星风产生的机械能光度 $E_0^{\text{mech}}$ 通过辐射激波转化为光学线发射。激波 Hβ 相对光电离 Hβ 的贡献：

$$\frac{L_{\text{H}\beta}(\text{shock})}{L_{\text{H}\beta}(\text{photo})} = \frac{\alpha E_0^{\text{mech}}}{\alpha_{\text{eff}} \, h\nu_{\text{H}\beta} \, S^*} \quad (1)$$

其中 $\alpha$ 为转化为 Hβ 通量的比例、$\alpha_{\text{eff}}$ 为氢的有效复合系数、$S^*$ 为热星团产生的电离光子数。

## 6.3 SNR 辐射阶段

[FACT] SNR 变为辐射激波的条件：冷却时标 < 动力学膨胀时标。

[FACT] Sedov-Taylor 理论：
$$\tau_{\text{exp}} \equiv R/v_s = 5t/2$$

[FACT] Dopita & Sutherland 1996 辐射激波冷却时标：
$$\tau_{\text{cool}} \simeq 200 \, v_{100}^{-4.4} \, Z \, n \quad \text{（单位：yr）} \quad (2)$$
其中 $v_{100}$ 是激波速度（100 km s⁻¹ 单位），Z 相对太阳丰度，n 前激波密度。

[FACT] 代入 $n \simeq 350$ cm⁻³：SNR 通常在 **1 pc** 半径、**600 km s⁻¹** 速度时变辐射；此时 SNR 约 600 yr 老，膨胀时标约 1500 yr。

## 6.4 样本的 SFR 与 SNR 数目

[FACT]
- 总机械能光度：$6 \times 10^{41}$ erg s⁻¹ (M☉ yr⁻¹)⁻¹（Leitherer et al. 1999）；
- 由平均 IR 光度（Kennicutt 1998）导出 SFR ≈ **3.4 M☉ yr⁻¹**（注意 Kennicutt 定义 $L_{\text{IR}} = L_{\text{FIR}}$）；
- 假设 IR 光度均匀分布于 > 7 kpc 星系，1 kpc 视场内 SFR ≈ **0.07 M☉ yr⁻¹**；
- 用 Ha 光度对模板星暴的 SFR ≈ **0.04 M☉ yr⁻¹**（低于 FIR 值——尘埃吸收降低 Ha 探测）。

[FACT] 600 km s⁻¹ 激波模型（球形，1 pc 半径，太阳丰度，n = 350 cm⁻³）机械能光度：
$$3.6 \times 10^{39} \text{ erg s}^{-1}$$

[FACT] 预期 1 kpc 内总机械光度 ≈ $4 \times 10^{40}$ erg s⁻¹，因此平均有 **11.2 个 SNR** 同时存在于 1 kpc 视场内。

## 6.5 Table 2 — 激波贡献光度

[FACT] 600 km s⁻¹ 激波 + 球形前驱体（1 pc）产生的光度：

| 谱线 | L (erg s⁻¹) |
|------|-------------|
| [O III] | 2.5 × 10³⁹ |
| Hβ | 3.3 × 10³⁸ |
| Hα | 9.8 × 10⁴⁰ |

[FACT] SNR 对 Hβ 发射的贡献 ≈ **16–20%**。

## 6.6 综合 [O III]/Hβ 公式（关键公式 3）

[FACT] 观测总 log([O III]/Hβ) 为星暴与 SNR 贡献之和：
$$\log(\text{[O III]}/\text{H}\beta) = \log(\text{[O III]}_{\text{starb}} + \text{[O III]}_{\text{SNR}}) - \log(\text{H}\beta_{\text{starb}} + \text{H}\beta_{\text{SNR}}) \quad (3)$$

[FACT] 在 [O III]$_{\text{starb}} \to 0$（低全局 χ 极限）：
$$\log(\text{[O III]}/\text{H}\beta) \geq 0.0 \quad (4)$$
（密度 350 cm⁻³，SFR ≈ 0.07 M☉ yr⁻¹ 在 1 kpc² 内）

[FACT] 但观测到的实际下限为 log([O III]/Hβ) ≈ **−1.0**（比 SNR 模型下限低一个数量级）。

[FACT] **结论**：SNR 对 log([O III]/Hβ) 的贡献 **> 20%**，实际约 **~2%**（低一个数量级），**可忽略**。

[FACT] 200–300 km s⁻¹ 的激波速度预期与观测更相容，产生的 [O III]$_{\text{SNR}}$ 贡献可忽略。

---

# 7. Wolf-Rayet Emission in Starburst Galaxies（§5）

## 7.1 W-R 星系历史

[FACT]
- W-R 特征首次在矮发射星系 He2-10 发现（Allen, Wright & Goss 1976）；
- Osterbrock & Cohen 1982 定义 W-R 星系——含宽恒星发射线（大量 W-R 星）；
- Kunth & Joubert 1985：1 例正检，14 例疑似；
- Conti 1991 编目，宽 [He II] λ4686 或宽 λ4640 (N III) 为主要识别特征；
- Guseva, Izotov & Thuan 2000：几乎所有样本星系都显示宽 W-R 发射，是 N III λ4640、C III λ4650、[Fe III] λ4658、He II λ4686 的未分辨混合体；弱 W-R 线包括 N III λ4512、Si III λ4565。

## 7.2 模板平均星暴光谱

[FACT] 单个星系 S/N 不足以探测 W-R 特征，因此作者构建"平均"模板：
- 从样本中 56 个 Hβ S/N ≥ 60 且零红移蓝端截止 < 4620 Å 的星暴星系；
- **选择偏差警告**：选择高 S/N 星系可能偏向**年轻**、**更亮**的星暴；
- Hβ 吸收等值宽度（Gaussian 同时拟合吸收+发射，IRAF ngauss_fits）≈ **3.6 Å**；
- 对应连续星暴模型在太阳丰度下年龄上限 ≈ **7 Myr**（González Delgado & Leitherer 1999）。

## 7.3 He II λ4686 关键约束

[FACT] 模板平均光谱中：
- [Fe III] λ4658 与 He II λ4686 在 **2σ** 水平检出；
- 线不明显宽化——可能是低 S/N 效应；
- log(He II λ4686 / Hβ) ≈ **−1.6**。

[FACT] 模型预测对比：
| 电离连续谱 | log(He II λ4686/Hβ) |
|-----------|----------------------|
| PEGASE 或 STARBURST99 (Lejeune) | ≈ **−6** |
| STARBURST99 (Lejeune + **Schmutz**) | ≈ **−1.7** |

[FACT] Schmutz 扩展大气模型预测的 He II/Hβ ≈ −1.7 与观测 −1.6 **一致**，支持 Schmutz 大气更适用于星暴星系。

[FACT] 但 Schmutz 大气在 1–4 Ry 区间无法产生足够硬的 EUV——见 §6（continuum metal opacities 讨论）。

[INTERPRETATION] He II λ4686 提供了对 Schmutz 大气模型**唯一直接的光谱验证**，是 PEGASE vs STARBURST99 争论的关键锚点。

---

# 8. Continuum Metal Opacity in Starburst Galaxies（§6）

## 8.1 核心问题

[FACT] 观测要求在 1–4 Ry 区间有硬 EUV 场——PEGASE 提供了，但 Schmutz 扩展大气更适合星暴 W-R 星物理。

[FACT] 本文提出的可能解法：**在 Schmutz 扩展大气中使用 stellar population synthesis 模型时，引入 continuum metal opacities**。

## 8.2 EUV 不透明度研究史

[FACT]
- Aller 1959：用 21 cm H I 柱密度 + 均匀气体密度假设 → 估计 ISM 对 EUV 不透明；
- Cruddace et al. 1974：发现 ISM 不均匀 → 用覆盖因子 + 丰度估算有效吸收截面，证明 EUV 可穿透可观距离；
- Rumph, Bowyer & Vennes 1994：更新截面与丰度估算。

[FACT] 近年 EUV 望远镜（EUVE、ROSAT WFC、ALEXIS、FUSE、EIT）推进了恒星大气与一些 Seyfert 星系 EUV 研究（Cassinelli et al. 1995; Hwang & Bowyer 1997）。

[FACT] 但**星暴星系 EUV 谱仍不可见**——因 EUV 连续谱被吸收而弱到无法探测。因此必须依赖恒星种群合成代码的理论预测。

## 8.3 Continuum Metal Blanketing 的物理

[FACT] 连续谱金属不透明度与 H、He 不透明度一样，来自**束缚-自由跃迁**（即金属的光电离）。

[FACT] 连续谱金属不透明度允许：
- 部分 > 4 Ry 辐射被**吸收**，在 < 4 Ry 重新发射；
- 吸收比例取决于金属的吸收截面与丰度。

[FACT] 结果 EUV 连续谱：
- **He II 电离极限以上变软**（主要因 C 不透明度）；
- **1–4 Ry 区间更硬但更弱**——正是诊断图所需的形状。

[FACT] 潜在反证：若如此，Schmutz 模型应预测过多的 He II λ4686——与观测不符（观测 log ≈ −1.6，模型 ≈ −1.7，**相符**）。

[FACT] **结论**：Continuum metal blanketing 是可能解法之一，但**可能不是唯一解法**。

[CRITIQUE] 作者承认 He II λ4686 观测结果与 Schmutz 模型一致这一事实，使得 continuum metal blanketing 的解释力受到一定质疑——如果引入 continuum metal blanketing，He II λ4686 应更强。这一张力暗示问题可能是**多因素的**（如 IMF 斜率、W-R 星寿命、密度参数等）。

---

# 9. Extreme Starburst Classification Line（§7）

## 9.1 理论上限的构造

[FACT] 用 **PEGASE 网格**（最硬 EUV）在 VO87 诊断图上设定星暴模型理论上限。

[FACT] 现实范围：Z = 0.1 – 3.0；χ = 5 × 10⁶ – 3 × 10⁸ cm s⁻¹（−3.5 ≤ log U ≤ −2.0）；连续星暴模型**始终**落在经验上限线下方/左方。

[FACT] 原因：电离参数-金属丰度两参数网格在诊断图上**折回自身**——无参数组合能生成此折回上方的理论点。

## 9.2 关键公式（§7 三个分类线，矩形双曲线）

[FACT] Figure 16 显示分离星暴与其他激发机制的理论线（Kewley et al. 2001 使用的**极端星暴线**）：

$$\log\frac{\text{[O III]}\,\lambda 5007}{\text{H}\beta} \leq \frac{0.61}{\log(\text{[N II]}/\text{H}\alpha) - 0.47} + 1.19 \quad (5)$$

$$\log\frac{\text{[O III]}\,\lambda 5007}{\text{H}\beta} \leq \frac{0.72}{\log(\text{[S II]}\,\lambda\lambda 6717,31/\text{H}\alpha) - 0.32} + 1.30 \quad (6)$$

$$\log\frac{\text{[O III]}\,\lambda 5007}{\text{H}\beta} \leq \frac{0.73}{\log(\text{[O I]}\,\lambda 6300/\text{H}\alpha) + 0.59} + 1.33 \quad (7)$$

[FACT] 这些是**矩形双曲线**（rectangular hyperbolae）形式——是本文最重要的**可直接使用公式**。

[FACT] VO87 曾尝试用半经验方法确定该边界；本文首次给出**理论（而非半经验）** 星暴边界。

## 9.3 不确定度与分类效果

[FACT] 理论线 ±0.1 dex 用虚线表示（因化学丰度、耗竭因子、IMF 斜率、演化轨与大气模型误差）。

[FACT] 与 Kewley et al. 2001 中由激波建模产生的**极端混合线（extreme mixing line）** 结合，将星系分为 starburst、LINER、AGN 三类。

[FACT] 分类表现（关键对比）：
- 用理论极端星暴线：**6%** 模糊分类；
- 用传统 VO87 经验线：**16%** 模糊分类。

[FACT] **结论**：理论星暴线是**可靠的星系光学分类工具**，在不同诊断图上比 VO87 更一致。

---

# 10. 图表分析

## Figure 1 — EUV 谱随星暴年龄演化（Z = 1 Z☉）
- **(a) PEGASE** (Lejeune + Clegg & Middlemass PNN)
- **(b) STARBURST99 (Lejeune + Schmutz)**
- **(c) STARBURST99 (Lejeune only)**

**目的**：比较三组模型 EUV 谱随年龄演化，揭示 W-R 星启动后的差异。
**关键观测**：
- 零龄三曲线**重合**；
- >5 Myr 后 PEGASE（a）1–4 Ry 区间**最硬**；
- STARBURST99+Schmutz（b）在 >4 Ry（He II 以上）有最强辐射；
- STARBURST99+Lejeune 仅（c）**最软**。

## Figures 2–3 — Z = 0.2 与 2 Z☉ 的 EUV 谱
- 与 Fig. 1 相同结构；
- 高金属丰度下，大质量星对 EUV 场在**更年轻年龄**作出更大贡献；
- 1–4 Ry 区间**变硬**。

## Figures 4–6 — 瞬时模型在 VO87 图上
- [N II]/Hα、[S II]/Hα、[O I]/Hα vs [O III]/Hβ；
- **观测点大量落入"禁带"**——瞬时模型无法解释。

## Figures 7–8 — [O II] 相关图（瞬时）
- [N II]/[O II] vs [O III]/Hβ 与 [N II]/[O II] vs [O III]/[O II]；
- 观测上无 [O II] 数据，提供供天文界使用。

## Figures 9–11 — 连续模型在 VO87 图上
- **(a) PEGASE**：覆盖几乎所有观测点（最佳）；
- **(b) STARBURST99+Schmutz**：仍差，需更硬 EUV；
- **(c) STARBURST99+Lejeune**：被排除（太软）。

## Figures 12–13 — [O II] 相关图（连续）
- 同 Figs 7–8 用途。

## Figure 14 — 模板平均星暴光谱
- 56 个星暴星系平均（Hβ S/N ≥ 60, 蓝截止 < 4620 Å）；
- 通量单位：1 × 10⁻¹⁵ erg s⁻¹ cm⁻² Å⁻¹。

## Figure 15 — Fig. 14 局部放大
- 位置标记 N III λ4640、C III λ4650、[Fe III] λ4658、He II λ4686；
- [Fe III] 与 He II 在 2σ 检出。

## Figure 16 — 理论分类线与极端混合线
- 三幅 VO87 诊断图上的**粗线**为理论星暴上限；
- 虚线为 ±0.1 dex 误差范围；
- **极端混合线**（aggressive mixing line）用于星暴与 AGN 之间的过渡；
- 图中还显示 0%、20%、40%、60%、100% AGN 混合比例。

---

# 11. Conclusions（§8）重述

[FACT] 论文总结：
1. PEGASE 与 STARBURST99 用 157 个温热红外星暴星系比较，主差异在于**演化轨与恒星大气模型**；
2. 光学诊断图对**1–4 Ry 区间 EUV 谱硬度**最敏感；
3. PEGASE 在该区间比 STARBURST99 **更硬**，主要来自 W-R 星大气模型差异；
4. 模板平均光谱检出 **Fe III λ4658 与 He II λ4686**（2σ 水平），指示 W-R 活动，支持 Schmutz 大气模型；
5. **Continuum metal blanketing** 是使 Schmutz 大气模型达到观测 EUV 硬度的可能方案（但可能非唯一）；
6. SNR 激波机械能贡献到 EUV > 20%（Hβ 光度贡献 16–20%），**不足以**解释差异；
7. 用 PEGASE EUV 场给出**极端星暴线**（公式 5–7），分类可靠性优于 VO87。

---

# 12. 论证链（作者逻辑重建）

```
IRAS 温热星系含剧烈恒星形成 → EUV 电离辐射驱动星云发射线 → 
发射线诊断图对 1–4 Ry 硬度敏感 → 观测要求硬 EUV → 
PEGASE vs STARBURST99 差异主要源于 W-R 星大气 → 
Schmutz W-R 大气物理上更合理 → 但 Schmutz 无法单独给出 1–4 Ry 硬 EUV → 
He II λ4686 检出支持 Schmutz → 
Continuum metal blanketing 可能解决硬度差异 → 
SNR 激波贡献 >20% 不足以解决 → 
PEGASE 最硬 EUV 提供理论星暴上限 → 
给出公式 5–7 理论星暴分类线 → 
模糊分类率 6% (本文) vs 16% (VO87)，证明新分类更可靠
```

---

# 13. 关键参考文献与作用

| Reference | 作用 | 建议阅读 |
|-----------|------|---------|
| Dopita et al. 2000, ApJ 542, 224 | MAPPINGS III 对河外 H II 区的理论再校准（本文直接前身） | ★★★★★ |
| Kewley et al. 2000, ApJ 530, 704 | 观测方法与星暴星系初步分类 | ★★★★ |
| Kewley et al. 2001, ApJS 132, 37 | 样本全数据与最终分类 | ★★★★★ |
| Fioc & Rocca-Volmerange 1997, A&A 326, 950 | PEGASE 2 恒星种群合成代码 | ★★★★ |
| Leitherer et al. 1999, ApJS 123, 3 | STARBURST99 恒星种群合成代码 | ★★★★★ |
| Sutherland & Dopita 1993, ApJS 88, 253 | MAPPINGS III 光电离代码 | ★★★★★ |
| Veilleux & Osterbrock 1987 (VO87) | 半经验星暴/AGN 分类方案 | ★★★★★ |
| González Delgado & Leitherer 1999, ApJS 125, 479 | 星暴年龄定标（用于 §5 年龄上限估计） | ★★★ |
| Kennicutt 1998, ARA&A 36, 189 | SFR 与 L_FIR 关系 | ★★★★ |
| Clegg & Middlemass 1987, MNRAS 228, 759 | PNN 大气模型（PEGASE 用） | ★★★ |
| Schmutz, Leitherer & Gruenwald 1992, PASP 104, 1164 | W-R 大气模型（STARBURST99 用） | ★★★★ |
| Clegg 1992 / Cassinelli et al. 1995, ApJ 438, 932 | W-R 星大气 EUV 观测比较 | ★★★ |

---

# 14. 论文隐含假设与信息缺失

[FACT] 明确写出的隐含假设：
1. 非太阳丰度时，尘埃模型与耗竭因子**保持不变**；
2. 除 N 和 He 外所有元素为**初级核合成产物**；
3. 平面-平行、等压星云几何；
4. IMF 为**标准**（文献未明确说明斜率，疑为 Salpeter）；
5. 星暴星系 EUV 谱**不可见**，必须依赖理论；
6. He II λ4686 来自模板平均，可能偏向年轻/亮星暴。

[FACT] 文献**未明确提供**：
- IM F 具体斜率与质量范围；
- 具体每个星系的 SFR；
- PEGASE 与 STARBURST99 各自使用的 ZAMS；
- MAPPINGS III 网格的完整输出；
- He II λ4686 的实际等值宽度测量不确定度；
- 每个连续模型具体使用的金属丰度网格（0.01–3 Z☉ vs 0.05–2 Z☉ 的限制来自恒星轨本身）。

[CRITIQUE] 作者未讨论 IMF 斜率变化对 EUV 硬度的影响——这是重要的未系统量化的不确定度来源。
