---
title: '§7 The p-process in very massive stars exploding as pair-creation supernovae'
paper: 03_stellar-nucleosynthesis/0018_arnould-goriely-2003/literature_analysis/00_overview.md
chapter: 7
status: completed
read_date: '2026-08-16'
---

# §7 极质量大恒星中的 p 过程：对不稳定性超新星（PCSN）

## 7.1 极质量大恒星演化速写（§7.1，p.57–59）

- **ZAMS 质量阈值**：作者把 M_ZAMS ≳ 130 M☉ 的恒星归为\"very massive stars\"（VMS），其 O 核坍缩阶段的行为不同于 §4 的 CCSN。原文 p.57："stars with M_ZAMS in the approximate range 100 ≲ M_ZAMS ≲ 250 M☉ suffer a thermonuclear explosion triggered by a copious e⁺–e⁻ pair production"。
- **对不稳定性触发机制**：核心温度达到 T ≈ 10⁹ K 时，光子自发产生 e⁺e⁻ 对，γ = 1 + … 骤降至 4/3 以下，触发绝热失稳（原文 p.58 Fig. 39）。
- **质量分档**（p.57）：MZAMS < ~100 M☉ → 脉动不稳定性后 Fe 核坍缩；100 ≲ M_ZAMS ≲ 250 M☉ → PCSN；MZAMS ≳ 250 M☉ → He 核耗尽后直接坍缩成黑洞。作者强调这些界限不确定，且自转会"enlarge the PCSN mass domain"（Ref. [156]）。
- **Pop III 关联**：作者明确排除 Z=0 恒星对 p 过程的贡献——"these Z = 0 stars are of no concern here, as they do not contain the necessary seed s- and r-nuclides for the p-process"（p.57）。因此 §7 全部讨论 Z = Z☉ 的金属量模型。
- **观测对应**：作者提及 PCSN 曾被用来解释某些超新星（Ref. [154]，暗示 SN1987A 类或极亮事件）；2003 年时尚未被 SLSN 观测（如 SN2006gy、SN2005gj）证实，这些发现出现在本文之后。

## 7.2 PCSN 中的 p 过程（§7.2，p.58–60）

- **140 M☉ 模型**：详细计算见 Ref. [158]（Heger, Woosley & Howard 2003 类）—— 一颗 Z=Z☉、损失质量的 M_ZAMS = 140 M☉ 恒星。原文 p.58："By the end of core He burning, the model star resembles a Wolf-Rayet star of spectroscopic type WNL. It is made of an oxygen core of about 50 M☉ surrounded by an extended He envelope still containing some hydrogen enriched with nitrogen."
- **引爆过程**：核心 O 燃烧期间 e⁺e⁻ 对产生触发内核对流坍缩，伴随约 4 M☉ 的 O 爆炸性燃烧，时标 ~50 秒，释放动能 4.4×10⁵¹ erg（原文 p.58）。
- **种子来源**：与 §5 SNII 类似，PCSN 的 p 过程种子来自完整 s 过程计算（§4.2 中的 ²²Ne(α,n)²⁵Mg 源），轻核（<Fe）丰度直接取自恒星演化计算（p.58）。
- **反应网络**：沿用 §5 SNII 计算的网络（~20,000 反应、~2,000 核素，Ref. [24]），p.58。
- **[FACT] 核素产量 vs 黑洞质量 M_bh**：原文 Fig. 40（p.59）展示了不同残余黑洞质量下的归一化 p 核素产量。关键结果（p.59）：
  - **轻 p 核素（<Ba）匮乏**："a marked deficiency of the p-nuclides lighter than Ba relative to the heavy ones"。
  - **机制**："trapping in the black hole remnant of the layers that are hot enough for producing significant amounts of the light p-nuclei, while not contributing to the synthesis of the heavy ones"——高温层被黑洞吞噬，只留下能生成重 p 核素的中等温层。
- **[FACT] 参数不确定度**：M_bh 对峰值温度高度敏感，而峰值温度又取决于消耗的 O 总量、O 核初始质量，进而依赖金属度、质量损失率、对流描述、对流超混合等输入（p.59）——甚至不能排除无残余的情况（M_bh = 0）。
- **作者结论**（p.60）：PCSN 是**有价值的补充位点**（尤其在 Pop III 时代或大质量 IMF 中），但其实际宇宙学贡献在 2003 年仍属推测。"Even the absence of a remnant cannot be excluded"，且 M_bh 值的敏感性意味着轻 p 核素"depletion level is quite uncertain"。
- **宇宙化学意义**：若早期宇宙（高红移、低金属度阶段）PCSN 前身星丰富，则它们可能在**低金属度 p 核素超丰**中扮演关键角色——这与 §1 提到的某些极贫金属恒星的 p 核素异常吻合。

---

## 分章索引
- 上：06_puzzling_cases.md
- 下：08_typei_production.md


---

## 7.3 关键公式补充（FACT+LaTeX，原文页码已注）

> **FACT 补充**：§7 讨论对不稳定性超新星（PCSN），涉及对产生阈值、爆炸能量与黑洞残余质量的定量关系（原文 p.57–60）。

### 7.3.1 对产生阈值（原文 p.57–58，§7.1）
- 对产生阈值能量：$2m_ec^{2}=1.022\,\mathrm{MeV}$（原文 p.57）
- 对产生率阈值：$\exp(-2m_ec^{2}/kT)\gtrsim 10^{-3}$，即 $T_9\gtrsim 2$（原文 p.58）
- 绝热指数：$\gamma\to 4/3$ 时失稳（原文 p.58 Fig. 39）

### 7.3.2 爆炸能量与残余质量（原文 p.58–59，§7.2）
- 释放动能：$E_{\mathrm{kin}}\approx 4.4\times10^{51}\,\mathrm{erg}$（$M_{\mathrm{ZAMS}}=140\,M_{\odot}$，原文 p.58）
- 对爆炸核质量：$M_{\mathrm{expl}}\approx 4\,M_{\odot}$（原文 p.58）
- 残余黑洞质量标度：$M_{\mathrm{BH}}=M_{\mathrm{core}}-M_{\mathrm{expl}}$（原文 p.59 Fig. 40）
- p 核素产量归一化：$Y_p^{\mathrm{norm}}(M_{\mathrm{BH}})=Y_p(M_{\mathrm{BH}})/\sum_A Y_p(A,M_{\mathrm{BH}})$（原文 p.59）


### 7.3.3 关键 FACT 汇总（原文 p.57–60）
- **[FACT]** $M_{\mathrm{ZAMS}}=140\,M_{\odot}$ 模型释放动能 $4.4\times10^{51}\,\mathrm{erg}$（原文 p.58），是 PCSN 位点的代表性数值。
- **[FACT]** p 核素产量归一化对残余黑洞质量 $M_{\mathrm{BH}}$ 的高度敏感性是本篇 PCSN 讨论的核心定量发现（原文 p.59 Fig. 40）。
