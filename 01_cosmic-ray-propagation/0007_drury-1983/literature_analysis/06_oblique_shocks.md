---
section: "3.1"
title: "Oblique shocks — §3.1"
pages: "991-995"
parent: "00_overview.md"
previous: "05_linear_modifications.md"
next: "07_time_dependent.md"
---

# 3.1 Oblique shocks — §3.1

原文§3.1，p.991-995（fulltext.txt 行 754-911）

## 3.1 问题陈述

[FACT] "限制在平行激波似乎基本理论的主要缺陷"（p.991 行 756-757）：若磁场方向与激波传播方向无相关，平均激波斜度约 $60^\circ$。

[FACT] 直觉预期：粒子可能被直接反射，导致显著修正——"one might expect that the possibility of direct particle reflection from the shock would lead to significant alterations"（p.991 行 762-764）。

[FACT] 意外结果：**在 $\mathcal{O}(U/v)$ 阶**，斜度完全不影响稳态谱。

## 3.2 宏观推导（subluminal 斜激波）

[FACT] 设磁场线与激波面交点亚磁声运动。存在唯一框架：电场为零、$\mathbf{U}_1$ 沿 $\mathbf{B}_1$ 与激波法线夹角 $\theta_1$、$\mathbf{U}_2$ 沿 $\mathbf{B}_2$ 夹角 $\theta_2$（图 1a）。

[FACT] 输运方程 (2.11) 变为（p.991 行 773-777）：

$$U_i\cos\theta_i\,\frac{\partial f}{\partial x} = \kappa_{\parallel,i}\cos^2\theta_i\,\frac{\partial^2 f}{\partial x^2} + \kappa_{\perp,i}\sin^2\theta_i\,\frac{\partial^2 f}{\partial y^2}$$

其中通常 $\kappa_\parallel \geq \kappa_\perp \geq \kappa_{\perp\perp}$。

[FACT] 关键替换：用**法向分量** $U_{\rm eff} = U\cos\theta$、$\kappa_{\rm eff} = \kappa_\parallel\cos^2\theta + \kappa_\perp\sin^2\theta$——上游下游解在形式上与平行激波完全相同。

[FACT] 匹配条件（密度 $f$ 连续 + 粒子流 $S$ 连续，行 789-791）：

$$S = -\tfrac{1}{3}U p\frac{\partial f}{\partial p} - \kappa\frac{\partial f}{\partial x}$$

Liouville 定理 $\Rightarrow f_+ = f_-$，$S_+ = S_-$，得 $a=1,c=0$，粒子数守恒 $\Rightarrow d=1$；剩余参数 $b \sim 1/v$，当 $S/f = \mathcal{O}(U)$ 时 $b\cdot S = \mathcal{O}(U/v)$ 可忽略。

[FACT] **结论**：宏观扩散理论中，用正交分量后斜激波的谱与平行激波完全相同——仍由单一参数（压缩比 $r$）决定，"essentially independent of the obliquity"（p.991 行 806-807）。

## 3.3 反射修正辨析

[FACT] 一种常见论证（Fisk 1971, Achterberg & Norman 1980）认为若比例 $\epsilon$ 的入射粒子被反射，则匹配条件应改为 $f(0+) = (1-\epsilon)f(0-)$（方程 3.3）。

[FACT] Drury 判定这"显然是错误的"（"clearly incorrect"），理由是：
- 本文讨论的是**磁静力学反射**（magnetostatic），不涉及准直激波的波粒共振
- 反射在此情形下不改变粒子流匹配

[FACT] 更令人信服的证明：用微观推导重做（行 821-907），结果完全一致。

## 3.4 微观推导（p.991 行 821-907）

[FACT] 粒子从上游以投射角 $\mu_1$ 和回旋相位 $\alpha_1$ 抵达激波，被透射或反射；透射后下游扩散直到再次返回激波（图 2, p.989 行 838）。

[FACT] 定义五类相空间集合：$T_1$（上游入射导致透射）、$R_1$（上游反射）、$T_2$（下游返回透射）及它们的逆向集 $\bar{T}_1,\bar{R}_1,\bar{T}_2$（方程 3.4）。

[FACT] 由 Liouville 定理：$T_1 \cup R_1$ 覆盖右半球，$T_2$ 覆盖左半球——"no reflection from downstream"（3.5）。

[FACT] 透射概率（行 853-869）：$P_{\rm trans} = 2U_1\cos\theta_1 / v$；下游逃逸概率 = $4U_2\cos\theta_2 / v$（与平行激波相同，只用 $\cos\theta$ 修正）。

[FACT] 综合逃逸概率：$P_{\rm esc} = 4U_2\cos\theta_2 / (2U_1\cos\theta_1)$

[FACT] 平均动量增益 (3.10)-(3.14)：重复应用 Liouville 定理得到 $\langle\Delta p\rangle/p = 4(U_1\cos\theta_1 - U_2\cos\theta_2)/(3v)$。

## 3.5 关键结果

[FACT] 积分谱斜率（p.991 方程 3.15, 行 902-903）：

$$-\frac{d\ln N}{d\ln p} = \frac{4U_2\cos\theta_2/v\cos\theta_1}{\langle\Delta p\rangle/p} = \frac{3U_2\cos\theta_2}{U_1\cos\theta_1 - U_2\cos\theta_2}$$

[FACT] 用有效压缩比 $r = U_1\cos\theta_1/U_2\cos\theta_2$，得：

$$-\frac{d\ln N}{d\ln p} = \frac{3r}{r-1}$$

[FACT] **最终结论**（p.991 行 906-910）：若 $U$ 为传统激波速度（法向分量 $U = U_1\cos\theta_1$），稳态谱**不依赖斜度 $\theta$**，约束条件 $\sec\theta \ll v/U$——对近垂直激波此约束可能非常严苛。

[INTERPRETATION] 该结论的"remarkable"之处：即使激波几乎垂直，只要粒子 gyroradius $\ll$ 扩散长度（保证扩散近似有效），幂律谱指数仍由压缩比决定。

[CRITIQUE] 对近垂直激波，准直约束（gyroradius $\ll$ 扩散长度）可能破坏测试粒子假设——粒子可能无法在两侧有效扩散，此时 §4 非线性效应变得重要。

下一章：[[07_time_dependent.md]]
上一章：[[05_linear_modifications.md]]
