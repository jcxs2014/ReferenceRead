> 本章属于：Bhattacharjee & Sigl (1999), Phys. Rep. 320, 1–150
>
> 上一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/07_source_search_transport.md|07_source_search_transport.md]]
>
> 下一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/09_topdown_basic_fragmentation.md|09_topdown_basic_fragmentation.md]]

---

# 8. Bottom-up Acceleration & Sources (§5, p. 40–48)

## 8.1 本节核心内容

- DSAM 加速机制的简单模型推导，给出 E_max 的"benchmark"估计（公式 49）。
- Hillas 判据（公式 51）筛选候选源：AGN、射电星系、脉冲星等。
- AGN/Radio-galaxy 作为 UHECR 源的论证：**AGN 核心**被排除（能量损失严重）；**FR-II 射电星系 hot spots** 是主要候选（E_max 可达 ~$10^{21}$ eV），但受**距离**问题困扰。
- 脉冲星加速：除 magnetar 与 Fe 风模型外，绝大多数不超过 ~$10^{15}$ eV。
- GRB 与 UHECR 可能的关联（dissipative wind 模型）。

## 8.2 §5.1 DSAM 最大能量 (公式 43–50)

### 8.2.1 基本框架 [FACT]

```
dE/dt = E/T_acc                                    (43)
q = 1 + T_acc/T_esc                                (44)
T_acc = (3/($u_{1}$−$u_{2}$)) · ($D_{1}$/$u_{1}$ + $D_{2}$/$u_{2}$)            (45)
$D_{1}$,₂ ~ $\lambda$/3 > gE/(3ZeB)                            (46)
```
- 非相对论激波 g=1；相对论激波 MC 模拟 g ≃ 40 [342]，但有额外的 ~10× 补偿因子（高倾角）和 ~13.5×（平行）。

**最小 T_acc (公式 47)**：
```
T_acc >~ (g/2.25) · E/(ZeB)
```

**谱指数 (公式 48)**：
```
q(E > E_diff) ~ 1 + E/(2.25 E_diff),  其中 E_diff ≡ ZeBR/g
```

**最大能量（q=3 时） (公式 49)** [FACT] — **benchmark 估计**：
```
E_c ≡ E_{q=3} ~ $10^{17}$ · Z · (R/kpc) · (B/$\mu$G)  eV
```
- 假设 B 平行激波法线。

**倾斜磁场额外漂移加速 (公式 50)**：
```
E_max = Ze $u_{1}$ B R ~ $10^{18}$ · Z $u_{1}$ · (R/kpc) · (B/$\mu$G)  eV
```
- 比 (49) 高 ~10×（$u_{1}$ → c 时），但需要特殊条件（plasma 效应使 E 场更小）。

### 8.2.2 谱斜率 [FACT]

- 简单 DSAM：q = (r+2)/(r−1)，r<4 → q>2（典型 ~2.3–2.4）。
- 强激波 back-reaction：q = 1.5（harder）[337]。
- 超相对论激波 ($\Gamma$ → ∞)：q ≃ 2.2（softer）[338]。
- 相对论 blast wave：第一次 crossing ~ $\Gamma^{2}$ 能量增益，后续 cycles ~ 2× [339]。

## 8.3 Hillas 判据 (公式 51) [FACT]

```
(B/$\mu$G) · (R/kpc) > 2 · (E/$10^{18}$ eV) · 1/(Z $\beta$)
```
- 加速区尺寸 R > 回旋半径 2 r_g。
- **Hillas 图 (Fig. 25)**：只有 AGN、射电星系、脉冲星等少数源满足 ~$10^{20}$ eV 加速条件。

## 8.4 §5.2 Source Candidates

### 8.4.1 AGN & Radio-Galaxies

**支持 AGN 作为 UHECR 源的证据** [FACT]：
1. **Mrk 421, Mrk 501** (BL Lac) 在 > 10 TeV $\gamma$ 被观测 → 可由质子光 $\pi$ 产生解释（vs IC）。
2. EGRET diffuse $\gamma$-ray 能量密度 ~ E⁻² 质子注入谱到 $10^{20}$ eV 所需能量 → 支持河外质子加速。

**反对 AGN 核心作为 EHECR 源** [FACT, Norman et al. [13]]：
- AGN 核心典型 R ~ 0.02 pc, B ~ 5 G → 公式 (49)：E_c ~ $10^{19}$ eV。
- **主要问题**：中心引擎内辐射场强烈 → 加速质子通过 photo-pion 严重衰减。
- 同时考虑加速与能量损失 → 质子或核在 **E > ~$10^{16}$ eV 无法逃出核心**。
- 中子假设也不行（中子本身也受 photo-pion 衰减）。

**FR-II 射电星系 hot spots** [FACT] — **最有希望的加速器**：
- Hot spot 周围 soft photon 密度低 → photo-pion 损失不显著。
- 若 B 场足够强 → **E_max 可达 ~$10^{21}$ eV**。
- 但**主要问题**：hot spot 距地球大 cosmological 距离 > 100 Mpc [26] → GZK 效应使其粒子无法存活。
- **结论**：射电星系 hot spots 可能是 UHECR (>$10^{17}$ eV) 源，但**难以解释 $10^{20}$ eV 以上事件**。

**Boldt–Ghosh [27] 建议**：自旋超大质量黑洞（不活跃 quasar 遗迹）事件视界附近加速 → E_max ~ $10^{21}$ eV；本地 50 Mpc 内足够多候选 → 可解释 EHECR 通量。

### 8.4.2 Waxman-Bahcall Bound [FACT]

- [218]：比较 UHECR 通量 (E ~ $10^{19}$ eV) → 对 diffuse $\nu$ 通量给出更强上界。
- Mannheim, Protheroe, Rachen [353] 声称存在 loophole（仅 $10^{16}$ – $10^{18}$ eV 适用）。
- Bahcall & Waxman [352] 反驳 → 认为 bound **robust**。
- **不适用于**：对质子光学厚的源（如 AGN 核心）；**不适用于 top-down**（$\nu$ 是初级而非次级）。

### 8.4.3 Pulsars [FACT]

- **简单脉冲星直接加速**：~$10^{21}$ eV 势差，但 **pair-cascade 短路** → 实际 < $10^{15}$ eV。
- **吸积盘**：能量损失限制 ~$10^{15}$ eV。
- **Magnetar** (SGR 1900+14)：表面 B ~ $10^{15}$ G → 能量预算提高 2–3 个量级，但损失问题未解决。
- **Fe 离子 MHD 风** [355]：新形成强磁化脉冲星（初始 P < 4(B_s/$10^{13}$ G)^(1/2) ms）→ 可加速 Fe 离子 > $10^{20}$ eV，预言 EHECR 组成以 Fe 为主（可检验）。

### 8.4.4 其他候选源

| 源 | E_max | 备注 |
|---|---|---|
| 银河风终止激波 | 可能达 UHE | 依赖 B |
| 星系碰撞激波 | ~UHE | [357] |
| 星系团吸积/合并激波 | UHE | [358,359] |
| 结构形成大尺度激波 | UHE | [13] |

一般难以超过 $10^{20}$ eV。

## 8.5 §5.3 GRB-UHECR 关联

### 8.5.1 基本动机 [FACT]

- UHECR 所需能量释放率 ~ GRB $\gamma$ 辐射率 [361,362]。
- 预言谱与观测谱 E > ~$10^{19}$ eV 一致（质子注入 E⁻²·³±⁰·⁵ [288]，Fermi 加速）。
- **主要问题**：GZK 距离内 (< 50 Mpc) 宇宙学 GRB 率 ~**每世纪一次** → 观测 UHECR 时间窗内概率极低，除非磁场导致 > 百年时间延迟。

### 8.5.2 磁场下限 (公式 52) [FACT]

```
B >~ $10^{-10}$ · (E/$10^{20}$ eV) · (d/30 Mpc)⁻¹ · (l_c/1 Mpc)⁻^(1/2)  G
```
- N 个不同到达方向 → bound 增强 N^(1/2) 倍。
- 最近观测各向同性 [8] + EGMF 上界 [363] → 已构成挑战。
- GRB 距离标度变大 → 能量要求更苛刻 [363]。

### 8.5.3 Dissipative Wind Model [FACT]

- 光 + e⁺e⁻ + 少量重子风 → 超相对论 Lorentz 因子 $\gamma$ ≫ 1。
- 耗散半径 r_d 处 internal shock → 部分动能转 $\gamma$ 射线（GRB）。
- 耗散产生 near-equipartition 磁场 → 二阶 Fermi 加速。

**三重条件** [FACT]：
1. **加速时间 < 膨胀时间** (公式 53)：
```
B >~ (E/erg) ≃ $3\times10^{4}$ · (E/$10^{20}$ eV) · (r_d/$10^{13}$ cm)⁻¹  G
```
2. **$\pi$ 产生损失 < 加速** (公式 54)：
```
B >~ 20 · (L_$\gamma$/$10^{51}$ erg/s) · (r_d/$10^{13}$ cm)⁻² · ($\gamma$/300)⁻²  G
```
3. **同步损失 < 加速** (公式 55)：
```
B <~ $3\times10^{5}$ · ($\gamma$/300)² · (E/$10^{20}$ eV)⁻²
```

**同时满足**：需 r_d > $10^{12}$ ($\gamma$/300)⁻² (E/$10^{20}$ eV)³ cm（公式 56），以及 **$\gamma$ > 40 (E/$10^{20}$ eV)^(3/4) (t_GRB/s)⁻^(1/4)**。

### 8.5.4 次级产物 [FACT]

- **$\nu$ 通量**：~$10^{14}$ eV，数十事件/km³ 中微子望远镜 [365,370]；> $10^{19}$ eV 可被 AIRWATCH/MASS 探测 [366]。
- **MACRO 上界**：每个 GRB $0.87\times10^{-9}$ cm⁻² $\mu$ 通量 [372]。
- **同步辐射信号**：~1% 总 burst 能量在 10 MeV（GLAST 可探测）；数百 GeV（IACT 可探测）；~TeV afterglow [367–369]。
- 若 GeV cascade 解释 diffuse $\gamma$-ray → 每个 GRB 释放 ~$10^{56}$ erg，$\gamma$ > 500。

### 8.5.5 Waxman-Bahcall 与 Top-down 的区别 [FACT]

- Bottom-up（AGN/Radio/GRB）：$\nu$ 是次级产物，受 diffuse GeV $\gamma$-ray background 约束。
- Top-down：$\nu$ 是初级，通量可显著高于核子 → 但仍受 diffuse GeV $\gamma$ 约束（§7.4）。

## 8.6 关键数值速查

| 量 | 值 |
|---|---|
| DSAM E_c (benchmark, 公式 49) | $10^{17}$ Z (R/kpc)(B/$\mu$G) eV |
| 漂移加速 E_max (公式 50) | $10^{18}$ Z $u_{1}$ (R/kpc)(B/$\mu$G) eV |
| Hillas 判据 (公式 51) | B($\mu$G)·R(kpc) > 2·(E/$10^{18}$ eV)/(Z$\beta$) |
| AGN 核心 E_c | ~$10^{19}$ eV（但损失使可逃出 < $10^{16}$ eV） |
| FR-II hot spot E_max | 可达 ~$10^{21}$ eV（若 B 足够） |
| GRB 条件 $\gamma$ > | 40 (E/$10^{20}$ eV)^(3/4) (t/s)⁻^(1/4) |

## 8.7 [CRITIQUE] 与 1999 年后对照

- [FACT] **AGN 核心 vs hot spot** 的争论在 Auger 时代得到部分澄清：UHECR 到达方向与**近邻 AGN/星暴星系**的相关（Auger 2017–2020），暗示**河外离散源是 UHECR 主要成分**。
- [FACT] **Fe 组成**：Auger 显示 E > ~$10^{19}$·⁵ eV 组成**变重**（倾向 Fe），支持 §5.2.2 中 magnetar Fe 风模型或类似的重核加速源。
- [CRITIQUE] **GRB-UHECR 关联**：Auger 未发现显著 GRB 关联； IceCube 也未发现 UHE $\nu$ 与 GRB 关联 → 弱化了 §5.3 的 GRB 情景。