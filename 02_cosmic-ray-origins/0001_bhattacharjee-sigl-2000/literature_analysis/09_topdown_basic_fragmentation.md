---
chapter: 9
title: "Top-down Scenario — Basic Idea & Fragmentation"
pages: "48–58"
sections:
  - "6.1 The Basic Idea"
  - "6.2 From X Particles to Observable Particles: Hadron spectra in Quark–Hadron Fragmentation"
  - "6.3 Cosmic Topological Defects as Sources of X Particles: General Considerations"
related_chapters:
  prev: 08_acceleration_sources
  next: 10_cosmic_strings
status: done
---

> 本章属于：Bhattacharjee & Sigl (1999), *Phys. Rep.* 320, 1–150
>
> 上一章：`08_acceleration_sources.md`
>
> 下一章：`10_cosmic_strings.md`

# 9. Top-down Scenario: Basic Idea & Fragmentation (§6.1–6.3, p. 48–58)

[FACT] §6.1–6.3 覆盖 pp. 48–58，是全篇 top-down 场景的理论基座。§6.1 给出 top-down 的动机与三条必要条件；§6.2 系统导出 X 衰变到可观测粒子的 QCD 强子化链路（LPHD + MLLA）；§6.3 概括拓扑缺陷（TD）作为 X 源的分类与与暴胀的兼容性。

[INTERPRETATION] 这一节把整个 top-down 图景收敛到"三重约束 × 单注入谱"框架：**（a）近期衰变 / （b）$m_X \gg 10^{11}$ GeV / （c）足够衰变率** 决定可行性；**LPHD + MLLA** 决定注入谱形状 $dN_h/dx$；§6.3 决定 X 源的种类与产生机制。

---

## 6.1 The Basic Idea

[FACT] §6.1 建立 top-down 场景的动机与必要条件。

### 6.1.1 Top-down 动机

> **Top-down 场景的动机**

[FACT] DSAM 加速是**自限过程**：粒子回旋半径 $r_g = E/(ZeB) \leq R$（源尺寸） → $E_{\rm max} \sim ZeBR$。EHECR > $10^{11}$ GeV 要求 $R\cdot B$ 极大；实际还须考虑传播损失与源距离问题。

[FACT] **Top-down**：$X$ 粒子（$m_X > 10^{11}$ GeV）衰变 → 无需加速。**历史溯源**：Lemaître "Primeval Atom"（"the cosmic rays were glimpses of the primeval fireworks" [380]）。

### 6.1.2 Top-down 三条件

> **Top-down 的三条必要条件**

[FACT]
1. **(a) 近期衰变**：$X$ 在**近期宇宙学时代**衰变，或源距离 $\lesssim 100$ Mpc。例外：UHE $ν$ + RNB → $Z^{0}$ 共振（Z-burst，见 §5.2.4）。
2. **(b) $m_X \gg 10^{11}$ GeV**。
3. **(c) 数密度/衰变率** 足够大。

### 6.1.3 X 衰变链

> **X 粒子衰变链**

[FACT]

$$
X \to (\text{夸克, 轻子}) \to [\text{夸克强子化：jets of light mesons }(\pi)\text{ + baryons }N]
$$
$$
\to \pi^{0} \to 2\gamma,\qquad \pi^{\pm} \to \mu^{\pm}\,\nu_\mu \to (e^{\pm}) + \nu_{\rm e} + \bar\nu_\mu
$$

- **直接产生**：光子、中微子、带电轻子 + 少量核子。
- 核子占 hadron 总数 ~3–10% [FACT, collider 数据]。

**关键参数**：$m_X \gg 10^{11}$ GeV；核子占强子数 3–10%；源距离 $\lesssim 100$ Mpc 或近期衰变。

---

## 6.2 From X Particles to Observable Particles: Hadron spectra in Quark–Hadron Fragmentation

[FACT] §6.2 系统建立 X 粒子强子化到可观测粒子的理论链路。

### 6.2.1 Local Parton–Hadron Duality

> **局域部分子–强子对偶（LPHD）**

[FACT] **强子化三阶段**：
1. **Parton Cascade**（微扰 QCD，截止 $\langle k_\perp^{2}\rangle^{1/2}_{\rm cut-off} \sim 1$ GeV）
2. **Non-perturbative confinement**（LUND string [381] / cluster [382] 模型）
3. **Unstable hadron 衰变**

[FACT] **LPHD 核心假设**：非微扰强子化发生在 ~hadron mass 的低虚拟尺度，仅涉及低动量转移和局域色重排，**不显著改变 parton 谱形状**。强子化效应仅贡献整体归一化常数 $K(Y)$：

$$
x\,\frac{dN_h}{dx} = K(Y)\cdot x\,\frac{dN_{\rm part}}{dx}\;\;\text{(58)}
$$

[FACT] **MLLA 极限谱（公式 57）**：

$$
x\,\frac{dN_{\rm part}}{dx} = \frac{4C_F}{b}\,\Gamma(B)\int_{-\pi/2}^{\pi/2}\frac{d\ell}{\pi}\,e^{-B\alpha}\left[\frac{\cosh\alpha + (2\xi/Y-1)\sinh\alpha}{(4N_c/b)\,Y\,(\alpha/\sinh\alpha)}\right]^{B/2}\cdot I_B\!\left[\frac{16N_c}{bY}\frac{\alpha}{\sinh\alpha}(\cosh\alpha+(2\xi/Y-1)\sinh\alpha)\right]^{1/2}
$$

其中：$\xi = \ln(1/x)$, $Y = \ln(E_{\rm jet}/\Lambda_{\rm eff})$, $\alpha = \tanh^{-1}(1-2\xi/Y)+i\ell$；$B = a/b$, $a = 11N_c/3 + 2n_f/(3N_c^2)$, $b = (11N_c-2n_f)/3$；$N_c = 3$, $C_F = 4/3$, $I_B$ = 修正 Bessel 函数。

[FACT] **拟合参数**：$\Lambda_{\rm eff}^{\rm ch} \sim 250$ MeV（LEP $Z$-resonance, $E_{\rm cm} \sim 90$ GeV）；$K \sim 1.3$（LEP 能量）。

[FACT] **$\xi_{\rm max}$ 位置（公式 59）**：

$$
\xi_{\rm max} = Y\left[\frac{1}{2} + \sqrt{\frac{C}{Y} - \frac{C}{Y^2}}\right],\quad C = \frac{a^2}{16bN_c}
$$

- 该峰的存在直接关联 QCD 色相干效应导致的软胶子倍增抑制。LEP 数据确认 $\xi_{\rm max}$ 的 $Y$ 演化 [388]。

[FACT] **高能量极限下的高斯近似（公式 60）**：

$$
x\,\frac{dN_h}{dx} \propto \frac{1}{\sigma\sqrt{2\pi}}\exp\!\left[-\frac{(\xi-\xi_{\rm max})^{2}}{2\sigma^{2}}\right],\quad 2\sigma^{2} = \left(\frac{bY^{3}}{36N_c}\right)^{1/2}
$$

[FACT] **Hill 谱（公式 61, 62）**：

$$
\frac{dN_h}{dx} \simeq \frac{3}{2}\cdot 0.08\cdot\frac{\exp[2.6\,q\,\ln(1/x)]}{(1-x)^{2}\,(x/(q\ln(1/x)))^{-1}}\;\;\text{(61)}
$$
$$
\frac{dN_h}{dx} \simeq \frac{15}{16}\,x^{-3/2}\,(1-x)^{2}\;\;\text{(62)}
$$

- $n_f = 6$；3/2 因子包含中性 $\pi^{0}$。
- $x \ll 1$（EHE 能区）：(61) → **$dN_h/dE \propto E^{-1.3}$** ($α \sim 1.3$)；(62) → **$dN_h/dE \propto E^{-1.5}$** ($α \sim 1.5$)。

[FACT] **SUSY 对强子化的影响**：若 SUSY 在 $M_{\rm SUSY} \sim 1$ TeV "打开"：parton cascade 中 squarks/gluinos 与普通 quarks/gluons 等概率参与（$\tilde Q^{2} > M_{\rm SUSY}^{2}$）；一旦 $\tilde Q^{2} < M_{\rm SUSY}^{2}$，SUSY 粒子 decouple → 最终衰变为 LSP。**Berezinsky & Kachelriess [399]**：LSP 可能带走 ~40% 的 jet 总能量！SUSY MLLA 谱：$a \to a_{\rm SUSY} = 11N_c/3$；$b \to b_{\rm SUSY} = 9-n_f$ → $\xi_{\rm max}$ 移到更高 $\xi$（更低能量）。

[FACT] **硬 vs 软谱**：**$α = 2$ 是分界**——软谱 ($α > 2$)：粒子数与总能量均由低能端主导；**硬谱 ($1 < α < 2$)**：总能量由少数极高能粒子携带 → 更"自然"产生 EHECR。Top-down 一般 $α \sim 1.3\text{–}1.5$（硬）→ 预测 GZK 截断后有**"recovery"** [200]。硬谱也可能自然产生 "gap" [403]。

[CRITIQUE] LPHD + MLLA 仅在 ~100 GeV 被实验验证 → 外推到 > $10^{14}$ GeV 有**巨大不确定性**。Monte Carlo (HERWIG/JETSET) 与 MLLA+LPHD 在 $m_X \gg 10^{3}$ GeV 处显著不同 [391]。强子产额在 $x \sim 0.2\text{–}0.4$ 处反常高，与"介子主导"直觉矛盾（机制不明）。**Berezinsky & Kachelriess [399] 提出的 LSP 效应**（带走 40% 能量）对任何 TD 场景都是关键修正。

**关键公式**：

$$
\boxed{x\,\frac{dN_h}{dx} = K(Y)\cdot x\,\frac{dN_{\rm part}}{dx}\;(58),\quad \frac{dN_h}{dE}\propto E^{-1.3}\text{–}E^{-1.5}\;(61,62),\quad \xi_{\rm max} = Y\left[\tfrac12+\sqrt{C/Y-C/Y^2}\right]\;(59)}
$$

### 6.2.2 Nucleon, Photon and Neutrino Injection Spectra

> **核子、光子与中微子注入谱**

[FACT] 设 $X$ 平均衰变为 $\tilde N$ 体（$N_q$ 夸克 + $N_\ell$ 轻子），能量均分。

[FACT] **核子（公式 63）**：

$$
\Phi_{\rm N}(E_i,t_i) = \dot n_X(t_i)\cdot\frac{N_q\,f_N}{\tilde N}\cdot\frac{m_X}{x^{2}}\cdot\frac{dN_h}{dx},\quad x = \frac{\tilde N\,E_i}{m_X}
$$

[FACT] **光子（公式 64，$\pi^{0}\to 2\gamma$）**：

$$
\Phi_\gamma(E_i,t_i) \simeq 2\int_{E_i}^{m_X/\tilde N}\frac{dE}{E}\,\Phi_{\pi^{0}}(E,t_i),\qquad \Phi_{\pi^{0}} \simeq \frac{1}{3}\cdot\frac{(1-f_N)}{f_N}\cdot\Phi_{\rm N}
$$

[FACT] **中微子（公式 65，$\pi^{\pm}\to\mu^{\pm}\nu_\mu$）**：

$$
\Phi_{\nu_\mu+\bar\nu_\mu}(E_i) \simeq 2.34\int_{2.34\,E_i}^{m_X/\tilde N}\frac{dE}{E}\,\Phi_{\pi^{\pm}}(E,t_i),\qquad \Phi_{\pi^{\pm}} \simeq 2\,\Phi_{\pi^{0}}
$$

- 每个 $μ$ 衰变再产生 $ν_{\rm e}+\bar\nu_\mu$ → 每个 $\pi^{\pm}\to 3\,ν$。
- **总 $ν_\mu+\bar\nu_\mu \approx 2\times (65)$；总 $ν_{\rm e}+\bar\nu_{\rm e} \approx (65)$**。

[FACT] **相对丰度**（$f_N \sim 3\%$）：$\Phi_{\pi^{0}}/\Phi_{\rm N} \simeq 10$；$\Phi_{\pi^{\pm}}/\Phi_{\rm N} \sim 20$ → **光子与中微子在数上占主导**（至少 ×10 于核子）。

[FACT] **关键 Top-down 标志**：**$γ$/CR 通量比 > 1** 在足够高 EHECR 能区（§7 讨论）。

[FACT] **Top-down 与 Bottom-up 关键区别**：Top-down：$ν,γ$ 是**初级**产物（直接从 $π$ 衰变）。Bottom-up：$ν,γ$ 是**次级**（来自 GZK 相互作用产生的 $π$）。

**关键公式**：

$$
\boxed{\Phi_{\rm N} = \dot n_X\,\frac{N_q f_N}{\tilde N}\,\frac{m_X}{x^{2}}\frac{dN_h}{dx}\;(63),\quad \Phi_\gamma/\Phi_{\rm N}\sim 10,\quad \Phi_\nu/\Phi_{\rm N}\sim 20}
$$

### 6.2.3 X Particle Production/Decay Rate Required to Explain the Observed EHECR Flux: A Benchmark Calculation

> **X 粒子衰变率基准计算**

[FACT] **单 X 粒子光子注入谱（公式 66）**：假设 $X\to q\ell$（2-body），$dN_\gamma/dE_\gamma \propto E_\gamma^{-\alpha}$，$0<\alpha<2$：

$$
\frac{dN_\gamma}{dE_\gamma} = 0.6\,\frac{m_X}{2-\alpha}\cdot\frac{f_\pi}{0.9}\cdot\left(\frac{2E_\gamma}{m_X}\right)^{-\alpha}
$$

[FACT] **光子通量（公式 67）**：

$$
j_\gamma(E_\gamma) \simeq \frac{1}{4\pi\,l(E_\gamma)}\,\dot n_X\,\frac{dN_\gamma}{dE_\gamma}
$$

[FACT] **X 粒子衰变率要求（公式 68）**：

$$
(\dot n_{X,0})_{\rm EHECR} \simeq 1.2\times10^{-46}\left(\frac{l(E_\gamma)}{10\,{\rm Mpc}}\right)^{-1}\!\left(\frac{E^{2}j(E)}{1\,{\rm eV\,cm^{-2}s^{-1}sr^{-1}}}\right)\!\left(\frac{2E}{10^{16}\,{\rm GeV}}\right)^{\alpha-1.5}\!\left(\frac{m_X}{10^{16}\,{\rm GeV}}\right)^{1-\alpha}\!\frac{0.5}{2-\alpha}\,\frac{0.9}{f_\pi}\;{\rm cm^{-3}s^{-1}}
$$

[FACT] **能量注入率（公式 69）**：

$$
(Q_0)_{\rm EHECR} \simeq 1.2\times10^{-21}\left(\frac{l(E_\gamma)}{10\,{\rm Mpc}}\right)^{-1}\!\left(\frac{E^{2}j(E)}{1\,{\rm eV\,cm^{-2}s^{-1}sr^{-1}}}\right)\!\left(\frac{2E}{10^{16}\,{\rm GeV}}\right)^{\alpha-1.5}\!\left(\frac{m_X}{10^{16}\,{\rm GeV}}\right)^{2-\alpha}\!\frac{0.5}{2-\alpha}\,\frac{0.9}{f_\pi}\;{\rm eV\,cm^{-3}s^{-1}}
$$

[FACT] **数值示例**（$E^{2}j \sim 1$ eV cm$^{-2}$ s$^{-1}$ sr$^{-1}$ at $E=10^{11}$ GeV, $m_X=10^{16}$ GeV, $\alpha=1.5$, $f_\pi=0.9$）：

$$
\dot n_X \simeq 1\times10^{35}\,{\rm Mpc^{-3}yr^{-1}} \simeq 13\,{\rm AU^{-3}yr^{-1}}
$$

即 **每 10 Mpc 半径体积内，每年 ~10 个 X 粒子衰变**（每个太阳系大小）。作者承认：可能高估一个量级 [206]。

**关键公式**：

$$
\boxed{\dot n_{X,0}\!\simeq\!1.2\!\times\!10^{-46}\!\left(\frac{m_X}{10^{16}{\rm GeV}}\right)^{1-\alpha}{\rm cm^{-3}s^{-1}}\;(68),\quad \dot n_X\!\sim\!10^{35}{\rm Mpc^{-3}yr^{-1}}\;(m_X\!=\!10^{16}{\rm GeV})}
$$

---

## 6.3 Cosmic Topological Defects as Sources of X Particles: General Considerations

[FACT] §6.3 概括拓扑缺陷作为 X 源的类型学与物理背景。

### 6.3.1 TD 分类与质量标度

> **拓扑缺陷分类与质量标度**

[FACT] **TD 分类**：magnetic monopoles / cosmic strings / domain walls / superconducting cosmic strings / 混合系统 (necklaces 等)。产生于 GUT 相变；核心尺寸 $\sim \eta^{-1}$（$\eta$ 为 Higgs VEV）。

[FACT] **TD 质量标度**：

| TD 类型 | 质量标度 |
|---|---|
| Monopole | $\sim T_c \sim \eta$ |
| Cosmic string 线质量 $\mu$ | $\sim \eta^{2}$ |
| Domain wall 面密度 | $\sim \eta^{3}$ |

若 GUT 破缺：$\eta \sim 10^{16}$ GeV → $m_X \sim 10^{16}$ GeV。

### 6.3.2 与暴胀的兼容性

> **拓扑缺陷与暴胀的兼容性**

[FACT] 暴胀稀释了早期 TD → 看似矛盾。但 **preheating 非热相变** [412,413] 可在暴胀后产生 TD：inflaton 振荡通过 parametric resonance → 大场涨落 → 对称性恢复 → 再对称破缺 → TD 形成。

[FACT] **实验室验证**：$^{3}{\rm He}$ 超流相变中的 vortex-filament 形成（毫开尔文温度）→ Kibble-Zurek 机制的确认 [409]。

### 6.3.3 历史时间线

> **Top-down / TD 场景历史时间线**

| 时间 | 事件 |
|---|---|
| 1982 | Callan [414]: 弦环坍缩产生 $X$；Rubakov [415]: 单极子湮灭 → baryon asymmetry |
| 1983 | Hill [392]: monopolonium 衰变 → 高能粒子 |
| 1984 | Schramm & Hill [404]: 这些高能粒子即 EHECR |
| 1985 | Witten [420]: superconducting string |
| 1986 | OTW [421], HSW [393]: SCS 载流子发射 → UHECR |
| ~1986 | 弦 cusp evaporation [394,395], 环坍缩 [397,396] |
| 1990s | [200] 一般参数化 [178] $γ$/CR 标志 |

**关键参数**：$m_X \gg 10^{11}$ GeV；$\eta \sim 10^{16}$ GeV (GUT)；$\dot n_X \sim 10^{35}$ Mpc$^{-3}$ yr$^{-1}$；$α \sim 1.3\text{–}1.5$；SUSY LSP 能量份额 ~40%。

---

## 元数据

```yaml
chapter: 9
pages: "48–58"
subsections: ["6.1.1", "6.1.2", "6.1.3", "6.2.1", "6.2.2", "6.2.3", "6.3.1", "6.3.2", "6.3.3"]
key_formulas:
  - "x dN_h/dx = K(Y) · x dN_part/dx (Eq. 58, LPHD)"
  - "dN_h/dE ∝ E^{-1.3}–E^{-1.5} (Eq. 61,62, Hill)"
  - "Φ_N = ṅ_X (N_q f_N/Ñ) (m_X/x²) (dN_h/dx) (Eq. 63)"
  - "ṅ_X,0 ∝ (m_X/10¹⁶ GeV)^{1-α} cm⁻³s⁻¹ (Eq. 68)"
  - "TD mass scale: η, η², η³ (monopole, string, domain wall)"
keywords:
  - top-down scenario
  - Local Parton-Hadron Duality
  - MLLA
  - Hill spectrum
  - SUSY LSP
  - topological defects
references_internal:
  prev_chapter: 08_acceleration_sources
  next_chapter: 10_cosmic_strings
```

**引用页码**：全文引用基于 *Phys. Rep.* 320 (1999), pp. 48–58。