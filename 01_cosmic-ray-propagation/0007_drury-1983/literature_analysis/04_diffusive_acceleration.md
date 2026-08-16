---
section: "2.3"
title: "Diffusive acceleration at shocks — DSA 核心推导"
pages: "983-987"
parent: "00_overview.md"
previous: "03_shock_kinematics.md"
next: "05_linear_modifications.md"
---

# 2.3 Diffusive acceleration at shocks — 核心推导

原文§2.3，p.983-987（fulltext.txt 行 459-738）

## 2.1 概述：从单次穿越到随机过程

[FACT] 在 §2.2 单次穿越中粒子能量增益有限（"only a moderate amount"），且过程可逆，下游谱本质上就是入射谱的能量平移。

[FACT] 一旦引入扩散效应（diffusive effects），粒子与激波的相互作用次数成为**随机变量**——少数粒子通过多次穿越达到极高能量。

[FACT] 此随机性意味着"信息被摧毁（熵产生）"——下游能谱对入射谱细节**相对独立**。这是"幂律滤波器"图像的关键：激波把任意入射谱渐近变成 $p^{-a}$。

[FACT] 两种推导路径：微观（Bell 1978a）——跟踪单粒子能量变化与历史；宏观（Krymsky 1977, Axford et al. 1977, Blandford & Ostriker 1978）——使用分布函数及其输运方程。

## 2.2 宏观推导（§2.3.1, p.983 行 478-618）

[FACT] 假设：粒子速度 $\gg$ 流体速度；散射保持流体系下分布函数近似各向同性（扩散近似有效）；散射弹性；散射中心有效质量无穷大。

[FACT] 稳态输运方程 (2.31) 简化为 (2.32)：

$$U_i\frac{\partial f}{\partial x} = \frac{\partial}{\partial x}\left(\kappa_i\frac{\partial f}{\partial x}\right)$$

[FACT] 通解 (2.33)：$f = g_i(p) + h_i(p)\exp(U_i x/\kappa_i)$；边界条件（上游给定 $f_1(p)$ 入射，下游有限）给出 $f$ 上游为 $f_1(p) + g_1(p)[1-\exp(U_1 x/\kappa_1)]$，下游为 $g_2(p)$。

[FACT] 关键匹配条件 (2.39)-(2.40)——连续性 $f_1 + g_1 = f_2$ 与粒子流连续性——可从输运方程作为"弱解"（weak solution）直接推导（方程 2.41-2.42）。

[FACT] 消去 $g_1$ 引入 $r = U_1/U_2$，得 (2.43)：$p f_2' = -a f_2$，其中 $a = 3r/(r-1)$，解为 $f_2(p) = b\,p^{-a} + c\,p^{-a}\int_0^p f_1(p')\,p'^{a-1}\,dp'$（2.44）。

[FACT] 物理意义：第一项 = 来自背景热等离子体的注入贡献（"injected from the thermal background"）；第二项 = 上游被输运进来的粒子被加速——下游谱是上游谱与截断幂律的卷积。

[FACT] **滤波器性质**：若上游谱比 $p^{-a}$ 更硬（slope $<a$），下游谱在高动量端渐近为 $p^{-a}$，与入射谱细节无关（p.985 行 633-635）。

[FACT] 对强激波 $M\to\infty$、非相对论等离子体 $\gamma=5/3$：$r\to 4$，$a\to 4$（p.985 行 643）。与银河宇宙线源谱指数 $a \approx 4.3$ 接近（p.985 行 644-645）。

## 2.3 微观推导（§2.3.2, p.986 行 667-738）

[FACT] Drury 复述 Bell 的微观推导：从激波上游穿越到下游的粒子，其逃逸概率（不再返回）为 $4U_2/v$——因为激波下游粒子数密度 $n$ 恒定，逃逸流 $nU_2$，进入下游的流 $nv/4$（各向同性假设）。

[FACT] 单次穿越的动量变化：上游流体系动量 $p$，激波系 $p(1+\mu U_1/v)$，下游流体系 $p[1+\mu(U_1-U_2)/v]$；各向同性平均（权重 $2\mu$）：

$$\langle\Delta p\rangle = \frac{2}{3}\,p\,\frac{U_1-U_2}{v}$$

往返一次（两次穿越，$U_1,U_2$ 互换）总增益：

$$\langle\Delta p\rangle_{\rm round} = \frac{4}{3}\,p\,\frac{U_1-U_2}{v}$$

[FACT] 粒子返回 $n$ 次后的动量 (2.51)：

$$p_n = p_0\left(1 + \frac{4(U_1-U_2)}{3v}\right)^n \xrightarrow{n\to\infty} p_0\exp\left(\frac{4n(U_1-U_2)}{3v}\right)$$

[FACT] 返回 $n$ 次的概率 (2.53)：$P_n = \left(1 - 4U_2/v\right)^n \xrightarrow{n\to\infty} \exp(-4nU_2/v)$

[FACT] 累积概率给出幂律谱 (2.56)：

$$N_2(p) \propto p^{-a}, \quad a = \frac{3U_1}{U_1-U_2} = \frac{3r}{r-1}$$

## 2.4 关键物理洞察

[FACT] "as in all Fermi acceleration processes, the key to obtaining a power law is that the momentum gained by a particle in each elementary acceleration event should be proportional to the momentum it already has and to its probability of escaping."（原文 p.987 行 731-734）

[FACT] 与其他 Fermi 过程的关键区别：**比例常数由激波运动学固定**，不是任意的（"the constant of proportionality... is fixed by the kinematics of the shock"，原文 p.987 行 736-737）。

[FACT] 这就是 DSA 的"universal"性质：**谱指数只依赖压缩比**，与磁场几何、湍流细节、扩散系数大小无关（只要粒子足够快）。

[FACT] 幂律截断条件：要求 $\kappa(p) \to 0$ 比 $p^{\alpha}$ 增长更慢——若 $\kappa$ 增长过快（如 Bohm 扩散 $\kappa \propto p$），高能端截断会提前。

[CRITIQUE] 宏观推导虽然直接但"缺乏物理内容"（原文 p.986 行 649），因为物理都塞进了输运方程——这正是微观推导的必要性。

下一章：[[05_linear_modifications.md]]
上一章：[[03_shock_kinematics.md]]
