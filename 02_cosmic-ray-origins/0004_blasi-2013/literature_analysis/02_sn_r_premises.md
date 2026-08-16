---
chapter: 2
title: The bases of the SNR paradigm
pages: ""
sections:
  - "Summary"
related_chapters:
  prev: 01_introduction
  next: 03_test_particle_dsa
status: done
---

> 本章属于：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/00_overview.md|The Origin of Galactic Cosmic Rays（Blasi, 2013, arXiv:1311.7346）]]
>
> 上一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/01_introduction.md|01_introduction]]
>
> 下一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/03_test_particle_dsa.md|03_test_particle_dsa]]


# 2. The bases of the SNR paradigm

[FACT] §2 在原文中无三级子节编号，但由三个**主题段落**自然构成：(i) B/C ratio 反推扩散系数；(ii) SN 率反推加速效率；(iii) $\\xi_{\\rm CR}\\approx5$–10% 的\"10% 定律\"。本分章按原文的段落逻辑划分为三个 `###` 子节，标题逐字沿用原文自然段落主题，信息零丢失。

### B/C ratio → diffusion coefficient

> **中文译文**

[FACT] B/C ratio 是银河系 CR 传播研究最关键的**观测诊断量**：宇宙线在穿越银河系时，重核（C）与轻核（B）的流量比取决于 CR 沿旅程穿过的物质总量 grammage。

$$
X(E) = \\bar{n}\\,\\mu\\,v\\,\\tau_{\\rm esc}(E)
$$

[FACT] \"the ratio of boron and carbon fluxes is related to the grammage traversed by CRs, X(E) = $\\bar{n}\\,\\mu\\,v\\,\\tau_{\\rm esc}(E)$.\"

[FACT] \"For particles with energy per nucleon of 10 GeV/n the measured B/C corresponds to X ~ 1 g cm$^{-2}$.\"

**Eq. 1（逃逸时间）**：

$$
\\tau^* = \\frac{X(E^*)}{\\bar n \\mu c} = 90 \\left(\\frac{H}{3 \\text{ kpc}}\\right) \\text{ Myr}
$$

其中 $X\\sim 1$ g/cm$^{2}$；$\\mu\\approx1.4\\,m_p$；$\\bar n = n_{\\rm disc}\\cdot h/H = 5\\times10^{-2}\\cdot(n_{\\rm disc}/1\\text{ cm}^{-3})\\cdot(H/3\\text{ kpc})^{-1}$ cm$^{-3}$。

[FACT] \"$\\tau$* ~ 90 · (H/3 kpc) Myr\"（Eq. 1）——**比弹道时间大三至四个量级**，\"the strongest evidence so far for diffusive motion of CRs in the Galaxy.\"

[FACT] 由 $\\tau_{\\rm esc}$ 反推**扩散系数**：

$$
D(E) = 3\\times10^{28}\\left(\\frac{H}{3\\text{ kpc}}\\right) \\text{ cm}^2/\\text{s} \\quad \\text{at } 10\\text{ GeV}
$$

[FACT] 高刚度 B/C 数据与 $X(R)\\propto R^{-\\delta}$ 一致，$\\delta = 0.3$–$0.6$（刚度依赖的扩散，$\\delta\\approx0.3$ 对应 Kolmogorov 湍流，$\\delta\\approx0.6$ 对应 Kraichnan）。

[CRITIQUE] $\\delta$ = 0.3–0.6 范围过宽，源自 B/C 在高能段的斜率不确定。作者在此未展开，但对 §6.2 的**各向异性论证**（需要 $\\delta\\approx0.7$ 才能匹配 NLDSA 硬谱）有直接影响。

**关键参数**：

| 参数 | 数值 |
|------|------|
| $X(10\\text{ GeV/n})$ | ~1 g/cm$^{2}$ |
| $n_{\\rm disc}$ | ~1 cm$^{-3}$（标准） |
| $h$（盘面半厚度） | 150 pc |
| $H$（晕厚度） | ~3 kpc |
| $\\mu$ | ~1.4 $m_p$ |
| $\\tau_{\\rm esc}(10\\text{ GeV})$ | ~90 (H/3 kpc) Myr |
| $D(E=10\\text{ GeV})$ | ~$3\\times10^{28}$ (H/3 kpc) cm$^{2}$/s |
| $\\delta$ | 0.3–0.6 |

### SN rate → acceleration efficiency

> **中文译文**

[FACT] §2 的第二条链路用**银河 SN 率**和**单次 SN 能量**反推在地球处测到的质子谱，进而求得所需总加速效率 $\\xi_{\\rm CR}$。

[FACT] 单次 SN 动能：$E_{\\rm SN}=10^{51}\\cdot E_{51}$ erg；银河 SN 率 $R_{\\rm SN}\\approx30$ yr$^{-1}$；盘面半径 $R_d=10$ kpc。

[FACT] 注入谱形式：

$$
N(p) = \\xi_{\\rm CR}\\cdot E_{\\rm SN}/m^{2}\\cdot I(\\gamma)\\cdot(p/m)^{-\\gamma}
$$

其中 $I(\\gamma)\\approx 2(3-\\gamma)(\\gamma-2)/(4-\\gamma)$ 为归一化因子（保证总注入能量 $=\\xi_{\\rm CR}\\cdot E_{\\rm SN}$）。

**Eq. 2（地球处 CR 质子谱）**：

$$
J(E) = \\frac{c}{4\\pi}\\frac{N(E)\\,R_{\\rm SN}}{\\pi R_d^2\\cdot 2H\\cdot \\tau_{\\rm esc}(E)} = 8\\times10^{5}\\,\\xi_{\\rm CR}\\,I(\\gamma)\\left(\\frac{R_{\\rm SN}}{30\\,\\text{yr}^{-1}}\\right)\\left(\\frac{E}{m}\\right)^{-\\gamma-\\delta}\\left(\\frac{E^*}{m}\\right)^{\\delta}\\text{ m}^{-2}\\text{s}^{-1}\\text{sr}^{-1}\\text{GeV}^{-1}
$$

[FACT] **重要的不敏感性**：\"escape time normalized to B/C at $E^*$ makes $J(E)$ independent of $H$\"——即简单扩散模型里 CR 通量和 grammage 都按 $H/D(E)$ 标度，因此 halo 大小 $H$ 被消去。

[FACT] 归一化到 10 GeV 通量后得到**Eq. 3（所需 CR 加速效率）**：

$$
\\xi_{\\rm CR} \\approx 2.5\\times10^{-3}\\,\\frac{1}{I(\\gamma)}\\left(\\frac{E^*}{m}\\right)^{\\gamma-2}\\left(\\frac{R_{\\rm SN}}{30\\,\\text{yr}^{-1}}\\right)^{-1}
$$

[FACT] \"$\\xi_{\\rm CR}$ ≃ 2–3% ... the total CR acceleration efficiency is somewhat higher than the estimate in Eq. 3 ... between 5% and 10% for the bulk of SNRs.\"

[CRITIQUE] 银河系 SN 率 $R_{\\rm SN}=30$ yr$^{-1}$ 存在系统性不确定性（±30%），直接影响 $\\xi_{\\rm CR}$ 反演。

[CRITIQUE] 作者**未讨论源分布的径向依赖**（如内盘密度高）对 $\\xi_{\\rm CR}$ 估算的影响。

**ISM 声速与 Mach 数（Eq. 5–6，属 §3 前提，但基础在 §2 建立）**：

$$
c_s = \\sqrt{\\gamma_g kT/m_p} \\approx 11\\left(\\frac{T}{10^4\\text{ K}}\\right)^{1/2} \\text{ km/s}
$$

$$
\\mathcal{M}_s = V_{\\rm ej}/c_s \\approx 900\\,E_{51}^{1/2}\\,M_{\\rm ej,\\odot}^{-1/2}\\,(T/10^4\\text{ K})^{-1/2}
$$

### $\\xi_{\\rm CR} \\approx 5$–10% (the \"10% rule\")

> **中文译文**

[FACT] §2 的**核心结论**：把重核（非质子）的能量也计入后，总加速效率上修到 5–10%，与 Baade–Zwicky 提出 SNR 假说以来的\"10% 定律\"（10% of SN kinetic energy into CRs）**精确吻合**。

[FACT] 反演链：**B/C ratio** → $\\tau_{\\rm esc}$ → $D(E)$ 与 $\\delta$ → 由 SN 率 + 注入谱反演 $\\xi_{\\rm CR}$。两条链路（B/C 诊断 + SN 能量预算）互相独立、交叉验证。

**关键参数**：

| 参数 | 数值 |
|------|------|
| $R_{\\rm SN}$ | ~30 yr$^{-1}$ |
| $E_{\\rm SN}$ | $10^{51}$ erg |
| $R_d$（盘面半径） | 10 kpc |
| $\\xi_{\\rm CR}$（仅质子） | 2–3% |
| $\\xi_{\\rm CR}$（含重核） | **5–10%** |

[INTERPRETATION] $\\xi_{\\rm CR}\\approx10\\%$ 的\"10% 定律\"是 SNR 范式的**能量锚点**——但**并非直接观测**，而是推导值，受 SN 率、源分布、传播模型影响。

[INTERPRETATION] 作者用一条完整的能量预算推导说明 SNR 在**能量上**足以支持作为 CR 主源——这构成 SNR 范式的第一根支柱（\"能量学论证\"）。

---

## 元数据

```yaml
chapter: 2
pages: ""
subsections: ["B/C ratio → diffusion coefficient",
              "SN rate → acceleration efficiency",
              "$\\xi_{\\rm CR} \\approx 5$–10% (the \"10% rule\")"]
key_formulas:
  - "X(E) = n̄ · μ · v · τ_esc(E)"
  - "τ* = X(E*)/(n̄ μ c) = 90 (H/3 kpc) Myr (Eq. 1)"
  - "J(E) = (c/4π) N(E) R_SN / (π R_d^2 · 2H · τ_esc(E)) (Eq. 2)"
  - "ξ_CR ≈ 2.5×10$^{-3}$ / I(γ) · (E*/m)^(γ−2) · (R_SN/30 yr$^{-1}$)$^{-1}$ (Eq. 3)"
  - "c_s ≈ 11 (T/10$^{4}$ K)^½ km/s (Eq. 5)"
  - "M_s ≈ 900 E$_{51}$^½ M_ej,⊙$^{-}$½ (T/10$^{4}$ K)$^{-}$½ (Eq. 6)"
keywords:
  - B/C ratio
  - grammage X
  - escape time τ_esc
  - diffusion coefficient D(E) ∝ E^δ
  - SN rate R_SN
  - acceleration efficiency ξ_CR
  - 10% rule
references_internal:
  prev_chapter: 01_introduction
  next_chapter: 03_test_particle_dsa
```

**引用页码**：全文引用基于 *Physics Reports 525 (2013) 1–32*，arXiv:1311.7346，§2 pp. 9–10（对应论文 Eq. 1–6）。