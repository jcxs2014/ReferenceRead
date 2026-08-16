---
title: '§4 Massive stars: the pre-Type II supernova production of the p-nuclides'
paper: 03_stellar-nucleosynthesis/0018_arnould-goriely-2003/literature_analysis/00_overview.md
chapter: 4
status: completed
read_date: '2026-08-16'
---

# §4 大质量恒星：II 型超新星前的 p 核素生成

## 4.1 大质量恒星演化速写（§4.1，p.35–36）

- **质量范围**：M_ZAMS ≳ 10 M☉（作者实际写作 M ≳ 10 M☉，一般取 8–25 M☉ 为典型 SNII 前身；>25 M☉ 则剥为 Ib/Ic 型）。
- **洋葱式结构**（Fig. 23，p.35）：由内向外依次为 H 壳 → He 壳 → C 壳 → Ne 壳 → O 壳 → Si 壳 → Fe 核；每层燃烧温度递增（数十×10⁶ K 至 ~4×10⁹ K），燃烧时标骤降（原文："the duration of the successive nuclear-burning phases decreases in a dramatic way"）。
- **能量损失转变**：T > 5×10⁸ K 时中微子辐射开始主导能量损失（"see [104, Chapter 10]"），导致后续燃烧时标极短。
- **模型简化**：1D 球对称 + 无自转 + 唯象质量损失公式（Ref. [113–115]），旋转/多维效应被作者标记为"additional complexities"（p.36）。
- **超新星分类**：H 线保留 → SNII；H 壳被强星风剥离 → SNIb/Ic；本文 §5、§6 讨论 SNII，§8.2 讨论 SNIb/c。
- **能量量级**：典型 CCSN 动能 ~10⁵¹ erg；超新（hypernovae，可能为 GRB 前身）与"暗 SN"分别为偏离；作者明确 "No information is available to-date on the p-process in such objects"（p.36）。

## 4.2 p 过程的种子（§4.2，p.36–37）

- **种子来源**：He 燃烧核中 **²²Ne(α,n)²⁵Mg** 触发的 s 过程——²²Ne 来自 CNO 循环合成的 ¹⁴N 在 He 燃烧起始阶段的转化（原文 p.36）。
- **[FACT] 25 M☉ 模型种子丰度**（Fig. 24–25，p.36–37）：
  - s 核素主要在 **A > 90 区域**显著增强，与金属度 Z 关系不大。
  - 具体丰度受三个因素控制（p.37）：(i) ²²Ne(α,n) 产生的中子；(ii) He 核中初始铁峰与超铁核素（s 过程种子）；(iii) "中子毒物"（主要是 O，因 Fe/O 随金属度下降而变化）。
  - [Fe/O] = 0.42 [O/H]（p.36 Fig. 24 caption）。
  - **核物理不确定度**：带电粒子反应率（[119] vs NACRE）对 70 ≲ A ≲ 90 s 核素影响最大（Fig. 25）。
- **金属度效应**：Z = 0.1 Z☉ 时初始丰度 X(Z) = (Z/Z☉) X(Z☉)（A ≤ 30）和 X(Z) = (Z/Z☉)^1.42 X(Z☉)（A ≥ 30，含 Fe）。

## 4.3 非爆发 p 过程的讨论（§4.3，p.38–39）

- **早期假设（Ref. [1,10]）**：SNII 外层 H 富区是 p 过程最佳位点。
- **[FACT] 质疑**（Ref. [11,12]）：球对称 H 富区无法达到 T > 10⁹ K 的 (γ,n) 有效阈值——该假说被否定（非球对称喷流驱动 SNII 除外，Ref. [123]）。
- **修正位点**：转向大质量恒星**深 O-Ne 壳层**（Fig. 23）的爆发前/爆发阶段。
- **关键结论**（p.38）：
  - [122] 结论：大部分爆发前 p 核素**在爆炸中被摧毁**，因其集中于高温层。
  - [124] 结论：部分 pre-SN p 核素可存活，但存活率**强烈依赖恒星质量**。
- **多维混合的前景**（Ref. [125–127]，p.38–39）：
  - 2D 流体力学模拟显示 O 富壳层存在**由重力波驱动的额外对流混合**，产生特殊 C/O/Ne 富区。
  - [127] 一维化"流体质点"模型：Δρ/ρ = ±5% 初始密度扰动下，质点温度在 1.5–2.2×10⁹ K 附近振荡（Fig. 26）。
  - 作者结论（p.39）："Fig. 26 suggests that the p-process might have a good chance to develop in multi-dimensionally simulated pre-supernova O-rich shells"——且 pre-SN 生成的 p 核素在 2D 混合下**有更大概率存活**爆炸。

---

## 分章索引
- 上：03_nuclear_physics.md
- 下：05_snii_production.md


---

## 4.4 关键公式补充（FACT+LaTeX，原文页码已注）

> **FACT 补充**：§4 讨论大质量恒星演化与 s 过程种子的生成，涉及燃烧时标、中子产额、金属度缩放等定量关系（原文 p.35–39）。

### 4.4.1 燃烧时标与中微子损失（原文 p.35，§4.1）
- 核燃烧时标量级估计：$\tau_{\mathrm{burn}}\sim\dfrac{X\,Q\,m_H}{\rho\,\varepsilon_{\mathrm{nuc}}}$（原文 p.35–36）
- 中微子能量损失率：$\varepsilon_{\nu}\approx 5.7\times10^{11}\,\rho\,T_9^{9}\;\mathrm{erg\,cm^{-3}\,s^{-1}}$（Pair 过程主导，原文 p.35，原文 p.36 提到 $T>5\times10^{8}$ K 后中微子主导）
- 恒星寿命与质光比：$\tau_{\mathrm{MS}}\propto M/L\propto M^{-2.5}$（原文 p.35）

### 4.4.2 s 过程种子生成（原文 p.36，§4.2）
- 中子源反应率：$\dot{n}\propto X(^{22}\mathrm{Ne})\,\rho\,X(\alpha)\,\langle\sigma v\rangle_{^{22}\mathrm{Ne}(\alpha,n)}$（原文 p.36）
- 中子通量：$N_n=\dot{n}/\alpha$，$\alpha$ 为总中子俘获率（原文 p.36）
- 中子密度阈值：$n_n\gtrsim 10^{7}\text{–}10^{8}\,\mathrm{cm^{-3}}$ 用于驱动 s 过程（原文 p.36）

### 4.4.3 金属度缩放（原文 p.36–37，§4.2）
- 轻元素（$A\le 30$）金属度缩放：$X_Z(Z)=(Z/Z_{\odot})\,X_Z(Z_{\odot})$（原文 p.36 Fig. 24 caption）
- 重元素（$A\ge 30$，含 Fe）：$X_Z(Z)=(Z/Z_{\odot})^{1.42}\,X_Z(Z_{\odot})$（原文 p.36）
- 富金属度下 [Fe/O] 关系：$\mathrm{[Fe/O]}=0.42\,\mathrm{[O/H]}$（原文 p.36 Fig. 24）

### 4.4.4 非爆发 p 过程温度窗（原文 p.38，§4.3）
- 有效温度条件：$T\gtrsim 10^{9}\,\mathrm{K}$ 为光致分解显著阈值（原文 p.38）
- 流体质点温度振荡：$\Delta T/T\sim 0.2\text{–}0.3$，振荡中心 $T\approx 1.5\text{–}2.2\times10^{9}\,\mathrm{K}$（原文 p.38–39 Fig. 26）


### 4.4.5 关键 FACT 汇总（原文 p.35–39）
- **[FACT]** 中微子损失率 $\varepsilon_{\nu}\propto \rho\,T_9^{9}$ 解释了为何 $T>5\times10^{8}$ K 后燃烧时标骤降（原文 p.35）。
- **[FACT]** 金属度缩放指数 1.42（A≥30）解释了为何低金属度下 p 过程种子严重不足（原文 p.36）。
- **[FACT]** 非爆发位点 $T\gtrsim 10^{9}$ K 的有效温度条件是判断"是否能发生 p 过程"的定量门槛（原文 p.38）。
