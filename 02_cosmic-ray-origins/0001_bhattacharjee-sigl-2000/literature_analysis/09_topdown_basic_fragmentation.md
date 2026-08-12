> 本章属于：Bhattacharjee & Sigl (1999), Phys. Rep. 320, 1–150
>
> 上一章：`08_acceleration_sources.md`
>
> 下一章：`10_cosmic_strings.md`

---

# 9. Top-down Scenario: Basic Idea & Fragmentation (§6.1–6.3, p. 48–58)

## 9.1 本节核心内容

- Top-down 场景基本思想：超重 X 粒子衰变 → 强子化 → 高能光子/中微子/核子。
- X 粒子衰变**必须满足**三个基本条件：(a) 在近代衰变（~100 Mpc 内）；(b) m_X ≫ 10¹¹ GeV；(c) 数密度/衰变率足够大。
- 强子化理论：三阶段 factorization（parton cascade → 非微扰 confinement → 衰变）；LPHD 假设；MLLA 极限谱。
- X 粒子衰变率基准估算：~10³⁵ Mpc⁻³ yr⁻¹ (m_X = 10¹⁶ GeV 时)。

## 9.2 §6.1 The Basic Idea

### 9.2.1 Top-down 动机 [FACT]

- DSAM 加速是**自限过程**：粒子回旋半径 r_g = E/(ZeB) ≤ R (源尺寸) → E_max ~ ZeBR。
- EHECR > 10¹¹ GeV 要求 R·B 极大；实际还须考虑传播损失与源距离问题。
- **Top-down**：X 粒子（m_X > 10¹¹ GeV）衰变 → 无需加速。
- 历史溯源：**Lemaître "Primeval Atom"**（"the cosmic rays were glimpses of the primeval fireworks" [380]）。

### 9.2.2 Top-down 三条件 [FACT]

1. **(a) 近期衰变**：X 在**近期宇宙学时代**衰变，或源距离 <~100 Mpc。例外：UHE ν + RNB → Z⁰ 共振（Z-burst，见 §5.2.4）。
2. **(b) m_X ≫ 10¹¹ GeV**。
3. **(c) 数密度/衰变率** 足够大。

### 9.2.3 X 衰变链 [FACT]

```
X → (夸克, 轻子) → [夸克强子化: jets of light mesons (π) + baryons (N)]
→ π⁰ → 2γ
→ π± → μ ± ν_μ → (e ±) + ν_e + ν̄_μ
```
- **直接产生**：光子、中微子、带电轻子 + 少量核子。
- 核子占 hadron 总数 ~3–10% [FACT, collider 数据]。

## 9.3 §6.2 X Particles → Observable Particles

### 9.3.1 强子化三阶段 [FACT]

1. **Parton Cascade**（微扰 QCD，截止 ⟨k_⊥²⟩^(1/2)_cut-off ~ 1 GeV）
2. **Non-perturbative confinement**（LUND string [381] / cluster [382] 模型）
3. **Unstable hadron 衰变**

### 9.3.2 LPHD (Local Parton-Hadron Duality) [FACT]

**核心假设**：非微扰强子化发生在 ~hadron mass 的低虚拟尺度，仅涉及低动量转移和局域色重排，**不显著改变 parton 谱形状**。强子化效应仅贡献整体归一化常数 K(Y)。

```
x dN_h/dx = K(Y) · x dN_part/dx          (58)
```

**MLLA 极限谱 (公式 57)**：
```
x dN_part/dx = (4C_F/b) · Γ(B) · ∫₋π/2^π/2 dℓ/π · e^(−Bα) ·
               [(cosh α + (2ξ/Y − 1)sinh α) / ((4N_c/b)Y · (α/sinh α))]^(B/2)
               · I_B[{16N_c/(bY) · (α/sinh α) · (cosh α + (2(ξ/Y)−1)sinh α)}]^(1/2)
```
其中：
- ξ = ln(1/x), Y = ln(E_jet/Λ_eff), α = tanh⁻¹(1−2ξ/Y) + iℓ
- B = a/b, a = 11N_c/3 + 2n_f/(3N_c²), b = (11N_c − 2n_f)/3
- N_c = 3, C_F = 4/3, I_B = 修正 Bessel 函数

**拟合参数** [FACT]：
- Λ^ch_eff ~ 250 MeV（LEP Z-resonance, E_cm ~ 90 GeV）
- K ~ 1.3（LEP 能量）

### 9.3.3 ξ_max 位置 (公式 59) [FACT]

```
ξ_max = Y · [1/2 + sqrt(C/Y − C/Y²)]
C = a²/(16bN_c)
```
- 该峰的存在直接关联 QCD 色相干效应导致的软胶子倍增抑制。
- LEP 数据确认 ξ_max 的 Y 演化 [388]。

### 9.3.4 高能量极限下的高斯近似 (公式 60)

```
x dN_h/dx ∝ (1/(σ·√(2π))) · exp[−(ξ − ξ_max)² / (2σ²)]
2σ² = [bY³/(36N_c)]^(1/2)
```

### 9.3.5 Hill 谱 (公式 61, 62) [FACT]

```
dN_h/dx ≃ (3/2) · 0.08 · exp[2.6·q·ln(1/x)] / [(1−x)² · (x/(q·ln(1/x)))^(−1)]     (61)
dN_h/dx ≃ (15/16) · x^(−3/2) · (1−x)²                                         (62)
```
- nf = 6；3/2 因子包含中性 π⁰。
- x ≪ 1（EHE 能区）：
  - (61) → **dN_h/dE ∝ E^(−1.3)** (α ~ 1.3)
  - (62) → **dN_h/dE ∝ E^(−1.5)** (α ~ 1.5)

### 9.3.6 SUSY 对强子化的影响 [FACT]

若 SUSY 在 M_SUSY ~ 1 TeV "打开"：
- parton cascade 中 squarks/gluinos 与普通 quarks/gluons 等概率参与（Q̃² > M_SUSY²）。
- 一旦 Q̃² < M_SUSY²，SUSY 粒子 decouple → 最终衰变为 LSP。
- **Berezinsky & Kachelriess [399]**：LSP 可能带走 ~40% 的 jet 总能量！
- SUSY MLLA 谱：a → a_SUSY = 11N_c/3；b → b_SUSY = 9 − n_f → ξ_max 移到更高 ξ（更低能量）。

### 9.3.7 硬 vs 软谱 [FACT]

- **α = 2 是分界**：
  - 软谱 (α > 2)：粒子数与总能量均由低能端主导。
  - **硬谱 (1 < α < 2)**：总能量由少数极高能粒子携带 → 更"自然"产生 EHECR。
- Top-down 一般 α ~ 1.3–1.5（硬）→ 预测 GZK 截断后有**"recovery"** [200]。
- 硬谱也可能自然产生 "gap" [403]。

## 9.4 §6.2.2 Nucleon/Photon/Neutrino Injection Spectra

### 9.4.1 注入谱公式 [FACT]

设 X 平均衰变为 Ñ 体（N_q 夸克 + N_ℓ 轻子），能量均分：

**核子 (公式 63)**：
```
Φ_N(E_i, t_i) = ṅ_X(t_i) · N_q · f_N / Ñ · (m_X / x²) · (dN_h/dx)
其中 x = Ñ E_i / m_X
```

**光子 (公式 64, π⁰ → 2γ)**：
```
Φ_γ(E_i, t_i) ≃ 2 ∫_{E_i}^{m_X/Ñ} dE/E · Φ_{π⁰}(E, t_i)
Φ_{π⁰} ≃ (1/3) · ((1−f_N)/f_N) · Φ_N
```

**中微子 (公式 65, π± → μ± ν_μ)**：
```
Φ_{ν_μ + ν̄_μ}(E_i) ≃ 2.34 ∫_{2.34 E_i}^{m_X/Ñ} dE/E · Φ_{π±}(E, t_i)
Φ_{π±} ≃ 2 Φ_{π⁰}
```
- 每个 μ 衰变再产生 ν_e + ν̄_μ → 每个 π± → 3 ν。
- **总 ν_μ + ν̄_μ ≈ 2× (65)；总 ν_e + ν̄_e ≈ (65)**。

### 9.4.2 相对丰度 [FACT]

若 f_N ~ 3%：
- Φ_{π⁰}/Φ_N ≃ 10
- Φ_{π±}/Φ_N ~ 20
- → **光子与中微子在数上占主导**（至少 ×10 于核子）。

**关键 Top-down 标志** [FACT]：**γ/CR 通量比 > 1** 在足够高 EHECR 能区（§7 讨论）。

**Top-down 与 Bottom-up 关键区别**：
- Top-down：ν, γ 是**初级**产物（直接从 π 衰变）。
- Bottom-up：ν, γ 是**次级**（来自 GZK 相互作用产生的 π）。

## 9.5 §6.2.3 Benchmark Calculation (公式 68–69)

### 9.5.1 单 X 粒子光子注入谱 (公式 66) [FACT]

假设 X → q ℓ（2-body），dN_γ/dE_γ ∝ E_γ^(−α)，0 < α < 2：
```
dN_γ/dE_γ = 0.6 m_X / (2 − α) · (f_π/0.9) · (2E_γ/m_X)^(−α)
```

### 9.5.2 光子通量 (公式 67)

```
j_γ(E_γ) ≃ (1/(4π l(E_γ))) · ṅ_X · dN_γ/dE_γ
```

### 9.5.3 X 粒子衰变率要求 (公式 68)

```
(ṅ_X,0)_{EHECR} ≃ 1.2×10⁻⁴⁶ · (l(E_γ)/10 Mpc)⁻¹ · (E²j(E)/1 eV cm⁻² s⁻¹ sr⁻¹) ·
                  (2E/10¹⁶ GeV)^(α−1.5) · (m_X/10¹⁶ GeV)^(1−α) · (0.5/(2−α)) · (0.9/f_π)  cm⁻³ s⁻¹
```

### 9.5.4 能量注入率 (公式 69)

```
(Q_0)_{EHECR} ≃ 1.2×10⁻²¹ · (l(E_γ)/10 Mpc)⁻¹ · (E²j(E)/1 eV cm⁻² s⁻¹ sr⁻¹) ·
                (2E/10¹⁶ GeV)^(α−1.5) · (m_X/10¹⁶ GeV)^(2−α) · (0.5/(2−α)) · (0.9/f_π)  eV cm⁻³ s⁻¹
```

### 9.5.5 数值示例 [FACT]

EHECR 通量标度 E²j ~ 1 eV cm⁻² s⁻¹ sr⁻¹ at E = 10¹¹ GeV, m_X = 10¹⁶ GeV, α = 1.5, f_π = 0.9：
```
ṅ_X ≃ 1×10³⁵ Mpc⁻³ yr⁻¹ ≃ 13 AU⁻³ yr⁻¹
```
即 **每 10 Mpc 半径体积内，每年 ~10 个 X 粒子衰变**（每个太阳系大小）。

作者承认：可能高估一个量级 [206]。

## 9.6 §6.3 Cosmic Topological Defects: General

### 9.6.1 TD 分类 [FACT]

- Magnetic monopoles
- Cosmic strings
- Domain walls
- Superconducting cosmic strings
- 混合系统 (necklaces 等)

产生于 GUT 相变；核心尺寸 ~ η⁻¹（η 为 Higgs VEV）。

### 9.6.2 与暴胀的兼容性 [FACT]

- 暴胀稀释了早期 TD → 看似矛盾。
- 但 **preheating 非热相变** [412,413] 可在暴胀后产生 TD：
  - inflaton 振荡通过 parametric resonance → 大场涨落 → 对称性恢复 → 再对称破缺 → TD 形成。
- 实验室验证：³He 超流相变中的 vortex-filament 形成（毫开尔文温度）→ Kibble-Zurek 机制的确认 [409]。

### 9.6.3 TD 质量标度 [FACT]

| TD 类型 | 质量标度 |
|---|---|
| Monopole | ~ T_c ~ η |
| Cosmic string 线质量 μ | ~ η² |
| Domain wall 面密度 | ~ η³ |

若 GUT 破缺：η ~ 10¹⁶ GeV → m_X ~ 10¹⁶ GeV。

### 9.6.4 历史时间线 [FACT]

| 时间 | 事件 |
|---|---|
| 1982 | Callan [414]: 弦环坍缩产生 X；Rubakov [415]: 单极子湮灭 → baryon asymmetry |
| 1983 | Hill [392]: monopolonium 衰变 → 高能粒子 |
| 1984 | Schramm & Hill [404]: 这些高能粒子即 EHECR |
| 1985 | Witten [420]: superconducting string |
| 1986 | OTW [421], HSW [393]: SCS 载流子发射 → UHECR |
| ~1986 | 弦 cusp evaporation [394,395], 环坍缩 [397,396] |
| 1990s | [200] 一般参数化 [178] γ/CR 标志 |

## 9.7 关键数值速查

| 量 | 值 |
|---|---|
| Top-down 三条件 | (a) 近期衰变/源 < 100 Mpc; (b) m_X ≫ 10¹¹ GeV; (c) 足够衰变率 |
| 核子占强子数 | 3–10% |
| Λ^ch_eff (LEP fit) | 250 MeV |
| Hill 谱 α (x ≪ 1) | 1.3 (eq.61), 1.5 (eq.62) |
| SUSY LSP 能量份额 | ~40% [399] |
| (ṅ_X,0) EHECR 基准 | ~10³⁵ Mpc⁻³ yr⁻¹ (m_X=10¹⁶ GeV) |
| (Q_0) EHECR 基准 | ~10⁻²¹ eV cm⁻³ s⁻¹ |
| M_X GUT 典型 | 10¹⁶ GeV |

## 9.8 [CRITIQUE]

- [FACT] LPHD + MLLA 仅在 ~100 GeV 被实验验证 → 外推到 > 10¹⁴ GeV 有**巨大不确定性**。
- [FACT] Monte Carlo (HERWIG/JETSET) 与 MLLA+LPHD 在 m_X ≫ 10³ GeV 处显著不同 [391]。
- [FACT] 强子产额在 x ~ 0.2–0.4 处反常高，与"介子主导"直觉矛盾（机制不明）。
- [FACT] **Berezinsky & Kachelriess [399] 提出的 LSP 效应**（带走 40% 能量）对任何 TD 场景都是关键修正，需纳入归一化。
