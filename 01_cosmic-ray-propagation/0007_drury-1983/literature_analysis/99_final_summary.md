---
section: "summary"
title: "Final Summary"
parent: "00_overview.md"
previous: "98_vocabulary.md"
next: null
---

# 99. Final Summary — Drury (1983) DSA 综述

## 一句话总结

L. O'C. Drury (1983) 的综述以宏观输运方程和微观单粒子反弹双视角，系统推导了扩散激波加速（DSA）产生幂律谱的机制，并完整讨论了从斜激波、时间依赖、球激波到非线性修正（自激散射、修改激波结构、谱形变、注入、压力发散）的全部修正项，为之后 40 年的 DSA 文献奠定了理论与术语框架。

## 关键公式

| 编号 | 公式 | 意义 |
|---|---|---|
| 输运方程 | $\partial_t f + \mathbf{U}\cdot\nabla f - \nabla\cdot(\kappa\nabla f) - \frac{1}{3}(\nabla\cdot\mathbf{U}) p\partial_p f = 0$ | 各向同性粒子输运（2.11） |
| 谱指数 | $a = 3r/(r-1)$ | 只依赖压缩比 |
| 强激波谱 | $a = 4$（$r=4$） | 非相对论强激波，$N(E)\propto E^{-2}$ |
| 逃逸概率 | $P_{\rm esc} = 4U_2/v$ | 下游逃逸概率 |
| 平均动量增益 | $\langle\Delta p\rangle/p = 4(U_1-U_2)/(3v)$ | 单次穿越 |
| 加速时标 | $t_{\rm acc}(p) = 3(\kappa_1/U_1 + \kappa_2/U_2)/(U_1-U_2)$ | (3.39) |
| 斜激波有效 $r$ | $r = U_1\cos\theta_1/(U_2\cos\theta_2)$ | §3.1 |

## 关键数值

- 银河系宇宙线观测谱指数 ≈ −2.7（动能谱），对应 $a ≈ 2.7$；DSA 强激波预言 $a=4$——比观测略硬
- 典型扩散系数幂律 $\kappa \propto p^\alpha$，$\alpha ∈ [0.3, 0.5]$（观测）
- Bohm 极限：$\kappa \propto p$，$\alpha = 1$

## 主要发现（findings）

1. **谱指数普适性**：在测试粒子近似下，$a$ 只依赖压缩比，与磁场几何、扩散系数大小无关
2. **激波作为滤波器**：无论上游谱形态如何，下游谱在高动量端渐近趋于 $p^{-a}$
3. **加速时标**：$t_{\rm acc} \propto \kappa/(U_1-U_2)$；Bohm 极限下 $t_{\rm acc} \propto p$
4. **斜激波不影响谱指数**（在 $\sec\theta \ll v/U$ 约束内）
5. **非线性反馈不可避免**：下游粒子压力对强激波发散（§ 4.5），迫使引入子激波（sub-shock）结构
6. **注入问题（injection）是 DSA 理论的关键未解决问题**：从热等离子体到 DSA 能区的过渡机制仍不明

## 批评（critique）

- Drury 承认"没有任何稳态解可以适用于非常强的激波"——时间依赖效应不可避免
- 自激 Alfven 波的增长率可能"未知后果（unknown consequences）"——准线性理论在强非线性区失效
- 注入问题被明确标记为"very hard to quantify"——40 年后仍是 SNR 与 AGN 喷流加速的核心难题

## 与本库其它论文的关系

- [[bell-1978]] Bell 1978 的微观 DSA 推导与自激 Alfven 波分析在 Drury 1983 § 4.1 中被系统综述
- [[blandford-ostriker-1978]] Blandford & Ostriker 1978 的微扰展开在 Drury 1983 § 4.3 中被推广
- Drury 1983 是 [[strong-2007]], [[amato-blasi-2018]], [[genolini-2021]] 引用的 DSA 综述标准文献

## 25. Completeness Check

- [x] Abstract（p. 973 摘要）
- [x] Introduction（§1）
- [x] All main sections（§1-5，§3.3-3.4、§4.1-4.5、§5 在总述中覆盖，未生成独立文件）
- [x] Methods（宏观输运方程 + 微观反弹双推导）
- [x] Data（无数据；理论综述）
- [x] Background（§1 完整历史溯源）
- [x] Results（核心：谱指数 $a = 3r/(r-1)$）
- [x] Discussion（§3 线性修正 + §4 非线性修正）
- [x] Conclusion（§5 Concluding remarks）
- [x] Figures（Fig 1-8 已索引；未单独成文件分析）
- [x] Tables（原文无表）
- [x] Important equations（6 条关键公式已记录）
- [x] Important numerical values（谱指数、压缩比、扩散幂律）
- [x] Important references（Bell 1978, Blandford & Ostriker 1978, Axford et al. 1977, Krymsky 1977 等）

**注意**：受父代理指示，§3.3-3.4、§4.1-4.5、§5 未生成独立文件；后续补齐可参照 §2/§3 已有文件结构。

上一章：[[98_vocabulary.md]]
下一章：（无，此为终结）
