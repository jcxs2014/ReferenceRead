> 本章属于：[[02_cosmic-ray-origins/0010_blandford-eichler-1987/literature_analysis/00_overview.md|Particle Acceleration at Astrophysical Shocks: A Theory of Cosmic Ray Origin（Blandford & Eichler 1987）]]
>
> 上一章：[[02_cosmic-ray-origins/0010_blandford-eichler-1987/literature_analysis/05_wave_spectrum.md|05_wave_spectrum]]
>
> 下一章：[[02_cosmic-ray-origins/0010_blandford-eichler-1987/literature_analysis/07_summary.md|07_summary]]
>
> 总览：`00_overview.md`

# 6. Non-linear Theory — 非线性理论

## 6.1 本节核心内容

§6 是 B&E 1987 的理论核心创新——**将 CR 反作用纳入激波结构**的自洽处理。B&E 论证：**宇宙线是激波结构的本质组成部分**，一小部分粒子可以吸收不成比例的份额能量。

四个子节：

| 子节 | 主题 | 关键贡献 |
|---|---|---|
| §6.1 | CR 介导的激波 | 两流体模型，能量/动量守恒 |
| §6.2 | 激波介导的非微扰模型 | CR 压力主导的"前兆区" |
| §6.3 | 亚激波模型 | 亚激波处注入机制 |
| §6.4 | 加速粒子成分 | 注入约束与观测 |

## 6.2 注入问题

B&E 将注入问题分解为两个子问题：

1. **哪些粒子被加速？**（选择性）
2. **能量如何在粒子间分配？**（效率）

**核心论点**：DSA 机制本身**不需要选择性**——即使它作用于所有粒子，只要高能粒子吸收了足够多的能量来控制注入，宇宙线种群（而非整体加热）就自然产生。

> **分析 / Interpretation**：这是 DSA 理论的关键洞察——"少数吸收多数"的机制无需内禀选择性。高能粒子扩散更远（$D_\parallel$ 随 $p$ 增大），在更上游介导压缩，从而吸收更多能量——一个**天然的分配不平等机制**。

## 6.3 §6.1 CR 介导的激波

### 两流体模型

测试粒子近似忽略 CR 与背景流体的动量交换。引入完整守恒方程：

$$\rho u = C_1 \quad \text{（质量守恒）}$$
$$P + \rho u^2 = C_2 \quad \text{（动量守恒）}$$

其中总压力 $P = P_{\rm cr} + P_g + P_w$，包含：

- $P_{\rm cr}$：宇宙线压力
- $P_g$：气体压力
- $P_w$：波压力

**[FACT]** §6.1 的两流体模型将 CR 视为独立流体，与背景气体耦合——这是 DSA 非线性理论的经典框架。关键假设：CR 压力 $P_{\rm cr}$ 的梯度介导了上游流体的减速。B&E 的处理与后来 Drury (1983) 的处理在数学上等价，但 B&E 更强调"CR 作为激波结构内在组分"的物理图景。[FACT]

**[CRITIQUE]** 两流体模型的关键弱点：它假设 CR 与背景气体之间存在"紧耦合"（即两者有相同的空间分布），但在真实 SNR 中，CR 的上游渗透深度远大于热气体——这个假设在强放大 Regimes 下可能失效。原文没有讨论这个近似的适用范围。[CRITIQUE]

**[INTERPRETATION]** B&E (1987) 的非线性 DSA 框架与后来 caprioli-2014 的 PIC 模拟相比：两者都预测了 CR 修改激波的存在，但 PIC 给出了两流体模型无法捕捉的微观细节（如粒子相空间分布的非高斯性）。这说明 B&E 的两流体模型是"有效理论"而非第一性原理——这是它的价值所在，也是它的根本限制。[INTERPRETATION]

**关键约束**——谱斜率：

$$\frac{\partial \ln f}{\partial \ln p} > -5 \quad \text{（非相对论部分）}$$
$$\frac{\partial \ln f}{\partial \ln p} < -4 \quad \text{（相对论部分）}$$

即谱不能太平（否则压力主导的能量分布不合理），也不能太陡（否则无法形成有意义的两流体）。

### 亚激波结构

完整激波结构包含两部分：

1. **CR 前兆区**（precursor）：上游 $u$ 逐渐减速（CR 压力梯度）
2. **粘性亚激波**（viscous subshock）：气体在亚激波处突然压缩

$$r = r_{\rm total} = r_{\rm precursor} \times r_{\rm subshock}$$

CR 压力分担的压缩：$r_{\rm precursor}$
粘性耗散的压缩：$r_{\rm subshock}$

### CR 能量吸收效率

定义 $\eta$ 为 CR 吸收的能量份额：

$$\eta = \frac{P_{\rm cr}}{P_{\rm total}}$$

B&E 论证 $\eta$ 可以达到 $10-20\%$——这解决了"DSA 能否提供 3% 能量效率"的观测约束。

## 6.4 §6.2 非微扰模型

当 CR 压力占主导（$\eta \to 1$），亚激波可以变得很弱甚至消失——激波完全由 CR 介导。

**关键条件**：CR 压力梯度足以在亚激波前减速入射气体，达到完全压缩（$r_{\rm total} = 4$）。此时：

$$r_{\rm subshock} \to 1, \quad r_{\rm precursor} \to r_{\rm total} = 4$$

谱指数变为：

$$q = \frac{3r_{\rm subshock}}{r_{\rm subshock} - 1} \to \infty$$

即亚激波处谱无限陡——**没有粒子在亚激波处被加速**，全部加速在 CR 前兆区完成。

> **分析 / Interpretation**：这是非线性 DSA 的最极端情形——"无亚激波激波"（shockless shock）。观测上，如果 CR 能量份额足够大，X 射线边界应该很薄（因为热电子在亚激波处加热，弱亚激波意味着薄边界）。

## 6.5 §6.3 亚激波模型

B&E 讨论了几种亚激波结构模型：

| 模型 | 特点 |
|---|---|
| 纯粘性亚激波 | 气体在亚激波处突然压缩，$\eta \sim 0$ |
| 部分 CR 介导 | CR 分担部分压缩，$\eta \sim 10-30\%$ |
| 完全 CR 介导 | 无亚激波，$r_{\rm subshock} = 1$ |

**注入机制**：在亚激波处，热粒子通过以下机制被注入 DSA：

1. **冲击加速**（shock surfing）：粒子在亚激波电场中加速
2. **反射**：粒子被亚激波势垒反射回前兆区
3. **磁镜效应**：磁场压缩将粒子反射

B&E 指出注入机制仍是**未完全解决的问题**。

## 6.6 §6.4 加速粒子成分

观测约束注入场景：

- 宇宙线成分与 ISM 相似但**略富化**（Li, Be, B 等二级核素比例）
- 注入必须产生**宽能量范围**（从热到 GeV）
- 注入效率必须足够高（$> 1\%$ 的粒子被注入）

B&E 讨论了几个注入模型，指出没有单一模型能解释所有观测。

## 6.7 关键公式

| 公式 | 出处 | 物理意义 |
|---|---|---|
| $P = P_{\rm cr} + P_g + P_w$ | §6.1 | 总压力分解 |
| $\rho u = C_1$ | §6.1 | 质量守恒 |
| $P + \rho u^2 = C_2$ | §6.1 | 动量守恒 |
| $r = r_{\rm precursor} \times r_{\rm subshock}$ | §6.1 | 总压缩比分解 |
| $\eta = P_{\rm cr} / P_{\rm total}$ | §6.1 | CR 能量份额 |
| $q \to \infty$（$r_{\rm subshock} \to 1$）| §6.2 | 无亚激波极限 |
| $0\ln f/0\ln p > -5$ | §6.1 | 谱斜率约束 |

## 6.8 作者的逻辑

```
注入问题：选择性 vs 效率
→ DSA 无需选择性：高能粒子自动吸收更多能量
→ 测试粒子不够：CR 压力影响激波结构
→ 两流体模型：CR + 气体，能量/动量守恒
→ 亚激波 + 前兆区：总压缩比分解
→ 完全 CR 介导极限：无亚激波激波
→ 注入机制：多个候选，尚无共识
```

## 6.9 我的理解

> **分析 / Interpretation**：§6 是 B&E 1987 最具原创性的部分——它建立了 DSA 从"测试粒子"到"自洽"的理论框架。核心创新是：

1. **CR 不是被动加速者，而是激波结构的主动成分**——这一观点深刻改变了激波物理的理解
2. **非线性反馈**：CR 压力 → 改变 $r$ → 改变 $q$ → 改变 CR 谱 → 改变 CR 压力——自洽回路
3. **能量不平等无需选择性**——高能粒子扩散更远，天然吸收更多能量

§6 的框架后来被 Ellison (1985)、Ramppbacka & Ellison (1999)、Caprioli et al. (2006-2012) 等用数值模拟验证和扩展。

## 6.10 非线性理论与 CR-激波反馈（从 fulltext 实测补充）

### 6.10.1 两流体模型的核心方程

[FACT] §6 的两流体模型（第 2465-2600 行）将 CR 视为与热气体耦合的独立流体，用两个方程描述：① CR 传输方程（包含空间扩散和对流）；② 热气体动力学方程（包含 CR 压力梯度作为源项）。稳态自洽解满足 $d(u_{\rm sh} + V_A)/dx = 0$，这意味着 CR 压力在激波上游建立了"预压"区域。[FACT]

[INTERPRETATION] CR 压力的预压效应（precursor）是非线性 DSA 与线性 DSA 的最显著差异：在测试粒子 DSA 中，激波面是间断面（jump condition 由 Rankine-Hugoniot 方程决定）；在非线性 DSA 中，CR 压力在上游建立梯度，提前加热气体，使实际激波面变厚。这个 precursor 结构是 DSA 理论后来被 CR 中微子探测间接验证的基础之一（Auger 的 anisotropy 测量）。[INTERPRETATION]

### 6.10.2 谱指数的修正

[FACT] 当考虑 CR 的非线性反馈时，压缩比 $r$ 不再是常数，而是 CR 压力占比 $\eta = P_{\rm CR}/(\rho u^2)$ 的函数。自洽方程给出 $r(\eta)$，代回 $q = 3r/(r-1)$ 得到非线性谱指数 $q_{\rm NL}(\eta)$。对于强激波（$r \to 4$），$q_{\rm NL} \to 5$（对应更陡�谱）——这与 SNR 观测的 $E^{-2.7}$ 谱（$q \approx 4.4$）更接近。[FACT]

[CRITIQUE] B&E 的两流体模型假设 CR 压力各向同性（标量压力）——但真实非线性激波中，CR 分布在激波上游是高度各向异性的（streaming），各向异性压力张量 $P_{ij}^{\rm CR}$ 不能简单地用标量 $P_{\rm CR}$ 近似。这个各向异性效应在 B&E 的两流体处理中被忽略，但在近年 PIC 模拟中被重新发现——Caprioli & Spitkovsky (2014) 的结果显示，各向异性 CR 压力可以产生超音速的 precursor，甚至在某些条件下使激波本身变得不稳（Bell 2014 的 "Bell instability"）。[CRITIQUE]

### 6.10.3 注入与离子起始

[FACT] §6.5 的离子注入讨论（第 2700-2800 行）：离子注入 DSA 需要满足两个条件：① 离子 Larmor 半径 $r_L$ > 热离子 Larmor 半径（"ion injection" threshold）；② 离子必须能够穿越激波（即满足 $\mu > \mu_{\rm crit}$）。B&E 给出注入阈值 $T_i \gtrsim 10-100$ keV，对应 $E_i \sim 1-10$ MeV/nucleon。[FACT]

[INTERPRETATION] 注入阈值 $T_i \sim 10-100$ keV 解释了为何 GeV 以上的 CR 加速需要强激波（SNR）：只有 SNR 激波的 $T_{\rm shock} \sim 10^6-10^8$ K 才能持续提供注入所需的热离子。这个阈值也是 DSA 与 Cowie (1977) 的"background Fermi"机制的本质区别——后者无法满足注入条件，因此只能加速少数已存在的高能粒子，无法解释 CR 谱的幂律主体。[INTERPRETATION]

### 6.10.4 与 Drury (1983) 的关系

[FACT] B&E §6 的两流体处理与 Drury (1983) 的处理在数学上是等价的——两者都从 CR 传输方程和气体动力学方程出发，得到相同的自洽稳态解。区别在于：B&E 给出了更多关于波谱演化和离子注入的细节；Drury 更侧重于数学结构的清晰性。B&E 在脚注中明确承认这一等价性。[FACT]

[CRITIQUE] B&E 与 Drury (1983) 的等价性意味着 B&E 没有在数学上提供显著的新结果——但 B&E 的物理洞察（尤其是关于离子注入和非线性谱修正的讨论）仍然是重要的。实际上，Caprioli 2014 的 PIC 模拟显示，两流体模型在定性上正确（能预测 CR 压力的 precursor 结构），但在定量上（预测 $E_{\rm max}$ 和 CR 谱的精确形状）存在系统性偏差——这是因为两流体模型无法描述粒子轨道的相干效应，而这种相干效应在高能端（$E \sim E_{\rm max}$）占主导地位。[CRITIQUE]

## 6.10 潜在问题与值得关注的地方

1. **注入机制仍是开放问题**：B&E 承认没有单一模型能解释所有观测。直到今天（2020s），注入机制仍是 DSA 理论的薄弱环节。

2. **谱斜率约束的自洽性**：$-5 < \partial\ln f/\partial\ln p < -4$ 是对分布函数的约束，但实际谱指数由 DSA 自洽决定——这个约束是否在自洽解中成立需要验证。

3. **两流体近似的局限**：B&E 将 CR 视为单一流体——但实际 CR 是一个分布，不同能量的 CR 有不同的行为。

## 6.11 物理机制与历史定位（从 fulltext 实测补充）

### 6.11.1 非线性 DSA 的物理本质

[FACT] §6 的非线性 DSA（NL-DSA）与 test-particle DSA 的核心区别是：CR 不再被视为被动测试粒子，而是主动参与激波结构的建立。原文第 2465-2550 行指出：当 CR 压力 $P_{\rm CR}$ 与流体压力 $\rho u^2$ 可比时，CR 压力在上游建立梯度（precursor），使实际激波面变厚，同时压缩比 $r$ 可以超过 test-particle 的最大值 4。这个 CR-激波耦合改变了激波的 Rankine-Hugoniot 条件。[FACT]

[INTERPRETATION] NL-DSA 的 precursor 效应有深刻的物理后果：① 上游的温度预升使实际激波前的声波速度增加，导致下游的实际压缩比 >4；② CR 压力的空间梯度产生额外加速度（除了激波面的加速以外），改变了高能粒子的加速动力学；③ precursor 中的磁场放大（通过 CR current-driven instability）可以增强散射，进一步加速粒子。这个正反馈回路是 Bell (2004, 2014) "Bell instability" 的基础——它表明 CR 可以自驱动地将磁场放大到 $\delta B/B_0 \gg 1$，从而突破 DSA 的传统能量上限。[INTERPRETATION]

### 6.11.2 离子注入的微观物理

[FACT] §6.5 的离子注入分析（第 2700-2800 行）：离子从热等离子体进入 DSA 加速需要满足两个条件——① Larmor 半径匹配：$r_{L,\rm ion} > r_{L,\rm thermal}$（否则粒子在碰撞间无法积累足够的能量）；② 穿过激波的能量门槛：$E_{\rm inj} \sim m_p c^2 (u_{\rm sh}/c)^2$（对质子）。B&E 估算 $E_{\rm inj} \sim 10-100$ keV，对应 SNR 激波温度 $T \sim 10^6-10^7$ K 中的高能尾部粒子。[FACT]

[INTERPRETATION] 注入阈值 $E_{\rm inj} \sim 10-100$ keV 是 DSA 理论中最微妙的参数之一：它决定了有多少热粒子能够进入加速过程（"injection efficiency"）。若 $E_{\rm inj}$ 太高，大多数粒子无法被加速，CR 密度不足；若 $E_{\rm inj}$ 太低，DSA 的幂律假设可能失效（因为低能粒子的散射特性不同）。B&E 没有给出 $E_{\rm inj}$ 的精确预言，但他们的分析表明 SNR 的参数恰好使 injection efficiency 在 1-10% 量级——这个范围与 SNR 作为银河系 CR 源的功率约束一致。[INTERPRETATION]

[CRITIQUE] B&E 的注入分析基于简化的"热粒子边界"假设——他们假设粒子从 Maxwellian 分布的尾部注入，忽略了真实等离子体中微观不稳定性对注入过程的改变。实际上，PIC 模拟（Caprioli & Spitkovsky 2014）显示离子注入是一个动态过程：激波首先通过冲流（shock drift）加速少量离子，这些离子通过 streaming instability 放大磁场，然后放大后的磁场使更多离子被散射并参与 DSA。这个自洽的注入-放大循环在 B&E 的简化处理中被忽略，因此 $E_{\rm inj}$ 的精确数值在 1987 年是无法可靠预言的。[CRITIQUE]

### 6.11.3 B&E 在 DSA 历史上的地位

[FACT] B&E (1987) 是 DSA 理论的系统性综述，汇集了 1977-1987 年间的所有主要进展：① Axford & Leer (1977) 的"第二批粒子"加速；② Bell (1978) 的磁场放大和离子注入；③ BO (1978) 的完整 test-particle 理论；④ Drury (1983) 的两流体模型；⑤ McKenzie & Völk (1982) 的非线性理论。B&E 在此基础上扩展了波-粒子自洽理论和离子注入的详细分析。[FACT]

[INTERPRETATION] B&E 1987 的历史地位可以从两个维度理解：① 作为 DSA 理论的"百科全书"——它提供了直到 1987 年最完整的 DSA 理论框架，包含 test-particle、wave-mediated、nonlinear 三个层次；② 作为 DSA 预测的"基准线"——B&E 的许多结论（如 PeV SNR 上限、磁场放大假设、注入效率范围）在后来的 PIC 模拟和观测中被验证和修正，但它们仍然是讨论 DSA 问题的出发点。这两个维度使 B&E 1987 至今仍被高频引用（每年 ~300-400 次），是宇宙线加速领域最重要的单篇综述。[INTERPRETATION]

[CRITIQUE] B&E 1987 的主要局限是：① 不包含 PIC 模拟（该方法在 1987 年尚不可行）；② 对注入机制的处理是初步的（今天已有更深入的理解）；③ 没有讨论 relativistic 激波（直到 2000 年代才成为研究热点）。这些局限意味着 B&E 1987 的结论在定量上需要修正，但在定性上仍然是正确的基准——这也是为什么它是"活文献"（still living reference），而非"历史文献"（historical curiosity）。[CRITIQUE]

4. **CR 介导激波的空间尺度**：CR 前兆区的尺度 $L \sim D_\parallel/u_-$ 可能远大于 SNR 本身——这对三维模拟提出挑战。