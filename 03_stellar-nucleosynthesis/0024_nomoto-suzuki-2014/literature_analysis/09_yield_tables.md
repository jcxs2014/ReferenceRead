---
title: "§9 Yield Tables for Core-Collapse Supernovae"
paper: "nomoto-suzuki-2014"
section: 9
nav_prev: "08_emp_profiling.md"
nav_next: "10_conclusion.md"
---

上一章：`08_emp_profiling.md` — §8 EMP Profiling
下一章：`10_conclusion.md` — §10 Concluding Remarks

# §9 Yield Tables for Core-Collapse Supernovae — 核心坍缩 SN 产额表

本章是全文的**数据落点**——把 §3–§8 的物理讨论转化为**可用于 GCE 建模的具体产额表**，同时给出**历史产额表的问题清单**与**Nomoto et al. 2013 表的规格**。

## 9.1 质量范围选择

- [FACT] **GCE 主力区间**：`10 – 140 M☉` 恒星对 C 到 Fe-peak 元素的富集**贡献最大**——产额表以该区间为主

## 9.2 历史产额表及其问题

### 9.2.1 Woosley & Weaver 1995 (WW95)

- [FACT] **贡献**：最早以 M 和 Z 为参数的系统产额表，被 GCE 研究**广泛使用**
- [FACT] **问题 1**：**前置爆炸演化中未包含质量损失**
- [FACT] **问题 2**：核心坍缩 SN 模型**质量切割过深** → Fe 产额比 SN 1987A、1993J、1994I **偏大约 2 倍** → 抛射中 [α/Fe] ≈ 0，与贫金属星观测到的 [α/Fe] > 0.2 **不符**
- [FACT] **问题 3**：GCE 模型中若强行将 Fe 产额**人为减 2 倍**（如 Timmes et al. 1995, Romano et al. 2010）→ Fe-peak 元素间相对比**破坏**

### 9.2.2 Portinari et al. 1998

- [FACT] **方法**：从含质量损失的恒星演化模型得到 **C+O 核质量**，再采用对应 **C+O 核质量的 WW95 产额**
- [FACT] **遗留问题**：
  1. WW95 的 **Fe 产额问题**未解决
  2. **C+O 核结构保留质量损失记忆**——即使 C+O 核质量相同，**含/不含**质量损失模型的核结构显著不同 (Woosley et al. 1993)
  3. WW95 的 **`M = 40 M☉, E = 1 × 10⁵¹ erg`** 模型 **Mg 产额异常偏低**（相比其他模型）——此模型在 Timmes 1995 中未被采用，但在 Portinari 1998 的 GCE 模型中**贡献过大**

### 9.2.3 Hashimoto 1989 / Thielemann 1996 / Nomoto 1997

- [FACT] 太阳金属丰度 (`Z = Z☉`) 模型通过 **⁵⁶Ni 质量 vs. 主序质量关系**（从 SN 光变曲线与光谱获得）**确定质量切割**
- [FACT] **问题**：**仍不含质量损失**

> [CRITIQUE] §9 的历史评述清晰表明：**GCE 产额表 30 年演化**的核心挑战始终是 **"质量损失 + 质量切割 + Fe-peak 一致性"** 三者的耦合。这一诊断是 Nomoto 2013 表的**动机**。

## 9.3 Nomoto et al. (2013) 在线产额表

- [FACT] **最新进展**：多组提供核心坍缩 SN 与 HN 的产额 (Limongi & Chieffi 2006, 2012; Nomoto et al. 2006; Tominaga et al. 2007b; Heger & Woosley 2010)
- [FACT] **Nomoto et al. 2013 表的规格**：
  - 参数：主序质量 `M` 与金属丰度 `Z`
  - **含质量损失**
  - **Fe-peak 元素通过混合与回落自洽得到**
  - **⁵⁶Ni 抛射质量 vs. M 关系**通过观测约束确定
  - 数据来源：Nomoto et al. 2006, Kobayashi et al. 2006（含 Kobayashi et al. 2011 更新的三个模型），及 `Z = 0.05` 模型

### 9.3.1 正常核心坍缩 SN 表 (`E₅₁ = 1`)

| 金属丰度 Z | 包含的质量 M (M☉) |
|---|---|
| `Z = 0` | 11, 13, 15, 18, 20, **25, 30, 40, 100** |
| `Z = 0.001, 0.004, 0.008, 0.02, 0.05` | 13, 15, 18, 20, **25, 30, 40** |

### 9.3.2 超新星 (HN) 表

采用观测+模型得到的 **(M–E) 关系** (Fig. 1 right)：

| 金属丰度 Z | (M/M☉, E₅₁) 集合 |
|---|---|
| `Z = 0` | (20,10), (25,10), (30,20), (40,30), **(100,60)** |
| `Z = 0.001, 0.004, 0.008, 0.02, 0.05` | (20,10), (25,10), (30,20), (40,30) |

- [FACT] 在线表还包含**放射性物种表 (radioactive species tables)**

> [INTERPRETATION] Nomoto 2013 表是本文的**最终交付**：它把超新星、暗淡 SN、PISN、SN Ia 四类机制的产额**首次在一个自洽的 (M, Z) 网格上**整理，且把**质量损失 + 混合回落 + Fe-peak 一致性**三问题**同时解决**——直接支撑 §8 的丰度拟合，也为后续 GCE 研究提供**定量输入**。
