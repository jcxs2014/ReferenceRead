> 本章属于：Bhattacharjee & Sigl (1999), Phys. Rep. 320, 1–150
>
> 上一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/03_figures.md|03_figures.md]]
>
> 下一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/05_neutrinos_exotic_particles.md|05_neutrinos_exotic_particles.md]]

---

# 4. Propagation & GZK Cutoff (§4.1–4.2, p. 16–22)

## 4.1 本节核心内容

- 建立**传播长度、能量衰减长度、CEL 近似**的一般性框架（公式 7–12）。
- **GZK 效应**详述：质子 + CMB 光子的 photo-pion 阈值、截面、相互作用长度 ~6 Mpc。
- 其他损失机制：PPP（对产生）、红移、中子 β-衰变、核的光致分裂（Giant Dipole Resonance）。
- **UHE 光子的 EM 级联**（pair production + inverse Compton）：级联深度、截止能量 ~100 GeV、E⁻¹·⁵ 堆积谱。
- 高 QED 过程（双对产生 DPP、三对产生 TPP）在 EHE 能区的重要性。

## 4.2 §4 起始的一般记号与公式 [FACT]

### 4.2.1 相互作用长度 (公式 7)

```
l(E)⁻¹ = ∫dε · n_b(ε) · ∫₋₁⁺¹ dμ · (1 − μββ_b)/2 · σ(s)
```
- n_b(ε)：背景粒子单位能量数密度
- β_b = (1 − m_b²/ε²)^(1/2)
- β = (1 − m²/E²)^(1/2)
- μ：入射动量夹角余弦
- σ(s)：总截面
- **质心能量平方** (公式 8)：
```
s = m_b² + m² + 2εE(1 − μββ_b)
```

### 4.2.2 能量衰减长度 (公式 9)

通过引入**非弹性度** η(s) 定义能量衰减长度：
```
η(s) ≡ 1 − (1/σ(s)) · ∫dE' · E' · (dσ/dE')(E', s)
```
- E' 为"leading particle"（携带最多能量的反冲粒子）的归一化能量。

### 4.2.3 CEL 近似下的"扩散方程" (公式 10)

```
∂_t n(E) = −∂_E [b(E) · n(E)] + Φ(E)
```
- b(E) = E / l_E(E)：能量损失率
- Φ(E)：本地注入谱
- 适用条件：leading 粒子与 non-leading 粒子性质不同，且 η(s) ≪ 1

### 4.2.4 河外各向同性源的积分公式 (公式 11, 12)

对物质主导平坦宇宙 (Ω₀ = 1)：
```
j(E) = (3/(8πt₀)) · ∫₀^{z_i,max} dz_i · (1+z_i)⁻^(11/2) · (dE_i(E,z_i)/dE) · Φ(E, z_i)
```
- t₀：宇宙年龄
- E_i(E, z_i)：注入红移 z_i 处的注入能量，满足 dE/dt = b(E)
- 均匀 Φ(E) 时简化为 (公式 12)：
```
j(E) ≃ (1/(4π)) · l_E(E) · Φ(E)
```
（前提是 l_E(E) ≪ 视界尺寸，可忽略红移演化）

## 4.3 §4.1 Nucleons, Nuclei, and the GZK Cutoff

### 4.3.1 GZK 阈值 [FACT]

Greisen (1966) 与 Zatsepin–Kuzmin (1966) 独立指出：质子在高能下，其静止系中 CMB 光子能量可超过 **photo-pion 产生**阈值：

```
E_lab,thr^γ ≡ m_π + m_π²/(2m_N) ≃ 160 MeV
```

对应质子阈值（对背景光子 ε，公式 13）：
```
E_th = m_π(m_N + m_π/2)/ε ≃ 6.8 × 10¹⁶ · (ε / eV)⁻¹  eV
```
- CMB 典型 ε ~ 10⁻³ eV → **GZK cutoff** 出现在"数十 EeV"处（即 ~5×10¹⁹ eV），此时质子相互作用长度降至 **~6 Mpc**。

### 4.3.2 截面特征 [FACT, Fig. 8]

- 阈值附近：显著的 Δ(1232) **单 π 共振**。
- 高能极限：σ 随 s 对数增长。
- 第一个共振之后：由**多重 π 产生** N γ_b → N(nπ), n > 1 主导。

### 4.3.3 其他损失机制

**质子-对产生 (PPP, p γ_b → p e⁺ e⁻)** [FACT, 公式 14]
```
E_th = m_e(m_N + m_e)/ε ≃ 4.8 × 10¹⁴ · (ε / eV)⁻¹  eV
```
- CMB 中 PPP 发生于 E ~ 5×10¹⁷ eV。
- 首个天体物理讨论：Blumenthal [158]。
- 核电荷 Z 的情形：PPP 截面 ~ Z² × triplet pair production 截面。

**红移**：PPP 阈值附近的下一个主要损失机制。

**中子 β-衰变 (n → p e⁻ ν̄_e)** [FACT, 公式 15]
```
R_n = τ_n · E/m_N ≃ 0.9 · (E / 10²⁰ eV)  Mpc
```
- τ_n = 888.6 ± 3.5 s
- 对 E ≲ 10²⁰ eV 的中子主导损失。

**核的光致分裂（Giant Dipole Resonance）** [FACT]
- 对 E ≳ 10¹⁹ eV 的核是主导损失。
- 早期估算：衰减长度 ~几 Mpc。
- **Mrk 421, Mrk 501** 多 TeV γ 观测 [163,164] → IRB 比先前假设低约 **10 倍** → 核衰减长度增加。
- 最新 MC 模拟 [167–169]：降低 IRB 后，CMB 成为主导 → **E ~ 2×10²⁰ eV 处衰减长度 ~10 Mpc**。
- 这意味着：**若最高能事件为重核，加速器距离不能超过几十 Mpc**。

### 4.3.4 GZK 的物理论证 [FACT, 作者强调]

> "Even for conventional local sources, the maximal energy to which charged primaries can be accelerated is expected to be limited ... and it is generally hard to achieve energies beyond the cutoff energy."
>
> "a cutoff is expected at least for extragalactic nucleon primaries irrespective of the production mechanism."

**这是 §2.2 中"最高能过量事件"为什么是 UHECR 物理最核心谜题的关键**：若 GZK 是"无加速机制无关"的必然结果，而观测到 >10²⁰ eV 事件超出 GZK 预期 → 必须用新物理（新粒子、新传播机制或 top-down 场景）解释。

## 4.4 §4.2 UHE Photons & Electromagnetic Cascades

### 4.4.1 主导过程 [FACT]

- **Pair Production (PP)**：γ γ_b → e⁺ e⁻
- **Inverse Compton Scattering (ICS)**：e e⁺ + γ_b → 更高能 γ

阈值（公式 16）：
```
E_th = m_e²/ε ≃ 2.6 × 10¹¹ · (ε / eV)⁻¹  eV
```

高能极限截面（公式 17）：
```
σ_PP ≃ 2 σ_ICS ≃ (3/2) σ_T · (m_e²/s) · ln(s/(2m_e²))   (s ≫ m_e²)
```

### 4.4.2 级联发展 [FACT]

Klein-Nishina 极限下：PP 产生的 e⁺/e⁻ 携带大部分原始 γ 能量 → ICS 非弹性度 ~1 → upscattered γ 又成 leading → **反复 PP–ICS 循环** → EM cascade。

- **能量衰减长度 > 相互作用长度**（有效穿透更深，见 Fig. 11, 12）。
- **级联堆积谱**：级联发展加速 → γ 落入 PP 阈值以下 → **E⁻¹·⁵ 特征谱** [35, 182–184]。
- 完全发展级联的能量在 **~100 GeV 以下堆积** → 受 EGRET diffuse γ-ray 数据约束。

### 4.4.3 通用射电背景 (URB) [FACT]

- 关键背景：ε ≲ 10⁻⁶ eV（~100 MHz），即**射电背景**。
- URB 的河外成分不确定（银河 vs 河外难以分开）。
- 1 MHz 以下 URB 因 free-free 吸收指数截断，截断位置 **0.1–2 MHz 不确定**。
- Fig. 10 比较了理论 [175] vs 早期理论 [174] vs 观测 [173]。

### 4.4.4 EGMF 对级联的影响 [FACT]

- 河外磁场抑制级联发展（通过 e⁺e⁻ 同步冷却）。
- 若同步冷却时标 < ICS 时标 → 级联停止 → UHE γ 通量由"直接"γ（起源 < 吸收长度）主导。
- 强 EGMF 效应：**高能端通量降低、~几十–几百 GeV 通量升高**。

### 4.4.5 高 QED 过程 [FACT]

**双对产生 (DPP, γ γ_b → e⁺e⁻e⁺e⁻)** — 公式 18：
```
σ_DPP ≃ 172α⁴/(36πm_e²) ≃ 6.45 μbarn   (s ≫ m_e²)
```
- DPP 主导 PP 的能区：**E > 10²¹–10²³ eV**（强 URB 时取较高值）。

**三对产生 (TPP, e γ_b → e e⁺e⁻)** — 公式 19, 20：
```
σ_TPP ≃ (3α/(8π)) σ_T · (28/9 ln(s/m_e²) − 218/27)
η ≃ 1.768 · (s/m_e²)^(−3/4)   (s ≫ m_e²)
```
- 尽管 σ_TPP ~ σ_ICS 在 E ~ 10¹⁷ eV 就已可比，但因 η ≲ 10⁻³，能量衰减直到 **~10²² eV** 才重要。
- 主要影响：产生大量次级电子，把它们带到 UHE 以下。
- 若 B_rms > ~10⁻¹² G → 同步冷却主导 TPP → 可忽略。

### 4.4.6 其他可忽略过程 [FACT]

- μ⁺μ⁻, τ⁺τ⁻, π⁺π⁻ 对产生（~比 e⁺e⁻ 小 10×）
- 双 Compton 散射（α³ 阶，UHE 下 <10%）
- γ γ_b → γ γ（z > ~100 时才重要）
- Bethe-Heitler 对产生
- γ B → e⁺e⁻（银河系强度 ~10⁻⁶ G 需 E > ~10²⁴ eV；EGMF 下更高）

## 4.5 关键数值速查

| 量 | 值 |
|---|---|
| Photo-pion 阈值 (E_lab) | 160 MeV |
| GZK 质子阈值 | ~6.8×10¹⁹ eV |
| GZK 质子相互作用长度 | ~6 Mpc |
| PPP 质子阈值 | ~5×10¹⁷ eV |
| 中子衰变范围 | 0.9 Mpc (E=10²⁰ eV) |
| 核光致分裂长度 (2×10²⁰ eV) | ~10 Mpc (低 IRB) |
| UHE γ PP 阈值 | 2.6×10¹¹ (ε/eV)⁻¹ eV |
| DPP 主导能区 | 10²¹–10²³ eV |
| TPP 主导 EGMF 下限 | B_rms > 10⁻¹² G |
| 完全发展级联堆积能量 | ~100 GeV |

## 4.6 [CRITIQUE] 与 1999 年后发展的对照

- [FACT] 2017 年 Pierre Auger 合作组首次确认 E > 5×10¹⁹ eV 处**能谱陡化**（与 GZK 预期一致）[Nature 551, 56–62 (2017)]。
- [CRITIQUE] 1999 年的"最高能过量"谜题在 Auger 时代得到部分澄清：Fly's Eye 与 AGASA 数据在 ~10²⁰ eV 附近有统计量差异；Auger 数据支持"明显 GZK 截断"，但 UHE 端仍有少量极端事件。
- [FACT] 目前仍存在的谜题：若 GZK 成立，>10²⁰ eV 事件需极近源（<~100 Mpc），而 100 Mpc 内缺乏明确加速器源——这正是 Bhattacharjee & Sigl 提出 top-down 的动机。