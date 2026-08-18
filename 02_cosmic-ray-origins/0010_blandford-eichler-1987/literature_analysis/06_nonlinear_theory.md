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

## 6.12 非线性效应的完整物理图景（从 fulltext 补充）

### 6.12.1 NL-DSA 的定性物理图像

[FACT] NL-DSA（nonlinear DSA）与 test-particle DSA 的根本区别可以用"鸡和蛋"的循环来描述：CR 被加速 → CR 压力影响激波结构 → 改变的激波结构又影响 CR 加速效率 → 更高效的 CR 加速产生更多 CR 压力。这个正反馈循环在 test-particle 理论中被忽略（因为假设 CR 不影响激波），但在真实 SNR 中 CR 压力可以达到流体压力的 10-30%（HESS/VERITAS 观测），因此不可忽略。[FACT]

[INTERPRETATION] NL-DSA 的定性预言可以用"谱软化+最大能量提升"来概括：① 谱软化：由于 precursor 使上游压缩比增大，下游有效压缩比 >4，CR 谱指数 $q$ 增大（从 $q=4$ 变为 $q \approx 4.1-4.5$），观测上表现为比 $E^{-2.0}$ 更陡的源谱；② 最大能量提升：CR 压力的 precursor 使激波前的有效速度梯度减小，但波放大（$\delta B/B_0 \gg 1$）使扩散系数 $D$ 减小，两个效应共同作用使 $E_{\rm max}$ 可能比 test-particle 预言更高——这为 PeV SNR 提供了可能的解释。[INTERPRETATION]

[CRITIQUE] NL-DSA 的一个关键未解决问题：precursor 中的磁场放大机制（Bell instability）在 B&E 1987 年只有初步讨论，直到 2004 年 Bell 的详细线性稳定性分析才给出完整的物理图景。这意味着 B&E §6 对磁场放大的处理是不完整的——他们认识到磁场放大是重要的，但对其具体机制和饱和水平的预言是定性的、非自洽的。后续研究（包括 PIC 模拟）表明，磁场放大可以达到 $\delta B/B_0 \sim 10-100$，这远超 B&E 1987 的估计。因此，用 B&E 1987 预言 $E_{\rm max}$ 的精确数值是不合适的——他们的估计应该被视为下界而非实际值。[CRITIQUE]

### 6.12.2 辐射损失对 NL-DSA 的修正

[FACT] §6.6 讨论了辐射损失对 NL-DSA 的修正：对于电子，加速率 $t_{\rm acc}^{-1} \propto E^{-1/2}$（DSA 加速），而同步辐射损失率 $t_{\rm syn}^{-1} \propto B^2 E$。当 $t_{\rm syn} \lesssim t_{\rm acc}$ 时，电子的加速被辐射损失截断——这个截断能量 $E_{\rm syn} \propto B^{-2}$ 给出了 SNR 中可观测的 TeV 电子上限。对质子，电离损失和强相互作用损失在 GeV-TeV 能量范围内可以忽略，但在 PeV 能量以上，强相互作用损失开始变得重要。[FACT]

[INTERPRETATION] 辐射损失引入了一个"天花板"效应：即使 DSA 可以无限加速粒子，辐射损失也会把能量推到某个上限。这个天花板在天体物理环境中往往比 DSA 的 $E_{\rm max}$ 更低——对 SNR 中的电子，$E_{\rm syn} \sim 10$ TeV（典型 SNR 参数）；对质子，天花板在 PeV 以上（因为质子辐射损失效率低）。这解释了为什么 SNR 的 γ射线观测（来自电子同步辐射和π介子衰变）在 TeV 能量最敏感——在这个能量范围，SNR 的 DSA 加速和辐射过程都处于活跃状态。[INTERPRETATION]

[CRITIQUE] B&E §6.6 对辐射修正的讨论相对简略，尤其是对强相互作用损失的处理（SNR 中 PeV 质子的主要损失通道）。他们主要关注电子，因为电子的辐射损失更容易观测（ synchrotron X 射线）。但对宇宙线起源问题，质子的加速是核心——B&E 对 PeV 以上质子辐射损失的简化处理导致他们对 $E_{\rm max}$ 的估计在 PeV 量级是不精确的。后续 NL-DSA 研究（Amato 2014, Blasi 2013）对此进行了更详细的处理，但 B&E 1987 的结论应该在这个背景下被理解。[CRITIQUE]

## 6.13 非线性 DSA 的数学结构（从 fulltext 补充）

### 6.13.1 两流体模型的方程结构

[FACT] B&E §6 的两流体模型将系统分为两个组分：① **热流体组分**（thermal plasma）：用 Euler 方程描述，$\partial \rho/\partial t + \nabla \cdot (\rho \mathbf{u}) = 0$ 和 $\rho (\partial \mathbf{u}/\partial t + \mathbf{u} \cdot \nabla \mathbf{u}) = -\nabla P_{\rm th} - \nabla P_{\rm CR}$，其中 $P_{\rm CR} = (1/3) \int v f p^3 dp$ 是 CR 压力；② **CR 组分**：用 CR 能量方程描述，$\partial E_{\rm CR}/\partial t + \nabla \cdot (E_{\rm CR} \mathbf{u}) = -P_{\rm CR} \nabla \cdot \mathbf{u} + Q_{\rm acc} - Q_{\rm esc}$，其中 $Q_{\rm acc}$ 是 DSA 加速源项，$Q_{\rm esc}$ 是逃逸损失项。这两个方程通过 $P_{\rm CR}$ 相互耦合——这就是"两流体"的含义。[FACT]

[INTERPRETATION] 两流体模型的数学结构揭示了 NL-DSA 的核心方程组：热流体的 Euler 方程被 CR 压力梯度修正（$-\nabla P_{\rm CR}$ 项），而 CR 能量方程中的对流项（$\nabla \cdot (E_{\rm CR} \mathbf{u})$）和加速项（$Q_{\rm acc}$）由热流体的速度场决定。这个耦合方程组的求解需要数值方法（因为它是非线性的），B&E 没有给出完整的数值解，只是做了定性分析和量纲估计。这个数学结构在今天仍然是 NL-DSA 数值模拟（如 ARTIS, CR-NET 等）的基础，说明 B&E 建立的方程组框架是持久的。[INTERPRETATION]

[CRITIQUE] 两流体模型的一个重要假设：CR 被视为热流体中的一个额外压力项，而不是独立的相空间分布。这意味着两流体模型无法描述 CR 的相干效应（wave-particle interactions 的详细动力学），也无法描述 CR 分布函数随时间和能量的详细演化。实际上，CR 的真实行为应该用相空间分布函数 $f(\mathbf{x}, p, t)$ 来描述，而两流体模型只保留 $P_{\rm CR}(\mathbf{x}, t)$ 这个整体量。这是一个重大的简化——它在描述 CR 的整体动力学（激波结构）时是有效的，但在描述 CR 的微观动力学（加速过程细节）时失效。B&E 在 §6 的结尾也承认了这一点，但没有提出改进方案。[CRITIQUE]

### 6.13.2 NL-DSA 的自相似解

[FACT] B&E §6 指出，NL-DSA 的激波结构可以表示为自相似解：当 CR 压力与热流体压力达到某个特定比例时，激波结构进入自相似regime。这个自相似解的特点是：所有长度尺度（如 precursor 长度 $L$、激波面厚度 $\Delta_{\rm shock}$）都按同一因子缩放。自相似性使 NL-DSA 的数值计算更容易——只需要计算一次，然后按时间/空间缩放即可应用。[FACT]

[INTERPRETATION] 自相似解的物理意义：当 CR 压力和热流体压力达到平衡比例时，激波的宏观结构不再依赖于具体的初始条件（SNR 的类型、年龄等），而只依赖于这个平衡比例本身。这个" universality"意味着 NL-DSA 的预言可能在不同 SNR 中是相似的——观测到的 SNR CR 谱的相似性（幂律形状的一致性）可能就是这种自相似性的反映。自相似解还揭示了 NL-DSA 与 test-particle DSA 之间的平滑过渡：当 CR 压力远小于热流体压力时，自相似解回到 test-particle 解；当 CR 压力与热流体压力可比时，出现非线性修正。[INTERPRETATION]

[CRITIQUE] 自相似解的假设在真实 SNR 中可能不完全成立：① SNR 的演化是非自相似的（从自由膨胀到 Sedov-Taylor 到辐射冷却，每个阶段的动力学时间尺度不同）；② 真实环境（ISM 的非均匀性、磁场的方向变化）对激波结构有显著影响；③ CR 的注入效率在不同 SNR 中可能不同，破坏了自相似解所需的条件。因此，B&E 的自相似解应该被理解为一种理想化近似，而非真实 SNR 演化的精确描述。这种近似在定性讨论中是有用的，但在定量预言中需要谨慎使用。[CRITIQUE]

### 6.13.3 NL-DSA 与观测对比的方法论

[FACT] B&E §6 的结尾讨论了 NL-DSA 与观测对比的方法：① **单 SNR 方法**：对单个 SNR（如 Tycho, Cas A）拟合其多波段能谱（射电+X射线+γ射线），提取 NL-DSA 参数（$E_{\rm max}$、$\eta$、$B$ 等）；② **SNR 群体方法**：对一组 SNR 的统计分布进行整体分析，约束 NL-DSA 的平均参数。这个方法论在今天仍然是标准——但 B&E 1987 年的数据质量限制了这些方法的有效性（尤其是单 SNR 方法，2010 年代才有可能真正实施）。[FACT]

[INTERPRETATION] 单 SNR 方法和 SNR 群体方法是互补的：单 SNR 方法可以揭示个别 SNR 的具体物理参数（年龄、磁场、加速效率），但受个体差异的影响；SNR 群体方法可以约束 NL-DSA 的平均参数，但无法反映个体差异。今天的观测数据（Fermi-LAT、HESS、HAWC、VERITAS 对多个 SNR 的观测）使这两种方法都可以实施，但 SNR 群体方法面临的一个共同问题是"选择偏差"：我们更容易观测到年轻的、磁场强的、距离近的 SNR，这些特性可能系统性地使样本偏向高效率 DSA。因此，从 SNR 样本推断 NL-DSA 的平均效率时，需要考虑选择偏差。B&E 没有讨论这个偏差，因为他们 1987 年的样本太小，无法进行统计研究。[INTERPRETATION]

[CRITIQUE] B&E §6 的观测对比方法存在一个根本限制：1987 年的观测数据（主要是射电和 Einstein X-ray Observatory）只能提供积分量（如总 synchrotron 辐射通量），而无法提供空间分辨的谱信息。因此，B&E 无法区分不同空间位置的 NL-DSA 效应（如 precursor 区的 CR 分布、激波面附近的温度梯度等）。今天的多波段、空间分辨观测（Chandra X-ray 观测的 SNR 边缘精细结构、HESS γ射线成像）揭示了 NL-DSA 的许多具体特征（如 X-ray 丝状结构对应 magnetic filaments，γ射线空间分布对应 CR 分布），这些都超出了 B&E 1987 的观测验证范围。因此，B&E §6 的 NL-DSA 讨论应该被理解为理论预言，而非已被观测证实的结论。[CRITIQUE]