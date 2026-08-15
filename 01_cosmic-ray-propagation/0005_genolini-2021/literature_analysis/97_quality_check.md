# 97. Quality Check — Completeness 自检
> 上一章：[[01_cosmic-ray-propagation/0005_genolini-2021/literature_analysis/05_summary_conclusion.md|05_summary_conclusion]]
> 下一章：[[01_cosmic-ray-propagation/0005_genolini-2021/literature_analysis/98_vocabulary.md|98_vocabulary]]

## 文献信息

| 字段 | 内容 |
|---|---|
| 标题 | New minimal, median, and maximal propagation models for DM searches with Galactic CRs |
| 作者 | Y. Génolini, M. Boudaud, M. Cirelli, L. Derome, J. Lavalle, D. Maurin, P. Salati, N. Weinrich |
| 期刊 | Physical Review D 104, 083005 (2021) |
| DOI | 10.1103/PhysRevD.104.083005 |
| arXiv | arXiv:2103.04108 |
| 年份 | 2021 |
| 页数 | ~20 页 |
| 类型 | 方法论 + 数据分析 |

## 文件清单

| 文件 | 行数 | 状态 |
|---|---|---|
| 00_overview.md | 82 | ✓ |
| 01_introduction.md | 62 | ✓ |
| 02_generalities.md | 176 | ✓ 传输方程 + DM 通量标度推导 |
| 03_statistical_method.md | 74 | ✓ pinching 方法 |
| 04_new_min_med_max.md | 83 | ✓ 定量结果 |
| 05_summary_conclusion.md | 38 | ✓ |
| 97_quality_check.md | — | ✓ |
| 98_vocabulary.md | — | ✓ |
| 99_final_summary.md | — | ✓ |

## 公式覆盖

| 编号 | 公式 | 所在分章 | 状态 |
|---|---|---|---|
| 1 | CR 传输方程（能量空间）| 02_generalities | ✓ |
| 2 | DM 湮灭源项 $Q = \langle\sigma v\rangle\rho^2/(2m^2) \cdot dN/dE$ | 02_generalities | ✓ |
| — | NFW 剖面 | 02_generalities | ✓ |
| 4 | $L \ll R$ 时通量 $\propto \rho_\odot$ | 02_generalities | ✓ |
| 7 | $dp/dE \propto L^2/K$ | 02_generalities | ✓ 核心 |
| 8 | NFW 级数展开 | 02_generalities | ✓ |
| 10 | 正电子传播尺度 $\ell = \sqrt{4K/\dot{E}}$ | 02_generalities | ✓ |
| 15 | $de^+/dE \propto L^2/(K^{1/2}\dot{E}^{1/2})$ | 02_generalities | ✓ 核心 |
| A1 | 扩散系数完整形式（含高低刚度断裂）| 02_generalities | ✓ |
| — | Handy fitting formulae（附录 E）| 04_new_min_med_max | 已标注 |

## 数值信息检查

| 数值 | 值 | 状态 |
|---|---|---|
| $K_0$（MED）| $10^{27.97}$ cm$^{2}$/s | ✓ |
| $L$（MED）| 4.0 kpc | ✓ |
| $\delta$（MED）| 0.46 | ✓ |
| $R_l$（MED）| 5.0 GV | ✓ |
| $\ell$（MED）| 1.50 | ✓ |
| 暗晕尺度半径 $r_s$ | $\sim 20$ kpc | ✓ |
| 银心距离 $R_\odot$ | $\sim 8.2$ kpc | ✓ |
| 反质子不确定性缩小 | $\sim 6$ 倍 | ✓ |
| 正电子不确定性缩小 | $\sim 2$ 倍 | ✓ |

## 已知不足

1. **§IV 拟合公式未详细展开**：附录 E 的 fitting formulae 因 OCR 局限未完全提取
2. **BIG 和 QUAINT 方案**：附录 C 讨论，但正文以 SLIM 为主
3. **Figure 分析**：本文 Fig. 1-4（参数分布、通量比较），已在正文按说明分析