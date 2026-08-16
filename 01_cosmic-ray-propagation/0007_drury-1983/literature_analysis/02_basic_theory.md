---
section: "2 / 2.1"
title: "Basic theory — Transport of energetic charged particles"
pages: "976-982"
parent: "00_overview.md"
previous: "01_introduction.md"
next: "03_shock_kinematics.md"
---

# 2. Basic theory / 2.1 Transport

## 2.1 输运方程的启发式推导

[FACT] Drury 从均匀磁场中的带电粒子运动出发：粒子沿磁力线做螺旋运动，平行速度 $v_{\parallel}$ 与回旋速度 $v_{\perp}$ 叠加。

[FACT] 投掷角余弦：$\mu = \mathbf{p}\cdot\mathbf{B}/(pB)$（pitch cosinus）。

[FACT] 通过假设散射足够强使分布各向同性化，从相空间密度 $f(\mathbf{x}, p, t)$ 出发推导输运方程。

## 2.2 关键输运方程（2.11）

[FACT] 各向同性化后的输运方程：

$$ \frac{\partial f}{\partial t} + \mathbf{U}\cdot\nabla f - \nabla\cdot(\kappa\nabla f) - \frac{1}{3}(\nabla\cdot\mathbf{U})\, p\,\frac{\partial f}{\partial p} = 0 $$

其中：
- $f(\mathbf{x}, p, t)$：相空间密度（isotropic part）
- $\mathbf{U}$：流体速度
- $\kappa$：扩散系数
- $\nabla\cdot\mathbf{U}$ 项：绝热增益/损耗（adiabatic gain/loss）

[INTERPRETATION] 第三项是扩散，第四项是 adiabatic cooling/heating——这是 Fermi 第二类加速的微观来源（下游湍流中散射中心随机运动导致的二阶效应）。

## 2.3 物理意义

[FACT] 方程 (2.11) 是全文后续所有推导的基础方程，被 Drury 明确标注为"elementary result"。

[CRITIQUE] 该方程假设各向同性化（quasi-linear scattering regime），在非线性和准直激波情形需要修正（§ 4.1 讨论自激散射是否破坏此假设）。

下一章：[[03_shock_kinematics.md]]
上一章：[[01_introduction.md]]
