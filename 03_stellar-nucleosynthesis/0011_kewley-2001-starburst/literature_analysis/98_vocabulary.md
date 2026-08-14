# 98. Vocabulary — 学术词汇与术语

> 文献：0011_kewley-2001（Kewley, Dopita, Sutherland, Heisler & Trevena 2001, "Theoretical Modeling of Starburst Galaxies", ApJ 556:121）。本词汇表基于 `literature_analysis/` 中各分析文件提取。
> 上一章：[[03_stellar-nucleosynthesis/0011_kewley-2001-starburst/literature_analysis/97_quality_check.md|97_quality_check.md]]
> 下一章：[[03_stellar-nucleosynthesis/0011_kewley-2001-starburst/literature_analysis/99_final_summary.md|99_final_summary.md]]

## A. 学术逻辑词（跨篇高频，标注逻辑功能）

| 中文逻辑词 | 英文等价词 | 词性 | 逻辑功能 | 原文/分析例句 | 逻辑说明 |
|-----------|-----------|------|----------|---------------|----------|
| 然而 | however | adv. | 转折 | "Schmutz 大气模型更接近物理现实，但无法单独产生 1–4 Ry 的硬 EUV——**连续谱金属不透明度（continuum metal blanketing）** 可能是解法之一" | 承前 Schmutz 更优 → 转后仍需补充机制 |
| 因此 | therefore | adv. | 因果 | "瞬时模型的**主要问题**：许多星暴星系落在电离参数-金属丰度网格曲面'折回'（fold）上方/右方；**'禁带'区域**——任何金属丰度与电离参数组合都无法到达" | 从瞬时模型结果推出禁带 |
| 从而 | thereby | adv. | 因果(由此) | "PEGASE 的 1–4 Ry 连续谱比 STARBURST99 更硬，差异主要来自 **W-R 星大气模型** 的不同" | 大气模型差异 → EUV 谱差异 |
| 而 | whereas | conj. | 对比 | "PEGASE 用 Clegg & Middlemass PNN 大气；STARBURST99 用 Schmutz W-R 大气" | 对比两套代码的大气模型 |
| 尽管 | despite | prep. | 让步 | "尽管本文使用 PEGASE 与 STARBURST99 两套独立代码，其 1–4 Ry 谱的差异主要源于 W-R 星大气模型" | 让步代码独立，但关键差异点单一 |
| 尤其 | in particular | adv. | 举例 | "星云发射线光谱对电离 EUV 辐射的硬度**极其敏感**" | 强调诊断图的关键灵敏区 |
| 特别是 | specifically | adv. | 举例 | "MAPPINGS III 中**尘埃物理**的自洽处理：辐射场被尘埃吸收、尘埃带电、光电加热" | 具体列举尘埃物理三要素 |
| 虽然 | although | conj. | 让步 | "作者因此更偏袒 Schmutz 大气模型（物理上更适合 W-R 星），但该模型无法单独解释观测到 1–4 Ry 的硬 EUV" | 让步 Schmutz 物理更优 |
| 于是 | consequently | adv. | 因果 | "SNR 机械能贡献到光电离模型 >20%（Hβ 光度贡献约 16–20%），不足以解释差异" | 从贡献量推出不足以解释诊断图 |
| 反之 | on the contrary | phrase | 转折 | "Geneva+Lejeune 被排除"（相对 PEGASE 唯一覆盖） | 承前 PEGASE 成功，转后排除某模型 |
| 进而 | furthermore | adv. | 递进 | "提出 **continuum metal blanketing** 作为在 Schmutz 大气中恢复 1–4 Ry 硬 EUV 的方案" | 递进提出解决方案 |
| 同时 | simultaneously | adv. | 递进 | "用**两套独立代码**（不同演化轨、大气、IMF 默认值）交叉检验理论预测的鲁棒性" | 两个方法并行 |
| 换言之 | that is | phrase | 举例 | "诊断图对 **1–4 Ry** 区间的 EUV 谱指数最敏感" | 关键物理约束 |
| 总之 | overall | adv. | 结论 | "分类模糊率 6%（理论）vs 16%（VO87）——本文最直接的实证价值" | 结论性对比 |
| 此外 | moreover | adv. | 递进 | "此外，SNR 贡献仅考虑单一激波速度（600 km s⁻¹），作者预期 200–300 km s⁻¹ 更相容" | 补充局限 |
| 甚至 | even | adv. | 递进 | "连续星暴**始终**落在经验上限线下方/左方" | 递进强调分类线稳健 |
| 如果 | if / should | conj. | 让步 | "如果引入 continuum metal blanketing，He II λ4686 应更强——**仍与观测相符**" | 假设性检验 |
| 由此 | hence | adv. | 因果 | "He II λ4686 观测提供对 Schmutz 大气模型**唯一直接的光谱验证**" | 从观测推出模型约束 |
| 尽管 | although | conj. | 让步 | "作者承认 He II λ4686 观测结果与 Schmutz 模型一致这一事实，使得 continuum metal blanketing 的解释力受到一定质疑" | 让步证据支持 Schmutz |
| 换言之 | i.e. | phrase | 举例 | "诊断图上的'折回'（fold）是两参数网格（Z-χ）的**内在拓扑**" | 定义折回 |

*共 20 个逻辑词，均在本篇分析文本中实际出现。*

## B. 领域术语（本篇特有）

| 术语（英文/中文） | 中文释义 | 出现次数 | 首次出现章节 |
|-----------------|----------|----------|-------------|
| starburst galaxy | 星暴星系 | 30+ | §0.1 |
| stellar population synthesis | 恒星种群合成 | 15+ | §1.1 |
| PEGASE (Fioc & Rocca-Volmerange) | PEGASE 恒星种群代码 | 15+ | §3 |
| STARBURST99 (Leitherer) | STARBURST99 恒星种群代码 | 15+ | §3 |
| MAPPINGS III | 光电离代码 | 15+ | §1.1 |
| Padua evolutionary tracks | Padova 演化轨 | 8+ | §3.2 |
| Geneva tracks | Geneva 演化轨 | 8+ | §3.2 |
| Clegg & Middlemass PNN atmosphere | PNN 高温大气模型 | 6+ | §3.1 |
| Schmutz W-R atmosphere | Schmutz 扩展 W-R 大气 | 8+ | §3.5 |
| Wolf-Rayet (W-R) star | 沃尔夫-拉叶星 | 20+ | §7 |
| emission measure ($\int n^2 dr$) | 发射测度 | 4 | §3.4 |
| density parameter | W-R 密度参数 | 4 | §3.4 |
| transformed radius | 变换半径 $R_t$ | 2 | §3.4 |
| EUV spectrum (1–4 Ry) | 极紫外光谱（54–756 eV） | 25+ | §0.1 |
| He II ionization edge | He II 电离边（4 Ry = 54.4 eV） | 8+ | §7 |
| He II λ4686 | 氦 II 4686 Å 发射线 | 10+ | §7.3 |
| photoionization | 光电离 | 10+ | §1.1 |
| ionization parameter (χ, U) | 电离参数 | 10+ | §4.1 |
| metallicity (Z/Z☉) | 金属丰度（相对太阳） | 12+ | §4.1 |
| depletion factor (D) | 尘埃耗尽因子 | 5 | §4.3 |
| BPT diagram (Baldwin-Phillips-Terlevich) | BPT 发射线诊断图 | 8+ | §1.2 |
| VO87 (Veilleux & Osterbrock 1987) | 半经验星暴-AGN 分类图 | 8+ | §1.2 |
| extreme starburst classification line | 极端星暴分类线（Kewley 2001） | 8+ | §9 |
| rectangular hyperbola | 矩形双曲线（分类线拟合形式） | 4 | §9.1 |
| instantaneous burst | 瞬时星暴 | 8+ | §5.1 |
| continuous starburst | 连续星暴 | 8+ | §5.2 |
| dynamical equilibrium (birth/death) | 星生/星死动态平衡 | 3 | §3.3 |
| continuum metal blanketing | 连续谱金属不透明度 | 10+ | §8 |
| bound-free opacity | 束缚-自由不透明度 | 3 | §8.3 |
| SNR (supernova remnant) | 超新星遗迹 | 10+ | §6 |
| radiative shock | 辐射激波 | 5 | §6.3 |
| Sedov-Taylor phase | Sedov-Taylor 自由膨胀相 | 3 | §6.3 |
| cooling time ($\tau_{cool}$) | 冷却时标 | 4 | §6.3 |
| SFR (star formation rate) | 恒星形成率 | 6+ | §6.4 |
| Kennicutt (1998) calibration | Kennicutt SFR 定标 | 3 | §6.4 |
| IRAS warm galaxy sample | IRAS 温热红外星系样本 | 5 | §2.1 |
| [O III]/Hβ | 诊断图纵轴（强激发比） | 10+ | §4.1 |
| [N II]/Hα, [S II]/Hα, [O I]/Hα | 诊断图横轴（低激发比） | 8+ | §4.1 |
| fold (grid topology) | 网格折回（禁带拓扑） | 5 | §5.1 |
| forbidden line ([S II], [O III]) | 禁戒线 | 5 | §4.1 |
| MRN dust size distribution | Mathis-Rumpl-Nordsieck 尘埃尺寸分布 | 3 | §4.2 |
| Bohlin-Savage-Drake (1978) | 消光-柱密度关系 | 2 | §4.2 |
| He/H–Z relation | 氦-金属丰度关系 | 3 | §4.3 |
| primary vs secondary N | 初级 vs 次级氮 | 5 | §4.3 |
| N/O–Z☉ 0.23 transition | 氮 0.23 Z☉ 转折点 | 4 | §4.3 |
| IMF (initial mass function) | 初始质量函数 | 3 | §1.1 |
| He II λ4640 (N III) | N III 4640 与 He II 4658 混杂 | 2 | §7.1 |
| [Fe III] λ4658 | 铁 III 4658 禁戒线 | 3 | §7.1 |
| W-R galaxy | W-R 星系（宽恒星发射线） | 4 | §7.1 |

*共 45 个领域术语（按出现频次大致降序排列；仅列出在本文分析文本中实际出现者）。*

## C. 长难句摘录

### C1. §1.3 星暴 vs H II 区的差异

> "对于**星暴星系**（星暴光度可比肩宿主星系），情况截然不同：恒星形成很可能持续至少一个星系动力学时标——**连续星暴（continuous starburst）** 假设更合适；因此恒星质量损失配方与演化轨的假设起更大作用；对 > 几 Myr 的星暴，**W-R 星** 在决定 EUV 谱强度与形状上至关重要。"

**主干**：星暴星系与 H II 区情况不同 → 需要连续星暴假设 → 演化轨和质量损失方案更关键 → W-R 星决定 EUV 谱。

**修饰**："情况截然不同"是总起转折；破折号内"连续星暴"是关键假设；"因此"引出连锁因果；分号连接三层递进。

**翻译**：对于星暴星系（其星暴光度与宿主星系相当），情况与 H II 区截然不同：恒星形成很可能持续至少一个星系动力学时标，因此连续星暴假设更为合适；这使得恒星质量损失配方与演化轨的假设产生更大的影响；而对持续时间超过几 Myr 的星暴，W-R 星在决定 EUV 辐射谱的强度与形状上起决定性作用。

---

### C2. §3.4 W-R 密度参数

> "W-R 大气出射 EUV 谱关键取决于被用于维持 W-R 风区电离的电离光子比例，即发射测度 $\int n^2\, dr$，正比于 $(\dot{M}_0/v_\infty)^2 R_*^{-3}$"

**主干**：W-R EUV 谱取决于电离光子比例 → 即发射测度 → 正比于密度参数。

**修饰**："即"是同位语定义；"$\int n^2 dr$"是发射测度的数学形式；"$(\dot{M}_0/v_\infty)^2 R_*^{-3}$"是 Schmutz 密度参数，含质量损失率、终端速度、光球半径三个物理量。

**翻译**：W-R 大气的出射 EUV 谱关键取决于用于维持 W-R 风区电离的电离光子比例，即发射测度 $\int n^2\, dr$，它正比于 Schmutz 密度参数 $(\dot{M}_0/v_\infty)^2 R_*^{-3}$，其中 $\dot{M}_0$ 是质量损失率、$v_\infty$ 是终端速度、$R_*$ 是光球半径。

---

### C3. §5.2 PEGASE 唯一覆盖

> "**PEGASE 2 (Padova + Lejeune + Clegg & Middlemass PNN)**：**唯一**能覆盖几乎所有星暴星系的模型；谱在 1–4 Ry 区间**随 W-R 星启动变硬**（PNN 大气的直接结果）；电离参数范围：6 × 10⁶ ≤ χ ≤ 6 × 10⁷；金属丰度覆盖 0.2 – 3 Z☉；大多数星暴一致于 **1–3 Z☉**"

**主干**：PEGASE 是唯一覆盖所有观测点的模型 → 因 PNN 大气使 1–4 Ry 变硬 → 给出电离参数与金属丰度约束。

**修饰**：分号连接五个事实：唯一覆盖 → 硬 EUV 来源 → χ 范围 → Z 范围 → 星暴普遍金属丰度 1–3 Z☉。

**翻译**：PEGASE 2（Padova 演化轨 + Lejeune 大气 + Clegg & Middlemass PNN 大气）是唯一能覆盖几乎所有观测星暴星系位置的模型；其 EUV 谱在 1–4 Ry 区间随 W-R 星的启动而变硬（这是 PNN 大气的直接结果）；模型覆盖的电离参数范围为 6×10⁶ ≤ χ ≤ 6×10⁷ cm s⁻¹，金属丰度范围为 0.2–3 Z☉，其中大多数观测星暴与 1–3 Z☉ 的金属丰度一致。

---

### C4. §6.6 SNR 贡献可忽略

> "**结论**：SNR 对 log([O III]/Hβ) 的贡献 **> 20%**，实际约 **~2%**（低一个数量级），**可忽略**。"

**主干**：SNR 对 [O III]/Hβ 的贡献 ~2% → 可忽略。

**修饰**：">20%"是 Hβ 光度的贡献上界（用于说明理论最大）；"实际 ~2%"是 [O III]/Hβ 的实际贡献；"低一个数量级"说明实际值比 Hβ 上界低 10×；"可忽略"是结论。

**翻译**：结论：尽管 SNR 对 Hβ 光度贡献可达 >20%，但对 log([O III]/Hβ) 的诊断比值贡献实际仅约 ~2%（比 Hβ 上界低一个数量级），因此可忽略。

---

### C5. §8.3 Continuum metal blanketing 方案

> "连续谱金属不透明度允许：**部分 > 4 Ry 辐射被吸收**，在 < 4 Ry 重新发射；吸收比例取决于金属的吸收截面与丰度……**He II 电离极限以上变软**（主要因 C 不透明度）；**1–4 Ry 区间更硬但更弱**——正是诊断图所需的形状。"

**主干**：连续谱金属不透明度 → >4 Ry 被吸收 → <4 Ry 重发射 → He II 以上变软 + 1–4 Ry 变硬变弱 → 满足诊断图。

**修饰**：分号列举三重效应（吸收、>4 Ry 变软、1–4 Ry 变硬）；"正是诊断图所需的形状"是结论性评价。

**翻译**：连续谱金属不透明度允许部分能量 >4 Ry（>54.4 eV）的辐射被金属元素吸收，并在 <4 Ry 波段重新发射；吸收比例取决于金属的光电离截面与丰度。其结果是 EUV 连续谱在 He II 电离极限以上变软（主要来自碳的不透明度），而在 1–4 Ry 区间变硬但变弱——这正是诊断图所需的谱形。