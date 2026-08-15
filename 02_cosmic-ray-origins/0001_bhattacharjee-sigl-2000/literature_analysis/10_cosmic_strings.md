---
chapter: 10
title: "Cosmic Strings as X-Particle Sources"
pages: "59–72"
sections:
  - "6.4.1 Evolution of Cosmic Strings"
  - "6.4.2 Intercommuting of Long Strings"
  - "6.4.3 Final Stage of Loop Shrinkage"
  - "6.4.4 Cusp Evaporation"
  - "6.4.5 Collapse or Repeated Self-intersections of Closed Loops"
  - "6.4.6 Direct Emission of X Particles from Cosmic Strings"
  - "6.5 X Particles from Superconducting Cosmic Strings"
related_chapters:
  prev: 09_topdown_basic_fragmentation
  next: 11_monopoles_vortons_necklaces
status: done
---

> 本章属于：Bhattacharjee & Sigl (1999), *Phys. Rep.* 320, 1–150
>
> 上一章：`09_topdown_basic_fragmentation.md`
>
> 下一章：`11_monopoles_vortons_necklaces.md`

# 10. Cosmic Strings as X-Particle Sources (§6.4–6.5, p. 59–72)

[FACT] §6.4–6.5 覆盖 pp. 59–72，是全篇 TD 场景中讨论最详尽的一节：系统梳理了 cosmic string 产生 X 粒子的五种机制（intercommuting / final-stage loop shrinkage / cusp evaporation / collapse & repeated self-intersections / direct emission），最后给出 superconducting cosmic strings (SCS) 的场景。

[INTERPRETATION] §6.4 的核心结论是：**GUT-scale 弦在多数机制下 X 产额不足**，但**轻弦（$\eta \sim 10^{13}\text{–}10^{14}$ GeV）通过 loop 碎裂过程可自然产生足够 X 粒子**，同时绕过 $γ$ 背景约束。**SCS**（§6.5）则因演化不确定性与 $p<1$ 时间依赖，成为**最被约束的 TD 候选**。

---

## 6.4 X Particle Production from Cosmic Strings

### 6.4.1 Evolution of Cosmic Strings

> **宇宙弦演化**

[FACT] **演化阶段**：
1. **形成后**：随机缠绕网络。
2. **摩擦主导期**（$T > (G\mu)^{1/2}\eta$）：弯曲弦段达终端速度 $\propto 1/r$；弦被拉直、长度缩短 → $\xi_{\rm s}$ 增加 → $\rho_{\rm s}$ 下降。
3. **相对论期**：摩擦可忽略。
   - 情形(a) **Scaling 解**：$\xi_{\rm s}/t = \rm const$ → $\rho_{\rm s,scaling} \propto 1/t^{2}$
   - 情形(b) $\xi_{\rm s}$ 增长慢于 $t$ → 弦过早主导宇宙（被排除）。

[FACT] **Scaling 能量损失**：

$$
\dot\rho_{s,{\rm total}} = -2(\dot R/R)\,\rho_{\rm s} + \dot\rho_{s,{\rm loss}}\;\;\text{(71)}
$$

- 辐射主导：$\dot\rho_{s,{\rm loss}} = -\rho_{\rm s}/t$
- 物质主导：$\dot\rho_{s,{\rm loss}} = -(2/3)\,\rho_{\rm s}/t$

[FACT] **环形成与小尺度结构**：
- **早期数值模拟**：大 (horizon-size) 环形成。
- **高分辨率模拟**：大量小尺度结构（kinks）→ 环尺寸远小于 horizon。
- **稳定尺度 $\zeta$**：gravitational radiation 反作用稳定化 → $\zeta \sim \Gamma G\mu t$（$\Gamma \sim 100$）。

[FACT] **Scaling 弦的 loop distribution（公式 72–76）**：Scaling 解 $\rho_{\rm s} = \mu/(xt)^{2}$, $x\in[0.3\text{–}0.7]$（近期模拟 $x \sim 0.3$）。环长度 $L_b = K\,\zeta(t_b) = K\,\Gamma G\mu t_b$（公式 72）。环诞生率（物质主导，公式 73）：

$$
\frac{dn_b}{dt} = \frac{2}{3x^{2}}\,(\Gamma G\mu)^{-1}\,K^{-1}\,t^{-4}
$$

环长度分布（公式 76）：

$$
\frac{dn}{dL}(L,t) = \frac{2}{3x^{2}}\,\frac{K+1}{K}\cdot\frac{1}{t^{2}\,(L+\Gamma G\mu t)^{2}},\quad L\leq K\Gamma G\mu t
$$

[FACT] **现代 loop 数量与尺度**（$G\mu=10^{-6}$ 时）：

| 量 | 值 |
|---|---|
| 最丰环长度 | ~200 $(G\mu/10^{-6})(\Omega_0 h^2)^{-1/2}$ kpc |
| 数密度 | $\sim 4.6\times10^{-6}\,(G\mu/10^{-6})^{-1}(\Omega_0 h^2)^{3/2}$ Mpc$^{-3}$ |
| 典型间隔 | ~60 $(G\mu/10^{-6})^{1/3}(\Omega_0 h^2)^{-1/2}$ Mpc |

**关键公式**：

$$
\boxed{\rho_{\rm s} = \frac{\mu}{(xt)^{2}}\;,\quad \zeta\sim\Gamma G\mu t\;,\quad \frac{dn_b}{dt}=\frac{2}{3x^{2}}(\Gamma G\mu)^{-1}K^{-1}t^{-4}\;(73)}
$$

### 6.4.2 Intercommuting of Long Strings

> **长弦交叉**

[FACT] **机制**：两条弦段交叉 → 重叠长度 $\sim w\sim\eta^{-1}$ → Higgs 相未定义 → 拓扑去除事件。释放能量 $\sim \mu w\sim\eta$ → 每个 intercommuting 释放 ~1 个 X 粒子。

[FACT] **速率估算**：

$$
n_{\rm ic}(t) = \frac{\chi}{\xi_{\rm s}^{4}}\;\;\text{(77)},\quad \xi_{\rm s}\sim x t,\;x\sim 0.3\text{–}0.7
$$

- **结论**：intercommuting 过程的 X 产额 **utterly negligible**，远不足以解释 EHECR 通量。

### 6.4.3 Final Stage of Loop Shrinkage

> **闭环收缩的终结阶段**

（本节在原文 TOC 中列出为 "Final Stage of Loop Shrinkage"，内容涵盖 loop 引力辐射耗尽后的坍缩行为，作为 §6.4.4–6.4.5 的前置背景；具体 X 产率主要集中于 §6.4.4 与 §6.4.5。）

[FACT] 大环 $L/4$ 时刻坍缩为 double-line 配置 → 整体湮灭为 X 粒子；或反复自相交分裂为越来越小的子环 → debris of tiny loops（~$\eta^{-1}$ 尺度）→ X 粒子。**碎裂时间**：$\tau_{\rm debris}\sim L \ll \tau_{\rm grav}\sim(\Gamma G\mu)^{-1}L$。

### 6.4.4 Cusp Evaporation

> **Cusp 蒸发**

[FACT] **机制**：**Cusp**——弦上某点瞬时以光速运动 → 曲率半径极小 → Nambu-Goto action 失效。具有有限宽度 $w$ 的真实弦在 cusp 附近 → 弦段重叠 → "蒸发"为 X 粒子。**Kink 碰撞**也可形成 cusp（沿相反方向传播的 kinks 相撞 [424]）。

[FACT] **Cusp 长度**：

**原始估计** [423]：

$$
\ell_c \sim \zeta^{2/3}\,w^{1/3}
$$

**更一般估计** [425]：

$$
\ell_c \sim (L\,w)^{1/2}
$$

比旧估计小 $(w/L)^{1/6}$ → 对 GUT 尺度字符串（$\sim 10^{16}$ GeV），$w/L$ 为天文数字小量 → **$\ell_c$ 被严重压低**。

[FACT] **X 粒子数**：单次 cusp 事件 ~$(\eta\zeta)^{2/3}$（长弦）或 ~$(\eta L)^{2/3}$（闭环）。对 GUT 尺度：$\eta\sim 10^{16}$ GeV，但 $L/w\sim$ 极大 → cusp 效率低。**结论**：**cusp evaporation 不足以产生可观 EHECR 通量**。

**关键公式**：

$$
\boxed{\ell_c \sim \zeta^{2/3}w^{1/3}\;(旧),\quad \ell_c\sim(Lw)^{1/2}\;(新)}
$$

### 6.4.5 Collapse or Repeated Self-intersections of Closed Loops

> **闭环的坍缩与反复自相交**

[FACT] **机制**：大环 $L/4$ 时刻坍缩为 double-line 配置 → 整体湮灭为 X 粒子；或反复自相交分裂为越来越小的子环 → debris of tiny loops（~$\eta^{-1}$ 尺度）→ X 粒子。

[FACT] **速率（公式 84）**：假设 $f_X$ 的环能量转化为 X：

$$
\dot n_X(t) = f_X\cdot\frac{\mu}{m_X}\cdot\frac{2}{3x^{2}}\,t^{-3}\;\;\text{(84)}
$$

[FACT] **解释 EHECR 的条件（公式 85）**：

$$
f_X\cdot\eta_{16}^{3/2} \simeq 2.8\times10^{-5}\;\;\text{(85)}
$$

（$\eta_{16} = \eta/10^{16}$ GeV, $l(E_\gamma=300\,{\rm EeV})=50$ Mpc）

[FACT] **级联 $γ$ 约束（公式 86–88）**：

$$
\omega_{\rm cas} \simeq \frac{1}{2}\,m_X\,\dot n_X\,t_0\;\;\text{(86)},\qquad \omega_{\rm cas} \leq 2\times10^{-6}\,{\rm eV\,cm^{-3}}\;\;\text{(87)}
$$

导出（公式 88）：

$$
f_X\cdot\eta_{162} \leq 9.6\times10^{-6}\;\;\text{(88)}
$$

[FACT] **允许窗口**（联立 (85)+(88)）：

$$
9.2\times10^{12}\,{\rm GeV}\,\lesssim \eta\,\lesssim 1.2\times10^{15}\,{\rm GeV},\qquad f_X\sim 2.8\times10^{-5}\,\eta_{16}^{-3/2},\qquad f_X\in[6.7\times10^{-4},1]
$$

- **$m_X \gg 10^{15}$ GeV 时 GUT-scale 弦难以同时满足**（违反 $γ$ 背景约束）。
- **$\eta \sim 10^{13}$ GeV 的"轻"弦**是自然候选。

[FACT] **数值模拟支持**：
- **Siemens-Kibble [431]**：环自相交概率随谐波数**指数增长**；kinks 是高谐波配置 → 有 kink 的环高概率自相交 → $f_X \sim \rm few\times 10^{-4}$ 是**合理的**。
- **Vilenkin [429]**：子环碎裂过程中部分能量转化为动能 → X 粒子可能**相对论性**（空间分散）。
- **Berezinsky-Blasi-Vilenkin [406]**：对 relativistic X 情形，某些 loop fragmentation 模型下无法同时满足 (85)+(88) → 但其他模型（如 Siemens-Kibble）可绕过。
- **Bhattacharjee-Sigl [432]**：$f_X\sim 1$ 时（全部环碎裂为 X），若 $\eta \lesssim 3.1\times10^{13}$ GeV 且 $f_{\rm KE}\lesssim$ few%，可解释 EHECR 且不违反 $γ$ 约束。

[FACT] **轻弦的额外优势**：Loop 数密度 $\propto (G\mu)^{-1}$ → $\eta = 10^{13}$ GeV 时（$G\mu\sim 10^{-12}$），与 $\eta=10^{16}$ GeV 相比 loop 数密度**大 $10^{6}$ 倍**。GZK 半径 (50 Mpc) 内：GUT 弦 (~$10^{16}$ GeV) ~ 2.4$(\Omega_0 h^2)^{3/2}$ 个 loop；轻弦 (~$10^{13}$ GeV) ~ $2.4\times10^{6}$ 个 loop。**结论**：轻弦（$\eta \sim \rm few\times 10^{13}$ GeV）通过快速多重碎裂过程可**自然产生足够多 X 粒子**。

**关键公式**：

$$
\boxed{\dot n_X = f_X\frac{\mu}{m_X}\frac{2}{3x^{2}}t^{-3}\;(84),\quad f_X\eta_{16}^{3/2}\simeq 2.8\times10^{-5}\;(85),\quad f_X\eta_{162}\leq 9.6\times10^{-6}\;(88)}
$$

### 6.4.6 Direct Emission of X Particles from Cosmic Strings

> **宇宙弦直接发射 X 粒子**

[FACT] **Vincent-Antunes-Hindmarsh [417]**（新数值模拟）：若不人为设环尺寸截断 → 环主要在最小尺度（~弦宽度 $w$）上形成 → 立即坍缩为 X。→ **弦能量主要通过直接 X 粒子发射维持 scaling**，几乎无"大"环形成。这**颠覆**了早期模拟结论（能量主要损失于引力辐射环）。已被 **Moore-Shellard [434]** 质疑。

[FACT] **若 [417] 正确**：$\dot n_X = (84)$ with $f_X=1$ → 与 (68) 对比 → $\eta \lesssim 10^{13}$ GeV（否则会超量产生 EHECR）。
- → **GUT-scale 弦被排除**。
- → 唯一预测：若长弦恰在 ~50 Mpc 内，EHECR 应呈**filamentary/linear 各向异性**（对应弦的空间分布）。

**关键参数**：Scaling $x \sim 0.3$；$\zeta \sim \Gamma G\mu t$；$\eta$ 允许窗口 $9.2\times10^{12}$ – $1.2\times10^{15}$ GeV；direct emission $\eta \lesssim 10^{13}$ GeV。

---

## 6.5 X Particles from Superconducting Cosmic Strings

[FACT] §6.5 讨论 SCS（superconducting cosmic strings）作为 X 源的物理与演化。

### 6.5.1 基本物理

> **SCS 基本物理**

[FACT] 弦携带**持续电流**：
- 由弦内**带电费米子零模**（零模：弦内质量为零，弦外有质量 $m_F$）或**带电 Higgs 凝聚**承载。
- 也可以来自 trapped 电荷（Kibble 机制）或不同电流弦段间 inter-commuting。

[FACT] **临界电流**：
- 费米子情形：弦内 Fermi 动量 $p_F$ 超 $m_F$ → 费米子不再 trapped → 开始被释放。
- 玻色子情形：弦内凝聚能量密度过高 → EM 对称性恢复 → 失去超导。
- **上限**：$J_c \leq J_{\rm max} \simeq e\,\eta$（两种情形）。

[FACT] 弦外**X 粒子质量**：$m_F = g\,\eta$（$g \sim$ Yukawa 耦合），可达 GUT 尺度 $\sim 10^{16}$ GeV。

### 6.5.2 OTW-SCS 演化场景

> **OTW-SCS 演化场景**

[FACT] **Ostriker-Thompson-Witten [421]**：原初磁场随宇宙膨胀 → 通过弦环的磁通变化 → 弦环上感应电流。环振荡 → 电磁辐射 + 引力辐射损失 → 环缩小 → 电流 $J\propto L^{-1}$ 增加 → 达到 $J_c = J_s$。饱和环释放 X 粒子。

### 6.5.3 X 粒子发射率

> **SCS 的 X 发射率**

[FACT] **饱和环上费米子总数**：$N_F = (m_F/\pi)\,L$。

[FACT] **电磁辐射主导**（$G\mu \lesssim 10^{-8}$ 或 $g > 10(G\mu)^{1/2}$，公式 89）：

$$
\dot N_F = \frac{4}{\pi^{2}}\,\alpha_{\rm em}\,\gamma_{\rm em}\,g^{3}\,\eta\;\;\text{(89)},\quad \gamma_{\rm em}\simeq 100
$$

[FACT] **引力辐射主导**（$g \ll 10(G\mu)^{1/2}$，公式 90）：

$$
\dot N_F = \frac{g}{\pi}(\Gamma G\mu)\,\eta\;\;\text{(90)}
$$

[FACT] **条件**（产生 EHECR）：$m_F = g\eta \geq 10^{12}$ GeV → $\eta \geq 10^{12}$ GeV → $G\mu \geq 10^{-14}$，且 $10^{-7}(G\mu)^{-1/2} \leq g \leq 1$。

### 6.5.4 SCS 主要困难

> **SCS 场景的主要困难**

[FACT] SCS 演化**高度不确定**（无详细数值模拟）。
- 若采用 **OTW 场景**（$L_s$ 常数）：$\dot n_X \propto t^{-4}$，HSW [393] 表明某些参数范围可产生可观测通量。
- 若 $L_s$ 随时间增长（如 dynamos 增磁）：$L_s(t_0)$ 更小 → 当前 $\dot n_X$ 不够。
- 若 $L_s$ 随时间减小：早期注入能量过大 → **违反 CMB 畸变与 Big Bang 核合成** [437]。
- 其他不确定性：环可复杂折叠、增强电荷载体发射；**Vorton 稳定性**：弦可能稳定为电流携带的小环（vorton，§6.6）；弦附近强磁场区域中 X 衰变产物能量严重降解 [440]（可能解决：若 X 寿命足够长可漂移到弱场区 [393]，或 AC 电流区 [406]）。

[FACT] **结论**：最简单 SCS 模型**一般无法产生足够 EHECR 通量** → 但**尚无定论**（SCS 物理远未完全理解）。

**关键公式**：

$$
\boxed{\dot N_F = \frac{4}{\pi^{2}}\alpha_{\rm em}\gamma_{\rm em}g^{3}\eta\;(EM,\;89),\quad \dot N_F = \frac{g}{\pi}(\Gamma G\mu)\eta\;(grav,\;90)}
$$

---

## 元数据

```yaml
chapter: 10
pages: "59–72"
subsections: ["6.4.1", "6.4.2", "6.4.3", "6.4.4", "6.4.5", "6.4.6", "6.5.1", "6.5.2", "6.5.3", "6.5.4"]
key_formulas:
  - "ρ_s = μ/(xt)² (scaling)"
  - "ṅ_X = f_X (μ/m_X) (2/(3x²)) t⁻³ (Eq. 84)"
  - "f_X η₁₆^{3/2} ≃ 2.8×10⁻⁵ (Eq. 85)"
  - "f_X η₁₆₂ ≤ 9.6×10⁻⁶ (Eq. 88)"
  - "Ṅ_F = (4/π²) α_em γ_em g³ η (Eq. 89)"
keywords:
  - cosmic string scaling
  - intercommuting
  - cusp evaporation
  - loop self-intersection
  - direct X emission
  - superconducting cosmic string
  - OTW scenario
references_internal:
  prev_chapter: 09_topdown_basic_fragmentation
  next_chapter: 11_monopoles_vortons_necklaces
```

**引用页码**：全文引用基于 *Phys. Rep.* 320 (1999), pp. 59–72。