# Bhattacharjee & Sigl (1999) — Final Summary

> **原文**：P. Bhattacharjee & G. Sigl, "Origin and Propagation of Extremely High Energy Cosmic Rays", *Phys. Rep.* 320 (1999) 1–150, [arXiv:astro-ph/9811011](https://arxiv.org/abs/astro-ph/9811011).
>
> **注意**：本目录名为 `0001_longair-ptuskin-1999`，但实际论文是 **Bhattacharjee & Sigl (1999)**（非 Longair-Ptuskin）。本分析基于 PDF 真实内容。
> 上一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/98_vocabulary.md|98_vocabulary.md]]

---

## 1. 论文全景

这是 **UHECR 起源问题在 2000 年前最完整、最权威的综述**，涵盖从观测到传播理论、加速机制、top-down 拓扑缺陷模型到宇宙学约束的**全部内容**。文章引用 ~512 篇参考文献，跨越粒子物理、宇宙学、天体物理、磁场理论四大领域。

### 1.1 章节结构

| 章 | 主题 | 分析文件 |
|---|---|---|
| §1 | Introduction & Scope | `01_introduction.md` |
| §2 | Observed Cosmic Rays | `02_observed_cosmic_rays.md` |
| §3 | Bulk Origin: General Considerations | `03_figures.md` |
| §4.1–4.2 | Propagation & GZK Cutoff | `04_propagation_gzk.md` |
| §4.3 | UHE Neutrinos & Exotic Particles | `05_neutrinos_exotic_particles.md` |
| §4.4 | Galactic & Extragalactic Magnetic Fields | `06_magnetic_fields_constraints.md` |
| §4.7–4.8 | Transport Eqs & Quantum Gravity | `07_source_search_transport.md` |
| §5 | Bottom-up Acceleration & Sources | `08_acceleration_sources.md` |
| §6.1–6.3 | Top-down: Basic Idea & Fragmentation | `09_topdown_basic_fragmentation.md` |
| §6.4–6.5 | Cosmic Strings & Superconducting Strings | `10_cosmic_strings.md` |
| §6.6–6.8 | Monopoles, Vortons, Necklaces | `11_monopoles_vortons_necklaces.md` |
| §6.9–6.14 | General Param, MSRP, PBH, Exotic | `12_xparticles_special_models.md` |
| §7 | Observational Constraints on TD | `13_constraints_on_td.md` |
| §8 + Refs | Summary, Conclusions, References | `14_conclusion_and_references.md` |
| — | 文献元信息、目录、写作方法 | `00_overview.md` |

---

## 2. 核心结论

### 2.1 UHECR 观测事实

- **能谱**：膝（~3×$10^{15}$ eV）→ 踝（~3×$10^{18}$ eV）→ GZK 区（> $10^{19}$·⁹ eV）。
- **组成**：膝→踝逐渐变轻；踝后变重（与 Auger 2009 结果一致，原文当时仍认为 EHE 为纯核子）。
- **各向异性**：AGASA 1998–2000 数据 → **大尺度各向同性**，小尺度 ~ 30 Mpc 聚类 [83]。
- **AGASA 数据显示无 GZK cutoff** [82]（后来 Auger 2007 在 ~6×$10^{19}$ eV 观测到陡峭截断）。

### 2.2 传播物理的关键公式

- **GZK 阈值**（p + γ_CMB → Δ → p + π⁰）：E_p ≳ 5×$10^{19}$ eV。
- **能量损失长度**：l_E ≃ 50 Mpc（@ E > $10^{20}$ eV）；l_E ≃ 60 Mpc（@ 5×$10^{19}$ eV）。
- **CMB 上 pair production**：E ≃ $10^{13}$ – $10^{15}$ eV 处显著（对光子而言）。
- **EGMF 效应**：偏转 τ_E ∝ E⁻²（rectilinear），E⁻¹（Bohm），E⁻¹/³（Kolmogorov 扩散）。
- **AGASA 约束**：B ≲ 2×$10^{-11}$ (l_c/Mpc)^(−1/2)(d/30 Mpc)⁻¹ G（式 38）。
- **VLI 约束**：(c_p − c) < $10^{-23}$（若 $10^{20}$ eV 事件为质子）。

### 2.3 Bottom-up（加速）场景的困境

| 源 | E_max | 问题 |
|---|---|---|
| SNR | ~$10^{15}$ eV | 远不够 |
| AGN 核心 | ~$10^{19}$ eV | 能量损失阻止逃逸 |
| FR-II hot spots | ~$10^{21}$ eV | 距离 > 100 Mpc → GZK 损耗 |
| 简单脉冲星 | ~$10^{15}$ eV | pair-cascade 短路 |
| Magnetar Fe 风 | > $10^{20}$ eV (Fe) | 预言重核组成 |
| GRB dissipative wind | ~$10^{20}$ eV | 速率 ~ 每世纪一次（在 GZK 内）|
| 死 quasar 遗迹 [27] | ~$10^{21}$ eV | 需详细模型验证 |

### 2.4 Top-down 场景

**核心逻辑**：超重 X 粒子（m_X > $10^{11}$ GeV）衰变 → QCD 强子化 → 光子/中微子/核子，无需加速。

**关键公式**：
- DSAM E_max：E_c ~ $10^{17}$ Z (R/kpc)(B/μG) eV（式 49）。
- X 粒子衰变率基准：ṅ_X ~ $10^{35}$ Mpc⁻³ yr⁻¹（m_X = $10^{16}$ GeV，式 68）。
- 能量注入率基准：Q_0 ~ $10^{-21}$ eV cm⁻³ s⁻¹（式 69）。
- TD 一般参数化：ṅ_X = ($Q_{0}$/m_X)(t/$t_{0}$)^(−4+p)（式 93）。

**各 TD 过程的 p 值**：

| TD 过程 | p | 状态 |
|---|---|---|
| 宇宙弦 loop 碎裂 | 1 | Viable（η ~ $10^{13}$ GeV）|
| Monopolonium | 1 | Viable |
| Necklaces | 1 | Viable（r ≫ 1）|
| Vorton 衰变 | 2 | Viable（η_s ~ $10^{12}$–$10^{14}$ GeV）|
| SCS 最简单模型 | < 1 | **已排除**（CMB/BBN 约束）|
| MSRP 衰变 | 2 | Viable（halo 聚类）|

### 2.5 观测约束 (Four-Way Squeeze)

| 约束 | 限制 |
|---|---|
| **弥漫 γ-ray** (EGRET) | p = 0 完全排除；p = 1 需 q > 1.7（m_X = $10^{16}$ GeV）；$Q_{0}$ < $10^{-22}$ eV cm⁻³ s⁻¹ |
| **BBN / 4He 光致分解** | (³He+D)/H < 5×$10^{-5}$（与 γ 约束独立）|
| **CMB 畸变** | 排除 p = 0 |
| **弥漫 ν 通量** | SLBY98 ~ 0.15 yr⁻¹ (1 km³ @ > $10^{19}$ eV)，模型无关上限 (式 105) |

### 2.6 Top-down 场景的核心预言

1. **EHECR 由基本粒子组成**（核子 + 光子 + 中微子），**无重核**。
2. **硬谱**（α ~ 1.3–1.5）→ GZK 截断后有 **"recovery"**（或 "gap"）。
3. **γ/CR > 1** 在足够高 EHECR 能区（但 EGMF 或高 URB 可压低）。
4. **弥漫 ν 通量** ~ 0.1–1 event/yr @ 1 km³。
5. **GHXPD 各向异性** 10%–40%（Galactic Center vs Anticenter）。

---

## 3. 与 1999 年后数据的对照

### 3.1 验证的预言

- **Auger 2017–2019**：UHECR 到达方向与**邻近活动星系/星暴星系相关** [Auger PRD 2017–2018] → 支持**河外离散源**，否定 MSRP halo 主导场景，但**兼容 §6.13 中 GHXPD 作为 < 10% 分量的可能性**。
- **IceCube 2013–2020**：观测到弥漫 ν 通量，与本文 SLBY98 TD 预言的 ~1 PeV ν 事件率量级一致。
- **CMB Planck 2018**：宇宙弦 Gμ < $10^{-7}$ → 排除 GUT-scale ($10^{16}$ GeV) 弦 → 与 §10.6 讨论的 η ≲ $10^{13}$ GeV 轻弦场景一致。
- **GLAST/Fermi-LAT (2008+)**：弥漫 γ 谱在 10 MeV–100 GeV 比 EGRET 高 → TD 级联约束**更严**（§13.2 讨论的 ω_cas 上限需下调）。

### 3.2 未验证或被排除的预言

- **AGASA "无 GZK cutoff"** → Auger 2007 观测到清晰 GZK 截断 @ ~6×$10^{19}$ eV → **否定 AGASA 无 cutoff 结论**。
- **GHXPD 大尺度各向异性**（10%–40%） → Auger 数据未观测到相应量级的 halo 尺度各向异性 → **GHXPD 主导场景基本被排除**。
- **MSRP 作为暗物质**（Ω_X h² ~ 1）→ 现代暗物质搜索（LUX, XENON, PandaX, LZ）+ Auger 相关数据 → **超重 MSRP 主导场景受到严重限制**。
- **纯光子 EHECR** → Auger 组成测量显示 EHECR 为**核子/重核混合**（非光子主导）→ 对纯 TD 光子主导场景不利。

### 3.3 仍开放的问题

- **EGMF 强度**：本文讨论的 B ≲ $10^{-9}$ G → 现代 Faraday rotation 约束在 ~$10^{-9}$ G 量级（基本一致）。
- **Z-burst 机制**：取决于 eV 质量 ν 的宇宙数密度 → 若 ν 是 hot DM → 现代宇宙学（结构形成）**对 eV 质量 ν 极敏感** → Z-burst 场景受到限制。
- **TeV-scale Higgs X**（§6.11）：Fermi-LAT 数据显示 10–100 GeV 弥漫 γ 可能有额外成分 → 部分符合 [418] 预言，但非独特。

---

## 4. 方法论评述

### 4.1 论文的优势 [FACT]

- **四领域交叉**：第一篇将 QCD 强子化、宇宙学约束、AGN 加速、TD 模型在**同一框架**下系统整合的综述。
- **公式驱动**：关键公式从 DSAM (49) 到 general parametrization (93) 到级联谱 (98) 完整推导。
- **数值基准**：ṅ_X ~ $10^{35}$ Mpc⁻³ yr⁻¹ 与 Q_0 ~ $10^{-21}$ eV cm⁻³ s⁻¹ 至今仍被引用作为 benchmark。
- **Table 1** 是 UHECR 领域**首次**系统比较 TD 参数空间。

### 4.2 局限性 [CRITIQUE]

- **强子化不确定性**：MLLA+LPHD 仅在 ~100 GeV 验证 → 外推到 > $10^{14}$ GeV 不确定性极大。
- **EGMF 不确定**：1999 年时 B_EGMF 的测量极弱 → 现代数值在 ~$10^{-9}$ – $10^{-11}$ G。
- **Monte Carlo vs MLLA+LPHD 差异**：本文指出 [391] 两者在 m_X ≫ $10^{3}$ GeV 显著不同，但未做详细 MC 验证。
- **AGASA 数据的解读**：本文倾向于支持"无 GZK cutoff" → 后来被 Auger 否定。
- **各向异性测量能力**：1999 年北半球阵列无法观测 GC → Auger 南半球阵列直到 2010s 才解决。

---

## 5. 文件清单

| 文件 | 覆盖章节 | 字数估计 |
|---|---|---|
| `00_overview.md` | 文献元信息、目录结构 | ~1500 字 |
| `01_introduction.md` | §1 | ~1800 字 |
| `02_observed_cosmic_rays.md` | §2 | ~4000 字 |
| `03_figures.md` | §3 | ~3000 字 |
| `04_propagation_gzk.md` | §4.1–4.2 | ~5000 字 |
| `05_neutrinos_exotic_particles.md` | §4.3 | ~4500 字 |
| `06_magnetic_fields_constraints.md` | §4.4 | ~4000 字 |
| `07_source_search_transport.md` | §4.6–4.8 | ~4500 字 |
| `08_acceleration_sources.md` | §5 | ~5000 字 |
| `09_topdown_basic_fragmentation.md` | §6.1–6.3 | ~5500 字 |
| `10_cosmic_strings.md` | §6.4–6.5 | ~6500 字 |
| `11_monopoles_vortons_necklaces.md` | §6.6–6.8 | ~4000 字 |
| `12_xparticles_special_models.md` | §6.9–6.14 | ~7500 字 |
| `13_constraints_on_td.md` | §7 | ~8500 字 |
| `14_conclusion_and_references.md` | §8 + Refs | ~6000 字 |
| `99_final_summary.md` | **本文件** | ~4000 字 |
| **总计** | | **~68,000 字** |

---

## 25. Completeness Check

- [x] Abstract
- [x] Introduction (§1)
- [x] All main sections (§2–§8)
- [x] Methods（DSAM 加速理论、GZK 传播方程、拓扑缺陷计算）
- [x] Data（§2 观测谱：AGASA/HiRes/Fly's Eye 等全程外实验数据）
- [x] Background（CMB 光子场、EGMF、弥散伽马射线背景）
- [x] Signal（UHECR 事件聚类、GZK 截断、top-down 模型信号）
- [x] Statistics（小尺度聚类显著性、AGASA vs HiRes 差异）
- [x] Systematics（能量标度不确定度、B 场模型依赖性）
- [x] Results
- [x] Discussion（bottom-up vs top-down 全面对比）
- [x] Conclusion（§8 总结与展望）
- [x] Appendix（参考文献 ~512 篇）
- [x] Figures（Fig. 1–32 在主体文件中引用分析）
- [x] Important equations（Eq. 1–100+, 含 GZK 阈值、DSAM 最大能量、TD 能量注入率）
- [x] Important numerical values（核心数值已保留）
- [x] Important references（00_overview.md 已标注核心文献）

> 结束：本文共生成 16 个分析文件，覆盖文献全部 150 页（arXiv 版本）的正文与参考文献。