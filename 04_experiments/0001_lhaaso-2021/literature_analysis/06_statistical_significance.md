---
title: "§6 Statistical Significance"
paper: "lhaaso-2021"
section: 6
nav_prev: "05_background_and_systematics.md"
nav_next: "07_future_prospects.md"
---
上一章：`05_background_and_systematics.md` — §5
下一章：`07_future_prospects.md` — Statistical Significance

# §06. Statistical Significance — 统计显著性

>
>

---

## 6.1 显著性定义

[FACT] 原文对 Table 1 显著性的定义（原文 p.78–80）：**"statistical significance of detection above 100 TeV (calculated using a point-like template for the Crab Nebula and LHAASO J2108+5157 and 0.3° extension templates for the other sources)"**。

[FACT] 方法（原文 p.355–362）：似然比检验（likelihood ratio test）——源信号模型 vs. 背景-only 模型；对 12 源假设 0.3° 高斯延展模板。

---

## 6.2 12 源的显著性一览

| 源名 | 显著性 (σ) | E_max (PeV) |
|---|---|---|
| LHAASO J0534+2202 | **17.8** | 0.88 |
| LHAASO J1825-1326 | **16.4** | 0.42 |
| LHAASO J1839-0545 | 7.7 | 0.21 |
| LHAASO J1843-0338 | 8.5 | 0.26 |
| LHAASO J1849-0003 | 10.4 | 0.35 |
| LHAASO J1908+0621 | **17.2** | 0.44 |
| LHAASO J1929+1745 | 7.4 | 0.71 |
| LHAASO J1956+2845 | 7.4 | 0.42 |
| LHAASO J2018+3651 | 10.4 | 0.27 |
| LHAASO J2032+4102 | 10.5 | 1.42 |
| LHAASO J2108+5157 | 8.3 | 0.43 |
| LHAASO J2226+6057 | 13.6 | 0.57 |

[FACT] **全部 12 个源 ≥7σ**（原文 p.19, p.29, p.362），最低为 J1929+1745 与 J1956+2845 的 7.4σ。

[FACT] **三个最显著源**（16–18σ 段）：J0534+2202、J1825-1326、J1908+0621——这些源被选为 SED 分析的样本（原文 p.391–404）。

---

## 6.3 蟹状星云与单事件验证

[FACT] **蟹状星云检测**：136 天运行达 **30σ** 显著性（原文 p.334–335）。

[FACT] **1.4 PeV 光子误机概率**：对 J2032+4102 最高能光子（原文 p.375–390），通过 10,000 MC 事件（几何参数与实测事件一致，±10% 总粒子数、±2σ ED 数）估计能量与误差；N_μ/N_e = 1/941 拒绝几乎全部 CR 背景；在 1° 锥内 >1.4 PeV 的 1,044 个观测事件中，误机概率估计为 **0.028%**（原文 p.386–390）。

---

## 6.4 统计量与 AIC

[FACT] 三源 SED 拟合的对数抛物线 vs 幂律 AIC 比较（原文 Fig. 1 caption, p.190–200）：
- **J2226+6057**：AIC(LOG)=11.6 vs AIC(PL)=15.1 → ΔAIC = 3.5（log-parabola 显著更好）
- **J1908+0621**：AIC(LOG)=24.4 vs AIC(PL)=30.1 → ΔAIC = 5.7
- **J1825-1326**：AIC(LOG)=12.3 vs AIC(PL)=14.8 → ΔAIC = 2.5

> 分析：所有三源均支持对数抛物线（含能量依赖的谱陡化）——物理意义：加速截断或 γ-γ 吸收叠加的"smooth cutoff"。

[FACT] **TS 图（significance map）**：√TS = σ，对 25 TeV 以上 γ 用高斯型 PSF 平滑（原文 p.194–200）。

---

## 6.5 多检验校正

[FACT] 本文未明确报告天图扫描的 trials factor，但 12 源全部 >7σ，即使考虑大天区的 trials factor，也远高于偶然阈值（原文 p.362）。

---

## 6.6 与既有观测对比

[FACT] **HESS 2016 银心 PeVatron**（引文 2）：γ 谱延伸至 ~0.04 PeV，硬谱 → LHAASO 1.4 PeV 是量级提升（原文 p.13–17）。

[FACT] **Tibet ASγ、HAWC**（引文 3–6）：少数 >100 TeV 的"marginal detection"（原文 p.406–417）——LHAASO 12 源的 >7σ 显著性远超这些报告。

[FACT] **CASA-MIA**（引文 24–25）：1980s 首个 >100 TeV γ 尝试，因 MD 密度不足（~1%）无法达到 10$^{-4}$ 背景抑制——LHAASO 的 1,188 MD 覆盖解决了这一瓶颈（原文 p.407–417）。
