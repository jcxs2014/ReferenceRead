---
section: "vocab"
title: "Vocabulary — 术语表"
parent: "00_overview.md"
previous: "97_quality_check.md"
next: "99_final_summary.md"
---

# 98. Vocabulary

## A. 学术逻辑词（中文→英文等价词）

| 中文 | 英文等价 | 逻辑功能 | 例句（本综述） | 说明 |
|---|---|---|---|---|
| 然而 | however / nevertheless | 转折 | "However, the reaction of the accelerated particles ... cannot in general be ignored." | 线性→非线性过渡的标志词 |
| 因此 | thus / therefore | 因果 | "Thus in the linear theory the downstream particle pressure diverges..." | 推导结论 |
| 此外 | furthermore / moreover | 递进 | "Furthermore, shocks in fluids with ratio of specific heats γ..." | 补充前提 |
| 显然 | clearly / obviously | 断言 | "it is reasonably clear that the condition..." | 强断言 |
| 尽管 | although / even though | 让步 | "although the spectrum is not a simple power law..." | 让步后仍有主结论 |
| 即 | i.e. | 定义 | "i.e. steeper than in an unmodified shock" | 展开说明 |
| 例如 | e.g. / for example | 举例 | "obvious examples are synchrotron losses..." | 例示 |
| 反之 | conversely / on the other hand | 对照 | "conversely, the flux to ∞ is..." | 反向论证 |
| 特别地 | in particular / notably | 特例 | "in particular the diffusion coefficient" | 聚焦要点 |
| 简言之 | in brief / in short | 总结 | "the central idea ... is simple and persuasive" | 收束 |
| 关键在于 | the crucial point is / the key is | 聚焦 | "the key to obtaining a power law is..." | 强调机制 |
| 尽管...仍 | ...and yet | 转折 | "basic idea's chief attraction..." | 让步式强调 |
| 换言之 | or equivalently | 重述 | 文中多次在宏观/微观视角切换时使用 | 等价格式 |
| 假设 | assuming that | 前提 | "Assuming that the accelerated particles could be treated as test particles..." | 假设性陈述 |
| 由此 | hence / thereby | 因果 | "thereby producing a power law" | 结果链 |

## B. 领域术语

| 术语/缩写 | 中文 | 释义（本文语境） | 首现章节 |
|---|---|---|---|
| DSA | Diffusive Shock Acceleration | 扩散激波加速，又称 first-order Fermi 加速 | §1 |
| Fermi acceleration | Fermi 加速 | 粒子与运动散射中心相互作用获得能量；DSA 为 first-order，湍流随机加速为 second-order | §1 |
| Power law spectrum | 幂律谱 | $f(p) \propto p^{-a}$，谱指数 $a$ 只依赖压缩比 | §2.3 |
| Compression ratio $r$ | 压缩比 | $r = U_1/U_2$，上下游流速比 | §2.3 |
| Spectral index $a$ | 谱指数 | $a = 3r/(r-1)$；强激波（$r=4$）→ $a=4$ | §2.3 |
| Transport equation | 输运方程 | 式 (2.11)：扩散-对流-绝热方程 | §2.1 |
| Diffusion coefficient $\kappa$ | 扩散系数 | 描述粒子在磁场湍流中的随机游走长度 | §2.1 |
| Test particle | 测试粒子 | 粒子对背景场无反馈的近似 | §3 |
| Scatter-free acceleration | 无散射加速 | 单次穿越激波的几何加速，动量增益有限 | §2.2 |
| Oblique shock | 斜激波 | $\theta_1 \neq 0$，磁场与激波法线有夹角 | §3.1 |
| Parallel shock | 平行激波 | $\theta_1 = 0$ | §2.2 |
| Non-linear modification | 非线性修正 | 考虑粒子反作用对激波结构和谱的影响 | §4 |
| Self-induced scattering | 自激散射 | 加速粒子自激 Alfven 波作为散射中心（Bell 1978a） | §4.1 |
| Shock structure | 激波结构 | 含宇宙线压力的扩展 Rankine–Hugoniot 条件 | §4.2 |
| Injection | 注入 | 背景等离子体粒子进入 DSA 机制的过程 | §4.4 |
| Pressure divergence | 压力发散 | $\gamma_c \to 1$ 时下游粒子压力趋于无穷 | §4.5 |
| Bohm diffusion | Bohm 扩散 | 最小扩散系数极限，$\kappa \propto p$ | §3.2, §4.3 |
| Adiabatic cooling | 绝热冷却 | 流体膨胀导致的粒子能量损失 | §2.1, §3.4 |
| Spherical shock | 球激波 | 点爆炸或星风终止激波，需奇异摄动理论处理 | §3.3 |
| Stellar-wind terminator | 星风终止激波 | 星风与星际介质相遇形成的终止激波 | §1, §3.3 |

## C. 长难句（3 例）

### C.1 幂律普遍性

**原文**："The significance of this is that if the upstream spectrum is softer than a power law spectrum with slope $a$, then the downstream spectrum has as asymptote at high momenta a power law spectrum of slope $a$ regardless of the detailed form of the incoming spectrum."

**主干**：downstream spectrum has an asymptote of slope $a$.

**修饰**：条件子句（if upstream softer than $p^{-a}$） + 让步（regardless of detailed form）

**中译**：其意义在于，如果上游谱比斜率为 $a$ 的幂律谱更软，则下游谱在高动量端以斜率为 $a$ 的幂律谱为渐近——无论入射谱的详细形态如何。

### C.2 微观推导关键

**原文**："As in all Fermi acceleration processes, the key to obtaining a power law is that the momentum gained by a particle in each elementary acceleration event should be proportional to the momentum it already has and to its probability of escaping from the acceleration region."

**主干**：the key ... is that the momentum gained ... should be proportional to the momentum it already has and to its probability of escaping.

**修饰**：类比（as in all Fermi processes）

**中译**：如同所有 Fermi 加速过程，获得幂律的关键在于：粒子每次基本加速事件获得的动量，必须与其已有的动量成正比，并与其逃逸出加速区域的概率成正比。

### C.3 非线性反馈

**原文**："It is easy to see from the elementary theory that the ratio of the downstream energetic particle pressure to that upstream is $a(\alpha - 3 - \gamma_c)^{-1}$ where $\alpha = 3r(r-1)^{-1}$ is the slope of the power law and $\gamma_c$ is the effective specific heat ratio of the particles; thus in the linear theory the downstream particle pressure diverges for sufficiently strong shocks."

**主干**：ratio ... is $a(\alpha-3-\gamma_c)^{-1}$ ... thus pressure diverges for strong shocks.

**修饰**：插入解释 $\alpha$ 和 $\gamma_c$ 的定义

**中译**：从基本理论可易见：下游与上游高能粒子压力之比等于 $a(\alpha-3-\gamma_c)^{-1}$，其中 $\alpha = 3r/(r-1)$ 是幂律斜率，$\gamma_c$ 是粒子的有效比热比；因此在（线性）理论中，对于足够强的激波，下游粒子压力会发散。

上一章：[[97_quality_check.md]]
下一章：[[99_final_summary.md]]
