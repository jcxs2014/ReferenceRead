> 本章属于：Bhattacharjee & Sigl (1999), Phys. Rep. 320, 1–150
>
> 上一章：`06_magnetic_fields_constraints.md`
>
> 下一章：`08_acceleration_sources.md`

---

# 7. Transport Equations & Quantum Gravity Effects (§4.7–4.8, p. 31–40)

## 7.1 §4.7 Detailed Propagation Calculations

### 7.1.1 一维 Boltzmann 方程 (公式 35) [FACT]

对一组粒子种类 i，局域能量密度 n_i(E) 的演化：
```
∂_t n_i(E) =
  − n_i(E) ∫dε n_b(ε) ∫₋₁⁺¹ dμ (1−β_b β_i)/2 · Σ_j σ_{i→j}[s=εE(1−β_b β_i)]

  + ∫dE' ∫dε n_b(ε) ∫₋₁⁺¹ dμ Σ_j (1−β_b β'_j)/2 · n_j(E') · dσ_{j→i}/dE[s=εE'(1−β_b β_j), E]

  + Φ_i
```
- 第一项：species i 通过相互作用**损失**；第二项：其他 species j 通过相互作用**产生** i；第三项：注入。

### 7.1.2 求解方法 [FACT]

| 粒子 | 求解方法 | 参考 |
|---|---|---|
| 核子/核 | CEL 近似 [288,289] 或精确 Boltzmann 方程 [290,156,291]；Monte Carlo [292,26,293,294]；核光致分裂 MC [25,167,169] | |
| EM cascade | Hybrid MC + matrix doubling [296] 或隐式数值 [156,205,206]；能量覆盖 100 MeV – 10¹⁶ GeV (GUT scale) | [259,295] |
| 中微子 | 完整 Boltzmann 方程 [195]；规范流量 [196]；半解析 [298] | |
| 全耦合 | [205,206] 集成代码：nucleons + γ + e + ν 联立 | |

### 7.1.3 CEL 近似的局限 [FACT]

- 对 PPP（小非弹性度）：**优秀**。
- 对 π 产生（大非弹性度，随机性）：CEL 在 GZK 截断**正下方**产生更尖锐的堆积谱（"pile-up"）vs 精确解 [290]。
- CEL 对连续源分布或远距离 discrete 源**仍可工作**（多次 π 产生事件平均下）。

## 7.2 §4.7.2 Angle-Time-Energy Images

### 7.2.1 强偏转 (Diffusion 近似) [FACT]

大尺度磁场（10⁻⁸ – 10⁻⁶ G，如星系团内）→ 扩散近似适用。

**能量损失-扩散方程 (公式 36)**：
```
∂_t n(r,E) = −∂_E[b(E) n(r,E)] + ∇·[D(r,E) ∇n(r,E)] + Φ(E)
```

- 若 D(r,E) 不依赖 r → **Syrovatskii 解析解** [300]。
- 应用于 EGMF ~几×10⁻⁸ G，E 至 ~10²⁰ eV。
- 但**在 UHECR 实际应用中，扩散近似与 rectilinear 之间的过渡区**是典型情况，此方程适用性有限。

**各向异性 (公式 37)**：
```
δ(E) = (3 D(r,E) / n(r,E)) |∇n(r,E)|
```

### 7.2.2 小偏转 (Monte Carlo, 3D) [FACT]

磁场建模：Gaussian 随机场，零均值，功率谱 B²(k) ∝ kⁿᴴ for k < k_c，其中 k_c = 2π/l_c。

**Monte Carlo 流程**：
1. 傅里叶变换生成磁场网格实现。
2. 注入粒子 E 对数均匀分布 → 在磁场中求解运动方程（含 π 产生 + PPP）。
3. 记录到达能量、时间、方向。
4. 典型 40000 粒子 → 生成 time-energy histogram。
5. 通过 Poisson 抽样模拟观测事件。

### 7.2.3 关键参数与 likelihood 分析

**参数** [FACT]：
- τ₁₀₀：E = 100 EeV 处磁偏转延迟（公式 32）。
- T_S：源发射时间尺度（T_S ≪ 1 yr = burst；T_S ≫ 1 yr = 连续源）。
- γ：注入谱微分指数。
- N₀：源到探测器的总 fluence。

**EGMF 约束 (公式 38)** [FACT, 来自 AGASA 200 EeV 事件对分析]：
```
B ≲ 2×10⁻¹¹ · (l_c/1 Mpc)⁻^(1/2) · (d/30 Mpc)⁻¹  G
```
- 若证实，比 Faraday rotation 强两个量级。

**五种 generic time-energy 图像情形**（根据 τ_E vs T_S vs 实验寿命）：
- **τ_E ≪ T_S**：距离由 pion 产生特征（GZK cutoff 以上）确定，误差 ~2×。
- **T_S ≪ τ_E < 实验寿命**：磁场强度可从 time-energy 图像得到。
- **T_S ≫ τ_E ≫ 实验寿命**：只能给磁场下限（与 Faraday 结合可得数量级估计）。
- **T_S ~ τ_E**：最佳参数估计情况。

### 7.2.4 发射时间尺度可探测范围 (公式 39) [FACT]

```
3×10³ (Δθ/1°)² (d/10 Mpc) yr ≲ T_S ≃ τ_E ≲ 10⁴ – 10⁷ (E/100 EeV)⁻² yr
```

### 7.2.5 一般情形：扩散 vs rectilinear 的过渡区 [FACT]

Monte Carlo 推广到任意偏转 [311]：
- Supergalactic Plane 建模为厚度几 Mpc、密度高斯剖面的 sheet。
- Kolmogorov 谱 n_H = −11/3（Kraichnan 谱 n_H = −7/2 也考虑）。

**扩散系数 (公式 40)**：
```
D(E) ≃ (1/3) r_g(E) B · ∫_{1/r_g}^∞ dk k² ⟨B²(k)⟩
```
- Kolmogorov 谱下：
  - 扩散区 (τ_E >~ d)：D(E) ∝ E^(1/3)（r_g < L/2π）→ τ_E ∝ E^(−1/3)
  - Bohm 扩散 (r_g > L/2π)：D(E) ∝ E → τ_E ∝ E⁻¹
  - Rectilinear：τ_E ∝ E⁻²

**关键观测** [FACT, Fig. 19, 20]：
- Fig. 19 显示 bursting source 上 τ-E 关系的三个 regime。
- Fig. 20：最优场强（源 d=10 Mpc, B_max = 10⁻⁷ G）对 E > 10 EeV 数据的最佳拟合。
- 有效回旋半径 ~解析估计的 10×。
- 不同磁场实现间谱涨落显著。

### 7.2.6 现代 AGASA 数据启示 [FACT]

- 最新 AGASA 数据显示 EHECR **各向同性** [83]。
- 单一源 + 强场解释 → GZK 以上通量被过度抑制 → **需要连续源分布** [314]。
- 弥漫源分布 + Supergalactic Plane 关联 + **B >~ 0.05 μG** → 可解释大尺度各向同性 + 小尺度聚团 [316]。
- Fig. 24：B_max = 0.05 和 0.5 μG 均能很好地拟合数据。

## 7.3 §4.8 Anomalous Kinematics & Quantum Gravity

### 7.3.1 Lorentz Invariance Violation (VLI) 约束 [FACT]

- 若 10²⁰ eV 事件是质子 → (c_p − c) < 10⁻²³（否则质子会在 ~几百 cm 内通过 Cherenkov 辐射损失能量）。
- VLI 可避免 GZK 截断（微小偏离下，阈值升高）。
- **VPE (Violation of Equivalence Principle) 等效** → 质子与光子的引力耦合差异 < 10⁻¹⁹（比 Eötvös 实验精确 5 个量级）。

### 7.3.2 量子引力色散关系 (公式 41) [FACT]

```
c²k² ≃ E² + χ E³/E₀
```
- 对应光子群速度 ∂E/∂k = c[1 − χ E/E₀ + O(E²/E₀²)]
- χ = ±1；E₀ = 量子引力尺度
- 阈值 (公式 42)：
```
ε ≃ E/4 · [m_e²/(E₁E₂ + θ₁θ₂)] + χ E²/(4E₀)
```

**两种情形**：
- **χ < 0 (c_γ > c_p)**：E > E_c 时光子可自发衰变 → 河外光子传播受阻 → 观测 > 20 TeV 河外光子 [328,329] 约束 **E₀ >~ M_Pl** 或 (c²_i − c²) > ~ −2×10⁻¹⁷。
- **χ > 0**：E > E_c 时 ε 增长 → 光子传播不受阻 → 可观测 > 100 TeV 来自 > 100 Mpc 的河外光子。

**时间色散 (公式)**：
```
Δt ≃ (d/c)(E/E₀) ≃ 1 (d/100 Mpc)(E/TeV)(E₀/M_Pl)⁻¹ s
```
- Mrk 421 > 2 TeV γ 在 300 s 内到达 → E₀ > 4×10¹⁶ GeV [331]。
- HEGRA 若观测到 > 200 TeV GRB γ 在 200 s 内 → E₀ ≃ M_Pl。

### 7.3.3 快子中微子 [FACT]

- Kostelecký [333]：ν_e 为 tachyon。
- 核内质子可衰变 p → n + e⁺ + ν_e，阈值 Eth = m(A,Z)[m(A,Z±1)+m_e−m(A,Z)]/|m_νe|
- 自由质子：Eth ≃ 1.7×10¹⁵/(|m_νe|/eV) eV。
- Ehrlich [334] 主张 m²_νe ≃ −(0.5 eV)² 可同时解释 knee 与高能端。
- [CRITIQUE] 与氚 β 衰变实验最佳拟合值 m²_νe < 0 一致（但最可能是实验未解决的系统问题），不过 |m²_νe| 值通常比 fit knee 所需大。
- 预测 knee 附近有 neutron 谱线 [336]。

## 7.4 关键数值速查

| 量 | 值 |
|---|---|
| τ_E 三个 regime | E⁻² (rectilinear), E⁻¹ (Bohm), E⁻¹/³ (Kolmogorov 扩散) |
| AGASA 约束 (公式 38) | B ≲ 2×10⁻¹¹ G (l_c/Mpc)^(-1/2) (d/30 Mpc)^-1 |
| VLI 约束 (10²⁰ eV 质子) | (c_p−c) < 10⁻²³ |
| VPE 约束 | (g_p/g_γ)−1 < 10⁻¹⁹ |
| 量子引力色散 E₀ 下限 (Mrk 421) | E₀ > 4×10¹⁶ GeV |
| M_Pl | 2.4×10¹⁸ GeV |
