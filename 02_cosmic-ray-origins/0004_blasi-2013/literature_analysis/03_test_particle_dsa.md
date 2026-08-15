---
chapter: 3
title: Test-particle DSA
pages: "9–26"
sections:
  - "3.1 Collisionless shocks"
  - "3.2 Transport of charged particles in magnetic fields: basic concepts"
  - "3.3 DSA through the transport equation"
  - "3.4 Maximum energy: time versus space"
related_chapters:
  prev: 02_sn_r_premises
  next: 04_nl_dsa
status: done
---

> 本章属于：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/00_overview.md|The Origin of Galactic Cosmic Rays（Blasi, 2013, arXiv:1311.7346）]]
>
> 上一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/02_sn_r_premises.md|02_sn_r_premises]]
>
> 下一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/04_nl_dsa.md|04_nl_dsa]]
>
# 3. Test-particle DSA — test-particle 扩散激波加速的理论核心

[FACT] §3 覆盖 pp. 9–26（约 18 页），是 Blasi 综述中最技术的一节。核心任务：在不考虑 CR 反作用（test-particle 极限，$\xi_{\rm CR} \ll 1$）的前提下，严格推导 DSA 谱指数与最大能量上限。四个子节依次覆盖：**无碰撞激波**（§3.1）→ **粒子在磁场中的输运**（§3.2）→ **通过传输方程的 DSA 推导**（§3.3）→ **最大能量：时间 vs 空间**（§3.4）。

[INTERPRETATION] §3 的逻辑链条是：**激波能形成吗？**（§3.1）→ **粒子如何在 $B_0$ + 波动背景中运动？**（§3.2）→ **把粒子输运缝合进激波跳变条件**（§3.3）→ **能加速到多高能？**（§3.4）。四个子节构成"形成→输运→缝合→上限"的闭合物理图景；test-particle 假设在 §3.4 末尾暴露其极限，自然过渡到 §4 NLDSA。

---

## 3.1 Collisionless shocks

[FACT] §3.1 讨论 SNR 激波属于**无碰撞激波**（collisionless shock）——与地球大气激波靠分子碰撞形成不同，ISM 中粒子-粒子碰撞的 mean free path 远大于激波尺度，激波只能通过**电磁不稳定性**（collective effects）形成。Treumann (2009) 给出了该领域的详尽综述。

[FACT] Blasi 明确将本综述限制在**非相对论激波**：$v_{\rm sh} \ll c$。该条件可用 Alfvénic Mach 数重写（Eq. 9）：

$$
\frac{v}{v_c} \ll M_A = \frac{v}{v_A} = \frac{m_p}{m_e}^{1/2}\frac{\omega_{p,e}}{\omega_{c,e}} = 1.3\times10^{5}\, n_{\rm cm^{-3}}^{1/2}\, B_{\mu G}^{-1} \quad \text{(Eq. 9)}
$$

其中 $v_A = B_0/\sqrt{4\pi m_p}$ 为 Alfvén 速度，$\omega_{p,e}$、$\omega_{c,e}$ 为电子等离子体频率与回旋频率。

[FACT] 在电子-质子等离子体中，**Coulomb 散射**以三种方式作用：(1) 电子自身热化到 Maxwell 分布；(2) 质子自身热化；(3) 电子-质子相互热化。三者存在明确的层次结构：**电子自热化最快 → e-p 热化次之 → 质子自热化最慢**。

[FACT] 两粒子群（温度 $T_1, T_2$，质量 $m_1, m_2$，同电荷 $q$、同密度 $n$）的**热化时间**（Spitzer 1962，Eq. 10）：

$$
\tau_{\rm eq} = \frac{3 m_1 m_2 k_B^{3/2}}{8(2\pi)^{1/2}\, n\, q^4\, \ln\Lambda}\left(\frac{T_1}{m_1} + \frac{T_2}{m_2}\right)^{3/2}
$$

[FACT] 特化到电子自热化（Eq. 11）：$\tau_{\rm eq,ee} \approx 1200\, (n/1\,{\rm cm^{-3}})^{-1}(T_e/10^{8}\,{\rm K})^{3/2}$ 年；质子自热化（Eq. 12）：$\tau_{\rm eq,pp} \approx 2.3\times10^{6}\, (n/1)^{-1}(T_p/10^{8}\,{\rm K})^{3/2}$ 年。

[FACT] 强激波后温度 $T_p = \frac{3}{16}\, m_p\, V_{\rm sh}^2 / k_B$（Eq. 13），故 $kT_e \approx (m_e/m_p)\, kT_p$——**电子永远跟不上质子温度**，年轻 SNR 电子-质子热化时间可达数千年，远超遗迹年龄（典型 SNR 年龄 $\sim 10^2$–$10^4$ 年），因此电子不热化是可观测特征。

[FACT] 对于**平行激波**（parallel shock），Weibel 不稳定性产生小尺度磁场，提供耗散机制。Blasi 强调**注入机制（injection）** 仍是"one of the most poorly known aspects of the physics of collisionless shocks"；PIC 模拟（Spitkovsky 2008a,b；Sironi & Spitkovsky 2011；Gargaté & Spitkovsky 2012）为注入物理提供了新的视角。

[CRITIQUE] §3.1 指出 Coulomb 热化的层次结构隐含一个重要推论：在年轻 SNR 中**质子尚未 Maxwellian 化**时电子-质子已发生碰撞——这一非平衡状态直接影响注入能谱的形状，是 NLDSA 中"预加速 (pre-acceleration)"问题的底层。

[CRITIQUE] 作者对**注入**采取保守态度（"one of the most poorly known aspects"），未进一步展开 dust sputtering（Meyer, Ellison）在重核加速中的作用——这一点在 §4 讨论 subshock 结构时才有进一步处理。

---

## 3.2 Transport of charged particles in magnetic fields: basic concepts

[FACT] §3.2 讨论带电粒子在均匀 $B_0$ + Alfvén 波动背景下的运动学，为 §3.3 DSA 方程的推导提供散射截面与扩散系数。

[FACT] **Fermi 二阶加速**（随机加速，"second-order"）：平均能量增益 $\langle\Delta E/E\rangle = \frac{4}{3}(V/c)^2$，标度是 $(V/c)^2$。**ISM 中** Alfvén 速度 $v_A = B/\sqrt{4\pi\rho} = 2\, B_\mu \cdot n_{{\rm i},\rm cm^{-3}}$ km/s，太小——**二阶加速在 SNR 中不重要**，DSA 的关键是**一阶**（"first-order Fermi"）。

[FACT] 粒子在均匀 $B_0$ 中：Larmor 频率 $\Omega = qB_0/(mc\gamma)$，投掷角方向速度 $v_z = v\mu$，回旋半径 $r_L = v/\Omega$。在弱湍流 $B' \ll B_0$ 假设下，粒子沿磁力线做准直线运动，与 $B'$ 的碰撞导致**投掷角扩散（pitch-angle diffusion）**。

[FACT] **投掷角扩散系数**（Quasi-Linear Theory，Eq. 29–30）：

$$
\nu = \langle \Delta\theta\,\Delta\theta / \Delta t \rangle = \frac{\pi}{4}\, \frac{k P(k)}{B_0^2 / 8\pi}\, \Omega
$$

其中 $P(k)$ 为沿 $B_0$ 方向的 Alfvén 波动动量谱密度。

[FACT] **空间扩散系数**（Eq. 32）：

$$
D(p) \approx \frac{1}{3}\, \frac{r_L\, v}{F}, \qquad F \equiv \frac{k P(k)}{B_0^2 / 8\pi}
$$

[FACT] 观测约束：CR 在银河系被约束 $\sim 10^7$ yr → $D \sim 10^{29}$ cm$^2$/s → 共振尺度需 $\delta B / B_0 \sim 6\times10^{-4}$。这意味着**准线性理论（QLT，$F \ll 1$）** 在银河系大尺度输运上自洽——但在 SNR 加速前沿要求 $F \gg 1$（见 §3.4）。

[FACT] §3.2 还讨论了粒子**垂直于 $B$ 场**的输运，引入 **non-linear guiding center theory**（Jokipii & Parker 1969；Jokipii 1966）——这对 §6.4 SNR–MC 各向异性扩散的分析至关重要。

[CRITIQUE] §3.2 的 QLT 建立在 $B'/B_0 \ll 1$ 假设上，这在银河系传播尺度有效，但在 SNR 激波前沿（Bell 放大 $B'/B_0 \sim 10$–$100$）**完全失效**——这是 §4 非线性 DSA 的起点。

[CRITIQUE] 作者提到 perpendicular transport 与 non-linear guiding center theory 时仅做介绍，未展开其数学——这一点在 §6.4 分析 SNR–MC 各向异性扩散时才再次浮现。

**关键公式**：

$$
\boxed{D(p) \approx \frac{1}{3}\, \frac{r_L\, v}{F} \quad \text{(Eq. 32, QLT spatial diffusion)}}
$$

---

## 3.3 DSA through the transport equation

[FACT] §3.3 在 shock 静止、平行、定态的框架下，将 §3.2 的扩散系数代入传输方程，完成 DSA 谱指数的严格推导。参考 Skilling (1975a)。

[FACT] **压缩比**（Eq. 33）：

$$
r = \frac{u_1}{u_2} = \frac{4 M_s^2}{M_s^2 + 3} \xrightarrow{M_s \to \infty} 4
$$

[FACT] **DSA 传输方程**（Shock 静止系，Eq. 34）：

$$
u \frac{\partial f}{\partial z} = \frac{\partial}{\partial z}\left(D\frac{\partial f}{\partial z}\right) + \frac{1}{3}\frac{du}{dz}\, p\frac{\partial f}{\partial p} + Q
$$

三项依次为：粒子流守恒、空间扩散、对流-绝热动量变化（$\frac{1}{3}\nabla\cdot\mathbf{u}$ 效应）；$Q$ 为注入项。

[FACT] **注入项**（$\delta$ 函数近似，Eq. 35）：

$$
Q(p, x) = \eta\, n_1\, u_1 \,\frac{1}{4\pi\, p_{\rm inj}^2}\, \delta(p - p_{\rm inj})\, \delta(z)
$$

$\eta$ 为注入效率（injection efficiency），在 test-particle 极限下 $\eta \ll 1$。

[FACT] 关键结果（Eq. 40, 41）：

$$
f_0(p) = \frac{3r}{r-1}\, \eta\, n_1\, \frac{1}{4\pi\, p_{\rm inj}^2}\left(\frac{p}{p_{\rm inj}}\right)^{-\frac{3r}{r-1}}
$$

$$
\alpha \equiv \frac{3r}{r-1} \xrightarrow{M_s\to\infty} 4
$$

[FACT] Blasi 明确强调："The spectrum of accelerated particles is a **power law in momentum** (and not in energy, as is often assumed in the literature)." 因此相对论下（$p \propto E$）$n(\varepsilon) \propto \varepsilon^{-2}$；非相对论下（$p \propto \sqrt{\varepsilon}$）$n(\varepsilon) \propto \varepsilon^{-3/2}$。

[FACT] 第二个关键结论："The shape of the spectrum of the accelerated particles **does not depend upon the diffusion coefficient**." 谱指数完全由压缩比 $r$ 决定——DSA 的"招牌"结论。

[CRITIQUE] 谱形与 $D$ 无关是"good news"，但代价是**test-particle 理论不能内禀地给出 $p_{\rm max}$**——$p_{\rm max}$ 必须靠外部边界条件（时间、空间、几何）决定，见 §3.4。

[CRITIQUE] §3.3 推导假设 shock 静止、平行、定态——**倾斜激波**（oblique shock）会显著改变粒子返回概率，使谱硬化的方向依赖性（"injection fraction"）无法捕捉；该问题在 §4 NLDSA 中才得到部分处理。

**关键公式**：

$$
\boxed{\alpha = \frac{3r}{r-1} \quad \xrightarrow{r=4}\quad 4 \qquad \text{(DSA test-particle spectral index)}}
$$

---

## 3.4 Maximum energy: time versus space

[FACT] §3.4 讨论 SNR 激波能达到的**最大能量**。Blasi 明确指出定义存在**三种**（"At least three different definitions of the maximum energy should be considered"），且"which definition works the best or best describes reality"并不总清晰。

[FACT] **单次循环的能量增益**（Bell 1978a，Eq. 44，"first-order Fermi"）：

$$
\left\langle \frac{E'_1 - E_1}{E_1}\right\rangle_{\mu_1,\mu_2} = \frac{4}{3}\,\beta
$$

其中 $\beta = (u_1 - u_2)/c$。**标度为 $\beta^1$ → 一阶 Fermi**（对比 §3.2 中 $(V/c)^2$ 的二阶）。

[FACT] **加速时间**（Drury 1983；Lagage & Cesarsky 1983a,b，Eq. 47）：

$$
\tau_{\rm acc}(p) = \frac{3}{u_1 - u_2}\int_0^p \frac{dp'}{p'}\left[\frac{D_1(p')}{u_1} + \frac{D_2(p')}{u_2}\right]
$$

[FACT] **定义 1（时间约束，§3.4 主线）**：$\tau_{\rm acc}(p_{\rm max}) \leq \tau_{\rm SNR}$（对电子则用 SNR 年龄与同步/IC 损失时标的较小者）。推导给出（Eq. 48, 49）：

$$
F(k_{\rm min}) \approx \frac{1}{3}\,\frac{c}{V_s}\,\frac{r_L(p_{\rm max})}{R_{\rm SNR}}
$$

[FACT] **关键推论**：回旋半径参考值 $r_L(p_{\rm max}) = 1\,{\rm pc}\cdot (E/10^{15}\,{\rm eV})\cdot B_\mu^{-1}$（Eq. 50）。由于 $c/V_s \sim 100$ 而 $r_L/R_{\rm SNR} \sim 0.1$，**必须 $F(k_{\rm min}) \gg 1$**，即 $\delta B / B_0 \gg 1$——**磁场放大是 PeVatron 的必要条件**。

[FACT] Blasi 明确结论："Without such a mechanism ... the maximum energy that could be achieved at ~1000 years old SNR with $V_{\rm sh} = 3000$ km/s is only a fraction of GeV."

[FACT] **定义 2（空间约束）**：粒子扩散出去即泄漏，$D(p_{\rm max})/V_{\rm sh} \approx \chi\, R_{\rm sh}$（Eq. 51）；在 Sedov 阶段该约束**比时间约束更严**。

[FACT] **定义 3（几何约束）**：$r_L(p_{\rm max}) = R_{\rm sh}$，作为上界，会**高估 $p_{\rm max}$ 约 $c/V_{\rm sh}$ 因子**。

[CRITIQUE] §3.4 的核心论证是**"SNR 要达到 PeV 必须依赖磁场放大"**——这一步为下一章 §4 非线性理论埋下伏笔：test-particle 理论里 $F \ll 1$（QLT）的假设在 $p_{\rm max}$ 处失效，$\delta B \ll B_0$ 的准线性理论在最强散射点必然崩溃，必须让 CR 自激散射中心（self-generated turbulence）——这正是 §4 NLDSA 的起点。

[CRITIQUE] Test-particle 假设要求 $\xi_{\rm CR} \ll 1$，而 §2 推导出的 $\xi_{\rm CR} \sim 10\%$ 已接近上限——**这正是 §4 非线性理论出现的历史动因**。

[CRITIQUE] DSA 谱与 $D$ 无关，但 $p_{\rm max}$ 完全由 $D$ 决定——作者已指出这种**谱形与最大能量的解耦**：理论预测的谱斜率很干净，但最大能量完全由我们不知道的磁化放大机制决定。

[FACT] 文中未给出具体 SNR 上应用上述估计的案例——这一空缺在 §6.3（Tycho 案例）才被补齐。

**关键公式**：

$$
\boxed{F(k_{\rm min}) \approx \frac{1}{3}\,\frac{c}{V_s}\,\frac{r_L(p_{\rm max})}{R_{\rm SNR}} \quad \text{[PeVatron 必要条件]} \qquad \tau_{\rm acc} = \frac{3}{u_1-u_2}\int\!\frac{dp'}{p'}\!\left[\frac{D_1}{u_1}+\frac{D_2}{u_2}\right]}
$$

---

| 物理量 | 典型值 |
|--------|--------|
| $V_{\rm ej}$ | $\sim 10^{4}$ km/s |
| $M_s$ | $\sim 900$ |
| $R_{\rm ST}$ | $\sim 2$ pc |
| $T_{\rm ST}$ | $\sim 200$ yr |
| $\tau_{\rm eq,ee}$ | $\sim 10^{3}$ yr |
| $\tau_{\rm eq,pp}$ | $\sim 10^{6}$ yr |
| $kT_p$ | $5.6\times10^{8}\,(V_{\rm sh}/5000)^2$ K |
| $D(1\,{\rm GeV})$ | $\sim 10^{29}$ cm$^2$/s |
| $\delta B/B$（$10^{7}$ yr 约束） | $\sim 6\times10^{-4}$ |
| $r_L(10^{15}\,{\rm eV}, 1\mu{\rm G})$ | 1 pc |
| $c/V_s$ | $\sim 100$ |
| $r_L/R_{\rm SNR}$ | $\sim 0.1$（PeV 情形） |

## 图表分析

参见 `09_figures_tables.md`（Figure 4 SNR 形态：RX J1713.7-3946 与 Tycho；Figure 5 带电粒子在磁场中的轨迹；Figure 6 test-particle 加速示意）。

---

## 元数据

```yaml
chapter: 3
pages: "9–26"
subsections: ["3.1", "3.2", "3.3", "3.4"]
subsection_titles:
  - "Collisionless shocks"
  - "Transport of charged particles in magnetic fields: basic concepts"
  - "DSA through the transport equation"
  - "Maximum energy: time versus space"
key_formulas:
  - "D(p) ≈ (1/3) r_L v / F (Eq. 32, QLT)"
  - "α = 3r/(r-1) → 4 (Eq. 41, DSA test-particle)"
  - "τ_acc = 3/(u_1-u_2) ∫ dp'/p' [D_1/u_1 + D_2/u_2] (Eq. 47)"
  - "F(k_min) ≈ (1/3)(c/V_s)(r_L/R_SNR) (Eq. 48)"
keywords:
  - collisionless shock
  - Coulomb equilibration
  - quasi-linear theory (QLT)
  - pitch-angle diffusion
  - Skilling transport equation
  - test-particle DSA
  - α = 3r/(r-1)
  - maximum energy (time/space/geometric)
  - PeVatron
references_internal:
  prev_chapter: 02_sn_r_premises
  next_chapter: 04_nl_dsa
references_external:
  - "Treumann 2009 (collisionless shocks review)"
  - "Spitzer 1962 (Coulomb equilibration)"
  - "Skilling 1975a (transport equation)"
  - "Bell 1978a (single-cycle energy gain)"
  - "Drury 1983 (acceleration time)"
  - "Lagage & Cesarsky 1983a,b (acceleration time)"
  - "Spitkovsky 2008a,b; Sironi & Spitkovsky 2011; Gargaté & Spitkovsky 2012 (PIC injection)"
```

**引用页码**：本文 §3 覆盖 pp. 9–26，引用基于 *Space Science Reviews* 190 (2014) 365–464（arXiv:1311.7346v2, 9 Dec 2013）。