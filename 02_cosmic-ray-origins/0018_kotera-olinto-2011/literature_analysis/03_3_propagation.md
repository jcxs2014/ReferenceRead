> 本章属于：**The Astrophysics of Ultrahigh Energy Cosmic Rays** (Kotera & Olinto, 2011)
>
> 上一章：`02_2_observations.md`
>
> 下一章：`04_4_transition.md`

# §3 The Propagation of Ultrahigh Energy Cosmic Rays

## 1. 本节核心内容

UHECR 从源到地球经历两类过程：(i) 与宇宙背景辐射作用 → 改变能量与成分，不改方向；(ii) 与宇宙磁场作用 → 改变方向与到达时间，不改能量与成分。两过程共同决定观测到的谱形、各向异性、成分，并产生次级中微子与光子（为 §6.3 多信使做铺垫）。

## 2. 原文内容

[FACT] **§3.1 Interaction processes on cosmic backgrounds**：
- 最高能：与 CMB 作用；次高能：与 IR-UV 背景作用 (Kneiske et al. 2004; Stecker et al. 2006)
- 质子光核作用：pγ → Nπⁿ (光致π产生) 或 pγ → pe⁺e⁻ (Bethe-Heitler 对产生)
- 阈值：E_p,π ≈ 200 EeV (ε_CMB/ε) 光致π；E_p,ee ≈ 0.8 EeV (ε_CMB/ε) 对产生；ε_CMB ≈ 2.7 k_B T_CMB ≈ 6×10⁻⁴ eV
- 能量损失长度 x_loss = |E⁻¹ dE/dt|⁻¹；E > 60 EeV 时急剧缩短 → GZK 特征
- **核光致离解**：CMB + IR-UV 光子，三机制按能量递增：
  - Giant Dipole Resonance (GDR, ε ≈ 8–30 MeV)
  - Quasi-Deuteron (QD, ε ≈ 20–150 MeV)
  - Baryonic Resonance (ε ≳ 150 MeV)
- 一次近似下，核的 Lorentz 因子在光致离解中近似守恒
- A < 20 核在几十 Mpc 内即离解 (Fig 4)；只有 Fe 族核能存留至 trans-GZK

[FACT] 传播代码：SOPHIA (Mücke et al. 1999) 解析 photo-hadronic；CRPropa (Armengaud et al. 2007) 蒙特卡洛公开代码；Allard et al. (2006) 完整核传播工具。

[FACT] Emax 若取 ~100 EeV 幂律分布而非单值，未来探测器可在高能端看到谱"回升" (Kachelriess & Semikoz 2006)。

[FACT] **§3.2 Magnetic fields**：
- 银河磁场：偏转 ≤ ~10 Z (40 EeV/E)；规则分量可扭曲源像 (Harari et al. 1999)
- 星系团磁场 ~1–40 μG；团外：B∥² l_B^1/2 ≤ 10⁻⁸ G·Mpc¹/² (Ryu et al. 1998)
- EGMF 范围从 ~10⁻¹⁶ – 10⁻⁹ G；Fermi γ-ray 观测暗示 10⁻¹⁶–10⁻¹⁵ G (Neronov & Vovk 2010)
- **磁化区域层级** (Fig 8)：Galaxy 1 kpc × 10 kpc；halo 10–100 kpc；cluster 5 Mpc；supercluster? 30–40 Mpc；filament 1 Mpc；voids? 10–300 Mpc
- EGMF 起源：原初 (Widrow 2002) vs. 天体污染 (galactic winds/jets, Kronberg 1999; Cen 2005)
- 模拟差异极大：Sigl et al. 2004 得 p >100 EeV 偏转 10–20°；Dolag et al. 2004 得 <1°
- **随机分析方法** (Kotera & Lemoine 2008b)：B < 10⁻¹² G 时偏转 <1°，可视为在磁化散射中心间直线传播 + 局部偏转 (Fig 10)
- **扩散机制**：当 t_scatt (scattering time) 满足 ² ~ 1 时进入扩散；强场下 UHECR 可被"困"在局部巨超星系团 (Lemoine et al. 1999)
- **磁视界**：若粒子路径长度 > cH₀⁻¹，则源不可见 → d ≈ c H₀⁻¹ t_scatt¹/² ≈ 65 Mpc (c t_scatt / 1 Mpc)¹/² → 在低能段产生"磁截断"

## 3. 关键公式

| 公式 | 含义 |
|------|------|
| E_p,π ≈ 200 EeV (ε_CMB/ε) | 光致π产生阈值 |
| E_p,ee ≈ 0.8 EeV (ε_CMB/ε) | 对产生阈值 |
| x_loss = \|E⁻¹ dE/dt\|⁻¹ | 能量损失长度 |
| t_delay ≈ 2.3×10² yr · Z² · (D/10 Mpc)² · (B/2×10⁻⁹ G)² · (0.1 Mpc/l_B)² · (10²⁰ eV/E)⁻² | 磁场引起的时间延迟 (§6.2 引用) |
| d_mag ≈ 65 Mpc · (c t_scatt / 1 Mpc)¹/² | 磁视界 |

## 4. 关键参数

| 数值 | 单位 | 含义 |
|------|------|------|
| ε_CMB ≈ 6×10⁻⁴ | eV | CMB 平均光子能量 |
| 60 EeV | 能量 | GZK 能量损失陡降起始 |
| 8–30 / 20–150 / ≳150 | MeV | GDR / QD / Baryonic 能段 |
| ~1–40 | μG | 星系团磁场 |
| 10⁻¹⁶–10⁻⁹ | G | EGMF 允许范围 |
| 10⁻¹⁶–10⁻¹⁵ | G | Fermi 暗示 EGMF 强度 |
| ~100 Mpc | 距离 | 磁视界典型尺度 |

## 5. 图表分析

- **Fig 7 (proton energy loss lengths)**：黑线为 CMB+IR-UV 光致π，红线为 CMB 对产生；虚线为 interaction length；点线为宇宙学红移损失。E > 60 EeV 时 x_loss 骤降。
- **Fig 8 (magnetized regions schematic)**：从 Galaxy (1 kpc×10 kpc) → halo (10–100 kpc) → cluster (5 Mpc) → filament (1 Mpc) → supercluster (30–40 Mpc) → voids (10–300 Mpc)。直观展示 UHECR 传播途经的所有磁化区。
- **Fig 9 (EGMF filling factor)**：Sigl 2004 (蓝虚线)、Dolag 2005 (红点虚)、Das 2008 (粉长虚)、Donnert 2009 (绿实)。不同模拟方法 → 填充因子差异显著。
- **Fig 10 (deflection skymap)**：E ≳ 6×10¹⁹ eV 质子，Kotera & Lemoine 2008b 方法，假设 3 次散射中心 /100 Mpc、每次 ~1.7° 偏转。白点 = Auger 事件。

## 6. 作者的逻辑

传播 = 背景辐射 + 磁场两个独立维度 → 谱 (被背景辐射决定) 与 各向异性 (被磁场决定) 分离 → 传播模型能拟合观测谱 (Fig 2) → 次级中微子/光子是观测"验证传播"的关键 → 自然过渡到 §4 转换、§6.3 多信使。

## 7. 我的理解

[INTERPRETATION] 本节最重要的思想是**将"观测谜题"归因到"传播物理的两个独立自由度"**：成分/谱 ← 背景辐射 (可计算、物理明确)；方向性 ← 磁场 (未知、模拟差异巨大)。这让"成分变重"和"各向异性"不再矛盾：一个靠 p/Fe 光致损失自然解释，一个靠 EGMF 不确定性吸收。

[INTERPRETATION] Fig 8 的层级化磁化区是本文最"信息密度高"的一张图——它把 UHECR 传播的物理路径压缩成一张分层地图，是理解后续所有"偏转 - 延时 - 磁视界"讨论的锚点。

## 8. 潜在问题与值得关注的地方

- [CRITIQUE] EGMF 强度从 10⁻¹⁶ 到 10⁻⁹ G 的跨度 (7 个数量级) 意味着磁场对 UHECR 的所有预测都是"模型依赖的"。2011 年的这一认知 → 2013–2017 的 EGMF 约束进展 (Neronov & Vovk 后续修订、Blazars γ-ray cascades)。
- [CRITIQUE] 核光致离解的近似"守恒 Lorentz 因子"仅一阶正确；实际光致离解会改变 Z/A 比 → 影响 Xmax 预测 → 影响 §2.3 成分判读。这是 Auger 成分分析的**系统性未决问题**之一。
- [FACT] t_delay 公式是 §6.2 中"瞬时源与 UHECR 到达无时间巧合"的关键物理依据。
