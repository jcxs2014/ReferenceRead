---
# 98. Vocabulary — 学术词汇与术语
> 上一章：[[01_cosmic-ray-propagation/0003_weinrich-2020/literature_analysis/97_quality_check.md|97_quality_check]]
> 下一章：[[01_cosmic-ray-propagation/0003_weinrich-2020/literature_analysis/99_final_summary.md|99_final_summary]]

## A. 学术逻辑词

| 单词 | 词性 | 逻辑功能 | 中文 | 原文例句 |
|------|------|----------|------|----------|
| however | adv. | 转折 | 然而 | "However, for 10Be, Be/B, Al/Mg) in which the CR clock appears both..." |
| therefore | adv. | 因果 | 因此 | "Therefore, we stress that uncertainties were derived on log(L)" |
| notably | adv. | 强调 | 尤其 | "notably, this analysis uses the same propagation model" |
| in particular | adv. | 强调 | 尤其 | "in particular, the halo size of the Galaxy is set to be a hard boundary" |
| consequently | adv. | 因果 | 因此 | "consequently, this quantity gives a direct constraint on L" |
| whereas | conj. | 对比 | 而 | "whereas the stable secondary species have a much shorter lifetime" |
| namely | prep. | 解释 | 即 | "namely from Li/C and B/C data only" |
| hence | adv. | 因果 | 因此 | "hence covering an energy range in which 10Be goes" |
| given | prep. | 条件 | 鉴于 | "Given the poor sensitivity of B/C to L" |
| despite | prep. | 让步 | 尽管 | "despite potential issues on sub-galactic scales" |
| accordingly | adv. | 因果 | 相应地 | "accordingly, the uncertainties on L" |

## B. 领域术语

| 术语 | 中文 | 释义 | 首次出现章节 |
|------|------|------|-------------|
| galactic halo size | 银河晕大小 | CR 扩散区域的垂直半高 $L$ | §1 |
| CR clock | 宇宙线时钟 | 放射性同位素的衰变作为传播时间的时钟 | §3 |
| radioactive isotope | 放射性同位素 | 半衰期 $< 10^7$ yr 的不稳定核素（如 $^{10}{\rm Be}$）| §3 |
| Boron-10 ($^{10}{\rm Be}$) | 硼-10 | 半衰期 1.387 Myr 的放射性同位素——CR 时钟的标准 | §3 |
| B/C ratio | 硼/碳比率 | 最常用的二级/一级比率——传播参数的强约束 | §1 |
| Be/B ratio | 铍/硼比率 | $^{10}{\rm Be}$ 衰变贡献的二级比率——对 $L$ 敏感 | §3 |
| $^{10}{\rm Be}$/$^{9}{\rm Be}$ ratio | 硼-10/硼-9 比率 | 直接测量 $^{10}{\rm Be}$ 丰度的同位素比率 | §3 |
| $^{10}{\rm Be}$/Be ratio | 硼-10/硼比率 | 直接测量 $^{10}{\rm Be}$ 丰度的同位素比率 | §3 |
| $K_0/L$ degeneracy | 扩散系数/晕高简并 | B/C 只约束比值 $K_0/L$，对两者单独不敏感 | §1 |
| BIG configuration | BIG 配置 | 7 参数传播方案（含对流+再加速+断裂）| §2 |
| SLIM configuration | SLIM 配置 | 5 参数简化方案（$V_c=V_A=0$）| §2 |
| QUAINT configuration | QUAINT 配置 | 6 参数方案（含对流+再加速+高刚度断裂）| §2 |
| force-field approximation | 力场近似 | Solar modulation 的一维近似处理 | §2 |
| minos algorithm | minos 算法 | IMinuit 中给出非对称误差的算法 | §2 |
| nuisance parameters | 烦扰参数 | 交叉截面/Solar modulation 等不关心的参数 | §2 |
| AMS-02 | Alpha Magnetic Spectrometer | 国际空间站精密宇宙线探测器 | §1 |
| PAMELA | | 卫星宇宙线探测器 | §3 |
| ACE-CRIS | | ACE 卫星的宇宙线探测仪器 | §3 |
| GALPROP | | 宇宙线传播数值代码 | §1 |
| isotopic ratio | 同位素比率 | 放射性同位素/稳定同位素的比值 | §3 |
| confidence level | 置信水平 | 参数约束的统计置信度 | §3 |
| cross-section uncertainty | 交叉截面不确定性 | 核碎裂反应截面的实验误差 | §3 |

## C. 长难句摘录

### C1. §1（$^{10}{\rm Be}$ 时钟的核心句）

> "Radioactive secondary species whose lifetime is shorter than the propagation time scale can break the degeneracy between the diffusion coefficient normalisation and the halo size of the Galaxy."

**主干**：Radioactive species + can break + the degeneracy + between + $K_{0}$ and L
**修饰**：whose lifetime...（定语从句），the propagation time scale（比较对象），between...and（结构）
**翻译**：寿命短于传播时间尺度的放射性二级同位素可以打破扩散系数归一化和银河晕大小之间的简并。
**逻辑功能**：本文方法论的核心洞察——用 $^{10}{\rm Be}$ 衰变打破 $K_0/L$ 简并。

### C2. §3（晕大小的直接约束句）

> "This quantity gives a direct constraint on L - we do not show results for the transport parameters as they are available and were abundantly discussed in the companion paper."

**主干**：This quantity + gives + a direct constraint + on L
**修饰**：direct（强调），companion paper（关联引用）
**翻译**：这一量给出了对 $L$ 的直接约束——我们不展示传输参数的结果，因为它们已经在合作论文中充分讨论。
**逻辑功能**：强调本文聚焦 $L$——与传播参数分析的分工。