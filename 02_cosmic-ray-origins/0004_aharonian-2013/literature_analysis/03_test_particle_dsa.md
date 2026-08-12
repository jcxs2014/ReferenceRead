# 3. The theory of diffusive shock acceleration of test particles

> 本章属于：The Origin of Galactic Cosmic Rays（Blasi, 2013, arXiv:1311.7346）
>
> 上一章：`02_sn_r_premises.md`
>
> 下一章：`04_nl_dsa.md`

## 3.1 本节核心内容

- 建立 SNR 演化时间标度（Sedov-Taylor 半径/时间）。
- 无碰撞激波（collisionless shock）的形成机制与等离子体时间标度。
- 粒子在磁场与 Alfvén 波背景下的输运：投掷角扩散、空间扩散系数 D(p)。
- **DSA 传输方程**（Skilling 1975a）的推导，得出 test-particle 谱指数 α = 3r/(r−1)，强激波极限 α→4，即微分能量谱 n(ϵ)∝ϵ⁻²。
- **三种最大能量定义**：时间限制、空间限制、几何限制；指出 SNR 要达到 PeV 需要磁化放大 ~10–100 倍。

## 3.2 原文内容（要点摘录）

- [FACT] §3.1 无碰撞激波：地球大气激波靠分子碰撞；ISM 中的 SNR 激波属于 collisionless shock，由**电磁不稳定性**集体效应形成（Treumann 2009）。
- [FACT] 非相对论条件 v ≪ c 等价于 Alfvenic Mach 数 M_A ≪ 1.3 × 10⁵ · n¹/² cm⁻³ · B⁻¹ µG（Eq. 9）。
- [FACT] Coulomb 热化时间分层：电子自热化 τ_eq,ee 最快，质子自热化 τ_eq,pp 最慢；对典型 SNR 参数 τ_eq,ee ≈ 1200·(n/1 cm⁻³)⁻¹·(T_e/10⁸ K)³/² 年，τ_eq,pp ≈ 2.3×10⁶·(n/1)⁻¹·(T_p/10⁸ K)³/² 年。
- [FACT] 对于强激波 T_p = (3/16) m_p V²_sh / k_B，故 kT_e ≈ (m_e/m_p) kT_p（Eq. 13）：电子永远跟不上质子温度。
- [FACT] 年轻 SNR 的电子-质子热化时间可达数千年，远超遗迹年龄 → 电子不热化是可观测特征（如 [O] 离子非平衡辐射）。
- [FACT] 平行激波：Weibel 不稳定性产生小尺度磁场 → 耗散机制。
- [FACT] 注入机制仍"one of the most poorly known aspects"。PIC 模拟（Spitkovsky 2008a,b；Sironi & Spitkovsky 2011；Gargaté & Spitkovsky 2012）提供注入物理的新视角。

### §3.2 粒子输运

- [FACT] Fermi 二阶加速：平均能量增益 ⟨ΔE/E⟩ = (4/3)(V/c)²，标度是 (V/c)² → "second order"。
- [FACT] ISM 中 Alfvén 速度 v_A = B/√(4πρ) = 2 B_µ · n_i,cm⁻³ km/s，太小 → 二阶加速不重要。
- [FACT] 粒子在均匀 B₀ + Alfvén 波背景下的运动：Larmor 频率 Ω = qB₀/(mcγ)，v_z = vµ，回旋半径 r_L = v/Ω。
- [FACT] 投掷角扩散系数（Q-LT）：ν = ⟨ΔθΔθ/Δt⟩ = (π/4)(kP(k)/(B₀²/8π))·Ω（Eq. 29/30）。
- [FACT] 空间扩散系数：D(p) ≈ (1/3) r_L v / F，其中 F = kP(k)/(B₀²/8π)（Eq. 32）。
- [FACT] CR 在星系被约束 ~10⁷ yr → D ~ 10²⁹ cm²/s → 共振尺度需 δB/B ~ 6 × 10⁻⁴。

### §3.3 DSA 传输方程

- [FACT] 激波压缩比 r = u₁/u₂ = (4 M²_s)/(M²_s + 3) → 强激波 r→4（Eq. 33）。
- [FACT] 传输方程（Skilling 1975a，shock 静止、平行、定态）：
$$u \frac{\partial f}{\partial z} = \frac{\partial}{\partial z}\left(D\frac{\partial f}{\partial z}\right) + \frac{1}{3}\frac{du}{dz}p\frac{\partial f}{\partial p} + Q \quad (34)$$
- [FACT] 注入项（δ 函数近似）：Q(p, x) = η n₁ u₁ / (4π p²_inj) · δ(p−p_inj)·δ(z)（Eq. 35）。
- [FACT] 关键结果（Eq. 40, 41）：
$$f_0(p) = \frac{3r}{r-1}\,\eta n_1\frac{1}{4\pi p^2_{\rm inj}}\left(\frac{p}{p_{\rm inj}}\right)^{-\frac{3r}{r-1}}$$
$$\alpha = \frac{3r}{r-1} \xrightarrow{M_s\to\infty} 4$$
- [FACT] "The spectrum of accelerated particles is a power law in momentum (and not in energy as is often assumed in the literature)。" 相对论下 n(ϵ)∝ϵ⁻²，非相对论下 n(ϵ)∝ϵ⁻³/²。
- [FACT] "The shape of the spectrum of the accelerated particles does not depend upon the diffusion coefficient."

### §3.4 最大能量

- [FACT] 单次循环的能量增益（Bell 1978a）：
$$\left\langle\frac{E'_1 - E_1}{E_1}\right\rangle_{\mu_1,\mu_2} = \frac{4}{3}\beta \quad (44)$$
标度为 β¹ → "first order Fermi"。
- [FACT] 加速时间（Drury 1983；Lagage & Cesarsky 1983a,b）：
$$\tau_{\rm acc} = \frac{3}{u_1 - u_2}\int_0^p \frac{dp'}{p'}\left[\frac{D_1(p')}{u_1}+\frac{D_2(p')}{u_2}\right] \quad (47)$$
- [FACT] 时间约束（Eq. 48, 49）：τ_acc(p_max) ≤ τ_SNR → 得到条件
$$F(k_{\rm min}) \approx \frac{1}{3}\frac{c}{V_s}\frac{r_L(p_{\rm max})}{R_{\rm SNR}}$$
- [FACT] 关键推论：r_L(p_max) = 1 pc · (E/10¹⁵ eV) · B⁻¹_µ；由于 c/V_s ~ 100 而 r_L/R_SNR ~ 0.1，**必须 F(k_min) ≫ 1**，即 δB/B₀ ≫ 1。
- [FACT] "Without such a mechanism ... the maximum energy that could be achieved at ~1000 years old SNR with V_sh=3000 km/s is only a fraction of GeV."
- [FACT] 三种最大能量定义：
  1. **时间约束** τ_acc(p_max) ≤ τ_SNR（§3.4 主线）。
  2. **空间约束** D(p_max)/V_sh ≈ χ·R_sh（Eq. 51），在 Sedov 阶段更严。
  3. **几何约束** r_L(p_max) = R_sh，作为上界（高估 p_max 约 c/V_sh 因子）。

## 3.3 关键公式汇总

| 编号 | 公式 | 含义 |
|------|------|------|
| 4 | V_ej = 10000 E₅₁^½ · M_ej,⊙⁻¹/² km/s | 抛射物初速 |
| 5 | c_s ≈ 11 (T/10⁴ K)^½ km/s | ISM 声速 |
| 6 | M_s ≈ 900 E₅₁^½ M_ej,⊙⁻¹/² (T/10⁴ K)⁻¹/² | 抛射物 Mach 数 |
| 7 | R_ST ≈ 2 M_ej,⊙^1/3 (n_ISM/1 cm⁻³)⁻¹/³ pc | Sedov-Taylor 半径 |
| 8 | T_ST ≈ 200 M_ej,⊙^5/6 E₅₁⁻¹/² (n_ISM/1)⁻¹/³ yr | Sedov 起始时间 |
| 9 | M_A ≪ 1.3×10⁵ n¹/² B⁻¹ | 非相对论激波条件 |
| 10 | τ_eq = 3m₁m₂k³/²_B / [8(2π)^½ n q⁴ lnΛ] · (T₁/m₁+T₂/m₂)^3/² | Coulomb 热化时间（Spitzer 1962） |
| 17–20 | Rankine-Hugoniot 跃变条件（强激波 r=4, T₂/T₁ = 5M²/16） | 质量-动量-能量守恒 |
| 21 | kT₂ = 3/16 m_p u₁² | 强激波后温度 |
| 32 | D(p) ≈ (1/3) r_L v / F | 空间扩散系数 |
| 33 | r = 4M²_s/(M²_s+3) → 4 | 压缩比 |
| 40 | f₀(p) ∝ (p/p_inj)^(-3r/(r-1)) | test-particle 动量谱 |
| 41 | α = 3r/(r−1) → 4 | 动量谱指数 |
| 44 | ⟨ΔE/E⟩ = (4/3)β | 单次循环能量增益 |
| 47 | τ_acc = 3/(u₁−u₂) ∫ dp'/p' [D₁/u₁ + D₂/u₂] | 加速时间 |
| 48 | F(k_min) ≈ (1/3)(c/V_s)(r_L/R_SNR) | PeVatron 条件 |
| 50 | r_L(p_max) = 1 pc · (E/10¹⁵ eV) · B⁻¹_µ | 回旋半径参考值 |
| 51 | D(p_max)/V_sh ≈ χR_sh | 空间约束最大能量 |

## 3.4 关键数值

| 物理量 | 典型值 |
|--------|--------|
| V_ej | ~10⁴ km/s |
| M_s | ~900 |
| R_ST | ~2 pc |
| T_ST | ~200 yr |
| τ_eq,ee | ~10³ yr |
| τ_eq,pp | ~10⁶ yr |
| kT_p | 5.6×10⁸ (V_sh/5000 km/s)² K |
| D(1 GeV) | ~10²⁹ cm²/s |
| δB/B 约束（10⁷ yr 困住） | ~6×10⁻⁴ |
| r_L(10¹⁵ eV, 1µG) | 1 pc |

## 3.5 图表分析

参见 `09_figures_tables.md`（Figure 4 SNR 形态、Figure 5 带电粒子在磁场中的轨迹、Figure 6 test-particle 加速示意）。

## 3.6 作者的逻辑

- 从 SNR 动力学的**时空框架**（§3 前半）→ 到粒子如何在磁场中输运（§3.2）→ 到把两者缝合在一起的 DSA 传输方程（§3.3）→ 到能达到的最大能量（§3.4）。
- [INTERPRETATION] §3.4 的核心论证是**"SNR 要达到 PeV 必须依赖磁场放大"**——这一步为下一章（§4）非线性理论埋下伏笔：因为 test-particle 理论里 F≪1 的假设在 p_max 处失效，δB≪B₀ 的准线性理论在最强散射点必然崩溃。

## 3.7 我的理解

- [FACT] α=4 意味着动量谱 f(p)∝p⁻⁴，能量谱 dN/dE∝E⁻²（相对论）——这是 SNR 范式的"理论招牌"。
- [INTERPRETATION] 作者刻意强调 spectrum 与 D 无关（"good news"），但代价是 test-particle 理论**不能内禀地给出 p_max**，必须靠外部边界条件。
- [CRITIQUE] 作者对"注入（injection）"的处理比较保守（"one of the most poorly known aspects"），没有进一步展开 dust sputtering（Meyer, Ellison）在重核加速中的作用。
- [CRITIQUE] §3.2 提到的粒子垂直于 B 场输运、non-linear guiding center theory 等内容对 CR 传播至关重要，但作者只做了介绍——这些正是 §6.4（SNR-MC 各向异性扩散）的理论基础。

## 3.8 潜在问题与值得关注的地方

- [CRITIQUE] Test-particle 假设要求 ξ_CR ≪ 1，而 §2 推导出的 ξ_CR ~10% 已接近上限——为 §4 非线性理论的出现提供动因。
- [CRITIQUE] DSA 谱与 D 无关，但 p_max 由 D 决定——作者已指出这种**解耦**导致"理论预测的谱斜率很干净，但最大能量完全由我们不知道的磁化放大机制决定"。
- **信息缺失**：文中未给出具体 SNR 上应用上述估计的案例，这在 §6.3（Tycho 案例）才被补齐。
