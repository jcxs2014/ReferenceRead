> 本章属于：Bhattacharjee & Sigl (1999), Phys. Rep. 320, 1–150
>
> 上一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/04_propagation_gzk.md|04_propagation_gzk.md]]
>
> 下一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/06_magnetic_fields_constraints.md|06_magnetic_fields_constraints.md]]

---

# 5. UHE Neutrinos & Exotic Particles (§4.3, p. 22–28)

## 5.1 本节核心内容

- UHE 中微子主要与**宇宙 relic neutrino background (RNB)** 相互作用。
- **Z-burst** 情景：UHE 中微子与 relic 中微子在 Z⁰ 共振处湮灭，产生高能次级粒子，作为 EHECR 候选源。
- UHE 中微子**探测**：通过 $\mu$ 子（CC 相互作用），$\nu$_$\tau$ 可"再生"穿透地球。
- **新物理增强中微子截面**的可能：extra dimensions, generation symmetry。
- **SUSY 候选粒子**：轻 quasi-stable gluino → S⁰ R-hadron（质量 0.1–1 GeV），有效 GZK 阈值提高 → 可作为 EHECR 候选。
- **QCD 奇特粒子**：uuddss H-dibaryon (M_H ≃ 1700 MeV) 也可作为 EHECR 候选。

## 5.2 §4.3.1 UHE 中微子传播

### 5.2.1 与 RNB 的相互作用 [FACT]

中微子-UHE 中微子 (E) 与 relic 中微子 ($\epsilon$) 的平均 CM 能量平方：
```
⟨s⟩ ≃ (45 GeV)² · ($\epsilon$/$10^{-3}$ eV) · (E/$10^{15}$ GeV)   (公式 21)
```
- relativistic relic $\nu$: $\epsilon$ ≃ 3T_$\nu$(1+$\eta$_b/4)，T_$\nu$ ≃ 1.9(1+z) K = 1.6×$10^{-4}$(1+z) eV
- nonrelativistic relic $\nu$ (m_$\nu$ ≲ 20 eV): $\epsilon$ ≃ max[3T_$\nu$, m_$\nu$]

**主导相互作用**：
- t-channel W±: $\nu$_i + $\nu$̄_j → l_i + l̄_j
- s-channel Z⁰: $\nu$_i + $\nu$̄_i → f f̄
- t-channel Z⁰: $\nu$_i + $\nu$̄_j → $\nu$_i + $\nu$̄_j

**s-channel Z⁰ 微分截面 (公式 22)**：
```
d$\sigma$/(d$\mu$) = (G_F² s / 4$\pi$) · M_Z² / [(s−M_Z²)² + M_Z²$\Gamma$_Z²] · [g_L²(1+$\mu$*)² + g_R²(1−$\mu$*)²]
```
- $\mu$*：CM 散射角余弦
- g_L, g_R：左右耦合常数

**t-channel 截面 (公式 23)**：
```
$\sigma$_t(E,$\epsilon$) ~ min[$10^{-34}$, 3×$10^{-39}$ · ($\epsilon$/$10^{-3}$ eV) · (E/$10^{20}$ eV)]  cm²
```

### 5.2.2 中微子-核子截面 [FACT, 公式 24]

```
$\sigma$_$\nu$N(E) ~ $10^{-31}$ (E/$10^{20}$ eV)^0.4  cm²    for E ≳ $10^{15}$ eV
```
- 尽管 $\sigma$_$\nu$N > $\sigma$_$\nu$$\nu$ (RNB)，但 RNB 粒子数密度比重子密度高 **~$10^{10}$** → RNB 相互作用仍占主导（除 GUT 尺度能量外）。

### 5.2.3 其他中微子相互作用

- **$\nu$ + $\gamma$ → l W⁺** [197]：W± 产生阈值以上可与 $\nu$$\nu$ 过程可比，但永远不主导。
- **$\gamma$ + $\nu$ → $\gamma$ + $\gamma$ + $\nu$** [198]：
```
$\sigma$ ≃ 9×$10^{-56}$ (s/MeV²)⁵  cm²    valid up to s ≲ 10 MeV²
```
- 若 s⁵ 行为持续到 s ~几百 MeV²，则此过程在 E ~ 3×$10^{17}$ ($\epsilon$/$10^{-3}$ eV) eV 开始主导 [199]。

### 5.2.4 Z-burst 情景 [FACT]

**核心机制**：若 relic 中微子质量 ~1 eV（热暗物质，可能聚集在星系团/银晕）：
- E = M_Z²/(2m_$\nu$) = **4×$10^{21}$ (eV/m_$\nu$) eV** 处，Z⁰ 共振湮灭概率增大。
- Z⁰ 衰变产物：主要核子 (~E_$\nu$/5) 和 $\gamma$ (~E_$\nu$/40)。
- 若 UHE $\nu$ 是加速质子的次级产物 → 需要**加速到 ≥ 几 $10^{22}$ eV** → 更可能来自 non-acceleration (top-down) 场景。

**关键约束**：
- Z⁰ 湮灭主要由**非聚集的** RNB 主导（而非银晕内聚集的），除非新 $\nu$ 源 [204]。
- EGRET diffuse $\gamma$-ray (~10 GeV) 约束：
  - 若 X 粒子只衰变到 $\nu$：f_$\nu$ ≳ 20 (l_$\nu$/5 Mpc)⁻¹
  - 若 L_$\gamma$ ~ L_$\nu$（多数模型）：f_$\nu$ ≳ $10^{3}$ (l_$\nu$/5 Mpc)⁻¹
  - 若大部分 EM 能量在 TeV 段释放 → 可放宽
- Z-burst 要求源对加速质子**光学厚**（否则 GZK 以下质子流将与 $\nu$ 流可比 [204]）。

**Z-burst 参数**（Super-K 结果 [212]）[FACT]：
- m_$\nu$ ≃ 0.07 eV, $\Omega$_$\nu$ ≃ 0.01，源 z ~ 几 → 需 $\nu$ 源产生 E ≥ $10^{22}$ eV。

### 5.2.5 中微子振荡 [FACT]

Super-K 结果：$\mu$-$\tau$ 近最大混合，|$\Delta$m²| ≃ 5×$10^{-3}$ eV² [212]：
```
L_osc = 2E/|$\Delta$m²| = 2.6×$10^{-6}$ (E/PeV) (|$\Delta$m²|/5×$10^{-3}$ eV²)⁻¹ pc
```
- 银河系 halo 中的 RNB 势引起的共振转换可能影响 UHE $\nu$ 味组成 [224]。
- 长基线对 $\nu$ 衰变敏感 [225]。

## 5.3 §4.3.1 Neutrino Detection

### 5.3.1 基本方法 [FACT]

通过 CC 反应产生的 $\mu$ 子探测。折叠 quark-$\nu$ 基本截面与核子内 parton 分布函数 (PDF)。对 x ≃ M_W²/(2m_N E) 的 parton 最敏感。

**中微子-核子 CC 截面 (公式 25)**：
```
$\sigma$_$\nu$N(E) ≃ 2.36×$10^{-32}$ (E/$10^{19}$ eV)^0.363  cm²    ($10^{16}$ eV ≲ E ≲ $10^{21}$ eV)
```
- CTEQ4-DIS 参数化 [227]。
- 非主导 1/x 对数贡献 [231]：与 [227,230] 差异 <1.5 倍（至 $10^{21}$ eV）。
- NC 截面比 CC 小 2–3 倍。
- Glashow 共振：$\nu$̄_e e → W⁻，E = 6.3×$10^{15}$ eV。

### 5.3.2 地球衰减 [FACT]

- >~100 TeV 中微子在地球内开始被吸收（$\sigma$ 随 E 增长）。
- **$\tau$ 中微子再生**：$\tau$ 中微子能量到 ~100 PeV 仍可穿透地球，因为 $\tau$ 衰变再产生 $\tau$ 中微子。
- PeV 能量处**"double-bang"事件** [222]：
  - 第 1 个 bang：CC 产生 $\tau$
  - 第 2 个 bang：$\tau$ 在 ~100 m 外衰变
- 各向同性 10 TeV–10 PeV $\nu$ 流可作为地球密度分布的探针（中微子吸收层析 [234]）。

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
$\sigma$_g ≃ 4$\pi$s/M_{4+n}⁴ ≃ $10^{-27}$ (M_{4+n}/TeV)⁻⁴ (E/$10^{20}$ eV)  cm²   (公式 26)
```
- 中微子 $\sigma$_$\nu$N > $10^{-27}$ cm² 开始在大气中作用 → 中微子成为 EHECR 事件候选！
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
r_n ≃ M_{4+n}⁻¹ (M_Pl/M_{4+n})^{2/n} ≃ 2×$10^{-17}$ (TeV/M_{4+n}) (M_Pl/M_{4+n})^{2/n}  cm
```
- 对应上限：r_6 ≲ 3×$10^{-4}$ mm, r_7 ≲ 4×$10^{-7}$ mm, r_8 ≲ 2×$10^{-8}$ mm。

## 5.5 §4.3.2 超对称粒子 (SUSY)

### 5.5.1 轻 quasi-stable gluino [FACT]

**机制**：若 gluino 质量 ~0.1–1 GeV [245]，最轻 gluino-baryon uds ̃g 记作 **S⁰**，可长寿命或稳定。

**有效 GZK 阈值提高** [246]：
- 阈能被抬高（m_{S⁰} 代替 m_N 代入公式 13）。
- 截面峰值位置抬高 (m_{S⁰}/m_N)·(m*−m_{S⁰})/(m_$\Delta$−m_N) 倍（质量间距比 >~2）。
- 有效 GZK 阈值**提高几个量级** → **源可远 15–30 倍** 于核子情形。

**观测关联** [FACT, Farrar & Biermann [247]]：
- 5 个最高能量 CR 事件到达方向与 z = 0.3–2.2 致密类星体可能相关。
- 但统计分析受 Hoffman [248] 批评，Farrar & Biermann [249] 回应。

### 5.5.2 加速器约束 [FACT]

- [245] 的轻 gluino 情景已被加速器约束否定 [250,251]。
- "可调节"gluino 质量情景 [243] 仍可能：
  - 候选：R⁰ (glueballino g̃g)，$\rho$̃（isotriplet ̃g−(uū−dd̄)₈）
- EAS 组成约束 [254]：**初级粒子静止质量 <~50 GeV**；Auger 数据可降至 ~10 GeV。
- S⁰ 需作为加速质子与物质作用的次级产物 → 质子需加速到 ≥ $10^{21}$ eV。
- 次级过程也产生 $\nu$ 和 $\gamma$ → 可通过 EGRET/GLAST/HEGRA/WHIPPLE/VERITAS 约束。
- 质子→R-hadron 分支比 >~0.01（粗略估计）。

## 5.6 §4.3.3 其他奇特粒子

### 5.6.1 uuddss H-dibaryon [FACT]

- QCD instanton 诱导 uds-uds 束缚态，M_H ≃ 1700 MeV [255]。
- 性质类似 S⁰：中性、自旋 0。
- **有效 GZK 截断 ~7.3×$10^{20}$ eV**（比核子高）。
- 可作为高红移源的 EHECR 事件候选。

## 5.7 关键数值速查

| 量 | 值 |
|---|---|
| ⟨s⟩ for UHE $\nu$ on RNB | (45 GeV)² ($\epsilon$/$10^{-3}$ eV)(E/$10^{15}$ GeV) |
| $\sigma$_t(E,$\epsilon$) (t-channel) | min[$10^{-34}$, 3×$10^{-39}$($\epsilon$/$10^{-3}$ eV)(E/$10^{20}$ eV)] cm² |
| $\sigma$_$\nu$N (CC, 公式 25) | 2.36×$10^{-32}$ (E/$10^{19}$ eV)^0.363 cm² |
| Z-burst 阈值 | 4×$10^{21}$ (eV/m_$\nu$) eV |
| Super-K |$\Delta$m²| | 5×$10^{-3}$ eV² |
| ADD $\sigma$_g (公式 26) | $10^{-27}$ (M/TeV)⁻⁴ (E/$10^{20}$ eV) cm² |
| ADD 约束 | n ≥ 4, M_{4+n} > 1 TeV |
| S⁰ gluino 质量 | 0.1–1 GeV |
| S⁰ GZK 阈值提升 | 提高几倍，源距离 15–30× |
| EHECR 粒子静止质量上限 | <~50 GeV（Auger 可降到 10 GeV）|
| H-dibaryon 质量 | 1700 MeV |
| H-dibaryon GZK 阈值 | 7.3×$10^{20}$ eV |

## 5.8 [CRITIQUE] 历史评价

- [FACT] **Z-burst 情景**在 IceCube 观测限制下（未发现对应 UHE 中微子）已基本被否定。
- [FACT] 加速器（LHC）未发现大额外维度（ADD），M_{4+n} >~ 5–10 TeV 对 n=2。
- [CRITIQUE] 整个 §4.3 的"奇特 EHECR 粒子"假设在 1999 年是开放问题，但 2020 年后由于 Auger 显示**最高能事件到达方向与近邻星系的关联**（如 Centaurus A 在 2017–2018 年数据中显著），支持了"重核（如 Fe）来自近邻源"的 Bottom-up 解释，使 exotic primary 假设更弱。