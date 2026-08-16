---
title: "§1 Introduction"
paper: "nomoto-suzuki-2014"
section: 1
nav_prev: ""
nav_next: "02_progenitor_energy.md"
---

上一章：（无）
下一章：`02_progenitor_energy.md` — §2 Progenitor's Mass and Explosion Energy

# §1 Introduction — 引言

## 1.1 宇宙重元素的起源问题

- [FACT] **BBN 的局限**：大爆炸核合成仅产生最轻元素（H、He、D、极少量 Li/Be），而 C、O、Ne、Mg、Si、Fe 等更重的元素**必须在恒星演化与爆发的过程中合成**——本文由此引入"恒星核合成"这一主题。
- [FACT] **第一星 (Pop III) 的角色**：宇宙早期首批恒星（**金属丰度为零，Pop III**）演化的末期以超新星（SNe）形式爆发，释放**巨大爆炸能量**并**抛射核合成富集的星周物质**——这是宇宙中"第一批重元素"的来源。

> [INTERPRETATION] 本文把超新星**同时**视为化学富集（chemical enrichment）与能量反馈（energy feedback）的双载体，因此其**产额**（yields，即每颗 SN 抛射的各元素质量）是星系化学演化（GCE）模型的**核心输入量**。

## 1.2 为什么 EMP 星能"读取"单颗 SN 的指纹

- [FACT] **早期宇宙的低丰度环境**：早期宇宙金属含量极低，**单颗 SN 的抛射**可以**主导**该气体原本已有的金属含量。
- [FACT] **下一代恒星继承单 SN 产物**：下一代恒星从被该 SN 富集的气体中形成；这些恒星中的长寿命低质量星至今仍可观测，被定义为**极贫金属星 (Extremely Metal-Poor, EMP)** (Beers & Christlieb 2005)。
- [FACT] **结论**：EMP 星的元素丰度模式**反演**给出 Pop III SN 的核合成产额，进而**约束第一星的质量区间**。

### 1.2.1 金属贫乏星的分类（Beers & Christlieb 2005）

| 分类 | 记号 | 金属丰度范围 |
|---|---|---|
| Very Metal-Poor | VMP | −3 < [Fe/H] < −2 |
| Extremely Metal-Poor | EMP | −4 < [Fe/H] < −3 |
| Ultra Metal-Poor | UMP | −5 < [Fe/H] < −4 |
| Hyper Metal-Poor | HMP | −6 < [Fe/H] < −5 |
| Mega Metal-Poor | MMP | [Fe/H] < −6 |

> [FACT] 上表的 [Fe/H] 区间在本文 **§8 各小节**中会被逐一使用——这是本文明确采用的"丰度档案"（abundance profiling）分析框架。

## 1.3 观测对理论的两重挑战

- [FACT] **挑战 1 — 异常丰度的 EMP 星**：近年发现若干 EMP 星的丰度模式**极为异常**，包括：
  - **碳增强金属贫乏星 (Carbon-Enhanced Metal-Poor, CEMP)**：显著 [C/Fe] 增丰
  - **HMP 星**：如 HE 1327-2326、HE 0107-5240
  - 这些**与以往大质量恒星核合成产额显著不同**，对恒星演化与核合成理论提出挑战。
- [FACT] **挑战 2 — GRB–SN 关联**：已光谱证实 4 颗与伽马射线暴 (GRB) 相关的 SN：
  - GRB 980425/SN 1998bw、GRB 030329/SN 2003dh、GRB 031203/SN 2003lw、GRB 120422A/SN 2012bz
  - 均为**动能 E > 10⁵² erg 的极强 SN**（> 10 倍于正常核心坍缩 SN）
- [FACT] **超新星 (Hypernova, HN) 定义**：本文采用动能 `E > 10 E₅₁`（即 `E₅₁ ≡ E/10⁵¹ erg > 10`）作为超新星的判据（Woosley & Bloom 2006）。

> [INTERPRETATION] 超新星的**引入**把 "GRB 天体物理学" 与 "恒星核合成" 这两个分支用**同一个物理量**（爆炸能量 E₅₁）联系起来——HN 既是化学富集的强源，也是 γ 暴的物理前身。

## 1.4 本文范围与方法

- [FACT] 本文**简要评述**核心坍缩 SN 的核合成模型最新进展，重点关注：
  1. 爆炸能量（从 HN 到 faint SN）
  2. **混合与回落 (mixing & fallback)**：加工物质的重新分布
  3. **非球对称性 (asphericity)**：喷射型（jet-induced）爆炸
- [FACT] 这些 SN 核合成模型的**参数**通过 **EMP/UMP/HMP 星**的观测丰度**约束**
- [FACT] **方法论**：将恒星核合成产额与 EMP/UMP/HMP 星的丰度模式**逐一对比**，形成"单 SN 机制识别"（individual SN mechanism identification）的新途径
- [FACT] 更详细的推导见 **Nomoto, Kobayashi & Tominaga 2013 (ARAA 51:457)**——本库 `0020_nomoto-2013`（本文的**母综述**）

> [CRITIQUE] 作为一篇 IAU 短综述（13 页），本文不推导公式、不给出新的产额数据，而是**把 Nomoto 2013 母综述的核心结论重新聚焦到"产额对 GCE 建模的约束"**这一应用层。因此本文的价值在于**产额表应用的物理论证**，而非新的理论推导。
论文采用惯例的金属丰度对数记号：

$$
[\mathrm{X}/\mathrm{H}] \equiv \log_{10}\!\left(\frac{N_{\mathrm{X}}}{N_{\mathrm{H}}}\right)_{\star} - \log_{10}\!\left(\frac{N_{\mathrm{X}}}{N_{\mathrm{H}}}\right)_{\odot}
$$

$$
[\mathrm{X}/\mathrm{Fe}] \equiv [\mathrm{X}/\mathrm{H}] - [\mathrm{Fe}/\mathrm{H}]
$$

超新星动能以 $10^{51}$ erg 为单位归一化：

$$
E_{51} \equiv \frac{E}{10^{51}\,\mathrm{erg}}
$$

**超新星 (Hypernova) 判据**（§1, Woosley & Bloom 2006）：

$$
E_{51} > 10 \quad \Longleftrightarrow \quad E > 10^{52}\,\mathrm{erg}
$$

**极贫金属 (EMP) 星分级**（Beers & Christlieb 2005；§1.2.1）：

$$
\begin{cases}
-3 < [\mathrm{Fe}/\mathrm{H}] < -2 & \text{VMP (Very Metal-Poor)}\\
-4 < [\mathrm{Fe}/\mathrm{H}] < -3 & \text{EMP}\\
-5 < [\mathrm{Fe}/\mathrm{H}] < -4 & \text{UMP (Ultra Metal-Poor)}\\
-6 < [\mathrm{Fe}/\mathrm{H}] < -5 & \text{HMP (Hyper Metal-Poor)}\\
[\mathrm{Fe}/\mathrm{H}] < -6 & \text{MMP (Mega Metal-Poor)}
\end{cases}
$$

---

