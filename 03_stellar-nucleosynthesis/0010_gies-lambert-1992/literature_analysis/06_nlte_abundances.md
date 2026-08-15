# 6. Abundances from Non-LTE Calculations — non-LTE 丰度

> 本章属于：Gies & Lambert (1992) — ApJ 387:673
>
> 上一章：[[03_stellar-nucleosynthesis/0010_gies-lambert-1992/literature_analysis/05_lte_abundances.md|05_lte_abundances.md]]
>
> 下一章：[[03_stellar-nucleosynthesis/0010_gies-lambert-1992/literature_analysis/07_results_and_discussion.md|07_results_and_discussion.md]]

---

## 6.1 研究动机

[FACT] 由于样本恒星在 H-R 图上"adjacent to regions where departures from LTE become significant"，作者用 non-LTE 交叉验证丰度对 LTE 假设的敏感性。

---

## 6.2 C II、N II、O II non-LTE EW 表

[FACT] 来源：
- **C II**：Eber & Butler (1988)、Becker (1988)
- **N II**：Becker & Butler (1988a)、Becker (1988)
- **O II**：Becker & Butler (1988b)

[FACT] 这些表给出 W$\lambda$ 作为 T_eff、log g、$\xi$、丰度的函数，基于：
- blanketed **LTE 大气模型**
- 但 C II、N II、O II 原子的**详细 non-LTE 能级布居**

[FACT] 丰度计算方法与 § 5 相同：对给定 (T_eff, log g) 找每个 line 在三个 $\xi$ 下的丰度，再选 log $\epsilon$ vs EW 斜率为零的 $\xi$。

[FACT] **局限性**：
- Becker & Butler 表的 log g 最低到 3.0（O II 表到 3.5），对 3 颗 log g 更低的超巨星需**外推**；
- O II 表从 T_eff = 24,000 K 起，因此 T_eff < 23,000 K 的星不计算 non-LTE O 丰度。

---

## 6.3 Table 9 — Non-LTE 平均丰度（p.689–690）

[FACT] 表 9 对 39 颗星给出 non-LTE 平均的 log $\epsilon$(He)、log $\epsilon$(C)、log $\epsilon$(N)、log $\epsilon$(O)，及 $\sigma$、$\Delta$ 修正。

[FACT] 平均由以下线组成：
- 所有可用 C II 线；
- N II $\lambda$$\lambda$4630–5045 之间（不含 $\lambda$$\lambda$5002, 5025）；
- O II $\lambda$$\lambda$4638–4705 之间。

[FACT] **内部一致性**：不同线给出的丰度基本一致，**除**：
- **C II $\lambda$$\lambda$6578、6582**：丰度比其他 C II 线低 **> 0.3 dex**（异常，作者未纳入平均）

[FACT] **关键 non-LTE 均值**（从表 9 提取的非超巨星代表）：
- log $\epsilon$(He) ≈ 10.82 – 11.16（中值 ≈ 10.95）
- log $\epsilon$(C) ≈ 7.83 – 8.58（中值 ≈ 8.15）
- log $\epsilon$(N) ≈ 7.83 – 8.69（中值 ≈ 8.15）
- log $\epsilon$(O) ≈ 8.63 – 9.01（中值 ≈ 8.80）

---

## 6.4 He I 的 non-LTE 处理

[FACT] 用 **Auer & Mihalas (1973a)** 模型：改进的 He I 线展宽理论，允许 He 原子与大气模型的非 LTE 偏离。

[FACT] 该模型提供 3 条观测到的 He I 线（$\lambda$$\lambda$4713, 5015, 5047）在**太阳丰度**下的 LTE 与 non-LTE 预测 EW，以及 ±0.3 dex 丰度偏差下的非 LTE 预测。

### 式 (5) — 幂律近似

$$W_\lambda \propto \varepsilon^\beta, \quad \beta \approx 0.5$$

假设相对强的 He I 线在曲线生长的饱和区近似幂律。

### 式 (6) — He 丰度推导

$$\log \varepsilon(\text{He}) = 11.00 + \frac{1}{\beta}\log\frac{W_\lambda(\text{obs})}{W_\lambda(\text{NLTE})}$$

$W_\lambda(\text{NLTE})$ 与 $\beta$ 由 Auer & Mihalas 表按 T_eff、log g 插值得到。

[FACT] **已知系统误差**：作者 T_eff、log g 基于 line-blanketed 大气，而 Auer & Mihalas 不是——**热端恒星可能有系统误差**。

[FACT] **未处理**：
- 5 颗 T_eff > 28,500 K 的星（Auer & Mihalas 表到 27,500 K）；
- HD 198478（log g = 2.1，表到 log g = 2.5）。

[FACT] **结果**：
- 非超巨星全部**近太阳 He 丰度**（log $\epsilon$ ≈ 11.00）；
- 5 颗超巨星**显著 He 富集**，且若采用低温尺度 § 5，富集更甚；
- 作者**主张谨慎解释**：式 (5) 幂律在丰度显著偏离太阳时变不准确，超巨星 He 富集幅度可能有**大误差**。

[FACT] **Kudritzki et al. (1989)** 对 9 颗银河/Magellanic Cloud B 超巨星定量光谱分析，**全部 9 颗发现 He 富集**——支持本文发现的方向。

[FACT] He 富集的**次级影响**：不仅增强 He I 线，也改变 H 线与 Balmer 跳变强度。若超巨星确实 He 富集，本文用**太阳丰度大气**推导的 T_eff、log g 可能有系统误差 → 因此超巨星丰度**应视为初步结果**。

---

## 6.5 Si 线的 non-LTE 处理

[FACT] Becker & Butler (1990) 新发表的 Si II、Si III、Si IV EW 表被用于检查新预测是否改善 LTE 结果。

[FACT] **关键发现**：
- **Si II 异常**：LTE 平均 log $\epsilon$(Si) = 6.86 ± 0.19，**显著低于** Si III 与 Si IV；用 Becker & Butler (1990) non-LTE 也未改善；
- **Si III**（Lennon et al. 1986 non-LTE）：
  - LTE：log $\epsilon$(Si) = **7.63 ± 0.26**
  - non-LTE（Table 11）：log $\epsilon$(Si) = **7.69 ± 0.40**（删两热星 HD 34078, 36512 后）
  - LTE 与 non-LTE 结果**几乎相同**
- **Si IV**（3 颗星）：
  - LTE：log $\epsilon$(Si) = 7.51 ± 0.36
  - non-LTE（Becker & Butler 1990）：log $\epsilon$(Si) = 7.47 ± 0.08
  - 与 Si III 一致

[FACT] 作者**建议**：因 Si II 异常未解，**Si III 与 Si IV 的 Si 丰度更可靠**。

[FACT] Dufton et al. (1990) 对 h & $ι$ Per 与 Cep OB3 的 log $\epsilon$(Si) = 7.5 ± 0.2（1–2 条 Si III/IV 线），与本文 Si III 结果一致。

---

## 6.6 Table 8 — 超巨星丰度（低 T* 尺度，p.688）

[FACT] 若用 Underhill et al. (1979) 比本文低 ~3000 K 的超巨星温度：
- log $\epsilon$(He) 明显**更高**（He 富集更甚）；
- log $\epsilon$(C) 显著变化；
- log $\epsilon$(N) 也有变化。

[FACT] 示例：HD 51309
- He I：log $\epsilon$ = 11.46 ($\sigma$=0.14, n=3)
- C II：log $\epsilon$ = 8.51 ($\sigma$=0.07, n=5)
- C III：log $\epsilon$ = 8.63 ($\sigma$=0.15, n=12)
- N II：log $\epsilon$ = 8.63 ($\sigma$=0.15, n=12)
- N III：log $\epsilon$ = 9.21 ($\sigma$=0.10, n=8)
- O II：log $\epsilon$ = 9.21 ($\sigma$=0.10, n=8)
- Si II：log $\epsilon$ = 6.79 ($\sigma$=0.04, n=2)

[INTERPRETATION] 超巨星在低 T* 尺度下 N、C、O 都很高，但因太阳丰度大气的假设在 He 富集情况下不成立，这些值**应谨慎使用**。

---

## 6.7 关键数值汇总

| 参数 | LTE | non-LTE |
|------|-----|---------|
| C II 表 | Kurucz 大气 + WIDTH6 | Becker & Butler 1988a |
| N II 表 | 同上 | Becker & Butler 1988b |
| O II 表 | 同上 | Becker & Butler 1988c |
| He I 表 | WIDTH6 | Auer & Mihalas 1973a（幂律 $\beta$≈0.5） |
| Si III | Lennon et al. 1986 non-LTE | 同上 |
| Si IV | — | Becker & Butler 1990 |
| non-LTE 均值 log $\epsilon$(C) | — | ≈ 8.15 |
| non-LTE 均值 log $\epsilon$(N) | — | ≈ 8.15 |
| non-LTE 均值 log $\epsilon$(O) | — | ≈ 8.80 |
| non-LTE 均值 log $\epsilon$(He) | — | ≈ 10.95（非超巨星） |
| C II $\lambda$6578, 6582 异常 | — | 低 > 0.3 dex |
| Si II 异常 | log $\epsilon$=6.86 | non-LTE 未改善 |
| Si III 均值 | 7.63 ± 0.26 | 7.69 ± 0.40 |
| Si IV 均值 | 7.51 ± 0.36 | 7.47 ± 0.08 |

---

## 6.8 我的理解 [INTERPRETATION]

[INTERPRETATION]
1. 本文首次对早 B 星同时用**完整的 C II / N II / O II non-LTE EW 表**（Becker & Butler 三组 Munich 组工作）系统计算丰度，是 1990 年代初 B 星丰度分析的方法学里程碑；
2. 两条路径（LTE/non-LTE）丰度结果的一致性，是**反驳"non-LTE 效应污染 LTE 结果"这一潜在批评**的最强论据；
3. He 的幂律近似（式 5–6）是**实用的半解析方法**，但作者在超巨星上明确标注其不确定性，这种**对近似极限的自我约束**很专业。

---

## 6.9 潜在问题 [CRITIQUE]

[CRITIQUE]
1. Becker & Butler 表本身基于 Kurucz LTE 大气 + non-LTE 原子——**大气层 LTE**，对超巨星（低 log g、高 T_eff）而言，这仍是半 non-LTE；
2. Auer & Mihalas (1973a) He 模型不是 line-blanketed——热端 T_eff 有系统偏差，作者承认但未量化；
3. Si II 的 0.8 dex 异常（log $\epsilon$=6.86 vs Si III/IV 的 ~7.5）**未被解释**——可能源于 Si II 线的严重 non-LTE 效应、错误 log gf、或尘埃效应（但大气谱无尘埃），这是后续研究需要解决的问题；
4. 超巨星 3 颗需**外推** Becker & Butler 表，外推丰度的误差未量化。