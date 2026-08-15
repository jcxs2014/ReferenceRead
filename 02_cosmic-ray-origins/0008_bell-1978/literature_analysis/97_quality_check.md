# 97. Quality Check — 完成度自查
> 上一章：[[02_cosmic-ray-origins/0008_bell-1978/literature_analysis/05_critical_assessment.md|05_critical_assessment]]
> 下一章：[[02_cosmic-ray-origins/0008_bell-1978/literature_analysis/98_vocabulary.md|98_vocabulary]]

> **文献**：`0008_bell-1978`  
> **精读方式**：PDF 视觉读取（页 147–156）+ 已知物理推导交叉验证

## 文献信息

| 字段 | 内容 |
|---|---|
| 标题 | The acceleration of cosmic rays in shock fronts — I |
| 作者 | A. R. Bell（Mullard Radio Astronomy Observatory, Cavendish Laboratory） |
| 期刊 | MNRAS 182, 147–156 (1978) |
| DOI | 10.1093/mnras/182.2.147 |
| 收到 | 1977 June 23 |
| 本文归属 | DSA 理论起源（与 B&O 1978 双源头） |

## 文件清单

| 文件 | 状态 | 行数 |
|---|---|---|
| 00_overview.md | ✅ | 73 |
| 01_introduction.md | ✅ | 100 |
| 02_energy_spectrum.md | ✅ | 144 |
| 03_alfven_waves.md | ✅ | 137 |
| 04_application_snr.md | ✅ | 55 |
| 05_critical_assessment.md | ✅ | 110 |
| 98_vocabulary.md | ✅ | — |
| 99_final_summary.md | ✅ | — |
| **合计** | **8 个分析文件** | |

## 章节与元素覆盖

| 论文章节 | 主题 | 自身分章 | 状态 |
|---|---|---|---|
| §1 | Introduction | 01_introduction | ✅ |
| §2 | The energy spectrum | 02_energy_spectrum | ✅ |
| §3 | Alfvén waves upstream | 03_alfven_waves | ✅ |
| §4 | Application to SNR | 04_application_snr | ✅ |
| — | 综合批判（跨章节） | 05_critical_assessment | ✅ |

## 图表覆盖

| 元素 | 数量 | 状态 |
|---|---|---|
| 图（Figure） | 1（Figure 1：平行激波几何） | ✅ 在 02_energy_spectrum.md "§2.8 图 1 详细解读" |
| 表（Table） | 0（本文无独立表） | ✅ 无 |
| 公式（Equation） | 23 个（编号 1-23，部分无编号） | ✅ 全部提及，关键公式（1-11、20、23）独立列项 |
| 参考文献 | 论文引用了 Wentzel 1974、Jokipii 1966、Fisk 1971、Formisano 1974、Greenstadt 1975、Skilling 1975、Kulsrud & Cesarksy 1971、Chin & Wentzel 1972、Boyd & Sanderson 1969 等 | ✅ 全部在分章正文中出现 |

## 关键公式覆盖清单

| 公式 | 含义 | 出处分章 |
|---|---|---|
| (1) | 扩散-对流方程 | 02_energy_spectrum.md |
| (2) | 稳态解 | 02_energy_spectrum.md |
| (3) | 逃逸概率 $\eta = 4u_2/v$ | 02_energy_spectrum.md |
| (4) | 单次穿越能量增长 | 02_energy_spectrum.md |
| (5)-(7) | 对数能量增长 | 02_energy_spectrum.md |
| (8) | 循环 $l$ 次的概率 | 02_energy_spectrum.md |
| (9) | 幂律谱 $N(E) \propto E^{-\mu}$ | 02_energy_spectrum.md |
| (10) | 谱指数 $\mu = (2u_2+u_1)/(u_1-u_2)$ | 02_energy_spectrum.md |
| (11) | 含 Alfvén 波速修正 | 02_energy_spectrum.md |
| (13) | 粒子扩散方程 | 03_alfven_waves.md |
| (14) | 扩散系数 $D(x)$ | 03_alfven_waves.md |
| (15) | 波演化方程 | 03_alfven_waves.md |
| (20) | 特征长度 $x_0 \propto E^{1.5}$ | 03_alfven_waves.md |
| (23) | 临界能量 $E_{\rm crit} \sim 3.5$ TeV | 03_alfven_waves.md |

## 数值/事实摘录

- **谱指数**：$\mu = 2$（强激波 test-particle）→ $\mu = 2.5$（含波速修正）
- **临界能量**：$E_{\rm crit} \sim 3.5 \times 10^{12}$ eV（典型年轻 SNR）
- **SNR Cas A 加速能力**：$f(0,p) - f_0(p) \geq 10^4 f_{\rm gal}(p)$
- **动力学参数**：激波速度 $v_s \sim 10^8$ cm/s；$n_H \sim 1$ cm$^{-3}$；$B \sim 10^{-5}$ G；SNR Cas A 年龄 ≈ 330 年

## 内容质量评估

| 维度 | 评价 |
|---|---|
| **物理覆盖** | ✅ 核心机制（test-particle 极限 DSA）完整 |
| **数学严谨性** | ✅ 11 个方程推导链完整 |
| **观测对接** | ✅ Cas A 同步辐射 + $10^{4}$ 因子不等式 |
| **历史定位** | ✅ 与 B&O 1978、B&E 1987、Blasi 2013、Gabici 2019 关联 |
| **批判性** | ✅ 列出 5 个明确局限（test-particle、平行激波、注入问题、$E_{\rm crit}$ 依赖、膝部困境） |

## 已知不足

- **PDF 文本层为空白**（NASA ADS 扫描版），精读基于 PDF 视觉读取（10 页）+ 已知物理推导交叉验证
- **Part I 限制**：本文是系列三篇之 Part I，II（pp.443–455）和 III（在同卷）涉及非线效应和斜激波论述

## 验收通过

- ✅ 三件套（00/98/99）齐全
- ✅ 正文分章 4 文件 + 综合批判 1 文件（共 5 个内容文件）
- ✅ 全部公式、图、文献引用均覆盖
- ✅ 批判性分析（每个分章独立 + 跨章节综合）

