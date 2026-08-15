# 03. Stellar Models — Kappeler et al. (2011) §III 精读

> 本章属于：The history of the s-process: Its status in the light of modern nucleosynthesis modeling
>
> 上一章：`02_nuclear_physics.md`
>
> 下一章：`04_observational_constraints.md`

---

## 3.1 本节核心内容

[FACT] §III 系统综述 s 过程的**两种恒星场景**及其演化模型：

1. **Weak s 过程**：大质量恒星（M > 8 M☉）的 Core He 燃烧与 Shell C 燃烧壳层
2. **Main s 过程**：低-中等质量 AGB 星（1–3 M☉）的 He 壳层闪
3. **Strong s 成分**（低金属丰度 AGB 星的 first strong pulse）——在 §III.C 末尾引入
4. **经典方法**（Classical approach）——作为对照和 r-residual 分离的基础

[FACT] §III 的核心论点是：**s 过程不是一个单一的过程，而是依赖于初始质量、金属丰度、$^{13}{\rm C}$ 口袋强度、TDU 效率、质量损失率的复杂多参数过程。**

## 3.2 原文内容

### 3.2.1 章节结构

[FACT] §III 分为五个子节：

- **III.A Classical approach**（171 页起）：经典模型及其局限
- **III.B Massive stars**（171 页起）：weak s 过程在大质量星的场景
- **III.C AGB stars**（171 页起）：main s 过程在低质量 AGB 星的场景
- **III.D Theoretical AGB results**（173 页起）：FRANEC + postprocess 代码的具体结果
- **III.E The main s component and galactic chemical evolution**（176 页起）：银河系化学演化中的 s 过程

### 3.2.2 经典方法（III.A）

[FACT] 经典方法的诞生源于恒星模型不成熟的时代：

[FACT] Seeger et al. (1965) 提出的经典模型假设：
- 一部分 $f$ 的太阳 $^{56}{\rm Fe}$ 被辐照
- 中子暴露服从指数分布
- 中子密度与温度**不随时间变化**

[FACT] 反应流解析解（原文 Eq. 5，§II 已详细讨论）：

$$ \langle\bar{\sigma}\rangle_i N_{s,i} = {}^{56}{\rm Fe}_{\odot}\, f\, \rho_0\, \left(1 + \frac{\rho_0}{\langle\bar{\sigma}\rangle_i}\right)^{-1} $$

[FACT] 拟合得到的两个全局参数：
- $f \approx 0.04\%$：被辐照的 $^{56}{\rm Fe}$ 分数
- $\rho_0 \approx 15$ n/种子：平均中子暴露

[FACT] **经典模型的巨大成功**：在分支点之外的 s-only 核素，均方偏差仅 3%（Käppeler, Gallino et al., 1990）。

[FACT] **经典模型的致命失败**——$^{142}{\rm Nd}$（Arlandini et al., 1999）：
- $^{142}{\rm Nd}$ 是 $N=82$ magic neutron number 附近的 s-only 核素
- 经典模型预测的系统性偏差说明**经典假设（恒定参数）无法复现分支点细节**
- 这一失败直接导致第一代恒星 s 过程模型的建立（Gallino et al., 1998；Arlandini et al., 1999）

[FACT] **经典方法仍有的价值**：
- **R-residual 分离**：$N_r = N - N_s$ 从太阳丰度中减去 s 过程成分得到 r 过程成分
- 图 8 显示：经典模型与恒星模型给出的 r-residual **几乎相同**，因为主 s 成分在 magic numbers 之间达到反应流平衡

### 3.2.3 大质量星（III.B）——Weak s 过程

[FACT] **大质量星定义**：$M > 8\ M_{\odot}$，以 II 型超新星（SN II）结束生命。

[FACT] Weak s 过程发生的**两个阶段**：

**阶段 1：Core He 燃烧**
- 温度 $T \approx 3\times10^8$ K
- 中子源反应：$^{22}{\rm Ne}(\alpha,n)^{25}{\rm Mg}$
- 中子密度 $n_n \sim 10^{10}$ cm$^{-3}$

**阶段 2：Shell C 燃烧**
- 温度 $T \approx 1\times10^9$ K
- 中子源反应：$^{22}{\rm Ne}(\alpha,n)^{25}{\rm Mg}$
- $\alpha$ 粒子来自 $^{12}{\rm C}(^{12}{\rm C},\alpha)^{20}{\rm Ne}$
- 中子密度 $n_n \gtrsim 10^{12}$ cm$^{-3}$

[FACT] $^{22}{\rm Ne}$ 的来源链（关键）：

$$ ^{14}{\rm N}(\alpha,\gamma)^{18}{\rm F}(\beta^+)^{18}{\rm O}(\alpha,\gamma)^{22}{\rm Ne} $$

其中 $^{14}{\rm N}$ 来自前 H 燃烧阶段的 CNO 循环产物。

[FACT] **这一来源链是 weak s 过程"次级"性质的根本原因**：$^{22}{\rm Ne}$ 依赖 CNO 循环产物，因此 weak s 过程的产额随金属丰度降低而减少。

[FACT] **Supernova 抛射的复杂性**：

- 25 M☉ 恒星的核心质量 >3.5 M☉ 部分被爆炸核合成摧毁
- 但 2.5 M☉ 以下的核层保留了 s 过程特征（Raiteri et al., 1993；Woosley & Weaver, 1995；Limongi et al., 2000）
- Postprocess 模型和全恒星演化模型都验证了这一场景

[FACT] **Weak s 过程的传播效应**：

[FACT] 原文核心警告：**weak s 过程没有达到反应流平衡**，因此：
> "a particular MACS not only determines the abundance of the respective isotope, but also affects the abundances of all heavier isotopes as well"

[FACT] **关键案例：$^{62}{\rm Ni}$(n,$\gamma$)$^{63}{\rm Ni}$**

- 该截面长期被 TOF 数据高估
- 修正后（Nassar et al., 2005；Tomyo et al., 2005；Alpizar-Vicente et al., 2008）引起 Fe–Sr 区间所有 s 过程丰度的**系统性重新分配**
- 这一传播效应对银河系化学演化模型有直接影响

[FACT] **Weak s 的贡献估计**（§V 总结）：
- 太阳 Zn 的一半
- 太阳 Cu 的 70–80%
- 太阳 Ga、Ge、As 的 70–80%

[FACT] **LEPP（Light Element Primary Process）**：

[FACT] 太阳系中轻 s 元素（Sr, Y, Zr）包含一个**仍未知起源的初级来源**，称为 LEPP。
- 不同于 weak s（次级）和主 s（AGB，初级-次级混合），LEPP 是**纯初级**
- 可能关联到大质量星 pre-explosive 或 explosive 核合成阶段
- 是所有 s 过程研究中最悬而未决的问题之一

### 3.2.4 AGB 星（III.C）——Main s 过程

[FACT] **AGB 星质量范围**：1–8 M☉（本文重点 1–3 M☉ 的低质量 AGB）

[FACT] **热脉冲 AGB（TP-AGB）的演化序列**：

1. He 壳层闪（He shell flash）：不稳定的 He 壳层燃烧
2. 间歇性的对流混合（thermal pulse, TP）：He 壳层对流传到 H 燃烧壳层
3. **Third dredge-up (TDU)**：对流包络向下扩展，将 s 过程产物带入恒星表面
4. 间歇性质量损失（stellar winds）：AGB 星通过星风损失大部分包络

[FACT] **主 s 过程的两个中子源**：

**中子源 1：$^{12}{\rm C}$($\alpha$,n)$^{16}{\rm O}$**
- 温度 $T \approx 0.9\times10^8$ K
- 中子密度 $n_n \sim 10^6 – 10^8$ cm$^{-3}$
- 暴露时间 ~10,000 年
- **初级过程**（与金属丰度无关，因为 $^{12}{\rm C}$ 是恒星自己合成的）

**中子源 2：$^{22}{\rm Ne}$($\alpha$,n)$^{25}{\rm Mg}$**
- 温度 $T \approx 3.5\times10^8$ K（中等质量 AGB，4 < M/M☉ < 8）
- 中子密度更高
- 次级过程（依赖金属丰度）

[FACT] **$^{13}{\rm C}$ 口袋（13C pocket）——主 s 过程的关键**：

[FACT] $^{13}{\rm C}$ 口袋是 s 过程中**最核心的微物理结构**，其形成机制为：

1. TDU 后对流包络回落
2. H 壳层点火，温度升高，熵降低
3. 第一次 convective He 不稳定性扩展穿过 H 壳层
4. **质子被"捕获"到富含 $^{12}{\rm C}$ 的 He 层**
5. $^{12}{\rm C}(p,\gamma)^{13}{\rm N}(\beta^+)^{13}{\rm C}$ 形成薄的 $^{13}{\rm C}$ 富集层
6. 下一次 TP 期间，$^{13}{\rm C}$($\alpha$,n)$^{16}{\rm O}$ 提供中子

[FACT] **$^{13}{\rm C}$ 口袋的 ab initio 处理**：

[FACT] 早期模型中 $^{13}{\rm C}$ 口袋是**人为参数**（Straniero et al., 2003, 2006；Gallino et al., 1998；Arlandini et al., 1999 的"标准口袋"ST）

[FACT] 现代模型通过以下物理过程自然产生 $^{13}{\rm C}$ 口袋：
- **对流超射（convective overshoot）**：Herwig et al. (1997)、Herwig (2000, 2004) 引入指数扩散超射
- **旋转（rotation）**：Langer et al. (1999)
- **重力波混合（gravity wave mixing）**：Denissenkov & Tout (2003)

[FACT] **中等质量 AGB（4 < M/M☉ < 8）**：
- He 壳层闪温度达 $3.5\times10^8$ K
- $^{22}{\rm Ne}$($\alpha$,n)$^{25}{\rm Mg}$ 贡献显著
- 但 He 壳层质量和 TDU 效率远小于低质量 AGB
- 因此包络中的 s 过程丰度**远低于**低质量 AGB 的预测

[FACT] **低金属丰度 AGB 的"strong component"**：

[FACT] 原文 III.C 末尾引入一个**关键新现象**——**strong s 过程成分**（限于最低质量 AGB 星，发生 TDUs）：

- 仅发生在 $\rm[Fe/H] < -2.5$ 的 AGB 星
- 第一个完全发展的 TP 期间发生
- $^{13}{\rm C}$ 口袋形成机制不同于大质量 AGB 的"标准口袋"
- He 壳层可能**分裂为两个子壳**（Cristallo, Piersanti et al., 2009）：
  - 下子壳：$^{12}{\rm C}$($\alpha$,n)$^{16}{\rm O}$ 主导
  - 上子壳：CNO 循环 + $^{13}{\rm C}$($\alpha$,n)$^{16}{\rm O}$
- **第一次 TDU 携带轻 s 元素（ls）到表面**
- **第二次 TDU 携带重 s 元素（hs）和 Pb 到表面**

[FACT] 这一"strong component"可能是低金属丰度 CEMP-s 星中高 s 增强度的关键来源（§III.D 和 §IV.B.2 详述）。

### 3.2.5 AGB 理论结果（III.D）

[FACT] 本文使用的 AGB 模型体系：

- **FRANEC 演化代码**：Frascati Raphson-Newton evolutionary code（Chieffi & Straniero, 1989）
- **Postprocess 代码**：包含完整的 s 过程反应网络至 Bi（Bisterzo et al., 2010）
- **$^{13}{\rm C}$ 口袋参数化**：从"标准口袋"（ST）出发，乘以不同系数（ST×2, ST, ST/2, ST/3, ..., ST/150）

[FACT] 图 10 展示 $^{13}{\rm C}$ 口袋形成过程（Straniero et al., 2009）：
- (a) TDU 刚发生，对流包络回落
- (b) $^{13}{\rm C}$ 在较热区域开始形成
- (c) $^{14}{\rm N}$ 也开始产生
- (d) $^{13}{\rm C}$ 和 $^{14}{\rm N}$ 口袋完全形成

[FACT] $^{13}{\rm C}$ 口袋的边界条件：

- **最低 $^{13}{\rm C}$ 口袋**：刚好能影响最终 s 过程分布
- **最高 $^{13}{\rm C}$ 口袋**：ST×2——超过此值则 $^{13}{\rm C}$(p,$\gamma$)$^{14}{\rm N}$ 反应竞争使 $^{13}{\rm C}$ 增加不显著
- **效率假设为常数**：对所有 TP 周期相同

[FACT] **三个 s 过程峰的定义**：

$$ \rm[ls/Fe] = \frac{1}{2}\left(\rm[Y/Fe] + \rm[Zr/Fe]\right) $$

$$ \rm[hs/Fe] = \frac{1}{3}\left(\rm[La/Fe] + \rm[Nd/Fe] + \rm[Sm/Fe]\right) $$

- ls 元素（轻 s）：Sr, Y, Zr（$N=50$ magic number 附近）
- hs 元素（重 s）：Ba, La, Ce, Nd, Sm（$N=82$ magic number 附近）
- Pb（$N=126$ magic number 附近）

[FACT] **AGB 模型预测与观测的比较**（图 12 与 13）：
- 银盘金属丰度（$\rm[Fe/H] = -1$）：理论预测与 Ba 星、CEMP-s 星的 $\rm[hs/ls]$ 和 $\rm[Pb/hs]$ 观测值一致
- 低金属丰度（$\rm[Fe/H] < -2.5$）：$^{13}{\rm C}$ 口袋效率变化可解释 CEMP-s 星的丰度散布
- $\rm[hs/ls]$ 最大预测值 1 dex（不论初始 r 增强）

### 3.2.6 银河系化学演化（III.E）

[FACT] 银河系结构组成：

| 成分 | 金属丰度 | 年龄 | 特征 |
|---|---|---|---|
| **薄盘（thin disk）** | ~太阳 | 0–10 Gyr | 太阳所在 |
| **厚盘（thick disk）** | 较低 | 老 | 可能形成于早期小星系合并 |
| **核球（bulge）** | 宽分布（含太阳） | 老 | 早期形成，观测困难 |
| **晕（halo）** | 贫金属 | >10 Gyr | 含约 150 个球状星团 |
| **卫星矮星系** | 多样 | 多样 | 与银河系相互作用形成 |

[FACT] **主 s 过程在银河系演化中的作用**：
- 所有 $A > 90$ 的 s 同位素来自主 s 过程
- 太阳 Pb 的一半来自主 s 过程
- 另一半来自低金属丰度 AGB 星的 strong component

[FACT] **Weak s 对银河系化学演化的贡献**：

- 太阳 Zn：~50% 来自 weak s；剩余 64Zn 来自超新星 $\nu$-wind 的 r 冻结
- 太阳 Cu：weak s 贡献 90%，main s 贡献 5%，SN Ia 不贡献
- 预测：$\rm[Zn/Fe]$ 在晕中应约 +0.2 dex（与观测一致）
- 预测：$\rm[Cu/Fe]$ 在晕中应恒定且强负，约 $-0.8$ dex

[FACT] 这些预测已被观测证实（Bisterzo et al., 2004；Pignatari et al., 2010）。

[FACT] **s 过程对银河系金属丰度演化的影响**：
- 银河系化学演化中的 s 过程产额对**中子源反应率、$^{13}{\rm C}$ 口袋、初始质量函数（IMF）**高度敏感
- 这些不确定性直接影响**核素合成年代学**（如 Re/Os、W/Pt 宇宙时钟）

## 3.3 关键公式

### 3.3.1 反应流（经典方法，Eq. 5）

$$ \langle\bar{\sigma}\rangle_i N_{s,i} = {}^{56}{\rm Fe}_{\odot}\, f\, \rho_0\, \left(1 + \frac{\rho_0}{\langle\bar{\sigma}\rangle_i}\right)^{-1} $$

极限行为：
- $\langle\bar{\sigma}\rangle_i \gg \rho_0$：$\langle\bar{\sigma}\rangle_i N_{s,i} \to {}^{56}{\rm Fe}_{\odot}\, f\, \rho_0$（饱和）
- $\langle\bar{\sigma}\rangle_i \ll \rho_0$：$\langle\bar{\sigma}\rangle_i N_{s,i} \to {}^{56}{\rm Fe}_{\odot}\, f\, \langle\bar{\sigma}\rangle_i$

### 3.3.2 R-residual 方法

$$ N_r(A) = N_{\odot}(A) - N_s(A) $$

- $N_{\odot}(A)$：太阳系丰度
- $N_s(A)$：s 过程贡献（来自经典模型或恒星模型）
- 两种方法给出的 $N_r$ 分布几乎相同（图 8）

### 3.3.3 $^{13}{\rm C}$ 口袋效率参数化

$$ ^{13}{\rm C}_{\rm pocket} = \alpha \cdot ^{13}{\rm C}_{\rm ST} \quad \text{with } \alpha \in \{2,\ 1,\ 1/2,\ 1/3,\ \ldots,\ 1/150\} $$

其中 $^{13}{\rm C}$_ST 是 Gallino et al. (1998) 和 Arlandini et al. (1999) 的标准口袋。

### 3.3.4 s 过程峰丰度比

$$ \rm[ls/Fe] = \frac{1}{2}\left(\rm[Y/Fe] + \rm[Zr/Fe]\right) $$

$$ \rm[hs/Fe] = \frac{1}{3}\left(\rm[La/Fe] + \rm[Nd/Fe] + \rm[Sm/Fe]\right) $$

$$ \rm[hs/ls] = \rm[hs/Fe] - \rm[ls/Fe] $$

### 3.3.5 稀释因子（CEMP-s 星）

$$ d_{\rm il} = \log_{10}\frac{M_{\rm env}}{M_{\rm AGB\ transferred}} $$

- $M_{\rm env}$：观测恒星对流包络的质量
- $M_{\rm AGB\ transferred}$：从 AGB 伴星通过星风转移的质量

[FACT] 稀释因子用于模拟 CEMP-s 星的双星质量传输过程。

### 3.3.6 $^{22}{\rm Ne}$ 中子源的链式反应

$$ ^{14}{\rm N}(\alpha,\gamma)^{18}{\rm F}(\beta^+)^{18}{\rm O}(\alpha,\gamma)^{22}{\rm Ne} $$

$$ ^{22}{\rm Ne}(\alpha,n)^{25}{\rm Mg} \quad \text{（实际中子源）} $$

## 3.4 关键参数

| 参数 | 数值 | 备注 |
|---|---|---|
| 大质量星质量范围 | $M > 8\ M_{\odot}$ | SN II 前身 |
| Core He 燃烧温度 | $T \approx 3\times10^8$ K | weak s |
| Shell C 燃烧温度 | $T \approx 10^9$ K | weak s 高温阶段 |
| Core He 燃烧中子密度 | $n_n \sim 10^{10}$ cm$^{-3}$ | $^{22}{\rm Ne}$ 源 |
| Shell C 燃烧中子密度 | $n_n \gtrsim 10^{12}$ cm$^{-3}$ | $^{22}{\rm Ne}$ 源 |
| 主 s AGB 质量范围 | $1–3\ M_{\odot}$ | |
| 中等质量 AGB | $4–8\ M_{\odot}$ | $^{22}{\rm Ne}$ 源主导 |
| $^{13}{\rm C}$ 口袋温度 | $T \approx 0.9\times10^8$ K | $^{12}{\rm C}$($\alpha$,n)$^{16}{\rm O}$ |
| 主 s 过程暴露时间 | ~10,000 年 | $^{13}{\rm C}$ 源 |
| $^{13}{\rm C}$ 口袋效率参数 | $\alpha \in [1/150,\ 2]$ | ST 的倍数 |
| Strong s 金属丰度界限 | $\rm[Fe/H] < -2.5$ | |
| 经典模型 $f$（$^{56}{\rm Fe}$ 辐照分数） | 0.04% | |
| 经典模型 $\rho_0$（平均中子暴露） | 15 n/种子 | |
| Weak s 对太阳 Zn 贡献 | ~50% | |
| Weak s 对太阳 Cu 贡献 | 70–80% | |
| Weak s 对太阳 Ga/Ge/As 贡献 | 70–80% | |
| 主 s 对 $A > 90$ s 同位素贡献 | ~100% | |
| 主 s 对太阳 Pb 贡献 | ~50% | |
| Strong s 对太阳 Pb 贡献 | ~50% | 另一半 |

## 3.5 图表分析

### Figure 8 — R-residual 分布

**1. 目的**：对比经典模型与恒星模型给出的 r 过程成分。

**2. 坐标轴**：横轴质量数 $A$，纵轴核素丰度（Ni 相对 Si =$10^{6}$）。

**3. 图中元素**：
- 空心方块：r-residual 值（$N_r = N - N_s$）
- 实心方块：r-only 核素的实验丰度

**4. 关键观察**：经典模型与恒星模型的 r-residual **几乎相同**，且与 r-only 核素丰度吻合。

**5. 物理意义**：主 s 成分在 magic numbers 之间达到反应流平衡，因此经典与恒星模型的 s 成分相同，r-residual 自然一致。

### Figure 10 — $^{13}{\rm C}$ 口袋形成

**1. 目的**：分四步展示 $^{13}{\rm C}$ 口袋从 TDU 后到完全形成的演化过程。

**2. 图中元素**：
- 横线：$^{12}{\rm C}$（点线）
- 纵线：$^{13}{\rm C}$（实线）
- 斜线：$^{14}{\rm N}$（虚线）
- 交叉：H

**3. 四步演化**：
- (a) TDU 刚发生，对流包络回落
- (b) 较热区域开始产生 $^{13}{\rm C}$
- (c) $^{14}{\rm N}$ 也开始产生
- (d) $^{13}{\rm C}$ 和 $^{14}{\rm N}$ 口袋完全形成

**4. 物理意义**：$^{13}{\rm C}$ 口袋是主 s 过程中子源的核心微物理结构，其形成机制直接决定 s 过程效率。

### Figure 12 — [hs/ls] 和 [Pb/hs] vs [Fe/H]

**1. 目的**：对比 AGB 模型预测与 Ba 星、CEMP-s、CEMP-s=r 星的观测。

**2. 坐标轴**：横轴 [Fe/H]，纵轴 [hs/ls] 或 [Pb/hs]。

**3. 关键观察**：
- 银盘金属丰度（[Fe/H] = -1）：理论预测与观测一致
- 晕金属丰度：[Pb/hs] 散布 ~2 dex
- 1.3 M☉ AGB 模型 + r 增强 2 dex 可解释 CEMP-s=r 星

**4. 物理意义**：$^{13}{\rm C}$ 口袋效率的变化（对应氢混合进 $^{13}{\rm C}$ 口袋的程度）是观测散布的主要解释。

### Figure 13 — [hs/ls] vs [Fe/H]（含 r 增强）

**1. 目的**：在初始 r 增强（[r/Fe]$_{ini}$ = 2）下展示 AGB 模型的 [hs/ls] 预测。

**2. 关键观察**：
- 不论是否包含 r 增强 2 dex，[hs/ls] 最大预测值 = 1
- 模型与 CEMP-s=r 星的 ms-TO 观测吻合良好

### Table（AGB 模型参数化）

| 模型参数 | 值 | 备注 |
|---|---|---|
| 初始质量 | 1.3 M☉ | |
| $^{13}{\rm C}$ 口袋 | ST×2 到 ST/150 | 覆盖观测散布 |
| 初始 r 增强 | [r/Fe]$_{ini}$ = 2 | 解释 CEMP-s=r 星 |
| 稀释因子 | 0–1 dex | 对应质量传输比例 |

## 3.6 作者的逻辑

[FACT] §III 的论证链：

```
s 过程核合成发生在 He 燃烧层
  → 两类恒星：大质量星（weak s）和 AGB 星（main s）
    → 经典方法曾成功但存在不自洽
      → 新一代恒星模型解决经典方法的不自洽
        → AGB 星：$^{13}{\rm C}$ 口袋 → TDU → 表面 s 过程增强
          → 参数化：质量、金属丰度、$^{13}{\rm C}$ 口袋、TDU、质量损失率
            → 与观测对比（Ba 星、CEMP-s）
              → 银河系化学演化中的 s 过程贡献
```

[FACT] 作者在 §III 中反复强调的核心逻辑：**AGB 星是 s 过程的主工厂**——主 s 成分的丰度由 $^{13}{\rm C}$ 口袋决定，而 $^{13}{\rm C}$ 口袋的效率又由恒星质量和金属丰度决定。

## 3.7 我的理解

[INTERPRETATION] §III 最重要的认识是：**s 过程不是单一过程，而是一个随恒星参数（质量、金属丰度）连续变化的多分量过程**。

- **Weak s**：大质量星、次级过程、Fe–Sr 区间
- **Main s**：低质量 AGB、初级过程、Sr–Bi 区间
- **Strong s**：最低质量低金属丰度 AGB、first strong pulse、Pb 的第二半

[INTERPRETATION] $^{13}{\rm C}$ 口袋是整个 AGB s 过程研究的**中心枢纽**——它的形成机制、深度、效率决定了：
- 中子产量（$^{12}{\rm C}$($\alpha$,n)$^{16}{\rm O}$）
- 反应流时间结构（10,000 年的暴露时间）
- 表面 s 过程丰度（通过 TDU）
- CEMP-s 星的丰度散布

[CRITIQUE] **$^{13}{\rm C}$ 口袋仍然部分参数化**：尽管现代模型通过对流超射、旋转混合等物理过程产生了 $^{13}{\rm C}$ 口袋，但口袋的**精确深度和效率**仍不完全由 ab initio 物理决定。这是当前 AGB 模型最大的系统不确定性。

[CRITIQUE] **LEPP 的悬案**：轻 s 元素（Sr, Y, Zr）中有一个未知的初级来源——LEPP。§III.B 末尾明确提出但完全没有解决，这是 s 过程研究中**最未解的谜题**。

[CRITIQUE] **Strong s 成分的理论依据**：Cristallo et al. (2009) 提出 He 壳层分裂机制，但这一机制的**物理必然性**和**观测约束**仍待进一步确认。若该机制不成立，则低金属丰度 CEMP-s 星的强 s 增强需要其他解释。

## 3.8 潜在问题与值得关注的地方

### 8.1 $^{13}{\rm C}$ 口袋的 ab initio 边界

[CRITIQUE] 虽然对流超射、重力波混合等物理过程使 $^{13}{\rm C}$ 口袋不再纯靠参数化，但口袋的深度仍与恒星演化代码中的**对流超射参数**有关。这意味着：
- 不同代码给出不同 $^{13}{\rm C}$ 口袋
- 与观测的\"吻合\"可能只是调参的结果
- 需要独立的观测约束（如表面 C/N 比）来锚定口袋深度

### 8.2 CEMP-s 星的 r 增强解释

[CRITIQUE] 图 13 显示，1.3 M☉ AGB 模型 + [r/Fe]$_{ini}$ = 2 可解释 CEMP-s=r 星。但：
- r 增强 2 dex 是否需要假设**超新星污染**？
- 该 r 增强是**双星系统的初始条件**，不是 AGB 模型预测的结果
- 因此 AGB 模型对 CEMP-s=r 星的\"解释\"实际上是**双星演化 + r 过程天体物理**的复合结果

### 8.3 中等质量 AGB 的贡献

[CRITIQUE] 中等质量 AGB（4–8 M☉）的 s 过程产额低，因为：
- He 壳层质量小
- TDU 效率低
- $^{22}{\rm Ne}$($\alpha$,n)$^{25}{\rm Mg}$ 源虽然强，但不足以弥补 He 壳层质量的不足

这是否意味着中等质量 AGB 星在银河系化学演化中可以忽略？§III 没有明确回答。

### 8.4 银河系化学演化的参数敏感性

[CRITIQUE] §III.E 的 s 过程产额对以下参数敏感：
- **中子源反应率**：$^{12}{\rm C}$($\alpha$,n)$^{16}{\rm O}$、$^{22}{\rm Ne}$($\alpha$,n)$^{25}{\rm Mg}$
- **$^{13}{\rm C}$ 口袋效率**：质量-金属丰度依赖
- **初始质量函数（IMF）**：AGB 星的质量分布
- **星风质量损失率**：AGB 演化时间尺度

这些参数中任何一个的变化都可能显著影响银河系化学演化模型中的 s 过程产额。

### 8.5 经典模型的\"残余价值\"

[CRITIQUE] 经典模型虽然在分支点细节上失败，但其 r-residual 方法在 A>90 区间仍是**目前最可靠的 r 过程成分分离方法**——因为恒星模型与经典模型在此区间的 s 成分一致。

---

## §III 章节元数据

```yaml
---
chapter: 3
title: 'Stellar Models'
source_page: '166–177'
parent_doc: '0017_kaeppeler-2011'
parent_title: 'The s process: Nuclear physics, stellar models, and observations'
parent_authors: 'Kappeler, Gallino, Bisterzo, Aoki'
parent_year: 2011
parent_journal: 'Rev. Mod. Phys. 83, 157'
parent_doi: '10.1103/RevModPhys.83.157'
summary: 'Weak s（大质量星）、Main s（AGB 星）、Strong s（低金属丰度 AGB）的恒星场景与模型'
key_figures:
  - 'Fig. 8: R-residual 分布（经典 vs 恒星模型）'
  - 'Fig. 10: 13C 口袋形成四步演化'
  - 'Fig. 12: [hs/ls] 和 [Pb/hs] vs [Fe/H]'
  - 'Fig. 13: [hs/ls] vs [Fe/H] 含 r 增强'
key_equations:
  - '反应流（Eq. 5）'
  - 'R-residual 分离'
  - '13C 口袋效率参数化'
  - 's 过程峰丰度比 [ls/Fe]、[hs/Fe]'
  - '稀释因子 d_il'
  - '22Ne 中子源反应链'
key_topics:
  - '经典方法与其失败（142Nd）'
  - 'Weak s（大质量星 Core He / Shell C 燃烧）'
  - 'Main s（AGB 星热脉冲、13C 口袋、TDU）'
  - 'Strong s（低金属丰度 first strong pulse）'
  - 'LEPP（轻元素初级过程）'
  - '银河系化学演化中的 s 过程'
next_chapter: '04_observational_constraints.md'
prev_chapter: '02_nuclear_physics.md'
---
```
