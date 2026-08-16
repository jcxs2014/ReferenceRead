---
section: "3"
title: "Linear modifications (test-particle regime) — §3 总述"
pages: "987-1003"
parent: "00_overview.md"
previous: "04_diffusive_acceleration.md"
next: "06_oblique_shocks.md"
---

# 3. Linear modifications — 总述

原文§3 引子，p.987（fulltext.txt 行 739-753）

## 3.1 章节框架

[FACT] 第 3 节处理"粒子视为测试粒子"（test particles）假设下的所有修正：粒子之间互不影响，粒子对背景等离子体亦无反馈。

[FACT] 关键线性化假设（原文 p.987 行 745-747）：粒子"move without influence on one another or on the background plasma"——这使输运问题线性化，数学分析大大简化。

[FACT] 分类：
- §3.1 斜激波（Oblique shocks, p.991）
- §3.2 时间依赖解（Time-dependent solutions, p.995）
- §3.3 非平面激波/球激波（Non-planar shocks, p.1000）：(a) 点爆炸球激波；(b) 星风终止激波
- §3.4 附加能量增益/损耗（Additional energy gains and losses, p.1001）
- §3.5 $\mathcal{O}(U/v)$ 高阶效应（Effects of higher order, p.1002）

## 3.2 第 2 节理想假设回顾（原文行 748-751）

[FACT] §2 中理想化条件：

- 激波平行（parallel）
- 稳态（steady）
- 平面（plane）
- 粒子速度 $\gg$ 背景等离子体速度
- 散射弹性
- 无附加能量损失
- 粒子不反作用于等离子体系统（测试粒子）

[FACT] §3 放松前 6 条理想化，保留最后一条（测试粒子）。§4 放松最后一条——讨论非线性反作用。

## 3.3 共同特点

[FACT] **谱指数 $a = 3r/(r-1)$ 保持形式不变**——所有修正只改变谱的振幅、时间尺度或切点（cut-off）位置，不改变谱指数本身（在 $\mathcal{O}(U/v)$ 阶）。

[FACT] 例外：§3.3 球激波引入 $\mathcal{O}(\kappa/RR')$ 的一阶修正，将谱指数修正为 $\alpha_{\rm sph} = a + \delta\alpha$（详见 §3.3）。

[FACT] §3.4 附加能量损失可以改变谱指数（引入额外 $p\,dp/dt$ 项），但不改变基本幂律形态——只是在渐近端出现截断。

## 3.4 数学方法概览

[FACT] §3.1（斜激波）：将宏观推导中的输运方程在正交坐标系下分解，引入有效压缩比 $r_{\rm eff} = U_1\cos\theta_1 / U_2\cos\theta_2$。

[FACT] §3.2（时间依赖）：Laplace 变换技术，将 (2.31) 化为 $(s + U\partial_x)\tilde{f} = \kappa \partial_x^2 \tilde{f} + \tilde{Q}$，解析延拓到 $s\to 0$ 极点提取稳态解，其余奇点贡献瞬态。

[FACT] §3.3（球激波）：奇异摄动理论（singular perturbation theory）——小参数 $\epsilon = \kappa/(RR')$，将"outer"（远离激波面）解与"inner"（激波面前边界层）解匹配。

[FACT] §3.4（附加损耗）：在输运方程中加源/汇项，重新匹配并积分。

[FACT] §3.5（高阶）：对 §2-§3.4 结果做 $U/v$ 展开的下一阶修正。

[INTERPRETATION] §3 全章论证的核心信息：DSA 幂律的"普适性"在测试粒子极限下极为稳健——无论激波几何、时间演化、附加耗散，谱指数都被压缩比牢牢钉住。

下一章：[[06_oblique_shocks.md]]
上一章：[[04_diffusive_acceleration.md]]
