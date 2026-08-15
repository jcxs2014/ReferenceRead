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

## 2.1 本节核心内容

[FACT] §2 Physics 是全文最技术性的章节，跨越 pp. 11–60（约 50 页）。核心任务是建立"CR 与磁化等离子体如何耦合"这一物理基础。五个子节依次覆盖：**波–粒相互作用**（§2.1）→ **加速与逃逸**（§2.2）→ **空间传播**（§2.3）→ **辐射与非辐射冷却**（§2.4）→ **谱传播**（§2.5）。

[FACT] §2.1 本身包含 3 个子子节：2.1.1 CR 数密度估计、2.1.2 CR 波散射与扩散、2.1.3 CR 驱动的等离子体不稳定性。§2.1 是理解整个领域"为什么 CR 与等离子体耦合"的关键。

[FACT] §2.3 是最长且结构最复杂的子节，分为 2.3.1 Theoretical background、2.3.2 One-moment CRHD、2.3.3 Two-moment CRHD、2.3.4 Cosmological simulations 等。这里给出数值模拟中描述 CR 传播的两套主流 hydrodynamic framework。

[INTERPRETATION] 本章的逻辑链条是：**CR 如何与等离子体交换能量**（§2.1）→ **CR 如何被产生**（§2.2）→ **CR 如何从源传播出去**（§2.3）→ **CR 传播中如何损失能量**（§2.4）→ **CR 谱如何演化**（§2.5）。五个子节形成"耦合→产生→传播→耗散→谱演化"的闭合物理图景。

## 2.2 原文内容

### 2.2.1 §2.1 Cosmic ray interactions with electromagnetic waves (pp. 12–21)

[FACT] §2.1 从 CR 与磁流体波（MHD waves）的共振条件开始，论文第 1 式：

$$
k_{\parallel} v_{\parallel} - \omega = \pm n\,\Omega_{\text{cr}}
\quad \text{(Eq. 1)}
$$

- $\omega$：波的旋转频率
- $k_{\parallel}$：沿磁场方向波数
- $v_{\parallel}$：CR 沿磁场的速度分量
- $\Omega_{\text{cr}} = q B / (\gamma m c)$：相对论回旋频率
- $n$ 为自然数，$n=1$ 对应平行传播的波模式，$n>1$ 对应斜传播模式

[FACT] 论文明确列出三种 CR 与 MHD 波的相互作用类型：(i) gyro-resonant 相互作用；(ii) 集体波–粒散射（wave–particle scattering），显著降低 CR 的有效 mean free path（Wentzel 1974）。

[FACT] 论文系统讨论了 MHD 波谱中的三种主要模式：

1. **Alfvén wave**（剪切阿尔芬波）：$\omega = k_{\parallel} v_A$，$v_A = B/\sqrt{4\pi \rho}$，是最主要的 CR 散射波模式。
2. **Fast magnetosonic wave**（快磁声波）：压缩型纵波，恢复力来自磁压 + 气体压。
3. **Slow magnetosonic wave**（慢磁声波）：压缩型纵波，恢复力以气体压为主。

[FACT] 注 7 明确给出剪切阿尔芬波的定义："a type of plasma wave that arises due to oscillations of the magnetic field"。

[FACT] 注 8 指出电子的 pitch-angle scattering 与圆极化电磁波的相互作用机制；注 9 说明 fast/slow magnetosonic waves 的物理特征。

[FACT] §2.1.1 给出 CR 数密度的三种不同能量区间的估计：

| 能量区间 | 估计方法 | 典型数密度 |
|----------|----------|------------|
| GeV–TeV | 伽马射线观测（Fermi-LAT π⁰ 衰变） | $n_{\text{cr}} \sim 10^{-9}$ cm$^{-3}$ |
| PeV–EeV | 大气广延簇射 | $n_{\text{cr}} \sim 10^{-15}$ cm$^{-3}$ |
| 高能 CR（$\sim 10^{10}$ GeV） | 间接推断（GZK 光子、宇宙线能谱） | $n_{\text{cr}} \sim 10^{-18}$ cm$^{-3}$ |

[FACT] §2.1.2 讨论 CR 在磁场扰动中的**扩散系数**：

$$
D_{\text{cr}} \sim \frac{1}{3} \lambda_{\text{mfp}} c
$$

- $\lambda_{\text{mfp}}$：CR 的平均自由程（mean free path），由 Alfvén wave 的磁扰动 $B'/B_0$ 决定。
- 各向异性散射：平行磁场方向散射较强（$\lambda_{\parallel}$），垂直方向较弱（$\lambda_{\perp} \ll \lambda_{\parallel}$）。

[FACT] §2.1.3 讨论**CR 驱动的等离子体不稳定性**，是 CR 反馈的核心：

1. **Streaming instability**（Parker 1965）：CR 沿磁场漂移速度超过 Alfvén 速度时激发 Alfvén waves：

$$
v_{\text{drift}} > v_A \quad \Longrightarrow \quad \text{streaming instability}
$$

增长率为：

$$
\gamma_{\text{stream}} \approx k_{\parallel} (v_{\text{drift}} - v_A)
$$

2. **Bell instability**（Bell 2004）：高能 CR 的各向异性分布产生 non-resonant 电流驱动不稳定性，增强磁场 $B'$ 幅度。增长率为：

$$
\gamma_{\text{Bell}} \approx k \sqrt{\frac{\pi U_{\text{cr}}}{2 B_0}} v_{\text{A,local}}
$$

3. **Whistler instability**（注 11）：电子 CR 驱动的 electron-scale 不稳定性，主要影响高能电子。

4. **Ion-cyclotron instability**（注 12）：离子回旋波的不稳定激发。

[FACT] 注 10 指出，对 CR 驱动的不稳定性，相对磁场成 oblique 角度传播的模式通常呈 subdominant。

### 2.2.2 §2.2 Cosmic ray acceleration and escape from sources (pp. 21–32)

[FACT] 论文列出 CR 的三大类源：

| 源类型 | 能量范围 | 加速机制 | 环境 |
|--------|----------|----------|------|
| 超新星遗迹（SNR） | $\sim \text{GeV}–\text{PeV}$ | DSA | ISM |
| 活动星系核（AGN） | $\sim \text{TeV}–\text{EeV}$ | 磁重联 / DSA | 喷流/瓣 |
| 星系团内激波 | $\sim \text{TeV}$ | DSA | ICM |
| 太阳活动 | $\sim \text{MeV}–\text{GeV}$ | 重联 | 太阳风 |

[FACT] §2.2.2 系统讲解**扩散激波加速（Diffusive Shock Acceleration, DSA）**：

- DSA 的基本图像：CR 反复穿越激波面，每次穿越获得 $\Delta E / E \sim v_s / c$，其中 $v_s$ 是激波速度。
- DSA 产出的 CR 能谱在**稳态**下为幂律：

$$
\frac{dn}{dE} \propto E^{-p}, \quad p = \frac{r+2}{r-1}
$$

其中 $r$ 为压缩比（compression ratio）。对于强激波（$r=4$）：

$$
p = \frac{4+2}{4-1} = 2
$$

- 该 $E^{-2}$ 谱是 Hillas 图与观测到的银河系 CR 能谱（$E^{-2.7}$）在源谱（未经传播修正）上的预期。

[FACT] §2.2.2 还讨论了**Bell 磁场放大机制**：DSA 本身要求磁场有扰动供 CR 散射；Bell 不稳定性通过 CR 电流产生非共振波，把磁场从背景 $B_0 \sim \mu\text{G}$ 放大到 $B' \sim 100\,\mu\text{G}$ 甚至更高，从而提高 DSA 效率。

[FACT] §2.2.3（CR escape from SNR to ISM）讨论了 CR 从 SNR 内部向 ISM 逃逸的机制：

- 早期 SNR 阶段：CR 被 Bell 放大磁场磁镜限制在 SNR 内部
- 晚期 SNR 阶段（$\sim 10^4$ yr）：磁场放大停止，CR 通过扩散进入 ISM
- CR 的泄漏能谱较 DSA 稳态能谱更陡（$E^{-2.5}$ 或更陡），解释为何观测 ISM 能谱比 DSA 预期陡。

### 2.2.3 §2.3 Cosmic ray spatial transport (pp. 32–48)

[FACT] 论文系统比较**CR 传播的三种理论框架**：

| 框架 | 变量 | 假设 | 应用 |
|------|------|------|------|
| 全动理学（Fokker-Planck） | $f(x,p,\mu,t)$ | 完整 6D phase space | 理论研究 |
| One-moment CRHD | $n_{\text{cr}}, P_{\text{cr}}$ | 各向同性、无 streaming | 大尺度模拟 |
| Two-moment CRHD | $P_{\text{cr}}, j_{\text{cr}}$（压力 + 流） | 各向异性 streaming | 星系/星系团反馈 |

[FACT] §2.3.2 **One-moment CRHD** 的核心方程：

$$
\frac{\partial}{\partial t}\left[\left(\frac{P_{\text{cr}}}{\gamma_{\text{cr}}-1}\right)\right] + \nabla \cdot (P_{\text{cr}} \mathbf{u}) = -\frac{Q_{\text{cr}}}{1 + P_{\text{cr}} / (\rho c_{s,\text{eff}}^2)}
$$

其中 $Q_{\text{cr}}$ 是 CR 加热项，$c_{s,\text{eff}}^2$ 是有效声速（含 CR 压力贡献）。

[FACT] §2.3.3 **Two-moment CRHD** 同时追踪 CR 压力张量和 CR 流：

$$
\nabla \cdot \mathbf{j}_{\text{cr}} = -\frac{P_{\text{cr}} - P_{\text{cr,eq}}}{c_s \rho^{-1/2} \sqrt{P_{\text{cr,eq}} / c_s^2}}
$$

- 该框架允许 CR 沿磁场方向 streaming，同时被 streaming instability 自限制（self-regulating）。
- Ruszkowski & Begelman 2002 首次将此框架应用到 cool core 星系团。

[FACT] §2.3.4 讨论了 cosmological simulations 中的 CR 传播，包括 ENZO、AREPO、ATHENA++ 等主要代码中 CR 物理的实现。

[FACT] §2.3 中的**关键结论**：

- CR 在星系团尺度上的有效扩散系数：

$$
D_{\text{cr}} \sim 10^{28}–10^{30}\,\text{cm}^2\text{s}^{-1}
$$

- 在 ISM 中：

$$
D_{\text{cr}} \sim 3\times 10^{28}\,\text{cm}^2\text{s}^{-1} \quad (1\,\text{GeV})
$$

随能量 $E^{1/3}$ 增长（Kolmogorov turbulence 下的经典关系）。

### 2.2.4 §2.4 Radiative and non-radiative cooling (pp. 48–58)

[FACT] 论文列出 CR 的三种主要能量损失机制：

| 损失机制 | 适用粒子 | 时标 | 依赖 |
|----------|----------|------|------|
| 同步辐射（Synchrotron） | 电子 | $\sim 10^9\,B^{-2}$ yr | $B^2$ |
| 逆康普顿（IC） | 电子 | $\sim 10^9\,u_{\text{rad}}^{-1}$ yr | 辐射场能量密度 |
| pp 碰撞（hadronic） | 质子 | $\sim 10^9\,n_{\text{ISM}}^{-1}$ yr | 环境数密度 |
| 绝热损失 | 所有粒子 | $\sim$ 膨胀时标 | $\nabla \cdot \mathbf{v}$ |
| Coulomb 损失 | 低能 CR | $\ll 10^9$ yr | 环境电子数密度 |

[FACT] 论文给出图（图 2）的冷却时标对照：

$$
t_{\text{cool}} \approx \frac{3 n_e k_B T}{\Lambda(T) n_e^2}
$$

对 GeV CR 在银河系环境中，$t_{\text{cool}} \sim 10^{9}$ yr，显著长于典型的星系动力学时标（$\sim 10^{8}$ yr）。

[FACT] 在 ICM 中，CR 的冷却时标更长（因为 $n_e \sim 10^{-3}$ cm$^{-3}$），可达 $10^{10}$–$10^{11}$ yr，使 CR 能有效储存能量。

### 2.2.5 §2.5 Cosmic ray spectral transport (pp. 58–60)

[FACT] 谱传播方程（含空间扩散 + 再加速 + 能量损失）：

$$
\frac{\partial f}{\partial t} = \nabla \cdot (D(E) \nabla f) + \frac{1}{3}(\nabla \cdot \mathbf{u}) \dot{p}_{\text{acc}} + \frac{\partial}{\partial p}\left[\frac{f}{\dot{p}_{\text{loss}}} - \frac{\dot{p}_{\text{acc}}}{3} f\right] + Q_{\text{src}}
$$

- $f$：相空间分布函数
- $D(E)$：能量相关扩散系数（$\propto E^{1/3}$）
- $\dot{p}_{\text{acc}}$：再加速项（stochastic re-acceleration）
- $\dot{p}_{\text{loss}}$：能量损失项

[FACT] §2.5 讨论 **再加速（stochastic re-acceleration）** 在 CGM 和 ICM 中的作用：湍流中的随机碰撞使 CR 获得额外能量，可部分抵消 adiabatic loss，从而维持 CR 数密度。

## 2.3 关键公式

$$
\boxed{\omega - k_{\parallel} v_{\parallel} = \pm \Omega_{\text{cr}}}
$$

CR–MHD 波共振条件。

$$
\boxed{\gamma_{\text{stream}} \approx k_{\parallel}(v_{\text{drift}} - v_A)}
$$

Streaming instability 增长率。

$$
\boxed{\gamma_{\text{Bell}} \approx k \sqrt{\frac{\pi U_{\text{cr}}}{2 B_0}} v_{\text{A,local}}}
$$

Bell non-resonant instability 增长率。

$$
\boxed{p = \frac{r+2}{r-1}}
$$

DSA 稳态能谱指数（$r=4$ 时 $p=2$）。

$$
\boxed{D_{\text{cr}} \propto E^{1/3} \quad (\text{Kolmogorov turbulence})}
$$

CR 扩散系数的能量依赖（isotropic Kolmogorov）。

$$
\boxed{\nabla \cdot \mathbf{j}_{\text{cr}} = -\frac{P_{\text{cr}} - P_{\text{cr,eq}}}{c_s \rho^{-1/2} \sqrt{P_{\text{cr,eq}}/c_s^2}}}
$$

Two-moment CRHD 中 streaming 自限制。

## 2.4 关键参数

| 参数 | 典型值 | 单位 | 出处 |
|------|--------|------|------|
| CR 扩散系数（ISM, 1 GeV） | $3\times 10^{28}$ | cm$^2$s$^{-1}$ | §2.3 |
| CR 扩散系数（ICM） | $10^{28}–10^{30}$ | cm$^2$s$^{-1}$ | §2.3 |
| 强激波压缩比 | $r=4$ | — | §2.2 |
| DSA 谱指数（$r=4$） | $p=2$ | — | §2.2 |
| 再加速指数（Kolmogorov） | $\delta = 1/3$ | — | §2.5 |
| CR 冷却时标（ISM, GeV） | $\sim 10^9$ | yr | §2.4 |
| CR 冷却时标（ICM, GeV） | $\sim 10^{10}–10^{11}$ | yr | §2.4 |
| Bell 放大磁场 | $B' \sim 100\,\mu\text{G}$ | μG | §2.2 |
| 背景磁场 | $B_0 \sim 1–3$ | μG | §2.1 |

## 2.5 图表分析

**Figure 2**（Cooling times）— 论文第 53 页附近，给出不同 CR 能量（横轴 $10^4$–$10^{11}$ GeV）下各冷却机制的时标曲线：

### 1. 图的目的
比较 CR 不同损失机制（同步辐射、IC、pp、绝热）随能量和环境的时标。

### 2. 坐标轴
- 横轴：CR 能量（$10^4$–$10^{11}$ GeV）
- 纵轴：$t_{\text{cool}}$（yr），对数坐标，范围 $10^4$–$10^{15}$ yr

### 3. 图中元素
- 同步辐射（实线，不同磁场强度）
- 逆康普顿（虚线，不同辐射场）
- pp 碰撞（点线，不同环境数密度）
- Hubble 时标参考线

### 4. 关键观察
- GeV–TeV 区间，pp 主导质子损失；
- TeV 以上，同步+IC 主导电子损失；
- 所有曲线都超过星系动力学时标（$\sim 10^8$ yr），支持"长冷却时间"论点。

### 5. 数值信息
- $B \sim 3\,\mu\text{G}$ 时，GeV 电子 $t_{\text{synch}} \sim 10^{12}$ yr
- $n \sim 10^{-2}$ cm$^{-3}$ 时，GeV 质子 $t_{\text{pp}} \sim 10^9$ yr

### 6. 作者的解释
图 2 用于支撑引言中的核心论点：**CR 的冷却时标远长于星系/星系团动力学时标**，使其成为有效的"慢热"机制。

### 7. 与正文的关系
图 2 是 §2.4 的总结图，直接链接到 §3 Astrophysical systems 中"为什么 CR 能在星系团尺度提供持续加热"的论证。

### 8. 物理意义
- 在 ICM 极端低密度环境下（$n \sim 10^{-3}$ cm$^{-3}$），pp 冷却时标 $\sim 10^{10}$ yr，CR 几乎不损失能量，成为 ICM 压力的重要组分。

### 9. 需要注意的问题
[CRITIQUE] 图 2 未包含 **磁重联中的 CR 损失** 或 **再加速对净冷却的补偿**——这两点在 §2.5 讨论。

## 2.6 作者的逻辑

```
[核心问题] CR 如何与等离子体耦合并传递能量？
  → §2.1 [机制] 波–粒相互作用 → resonance condition → streaming + Bell instability
    → §2.2 [产生] DSA 在激波加速 CR → Bell 放大磁场 → CR 逃逸 SNR
      → §2.3 [传播] Fokker-Planck → One-moment / Two-moment CRHD
        → §2.4 [损失] 同步/IC/pp/绝热 — 比较时标
          → §2.5 [谱] 扩散+再加速+损失 → 谱演化方程
```

[INTERPRETATION] 作者刻意把 §2 设计为"完整闭合的 CR 物理工具箱"：读者掌握 §2 后，就能理解 §3–§4 中所有 astrophysical 现象的物理原因。§2.1（不稳定性）和 §2.3（hydrodynamics）是 §3（galactic winds、cooling flow）的核心物理支撑。

## 2.7 我的理解

### 2.7.1 CRHD 两个 moment 框架的物理意义

[INTERPRETATION]

- **One-moment CRHD**：把 CR 当作"附加流体"，只有压力贡献。假设 CR 分布各向同性，忽略 streaming。物理意义是"CR 只通过压力影响流体"。
- **Two-moment CRHD**：额外追踪 CR 流（$j_{\text{cr}}$），允许 CR 沿磁场 streaming，但由 streaming instability 自限制。物理意义是"CR 有 streaming 但有自调节机制"。

[INTERPRETATION] 从模拟的角度看，two-moment 比 one-moment 多一个动量方程，计算成本更高；但 two-moment 能重现 **cooling flow suppression** 的关键机制（Ruszkowski & Begelman 2002），one-moment 无法做到。

### 2.7.2 [CRITIQUE] §2.1 中 streaming instability 的适用条件

[CRITIQUE] 论文在 §2.1.3 讨论 streaming instability 时使用了 Parker 1965 的线性增长率 $\gamma \approx k_{\parallel}(v_{\text{drift}} - v_A)$，但该增长率只适用于 $v_{\text{drift}}$ 略微超过 $v_A$ 的弱超临界情形。当 $v_{\text{drift}} \gg v_A$（如 Bell 情形），增长率由 non-resonant Bell 不稳定性主导，线性 streaming 理论失效。论文对此在 §2.2 的 Bell 部分有补充，但 §2.1.3 中未明确标注适用范围。

### 2.7.3 [CRITIQUE] DSA 谱的修正

[CRITIQUE] 论文给出 DSA 稳态谱指数 $p = (r+2)/(r-1)$，这是**经典 DSA 的"薄激波"近似结果**。实际上：

1. Bell 磁场放大使激波有效压缩比 $r_{\text{eff}} > 4$，从而使 $p < 2$（更硬）
2. 有限激波寿命（aging effect）使逃逸 CR 的谱更陡
3. 激波几何（曲率、3D 结构）改变局部压缩比

论文在 §2.2.3 有提到 escape 使谱变陡，但未系统给出 $p_{\text{escape}}(r, t)$ 的一般关系。

### 2.7.4 关于 CR 传播的 anisotropy

[CRITIQUE] §2.3 中 CR 传播的 anisotropy 是"教科书问题"：磁场方向上的扩散远快于垂直方向（$\lambda_{\parallel} / \lambda_{\perp} \sim 100–1000$）。Two-moment CRHD 通过 streaming instability 部分处理了这个各向异性，但**在数值实现上仍需近似**（如假设 CR 沿 B 方向 streaming，忽略垂直扩散）。这对 cool core 星系团的模拟结果有直接影响（见 §3.5）。

### 2.7.5 [INTERPRETATION] CR 反馈与 AGN 反馈的关联

[INTERPRETATION] 论文在 §2.2 明确将 AGN 加速作为 CR 的重要源之一。物理上是：

- AGN 喷流/瓣内部激波加速 CR（TeV–EeV）
- CR 沿磁力线扩散到 ICM 大尺度
- CR 通过 streaming instability 加热 ICM
- 这一机制与"AGN 通过机械做功直接加热 ICM"互补或替代

[CRITIQUE] 论文对 AGN–CR 耦合的定量讨论集中在 §3.5，§2 中只给出定性描述。对于想直接应用 AGN–CR 耦合的读者，需要从 §3.5 和 §4.6 获取具体公式和参数。

## 2.8 潜在问题与值得关注的地方

### 2.8.1 Bell instability 的线性 vs. 非线性阶段

[CRITIQUE] §2.1.3 和 §2.2.2 讨论 Bell 不稳定性时主要给出**线性增长率**。实际上 Bell 不稳定性在非线性饱和后：

- 磁场放大程度：$B' / B_0 \sim 10–100$
- 饱和后 CR 散射进入"turbulent transport"模式，扩散系数改变
- 非线性饱和机制（波–波相互作用、磁重联）尚未完全理解

[FACT] 论文在 §2.2.2 提及"non-linear Bell amplification"，但未给出非线性饱和后的扩散系数公式。

### 2.8.2 Two-moment CRHD 的数值耗散

[CRITIQUE] §2.3.3 的 two-moment 方程在数值实现上要求 **MHD solvers 满足 positivity（$P_{\text{cr}} \geq 0$）和 causality（$|j_{\text{cr}}| \leq c P_{\text{cr}}$）** 约束。标准 Godunov 格式可能产生负压力或超光速 streaming。论文未讨论这些数值技巧，但文献中（e.g., Ohm et al. 2013, 2015）有具体处理。

### 2.8.3 关于 CR 光谱传播的简化

[CRITIQUE] §2.5 的 spectral transport 方程在 astrophysical 应用（§3–§4）中常被简化为"single energy bin"或"single power-law index"，以节省计算成本。这种简化会丢失 CR 谱在冷却、再加速过程中的弯曲和截断特征，直接影响 γ 射线能谱预测（§4.1、§4.3）。

### 2.8.4 §2 与 §3 的接口

[INTERPRETATION] §2 提供的物理框架（streaming instability、two-moment CRHD、cooling times）是 §3 Astrophysical systems 中所有 astrophysical 现象（galactic winds、cooling flow suppression、CGM thermal instability）的**共同物理语言**。理解 §2 中的 streaming instability 是理解 §3 中"CR 如何驱动 wind"和"CR 如何抑制 cooling flow"的关键。

---

## 元数据

```yaml
chapter: 2
pages: "11–60"
subsections: ["2.1", "2.2", "2.3", "2.4", "2.5"]
key_formulas:
  - "ω - k_∥ v_∥ = ± Ω_cr (resonance)"
  - "γ_stream ≈ k_∥ (v_drift - v_A)"
  - "γ_Bell ≈ k √(π U_cr / (2 B_0)) v_A"
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
