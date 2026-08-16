# 1. Introduction（引言）

**上一章**: 无（本文开篇） · **下一章**: [02_preagb.md](02_preagb.md) §2

## 1.1 引言核心

[FACT] 本文是 *Dawes Review 2*，题为 "Nucleosynthesis and stellar yields of low and intermediate-mass single stars"（Karakas & Lattanzio 2014, PASA, arXiv:1405.0062v1）。

[FACT] 初始质量在约 **0.8M⊙ 至 10M⊙** 之间的恒星主导银河系恒星种群，跨越从最长寿命的低质量恒星（~1.2×10¹⁰ 年，即银河系年龄）到 ≈20 Myr 的短寿命大质量恒星。

[FACT] 这些恒星对银河系化学演化至关重大（Travaglio et al. 2001a；Romano et al. 2010；Kobayashi et al. 2011b），并通过强星风/包络抛射产生近 **90% 的银河系 ISM 尘埃**（Sloan et al. 2008），大质量恒星产生其余部分。

[FACT] 低中质量恒星演化阶段：主序 → 红巨星支（RGB，一 dredge-up FDU）→ 水平支 → AGB（二 dredge-up SDU、热脉冲、三 dredge-up TDU）→ WD（C-O/ONe）。

[FACT] 银河系中间年龄恒星种群的光度在演化离开主序进入巨分支后由低中质量恒星显著贡献（Mouhcine & Lançon 2002；Maraston 2005）。

## 1.2 质量区定义

**表格 1.1 — 质量区间划分（图 1）**

| 名称 | 初始质量 (M⊙) | 关键核反应 | 最终残骸 |
|------|---------------|-----------|---------|
| 最低质量星 | <0.8 | 仅中心 H 燃烧 | 完全冷却 WD |
| 低质量星 | 0.8–2.25 | 简并 He 闪（core He flash） | C-O WD |
| 下中质量 | 2.25–4 | 中心 C 不点燃 | C-O WD |
| 中中质量 | 4–8 | 中心 C 点燃 | ONe WD |
| 上中质量 | 8–10 | 中心 Ne/… 电子俘获 | e- capture SN → NS |
| 大质量 | >10 | Fe 核坍缩 | 坍缩 SN → NS/BH |

[FACT] 边界依赖金属度：Z=10⁻⁴ 时 C 点燃 ~7M⊙，Z=Z⊙≈0.014 时 ~8M⊙。

## 1.3 恒星的产额计算（Stellar Yield Calculations）

[FACT] 恒星的产额定义为恒星生命周期内通过风/星风/抛射进入 ISM 的核素增量。对低中质量恒星，产额主要源于 AGB 阶段的强星风。

[FACT] 化学演化模型需要质量 × 金属度网格上的产额表。历史上 AGB 恒星被忽略（Matteucci & Francois 1989；Timmes et al. 1995），但过去 10 年内被证明对 C、N、F、Na、s-过程重元素贡献巨大。

## 1.4 本文结构

[FACT] 全文共 8 个主体章节 + 附录/参考文献：§1 引言 → §2 AGB 前演化（FDU、SDU、Li、低金属度）→ §3 AGB 演化与核合成（TP、HBB、TDU、s-过程、PIE、Super-AGB）→ §4 主要不确定性（对流、质量损失）→ §5 银河系化学增丰（含产额表）→ §6 总结与展望。

[INTERPRETATION] 本文定位为 *review*，而非原始研究——Karakas & Lattanzio 提供 AGB 恒星核合成与产额领域的最新综述，尤其突出他们自己 1–8M⊙、Z=10⁻⁴–0.02 的详细模型网格。

## 1.5 关键定量公式（贯穿全文）

**[FACT] 恒星初始—最终质量关系（IFMR）**（本文 §1.2 + §4.2 形式化）：

$$M_{\rm WD} = f(M_{\rm ZAMS}, Z) \approx 0.55 + 0.45\,\exp[-(M_{\rm ZAMS} - 1)/1.5]$$

经验拟合（Karakas & Lattanzio 2014 模型网格给出）。$M_{\rm ZAMS} \in [1, 8]\,M_\odot$ 时，$M_{\rm WD} \approx 0.55$–$1.0\,M_\odot$——本文 §1.2 / §4.2 据此给出恒星残骸与初始质量的关系。

**[FACT] AGB 产额定义**（本文 §1.3）：

$$Y_i(M, Z) = \int_{\rm AGB} \dot{M}_{\rm wind}(t)\,X_i(t)\,dt$$

其中 $Y_i$ 为核素 $i$ 在金属度 $Z$、初始质量 $M$ 的产额（$M_\odot$），$\dot{M}_{\rm wind}$ 为 AGB 星风质量损失率，$X_i(t)$ 为核素 $i$ 在抛射时刻的表面质量分数。本文 §3-§5 所有产额表基于此公式。

**[FACT] AGB 演化时间尺度**（本文 §1.1）：

$$t_{\rm AGB} \sim 10^{6-7}\,\mathrm{yr} \ll t_{\rm MS} \sim 10^{9-10}\,\mathrm{yr}$$

AGB 阶段相对主序极短，但对化学增丰的边际贡献最大——本文 §1.1 据此论证"AGB 阶段单位时间核合成产率最高"。

**[FACT] 质量损失率—周期关系**（本文 §3 Reimers → Vassiliadis-Wood）：

$$\dot{M} = \dot{M}_{\rm VW}(P, M) \approx 10^{-11.4 + 0.0125(P-100)}\,L/c^{2} \cdot \eta$$

Vassiliadis & Wood (1993) 经验公式，$P$ 为脉动周期（天），$\eta$ 为模型参数。本文 §3 / §4 据此作为 AGB TDU 计算的输入。

**[FACT] 产额表与化学演化耦合**（本文 §1.4 / §5）：

$$\frac{dX_i}{dt} = \frac{\partial}{\partial t}\left[\dot{M}_{\rm SF} \langle Y_i \rangle + {\rm sources}_i\right]$$

其中 $\langle Y_i \rangle$ 为 IMF × 产额表积分的均值。本文 §5 把产额表输入到化学演化代码（cbe/GEAR）。

上一章：无（本文开篇）
下一章：[02_preagb.md](02_preagb.md) §2
