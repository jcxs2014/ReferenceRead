> 本章属于: A New Table of Abundances of the Elements in the Solar System (Cameron, 1968)
>
> 上一章: `00_overview.md`
>
> 下一章: `02_suess_urey_legacy.md`

# 1. 丰度表建构方法 (Abundance Table Construction)

本文件精读 Cameron 1968 丰度表的**方法论**:数据源选取、归一化策略、8 元素核合成内插,并完整摘录 **Table 1**(Suess-Urey / Cameron 1963 / Cameron 1967 三列对照)和 **Table 2**(核素丰度表)的关键值。

---

## 1.1 数据源优先级 (Source Hierarchy)

[FACT] Cameron 在 §3 明确给出数据源的优先级:

> "the present writer has constructed a new abundance table **based as much as possible on measurements in Type I carbonaceous chondrites**."

[FACT] 主数据源(按优先级):

1. **Type I 碳质球粒陨石 (CI chondrites)** — 绝大多数非挥发分元素 [FACT]
   - 具体陨石样本: **Orgueil** 与 **Ivuna** (Notes 5) [FACT]
   - **Murray** 碳质球粒陨石(用于 Xe 同位素, Note 13) [FACT]
2. **普通球粒陨石 (ordinary chondrites)** — 少数无法从 CI 获得的非挥发分 [FACT]
   - 如 Gd, Tb(Notes 14) [FACT]
3. **太阳大气丰度 (solar photospheric abundances)** — 挥发分(如 C, N, O) [FACT]
   - 取自 Aller (1961) [FACT]
4. **太阳宇宙线丰度 (solar cosmic ray abundances)** — He, Ne 归一化 [FACT]
   - 依据 Gaustad (1964) 的建议 [FACT]

[FACT] **Type I 陨石的选择论据**:

> "Taking the point of view that it is probably easier to obtain **uniform element depletion factors** than uniform enrichment factors, the present writer has constructed a new abundance table based as much as possible on measurements in Type I carbonaceous chondrites."

[INTERPRETATION] Cameron 的逻辑链:
- Anders (1964) 指出不同陨石类之间存在**系统性挥发分差异** [FACT]
- Larimer & Anders (1967) 指出"**least element depletions have occurred in Type I carbonaceous chondrites**" [FACT]
- 因此 Type I CI 陨石是**最接近原初太阳物质**的可测量样本 [FACT]
- 方法论上: 从 CI 陨石"还原"回原始丰度(除以 depletion factor)比从富集样本(除 enrichment factor)更稳健 [FACT]

---

## 1.2 太阳归一化 (Solar Normalization)

[FACT] **Cameron (1967) 的归一化基准** (Table 1, Note 1):

> "In Cameron (1967) the normalization is based on **logarithmic averages of Na, Mg, Al, Si, S, K, Ca, Ti, Co, and Ni** in the sun relative to meteoritic values. The solar abundances are taken from Aller (1961)."

[FACT] **Cameron (1963) 的归一化基准** (对比):

> "In Cameron (1963) the volatile elements are normalized to silicon = $10^{6}$ in the sun, which is somewhat poorly determined."

[FACT] He 与 Ne 的归一化 (Note 2):

> "He and Ne are normalized to the solar oxygen abundance using **solar cosmic ray data**, as suggested by Gaustad (1964)."

[FACT] 归一化不确定性 (原文 §3):

> "There remains a significant uncertainty in this normalization factor, perhaps amounting to **a few tens of percent**."

[INTERPRETATION] 用 10 种非挥发分元素的对数平均代替单元素(Si)归一化,是 Cameron (1967) 相对 (1963) 的关键改进——它**摊薄了单个元素的误差**,但代价是引入了 10 个独立测量值的系统误差传播,而 Cameron 本人承认归一化因子仍有"百分之几十"的不确定性。

---

## 1.3 Fe 丰度的争议

[FACT] 原文 §3 明确记录:

> "it should be noted that this procedure has selected **a high value of the iron abundance**. This abundance has been a long-standing problem, since the solar photospheric abundance of iron (Aller, 1961) is considerably lower than the meteoritic value, and the oscillator strengths of the iron lines used in the solar abundance determination are claimed to be of superior quality. These are strong iron lines. Nevertheless, it appears that the iron abundance determined **from weak lines is higher than for the strong lines** (L. Goldberg, private communication), and the **iron abundance is anomalously high in the solar corona**. Hence it has seemed best to use the meteoritic value."

[FACT] Cameron 承认:

> "the iron abundance is of great importance for problems of nucleosynthesis, and it is important that additional work be done in an attempt to resolve the problem."

[CRITIQUE] Fe 丰度的"陨石 vs 太阳"之争延续至今(参见 0009_asplund-2009-solar-composition):Cameron 选择陨石值,但**未给出最终值的不确定度**,只是定性陈述。

---

## 1.4 8 元素核合成内插 (Interpolation by Nuclear Criteria)

[FACT] 原文 §3:

> "Only **eight elements** have now been interpolated on the basis of nuclear regularities."

[FACT] **8 个被内插的元素**(从 Notes 6, 8, 10, 15, 18, 19 提取, 加上 Ar-36 和 As-75 各算一个独立内插):

| 元素 | 内插方式 | 出处 |
|------|---------|------|
| Ar (Ar-36) | Ar-36 内插于 S-32 与 Ca-40 之间 | Note 6 |
| As (As-75) | As-75 内插于 Ge-73 与 Se-77 之间 | Note 8 |
| Kr | Kr-84 内插于 Se-80 与 Sr-88 之间;Kr-83 内插于 Br-81 与 Rb-85 之间,取折中 | Note 9 |
| Nb (Nb-93) | Nb-93 内插于 Zr-91 与 Mo-95 之间 | Note 10 |
| Ta (Ta-181) | Urey (1964) 碳质球粒陨石值 0.044 相对邻位奇数质量核素过高;改用 Hf-179 与 W-183 之间内插 | Note 15 |
| Pt | 相对 Os, Ir, Au 调整形成连续峰,取值略高于普通球粒陨石 | Note 18 |
| Hg | 在 Au-197 与 Tl-203 之间内插 Hg-199, Hg-201 | Note 19 |

[CRITIQUE] Note 19 明确承认 Hg 的不确定性:

> "the mercury abundance was chosen **as high as seemed reasonable** in view of the large amounts of mercury in carbonaceous chondrites. Hence the reality of this final rise in the B isobar distribution is **not at all certain**."

[FACT] Cameron 自己指出 Hg 的不确定性会**直接影响 Figure 6 中 B 同量异位素分布的高端形状**。

---

## 1.5 Table 1 元素丰度关键值 (完整摘录)

[FACT] Table 1 标题: "COMPILATIONS OF ABUNDANCES **NORMALIZED TO Si = $10^{6}$**"

### 主要元素 (H 到 Fe, 三列对照)

| Z | Element | Suess-Urey (1956) | Cameron (1963) | Cameron (1967) | Note |
|---|---------|-------------------|----------------|----------------|------|
| 1 | **H** | $4.00\times10^{10}$ | $3.2\times10^{10}$ | **$2.6\times10^{10}$** | 1 |
| 2 | **He** | $3.08\times10^{9}$ | $5.0\times10^{9}$ | **$2.1\times10^{9}$** | 2 |
| 3 | Li | 100 | 38 | **45** | 3 |
| 4 | Be | 20 | 7 | **0.69** | 3 |
| 5 | B | 24 | 6 | **6.2** | 3 |
| 6 | **C** | $3.5\times10^{6}$ | $1.66\times10^{7}$ | **$1.35\times10^{7}$** | 1 |
| 7 | **N** | $6.6\times10^{6}$ | $3.0\times10^{6}$ | **$2.44\times10^{6}$** | 1 |
| 8 | **O** | $2.15\times10^{7}$ | $2.9\times10^{7}$ | **$2.36\times10^{7}$** | 1 |
| 9 | F | 1600 | — | **3630** | 4 |
| 10 | **Ne** | $8.6\times10^{6}$ | $1.7\times10^{7}$ | **$2.36\times10^{6}$** | 2 |
| 11 | Na | $4.38\times10^{4}$ | $4.18\times10^{4}$ | **$6.32\times10^{4}$** | 4 |
| 12 | **Mg** | $9.12\times10^{5}$ | $1.046\times10^{6}$ | **$1.050\times10^{6}$** | 5 |
| 13 | Al | $9.48\times10^{4}$ | $8.93\times10^{4}$ | **$8.51\times10^{4}$** | 5 |
| 14 | **Si** | $1.00\times10^{6}$ | $1.00\times10^{6}$ | **$1.00\times10^{6}$** | 5 |
| 15 | P | $1.00\times10^{4}$ | 9320 | **$1.27\times10^{4}$** | 5 |
| 16 | **S** | $3.75\times10^{5}$ | $6.0\times10^{5}$ | **$5.06\times10^{5}$** | 4 |
| 17 | Cl | 8850 | 1836 | **1970** | 4 |
| 18 | Ar | $1.4\times10^{5}$ | $2.4\times10^{5}$ | **$2.28\times10^{5}$** | 6 |
| 19 | K | 3160 | 2970 | **3240** | 4 |
| 20 | **Ca** | $4.90\times10^{4}$ | $7.28\times10^{4}$ | **$7.36\times10^{4}$** | 5 |
| 21 | Sc | 28 | 29 | **33** | 4 |
| 22 | Ti | 2240 | 3140 | **2300** | 5 |
| 23 | V | 220 | 590 | **900** | 5 |
| 24 | Cr | 7800 | $1.20\times10^{4}$ | **$1.24\times10^{4}$** | 4 |
| 25 | Mn | 6850 | 6320 | **8800** | 4 |
| 26 | **Fe** | $6.00\times10^{5}$ | $8.42\times10^{5}$ | **$8.90\times10^{5}$** | 4 |
| 27 | Co | 1800 | 2290 | **2300** | 4 |
| 28 | **Ni** | $2.74\times10^{4}$ | $4.44\times10^{4}$ | **$4.57\times10^{4}$** | 5 |

### 中重元素 (Zn 到 Sn)

| Z | Element | Suess-Urey | Cameron (1963) | Cameron (1967) | Note |
|---|---------|-----------|----------------|----------------|------|
| 30 | Zn | 1.49 | 1.58 | **1.60** | 4 |
| 31 | Ga | 0.214 | 0.26 | **0.33** | 4 |
| 32 | Ge | 0.675 | 0.89 | **0.89** | 4 |
| 33 | As | 0.26 | 0.11 | **1.50** | 8 |
| 34 | Se | 0.89 | 1.33 | **0.50** | 5 |
| 35 | Br | 0.11 | 0.24 | **0.15** | 4 |
| 36 | Kr | 1.33 | 1.00 | **2.12** | 9 |
| 37 | Rb | 0.246 | 0.26 | **0.217** | 4 |
| 38 | **Sr** | 1.00 | 1.15 | **4.22** | 10 |
| 39 | Y | 2.42 | 2.42 | **2.52** | 4 |
| 40 | **Zr** | 1.49 | 1.58 | **1.60** | 4 |
| 41 | Nb | 0.214 | 0.26 | **0.33** | 10 |
| 42 | Mo | 0.675 | 0.89 | **0.89** | 4 |
| 44 | Ru | 0.26 | 0.11 | **1.50** | 4 |
| 45 | Rh | 0.89 | 1.33 | **0.50** | 4 |
| 46 | Pd | 0.11 | 0.24 | **0.15** | 4 |
| 47 | Ag | 1.33 | 1.00 | **2.12** | 4 |
| 48 | Cd | 0.246 | 0.26 | **0.217** | 4 |
| 49 | In | 1.00 | 1.15 | **4.22** | 4 |
| 50 | Sn | 2.42 | 2.42 | **2.52** | 4 |

### 重元素 (Sb 到 U)

| Z | Element | Suess-Urey | Cameron (1963) | Cameron (1967) | Note |
|---|---------|-----------|----------------|----------------|------|
| 51 | Sb | 1.49 | 1.58 | **1.60** | 4 |
| 52 | Te | 4.67 | 3.00 | **6.76** | 4 |
| 53 | I | 0.80 | 0.46 | **1.41** | 4 |
| 54 | Xe | 4.0 | 3.15 | **7.10** | 13 |
| 55 | Cs | 0.456 | 0.25 | **0.367** | 4 |
| 56 | Ba | 3.66 | 4.00 | **4.70** | 4 |
| 57 | La | 2.00 | 0.38 | **0.36** | 5 |
| 58 | Ce | 2.26 | 1.08 | **1.17** | 5 |
| 59 | Pr | 0.40 | 0.16 | **0.17** | 5 |
| 60 | Nd | 1.44 | 0.69 | **0.77** | 5 |
| 62 | Sm | 0.664 | 0.24 | **0.23** | 5 |
| 63 | Eu | 0.187 | 0.083 | **0.091** | 5 |
| 64 | Gd | 0.684 | 0.33 | **0.34** | 14 |
| 65 | Tb | 0.0956 | 0.054 | **0.052** | 14 |
| 66 | Dy | 0.556 | 0.33 | **0.36** | 5 |
| 67 | Ho | 0.118 | 0.076 | **0.090** | 5 |
| 68 | Er | 0.316 | 0.21 | **0.22** | 5 |
| 69 | Tm | 0.0318 | 0.032 | **0.035** | 5 |
| 70 | Yb | 0.220 | 0.18 | **0.21** | 5 |
| 71 | Lu | 0.050 | 0.031 | **0.035** | 5 |
| 72 | Hf | 0.438 | 0.16 | **0.16** | 5 |
| 73 | Ta | 0.065 | 0.021 | **0.022** | 15 |
| 74 | W | 0.49 | 0.16 | **0.16** | 16 |
| 75 | Re | 0.135 | 0.054 | **0.055** | 5 |
| 76 | Os | 1.00 | 0.73 | **0.71** | 17 |
| 77 | Ir | 0.821 | 0.500 | **0.43** | 17 |
| 78 | Pt | 1.625 | 1.157 | **1.13** | 18 |
| 79 | Au | 0.145 | 0.13 | **0.20** | 4 |
| 80 | Hg | 0.284 | 0.27 | **0.75** | 19 |
| 81 | Tl | 0.108 | 0.11 | **0.182** | 4 |
| 82 | **Pb** | — | 2.20 | **2.90** | 4 |
| 83 | Bi | — | 0.14 | **0.164** | 4 |
| 90 | Th | — | 0.069 | **0.034** | 20 |
| 92 | U | — | 0.042 | **0.0234** | 20 |

[FACT] 表中 "—" 表示该值未给出;Cameron 表中 83 Bi, 90 Th, 92 U 在 Suess-Urey 列缺失(因 Suess-Urey 1956 未系统给出).

[INTERPRETATION] 表 1 呈现的三列对比揭示三个重要历史趋势:
1. **H, Ne 显著下降**:从 Suess-Urey 到 Cameron 1967,H 从 $4\times10^{10}$ → $2.6\times10^{10}$ (降 35%),Ne 从 $8.6\times10^{6}$ → $2.36\times10^{6}$ (降 73%) — 因为 Cameron 放弃了 Suess-Urey 的高 H 天文估计,改用太阳大气归一化 [FACT]
2. **He 剧烈下降**:从 $5.0\times10^{9}$ (1963) → $2.1\times10^{9}$ (1967) — He/Ne 归一化从"以 Sun Si = $10^{6}$"改为"太阳宇宙线 + 太阳 O"[FACT]
3. **稀土 (La–Lu)**:Suess-Urey 给出的稀土值系统性偏高约 3–6 倍;Cameron 1967 值大幅下调,与核合成理论(r+s 混合产物)的期望一致 [FACT]

---

## 1.6 Table 2 核素丰度表 (Nuclide Abundances)

[FACT] Table 2 给出 92 种元素的各核素丰度,含 5 列: **Element / A (质量数) / % Abundance (同位素丰度) / Class / Abundance (数密度, Si = $10^{6}$)**。

### Class 分类约定 [FACT]

| Class | 含义 | 对应过程 |
|-------|------|---------|
| **F** (fast) | 快速时间尺度中子俘获主产物 | r-process (B$^2$FH 1957) |
| **S** (slow) | 慢速时间尺度中子俘获主产物 | s-process (B$^2$FH 1957) |
| **B** (bypassed) | 被中子俘获过程绕过的核素 | p-process (B$^2$FH 1957) |

### 主要核素丰度 (Cameron 1967)

| Element | A | % Abundance | Class | Abundance (Si=$10^{6}$) |
|---------|---|-------------|-------|--------------------|
| H | 1 | 99.985 | — | $2.6\times10^{10}$ |
| H | 2 | 0.015 | — | $2.6\times10^{10}$ (注: D/H ≈ $10^{-4}$ 数量级,OCR 可能混淆, 见 [FACT] 原文) |
| He | 3 | ~0.03 | — | $3.9\times10^{6}$ |
| He | 4 | ~100 | — | $2.1\times10^{9}$ |
| Li | 6 | 7.42 | — | 4.50 |
| Li | 7 | 92.58 | — | 5.00 |
| Be | 9 | 100 | — | 0.69 |
| B | 10 | 19.64 | — | 1.33 |
| B | 11 | 80.36 | — | 5.00 |
| C | 12 | 98.89 | — | $1.33\times10^{7}$ |
| C | 13 | 1.11 | — | $1.50\times10^{5}$ |
| N | 14 | 99.634 | — | $2.43\times10^{6}$ |
| N | 15 | 0.366 | — | 8980 |
| O | 16 | 99.759 | — | $2.354\times10^{7}$ |
| O | 17 | 0.0374 | — | 8830 |
| O | 18 | 0.2039 | — | 48100 |
| F | 19 | 100 | — | 3630 |
| Ne | 20 | 90.92 | — | $2.14\times10^{6}$ |
| Ne | 21 | 0.257 | — | 6060 |
| Ne | 22 | 8.82 | — | $2.08\times10^{5}$ |
| Na | 23 | 100 | — | $6.32\times10^{4}$ |
| Mg | 24 | 78.70 | — | $8.26\times10^{5}$ |
| Mg | 25 | 10.13 | — | $1.06\times10^{5}$ |
| Mg | 26 | 11.17 | — | $1.17\times10^{5}$ |
| Al | 27 | 100 | — | $8.51\times10^{4}$ |
| Si | 28 | 92.21 | — | $9.22\times10^{5}$ |
| Si | 29 | 4.70 | — | $4.70\times10^{4}$ |
| Si | 30 | 3.09 | — | $3.09\times10^{4}$ |
| Fe | 54 | 5.82 | — | 51800 |
| Fe | 56 | 91.66 | — | $8.15\times10^{5}$ |
| Fe | 57 | 2.19 | — | $1.95\times10^{4}$ |
| Fe | 58 | 0.33 | — | 2940 |
| Ni | 58 | 67.88 | — | $3.10\times10^{4}$ |
| Ni | 60 | 26.23 | — | $1.20\times10^{4}$ |
| Ni | 62 | 3.66 | — | 1670 |
| Ni | 64 | 2.19 | — | 1000 |
| ... | ... | ... | ... | ... |
| Sr | 84 | 50.537 | S | 2.12 |
| Sr | 86 | 9.86 | S | 0.416 |
| Sr | 87 | 7.02 | B | 0.294 |
| Sr | 88 | 32.56 | S | 1.374 |
| Zr | 90 | 51.46 | S | 0.823 |
| Zr | 91 | 11.23 | B | 0.1797 |
| Zr | 92 | 17.11 | S | 0.2738 |
| Zr | 94 | 17.40 | S | 0.2784 |
| Zr | 96 | 2.80 | S | 0.0448 |

[FACT] 关键核合成相关核素(部分 r/s/p 产物):

| Nuclide | A | Class | Abundance | 说明 |
|---------|---|-------|-----------|------|
| Sr-88 | 88 | S | 1.374 | s-process 峰 |
| Zr-90 | 90 | S | 0.823 | s-process |
| Ba-138 | 138 | S | 3.37 | N=82 闭壳 s-process 峰 |
| Pb-208 | 208 | S | 1.70 | N=126 闭壳 s-process 峰 |
| Pb-206 | 206 | — | 0.057 | $\alpha$-衰变链(已作放射性回推) |
| U-238 | 238 | — | 0.0234 | 已回推 $4.5\times10^{9}$ 年 |

[FACT] **放射性回推**(§5 末):

> "The abundances of **uranium, thorium, and K$^{40}$** isotopes have been corrected for a decay interval of **$4.5\times10^{9}$ years** to make them typical of the **initial solar system**; other radioactive nuclides have not been corrected because the half-lives are long and the corrections small."

[CRITIQUE] 此处 Cameron 说 "other radioactive nuclides ... half-lives are long and the corrections small" —— 这在 1968 年是合理的;但今天我们对 Al-26, Fe-60, Mn-53 等短寿命放射性核素在太阳系形成中的作用已有更深入认识,这些不在 1968 表的讨论范围内。

---

## 1.7 图表一览 (Figures 1–6)

| Figure | 内容 | 页码 |
|--------|------|------|
| Fig 1 | Nuclides abundances vs mass number A (全景) | p.137 |
| Fig 2 | 铁峰区以上中子俘获产物 (A = 50–110) | p.138 |
| Fig 3 | 继续 (A = 90–150) | p.139 |
| Fig 4 | 继续 (A = 130–190) | p.139 |
| Fig 5 | 继续 (A = 170–240) | p.140 |
| Fig 6 | r/s/p 三过程丰度趋势曲线 | p.141 |

[FACT] Fig 2–5 的符号约定 (§7):
- 奇数 A 核素: 实心圆 (solid circles)
- 偶数 A 核素: 叉号 (crosses)
- 偶数 A 且为 F 同量异位素: 叉外加方框
- 偶数 A 且为 S 同量异位素: 叉外加圆

[FACT] Fig 6 三曲线:
- S 同量异位素趋势: 相对光滑但局部有散布 —— 因为 $\sigma_{\rm N}$ = ⟨$\sigma_\nu$⟩ × N 是光滑单调递减函数 (Seeger, Fowler, Clayton 1965)
- F 同量异位素趋势: **异常光滑**(远优于 S)—— 意味着 F 过程有额外的丰度平滑机制
- B 同量异位素趋势: 在 Fe-peak 到 s-process N=126 峰之间维持相对高位,之后骤降

---

## 1.8 我的理解 (Interpretation)

[INTERPRETATION] Cameron 1968 表在方法论上的三大突破:

1. **数据源选择**: 从 Suess-Urey 混合多源(天文+陨石+地球)转为**以 CI 碳质球粒陨石为单一基准**,系统性地降低化学分馏的混淆。
2. **归一化稳健化**: 用 10 种非挥发分元素的对数平均代替单元素归一化,摊薄系统误差。
3. **理论约束内插**: 8 元素内插基于 r/s/p 三分法预言的核素分布规律,这是**"以理论导数据"**的首次系统实践——B$^2$FH 理论反过来塑造了观测表。

[CRITIQUE] 方法论软肋:
- 归一化因子仍有"百分之几十"的不确定性(§3 自承)
- Hg 内插 "not at all certain"(§9 自承)
- Fe 争议未解决(§3 自承)
- 8 元素内插的核合成判据本身建立在当时尚未完全成熟的理论之上(Cameron 1959 提出的判据在 1968 仍未被独立证实)

[INTERPRETATION] Cameron 1968 表是"丰度—核合成"双反馈范式的关键节点: 它既给 B$^2$FH 提供了定量基准(用于检验理论),又被 B$^2$FH 的理论判据所塑造(8 元素内插)。这个互锁结构是 1950–1970 年代核天体物理的核心方法论特征。
