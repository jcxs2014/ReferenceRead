---
title: "§98 Vocabulary"
paper: "lhaaso-2021"
section: 98
nav_prev: "97_quality_check.md"
nav_next: "99_final_summary.md"
---
上一章：`97_quality_check.md` — §97
下一章：`99_final_summary.md` — Vocabulary

# §98. Vocabulary — 术语表

>

---


## A. 学术逻辑词（≥15 条）

| 单词 | 词性 | 逻辑功能 | 中文 | 原文例句 | 逻辑说明 |
|---|---|---|---|---|---|
| here | adv. | 强调 | 此处 | "Here we report the detection..." | 指代本论文工作 |
| thus | adv. | 因果 | 因此 | "We thus conclude..." | 推导结论 |
| whereas | conj. | 对比 | 而 | "whereas the previous measurements..." | 强调差异 |
| owing to | prep. | 因果 | 由于 | "owing to the large collection area..." | 物理归因 |
| in particular | adv. | 举例 | 特别是 | "in particular at energies above 100 TeV..." | 聚焦 |
| most importantly | adv. | 递进 | 最重要 | "Most importantly, the detection..." | 强调核心结果 |
| therefore | adv. | 因果 | 因此 | "therefore the existence of..." | 推出物理结论 |
| consistent with | adj. | 一致 | 与...一致 | "consistent with the expected..." | 比对确认 |
| regardless of | prep. | 排除 | 不论 | "regardless of the exact composition..." | 模型无关 |
| suggests that | v. | 暗示 | 表明 | "This suggests that..." | 弱推断 |
| confirms | v. | 确认 | 证实 | "This confirms the existence of..." | 强确认 |
| in total | adv. | 总结 | 共计 | "in total 12 sources..." | 汇总数字 |
| among them | adv. | 列举 | 其中 | "among them, the brightest..." | 选取代表 |
| with significance of | n. | 显著性 | 显著度 | "with significance of >7σ" | 统计陈述 |
| of which | pron. | 限定 | 其中 | "of which 1.4 PeV is..." | 限定选取 |

## B. 领域术语

### 探测器与仪器

| 术语 | 全称/中文 | 说明 |
|---|---|---|
| LHAASO | Large High Altitude Air Shower Observatory / 高海拔宇宙线观测站 | 位于稻城海子山（海拔 4,410 m），由 KM2A+WCDA+WFCTA 三套阵列组成 |
| KM2A | Kilometer Square Array / 平方公里阵列 | 表面宇宙线阵列，1 km$^{2}$；含 ED 闪烁体 + MD 水中切伦科夫缪子 veto |
| ED | Electromagnetic detector / 电磁探测器 | 5,195 个塑料闪烁体计数器（15 m 网格） |
| MD | Muon detector / 缪子探测器 | 1,188 个地下水中切伦科夫探测器（30 m 网格，2.5 m 埋深） |
| WCDA | Water Cherenkov Detector Array / 水中切伦科夫探测器阵列 | 78,000 m$^{2}$、4.5 m 水深；能量桥接 Fermi-LAT 与 KM2A |
| WFCTA | Wide Field-of-view Cherenkov Telescope Array / 广角切伦科夫望远镜阵列 | 18 台 16°×16° FoV 望远镜，50 TeV–100 PeV |
| PSF | Point Spread Function / 点扩展函数 | 源角分辨率度量，本文 68% containment = 0.45°–0.62° |
| N_μ/N_e | 缪子数/电磁粒子数比 | KM2A 的 γ/CR 判别量，cut <1/230 |

### 物理量

| 术语 | 说明 |
|---|---|
| PeVatron | PeV 能量加速器（10$^{15}$ eV） |
| super-PeVatron | 加速至 >几 PeV 的源，膝区以上 CR 的可能来源 |
| CU | Crab Unit，蟹状星云在 100 TeV 的流量单位 = 6.1×10$^{-17}$ photons TeV$^{-1}$ cm$^{-2}$ s$^{-1}$ |
| SED | Spectral Energy Distribution / 谱能量分布 |
| log-parabola | 对数抛物线谱 dN/dE ∝ E$^{-\Gamma(E)}$，Γ(E)=a+b·logE |
| E_max | 最高能光子能量（表 1 中每个源） |
| E$^{2}$dN/dE | 能量通量（积分灵敏度指标） |
| γ-γ absorption | γ-γ 对产生吸收，>100 TeV 主导于 CMB，<100 TeV 主导于 ISRF |
| $\pi^{0}$ decay | 中性 π 介子衰变 γ，强子加速的"smoking gun" |
| Inverse Compton (IC) | 逆康普顿散射，轻子机制 UHE γ 的主要通道 |
| PWN | Pulsar Wind Nebula / 脉冲星风星云 |
| SNR | Supernova Remnant / 超新星遗迹 |
| DSA | Diffusive Shock Acceleration / 扩散激波加速（Bell 1978） |
| Hillas criterion | 加速极限判据 E_max ≲ ZeBLβ |
| knee | 银河宇宙线谱"膝区"（~3×10$^{15}$ eV） |
| first/second knee | 初级/次级膝（CR 能谱拐点） |

### 方法学

| 术语 | 说明 |
|---|---|
| background-free | background 抑制至远低于 1 事件/观测时间 |
| direct integration method | 背景估计方法（Fleysher 2003; Bartoli 2013） |
| likelihood ratio test | 似然比检验（源+背景 vs. 背景-only 模型） |
| forward unfolding | 向前展开（用探测器响应矩阵重构真实谱） |
| AIC | Akaike Information Criterion / 模型选择判据 |
| TS | Test Statistic，√TS = σ |
| MC | Monte Carlo 模拟 |
| 4FGL | Fermi LAT 第八年源目录 |
| Pass 8 | Fermi LAT 数据处理版本 |

### 关键数值（供速查）

| 量 | 值 |
|---|---|
| 海拔 | 4,410 m |
| KM2A ED 网格 | 15 m |
| KM2A MD 网格 | 30 m |
| KM2A 面积 | 1 km$^{2}$（+0.3 km$^{2}$ skirt） |
| ED 数 / MD 数 | 5,195 / 1,188 |
| MD 埋深 | 2.5 m（~20 辐射长度） |
| 有效运行时间 | 308.33 天（自 2019-12-27） |
| γ-like 事件数 | ~84,000 |
| 光子总数 >100 TeV | >530 |
| 最高能光子 | 1.4 PeV（J2032+4102） |
| 源数量 | 12 |
| 最低显著性 | 7σ |
| 角分辨率 >100 TeV | 15–20 角分 |
| 能量分辨率 >100 TeV | <14% |
| CR 抑制 @1 PeV | 10$^{-5}$ |
| 积分灵敏度 | 10$^{-14}$ erg cm$^{-2}$ s$^{-1}$ |

## C. 长难句分析

**例句 1**："The cosmic-ray spectrum observed at Earth carries information on the nature of the sources, the mechanisms of acceleration, and the transport through the interstellar medium, but the disentangling of these factors has been hampered by the limited statistics at the highest energies."

| 句子成分 | 内容 | 语法功能 |
|---|---|---|
| 主句 | The CR spectrum carries information | 主语+谓语 |
| on 引导 | on the nature/mechanisms/transport | 并列介宾短语 |
| but 转折 | the disentangling has been hampered | 转折+被动 |
| by 引导 | by the limited statistics | 限制原因 |
