> 本章属于：Virginia Trimble, "The origin and abundances of the chemical elements," Rev. Mod. Phys. 47 (1975) 877.
>
> 下一章：[[03_stellar-nucleosynthesis/0002_trimble-1975/literature_analysis/08_conclusions.md|08_conclusions.md]]
>
> 下一章（跨章节图/表）：`09_figures_and_tables.md`

# 7. The Evolution of Galaxies (Chemical Evolution Models)

## 7.1 本节核心内容

§IV 是本文的理论应用高潮：将 §III 中核合成的产量，通过初始质量函数（IMF）与恒星形成率的耦合，输入到银河/星系演化的封闭箱（closed-box）与开放箱（open-box）模型中，检验能否复现观测到的金属丰度-形态关系、金属丰度梯度、颜色-光度分布等。

## 7.2 A. Observations of Galaxies

### 7.2.1 关键观测约束

[FACT] §IV A 列举了化学演化模型必须同时满足的多项观测约束：
1. **形态分类与光度函数**：Hubble 序列（E/S0/Sa-Sd/Irr）中各类星系的相对数目与光度函数；
2. **颜色分布**：U-B、B-V 沿 Hubble 序列的系统变化；
3. **质量-光度比 (M/L)**：从 E 型到 Sc 型的 ~10× 变化；
4. **气体质量与气体分数**：椭圆星系几乎无气体（μ = M_gas/(M_gas + M_stars) ≪ 0.1），旋涡星系内 0.1–0.5；
5. **恒星形成率 (SFR)**：银河系当前 SFR ~ 3–5 M_☉/yr；
6. **超新星率 (SNR)**：银河系 ~15–60 年/SN，Type I 与 Type II 大致均分。

### 7.2.2 Supernova rate

[FACT] 银河系超新星总率：~15–60 yr/SN（1974 年 Tammann 估计），历史观测近 1000 年记录到的 ~4 例 SN 分布在 4.5 kpc 内，外推至全银河系约 23 yr/SN。

[FACT] 作者强调 Tammann (1974) 给出的 SN 率是下界（未修正不完备性）。

[FACT] SNR 形成间隔：25–75 yr (Ilovaisky & Lequeux 1972)；脉冲星形成率：~30 yr (Ostriker & Gunn 1970) 或 100–200 yr。

### 7.2.3 SN progenitor masses

[FACT] 传统对应：Type I SN ← 低质量恒星（如双白矮星、WD 吸积）；Type II SN ← 大质量恒星（M ≳ 4–8 M_☉）。

[FACT] 但 Tammann (1974) 列出至少 10 项困难，质疑 Type I 的低质量前身星模型，因此有提议所有 SN 都源自大质量年轻恒星。

## 7.3 B. Homogeneous, One-Zone Models with Constant IMF

### 7.3.1 封闭箱模型（Closed-box / Simple model）

[FACT] 这是 §IV 的核心。在以下假设下：
- 体积封闭（无 inflow、无 outflow）；
- 星际介质完美混合；
- 恒星形成率 dS/dt ∝ μⁿ（μ 为气体质量分数）；
- "即时回收"近似（instant recycling approximation）：大质量恒星产生后立即返回气体；
- IMF 恒定（Salpeter, α = 2.35）。

可得两个关键微分方程：

**气体分数演化**：
$$\frac{d\mu}{dt} = -(1-b)\frac{dS}{dt} = -(1-b)\, A\, \mu^n$$

其中 b 是 "回收分数"（fraction of matter returning to ISM per generation），对 Salpeter IMF：b ≈ 0.12–0.25。

**金属丰度演化**：
$$\frac{d(\mu Z)}{dt} = -Z\,\frac{d\mu}{dt} + y\,\frac{d\mu}{dt} \cdot (1 - Z)$$

即：第一项是恒星形成锁走金属；第二项是大质量恒星返回的净金属产量（产量 y 减去被恒星本身带走的 Z）。

**解析解**：
$$\boxed{Z = y \ln(1/\mu)}$$

这是化学演化理论最经典的公式之一，被称为 "simple model" 或 "closed-box" 关系。

### 7.3.2 关键参数与数值

| 参数 | 数值 |
|------|------|
| b（回收分数）| 0.12–0.25（Salpeter IMF）|
| y（净产量）| 0.003–0.013 |
| μ 观测范围 | 0.005–0.5 |
| Z 变化范围 | 0.7 y – 5.3 y（即 ~2.5× 变化）|
| α (Salpeter IMF)| 2.35 |
| n（SFR 依赖气体密度的幂次）| 1–2（Schmidt 1963）|
| SN 率 | 15–60 yr/银河系 |

### 7.3.3 关键结果

[FACT] 作者强调 simple model 的成功之处：
- **Z–μ 反相关**：Z 高的地方 μ 低（即消耗气体多的地方金属丰度高）——与观测一致；
- **Z 的相对均匀性**：μ 在 0.005–0.5 范围内变化时 Z 只变化 ~2.5 倍——解释了为何各类形态星系金属丰度相对接近；
- **时间无关**：这些结果不依赖 dS/dt 的具体时间依赖；
- **Z(t) 演化**：n = 1 时 Z ∝ t（线性增长）；n = 2 时 Z 增长更快但在 μ 小时饱和。

[FACT] 数值实现（Talbot & Arnett 1971; Fowler 1972; Searle et al. 1973; Tinsley 1968 及 NATO 1974）可复现：
- U-B、B-V 沿 Hubble 序列的变化；
- M/L 沿 Hubble 序列的变化；
- μ 与颜色的关系；
- 星系光谱能量分布。

### 7.3.4 已知失败

[FACT] simple model 的失败：
- 无法自然解释 α 元素（O、Mg、Si、Ca）与 Fe 的相对丰度比（α/Fe）在不同 [Fe/H] 处的变化——因为 α 主要来自 II 型 SN（快通道，t ~ Myr），Fe 主要来自 Ia 型 SN（慢通道，t ~ Gyr）。需要双通道模型。

## 7.4 C. Models with Variable IMF

[FACT] 允许 α 随金属丰度或时间变化的 IMF 可以调节产量。1975 年的提议包括：
- 富金属环境 IMF 更"平坦"（产生相对更多大质量恒星）；
- 贫金属环境 IMF 更"陡"。

[FACT] 作者对此态度谨慎，认为 IMF 变化缺乏独立观测证据。

## 7.5 D. Models with Infall or Inhomogeneity

[FACT] 开放箱模型引入气体 inflow 或 outflow：
- **infall 模型**（Lynden-Bell & Pringle 1974）：星系由外部气体在指数时标上落入形成。可解释为什么最贫金属恒星（[Fe/H] < −3）依然存在于银河晕中——这些恒星形成于原始气体尚未被富集之前。
- **inflow 时间尺度**：~$t_{0}$ = 5 × $10^{9}$ yr（量级）可复现银河系金属丰度梯度。
- **inhomogeneity 模型**：允许星系内部存在空间上不均匀的恒星形成（如内盘快、外盘慢），可自然产生金属丰度梯度 d[Fe/H]/dR ≈ −0.05–0.1 dex/kpc。

[FACT] 计算机模型（Tinsley 1974）表明：过去某一时期 ISM 金属丰度可能一度高于当前值，随后被低金属丰度的 halo 恒星释放的气体稀释——这一机制可解释"超金属"恒星的残余。

## 7.6 E. Dynamical Models of Galactic Evolution

### 7.6.1 Spherical galaxies (E/S0)
[FACT] 椭圆星系建模主要用球对称流体动力学 + 恒星形成 + 反馈。关键约束：几乎无气体、红色、低 M/L、缺乏 SN Ia。

### 7.6.2 Disk galaxies
[FACT] 旋涡星系使用轴对称盘模型，需要考虑角动量守恒、盘稳定性、旋臂密度波（Lin & Shu）对恒星形成的调制。

### 7.6.3 Models with massive halos
[FACT] 旋转曲线观测提示银河系存在大质量暗晕（M_halo/M_visible ~ 10–100），对化学演化没有直接影响，但影响星系形成动力学。

## 7.7 关键公式汇总

$$\xi(M) = \xi_0 M^{-\alpha}, \quad \alpha = 2.35 \ \text{(Salpeter)}$$
$$\frac{d\mu}{dt} = -(1-b)\, A\, \mu^n, \quad b \approx 0.12\text{–}0.25$$
$$\frac{d(\mu Z)}{dt} = -Z\frac{d\mu}{dt} + y(1-Z)\left(-\frac{d\mu}{dt}\right)$$
$$\boxed{Z = y \ln(1/\mu), \quad y \approx 0.003\text{–}0.013}$$
$$\text{SN rate: } 1\ /\ 15\text{–}60 \ \text{yr (银河系)}$$

## 7.8 [INTERPRETATION]

[INTERPRETATION] §IV 是全文的"闭环"：§I–§III 分别解决了丰度基准、恒星产量问题，§IV 把它们组装成一个动态的、可计算的银河演化模型。simple model 的解析解 Z = y ln(1/μ) 在 1975 年就是一个理论-观测的双重胜利——它以极少的参数复现了大量观测事实。

[INTERPRETATION] 作者反复引用 Tinsley 的工作，是因为 Tinsley 是 1970 年代化学演化数值模拟的奠基者。本文在某种意义上是 Tinsley 数值模型的理论总结与物理诠释。

## 7.9 [CRITIQUE]

[CRITIQUE] "即时回收"近似在 α 元素 vs Fe 的相对丰度问题上失败，因为这两种元素的产生时标相差 ~$10^{6}$ 倍。这一困难直到 1980s 才通过 "delayed SN Ia channel" 模型被解决（Thomson 1981, Tinsley 1979）。

[CRITIQUE] IMF 恒定假设在今天的观测下已被挑战：低金属丰度环境、矮星系、球状星团的 IMF 可能显著不同于银河系附近值。

[CRITIQUE] §IV 未充分讨论 outflow（超新星驱动风）对化学演化的影响——这是 1990s 后矮星系化学演化研究的核心。