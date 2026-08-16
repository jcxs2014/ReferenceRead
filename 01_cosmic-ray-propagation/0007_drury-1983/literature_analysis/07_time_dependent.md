---
section: "3.2"
title: "Time-dependent solutions — §3.2"
pages: "995-1000"
parent: "00_overview.md"
previous: "06_oblique_shocks.md"
next: "08_nonplanar_shocks.md"
---

# 3.2 Time-dependent solutions — §3.2

原文§3.2，p.995-1000（fulltext.txt 行 912-1118）

## 3.1 加速时标

[FACT] 量纲论证给出基本时间尺度为 $\kappa/U$——与 Forman & Morfill (1979)、Krymsky et al. (1979)、Vasil'yev et al. (1980)、Axford (1981a,b) 一致（p.995 行 914-917）。

[FACT] 模型系统：稳态平面激波，激波位置在 $t=0$ 时开启单能（monoenergetic）源 $Q\,\delta(p-p_0)$，初值 $f(0,x,p) = 0$。

[FACT] 对时间作 Laplace 变换：(2.31) 变为 (3.17)——上游下游各为 $\tilde{f}_i'' - p_i^2 \tilde{f}_i = -\tilde{Q}_i/\kappa_i$。

[FACT] 解 (3.18)：$\tilde{f}_i \propto \exp(p_i x)$，其中

$$p_i = \frac{1}{2\kappa_i}\left[(1+(-1)^i)\left(1+\frac{\kappa_i s}{U_i}\right)\right]^{1/2}$$

[FACT] 匹配条件 (3.19) 导致 (3.20)，引入 $A_i = (1+\kappa_i s/U_i)^{1/2}$，解的形式已知——由留数积分反演 Laplace 变换。

## 3.2 时变谱的解析结构

[FACT] 时变谱的完整反演 (3.22)——积分路径位于所有奇点右侧；$s=0$ 处的单极点给出**稳态谱** (3.24)：$f_0(\infty,p_0) = 3Q/(U_1-U_2)$（方程 3.25）。

[FACT] 注入动量 $p_0$ 处稳态值**立即**建立（$t>0$）。

[FACT] 一般时刻 $t>0$、动量 $p>p_0$ 的谱 (3.26)：

$$f(t,p_0,p_1) = f_0(\infty,p_0)\,\varphi(t,p_0,p_1)$$

其中 $\varphi(t)$ 由复积分定义 (3.27)，被积函数涉及 $h(s)$，$h(s) = -\frac{1}{2}\ln(A_1 A_2) + \ln(1+\frac{A_1-A_2}{A_1+A_2}\frac{U_2}{U_1})$。

[FACT] $\varphi(t)$ 物理解释（p.995 行 977-985）：
- 视作给定 $p_0,p_1$ 时**加速时间分布**（probability distribution function）
- 或固定 $t$，视作单脉冲注入粒子经时间 $t$ 的动量谱

## 3.3 加速时间的矩

[FACT] 正定性：$\int_0^\infty \varphi(t)\,dt = 1$（归一化，方程 3.30）

[FACT] **平均加速时间**（mean acceleration time, 方程 3.31, 行 1005）：

$$\langle t_{\rm acc}\rangle(p) = -\left.\frac{dh}{ds}\right|_{s=0} = \frac{3}{U_1-U_2}\left(\frac{\kappa_1}{U_1}+\frac{\kappa_2}{U_2}\right)$$

[FACT] 方差（variance, 方程 3.32, 行 1007-1011）：

$$(\Delta t)^2 = \langle t^2\rangle - \langle t\rangle^2 = -\left.\frac{d^2 h}{ds^2}\right|_{s=0} = \frac{6}{(U_1-U_2)^2}\left(\frac{\kappa_1}{U_1^2}+\frac{\kappa_2}{U_2^2}\right)\int_{p_0}^p\frac{dp'}{p'}$$

[FACT] 一般 $n$ 阶矩 = $h(s)$ 在 $s=0$ 处的 $n$ 阶导数（即加速时间分布的 $n$ 阶 cumulant）。

[FACT] 若 $\kappa \propto p^\alpha$（$\alpha>0$），相对宽度 (3.33)：

$$\frac{\Delta t}{\langle t\rangle} = \sqrt{\frac{3\alpha}{a}}\cdot\frac{\ln(p_1/p_0)}{1} \cdot \text{coeff}$$

——除非 $\alpha \approx 0$（$\kappa$ 几乎与 $p$ 无关），加速时间分布**峰值不尖**（行 1022-1024）。

## 3.4 小时间/大时间渐近行为

[FACT] 大 $s$ 展开 (3.34)：$h(s) \sim p_1\sqrt{s} - z = 3U_1 + \frac{\kappa_2}{U_2}\ln p_1 + \mathcal{O}(s^{-1/2})$

[FACT] 小 $t$ 行为 (3.36)：$\varphi(t) \sim (4\pi\kappa t)^{-1/2}\exp(-p_1^2 t/(4\kappa))$——扩散主导的尖锐峰值。

[FACT] 大 $t$ 行为 (3.38)：$s_0$ 为 $h(s)$ 的最右奇点，$\gamma = \frac{1}{2}$ 或 $\frac{3}{2}$ 分支点，

$$\varphi(t) \sim t^{-\gamma-1}\exp(s_0 t - h(s_0))[1+\mathcal{O}(t^{-\gamma-1})]$$

[FACT] $\kappa$ 与 $p$ 无关且 $A_1=A_2$ 的特例有显式解（Toptyghin 1980, Axford 1981b）；$\kappa \propto p^\alpha$ 情况可用 parabolic cylinder functions 表达（M. Forman 个人通讯）。

## 3.5 微观推导（p.995 行 1064-1118）

[FACT] 上游粒子总驻留时间（mean residence time, 行 1064-1072）：

$$\langle\tau_{\rm up}\rangle = \frac{4\kappa_1}{U_1 v}$$

——上游稳态扩散分布 $\propto \exp(U_1 x/\kappa_1)$，积分给出 $\kappa_1 n/U_1$；除以入射流 $nv/4$。

[FACT] 下游驻留时间：形式上无穷大（存在逃逸概率）——需计算**返回概率**。

[FACT] 返回概率（方程 3.41-3.43）：$P_{\rm ret}(x_0) = \exp(-U_2 x_0/\kappa_2)$；下游能返回激波的粒子数：

$$N_{\rm ret} = \frac{Q}{U_2}[1 - \exp(-U_2 x_0/\kappa_2)] \xrightarrow{x_0\to\infty} \frac{Q}{U_2}$$

[FACT] 下游有效驻留时间 = $\kappa_2/(U_2 v)$（行 1088-1090）。

[FACT] 一个完整循环时间（方程 3.44, 行 1113）：

$$\langle\tau_{\rm cycle}\rangle = \frac{4\kappa_1}{U_1 v} + \frac{4\kappa_2}{U_2 v}$$

[FACT] 每次循环动量增益 (3.45-3.46)：$\langle\Delta p\rangle/\langle p\rangle = 4(U_1-U_2)/(3v)$

[FACT] 由此加速时间尺度（原文 §3.2 结尾, 行 1118）：

$$t_{\rm acc}(p) = \frac{\langle\tau_{\rm cycle}\rangle}{\langle\Delta p\rangle/p}\ln\frac{p}{p_0} = \frac{3}{U_1-U_2}\left(\frac{\kappa_1}{U_1}+\frac{\kappa_2}{U_2}\right)\ln\frac{p}{p_0}$$

与宏观推导完全一致。

[FACT] Bohm 极限下 $\kappa \propto p$，则 $t_{\rm acc} \propto p\ln(p/p_0)$——动量越高，加速越慢。

[CRITIQUE] 单能源是理想化——真实天体物理源有宽幅注入谱；但叠加原理保证解的形式不变。

下一章：[[08_nonplanar_shocks.md]]
上一章：[[06_oblique_shocks.md]]
