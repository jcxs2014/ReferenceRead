---
title: "§2 Progenitor's Mass and Explosion Energy"
paper: "nomoto-suzuki-2014"
section: 2
nav_prev: "01_introduction.md"
nav_next: "03_8_10msun_ecsn.md"
---

上一章：`01_introduction.md` — §1 Introduction
下一章：`03_8_10msun_ecsn.md` — §3 8–10 M☉ EC-SNe

# §2 Progenitor's Mass and Explosion Energy — 前身星质量与爆炸能量

## 2.1 Pop III 前身星的质量

- [FACT] Pop III 恒星最终的命运取决于**低质量初始恒星通过吸积能增长到的质量**
- [FACT] **Ohkubo et al. (2009)** 对不同反馈与吸积率的情形进行了 Pop III 恒星演化计算（**Fig. 1 左**）：
  - 主序演化期间若**吸积未被大幅抑制**，则可形成**大质量**恒星
  - 图中演化轨迹的**箭头**指示演化方向；**括号数字**给出不同吸积率与辐射反馈效应下的最终质量
  - 作为对照：`M = 1000 M☉` 无吸积演化轨迹
- [FACT] **极端情形**：若 Pop III 主序**全期**维持快速吸积，其质量可**超过 300 M☉** (Ohkubo et al. 2006)——直接连接到 §7 的 PISN / IMBH 物理。
- [FACT] 文中统一用**主序质量 `M`**（记号 `M / M☉`）表示恒星质量，恒星演化、超新星爆炸与核合成模型均以 `M` 为自变量。

## 2.2 核心坍缩 SN 的爆炸能量尺度

- [FACT] **传统默认值**：在核合成计算中，爆炸动能常取 `E ≈ 1 × 10⁵¹ erg`（记作 `E₅₁ = 1`）
- [FACT] **经典范例：SN 1987A**：LMC 内的 SN 1987A 是该能量尺度的校准对象
- [FACT] **能量–质量关系的观测建立**：长 GRB 与核心坍缩 SN 之间的关联被**观测确立**（4 颗 GRB-associated SNe）：
  - GRB 980425/SN 1998bw
  - GRB 030329/SN 2003dh
  - GRB 031203/SN 2003lw
  - GRB 120422A/SN 2012bz (Melandri et al. 2012)

- [FACT] **GRB-SNe 共同属性**：
  | 属性 | 观测值 |
  |---|---|
  | 类型 | Type Ic-BL（宽线谱） |
  | E₅₁ | **30 – 50**（超新星） |
  | ⁵⁶Ni 抛射质量 | **0.3 – 0.5 M☉** |
  | 前身星质量 | SN 前身星的**高质量端** |

- [FACT] 这些性质通过把观测光变曲线、光谱与理论模型（Nomoto et al. 2006）**拟合**得到；汇总于 **Fig. 1 (right)**：25–40 M☉ 区间内，超新星分支与暗淡 SN 分支**同时存在**。

## 2.3 X-Ray Flash–SN 关联（能量低端的延伸）

- [FACT] **发现**：
  - GRB 060218/SN 2006aj：`E₅₁ ≈ 2`，前身星质量 `≈ 20 M☉`
  - GRB 100316D/SN 2010bh：`E₅₁ ≈ 10` (Bufano et al. 2012)
- [FACT] 对比 GRB-SNe：这两颗是**更弱、质量更小**的关联对象，把能量–质量图的**低端**下推到 E₅₁ ≈ 2 区域。

## 2.4 暗淡超新星 (Faint Supernovae)

- [FACT] **观测**：SNe II **1997D** 和 **1999br** 是能量极低的暗淡 SN (Turatto et al. 1998)
- [FACT] **E–M 图的双分支结构**（**核心论断**）：
  - 对于 `M > 20–25 M☉` 的前身星，爆炸能量**不是单一值**，而是分化为：
    - **明亮、高能分支**："hypernova branch"（高 E，大量 ⁵⁶Ni）
    - **暗淡、低能分支**："faint SN branch"（低 E，大部分 ⁵⁶Ni 回落）
  - 在更大质量处，faint SN 分支可能**退化为"失败超新星"分支**（"failed SN branch"）
  - 两支之间存在一个**连续分布的中间区域**
- [FACT] **物理图像（Nomoto et al. 2003）**：
  - `M ≳ 25 M☉` 恒星在演化末期**形成黑洞**
  - **非自转黑洞** → "安静坍缩"，仅少量重元素抛射 → **Faint SN**
  - **自转黑洞** → **超新星**（可能通过双星系统中伴星螺旋进入形成**快速自转核心**）

> [INTERPRETATION] §2 的**核心信息**是：核心坍缩 SN 的产额**不能**用单一 (M, E) 参数对描述，必须考虑 **E–M 双分支**——这一结构**贯穿全文**，并直接决定了后续 §3–§7 各质量区间如何对应到具体 SN 类型。

## 2.5 与 Nomoto 2013 母综述的对应

- [FACT] 本文 §2 基本是 Nomoto et al. 2013 (§4.5 Hypernovae, Faint Supernovae, and 25–140 M☉ Stars) 的**浓缩版**；双分支图像在两篇中一致
- [CRITIQUE] 母综述中的**3D 非球对称性、fallback 详细机制**在本文中**大幅压缩**——读者若需细节需回到 `0020_nomoto-2013`
