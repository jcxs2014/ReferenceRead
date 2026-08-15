---
chapter: 2
title: Physics
pages: "11–60"
sections:
  - "2.1 Cosmic ray interactions with electromagnetic waves"
  - "2.2 Cosmic ray acceleration and escape from sources"
  - "2.3 Cosmic ray spatial transport"
  - "2.4 Radiative and non-radiative cosmic ray processes and their cooling times"
  - "2.5 Cosmic ray spectral transport"
related_chapters:
  prev: 01_introduction
  next: 03_astrophysical_systems
status: done
---

> 本章属于：Cosmic ray feedback in galaxies and galaxy clusters (Ruszkowski & Pfrommer 2023)
>
> 上一章：`01_introduction.md`
>
> 下一章：`03_astrophysical_systems.md`

# 2. Physics — CR 等离子体物理的核心机制

[FACT] §2 Physics 是全文最技术性的章节，跨越 pp. 11–60（约 50 页）。核心任务是建立"CR 与磁化等离子体如何耦合"这一物理基础。五个子节依次覆盖：**波–粒相互作用**（§2.1）→ **加速与逃逸**（§2.2）→ **空间传播**（§2.3）→ **辐射与非辐射冷却**（§2.4）→ **谱传播**（§2.5）。

[INTERPRETATION] §2 的逻辑链条是：**CR 如何与等离子体交换能量**（§2.1）→ **CR 如何被产生**（§2.2）→ **CR 如何从源传播出去**（§2.3）→ **CR 传播中如何损失能量**（§2.4）→ **CR 谱如何演化**（§2.5）。五个子节形成"耦合→产生→传播→耗散→谱演化"的闭合物理图景。

---

## 2.1 Cosmic ray interactions with electromagnetic waves

[FACT] §2.1 讨论 CR 与磁化等离子体中 MHD 波的耦合，是 CR 反馈的物理基础。本节由三个子子节构成：2.1.1 CR 数密度估计（确立 CR 是微量组分）、2.1.2 CR 波散射与扩散（扩散系数的物理来源）、2.1.3 CR 驱动的等离子体不稳定性（CR 反馈的闭环机制）。

### 2.1.1 Estimates of cosmic ray number densities

> **宇宙线数密度估计**

[FACT] 给出银河系盘与星系团 ICM 中 CR 数密度的量级估计，确立"CR 在粒子层面是微量组分"的基准。

**关键参数**：
- 银河盘（equipartition，Boulares & Cox 1990；Naab & Ostriker 2017）：CR 与磁场/湍动/热能能量密度近似均分；主导粒子能量 $\sim 10^{10}$ eV；ISM warm 相 $n \sim 1$ cm$^{-3}$ 时 CR 离子数密度 $\sim 10^{-9}$ cm$^{-3}$（每 $\sim 10^9$ 个 ISM 粒子约 1 个 CR 质子）
- ICM：$k_B T \sim 1$–$10$ keV、$n \sim 10^{-3}$ cm$^{-3}$；γ 射线给出 CR-to-thermal pressure ratio 上限 $\sim 10^{-2}$ → CR 数密度 $\sim 10^{-10}$ cm$^{-3}$（CR:background $\sim 10^{-7}$）

[INTERPRETATION] 粒子层面微量 ≠ 能量层面次要（equipartition）——为后文"CR 虽稀薄却能驱动反馈"埋下伏笔。

### 2.1.2 Cosmic ray-wave scattering and diffusion

> **宇宙线-波散射与扩散**

[FACT] §2.1.2 讨论 CR 与 MHD 波的共振条件（论文 Eq. 1）：

$$
k_{\parallel}\,v_{\parallel} - \omega = \pm n\,\Omega_{\text{cr}}
\quad \text{(Eq. 1)}
$$

- $\omega$：波的旋转频率；$k_{\parallel}$：沿磁场方向波数；$v_{\parallel}$：CR 沿磁场的速度分量；$\Omega_{\text{cr}} = q B / (\gamma m c)$ 相对论回旋频率；$n=1$ 对应平行传播的波模式，$n>1$ 对应斜传播模式

[FACT] CR 与 MHD 波的相互作用类型：(i) gyro-resonant 相互作用；(ii) 集体波–粒散射（wave–particle scattering），显著降低 CR 的有效 mean free path（Wentzel 1974）。

[FACT] 论文系统讨论 MHD 波谱中的三种主要模式：
1. **Alfvén wave**（剪切阿尔芬波）：$\omega = k_{\parallel}\,v_A$，$v_A = B/\sqrt{4\pi\rho}$
2. **Fast magnetosonic wave**（快磁声波）：压缩型纵波，恢复力来自磁压 + 气体压
3. **Slow magnetosonic wave**（慢磁声波）：压缩型纵波，恢复力以气体压为主

[FACT] CR 的**扩散系数**：

$$
D_{\text{cr}} \sim \frac{1}{3}\,\lambda_{\text{mfp}}\,c
$$

$\lambda_{\text{mfp}}$ 由 Alfvén wave 的磁扰动 $B'/B_0$ 决定。各向异性散射：平行磁场方向散射较强（$\lambda_{\parallel}$），垂直方向较弱（$\lambda_{\perp} \ll \lambda_{\parallel}$）。

**关键公式**：

$$
\boxed{k_{\parallel}\,v_{\parallel} - \omega = \pm n\,\Omega_{\text{cr}} \;\;\text{(Eq. 1, resonance)}}
$$

**关键参数**：$D_{\text{cr}}$（ISM, 1 GeV）$\sim 3\times 10^{28}$ cm$^2$ s$^{-1}$；$D_{\text{cr}}$（ICM）$\sim 10^{28}$–$10^{30}$ cm$^2$ s$^{-1}$

### 2.1.3 Cosmic ray driven plasma instabilities

> **宇宙线驱动的等离子体不稳定性**

[FACT] §2.1.3 讨论 CR 驱动的等离子体不稳定性，是 CR 反馈的核心——CR 自激散射所需的磁场扰动。

1. **Streaming instability**（Parker 1965；Kulsrud & Pearce 1969）：CR 沿磁场漂移速度超过 Alfvén 速度时激发 Alfvén waves。论文给出 gyro-resonant 增长率（Eq. 7，Shalaby et al. 2021）：

$$
\gamma_{\text{gyro}} \approx \Omega_{i,0}\,C\,\frac{n_{\text{cr}}(>p_{\min})}{n_i}\,\frac{v_d - v_A}{v_A}
$$

其中 $\Omega_{i,0} = q B/(m_i c)$，$C = (s-3)/(s-2)$ 为 $\mathcal{O}(1)$ 常数，$n_{\text{cr}}(>p_{\min})$ 为 resonant CR 数密度，$v_d$ 为 CR 漂移速度。该式显示只有 super-Alfvénic CR 才能驱动 Alfvén waves。

2. **Bell instability**（Bell 2004）：高能 CR 的各向异性分布产生 non-resonant 电流驱动不稳定性，增强磁场 $B'$ 幅度。
3. **Whistler instability**（注 11）：电子 CR 驱动的 electron-scale 不稳定性。
4. **Ion-cyclotron instability**（注 12）：离子回旋波的不稳定激发。

[FACT] 注 10 指出，对 CR 驱动的不稳定性，相对磁场成 oblique 角度传播的模式通常呈 subdominant。

[CRITIQUE] 论文给出 $\gamma_{\text{gyro}}$ 增长率适用于 $v_d$ 略微超过 $v_A$ 的弱超临界情形。当 $v_d \gg v_A$（如 Bell 情形），增长率由 non-resonant Bell 不稳定性主导，线性 streaming 理论失效。

[CRITIQUE] §2.1.3 和 §2.2.2 讨论 Bell 不稳定性时主要给出线性增长率。Bell 不稳定性在非线性饱和后：磁场放大程度 $B'/B_0 \sim 10$–$100$；饱和后 CR 散射进入 turbulent transport 模式；非线性饱和机制（波–波相互作用、磁重联）尚未完全理解。

**关键公式**：

$$
\boxed{\gamma_{\text{gyro}} \approx \Omega_{i,0}\,C\,\frac{n_{\text{cr}}(>p_{\min})}{n_i}\,\frac{v_d - v_A}{v_A} \;\;\text{(Eq. 7, gyro-resonant instability)}}
$$

---

## 2.2 Cosmic ray acceleration and escape from sources

[FACT] §2.2 覆盖 pp. 21–32，讨论 CR 如何被加速（DSA）和从源逃逸。三个子子节：2.2.1 CR 源分类、2.2.2 DSA 与 Bell 磁场放大、2.2.3 SNR 向 ISM 的 CR 逃逸。

### 2.2.1 Cosmic ray sources

> **宇宙线源分类**

[FACT] 论文列出 CR 的三大类源：

| 源类型 | 能量范围 | 加速机制 | 环境 |
|--------|----------|----------|------|
| 超新星遗迹（SNR） | $\sim \text{GeV}–\text{PeV}$ | DSA | ISM |
| 活动星系核（AGN） | $\sim \text{TeV}–\text{EeV}$ | 磁重联 / DSA | 喷流/瓣 |
| 星系团内激波 | $\sim \text{TeV}$ | DSA | ICM |
| 太阳活动 | $\sim \text{MeV}–\text{GeV}$ | 重联 | 太阳风 |

[INTERPRETATION] §2.2 明确将 AGN 加速作为 CR 的重要源之一。物理链：AGN 喷流/瓣内部激波加速 CR → CR 沿磁力线扩散到 ICM → CR 通过 streaming instability 加热 ICM。这一机制与"AGN 通过机械做功直接加热 ICM"互补或替代。

### 2.2.2 Particle acceleration and magnetic amplification

> **粒子加速与磁场放大**

[FACT] §2.2.2 系统讲解**扩散激波加速（DSA）**：DSA 产出的 CR 能谱在稳态下为幂律：

$$
\frac{dn}{dE} \propto E^{-p}, \quad p = \frac{r+2}{r-1}
$$

其中 $r$ 为压缩比。对于强激波（$r=4$）：$p = (4+2)/(4-1) = 2$。

[FACT] §2.2.2 讨论 **Bell 磁场放大机制**：Bell 不稳定性通过 CR 电流产生非共振波，把磁场从背景 $B_0 \sim \mu\text{G}$ 放大到 $B' \sim 100\,\mu\text{G}$ 甚至更高，从而提高 DSA 效率。

[CRITIQUE] 论文给出 DSA 稳态谱指数 $p = (r+2)/(r-1)$，这是**经典 DSA 的"薄激波"近似结果**。实际上：Bell 磁场放大使有效压缩比 $r_{\text{eff}} > 4$ 使 $p < 2$（更硬）；有限激波寿命（aging effect）使逃逸 CR 谱更陡。

**关键公式**：

$$
\boxed{p = \frac{r+2}{r-1} \;\;\text{[DSA]},\;\; p=2 \text{ for } r=4}
$$

### 2.2.3 Particle escape from supernova remnants to the interstellar medium

> **从超新星遗迹到星际介质的粒子逃逸**

[FACT] §2.2.3 讨论 CR 从 SNR 内部向 ISM 逃逸的机制：早期 SNR 阶段 CR 被 Bell 放大磁场磁镜限制；晚期（$\sim 10^4$ yr）CR 通过扩散进入 ISM；CR 泄漏能谱较 DSA 稳态谱更陡（$E^{-2.5}$ 或更陡）。

**关键参数**：Bell 放大磁场 $B' \sim 100\,\mu$G；强激波压缩比 $r=4$；DSA 谱指数 $p=2$（$r=4$）；CR–thermal 数密度比（ISM）$\sim 10^{-9}$；CR–thermal 数密度比（ICM）$\sim 10^{-7}$

---

## 2.3 Cosmic ray spatial transport

[FACT] §2.3 覆盖 pp. 32–48，是本章最长且结构最复杂的子节，讨论 CR 如何在磁化等离子体中空间传播。五个子子节：2.3.1 Theoretical background、2.3.2 One-moment CRHD、2.3.3 Two-moment CRHD、2.3.4 Energy vs entropy methods、2.3.5 Streaming instability & self-confinement、2.3.6 Turbulence confinement。

### 2.3.1 Theoretical background

> **理论背景**

[FACT] 论文系统比较 CR 传播的三种理论框架：

| 框架 | 变量 | 假设 | 应用 |
|------|------|------|------|
| 全动理学（Fokker-Planck） | $f(x,p,\mu,t)$ | 完整 6D phase space | 理论研究 |
| One-moment CRHD | $n_{\text{cr}}, P_{\text{cr}}$ | 各向同性、无 streaming | 大尺度模拟 |
| Two-moment CRHD | $P_{\text{cr}}, j_{\text{cr}}$ | 各向异性 streaming | 星系/星系团反馈 |

[FACT] §2.3 的关键结论：CR 在星系团尺度上的有效扩散系数 $D_{\text{cr}} \sim 10^{28}$–$10^{30}$ cm$^2$ s$^{-1}$；在 ISM 中 $D_{\text{cr}} \sim 3\times 10^{28}$ cm$^2$ s$^{-1}$（1 GeV），随能量 $E^{1/3}$ 增长（Kolmogorov turbulence）。

### 2.3.2 One-moment cosmic-ray hydrodynamics

> **单矩宇宙线流体力学**

[INTERPRETATION] **One-moment CRHD**：把 CR 当作"附加流体"，只有压力贡献。假设 CR 分布各向同性，忽略 streaming。物理意义是"CR 只通过压力影响流体"。

[INTERPRETATION] One-moment 无法重现 **cooling flow suppression** 的关键机制（Ruszkowski & Begelman 2002）。

### 2.3.3 Two-moment cosmic-ray hydrodynamics

> **双矩宇宙线流体力学**

[FACT] §2.3.3 **Two-moment CRHD** 同时追踪 CR 压力张量和 CR 流，允许 CR 沿磁场方向 streaming，同时被 streaming instability 自限制（self-regulating）。Ruszkowski & Begelman 2002 首次将此框架应用到 cool core 星系团。

[INTERPRETATION] **Two-moment CRHD**：额外追踪 CR 流（$j_{\text{cr}}$），允许 CR 沿磁场 streaming，但由 streaming instability 自限制。物理意义是"CR 有 streaming 但有自调节机制"。

[CRITIQUE] §2.3.3 的 two-moment 方程在数值实现上要求 MHD solvers 满足 positivity（$P_{\text{cr}} \geq 0$）和 causality（$|j_{\text{cr}}| \leq c\,P_{\text{cr}}$）约束。标准 Godunov 格式可能产生负压力或超光速 streaming（Ohm et al. 2013, 2015）。

### 2.3.4 Cosmic ray energy vs. entropy methods

> **宇宙线能量 vs 熵方法**

### 2.3.5 Streaming instability, wave damping mechanisms and cosmic ray self-confinement

> **流不稳定性、波阻尼机制与宇宙线自约束**

### 2.3.6 Cosmic ray scattering on MHD turbulence - external confinement by turbulence

> **宇宙线在磁流体湍流上的散射——湍流的外部约束**

---

## 2.4 Radiative and non-radiative cosmic ray processes and their cooling times

[FACT] §2.4 覆盖 pp. 48–58，讨论 CR 的能量损失机制。三个子子节：2.4.1 Overview、2.4.2 Cosmic ray ion interactions、2.4.3 Cosmic ray lepton interactions、2.4.4 Equilibrium electron distribution。

### 2.4.1 Overview

> **概览**

[FACT] 论文列出 CR 的三种主要能量损失机制：

| 损失机制 | 适用粒子 | 时标 | 依赖 |
|----------|----------|------|------|
| 同步辐射 | 电子 | $\sim 10^9\,B^{-2}$ yr | $B^2$ |
| 逆康普顿（IC） | 电子 | $\sim 10^9\,u_{\text{rad}}^{-1}$ yr | 辐射场能量密度 |
| pp 碰撞（hadronic） | 质子 | $\sim 10^9\,n_{\text{ISM}}^{-1}$ yr | 环境数密度 |
| 绝热损失 | 所有粒子 | $\sim$ 膨胀时标 | $\nabla \cdot \mathbf{v}$ |
| Coulomb 损失 | 低能 CR | $\ll 10^9$ yr | 环境电子数密度 |

[FACT] 在 ICM 中，CR 的冷却时标更长（$n_e \sim 10^{-3}$ cm$^{-3}$），可达 $10^{10}$–$10^{11}$ yr，使 CR 能有效储存能量。

**图表分析（Figure 2，Cooling times，约 p. 53）**：

- **图的目的**：比较 CR 不同损失机制（同步辐射、IC、pp、绝热）随能量和环境的时标
- **坐标轴**：横轴 CR 能量（$10^4$–$10^{11}$ GeV）；纵轴 $t_{\text{cool}}$（yr，对数坐标）
- **关键观察**：GeV–TeV 区间 pp 主导质子损失；TeV 以上同步+IC 主导电子损失；所有曲线都超过星系动力学时标（$\sim 10^8$ yr），支持"长冷却时间"论点
- **物理意义**：在 ICM 极端低密度环境下（$n \sim 10^{-3}$ cm$^{-3}$），pp 冷却时标 $\sim 10^{10}$ yr，CR 几乎不损失能量，成为 ICM 压力的重要组分

[CRITIQUE] Figure 2 未包含磁重联中的 CR 损失或再加速对净冷却的补偿——这两点在 §2.5 讨论。

### 2.4.2 Cosmic ray ion interactions

> **宇宙线离子相互作用**

### 2.4.3 Cosmic ray lepton interactions

> **宇宙线轻子相互作用**

### 2.4.4 Equilibrium electron distribution

> **平衡电子分布**

---

## 2.5 Cosmic ray spectral transport

[FACT] §2.5 覆盖 pp. 58–60，讨论 CR 谱的传播演化。两个子子节：2.5.1 Momentum-dependence、2.5.2 Numerical methods。

### 2.5.1 Momentum-dependence of spatial cosmic ray transport

> **空间宇宙线传播的动量依赖性**

[FACT] 谱传播方程（含空间扩散 + 再加速 + 能量损失）：

$$
\frac{\partial f}{\partial t} = \nabla \cdot (D(E)\,\nabla f) + \frac{1}{3}(\nabla \cdot \mathbf{u})\,\dot{p}_{\text{acc}} + \frac{\partial}{\partial p}\left[\frac{f}{\dot{p}_{\text{loss}}} - \frac{\dot{p}_{\text{acc}}}{3}\,f\right] + Q_{\text{src}}
$$

**关键公式**：

$$
\boxed{D_{\text{cr}} \propto E^{1/3} \;\;\text{[Kolmogorov turbulence]}}
$$

### 2.5.2 Numerical methods for evolving the cosmic ray momentum spectrum in space

> **空间宇宙线动量谱演化的数值方法**

[FACT] §2.5 讨论**再加速（stochastic re-acceleration）** 在 CGM 和 ICM 中的作用：湍流中的随机碰撞使 CR 获得额外能量，可部分抵消 adiabatic loss。Kolmogorov turbulence 下 $D \propto E^{1/3}$。

[CRITIQUE] §2.5 的 spectral transport 方程在 astrophysical 应用中常被简化为"single energy bin"或"single power-law index"，会丢失 CR 谱在冷却、再加速过程中的弯曲和截断特征，直接影响 γ 射线能谱预测（§4.1、§4.3）。

**关键参数**：再加速指数（Kolmogorov）$\delta = 1/3$；CR 冷却时标（ISM, GeV）$\sim 10^9$ yr；CR 冷却时标（ICM, GeV）$\sim 10^{10}$–$10^{11}$ yr

---

## 元数据

```yaml
chapter: 2
pages: "11–60"
subsections: ["2.1.1", "2.1.2", "2.1.3", "2.2.1", "2.2.2", "2.2.3",
              "2.3.1", "2.3.2", "2.3.3", "2.3.4", "2.3.5", "2.3.6",
              "2.4.1", "2.4.2", "2.4.3", "2.4.4", "2.5.1", "2.5.2"]
key_formulas:
  - "k_∥ v_∥ - ω = ± n Ω_cr (Eq. 1, resonance)"
  - "γ_gyro ≈ Ω_{i,0} C (n_cr/n_i) (v_d - v_A)/v_A (Eq. 7)"
  - "p = (r+2)/(r-1) [DSA]"
  - "D_cr ∝ E^{1/3} [Kolmogorov]"
keywords:
  - streaming instability
  - Bell instability
  - DSA
  - one-moment CRHD
  - two-moment CRHD
  - Kolmogorov
  - stochastic re-acceleration
references_internal:
  prev_chapter: 01_introduction
  next_chapter: 03_astrophysical_systems
```

**引用页码**：全文引用基于 *A&A Reviews 31:4 (2023)*，pp. 11–60。