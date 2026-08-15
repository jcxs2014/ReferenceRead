# 97. Quality Check — Completeness 自检
> 上一章：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/05_critical_assessment.md|05_critical_assessment]]
> 下一章：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/98_vocabulary.md|98_vocabulary]]

## 文献信息

| 字段 | 内容 |
|---|---|
| 标题 | Particle Acceleration by Astrophysical Shocks |
| 作者 | R. D. Blandford (Caltech), J. P. Ostriker (Princeton) |
| 期刊 | The Astrophysical Journal, 221, L29–L32 |
| 年份 | 1978 |
| DOI | — |
| arXiv | — |
| 页数 | 4 页 (L29–L32) |
| 参考文献数 | 28 篇 |

## 文件清单

| 文件 | 行数 | 状态 |
|---|---|---|
| 00_overview.md | 95 | ✓ 元信息 + 摘要 + 结构表 |
| 01_introduction.md | 112 | ✓ §4 模板（8 子节）|
| 02_strong_shock_acceleration.md | 188 | ✓ §4 模板（8 子节）+ 完整公式推导 |
| 03_cosmic_ray_application.md | 135 | ✓ §4 模板（8 子节）|
| 04_extragalactic_radio_sources.md | 118 | ✓ §4 模板（8 子节）|
| 05_critical_assessment.md | 100 | ✓ 跨章节综合批判 |
| 97_quality_check.md | — | ✓ 本文 |
| 98_vocabulary.md | 71 | ✓ A 逻辑词 + B 术语 + C 长难句 |
| 99_final_summary.md | 23 | ✓ 核心结论 + 数值速查 |
| **合计** | **~842** | — |

## 公式覆盖（对照 fulltext）

| 编号 | 公式 | 所在分章 | 状态 |
|---|---|---|---|
| 1 | $v_A = 13(B/10^{-6})\sqrt{n}^{-1}$ km/s | 01_introduction | ✓ |
| 2 | $\langle \Delta(p^2)/p^2 \rangle = (1/3)(1+2r)r^{-2/3}-1$ | 01_introduction | ✓ |
| 3 | $r = u_-/u_+ = \tan\theta_+/\tan\theta_-$ | 02_strong_shock | ✓ |
| 4 | 长度尺度排序 $\delta \ll r_L \ll L \ll H$ | 02_strong_shock | ✓ |
| 5 | 扩散-对流方程（公式 1a）| 02_strong_shock | ✓ |
| 6 | 沿磁场扩散系数 $D_\parallel$ | 02_strong_shock | ✓ |
| 7 | 能量通量连续性（公式 1c）| 02_strong_shock | ✓ |
| 8 | 上游指数衰减解 | 02_strong_shock | ✓ |
| 9 | $df_+/d\ln p$ 关系 | 02_strong_shock | ✓ |
| 10 | **幂律解 $f_+(p) \propto p^{-q}$** | 02_strong_shock | ✓ |
| 11 | **$q = 3r/(r-1)$** | 02_strong_shock | ✓ |
| 12 | 平均能量增益 $3/(5-2r)$（非相对论）| 02_strong_shock | ✓ |
| 13 | 平均能量增益 $3/(4-r)$（超相对论）| 02_strong_shock | ✓ |
| 14 | 瞬态建立时间 $t_{\rm est}$ | 02_strong_shock | ✓ |
| 15 | 自激发增长率 $\gamma_{\rm growth}$ | 03_cosmic_ray | ✓ |
| 16 | 能量注入 $E_{\rm injected} \approx 10^{50}$ erg | 03_cosmic_ray | ✓ |
| 17 | 高能截断 $r_L \approx R_{\rm SNR}$ | 03_cosmic_ray | ✓ |
| 18 | 同步冷却时间 $t_{\rm synch} \propto 1/(\gamma B^2)$ | 04_extragalactic | ✓ |
| 19 | $E_{\rm max} \approx 10$ GeV（Cygnus A）| 04_extragalactic | ✓ |
| 20 | $s = 4.5 \Rightarrow r = 3$ | 03_cosmic_ray | ✓ |

**公式覆盖**：20/20 ✓

## 图 / 表覆盖

| 类型 | 论文中数量 | 分析数量 | 状态 |
|---|---|---|---|
| Figure | 0 | N/A | ✓（论文无 Figure）|
| Table | 0 | N/A | ✓（论文无 Table）|

## 数值信息检查

| 数值 | 值 | 所在分章 | 状态 |
|---|---|---|---|
| 超新星能量 | $10^{51}$ erg | 01_introduction | ✓ |
| ISM 密度 | $1 \text{ cm}^{-3}$ | 01_introduction | ✓ |
| Alfvén 速度 | $50 \text{ km s}^{-1}$ | 01_introduction | ✓ |
| CR 能量密度 | $10^{-12} \text{ erg cm}^{-3}$ | 01_introduction | ✓ |
| 冷却体积 | $10^{63.4} \text{ cm}^3$ | 01_introduction | ✓ |
| 压缩比（强激波）| $r = 4$ | 02_strong_shock | ✓ |
| 谱指数（理论）| $q = 4$ | 02_strong_shock | ✓ |
| 谱指数（观测）| $s = 4.5$ | 03_cosmic_ray | ✓ |
| 高能截断 | $10^{18}$ eV | 03_cosmic_ray | ✓ |
| 单次穿越增益 | $\sim 10^{-1}$ | 01_introduction | ✓ |
| 加速时间 | $\sim 10^6$ yr | 03_cosmic_ray | ✓ |
| 超新星率 | $10^{-18} \text{ cm}^{-3} \text{ yr}^{-1}$ | 03_cosmic_ray | ✓ |
| SNR 半径（Alfvénic 转变）| $> 100$ pc | 03_cosmic_ray | ✓ |
| 自激发适用上限 | $\sim 300$ GeV | 03_cosmic_ray | ✓ |
| Cygnus A 最大能量 | $\sim 10$ GeV | 04_extragalactic | ✓ |
| Cygnus A 磁场 | $\sim 10^{-4}$ G | 04_extragalactic | ✓ |
| Cygnus A 流速 | $3 \times 10^4$ km/s | 04_extragalactic | ✓ |

## 已知不足

1. **本文是 ApJ Letter 短文**（4 页），物理图像为主，数学处理较简略——相比 Bell 1978（MNRAS 179, 573）和 Drury 1979 的完整理论更侧重物理洞察
2. 文中多次引用 "will be described elsewhere"（Blandford, Cassé & Ostriker in prep; Blandford in prep），这些后续工作不在精读范围内
3. 公式（1a）的 OCR 转录可能存在符号误差（特别是向量算子 $\nabla$ 和扩散张量的表达）——已在正文中标注
4. §III 中 Alfvén 波自激发的处理为定性估算，未包含完整的色散关系和饱和机制
5. 98_vocabulary.md 术语表基于 OCR 文本提取，B 类术语可结合 PDF 原版进一步补充