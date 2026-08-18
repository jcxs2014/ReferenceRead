# 3. Accumulator 壳设计方案

> 本章属于：Cavendish Tests of Millicharged Particles
>
> 上一章：`02_recasting_cavendish.md`
>
> 下一章：`04_cosmic_ray_population.md`

## 3.1 本节核心内容

本章提出具体实验方案：**在 Cavendish 壳外再套一层静电 accumulator 壳**（Van de Graaff 加速器型），将腔体 mCP 密度提升 $10^{10}$ 量级。核心推导：积聚密度 $n_{\rm trap} = n_\chi \simeq 3\epsilon_{\rm strong}^{(\rm trap)} V_E^{(\rm trap)} t_{\rm trap}/R_{\rm trap}$。

## 3.2 原文内容（详细复述）

**[FACT]** Accumulator 积聚密度公式（来自 companion paper [30]）：

$$n_{\rm trap} = n_\chi \simeq 3\, \epsilon_{\rm strong}^{(\rm trap)}\, V_E^{(\rm trap)}\, \frac{t_{\rm trap}}{R_{\rm trap}}$$

- $R_{\rm trap}$：accumulator 壳半径
- $t_{\rm trap}$：累积时间
- $V_E^{(\rm trap)}$：与 Eq. (3) 同形式的积聚速度
- 物理意义：腔内密度可被提升 $10^{10}$ 量级

**[FACT]** 具体设计参数：
- 外 accumulator 壳半径 $R_{\rm trap} = 2$ m
- 内 Cavendish 壳半径 $R_0 = 1$ m
- 内实心球半径 $0.5$ m（增强 mCPs 散射与能量损失概率）
- 材料：**铁**，壳厚度均 $1$ mm
- Accumulator 固定电压：$\phi_{\rm trap} = -1$ MV（相对地，负号针对正电荷 mCPs）

**[FACT]** 选负电压的物理：正电荷 mCPs 不与原子核结合（中性束缚态），而负电荷 mCPs 可能被原子核捕获——正电荷 mCPs 因此**可被地球电场驱动积聚**（地球大气电场 $E_\oplus \sim 1$ V/cm 使正电荷向上被排斥）。

**[FACT]** Cavendish 内壳运行参数：$\phi_0 = 50$ kV、$\nu_0 = 250$ Hz（与 BGP 1970 类似）；锁相放大器积分时间延长至 $t_{\rm int} = 1$ yr（BGP 为 1 hr）→ 噪声降至 $10^{-9}$ V $\times \sqrt{\rm hr/yr} \sim 10^{-11}$ V。

**[FACT]** 噪声原则上可进一步通过**高 Q 谐振 LC 电路**参数化降低——但作者在正文中**未详细展开**，因为高 Q 电路需工作在**低温**，会显著增加 mCP 扩散时间 $t_{\rm diff}$。

**[FACT]** 保守实现（室温 + 大气压）即可参数化提升 Fig. 1 的灵敏度；作者进一步考虑：
1. 户外运行（消除室内房间大小限制）
2. 内区真空（$10^{-6}$ atm，降低 mCP 与空气散射导致的扩散时间）
3. 积聚时间 $t_{\rm trap} = 1$ yr

**[FACT]** 真空维持需**纯被动方式**（如低温泵 cryopumping），因为主动泵浦会同时抽空强耦合 mCPs。

**[FACT]** 在 $10^{-6}$ atm 下，mCPs 不一定在壳内与空气散射——其运动近似**弹道**，反而因内壳电场加速而**降低扩散时间**、增强大 $q_\chi$ 侧灵敏度。

**[FACT]** 积聚饱和条件（动力学混合 dark photon 模型）：当 $e'^2 n_\chi R_0 \sim eq_\chi E_0$ 时，mCP 积聚产生的暗电场主导，积聚停止——这发生在 $E_\chi \sim eq_\chi n_\chi R_0 \sim (eq_\chi/e')^2 E_0 \sim \epsilon^2 E_0$ 时，即 mCPs 屏蔽了 $\epsilon^2$ 比例的驱动电场。

**[FACT]** 积聚饱和对**动力学混合参数 $\epsilon \gtrsim \sqrt{\Delta\phi_\chi/\phi_0} \sim \sqrt{1\,\mathrm{nV}/100\,\mathrm{kV}} = 10^{-7}$** 的模型无关；对本信 Letter 探索的大多数参数空间**不重要**。

**[FACT]** 模型无关灵敏度（Supplemental Material [41]）：$n_\chi$ 可低至 $\sim 10^{-16}$ cm⁻³，覆盖的 $q_\chi$ 范围比 Fig. 1 宽得多。

## 3.3 关键公式

**公式 5（积聚密度，腔内）**：

$$n_{\rm trap} \simeq 3\, \epsilon_{\rm strong}^{(\rm trap)}\, V_E^{(\rm trap)}\, \frac{t_{\rm trap}}{R_{\rm trap}}$$

**公式 6（积聚饱和，暗光子动力学混合）**：

$$E_\chi \sim \left(\frac{eq_\chi}{e'}\right)^2 E_0 = \epsilon^2 E_0$$

饱和条件：$e'^2 n_\chi R_0 \sim eq_\chi E_0$，即 $\epsilon \lesssim 10^{-7}$ 时饱和无关紧要。

## 3.4 关键参数

| 参数 | 值 | 单位 |
|---|---|---|
| $R_{\rm trap}$ | 2 | m |
| $R_0$ | 1 | m |
| 内实心球半径 | 0.5 | m |
| 材料 | 铁 | — |
| 壳厚度 | 1 | mm |
| $\phi_{\rm trap}$ | $-10^6$ | V |
| $\phi_0$ | $5\times10^4$ | V |
| $\nu_0$ | 250 | Hz |
| $t_{\rm int}$ | $1$ yr $\approx 8.76\times10^6$ | s |
| 噪声（外推） | $\sim 10^{-11}$ | V |
| 内压 | $10^{-6}$ | atm |
| 最低可探测 $n_\chi$ | $\sim 10^{-16}$ | cm⁻³ |

## 3.5 图表分析

本章无独立图；设计参数直接用于 §VI Fig. 2 的灵敏度投影。

## 3.6 作者的逻辑

**问题** → Cavendish 本身灵敏度不够 → **方法** → 套 accumulator 壳（同 companion paper [30] 物理）→ **设计** → 2 m 铁壳 / -1 MV / 室内真空 10⁻⁶ atm / 1 yr 积分 → **结果** → 噪声降至 $10^{-11}$ V，密度 $10^{10}$ 提升 → **局限** → 暗光子动力学混合积聚饱和仅对 $\epsilon \ll 10^{-7}$ 无关。

## 3.7 我的理解（INTERPRETATION）

**[INTERPRETATION]** 本文最深刻的工程洞察：**Cavendish 灵敏度瓶颈不是电压/频率/材料，而是"腔内 mCP 密度太低"**——accumulator 壳解决的是这一密度瓶颈，与探测器本身的灵敏度提升正交。

**[INTERPRETATION]** 真空 + 弹道运动的设计思路巧妙：传统思维"降低气压=减少散射=更难积聚"，但本文指出在低气压下 mCPs 做弹道运动、被电场加速、扩散时间**反而更短**——这是非平凡的结果。

**[INTERPRETATION]** 选择**铁**而非更高 Z 材料的原因未明说——但从 $V_E$ 公式看，$Z$ 影响散射截面从而改变 $t_{\rm diff}$；铁 ($Z=26$) 可能是兼顾"散射足够强"与"work function 足够高"的折中。

## 3.8 潜在问题与值得关注的地方（CRITIQUE）

**[CRITIQUE]** $t_{\rm int}=1$ yr 的 Johnson 噪声外推假设"**Johnson 噪声对其他可约系统噪声持续主导**"——但 BGP 1970 仅验证到 1 hr；1 yr 时**接触电势漂移、地电场扰动、机械振动**等系统噪声可能显著放大，使外推失效。作者明确承认这一点。

**[CRITIQUE]** Accumulator 壳的**泄漏电流**（1 MV 跨 2 m 铁壳的击穿问题）完全未讨论——这是工程可行性上最致命的挑战。1 MV 在真空中需要**极清洁的表面**与**无尖端电极**，1 mm 铁壳能否稳定维持 -1 MV 是重大工程问题。

**[CRITIQUE]** 积聚饱和条件 $\epsilon \lesssim 10^{-7}$ 的推导隐含**假设暗光子 $e'$ 的耦合形式与 SM 光子类似**——若暗光子是 massive vector boson 与 SM 存在非标准耦合（如 kinetic mixing + dark Higgs mixing），饱和公式需修改。

**[CRITIQUE]** $n_{\rm trap} = 3\epsilon V_E t_{\rm trap}/R_{\rm trap}$ 假设 mCPs 源是**持续供应**——若实际 mCP 通量有日变化（如随太阳风/宇宙线强度变化），长时间积分下的"有效 $n_\chi$"需做时间平均修正。