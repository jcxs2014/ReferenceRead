> 本章属于：Bhattacharjee & Sigl (1999), Phys. Rep. 320, 1–150
>
> 上一章：`04_propagation_gzk.md`
>
> 下一章：`06_magnetic_fields_constraints.md`

---

# 5. UHE Neutrinos & Exotic Particles (§4.3, p. 22–28)

## 5.1 本节核心内容

- UHE 中微子主要与**宇宙 relic neutrino background (RNB)** 相互作用。
- **Z-burst** 情景：UHE 中微子与 relic 中微子在 Z⁰ 共振处湮灭，产生高能次级粒子，作为 EHECR 候选源。
- UHE 中微子**探测**：通过 μ 子（CC 相互作用），ν_τ 可"再生"穿透地球。
- **新物理增强中微子截面**的可能：extra dimensions, generation symmetry。
- **SUSY 候选粒子**：轻 quasi-stable gluino → S⁰ R-hadron（质量 0.1–1 GeV），有效 GZK 阈值提高 → 可作为 EHECR 候选。
- **QCD 奇特粒子**：uuddss H-dibaryon (M_H ≃ 1700 MeV) 也可作为 EHECR 候选。

## 5.2 §4.3.1 UHE 中微子传播

### 5.2.1 与 RNB 的相互作用 [FACT]

中微子-UHE 中微子 (E) 与 relic 中微子 (ε) 的平均 CM 能量平方：
```
⟨s⟩ ≃ (45 GeV)² · (ε/10⁻³ eV) · (E/10¹⁵ GeV)   (公式 21)
```
- relativistic relic ν: ε ≃ 3T_ν(1+η_b/4)，T_ν ≃ 1.9(1+z) K = 1.6×10⁻⁴(1+z) eV
- nonrelativistic relic ν (m_ν ≲ 20 eV): ε ≃ max[3T_ν, m_ν]

**主导相互作用**：
- t-channel W±: ν_i + ν̄_j → l_i + l̄_j
- s-channel Z⁰: ν_i + ν̄_i → f f̄
- t-channel Z⁰: ν_i + ν̄_j → ν_i + ν̄_j

**s-channel Z⁰ 微分截面 (公式 22)**：
```
dσ/(dμ) = (G_F² s / 4π) · M_Z² / [(s−M_Z²)² + M_Z²Γ_Z²] · [g_L²(1+μ*)² + g_R²(1−μ*)²]
```
- μ*：CM 散射角余弦
- g_L, g_R：左右耦合常数

**t-channel 截面 (公式 23)**：
```
σ_t(E,ε) ~ min[10⁻³⁴, 3×10⁻³⁹ · (ε/10⁻³ eV) · (E/10²⁰ eV)]  cm²
```

### 5.2.2 中微子-核子截面 [FACT, 公式 24]

```
σ_νN(E) ~ 10⁻³¹ (E/10²⁰ eV)^0.4  cm²    for E ≳ 10¹⁵ eV
```
- 尽管 σ_νN > σ_νν (RNB)，但 RNB 粒子数密度比重子密度高 **~10¹⁰** → RNB 相互作用仍占主导（除 GUT 尺度能量外）。

### 5.2.3 其他中微子相互作用

- **ν + γ → l W⁺** [197]：W± 产生阈值以上可与 νν 过程可比，但永远不主导。
- **γ + ν → γ + γ + ν** [198]：
```
σ ≃ 9×10⁻⁵⁶ (s/MeV²)⁵  cm²    valid up to s ≲ 10 MeV²
```
- 若 s⁵ 行为持续到 s ~几百 MeV²，则此过程在 E ~ 3×10¹⁷ (ε/10⁻³ eV) eV 开始主导 [199]。

### 5.2.4 Z-burst 情景 [FACT]

**核心机制**：若 relic 中微子质量 ~1 eV（热暗物质，可能聚集在星系团/银晕）：
- E = M_Z²/(2m_ν) = **4×10²¹ (eV/m_ν) eV** 处，Z⁰ 共振湮灭概率增大。
- Z⁰ 衰变产物：主要核子 (~E_ν/5) 和 γ (~E_ν/40)。
- 若 UHE ν 是加速质子的次级产物 → 需要**加速到 ≥ 几 10²² eV** → 更可能来自 non-acceleration (top-down) 场景。

**关键约束**：
- Z⁰ 湮灭主要由**非聚集的** RNB 主导（而非银晕内聚集的），除非新 ν 源 [204]。
- EGRET diffuse γ-ray (~10 GeV) 约束：
  - 若 X 粒子只衰变到 ν：f_ν ≳ 20 (l_ν/5 Mpc)⁻¹
  - 若 L_γ ~ L_ν（多数模型）：f_ν ≳ 10³ (l_ν/5 Mpc)⁻¹
  - 若大部分 EM 能量在 TeV 段释放 → 可放宽
- Z-burst 要求源对加速质子**光学厚**（否则 GZK 以下质子流将与 ν 流可比 [204]）。

**Z-burst 参数**（Super-K 结果 [212]）[FACT]：
- m_ν ≃ 0.07 eV, Ω_ν ≃ 0.01，源 z ~ 几 → 需 ν 源产生 E ≥ 10²² eV。

### 5.2.5 中微子振荡 [FACT]

Super-K 结果：μ-τ 近最大混合，|Δm²| ≃ 5×10⁻³ eV² [212]：
```
L_osc = 2E/|Δm²| = 2.6×10⁻⁶ (E/PeV) (|Δm²|/5×10⁻³ eV²)⁻¹ pc
```
- 银河系 halo 中的 RNB 势引起的共振转换可能影响 UHE ν 味组成 [224]。
- 长基线对 ν 衰变敏感 [225]。

## 5.3 §4.3.1 Neutrino Detection

### 5.3.1 基本方法 [FACT]

通过 CC 反应产生的 μ 子探测。折叠 quark-ν 基本截面与核子内 parton 分布函数 (PDF)。对 x ≃ M_W²/(2m_N E) 的 parton 最敏感。

**中微子-核子 CC 截面 (公式 25)**：
```
σ_νN(E) ≃ 2.36×10⁻³² (E/10¹⁹ eV)^0.363  cm²    (10¹⁶ eV ≲ E ≲ 10²¹ eV)
```
- CTEQ4-DIS 参数化 [227]。
- 非主导 1/x 对数贡献 [231]：与 [227,230] 差异 <1.5 倍（至 10²¹ eV）。
- NC 截面比 CC 小 2–3 倍。
- Glashow 共振：ν̄_e e → W⁻，E = 6.3×10¹⁵ eV。

### 5.3.2 地球衰减 [FACT]

- >~100 TeV 中微子在地球内开始被吸收（σ 随 E 增长）。
- **τ 中微子再生**：τ 中微子能量到 ~100 PeV 仍可穿透地球，因为 τ 衰变再产生 τ 中微子。
- PeV 能量处**"double-bang"事件** [222]：
  - 第 1 个 bang：CC 产生 τ
  - 第 2 个 bang：τ 在 ~100 m 外衰变
- 各向同性 10 TeV–10 PeV ν 流可作为地球密度分布的探针（中微子吸收层析 [234]）。

## 5.4 新物理增强的中微子截面

### 5.4.1 新相互作用 [FACT]

**Generation Symmetry 情景** [235–236]：
- 引入破缺 SU(3) 规范对称（与 QCD 颜色 SU(3) 对偶）。
- 三族轻子/夸克代表 generation 对称量子数。
- 中微子与夸克有效强相互作用 → 有效截面 ~几何核子截面。
- 约束：FCNC 实验 → 新相互作用尺度 >~100 TeV。

**大额外维度 (ADD) 情景** [237–242]：
- n 个额外紧致维度，量子引力尺度 M_{4+n} ~ TeV。
- Bulk graviton (KK 模式) 交换增强两粒子截面：
```
σ_g ≃ 4πs/M_{4+n}⁴ ≃ 10⁻²⁷ (M_{4+n}/TeV)⁻⁴ (E/10²⁰ eV)  cm²   (公式 26)
```
- 中微子 σ_νN > 10⁻²⁷ cm² 开始在大气中作用 → 中微子成为 EHECR 事件候选！
- 具体信号：
  - IceCube/水冰中微子望远镜：E > E_c 处无事件。
  - Pierre Auger：E > E_c 处谱硬化。

**超新星约束** [240]：
```
M_6 >~50 TeV, M_7 >~4 TeV, M_8 >~1 TeV  (n=2,3,4)
```
- → 若中微子作 EHECR 候选，需 **n ≥ 4**。

**额外维度半径 (公式 27)**：
```
r_n ≃ M_{4+n}⁻¹ (M_Pl/M_{4+n})^{2/n} ≃ 2×10⁻¹⁷ (TeV/M_{4+n}) (M_Pl/M_{4+n})^{2/n}  cm
```
- 对应上限：r_6 ≲ 3×10⁻⁴ mm, r_7 ≲ 4×10⁻⁷ mm, r_8 ≲ 2×10⁻⁸ mm。

## 5.5 §4.3.2 超对称粒子 (SUSY)

### 5.5.1 轻 quasi-stable gluino [FACT]

**机制**：若 gluino 质量 ~0.1–1 GeV [245]，最轻 gluino-baryon uds ̃g 记作 **S⁰**，可长寿命或稳定。

**有效 GZK 阈值提高** [246]：
- 阈能被抬高（m_{S⁰} 代替 m_N 代入公式 13）。
- 截面峰值位置抬高 (m_{S⁰}/m_N)·(m*−m_{S⁰})/(m_Δ−m_N) 倍（质量间距比 >~2）。
- 有效 GZK 阈值**提高几个量级** → **源可远 15–30 倍** 于核子情形。

**观测关联** [FACT, Farrar & Biermann [247]]：
- 5 个最高能量 CR 事件到达方向与 z = 0.3–2.2 致密类星体可能相关。
- 但统计分析受 Hoffman [248] 批评，Farrar & Biermann [249] 回应。

### 5.5.2 加速器约束 [FACT]

- [245] 的轻 gluino 情景已被加速器约束否定 [250,251]。
- "可调节"gluino 质量情景 [243] 仍可能：
  - 候选：R⁰ (glueballino g̃g)，ρ̃（isotriplet ̃g−(uū−dd̄)₈）
- EAS 组成约束 [254]：**初级粒子静止质量 <~50 GeV**；Auger 数据可降至 ~10 GeV。
- S⁰ 需作为加速质子与物质作用的次级产物 → 质子需加速到 ≥ 10²¹ eV。
- 次级过程也产生 ν 和 γ → 可通过 EGRET/GLAST/HEGRA/WHIPPLE/VERITAS 约束。
- 质子→R-hadron 分支比 >~0.01（粗略估计）。

## 5.6 §4.3.3 其他奇特粒子

### 5.6.1 uuddss H-dibaryon [FACT]

- QCD instanton 诱导 uds-uds 束缚态，M_H ≃ 1700 MeV [255]。
- 性质类似 S⁰：中性、自旋 0。
- **有效 GZK 截断 ~7.3×10²⁰ eV**（比核子高）。
- 可作为高红移源的 EHECR 事件候选。

## 5.7 关键数值速查

| 量 | 值 |
|---|---|
| ⟨s⟩ for UHE ν on RNB | (45 GeV)² (ε/10⁻³ eV)(E/10¹⁵ GeV) |
| σ_t(E,ε) (t-channel) | min[10⁻³⁴, 3×10⁻³⁹(ε/10⁻³ eV)(E/10²⁰ eV)] cm² |
| σ_νN (CC, 公式 25) | 2.36×10⁻³² (E/10¹⁹ eV)^0.363 cm² |
| Z-burst 阈值 | 4×10²¹ (eV/m_ν) eV |
| Super-K |Δm²| | 5×10⁻³ eV² |
| ADD σ_g (公式 26) | 10⁻²⁷ (M/TeV)⁻⁴ (E/10²⁰ eV) cm² |
| ADD 约束 | n ≥ 4, M_{4+n} > 1 TeV |
| S⁰ gluino 质量 | 0.1–1 GeV |
| S⁰ GZK 阈值提升 | 提高几倍，源距离 15–30× |
| EHECR 粒子静止质量上限 | <~50 GeV（Auger 可降到 10 GeV）|
| H-dibaryon 质量 | 1700 MeV |
| H-dibaryon GZK 阈值 | 7.3×10²⁰ eV |

## 5.8 [CRITIQUE] 历史评价

- [FACT] **Z-burst 情景**在 IceCube 观测限制下（未发现对应 UHE 中微子）已基本被否定。
- [FACT] 加速器（LHC）未发现大额外维度（ADD），M_{4+n} >~ 5–10 TeV 对 n=2。
- [CRITIQUE] 整个 §4.3 的"奇特 EHECR 粒子"假设在 1999 年是开放问题，但 2020 年后由于 Auger 显示**最高能事件到达方向与近邻星系的关联**（如 Centaurus A 在 2017–2018 年数据中显著），支持了"重核（如 Fe）来自近邻源"的 Bottom-up 解释，使 exotic primary 假设更弱。
