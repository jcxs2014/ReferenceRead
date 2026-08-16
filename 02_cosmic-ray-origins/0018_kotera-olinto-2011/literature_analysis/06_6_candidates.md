> 本章属于：**The Astrophysics of Ultrahigh Energy Cosmic Rays** (Kotera & Olinto, 2011)
>
> 上一章：`05_5_acceleration.md`
>
> 下一章：`07_7_8_search_acks.md`

# §6 Candidate Sources and their signatures

## 1. 本节核心内容

系统评估 UHECR 候选源：**Hillas 判据** (必要但不充分) → 四大候选类别 (引力吸积激波、AGN、GRB、磁星) → 宇宙线天文学 (相关性) → **多信使** (中微子、γ 射线)。本章是全文的重头，直接对应用户路径 A 的重点。

## 2. 原文内容

### §6.1 Candidate Source Requirements

[FACT] **Larmor 半径**：r_L = E/ZeB ≈ 110 kpc · Z⁻¹ (μG/B) (E/100 EeV) ≫ 银河盘厚 → 最高能粒子无法被银河约束 → 河外源。

[FACT] **Hillas 判据** (Hillas 1984)：r_L ≤ R →
$$E_{\max} \approx 1\ \mathrm{EeV}\ Z\ (B/1\ \mu\mathrm{G})\ (R/1\ \mathrm{kpc})$$

[FACT] **Fig 11 (更新版 Hillas diagram)**：B-R 相空间中，蓝线 = 质子 E_max=10²⁰ eV 约束，红线 = Fe。候选源需位于红线以上。仅四类达到：**中子星、AGN、GRB、IGM 吸积激波**。

[FACT] Hillas 是**必要不充分**。需再满足：t_acc ≤ t_esc, t_age, t_loss。
- 逃逸时标：t_esc = R²/(2D)，D = 扩散系数
- 辐射损失时标：t_rad = (6m₄p c³ / T mₑ²) E⁻¹ B⁻² (1 + A)⁻¹，A = 240 U_rad/U_B
- 加速时标：t_acc = η · t_L，η ~1 for all Fermi；非相对论 1st order η ~ β_sh/2
- AGN 中心：t_rad ~ 10⁵ s · E₂₀⁻¹ · B_G⁻² (Eddington equipartition)；t_acc ~ 10⁷ s · η · E₂₀ · B_G⁻¹ · β_sh⁻²
- AGN 中心 E_max ~ 10¹⁹ eV · η⁻¹/² · B_G⁻¹/² · β_sh

[FACT] **Luminosity 下限** (Lemoine & Waxman 2009)：
$$L > L_B \approx \dot{W} R^2 B^2 /2 > 10^{45}\ Z^{-2}\ \dot{W}_{20}^2\ \mathrm{erg\ s^{-1}}$$
只有 FRII/FSRQ 满足 L_B ~ 10⁴⁵ erg/s；FRI、TeV blazar、BL Lac 只有 10⁴²⁻⁴⁴ erg/s (Celotti & Ghisellini 2008)。

[FACT] 粒子逃逸难题：高能量粒子在磁化加速区如何出来？→ 转化为中子 (Mannheim et al. 2001; Rachen 2008)，但幂律谱难保证。

[FACT] 能量密度要求：假设均匀 nsL₁₉：
$$(E^3 dN/dE)_{E=E_{19}} \approx 10^{24}\ eV^2 m^{-2} s^{-1} sr^{-1}\ (n_s/10^{-5}\ Mpc^{-3})(L_{19}/10^{42}\ erg/s)$$
正常星系密度 ~10⁻² Mpc⁻³；FRII ~10⁻⁹⁻¹⁰ Mpc⁻³。

### §6.1.1 Gravitational accretion shocks (cluster 吸积激波)

[FACT] 尺度 ~1–10 Mpc，B ~ 1 μG (van Weeren et al. 2010 测到 bow shock 同步辐射) → 可约束到 ~10²⁰ eV。
[FACT] **关键问题**：shock 上游 B 可能 <1 μG (void 弱磁化) → 需强磁放大 (Schlickeiser & Shukla 2003; Zweibel & Everett 2010)。
[FACT] Vannoni et al. 2009：几 km/s 的激波 + ~1 μG → 质子 E_max ≤ 几 × 10¹⁹ eV (辐射损失限制)。

### §6.1.2 AGN

[FACT] 分类：radio-quiet vs radio-loud。M_BH ~ 10⁹ M☉，中心 B ~ 300 G，R ~ 100 AU → 理论 E_max ~ 150 EeV，静电力可达 10²⁰ eV。但中心辐射损失使实际难达。
[FACT] Radio-loud：jet 内 B·R ~ 0.3 G·pc → E_max ~ 300 EeV；photo-interaction + adiabatic 损失限制。
[FACT] FRII/FSRQ hot spots/bow shocks：加速 + 逃逸比 jet 内容易 (Rachen & Biermann 1993)。
[FACT] 只有 L_B ~ 10⁴⁵ erg/s 的 FRII/FSRQ 满足能量要求。
[FACT] 但**本地 FRII 与最高能 UHECR 到达方向无相关** → 可能 EGMF 更强，或宇宙线为重核。
[FACT] AGN 通常视为**连续源**，但 flare 更易满足加速条件 (Farrar & Gruzinov 2009)。
[FACT] γ 射线特征：质子同步辐射、光致强子级联、μ 子同步辐射等 → 未来 CTA 可区分 hadronic/leptonic。

### §6.1.3 GRB

[FACT] 内激波 B ~ 10⁶ G at R ~ 10¹² cm (来自中心 ~10¹² G, R~10 km, B∝R⁻¹) → 参数覆盖 Fig 11 大片绿区。
[FACT] 加速机制：external shock Fermi (Vietri 1995)；mildly-relativistic internal/reverse shock (Waxman 1995; Murase et al. 2008b)；2nd order Fermi (Gialis & Pelletier 2003) → 可加速到 ~10²⁰ eV（需特定参数）。
[FACT] 能量约束：GRB 率 ~0.3 Gpc⁻³ yr⁻¹ (z=0) → 各向同性 UHECR 注入 E_UHECR ~ 10⁵³ erg (Guetta & Piran 2007)。
[FACT] **瞬发特性** → 解释了为何最高能事件无对应强 counterpart (Vietri 1995; Waxman 1995)。

### §6.1.4 Neutron Stars (Magnetars)

[FACT] 磁星：表面偶极场 ~10¹⁵ G (Wood & Thompson 2004; Harding & Lai 2006)。Blasi et al. 2000：relativistic wind unipolar induction (详见 §5.2)。
[FACT] **仅 5% 河外磁星为 fast-rotators 即可解释观测 UHECR 能量学** (Arons 2003)。
[FACT] 瞬发源 → 不应观测到 UHECR 与到达方向的时间巧合。
[FACT] **铁富含表面** → 自然允许重核注入 → 与 Auger 40 EeV 重核趋势一致。

### §6.2 Cosmic Ray Astronomy at Ultrahigh Energies

[FACT] Trans-GZK 事件偏转 ≤几度 (轻核) → 应与底层重子物质相关。
[FACT] 历史相关尝试：BL Lac (Tinyakov & Tkachev; Gorbunov) 争议大；Supergalactic plane (Stanev et al. 1995) 未被 AGASA 确认，Auger 中重现 (Stanev 2009)。
[FACT] **关键洞察**：Auger 相关的 AGN 大多是**低功率 Seyfert**，非 UHECR 加速器 → 相关性更可能反映**大尺度结构**而非源类识别。
[FACT] "Fake correlation" 效应 (Kotera & Lemoine 2008b; Ryu et al. 2010)：EGMF 时间延迟让瞬发源到达方向"伪造"与前景物质的相关。
[FACT] **时间延迟公式** (Alcock & Hatchett 1978)：
$$t_\Delta \approx 2.3\times10^2\ \mathrm{yr}\ Z^2\ (D/10\ Mpc)^2\ (B/2\times10^{-9}\ G)^2\ (l_B/0.1\ Mpc)^2\ (10^{20}\ eV/E)^{-2}$$
单条磁化 filament 引起的延迟：t_i ~ 0.93×10³ yr (r_i/2 Mpc)² (B_i/10⁻⁸ G)² (l_i/0.1 Mpc) (10²⁰ eV/E)⁻²
→ 瞬发源在 ~10³ yr 量级被"抹平"，解释无时间巧合。
[FACT] 若 E_thr 上检测到各向异性且假定为重核 Z → 应在 E > E_thr/Z 处也见到质子成分的各向异性 (Lemoine & Waxman 2009) → 约束 q_p/q_Z 注入比。

### §6.3 Multi-messenger approach

[FACT] 次级 ν 与 γ 由 UHECR 在源内或传播中产生；不受磁场影响 → 指向源。
[FACT] **γ 射线视界**：>TeV γ 与 CMB/radio 光子相互作用 → e⁺e⁻ → IC cascade → >100 TeV γ 视界 ~几 Mpc (Wdowczyk 1972; Protheroe & Stanev 1993)。EeV 以上光子可长距离传播。
[FACT] **中微子**：不与背景作用 → 长程；但截面小 → 需 km³ 探测器 (IceCube, Auger, ANITA, ARA)。
[FACT] **Cosmogenic 中微子**：UHECR 与 CMB 作用产生 (Greisen 1966 预言)。预测 flux 高度依赖注入谱指数、成分、Emax、源演化 → 不确定度几个量级 (Fig 12)。
[FACT] 可探测 flux 条件 (Fig 12)：
- 大质子 Emax (>100 EeV) + SFR/GRB 演化 + dip/ankle 转换 + 纯质子/银河混合成分
- IceCube：0.06–0.2 ν/年 (EeV 段)
- Auger (水切伦科夫)：0.03–0.06 ν/年

[FACT] Waxman-Bahcall 上限 (1999)：当 pγ optical depth = 1 时中微子光度 vs 观测宇宙线光度之比 → 中微子 flux 上限。
[FACT] 若源光深大 (optically thick) → Allard & Protheroe 2009：宇宙线无法加速到最高能，>EeV ν 被压。

[FACT] **源环境磁场的角色**：星系团磁场可约束 UHECR → 增加相互作用概率 → 提高中微子/γ 产率 (Berezinsky 1997; Colafrancesco & Blasi 1998; Kotera et al. 2009)。

## 3. 关键公式

| 公式 | 含义 |
|------|------|
| r_L = E/ZeB ≈ 110 kpc · Z⁻¹ (μG/B) (E/100 EeV) | Larmor 半径 |
| **E_max = Z·B·e·R·c ≈ 1 EeV · Z (B/μG)(R/kpc)** | **Hillas 判据 (核心)** |
| L > L_B = ẆR²B²/2 > 10⁴⁵ Z⁻² Ẇ₂₀² erg/s | 能量学下限 |
| t_esc = R²/(2D) | 逃逸时标 |
| t_rad = (6m₄p c³/Tmₑ²) E⁻¹ B⁻² (1+A)⁻¹ | 辐射损失 |
| t_Δ ≈ 2.3×10² yr · Z² · (D/10 Mpc)² · (B/2×10⁻⁹ G)² · (l_B/0.1 Mpc)² · (10²⁰ eV/E)⁻² | 磁场延时 |
| E_UHECR (GRB) ≈ 10⁵³ erg | 各向同性 GRB 注入能 |

## 4. 关键参数

| 数值 | 单位 | 含义 |
|------|------|------|
| 1 μG | 磁场 | Hillas 判据参考 |
| 1 kpc | 尺度 | Hillas 判据参考 |
| 10¹⁵ | G | 磁星表面场 |
| 10¹² | G | GRB 中心场 |
| 10¹² | cm | GRB 内激波位置 |
| 10⁶ | G | GRB R=10¹² cm 处 B |
| ~0.3 | G·pc | AGN jet B·R |
| 10⁻⁵ – 10⁻² | Mpc⁻³ | 候选源密度 |
| 10⁴² – 10⁴⁵ | erg/s | 候选源磁光度 |
| 10⁵³ | erg | GRB UHECR 注入能 |
| 10⁻⁹ | G | EGMF 参考 |
| 10³ | yr | 瞬发源到达方向被抹平的时间尺度 |
| 0.06–0.2 | ν/年 | IceCube cosmogenic ν 预期 (Favored models) |
| 0.03–0.06 | ν/年 | Auger cosmogenic ν 预期 |

## 5. 图表分析

- **Fig 11 (Hillas diagram)**：横轴 R (cm)，纵轴 B (G)。蓝线：质子 E_max=10²⁰ eV；红线：Fe E_max=10²⁰ eV。候选源标注：neutron star、white dwarf、AGN、AGN jets、GRB hot spots、SNR、IGM shocks。绝大多数天体达不到 Fe 线。
- **Fig 12 (cosmogenic neutrino flux)**：横轴 E_ν，纵轴 E²·Φ_ν。灰区 = 大质子 Emax + SFR/GRB 演化 + dip/ankle + 纯质子/混合成分。IceCube/Auger 灵敏度曲线展示探测可能性。不确定度跨越几个量级。

## 6. 作者的逻辑

Hillas 判据 → 筛选候选源 (4 类) → 逐一评估加速能力 + 能量学 → 讨论观测关联 (宇宙线天文学) → 指出瞬时源假说 (解决"无对应"问题) → 转到多信使 (次级 ν/γ 是唯一能"指认源"的探针) → 引出 §7 观测计划。

## 7. 我的理解

[INTERPRETATION] 本章最重要的一句话是 "**Hillas 判据是必要不充分**"。大多数早期候选源筛选只做到必要 (B·R 大)；作者强调还必须通过 **t_acc vs t_esc/t_age/t_loss** 竞争、**Luminosity 下限 L_B**、**成分自然产生能力**、**各向异性/对应**、**多信使信号** 五重检验。

[INTERPRETATION] 磁星类源在 2011 年是**"被忽视但自然解释重核 + 无瞬发对应"**的最佳候选；作者明确说 "they are scarcely discussed in the literature"。后续 2017–2022 磁星模型得到更多关注 (Kotera & Lemoine, Arons, Murase 系列)。

[INTERPRETATION] Fig 12 的核心信息：**cosmogenic neutrino 观测是约束 UHECR 模型参数空间最强的单一探针**——一个 EeV 中微子即可在 Fig 12 灰色带中划掉一半模型。

## 8. 潜在问题与值得关注的地方

- [CRITIQUE] Hillas diagram 仅考虑"磁约束"，忽略了辐射损失 (t_rad)、逃逸 (t_esc)、动力学时间 (t_dyn) 竞争；因此 Hillas 通过 ≠ 源成立。作者后续 §6.1 各源分析都在 Hillas 基础上补上这些约束。
- [CRITIQUE] GRB 的"瞬发 + 能量学"论证对 isotropic-equivalent 假设敏感；若考虑 beaming (θ_j ~ 0.1 rad)，实际注入能小 10³ 倍 → 需提高 GRB 率或效率。
- [CRITIQUE] Waxman-Bahcall 上限依赖 τ_pγ = 1 假设；如果 τ << 1 则 ν flux 更低，观测困难更大。
- [FACT] Fig 12 灰区给出的探测预期 (0.03–0.2 ν/年) 与 IceCube 2013 首批 PeV 事件、2017–2020 结果有对比价值——这正是用户路径 A 与 alvesbatista-2019 之间的桥。
