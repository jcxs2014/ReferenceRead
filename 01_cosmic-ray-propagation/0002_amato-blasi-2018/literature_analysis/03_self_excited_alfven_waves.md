> 本章属于：Cosmic ray transport in the Galaxy: A review（Amato & Blasi 2018）
>
> 上一章：`02_standard_predictions.md`
>
> 下一章：`04_self_generated_transport.md`
>
> 总览：`00_overview.md`

# 3. Self-Excited Alfvén Waves — 自激发 Alfvén 波

## 3.1 本节核心内容

§3 讨论**两种 streaming 不稳定性**——共振分支和非共振分支——的物理机制和生长率，以及波的阻尼过程。这两种不稳定是 CR 非线性传播的物理基础。

## 3.2 原文核心内容

### 3.2.1 CR 不是被动者

本文反复强调的核心论点：

> CRs are far from passive spectators of their acceleration and transport through the Galaxy. They rather affect the environment that hosts them in two main ways: (1) through an actual dynamical action where their energy density is large enough to compete with that of the background gas, and (2) through their ability at generating hydromagnetic waves.

**两种非线性作用**：

| 作用 | 物理条件 | 发生位置 |
|---|---|---|
| 动力学作用 | $U_{\rm CR} \gtrsim U_{\rm gas}$ | 加速源附近 |
| 自激发波 | $v_{\rm stream} > v_A$ | 普遍（只要有 CR streaming）|

### 3.2.2 Streaming 不稳定性

**触发条件**：粒子流速度超过局部 Alfvén 速度。

**历史**：自 1970s（Skilling 1971, Holmes 1975）已知。Wentzel (1974), Cesarsky (1980) 综述。

**两种模式**：

### 共振分支（Resonant Branch）

共振条件：粒子回旋半径 = 波波长：

$$p_{\rm res}(k) = \frac{e B_0}{c k}$$

生长率（公式 8）：

$$\gamma_{\rm CR}^{\rm RES}(k) = \frac{p^2 v_A}{c B_0} J_{\rm CR}^{\rm RES}(k)$$

等价地用密度梯度表示（公式 11）：

$$J_{\rm CR}^{\rm RES} = \frac{4\pi e D(p) p^3}{c} \frac{\partial \ln f}{\partial p}\bigg|_{p=p_{\rm res}}$$

> **分析 / Interpretation**：共振分支的生长率 $\propto D(p)$——扩散系数越大，波生长越快。这是**自洽耦合**的关键：$D(p)$ 由波振幅决定，波振幅又由 $D(p)$ 生长——这是一个**非线性回路**。

### 非共振分支（Non-Resonant / Bell Instability）

**更严格的条件**（公式 9）：

$$v_d > c \sqrt{U_B / U_{\rm CR}}$$

即粒子漂移速度必须超过电磁能量平衡速度。

**最大生长率**（公式 10）在 $k_c = 4\pi J_{\rm CR}/(c B_0)$ 处：

$$\gamma_{\rm CR}^{\rm NR}(k_c) = \frac{4\pi v_A J_{\rm CR}}{c B_0}$$

**两种模式的空间分布**：

| 模式 | 生长率公式 | 适用位置 |
|---|---|---|
| 共振 | $\gamma \propto p^2 v_A J_{\rm CR} / (c B_0)$ | 银河系传播（远离源）|
| 非共振 | $\gamma \propto 4\pi v_A J_{\rm CR} / (c B_0)$ | 加速源附近（高密度/高速度）|

> **分析 / Interpretation**：非共振分支的 $\gamma \propto J_{\rm CR}$（总电流），不依赖共振动量——因此在高密度区域（源附近）更强。Bell (2004) 指出非共振分支可以在 SNR 处产生足够大的磁场（$\sim 100\,\mu$G）解释 X 射线观测。

## 3.3 波的阻尼

波的振幅不可能无限增长——阻尼机制：

**共振阻尼**（CGL 阻尼）：波振幅饱和时的条件

**Landau 阻尼**：在电子/离子回旋频率以上，磁声波被 Landau 阻尼。

**离子回旋阻尼**：Alfvén 波在 $k v_A > \Omega_i$（离子回旋频率）时被离子回旋阻尼吸收——这是低能量 Alfvén 波的终止条件。

## 3.4 关键公式

| 编号 | 公式 | 出处 | 物理意义 |
|---|---|---|---|
| 8 | $\gamma_{\rm CR}^{\rm RES}(k) = p^2 v_A J_{\rm CR}^{\rm RES} / (c B_0)$ | §3 | 共振分支生长率 |
| 9 | $v_d > c\sqrt{U_B/U_{\rm CR}}$ | §3 | 非共振分支生长条件 |
| 10 | $\gamma_{\rm CR}^{\rm NR}(k_c) = 4\pi v_A J_{\rm CR} / (c B_0)$ | §3 | 非共振最大生长率 |
| 11 | $J_{\rm CR}^{\rm RES} = 4\pi e D(p) p^3/c \cdot \partial\ln f/\partial p$ | §3 | 共振电流 = 密度梯度 × 扩散 |

## 3.5 关键参数

| 参数 | 值 | 出处 |
|---|---|---|
| Alfvén 速度 | $v_A \sim 15$ km/s（传播区）| §3 |
| Alfvén 速度 | $v_A \sim 50-100$ km/s（源附近）| §3 |
| 共振波长 | $\lambda \sim 2\pi r_L(p)$ | §3 |
| 非共振最大 $k_c$ | $k_c = 4\pi J_{\rm CR}/(cB_0)$ | §3 |
| 离子回旋阻尼条件 | $k v_A > \Omega_i$ | §3 |

## 3.6 作者的逻辑

```
CR 不是被动者
→ 两种作用：动力学（能量密度）+ 自激发波（streaming）
→ Streaming 不稳定性：共振 + 非共振两种分支
→ 共振分支：$\gamma \propto D(p)$（自洽耦合）
→ 非共振分支：$\gamma \propto J_{\rm CR}$（源附近）
→ 波的阻尼（离子回旋 / Landau / CGL）
```

## 3.7 潜在问题与值得关注的地方

1. **自洽耦合的核心困难**：$\gamma_{\rm CR}^{\rm RES} \propto D(p)$ 而 $D(p) \propto 1/W(k)$（波振幅）——波越大扩散越慢，扩散越慢波生长越快——**正反馈**。这种正反馈可能导致饱和机制复杂。

2. **Bell 不稳定性**（非共振分支）：Bell (2004) 首次系统性研究。Amato & Blasi 2009 等进一步发展。本文作为综述回顾其进展。

3. **阻尼的物理**：本文未详细展开阻尼机制——§4 的饱和处理会用到阻尼，但具体阻尼率是模型依赖的。