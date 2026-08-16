---
title: "§6 Statistical Power"
paper: "ams02-2015"
section: 6
nav_prev: "05_background_and_systematics.md"
nav_next: "07_comparison_with_previous_experiments.md"
---

上一章：`05_background_and_systematics.md`
下一章：`07_comparison_with_previous_experiments.md` — 与前代实验对比

# §6 Statistical Power — 统计能力与拟合质量

## 6.1 本节核心内容

AMS-02 拥有宇宙线质子谱**史无前例的统计量**：$3.0\times10^{8}$ 质子事例，72 bin 覆盖 1 GV – 1.8 TV。这一规模使本文首次能给出**逐刚性**的谱指数 $\gamma(R)$（原文 p.7，Fig.4(b)），并以**99.9% C.L.**排除单幂律。双幂律 Eq.(3) 拟合 $\chi^2$/d.o.f. = 25/26，证实模型与数据吻合极好。

## 6.2 原文内容

- **事件数**（原文 p.3）：
  - 有效观测 $7.96\times10^{7}$ s
  - 总宇宙线 $4.1\times10^{10}$ 事件
  - 向下 $Z=+1$：$1.1\times10^{10}$
  - 最终质子样本：**$3.0\times10^{8}$**（3 亿事件）

- **统计误差贡献**（原文 §Results，p.6）：
  - 72 bin 内统计误差远小于系统误差（多数 bin 统计 <1%）
  - 双幂律拟合 fit 误差已计入统计与**未关联的系统误差**（原文 p.6 明确）
  - **MC 统计充分**：MC 事件数充足，MC 统计不贡献误差

- **拟合优度**（原文 p.6）：
  - $\chi^2$/d.o.f. = 25/26
  - 拟合范围：45 GV – 1.8 TV（共 26 d.o.f.）
  - 拟合参数：$C$、$\gamma$、$\Delta\gamma$、$s$、$R_0$（5 个参数）

- **单幂律排除**（原文 p.6）：
  - 99.9% C.L.（$R > 45$ GV）
  - 力场近似下的太阳调制也不能拟合 99.9% C.L.

- **unfolding 稳健性**（原文 p.3–p.4）：
  - 采用**两种独立 unfolding 方法**（迭代法 [19]、forward spline [20]）
  - 两种方法差异 <0.5%
  - bin 宽度 ±2、±4 倍变化，结果仍在系统误差内

## 6.3 关键公式

**统计 vs 系统误差合成**（原文 p.6 明确"sum in quadrature of statistical and systematic errors"）：

$$
\sigma_{\text{total}}^2 = \sigma_{\text{stat}}^2 + \sigma_{\text{sys}}^2
$$

**拟合 $\chi^2$ 定义**（标准，原文未显式给出但隐含）：

$$
\chi^2 = \sum_{i=1}^{N_{\text{bin}}} \frac{(\Phi_i^{\text{data}} - \Phi_i^{\text{model}})^2}{\sigma_i^2}
$$

对 26 d.o.f. 得到 25，$\chi^2$/d.o.f. = 0.96 —— 表明模型描述良好，无显著结构偏离。

## 6.4 关键参数

| 项目 | 数值 |
|---|---|
| 质子事例总数 | $3.0\times10^{8}$ |
| 观测时间 | $7.96\times10^{7}$ s（30 个月） |
| 有效 bin 数 | 72 |
| 单 bin 统计误差（中位） | <1%（多数 bin） |
| 拟合 $\chi^2$/d.o.f. | 25/26 |
| 单幂律排除置信度 | 99.9% C.L. |
| 拟合范围 | 45 GV – 1.8 TV |
| 拟合参数数 | 5（$C, \gamma, \Delta\gamma, s, R_0$） |
| 拟合 d.o.f. | 26 |

## 6.5 图表分析

**双幂律拟合 vs $\Delta\gamma=0$ 对照**（原文 Fig.4(a)）：
- 数据 × $\tilde{R}^{2.7}$
- **实线**（Eq.(3) 完整）：$\chi^2$/d.o.f. = 25/26，拟合极好
- **虚线**（$\Delta\gamma = 0$）：在 300–2000 GV 显著低于数据点
- **关键观察**：即使单幂律的 $\gamma$ 被重新优化，也无法拟合——**$\Delta\gamma \ne 0$ 是必要的**

## 6.6 作者的逻辑

1. 大事件数 → 高统计精度
2. 两种独立 unfolding → 交叉验证
3. 双幂律拟合优度良好 → 模型描述可信
4. 单幂律 99.9% C.L. 排除 → 新物理必要性

## 6.7 我的理解

AMS-02 的统计能力使本文**首次**能够：
- 把 $\gamma$ 视为 $R$ 的函数（而非单个常数）
- 在**单一实验**内排除单幂律假设（此前需多实验拼接）
- 给出**系统误差主导**的逐 bin 流强——这在宇宙线实验中是历史性的

> [FACT] 原文 p.6 明确："The Monte Carlo event samples have sufficient statistics such that they do not contribute to the errors." —— **MC 统计不再成为瓶颈**，这在宇宙线 MC 研究中不常见。

## 6.8 潜在问题与值得关注的地方

- [FACT] 拟合 d.o.f. = 26（45 GV – 1.8 TV，26 bin），$\chi^2 = 25$——非常接近 1，但**不保证**模型的正确性（可能偶然抵消）。
- [CRITIQUE] 拟合参数间的**相关矩阵**未在本文中报告——$\gamma$、$\Delta\gamma$、$R_0$ 三者之间必然强相关（特别是 $R_0$ 与 $\gamma$ 的 trade-off）。
- [CRITIQUE] 45 GV 以下的**太阳调制**用 force-field approximation 处理，$\phi = 0.50$–0.62 GV 由外部观测给定——这引入模型依赖，非 AMS 数据自洽。
- [FACT] 两种 unfolding 方法差异 <0.5%（原文 p.3）——这一**方法学稳健性**证明本文结论不依赖具体 unfolding 选择。
- [CRITIQUE] bin 宽度 ±2、±4 倍变化在系统误差内——但这一测试仅改变 bin 定义，未测试**模型依赖**（如改用分段幂律或 spline）。
