---
# 99. Final Summary — 最终总结

## 99.1 一句话总结

Génolini et al. (2021) 基于 AMS-02 最新二级/一级比率数据和晕大小约束，用系统统计方法（"pinching"）定义了新一代银河系 CR 传播 min/med/max 基准——反质子背景不确定性缩小 6 倍、正电子缩小 2 倍，直接服务于暗物质间接探测。

## 99.2 科学问题

**核心问题**：暗物质间接探测（反物质 CR 搜寻）需要 astrophysical background 的系统性不确定性边界。旧版 min/med/max（Cirelli 2008）已因 AMS-02 精密数据而过时。

## 99.3 核心方法

**三模型框架**：

1. 基于 AMS-02 Li/C、Be/C、B/C 联合分析的后验分布
2. 从协方差矩阵抽取 $10^5$ 个相关 SLIM 传播参数
3. "Pinching"：沿 $(\log_{10}L, \ell)$ 同时取上下分位数 → MIN/MED/MAX
4. 三种传播方案：SLIM（5 参数）、BIG（7 参数）、QUAINT（9 参数）

## 99.4 最重要结果

| 结果 | 值 | 意义 |
|---|---|---|
| 反质子不确定性缩小 | $\sim 6$ 倍 | DM 反质子约束大幅收紧 |
| 正电子不确定性缩小 | $\sim 2$ 倍 | 正电子 excess 解读更清晰 |
| MED 晕高 $L$ | 4.0 kpc | 与放射性同位素约束一致 |
| MED 扩散谱指数 | $\delta = 0.46$ | 与 AMS-02 B/C 拟合 |
| MED 低刚度断裂 | $R_l = 5$ GV | 反映扩散系数变平 |
| 拟合公式 | 附录 E | DM 搜寻可直接使用 |

## 99.5 核心创新

1. **系统统计方法**：从 $10^5$ 后验样本中"pinching"选择——比旧版人工选择更客观
2. **高低刚度断裂**：新模型包含扩散系数的两个断裂（$\sim 5$ GV 和 $\sim 10^4$ GV）
3. **晕大小约束**：显式纳入放射性同位素（$^{10}{\rm Be}$）的 $L$ 约束
4. **handy fitting formulae**：附录 E 提供解析拟合，降低 DM 搜寻的技术门槛

## 99.6 主要局限

- 唯象参数化——扩散系数断裂的物理起源未讨论
- 仅 SLIM 方案有完整统计处理（BIG/QUAINT 在附录 C 简要讨论）
- 未考虑 CR 驱动银河风
- 未考虑源附近禁闭效应

## 99.7 我应该记住什么

1. **min/med/max = 暗物质搜寻的 astrophysical background 边界**
2. **"pinching" = 沿 $(\log_{10}L, \ell)$ 方向同时取分位数**——本文方法论核心
3. **$L/K \sim$ 常数（B/C 强约束）**——$L$ 和 $K_0$ 必须同步变化
4. **反质子不确定性缩小 6 倍**——最显著的改进
5. **MED 参数**：$L = 4$ kpc, $\delta = 0.46$, $R_l = 5$ GV
6. **本文是方法论 + 数据更新**——不是新物理（与 Amato-Blasi 2018 的物理论证互补）
7. **与 Amato-Blasi 2018 的关系**：Amato-Blasi 论证 $D(p)$ 断裂的物理起源；本文用唯象模型拟合数据——两者从不同角度回答"传播参数是什么"

## 99.8 与相关工作的关系

| 论文 | 关系 |
|---|---|
| Cirelli et al. 2008 | 旧版 min/med/max（本文的替代）|
| Wechsler et al. 2020 | AMS-02 B/C 分析的原始来源 |
| Boudaud et al. 2014 | 传播参数不确定性对 DM 约束的影响 |
| Blasi et al. 2013 | SLIM/BIG/QUAINT 传播方案的原始定义 |
| Amato-Blasi 2018 | 非线性传播理论（本文的唯象参数化对应物理模型）|
| Weinrich et al. 2020 | 晕高 $L$ 的贝叶斯约束（同作者）|
| Strong & Moskalenko 2007 | GALPROP 旧范式 |

## 99.9 数值速查表

| 量 | 值 | 备注 |
|---|---|---|
| MED 晕高 $L$ | 4.0 kpc | |
| MIN 晕高 $L$ | 1.0 kpc | |
| MAX 晕高 $L$ | 8.0 kpc | |
| MED $K_0$ | $10^{27.97}$ cm²/s | |
| MED $\delta$ | 0.46 | |
| MED $R_l$ | 5.0 GV | |
| MED $\ell$（低刚度指数）| 1.50 | |
| MED $V_A$（Alfvén 速度）| 25 km/s | |
| 暗晕尺度半径 $r_s$ | $\sim 20$ kpc | NFW |
| 银心距离 $R_\odot$ | 8.2 kpc | |
| 反质子不确定性缩小 | $\sim 6$ 倍 | vs Cirelli 2008 |
| 正电子不确定性缩小 | $\sim 2$ 倍 | vs Cirelli 2008 |

## 99.10 引用格式

> Génolini, Y. et al. 2021, Physical Review D, 104, 083005; arXiv:2103.04108

## 99.11 值得进一步阅读

1. **Wechsler et al. 2020, PRD, 101, 043017** — AMS-02 B/C 分析的原始来源
2. **Blasi et al. 2013, JCAP, 09, 025** — SLIM/BIG/QUAINT 传播方案的定义
3. **Cirelli et al. 2008, JCAP, 10, 018** — 旧版 min/med/max
4. **Amato & Blasi 2018** — 非线性传播的物理基础（与本文唯象模型互补）
5. **Weinrich et al. 2020, PRL, 125, 131102** — 晕高 $L$ 的贝叶斯约束