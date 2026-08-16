# 5. Nucleosynthesis via Thermal Pulses（§3.5 热脉冲核合成）

**上一章**: [04_tdu.md](04_tdu.md) · **下一章**: [06_nucleosynthesis_hbb_sprocess.md](06_nucleosynthesis_hbb_sprocess.md)

## 5.1 热脉冲核合成整体图景

[FACT] 壳闪在 intershell 中加热 → 部分 ⁴He 经三重 α 转 ¹²C，部分 ¹²C(α,γ)¹⁶O。典型壳闪后 intershell 组成：~70–75% ⁴He、~20–25% ¹²C、几% ¹⁶O（质量分数）。

[FACT] ¹²C、¹⁶O 的相对比例取决于 α 捕获率（¹²C(α,γ)¹⁶O 反应率），本文用 Caughlan & Fowler 1988 反应率（见参考文献 wallerstein-1997 综述）。

[FACT] 更高温度 + 密度在 TP-AGB 末段产生，因核收缩使 He 壳更薄。

## 5.2 同位素演化

### 5.2.1 碳同位素比 ¹²C/¹³C
[FACT] 3M⊙ 模型：¹²C/¹³C 从 AGB 前的 ~20 上升到 tip-of-AGB 的 **119**。

[FACT] C(N) 星观测 ¹²C/¹³C 与太阳前 SiC 微晶 (40–100) 一致。

### 5.2.2 氮同位素比 ¹⁴N/¹⁵N
[FACT] AGB 演化后 ¹⁴N/¹⁵N 显著上升，3M⊙ tip-of-AGB 时 ~2500（图 22）。

### 5.2.3 Intershell 氧丰度
[FACT] ¹⁶O 主要来自 ¹²C(α,γ)¹⁶O；¹⁷O 来自 CNO 循环残余；¹⁸O 被 H 壳燃烧强消耗。

### 5.2.4 氟 ¹⁹F
[FACT] ¹⁹F 通过 ¹⁴N(α,γ)¹⁸F(β⁺)¹⁸O(α,γ)²²Ne(α,γ)²⁶Mg(α,γ)³⁰Si…；另一支为 ¹⁴N(α,n)¹⁷F(β⁺)¹⁷O(α,γ)²¹Ne → ¹⁹F。

[FACT] 3M⊙ tip-of-AGB 时 [F/Fe] 显著上升（图 22），是银河系 ¹⁹F 主要来源之一。

### 5.2.5 其他 intershell 物种
[FACT] ²²Ne 由 ¹⁴N(α,γ)¹⁸F(β⁺)¹⁸O(α,γ)²²Ne 产生；3M⊙ tip 时 ²²Ne/Ne ≈ 0.4。

### 5.2.6 重 Mg 同位素
[FACT] ²⁵²⁶Mg 主要来自 s-过程 + HBB，3M⊙ 模型中贡献较小，M ≥ 4M⊙ 时增强。

## 关键数值表（3M⊙, Z=0.02, tip-of-AGB）

| 物种 | 值 |
|------|----|
| He/H | 0.119 |
| C/O | 1.74 |
| ¹²C/¹³C | 119 |
| ¹⁴N/¹⁵N | ~2500 |
| N/O | 0.40 |
| ²²Ne/Ne | ~0.4（初值 0.068） |
| log ε(Ne) | 8.33（MS: 8.11） |

## 5.3 热脉冲核合成方程（LaTeX）

[FACT] **三重 α 反应速率**（$\varepsilon_{3\alpha}$ 的 $T$ 依赖极强，$\propto T^{40}$ 量级；决定壳闪的 thermonuclear instability）：原文 p.34
$$ 3\,^4\mathrm{He} \;\xrightarrow{3\alpha}\; ^{12}\mathrm{C} \;+\; \gamma, \qquad \varepsilon_{3\alpha} \propto \rho^{2}\,Y^{3}\,T^{40} $$

[FACT] **He intershell 壳闪后组成**（质量分数）：原文 p.34
$$ X(^{4}\mathrm{He}) \simeq 0.70\text{--}0.75, \qquad X(^{12}\mathrm{C}) \simeq 0.20\text{--}0.25, \qquad X(^{16}\mathrm{O}) \simeq \mathrm{few}\,\% $$

[FACT] **壳闪核合成产物比例**（$^{12}$C/$^{16}$O 取决于 $\lambda_{^{12}\mathrm{C}(\alpha,\gamma)^{16}\mathrm{O}}$）：原文 p.34
$$ \frac{dX(^{16}\mathrm{O})}{dt} \;=\; \lambda_{^{12}\mathrm{C}(\alpha,\gamma)^{16}\mathrm{O}}\,n(^{12}\mathrm{C})\,n_\alpha $$

[FACT] **$^{14}$N/$^{15}$N 上升**（3M$\odot$ tip-AGB $\approx 2500$；CNO 平衡）：原文 p.36
$$ \frac{^{14}\mathrm{N}}{^{15}\mathrm{N}}\bigg|_{\mathrm{tip\,AGB}} \;\approx\; 2500 \quad (M=3M_\odot,\; Z=0.02) $$

[FACT] **²²Ne 生成链**（由 $^{14}$N 累积）：原文 p.35
$$ ^{14}\mathrm{N}(\alpha,\gamma)^{18}\mathrm{F}(\beta^+)^{18}\mathrm{O}(\alpha,\gamma)^{22}\mathrm{Ne} $$

[FACT] **²²Ne 相对丰度变化**：原文 p.35
$$ \frac{^{22}\mathrm{Ne}}{\mathrm{Ne}}\bigg|_{\mathrm{tip}} \;\approx\; 0.4 \qquad (\text{initial } 0.068,\; M=3M_\odot) $$

[FACT] **¹⁹F 生成链**：原文 p.35
$$ ^{14}\mathrm{N}(\alpha,n)^{17}\mathrm{F}(\beta^+)^{17}\mathrm{O}(\alpha,\gamma)^{21}\mathrm{Ne}(\alpha,\gamma)^{25}\mathrm{Mg}(\alpha,\gamma)^{29}\mathrm{Si}(\alpha,\gamma)^{33}\mathrm{S}\to\cdots\to\,^{19}\mathrm{F} $$

[FACT] **¹²C/¹³C 时间演化**：原文 p.35
$$ \frac{d}{dt}\!\left(\frac{^{12}\mathrm{C}}{^{13}\mathrm{C}}\right) \;=\; \frac{1}{^{13}\mathrm{C}}\frac{d\,^{12}\mathrm{C}}{dt} - \frac{^{12}\mathrm{C}}{^{13}\mathrm{C}^{2}}\frac{d\,^{13}\mathrm{C}}{dt} $$

[FACT] **He 壳厚度随核质量减小**（决定壳闪幅度）：原文 p.34
$$ \Delta M_{\rm shell} \;\propto\; \frac{1}{M_c^{3/2}} \quad \Longrightarrow \quad \text{更大 }\Delta M_{\rm shell}\text{ 导致更弱壳闪} $$
