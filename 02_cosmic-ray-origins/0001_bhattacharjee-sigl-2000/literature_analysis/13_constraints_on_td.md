---
chapter: 13
title: "Observational Constraints on the Top-Down Scenario"
pages: "83–92"
sections:
  - "7.1 Low-Energy Diffuse γ-ray Background: Role of Extragalactic Magnetic Field and Cosmic Infrared Background"
  - "7.2 Constraints from Primordial Nucleosynthesis"
  - "7.3 Constraints from Distortions of the Cosmic Microwave Background"
  - "7.4 Constraints on Neutrino Fluxes"
related_chapters:
  prev: 12_xparticles_special_models
  next: 14_conclusion_and_references
status: done
---

> 本章属于：Bhattacharjee & Sigl (1999), *Phys. Rep.* 320, 1–150
>
> 上一章：`12_xparticles_special_models.md`
>
> 下一章：`14_conclusion_and_references.md`

# 13. Observational Constraints on the Top-Down Scenario (§7, p. 83–92)

[FACT] §7 覆盖 pp. 83–92，是全篇 top-down 场景的**观测审判庭**。四道核心约束：低能弥漫 $γ$-ray 背景（§7.1）、原初核合成 / 光致分解（§7.2）、CMB 谱畸变（§7.3）、弥漫中微子通量（§7.4）。

[INTERPRETATION] §7 的核心判据是**参数 $p$**（§6.9）：$p<1$ 场景（最简单 SCS 模型）被**完全排除**；$p=1$ 场景（普通弦、monopolonium、necklaces）受 $m_X$ 与幂律指数 $q$ 限制；$p=2$ 场景（MSRP / 均匀河外衰变）**几乎不受约束**。

---

## 7.1 Low-Energy Diffuse γ-ray Background: Role of Extragalactic Magnetic Field and Cosmic Infrared Background

[FACT] §7.1 是全文最长的约束章节，讨论 EM 级联饱和谱、EGRET 上限、EGMF 对级联的抑制、以及 Table 1 中的 viable $p=1$ 参数空间。

### 7.1.1 饱和级联谱 (公式 98)

> **饱和级联谱**

[FACT] 假设仅 CMB 为级联背景（公式 98）：

$$
j_{\gamma^{\rm cas}}(E) \simeq \frac{\omega_{\rm cas}}{E^{2}\,x\,(2+\ln(E_c/E_x))}\times\left\{\begin{array}{ll}
(E/E_x)^{-1.5} & E<E_x\\
(E/E_x)^{-2} & E_x<E<E_c\\
0 & E>E_c
\end{array}\right.
$$

**红移依赖特征能量（公式 99）**：

$$
E_c \simeq \frac{m_e^{2}}{2\cdot 2\,T_{\rm CMB}}\simeq\frac{4.9\times10^{4}\,{\rm GeV}}{(1+z)},\qquad E_x \simeq 0.04\,E_c \simeq\frac{2\times10^{3}\,{\rm GeV}}{(1+z)}
$$

- $T_{\rm CMB}\simeq 2.735(1+z)$ K。
- $E_c \sim 100$ TeV 处**谱变陡至 $E^{-5}$**（光子-光子散射主导 [189]），但仅在 $z > \sim 100$ 时重要 → **对可行 TD 场景无关**（大多数级联通量产生于更低红移）。

### 7.1.2 IR/O 背景修正

> **IR/O 背景修正**

[FACT] 近似乘以 $\exp[-\tau(E)]$（$\tau$ 为 $E$ 处对 IR/O 背景的配对光学深度）。对 IR/O 背景模型的细节**不敏感** [487]。

### 7.1.3 100 MeV–100 GeV 约束

> **EGRET 约束**

[FACT] **EGRET 观测** [185]：30 MeV – 100 GeV 弥漫 $γ$ 谱 ~ $E^{-2.1}$ → **最严约束在最高能端**。约束：总注入并级联到更低的能量密度 $\omega_{\rm cas}\simeq 4.5\times10^{-6}$ eV cm$^{-3}$。

### 7.1.4 对 TD 模型的 p 值约束

> **$p$ 值对 TD 的约束**

| $p$ 值 | 约束 |
|---|---|
| $p=0$（最简单 SCS 模型） | **完全排除** [437] |
| $p=1$（普通弦、monopole 湮灭） | 幂律指数必须满足 |

[FACT] **$p=1$ 时的 $q$ 约束（公式 101）**：

$$
q \gtrsim 2 - \frac{3/2}{3 + \log_{10}(m_X/10^{23}\,{\rm eV})}
$$

- 例：$m_X=10^{16}$ GeV → $q\gtrsim 1.7$。

### 7.1.5 详细数值计算（含 IR/O + EGMF）

> **含 EGMF 与 IR/O 的详细级联计算**

[FACT] 基于新 IR 背景估计 [163] + 最强 URB 版本 [175]。

[FACT] **无 EGMF**（Fig. 28）：预言 $γ$ 通量在 ~100 TeV 被 CMB 上的 PP 耗竭，100 GeV–100 TeV 被 IR/O 上 PP 耗竭并级联到低能。

[FACT] **EGMF ~ $10^{-9}$ G**（Fig. 29）：
- 强同步冷却快速移走低能级联对 → UHE $γ$ 通量大幅降低。
- 但对 $m_X\gtrsim 10^{25}$ eV，pair 同步辐射可能 $>10^{20}$ eV → UHE 通量不一定低。
- EGRET 约束对 EGMF 强弱**不敏感**（只要核子通量与 $γ$ 通量量级相当）。

### 7.1.6 UHE 能区预言

> **UHE 能区 $γ$ 通量预言**

[FACT]
- **无 EGMF**：$γ$/CR 通量比 @ $10^{19}$ eV $\simeq 0.1$。
- **EGMF > $10^{-11}$ G**：抑制级联 → $γ$ 谱降低。
- **EGMF = $10^{-9}$ G**：$γ$/CR $\simeq 0.02$。
- **探测需求**：$E^{2}j \sim 0.1\times$ EHECR 在 $10^{19}$ eV → 需要 $\sim 4\times10^{19}$ cm$^{2}$ s sr 曝光 → **Auger 可达**（可探测中性组分至 ~1% 通量）。

### 7.1.7 河外 vs 银河贡献

> **河外 vs 银河 $γ$ 贡献**

[FACT] **弥漫 $γ$ 中可能大量来自银河 halo** [488]（尤其 ~1 GeV）→ 河外真实贡献可能显著更小 → **约束更严 ~2–3×**。河外 $γ$ 可能主要来自**未分辨 blazars** [489]（部分争议 [490]，分析仅 ~25% 来自未分辨 blazar [491]）。> 10 GeV 可能有额外未解释成分 → **~100 GeV 以上重粒子衰变级联**可拟合 [418]。

### 7.1.8 Clustered TD 绕过 γ 约束

> **聚类 TD 如何绕过 $γ$ 约束**

[FACT] 若 TD 或长寿命 $X$ **在星系内聚类**（非均匀分布）→ **无级联** → 绕过弥漫 $γ$ 约束。例见 §6.13 MSRP GHXPD 场景。

### 7.1.9 Synchrotron 附加成分

> **Dubovsky–Tinyakov 同步辐射附加成分**

[FACT] **Dubovsky-Tinyakov** [492]：银河磁场中的 cascade 电子同步辐射 → 在 ~$10^{15}$ eV 附近产生额外 $γ$ 通量。对 TD 模型：预言接近 **CASA-MIA 上界** [258]。**注意**：此成分非 TD 独有信号（任何 >100 TeV 源都产生类似成分）。

### 7.1.10 $Q_0$ 总注入率上限

> **总能量注入率上限**

[FACT] 归一化到 EHECR 通量 → $Q_0^{\rm EHECR}\lesssim 10^{-22}$ eV cm$^{-3}$ s$^{-1}$（在 few 因子内）。EGRET 对 $\omega_{\rm cas}$ 给出 **$Q_0^{\rm EM}\lesssim 2.2\times10^{-23}\,h(3p-1)$ eV cm$^{-3}$ s$^{-1}$**。

[FACT] 对宇宙弦（若能量主要以 $X$ 发射损失）：$\eta\sim m_X\lesssim 10^{13}$ GeV [418, 298]。**SUSY GUT 中 $X$ 质量 $<10^{16}$ GeV 不受欢迎**（质子衰变约束）[494, 495] — 但若 TD 在 GUT 后相变中形成，则不受质子衰变约束 → $m_X<10^{16}$ GeV 可行。

### 7.1.11 Table 1（部分 viable $p=1$ 场景）

> **部分可行的 $p=1$ 参数空间 (Table 1)**

| $m_X$ (GeV) | URB | EGMF | FF | $f_N$ | Mode | $Q_0$ | < GZK | > GZK |
|---|---|---|---|---|---|---|---|---|
| $10^{13}$ | high | any | no-SUSY | 10% | $qq$ | 1.4 | N | $<10^{-11}$ |
| $10^{13}$ | high | $<10^{-11}$ | no-SUSY | 10% | $qq$ | 1.4 | N | <10% |
| $10^{13}$ | high | $<10^{-11}$ | no-SUSY | 10% | $ql$ | 0.88 | N | $γ$ |
| $10^{13}$ | any | $<10^{-11}$ | no-SUSY | <10% | $ql$ | 0.93 | $γ$ | $γ$ |
| $10^{14}$ | high | any | no-SUSY | 10% | $qq$ | 1.3 | N | $γ$+N |
| $10^{15}$ | any | any | any | 10% | $qq$,$ql$,$qν$ | 1.3 | $γ$ | $γ$ |
| $10^{16}$ | high | any | SUSY | 10% | $qq$ | 1.6 | N | $γ$+N |
| $10^{16}$ | high | $<10^{-9}$ | no-SUSY | 10% | $qq$ | 1.3 | $γ$,N | $γ$,$γ$+N |
| $10^{16}$ | any | $<10^{-11}$ | any | <10% | $qq$,$ql$,$qν$ | 1.9 | <med | $<10^{-11}$ |

- a: GeV. b: Gauss. c: 最大总能量注入率（$10^{-23}\,h$ eV cm$^{-3}$ s$^{-1}$ 单位）。
- d: GZK 上下通量主导成分。
- e: 对 eV 质量 $ν$ 要求 $f_ν l_ν > $ 给定值（高 URB, 无 EGMF）。
- f: EGMF $> \sim 10^{-10}$ G.
- g: EGMF $> \sim 10^{-9}$ G.

[FACT] **关键**：**存在 viable TD 场景预言核子通量可比 $γ$ 通量高**（即使 $γ$ 在产生时主导）→ 发生在**高 URB + 强 EGMF + 核子碎裂分数 ~10%** 情况下（例 Fig. 29）→ 这些场景即使 EHECR EAS 与光子初級粒子不一致仍可存活。

**关键公式**：

$$
\boxed{j_{\gamma^{\rm cas}}\simeq\frac{\omega_{\rm cas}}{E^2 x(2+\ln(E_c/E_x))}(\text{阶梯谱})\;(98),\quad E_c\simeq 4.9\times10^{4}(1+z)^{-1}\,{\rm GeV}\;(99),\quad Q_0^{\rm EM}\lesssim 2.2\times10^{-23}h(3p-1)}
$$

---

## 7.2 Constraints from Primordial Nucleosynthesis

### 7.2.1 机制与阈值

> **原初核合成机制**

[FACT] **$z>\sim 10^{3}$** 时宇宙对级联光子**不透明** [485]。级联光子存活 ~$l_E(E)$ 时间 → 有一定概率**光致分解 $^4$He**。阈值：$E_{4{\rm He}}^{\rm th}=19.8$ MeV → $z<\sim 3\times10^{6}$ 时级联光子可分解 $^4$He。

### 7.2.2 产生率与关键不等式

> **级联核合成产生率与约束**

[FACT] **公式 102**：

$$
n_D/{}^{3}{\rm He}\simeq \frac{Y}{4}\,n_B\int dE\,l_E(E)\,4\pi\,j_{\gamma^{\rm cas}}(E)\,\sigma_{\rm eff}^{D/{}^{3}{\rm He}}(E)
$$

[FACT] **关键不等式**：观测光致分解截面立即给出（公式 103）：

$$
(^{3}{\rm He}/D)_{\rm photo} > \sim 8
$$

- **级联核合成预言 $^3$He $\gg$ D** → 与观测 $(^{3}{\rm He}/D)_\odot < \sim 1.13$ [496] 矛盾。
- **$^4$He 光致分解不可能成为 D 和 $^3$He 的主要来源** [437]（公式 104）：

$$
(^{3}{\rm He}+D)/H)_{\rm photo} < \sim 5\times10^{-5}
$$

### 7.2.3 转化为 TD 约束

> **原初核合成对 TD 的约束**

[FACT] 约束 $3\times10^{6}\gtrsim z\gtrsim 10^{3}$ 时**最大瞬时 EM 能量释放**。Fig. 27 显示允许的 $\omega_{\rm cas}(z)$ 上限。

[FACT] **结论**：原初核合成对 TD 的约束与 §7.1 $γ$ 背景约束**可比但独立** [437]。

**关键参数**：$E_{4{\rm He}}^{\rm th}=19.8$ MeV → $z<3\times10^{6}$；$(^3{\rm He}+D)/H)_{\rm photo} < 5\times10^{-5}$。

---

## 7.3 Constraints from Distortions of the Cosmic Microwave Background

### 7.3.1 两个红移区间

> **CMB 谱畸变的两个红移区间**

[FACT] **区间 1：$z_{\rm th}\simeq 3\times10^{6} > z > z_\gamma\simeq 10^{5}$**

分数能量释放 $\Delta u/u$ → **Bose-Einstein 谱**，化学势（$\mu$ 畸变）：

$$
\mu \simeq 0.71\,\Delta u/u
$$

- 适用于 Klein-Nishina cascade（GUT 粒子衰变产生的光子谱近似），光子数变化可忽略。

[FACT] **区间 2：$z_\gamma > z > z_{\rm rec}\simeq 10^{3}$**

**Sunyaev-Zel'dovich 型畸变**（$y$ 畸变）：

$$
4y = \Delta u/u
$$

### 7.3.2 观测限制与对 TD 的约束

> **CMB 畸变的观测限制与 TD 约束**

[FACT] COBE-FIRAS 给出 $\mu$ 与 $y$ 的上限。转化为**瞬时能量释放**上限（图 27 虚线）。比级联核合成和 $γ$ 背景约束**更弱**，但仍足以**排除最简单 SCS 模型**（$p=0$）。

**关键公式**：

$$
\boxed{\mu\simeq 0.71\,\Delta u/u\;(z_{\rm th}>z>z_\gamma),\quad 4y=\Delta u/u\;(z_\gamma>z>z_{\rm rec})}
$$

---

## 7.4 Constraints on Neutrino Fluxes

[FACT] §7.4 讨论 TD 场景预言的弥漫 $ν$ 通量、与实验上界的关系，以及不同 TD 模型的对比。

### 7.4.1 TD 中微子通量特征

> **TD 中微子通量特征**

[FACT] $X$ 衰变为夸克+轻子 → 夸克强子化主要为 $π$ → **$ν$ vs EM 能量比 $r\simeq 0.3$**。**$ν$ 通量计算**：[195] 形状；[394] 绝对通量（cusp evaporation）；[200] 所有场景（含 $ν$ 级联）；[196] 改进（含 RNB 上 $ν$ 级联）。**重要**：早期计算 [200, 196] 未包含 §7.1–7.3 宇宙学约束。

### 7.4.2 与 AGASA 数据的关联

> **与 AGASA 数据的关联**

[FACT] **AGASA 数据显示无 GZK cutoff** [82] → 可能支持 MSRP halo 场景。但 AGASA 数据也兼容 $p=1$ 的**均匀河外 TD 场景**。

### 7.4.3 BHS0、BHS1 与 SLBY98 对比

> **不同 TD 模型的 $ν$ 通量对比**

| 模型 | $p$ | 特点 |
|---|---|---|
| BHS0 | 0 | 已被 §7.1–7.3 排除，也被 UHE $ν$ 实验排除 |
| BHS1 | 1 | 归一化到 $E\sim 4\times10^{19}$ eV 质子通量 |
| SLBY98 | 1 | 归一化到可见（核子+$γ$）总通量 |

- SLBY98 的 UHE $ν$（> $10^{20}$ eV）比 BHS1 **小 ~100×**：
  1. BHS1 归一化到质子；SLBY98 归一化到核子+$γ$。
  2. BHS1 $f_N$ 小 ~3×。
  3. BHS1 用旧 fragmentation 函数 (61)（更高能端更多能量）。

### 7.4.4 实验限制

> **弥漫 $ν$ 的实验限制**

| 实验 | 限制 |
|---|---|
| Frejus [501] | $E>10^{12}$ eV 水平 $μ$（能量损失 > 140 MeV/辐射长度） |
| EAS-TOP [502] | $10^{14}$–$10^{15}$ eV（非共振）；Glashow 共振（仅 $\barν_e$） |
| Fly's Eye [503] | $10^{17}$ – $10^{20}$ eV（深层穿透粒子） |
| AKENO [504] | 近水平 $μ$-poor 簇射 |
| Goldstone [109] | 月球中 $ν$ 激发 pulsed radio emission → 与 Fly's Eye 相当 |

### 7.4.5 SLBY98 可探测性与探测器灵敏度

> **SLBY98 可探测性与探测器灵敏度**

[FACT] 1 km$^{3}\times 2\pi$ sr 探测器：$ν_\mu > 10^{19}$ eV → **~0.15 yr$^{-1}$**；$ν_{\rm e}>10^{19}$ eV → ~0.089 yr$^{-1}$；$ν_\mu > 1$ PeV → ~1.2 yr$^{-1}$。**$τ$ 中微子再生** [223] 消除地球遮挡 → 向上通量增加 [221]。

| 探测器 | 接受度 $A(E)$ |
|---|---|
| HiRes ($μ$-$ν$, >$10^{19}$ eV) | ~3 km$^{3}\times 2\pi$ sr [84] |
| Auger ground array ($10^{19}$ eV) | ~20 km$^{3}$ sr |
| Auger ground array ($10^{23}$ eV) | ~200 km$^{3}$ sr |
| OWL 卫星 | $\sim 6\times10^{4}$ km$^{3}$ sr (> $10^{20}$ eV), duty cycle 0.08 [87] |
| Goldstone 100 天搜索 | > $10^{19}$ eV 达到 Auger 灵敏度 [109] |

- **探测 TD $ν$ 通量需要**：$A > \sim 10$ km$^{3}\times 2\pi$ sr 运行数年。
- **Auger 与 OWL 应能探测典型 TD $ν$ 通量**。

### 7.4.6 模型无关上限

> **模型无关 $ν$ 通量上限**

[FACT] 设 $ν$/EM 能量比 $r$ 为常数：Cascade 效应将大部分 EM 注入能量再循环为 ~10 GeV 峰值光子。要求：**$\max_E[E^{2}j_{\nu_\mu}(E)]\simeq r\cdot\max_E[E^{2}j_\gamma(E)]$**。用 10 GeV $γ$ 通量上界 →（公式 105）：

$$
R(E) \lesssim 0.34\,r\cdot\left[\frac{A(E)}{1\,{\rm km^{3}}\times 2\pi\,{\rm sr}}\right]\left(\frac{E}{10^{19}\,{\rm eV}}\right)^{-0.6}\,{\rm yr^{-1}}\;\;\text{(105)}
$$

- 对 $r\lesssim 20\,(E/10^{19}\,{\rm eV})^{0.1}$ 与现有 $ν$ 通量限制一致。
- **TD 不受 Waxman-Bahcall bound 约束**（核子不是 $γ$/$ν$ 的初级产物）。

### 7.4.7 $r\gg 1$ 情形与瞬态信号

> **$r\gg 1$ 情形与瞬态信号**

[FACT] 如 $X$ 只衰变为 $ν$ [206]（多数模型不自然）。或**镜像 sector (mirror) TD** 辐射 hidden neutrino [507] → 中微子可最大振荡为普通 $ν$ → 产生可观事件率。**探测** → 建立 $r$ 的**实验下限**。

[FACT] **瞬态信号** [81, 508]：AGASA > $4\times10^{19}$ eV 观测到的可能**关联** [81] 暗示 $t_b \ll 1$ yr 的**爆发源**。脉冲 fluence：~$r\,[A(E)/(1\,{\rm km^{3}}\times 2\pi\,{\rm sr})]\,(E/10^{19}\,{\rm eV})^{-0.6}$ $ν$ 在 $t_b$ 时间内。若 EGMF $\lesssim 10^{-15}$ G → GeV–TeV $γ$ 通量也有关联脉冲 [508]。

### 7.4.8 MSRP 的中微子特征

> **MSRP 的中微子特征**

[FACT] MSRP 场景中 $ν$ 通量与 UHE photon + nucleon 通量**量级相当**（不是更大）— $ν$ 通量主导于河外（因 halo 不增强 $ν$）→ **极难探测**，即使下一代实验。

**关键参数**：$\omega_{\rm cas}\lesssim 4.5\times10^{-6}$ eV cm$^{-3}$；$E_c=4.9\times10^{4}(1+z)^{-1}$ GeV；$ν$/EM 能量比 $r\sim 0.3$；模型无关率上限 $R\lesssim 0.34\,r\,[A/(1\,{\rm km^{3}}\times 2\pi\,{\rm sr})]\,(E/10^{19}\,{\rm eV})^{-0.6}$ yr$^{-1}$。

---

## 元数据

```yaml
chapter: 13
pages: "83–92"
subsections: ["7.1.1", "7.1.2", "7.1.3", "7.1.4", "7.1.5", "7.1.6", "7.1.7", "7.1.8", "7.1.9", "7.1.10", "7.1.11", "7.2.1", "7.2.2", "7.2.3", "7.3.1", "7.3.2", "7.4.1", "7.4.2", "7.4.3", "7.4.4", "7.4.5", "7.4.6", "7.4.7", "7.4.8"]
key_formulas:
  - "j_{γ^cas} ≃ ω_cas / [E$^{2}$ x (2+ln(E_c/E_x))] × step (Eq. 98)"
  - "E_c ≃ 4.9×10$^{4}$ (1+z)$^{-1}$ GeV (Eq. 99)"
  - "μ ≃ 0.71 Δu/u; 4y = Δu/u"
  - "R(E) ≲ 0.34 r [A/(1 km$^{3}$×2π sr)] (E/10$^{19}$ eV)$^{-0.6}$ yr$^{-1}$ (Eq. 105)"
keywords:
  - diffuse γ-ray background
  - EGRET constraint
  - cascading nucleosynthesis
  - CMB μ distortion
  - CMB y distortion
  - Waxman-Bahcall
  - SLBY98
  - neutrino flux
references_internal:
  prev_chapter: 12_xparticles_special_models
  next_chapter: 14_conclusion_and_references
```

**引用页码**：全文引用基于 *Phys. Rep.* 320 (1999), pp. 83–92。