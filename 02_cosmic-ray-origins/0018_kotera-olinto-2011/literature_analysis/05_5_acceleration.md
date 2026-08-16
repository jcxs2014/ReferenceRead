> 本章属于：**The Astrophysics of Ultrahigh Energy Cosmic Rays** (Kotera & Olinto, 2011)
>
> 上一章：`04_4_transition.md`
>
> 下一章：`06_6_candidates.md`

# §5 Acceleration Mechanisms

## 1. 本节核心内容

宇宙线加速必须克服两个约束：等离子体普遍抹平大尺度电场、但磁场无处不在，磁场的时空变化提供瞬变电场。作者综述三大类机制：**Fermi 激波加速 (§5.1)**、**单极感应器 (§5.2, 中子星)**、**其他模型 (§5.3, 磁重联/wake-field/shear)**，并强调每种机制的**适用条件、效率上限与失效机制**。

## 2. 原文内容

[FACT] 加速需满足：(a) 达到 EeV–>200 EeV；(b) 注入幂律谱与传播后观测谱匹配。

### §5.1 Fermi acceleration at shock waves

[FACT] Fermi 原理：宏观运动通过磁不均匀性将能量转移给微观粒子。
- **2nd order Fermi** (Fermi 1949)：散射中心随机速度 v/c = β → 单次能量增益 ΔE/E ~ β²（非相对论下低效；相对论情形 Pelletier 1999）
- **1st order Fermi** (Axford et al. 1977; Bell 1978; Blandford & Ostriker 1978)：相干宏观运动 (如激波)，ΔE/E ~ β。SNR 激波是银河 CR 的主加速机制；UHECR 候选区域：GRB 激波、AGN jets、AGN hot spots、引力吸积激波

[FACT] **关键限制 (Lemoine et al. 2006)**：若加速粒子的 Larmor 半径 r_L 远小于磁场相干长度，粒子被俘获在磁感线上被冲走 → Fermi 循环在第一次往返后即停止，除非磁场在 <<r_L 尺度被强放大。

[FACT] **Pelletier et al. 2009**：小尺度湍动磁场的噪声必须压过大尺度相干场的无扰动轨迹 → 上限 r_L 更严格。**超相对论激波下 1st order Fermi 基本失效**（MHD 范围内的 streaming instability 不足以放大磁场）。

[FACT] 可能的突破机制：Weibel-like 不稳定性 (Medvedev & Zakutnyaya 2009)、Cerenkov-plasma mode 共振 (Pelletier et al. 2009)。PIC 模拟 (Silva 2003; Hededal 2005; Spitkovsky 2008; Riquelme & Spitkovsky 2010) 开始看到 Fermi 加速的证据。

[FACT] **Shear acceleration** (Rieger & Duffy 2005; Lyutikov & Ouyed 2007)：粒子沿垂直于 jet 轴的流速梯度穿越 → 加速，与激波加速并列。

### §5.2 Unipolar Inductors

[FACT] 中子星 (及 BH + magnetized disk) 旋转 → 相对论 outflow ("wind")，E = v × B/c 感生电场，提供电压降落加速粒子。

[FACT] 普通脉冲星能量不足 (E > 10²⁰ eV)。

[FACT] **Blasi et al. 2000 magnetar 模型**：毫秒周期、B ~ 10¹⁵ G 表面磁场的年轻磁星：
$$E(\eta) \approx 3\times10^{21}\ \mathrm{eV}\ Z_1 (B/2\times10^{15}\mathrm{G}) (R/10\mathrm{km})^3 (\dot{\Omega}/10^4\mathrm{s}^{-1})^2$$
注入谱：dN/dE = 9η²I (1 + E/E_g)⁻¹ (2ZeBR³E)⁻¹
其中 I = 转动惯量，E_g = 引力波与电磁损失平衡的能量

[FACT] **Arons 2003**：磁星产生 UHECR 只在**极早期**（数天后），是**脉冲式爆发**。

[CRITIQUE] 作者指出：该模型最初为解释 AGASA 时代"无 GZK 截断"引入，需 s=1 硬谱；但当前观测谱不支持 s=1 → 需引入"初始电压分布"软化谱 + 引力波 (Kotera 2011)。

### §5.3 Other models

- **磁重联** (Zweibel & Yamada 2009)：磁场拓扑重联 → 释放能量加速。应用于 pulsar winds (Coroniti 1990; Lyubarsky & Kirk 2001)、新生毫秒脉冲星 (de Gouveia Dal Pino & Lazarian 2000)、GRB outflow (Thompson 2006)、磁星 winds (Arons 2003)
- **Wake-field / Ponderomotive acceleration** (Tajima & Dawson 1979)：粒子冲浪 ride 波 → 加速 (Buckley 1977; Contopoulos & Kazanas 2002)
- 其他 2nd order 过程 (太阳物理常见)：太慢，不适用于 UHECR

## 3. 关键公式

| 公式 | 含义 |
|------|------|
| ΔE/E ≈ β² | 2nd order Fermi 单次增益 |
| ΔE/E ≈ β | 1st order Fermi 单次增益 |
| E(η) ≈ 3×10²¹ eV Z₁ (B/2×10¹⁵ G)(R/10 km)³(Ω̇/10⁴ s⁻¹)² | 磁星 unipolar 感应 |
| dN/dE ∝ η²I (1+E/E_g)⁻¹ (2ZeBR³E)⁻¹ | 磁星注入谱 |
| t_acc ≈ A · t_L | 加速时间 (A~1 for all Fermi types) |
| t_acc ≈ 10⁷ s · η · E₂₀ · B_G⁻¹ · β_sh⁻² | 非相对论 1st order Fermi 在 AGN 中心 |
| E_max (AGN core) ≈ 10¹⁹ eV · η⁻¹/² · B_G⁻¹/² · β_sh | 辐射损失约束的 AGN Emax |

## 4. 关键参数

| 数值 | 单位 | 含义 |
|------|------|------|
| ~10¹⁵ | G | 磁星表面磁场 |
| ~10 ms | 周期 | 磁星早期自转周期 |
| 3×10²¹ | eV | 磁星理论 E_max |
| ~10⁻⁴ | s⁻¹ | 磁星早期 Ω̇ (参考) |
| 10¹⁹ | eV | AGN 中心加速 Emax (辐射损失限制) |

## 5. 图表分析

本章无独立图示（Fermi/单极感应器主要用公式 + Hillas diagram Fig 11 在 §6.1 展示）。

## 6. 作者的逻辑

加速机制分类 → Fermi (最主流) 的关键限制 (r_L 与相干长度) → 超相对论激波失效 → 需要新物理/机制 → 引入磁星单极感应器 (绕开激波限制) → 其他补充机制 → 为 §6 候选源的加速物理打底。

## 7. 我的理解

[INTERPRETATION] 作者对 Fermi 加速的态度是**"原则上能到 UHECR，但超相对论激波条件下很难成立"**。这一判断对 GRB 与 AGN jet 类源是重要限制——它们依赖的正是超相对论激波。因此 §6.1 中 GRB 与 AGN 的 Emax 讨论，本质上是 §5.1 结论的下游。

[INTERPRETATION] 磁星模型的"硬伤"是 s=1 注入谱；作者坦率承认这一缺陷（"does not fit the observed slope"），并给出软化方案。这是学术诚实。

## 8. 潜在问题与值得关注的地方

- [CRITIQUE] PIC 模拟在 2011 年刚开始出现 Fermi 加速的证据——2014–2020 已产生大量定量结果，但核心结论 (超相对论激波下 1st order Fermi 困难) 未被推翻，反而被强化。
- [CRITIQUE] Shear acceleration 在 §5.1 末尾被提，但没有被 §6 的候选源讨论充分采用；AGN jet 中可能更重要。
- [FACT] 磁星模型的早期爆发特征 → 解释了 "UHECR 到达方向与瞬发源不重合" 现象。
