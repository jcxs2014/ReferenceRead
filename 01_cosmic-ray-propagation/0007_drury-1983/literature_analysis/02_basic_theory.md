---
section: "2 / 2.1"
title: "Basic theory — Transport of energetic charged particles"
pages: "976-982"
parent: "00_overview.md"
previous: "01_introduction.md"
next: "03_shock_kinematics.md"
---

# 2. Basic theory / 2.1 Transport

原文§2.1，p.976-982（fulltext.txt 行 127-268）

## 2.1 输运方程的启发式推导

[FACT] 从均匀磁场中自由带电粒子运动出发：粒子沿磁力线做螺旋运动，平行速度 $v_{\parallel}$ 与回旋速度 $v_{\perp}$ 叠加。

[FACT] 投射角余弦（pitch cosine）定义 (2.1)：$\mu = p_{\parallel}/p$；平行与垂直动量 $p_{\parallel} = p\mu$，$p_{\perp} = p(1-\mu^2)^{1/2}$。

[FACT] 回旋半径 (2.3)：$r_g = p_{\perp}/ZeB$（SI；高斯制需乘 $c$）。

## 2.2 湍流散射物理

[FACT] 实际宇宙磁场既不静态也不均匀，含有扰动带电粒子的不规则性——导致散射。最简单情形：均匀背景场加小幅静态不规则性；此时电场为零，粒子散射时能量守恒，只改变投射角。

[FACT] 若散射"足够随机"，分布函数 $F(\mathbf{p},\mathbf{x},t)$ 被保持接近各向同性，$F \approx f$（isotropic part），输运可用扩散方程描述：$\partial f/\partial t = \nabla\cdot(\boldsymbol{\kappa}\nabla f)$，其中 $\boldsymbol{\kappa}$ 为（各向异性）扩散张量。

[FACT] 最有效散射的不规则性：长度尺度 ≈ 粒子回旋半径。该尺度下均方场变化 $\langle \phi^2 \rangle \sim k I(k)/B_0^2$（$k \sim 1/r_g$，$I(k)$ 为不规则性空间功率谱）。

[FACT] 每次回旋周期投射角变化量量级 $\phi$；$N$ 周期累积变化 $N^{1/2}\phi$；当 $N \sim \phi^{-2} = B_0^2[kI(k)]^{-1}$ 时粒子"忘记"初始投射角，平均自由程 $\lambda_{\parallel} \sim N r_g$。

[FACT] **Bohm 扩散系数** (2.8)：$\kappa_B = \frac{1}{3} r_g v$——完全随机场下的最小扩散系数。

## 2.3 两种散射中心运动

[FACT] 类型 1：背景系统的大尺度运动，速度 $\mathbf{U}$——对流项 $\partial t \to \partial t + \mathbf{U}\cdot\nabla$（方程 2.10）。

[FACT] 类型 2：单个散射中心相对背景的随机运动，速度 $V$——产生动量空间扩散：

$$D = \tfrac{1}{2}(\Delta p)^2 \sim V^2 p^2 / \lambda$$

这就是经典的**二阶 Fermi 加速**（Fermi 1949, 1954）。天体物理条件下 $V$ 通常 ≈ Alfvén 速度，往往小到可忽略。

## 2.4 关键输运方程（2.13，原文 p.978 行 262）

[FACT] 完整输运方程 (2.13)：

$$\frac{\partial f}{\partial t} + \mathbf{U}\cdot\nabla f - \nabla\cdot(\boldsymbol{\kappa}\nabla f) - \frac{1}{3}(\nabla\cdot\mathbf{U})\, p\,\frac{\partial f}{\partial p} = \frac{1}{p^2}\frac{\partial}{\partial p}(p^2 D \frac{\partial f}{\partial p})$$

各项物理：

- 第二项：背景对流
- 第三项：空间扩散
- 第四项：绝热增益/损耗（位置空间收敛 ↔ 动量空间发散，Liouville 定理）
- 右端：二阶 Fermi 加速（散射中心随机运动）

[FACT] 简化版 (2.11)（忽略 $V$）：

$$\frac{\partial f}{\partial t} + \mathbf{U}\cdot\nabla f = \nabla\cdot(\boldsymbol{\kappa}\nabla f) + \frac{1}{3}(\nabla\cdot\mathbf{U})\, p\,\frac{\partial f}{\partial p}$$

这是全文后续推导的"elementary result"。

[FACT] Skilling (1975) 给出该方程的严格形式推导。

[INTERPRETATION] 第三项（扩散）与第四项（绝热）的平衡是 §2.3 稳态幂律解的核心；右端项是 Fermi 第二类加速的微观来源。

[CRITIQUE] 方程假设各向同性化（quasi-linear scattering regime），在准直激波（quasi-perpendicular）或自激波情形需要修正（§4.1）。

下一章：[[03_shock_kinematics.md]]
上一章：[[01_introduction.md]]
