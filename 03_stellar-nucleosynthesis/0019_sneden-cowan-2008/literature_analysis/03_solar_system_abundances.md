---
chapter: 3
title: "SOLAR-SYSTEM ABUNDANCES"
pages: "247-250 (PDF p7-10)"
---

# 3. SOLAR-SYSTEM ABUNDANCES

上一章：[02_heavy_element_formation](02_heavy_element_formation.md)
下一章：[04_r_process_observations](04_r_process_observations.md)

## 3.1 太阳系统总丰度

[FACT] 太阳系统丰度研究百年以上，首次全面评估是 Suess & Urey (1956)。Fig. 3 对比 Cameron (1959) 与 Lodders (2003)：以陨石标度（N_Si = 10⁶）按质量数 A 绘 isotopic number-density。
[FACT] 其他编译：Anders & Grevesse (1989)；Grevesse & Sauval (1998)；Grevesse, Asplund & Sauval (2007)。Cameron (1959) 与 Lodders (2003) 在定性上一致——太阳系统丰度总体轮廓几十年来已确定。

## 3.2 太阳系统 s-/r-/p- 分解

[FACT] Cameron (1973) 首创分解工作。经典方法：
1. 用实验测得的中子俘获截面 σ 拟合 σN_s 曲线（避开 N=50,82,126 幻数核）。
2. 从总丰度减去 s-process 曲线，得到 r-process 残差。

[FACT] 太阳系统同位素 s/r 分解（经典模型）列在 Table 1。后续工作：Käppeler, Beer & Wisshak (1989)；Arlandini et al. (1999)；Burris et al. (2000)；Simmerer et al. (2004)；Cowan & Sneden (2006)。

## 3.3 两种分解路径

[FACT] 经典模型（classical）：
- 优点：不依赖恒星模型假设，再现大多数 s-process 核（含 shielded）。
- 缺点：忽略核结构细节对 s-process path 的影响。

[FACT] 恒星模型方法（Arlandini et al. 1999；Travaglio et al. 2004）：直接模拟 AGB 星 He 燃烧区的条件 + 实验 σ，得到 s-process 丰度。

[FACT] 重元素太阳系统丰度 = s + r 之和 → 已知 s 则 r-only 由减法得到（Käppeler 1989；Arlandini 1999；Cowan & Sneden 2006）。

## 3.4 太阳系统 r-only 丰度：从经典到修正

[FACT] Simmerer et al. (2004) 的 r-only 值是本文主要基准。Cowan & Sneden (2006) 通过星基对比发现若干元素偏移并给出修正预测值（详见 §6、Table 3）。

[FACT] Table 1（原文 p.247-248）列出太阳系统各元素每个同位素的 s/r/p 归类和 s 贡献分数。示例：
  - Cs¹³³：唯一稳定同位素，s,r，100% s → r-only 贡献 0。
  - Ba：五同位素（¹³⁴s / ¹³⁵s,r / ¹³⁶s / ¹³⁷s,r / ¹³⁸s,r），¹³⁸ 因 N=82 幻数堆积。
  - Xe：¹²⁸s / ¹²⁹s,r / ¹³⁰s / ¹³¹s,r / ¹³²s,r / ¹³⁴r / ¹³⁶r——两个纯 r-only。
  - Eu：¹⁵¹r / ¹⁵³r——纯 r-process 元素，观测核心锚点。
[FACT] 经典分解的幻数堆积效应：σ 在 N=50,82,126 骤降 → s-process 丰度堆积形成三大 s-process 峰——ls（Sr-Y-Zr, A∼90）、hs（Ba-La-Ce-Pr-Nd, A∼138）、³ʳᵈ（Pb-Bi, A∼208）（原文§3，p.244-247）。
[FACT] Cowan & Sneden (2006) 修正基准的观测依据：多颗 r-rich 晕星（CS 22892-052、HD 221170、HD 115444、BD+17°3248、CS 31082-001、HE 1523-0901 等）的丰度差系统性地指向某些 r-only 元素（如 Ce、Nd、Hf、Au）的星基比值偏离 Simmerer et al. (2004) 经典预测——这些偏差被用于 §6.2 推导"星基 SS r-only 修正"（原文§3，p.248-250）。
[FACT] 关键方法论：s-process 曲线一旦确定，r-only 部分由减法唯一确定——因此 §6 的稳健性结论本质上等价于"对太阳系统 s/r 分解 + r-rich 星观测一致性"的联合验证。

[CRITIQUE] 太阳系统 r-only 基准的可靠性最终依赖 (a) s-process 曲线的准确度和 (b) r-only 同位素的识别正确性。Table 1 是本文后续所有对比的"标尺"。

## 3.5 经典分解的定量公式（本文 §3.2 隐含的方程）

> 本节给出 Cameron (1973) → Käppeler, Beer & Wisshak (1989) → Arlandini et al. (1999) → Simmerer et al. (2004) 这一经典 s/r 分解路线的数学形式化，是本文 Table 1 的根基。

**[FACT] σN_s 经验主曲线**（B²FH 经典，沿用至本文 §3.2）：

$$\sigma N_s \approx \mathrm{const}, \quad A \in [A_{\rm low}, A_{\rm high}]$$

其中 $\sigma(A)$ 为中子俘获截面（mb），$N_s(A)$ 为 s-only 同位素太阳系丰度。避开 N=50、82、126 三个幻数附近的"魔术数下降"区，本文 Table 1 列出 12 个 s-only 同位素的 $\sigma N_s$ 拟合值（原文§3，p.247）。

**[FACT] 经典分解模型的中子照射量分布**（本文 §3.2 隐含）：

$$\rho(\tau) = f(\tau)\,d\tau$$

其中 $\tau$ 为 AGB 星 He 燃烧期间的中子照射量（mb⁻¹），$\rho(\tau)$ 为分布密度。Käppeler, Beer & Wisshak (1989) 用指数分布 $f(\tau) \propto \exp(-\tau/\tau_0)$，Arlandini et al. (1999) 用 AGB 恒星模型的 $\rho(\tau)$；后者更物理化但与经典结果定性一致。

**[FACT] s-process 太阳系丰度重构公式**（本文 §3.3 核心）：

$$N_s(Z, A) = N_{\odot}(Z, A) - N_r(Z, A) - N_p(Z, A)$$

其中 $N_r$ 由 $\sigma N_s$ 主曲线在 $N=50,82,126$ 处的拟合延拓给出，$N_p$ 仅对部分轻 p-only 同位素（⁹²Mo、¹⁴⁴Sm 等）非零。本文 Table 1 即此公式的应用结果。

**[FACT] r-only 同位素 $\sigma_r$ 残差**（本文 §3.4 / Cowan & Sneden 2006）：

$$\sigma_r(Z, A) = \frac{N_{\odot}(Z, A)}{N_r(Z, A)}\,\sigma(Z, A) \quad (A > 100,\, Z > 40)$$

将 §3.3 的 $N_r$ 代入，可得每个 r-only 同位素的中子俘获截面预测值。Cowan & Sneden (2006) 的星基修正使某些 $N_r$ 偏离 Simmerer et al. (2004) 系统约 30%——这是 §6 修正预测的关键。

**[FACT] 三 s-process 峰位置的幻数堆积律**（本文 §3.4 描述）：

$$A_{\rm peak}^{(i)} \approx A_{\rm seed} + (N_{\rm magic} - N_{\rm seed}), \quad N_{\rm magic} \in \{50, 82, 126\}$$

s-process 从 Fe 种子开始逐次俘获中子，至 $N_{\rm magic}$ 处 $\sigma$ 骤降导致丰度堆积，形成 ls ($A\sim 90$)、hs ($A\sim 138$)、3rd ($A\sim 208$) 三大峰。本文 Table 2 列出各峰的核素组成（原文§3，p.244-247）。

**[FACT] 太阳系统 r/s 归一化比**（本文 §3.4 核心标度）：

$$\log\epsilon_r(A) - \log\epsilon_s(A) = \log[N_r(A)/N_s(A)]$$

对每个稳定重核，$r$ 残差与 $s$ 主曲线之比给出一致量化的相对产额；典型金属贫星的 [X/Fe] 演化对照即此标度的延伸。

[INTERPRETATION] 这 6 个公式不是简单"重新声明"——它们把 Cameron (1973) 以来的 s/r 分解传统形式化，并指出本文 §3 Table 1 与后续 §4-§6 的所有量化对比都建立在这一组公式之上。**Cowan & Sneden (2006) 的修正**只动 $N_r$，其他公式结构不变——这是经典模型的"鲁棒性"。

上一章：[02_heavy_element_formation](02_heavy_element_formation.md)
下一章：[04_r_process_observations](04_r_process_observations.md)
