# 4. 不可约宇宙线 mCP 通量与 Fig. 2

> 本章属于：Cavendish Tests of Millicharged Particles
>
> 上一章：`03_accumulator_design.md`
>
> 下一章：`05_references_and_further_reading.md`

## 4.1 本节核心内容

本章计算**宇宙线空气簇射衰变产生的不可约 mCP 通量** $n_\chi \sim 10^{-5}$ cm⁻³ $(q_\chi/10^{-4})^2$（$m_\chi \ll 1$ GeV），然后用 §V 的 accumulator+Cavendish 设计方案给出对这一**模型无关不可约通量**的灵敏度——即 Fig. 2。核心结果：**sub-GeV 质量区间，Cavendish+accumulator 方案可超越未来加速器（LDMX、LHC）灵敏度**。

## 4.2 原文内容（详细复述）

**[FACT]** 不可约通量来源：宇宙线空气簇射中**介子衰变**（$\pi/K \to \mu + \nu_\mu \to e + \nu_e$ 链上，若有 millicharge 混合，可产生 $\pi/K \to \ell + mCP$）产生的 mCPs，在地球表面热化。

**[FACT]** 不可约数密度（$m_\chi \ll 1$ GeV）：

$$n_\chi \sim 10^{-5}\,\mathrm{cm}^{-3} \times \left(\frac{q_\chi}{10^{-4}}\right)^2$$

该密度**不可约**——即无论 mCPs 是否为暗物质成分，宇宙线簇射都会持续产生。探测该密度等价于**直接测试模型本身**（独立于暗物质 relic 丰度），类似加速器搜索。

**[FACT]** 地球大气电场 $E_\oplus \sim 1$ V/cm 产生 $\phi_\oplus \sim 0.3$ MV 地壳–电离层电压差——**预期阻止轻热化 mCPs 蒸发**，显著增强局部丰度。作者在 Fig. 2 同时展示 $E_\oplus \neq 0$（增强）和 $E_\oplus = 0$（保守）两种情形；前者更现实。

**[FACT]** 在动力学混合暗光子模型中，$E_\oplus$ 积聚的正电荷 mCPs 会产生暗电场，使 mCPs 占据**地壳附近的窄径向带**——进一步增强局部密度。

**[FACT]** Fig. 2 与加速器比较：
- **LDMX** [44]（Fermilab 电子固定靶实验，mCP 对撞产生搜索）
- **LHC 方案** [14]（ATLAS/CMS 缺失横动量搜索）
- 对 sub-GeV 质量，**Cavendish+accumulator 使用几十年前技术已达成的噪声水平**，在**某些质量区间超越**未来加速器

**[FACT]** 关键论断："Cavendish 与加速器本质探测的是同一 mCP 参数空间（长程相互作用 mCPs）"——因此两者的比较是**公平且直接**的。

**[FACT]** 若 Johnson 噪声在 $t_{\rm int} \gg 1$ hr 时仍主导（BGP 1970 未显式验证），则对 $\sim 10^{-7}$ V 的噪声水平（对应 $t_{\rm int} \sim 1$ s），Cavendish+accumulator 仍能超越未来加速器。

**[FACT]** Discover tool 功能：accumulator 壳本身可作为**发现工具**——若探测到信号，可通过**改变 accumulator 运行时间、尺寸、电压**与信号的关联来确认 mCP 起源。

## 4.3 关键公式

**公式 7（不可约通量）**：

$$n_\chi^{\rm IR} \sim 10^{-5}\,\mathrm{cm}^{-3} \left(\frac{q_\chi}{10^{-4}}\right)^2 \quad (m_\chi \ll 1\,\mathrm{GeV})$$

**公式 8（探测该通量等价于模型测试）**：

$$\text{观测到的 }\Delta\phi_\chi \text{ 独立于暗物质 relic 丰度}$$

## 4.4 关键参数

| 参数 | 值 | 单位 |
|---|---|---|
| $n_\chi^{\rm IR}$（$q_\chi=10^{-4}$） | $10^{-5}$ | cm⁻³ |
| 质量适用范围 | $m_\chi \ll 1$ | GeV |
| $E_\oplus$ | $\sim 1$ | V/cm |
| $\phi_\oplus$ | $\sim 0.3$ | MV |
| 最低可探测 $n_\chi$ | $\sim 10^{-16}$ | cm⁻³（模型无关） |
| 比较对象 | LDMX、LHC | 加速器 |
| 超越质量区间 | sub-GeV | GeV |
| 等效测试噪声 | $\sim 10^{-7}$ | V（$t_{\rm int} \sim 1$ s） |

## 4.5 图表分析

**Figure 2（p.6）**：

- **目的**：展示专用 accumulator+Cavendish 方案对**宇宙线不可约 mCP 通量**的灵敏度
- **X 轴**：$q_\chi$（$10^{-6}$–$10^{-2}$，对数）
- **Y 轴**：$m_\chi$（$1$ MeV–$1$ GeV，对数）
- **两条曲线**（每种运行模式两条，共四条）：
  - 实线：$E_\oplus \neq 0$（大气电场增强积聚）
  - 虚线：$E_\oplus = 0$（保守）
  - 室内（$R_{\rm room}=10$ m 导电壁）vs 户外
- **橙色虚线**：未来加速器（LDMX [44] + LHC [14]）的灵敏度投影
- **观察**：Cavendish+accumulator（尤其 $E_\oplus \neq 0$）在**大 $q_\chi$ 区间**超越加速器；在小 $q_\chi$ 端被加速器超越
- **作者解释**：sub-GeV 时 Cavendish 用几十年前技术即可与未来加速器竞争

**[CRITIQUE]** Fig. 2 中 $E_\oplus = 0$ 情形被作者描述为"unrealistically conservative"（极不现实）——但仍作为保守估计保留。**$E_\oplus \neq 0$ 的增强效应缺乏独立实验验证**：地壳–电离层电压差 $\phi_\oplus \sim 0.3$ MV 是大气电学经典结果，但其对 mCPs 的**实际束缚效率**依赖于 mCP-大气散射细节，未被观测直接确认。

## 4.6 作者的逻辑

**问题** → mCP 是否有不可约（模型无关）通量？ → **方法** → 宇宙线簇射介子衰变产生 → **结果** → $n_\chi \sim 10^{-5}$ cm⁻³ $(q/10^{-4})^2$ 可测 → **下一步** → accumulator+Cavendish 方案探测 → **比较** → sub-GeV 超越 LDMX/LHC。

## 4.7 我的理解（INTERPRETATION）

**[INTERPRETATION]** 不可约通量的物理意义：**宇宙线是"免费的"mCP 源**——不需要假设 mCP 是暗物质成分，不需要 relic 丰度假设，探测它即"在实验室中直接验证模型"。这是本文相对加速器搜索的**哲学优势**——加速器搜索需要"产生 mCP 的相互作用顶点"，Cavendish 只需"mCP 存在"。

**[INTERPRETATION]** 与 ams02-2015 的潜在关联：AMS-02 精确测量的**反质子/正电子宇宙线谱**是宇宙线簇射模型的约束来源——若 AMS-02 数据修正了簇射中 $\pi/K$ 介子产生率，则 $n_\chi^{\rm IR}$ 会相应修正。**两篇文献在"宇宙线次级产物建模"这一环节共享不确定性**。

## 4.8 潜在问题与值得关注的地方（CRITIQUE）

**[CRITIQUE]** 不可约通量 $n_\chi^{\rm IR}$ 的具体计算来自 companion paper [30]，本信 **Letter 正文未给出推导**——读者无法独立验证 $10^{-5}$ cm⁻³ $(q/10^{-4})^2$ 这个数值。该数值依赖**宇宙线通量、大气深度分布、介子衰变分支比**等多个输入。

**[CRITIQUE]** 作者将不可约通量描述为"等价于测试模型本身"——但这一论断**仅在假设 mCP-标准模型耦合形式为标准电磁耦合**时成立。若 mCPs 通过**暗光子动力学混合**与 SM 耦合（本文主要讨论的模型），则"测试模型本身"需要同时约束动力学混合参数 $\epsilon$——而本文 Fig. 2 并未明确 $\epsilon$ 的取值。

**[CRITIQUE]** 与加速器比较的**公平性问题**：加速器搜索针对**新产生**的 mCPs（需要产生截面积），Cavendish 针对**已存在**的 mCPs（需要积聚效率）——两者在**不同耦合 regime** 各有优势。作者承认 Cavendish 在大 $q_\chi$ 端（$q_\chi \gtrsim 10^{-4}$）受积聚失效限制，但仍声称"sub-GeV 超越加速器"——精确的质量区间**未在正文明确给出**（Fig. 2 需目读）。