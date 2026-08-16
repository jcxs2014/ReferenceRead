---
title: "§99 Final Summary"
paper: "lhaaso-2021"
section: 99
nav_prev: "98_vocabulary.md"
nav_next: ""
---
上一章：`98_vocabulary.md` — §98
下一章：（无）

# §99. Final Summary — 最终总结

>

---

## 15.1 一句话总结

Cao et al. (2021, Nature 594:33–36) 报告 LHAASO KM2A 阵列在 308 天运行中，从银河系 12 个源探测到 >530 个 >100 TeV 光子（最高 1.4 PeV，来自 J2032+4102），全部 ≥7σ，**首次以 background-free 模式证实了银河系 PeVatron 的存在**。

---

## 15.2 核心方法

1. **缪子 veto 阵列**：5,195 EDs + 1,188 MDs（MD 埋深 2.5 m，20 辐射长度屏蔽电磁分量），N_μ/N_e < 1/230 判 γ
2. **CR 抑制 10$^{-5}$ @1 PeV** → background-free 探测模式
3. **似然比检验**（源+0.3° 高斯延展模板 vs. 背景-only 模型）
4. **SED 重建**：Δ(logE)=0.2 分 10 个 bin，向前展开 + 最小 $\chi^{2}$

---

## 15.3 最重要结果（定量）

| 物理量 | 值 |
|---|---|
| 光子数 >100 TeV | >530 |
| UHE γ 源数 | 12 |
| 最高能光子 | **1.4 PeV**（J2032+4102） |
| 最低显著性 | **7σ** |
| 蟹状星云显著性（136 d） | 30σ |
| 角分辨率 >100 TeV | 15–20 角分 |
| 能量分辨率 >100 TeV | <14% |
| 积分灵敏度 | 10$^{-14}$ erg cm$^{-2}$ s$^{-1}$ |
| CR 抑制 @1 PeV | 10$^{-5}$ |
| 三源内禀延展 | 0.30°、0.58°、0.36° |
| 三源 SED 谱指数（简单幂律） | Γ ≈ 2.9–3.4 |

---

## 15.4 核心创新

1. **首次 background-free UHE γ 探测**（缪子 veto 效率达 10$^{-5}$）
2. **首次无偏识别 12 个 PeVatron 候选**（vs HESS 2016 单个银心）
3. **首次 >1 PeV 光子来自单一源**（1.4 PeV, J2032+4102）
4. **三源 SED 用对数抛物线优于幂律** → 加速/吸收的"smooth cutoff"

---

## 15.5 与相关工作的关系

- **上承**：CASA-MIA（1980s，尝试失败）、HESS 2016（银心 PeVatron，~0.04 PeV）
- **库内关联**：
  - 0012_gabici-2019：PeVatron 搜寻方法论 → LHAASO 实现
  - 0004_blasi-2013：SNR 加速上限理论 → LHAASO 提供实测约束
- **后续发展**：完整 LHAASO 阵列灵敏度再降 1 量级；超 PeVatron 搜寻；WCDA+KM2A 全波段（1 TeV–1 PeV）精读

---

## 15.6 主要局限

1. PeVatron 除蟹星云外均未被 firm identification
2. 轻子 vs 强子机制在多数源有简并
3. 未配合中微子多信使数据
4. 蟹状星云 PSF 假设外推到所有源

---

## 15.7 我应该记住什么（12 条）

1. **1.4 PeV** 光子来自 LHAASO J2032+4102（天鹅座 Cocoon 方向）
2. **12 个 UHE γ 源** 全部 ≥7σ，>530 个 >100 TeV 光子
3. **KM2A 缪子 veto** 将 CR 抑制至 10$^{-5}$ @1 PeV
4. **1.4 PeV 光子误机概率 0.028%**，N_μ/N_e = 1/941
5. **积分灵敏度 10$^{-14}$ erg cm$^{-2}$ s$^{-1}$** 远超现有 γ 探测器
6. **三源 SED** 用对数抛物线拟合优于幂律（ΔAIC=2.5–5.7）
7. **12 源全部位于银河平面**，延展 ≥1°（≥10$^{4}$ pc$^{3}$ 尺度）
8. **100 TeV 通量范围 0.4–4 CU**（1 CU = 6.1×10$^{-17}$ ph/TeV/cm$^{2}$/s）
9. **蟹星云 = LHAASO J2108+5157**，首个"电子 PeVatron"证据
10. **J1908+0621 ↔ SNR G40.5-0.5**：若确认，SNR 首次加速 PeV 质子
11. **J2032+4102 ↔ Cyg OB2**：大质量恒星作为强子 PeVatron
12. **"tip of the iceberg"**：完整阵列预期发现数量级更多 UHE 源

---

## 15.8 Completeness Check

- [x] Abstract（p.7–24 原文摘要）
- [x] LHAASO facility overview（p.25–30）
- [x] KM2A detector design（p.308–336）
- [x] Data analysis pipeline（p.341–362）
- [x] 12 UHE γ-ray sources Table 1（p.63–80）
- [x] Three-source SED analysis（Fig. 1, p.45–200）
- [x] Scientific implications（p.136–147）
- [x] Background and systematics（p.351–390）
- [x] Statistical significance（p.362–390）
- [x] Future prospects（p.147–167）
- [x] Conclusions
- [x] Cross-references to gabici-2019、blasi-2013
- [x] Key numerical values verified against PDF (1.4 PeV + 12 源)

---

> 结束：本文共生成 **11 个分析文件**，覆盖 Nature 594 论文全部正文 + Methods + Fig.1 与 Table 1。
