# 3. STELLAR REACTION RATES FROM LABORATORY CROSS SECTIONS (Sec. III)

> 本章属于：**William A. Fowler (1984), *Experimental and theoretical nuclear astrophysics: the quest for the origin of the elements*, Rev. Mod. Phys. 56, 149–172**
>
> 上一章：[[03_stellar-nucleosynthesis/0003_fowler-1984/literature_analysis/02_early_research.md|02_early_research.md]]
>
> 下一章：[[03_stellar-nucleosynthesis/0003_fowler-1984/literature_analysis/04_hydrogen_burning.md|04_hydrogen_burning.md]]

## 3.1 本节核心内容

[FACT] 本节约 3 页，集中讨论**如何将实验室测量的核反应截面 σ 转换为恒星内部的天体物理反应速率**——这是实验核天体物理的**核心方法论**，也是 Fowler/Caughlan/Zimmerman (FCZ) 的贡献所在。

## 3.2 反应速率的定义

[FACT] 恒星中热核反应速率（per reaction type）通常表达为：

**N_A ⟨σu⟩** — reactions per sec per (mol·cm⁻³)

其中：
- **N_A = 6.022×$10^{23}$ mol⁻¹**（Avogadro 常数）
- **⟨σu⟩**：Maxwell-Boltzmann 平均，为 σ(u)·u 的函数
- σ 单位 cm²，u 单位 cm s⁻¹
- 乘以两种反应物的数密度乘积得到 reactions per sec per cm³

[FACT] N_A 的引入是为了能用**质量分数**（mass fractions）进行计算，详见 Fowler, Caughlan, Zimmerman (1967, 1975; Harris et al. 1983; Caughlan 1984)。

[FACT] FCZ (1967/1975) 给出了对**含超过两个反应物**的速率程序，以及针对 γ, e, n, p, α 与 A≲30 核的**解析表达式**。

[FACT] 文中明确指出：γ 使用了 **Bose-Einstein 统计**；但**简并态电子、中子、质子**的 Fermi-Dirac 统计推广与 **α 的 Bose-Einstein 统计推广未纳入**。

[FACT] 给出了**逆反应速率**（reverse rates）的计算因子。

## 3.3 S 因子——天体物理 S 因子（Table I）

### 3.3.1 中子反应

[FACT] 对**中子诱导反应**，定义 **S 因子 = σ × u**，以消除截面在低速时的 **u⁻¹ 奇点**。

### 3.3.2 带电粒子反应——核心公式（Table I）

对 p、α 或 ¹²C, ¹⁶O 等带电粒子反应，截面需考虑**从实验室最低能到天文相关能量**的 10 多个数量级的下降。方法由 **E. E. Salpeter (1952b, 1955)** 首倡，**Bethe (1967)** 强调。

**Table I 的核心公式：**

```
σ(E) = π · g · λ² · P(E) · (INTRINSIC NUCLEAR FACTOR)
S(E) = $E_{0}$(E) · exp( +E_b/E^(1/2) )
```

其中：
- **λ = ħ/(2μE)^{1/2}**：de Broglie 波长（约化质量 μ）
- **P(E) = exp(−2πη)**：**Gamow 穿透因子**（Gamow penetration factor），控制对库仑势垒的隧穿
- **η = π $Z_{0}$$Z_{1}$ e² / (ħv)**：Sommerfeld 参数
- **g = 2J+1 / (2$j_{0}$+1)(2$j_{1}$+1)**：自旋统计因子
- **S(E)**：天体物理 S 因子，缓慢变化，可外推

[FACT] 单位：σ 通常用 **barn ($10^{-24}$ cm²)**，能量用 **MeV (1.602×$10^{-6}$ erg)**，S 因子单位为 **MeV·b**（有时也用 keV·b）。

[FACT] 表 I 中标记 **$Z_{0}$, $Z_{1}$** 为两反应核的电荷数，**A** 为约化质量（原子质量单位）。

[FACT] **关键洞察**：S 因子缓慢变化，从而允许从实验室最低能测量**外推到极低的有效恒星能量**。但**内在核因子**本身的不确定性只能由实验室实验消除。

### 3.3.3 外推的不确定性

[FACT] 外推的主要不确定性来自 S(E) 随能量的变化——这**主要取决于**在形成复合核时选取的**半径**。这些半径值见 Woosley, Fowler, Holmes, Zimmerman (1978)。

[FACT] 文中特别指出：Gamow 穿透因子的消除基于**库仑波函数的 Schrödinger 方程求解**——这是高置信度的。

[FACT] 复合核共振恰好位于反应阈值之下或之上的情况，可通过研究**该共振参与的其他反应**（那些更容易研究的反应）来确定其性质。

## 3.4 Table II — 恒星反应速率函数

**Table II 给出的两个速率公式：**

**非共振（Nonresonant）速率：**
```
⟨σu⟩_nr ∝ T_9^(-2/3) · exp(-3E_0/kT)
```
积分形式：∫ S(E) exp(−E/$E_{0}$) exp(−E/kT) dE

**共振（Resonant）速率：**
```
⟨σu⟩_r ∝ T_9^(-1/2) · exp(-E_r/kT)
```
其中 **E_r** 是共振能量。

[FACT] **有效恒星反应能量 $E_{0}$：**
```
$E_{0}$ = 0.122 · ($Z_{0}$ $Z_{1}$ A)^(1/3) · T_9^(2/3)  MeV
```
其中 **$T_{9}$** 是以 $10^{9}$ K 为单位的温度。

[FACT] **Gamow 峰**：被积函数在 **E ≈ $E_{0}$** 处出现极大——即非共振反应的有效能量。

[FACT] 理论统计模型计算得到的反应速率表达式见 Woosley, Fowler, Holmes, Zimmerman (1978)。

## 3.5 反应符号约定

[FACT] Fowler 强调反应符号的实验室约定：¹²C(α,γ)¹⁶O 中，¹²C 是**靶**、α 是**入射束**、γ 是被检测粒子、¹⁶O 是**剩余核**。

[FACT] 若反过来（¹²C 轰击 ⁴He 气体靶，测 ¹⁶O 不测 γ），则实验符号为 ⁴He(¹²C,¹⁶O)γ。**恒星不在乎这个——恒星中所有粒子都在运动，只有质心系才有意义。**

[FACT] ¹²C(α,n)¹⁶O(e⁺+ν)¹⁵N：n 是即时产生并检测的中子，e⁺ 是 ¹⁶O β⁺ 衰变的正电子，ν 是同时发射的中微子。

[FACT] Fowler 自豪回忆 1955 年 1 月 26 日在瑞典皇家科学院作 "Nuclear Reactions in Stars" 报告——"有些你们在座的人听过那次报告"（呼应 30 年后再次登台）。

## 3.6 作者的逻辑链

实验测截面 → 用 S 因子剥离 Gamow 穿透因子的快速变化 → 在有效恒星能量 $E_{0}$ 处做 Maxwell-Boltzmann 平均 → 非共振 vs 共振两类速率公式 → 外推的可靠性依赖 S(E) 的缓慢变化与复合核半径选择。

## 3.7 关键公式汇总

| 量 | 公式 |
|----|------|
| 反应速率 | N_A ⟨σu⟩ (per mol·cm³·s) |
| σ(E) | πg λ² P(E) × [intrinsic] |
| S(E) | $E_{0}$(E) exp(+E_b/E^(1/2)) |
| $E_{0}$ | 0.122 ($Z_{0}$$Z_{1}$A)^(1/3) $T_{9}$^(2/3) MeV |
| ⟨σu⟩_nr | ∝ $T_{9}$^(−2/3) exp(−3$E_{0}$/kT) |
| ⟨σu⟩_r | ∝ $T_{9}$^(−1/2) exp(−E_r/kT) |

## 3.8 潜在问题与关注点

[CRITIQUE] 该节的方法论基础（S 因子外推）是**整个实验核天体物理的支柱**——后文多处（¹²C(α,γ)¹⁶O、¹²C+¹²C、¹⁶O+¹⁶O）都要回到这个框架讨论外推的不确定性。

[CRITIQUE] 文中承认对**简并电子/质子/中子的 Fermi-Dirac 统计**推广尚未完成——这在核心坍缩与中子星形成场景下会引入重要修正。

[CRITIQUE] 现代实验核天体物理已通过**深地实验室**（如意大利 LUNA 隧道，2000 年至今）把 ¹²C(α,γ)¹⁶O 的测量能推到 Fowler 1984 年无法触及的 300 keV 以下，部分验证/修正了当时 Fig. 6 的两种外推。