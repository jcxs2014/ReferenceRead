---
section: "2.3"
title: "Diffusive acceleration at shocks — DSA 核心推导"
pages: "987-987"
parent: "00_overview.md"
previous: "03_shock_kinematics.md"
next: "05_linear_modifications.md"
---

# 2.3 Diffusive acceleration at shocks — 核心推导

## 2.1 宏观（macroscopic）推导

[FACT] Drury 在稳态、平行平面激波、测试粒子近似下求解输运方程 (2.11)。引入 $r = U_1/U_2$ 压缩比，定义

$$ a = \frac{3r}{r-1} $$

[FACT] 稳态解为**动量空间的幂律**：

$$ f(p) = b\,p^{-a} $$

其中 $b$ 为任意积分常数，$a = 3r/(r-1)$ 是核心结果。

[FACT] 对非相对论强激波（$r = 4$）：$a = 4$，对应能谱 $N(E) \propto E^{-2}$。

[FACT] 对相对论强激波（$r = 4/3$）：$a = \sim 7$。

## 2.2 微观（microscopic）推导（Bell 1978a）

[FACT] Drury 复述 Bell 的微观推导：粒子多次穿越激波，每次获得的动量增益与概率之比为常数。

[FACT] 关键比值：
- **逃逸概率**（per shock crossing）：$P_{\rm esc} \sim 4U_2/v$（下游逃逸概率）
- **每次穿越的相对动量增益**：$\langle\Delta p\rangle/p = 4(U_1 - U_2)/(3v)$

[FACT] 幂律斜率 = 逃逸概率 / 平均动量增益（ratio of escape probability to mean momentum gain）：

$$ -\frac{d\ln N}{d\ln p} = a = \frac{3U_1}{U_1-U_2} = \frac{3r}{r-1} $$

[INTERPRETATION] 这就是 DSA 的"universal"性质：**谱指数只依赖压缩比**，与磁场几何、湍流细节、扩散系数大小无关（只要粒子足够快）。

## 2.3 关键物理洞察

[FACT] "as in all Fermi acceleration processes, the key to obtaining a power law is that the momentum gained by a particle in each elementary acceleration event should be proportional to the momentum it already has and to its probability of escaping."

[FACT] 幂律截断：如果上游谱比 $p^{-a}$ 更硬（slope $< a$），下游谱在高动量端渐近趋于 $p^{-a}$——**激波是一个"滤波器"**，把任意入射谱渐近变成 $p^{-a}$。

[CRITIQUE] 此"渐近幂律"依赖于扩散系数 $\kappa(p) \to 0$ 比 $p^{\alpha}$ 更慢——若 $\kappa$ 增长过快（如 Bohm 扩散 $\kappa \propto p$），高能端截断会提前。

下一章：[[05_linear_modifications.md]]
上一章：[[03_shock_kinematics.md]]
