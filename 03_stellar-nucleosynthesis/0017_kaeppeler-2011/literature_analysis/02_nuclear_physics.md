# 02. Nuclear Physics — Kappeler et al. (2011) §II 精读

> 本章属于：The history of the s-process: Its status in the light of modern nucleosynthesis modeling
>
> 上一章：`01_introduction.md`
>
> 下一章：`03_stellar_models.md`

---

## 2.1 本节核心内容

[FACT] §II 系统综述了 s 过程研究所需的核物理输入，重点是**中子俘获截面（(n,$\gamma$) cross sections）的测量与计算**，以及**恒星条件下 $\beta$ 衰变率的修正**。这一节在逻辑上是整个 s 过程研究的\"数据基石\"——所有的恒星模型与观测比较都依赖于这些核数据的精度。

[FACT] §II 的核心论点是：**仅靠实验不足以覆盖所有核素与所有能量；实验与理论（统计模型）的紧密结合是 s 过程核物理研究的根本范式。**

## 2.2 原文内容

### 2.2.1 章节结构

[FACT] §II 分为四个子节：

- **II.A Measurement of neutron-capture rates**：中子俘获率的实验测量方法
  - (1) Pulsed neutron sources（脉动中子源）
  - (2) Time-of-flight methods（飞行时间法）
  - (3) Data acquisition and analysis techniques（数据采集与分析技术）
  - (4) Activations（激活法）
  - (5) Studies on radioactive isotopes（放射性同位素研究）
- **II.B Cross-section calculations**：截面计算
  - (1) Statistical model（统计模型 / Hauser-Feshbach）
  - (2) Maxwellian averaged cross sections（Maxwellian 平均截面，MACS）
  - (3) Stellar enhancement factors（恒星增强因子，SEF）
- **II.C $\beta$-decay under stellar conditions**：恒星条件下的 $\beta$ 衰变
- **II.D Status and prospects**：截面数据现状与展望

### 2.2.2 中子源

[FACT] 中子俘获实验依赖的脉动中子源有三类：

**小型加速器（direct-current mode）**：

$$ ^7{\rm Li}(p,n)^7{\rm Be} \quad \text{可覆盖} \quad kT \approx 25\ {\rm keV}\ \text{到}\ 500\ {\rm keV} $$

用于模拟 AGB 星中 ²²Ne($\alpha$,n)²⁵Mg 中子源的温度（23 keV 有效温度）；

**电子直线加速器（white neutron source）**：

$$ e^- \rightarrow \gamma \xrightarrow{{\rm p.g.}} p, n $$

GELINA（Geel, Belgium）、ORELA（Oak Ridge）；连续中子能谱从热能到数十 MeV；

**散裂源（spallation source）**：

- LANSCE (Los Alamos)：$E_p = 800$ MeV 质子束
- n_TOF (CERN)：$E_p = 20$ GeV 质子束

[FACT] **n_TOF 是当前最亮的\"白中子源\"**：每个入射质子产生约 300 个中子；飞行路径 185 m、脉冲宽度 7 ns、重复率 0.4 Hz。

[FACT] n_TOF 与 LANSCE 的差异：

| 设施 | 飞行路径 | 时间分辨率 | 重复率 | 特点 |
|---|---|---|---|---|
| LANSCE | 20 m | 250 ns | 50 Hz | 高峰值中子通量 |
| n_TOF (CERN) | 185 m | 7 ns | 0.4 Hz | 高能量分辨率 |

### 2.2.3 探测器技术

**（a）4$\pi$ 吸收量热计（calorimetric detector）**：

[FACT] 核反应释放的总 $\gamma$ 级联能量等于中子结合能，这是最直接的捕获事件标识。

$$ E_{\rm casc} = \sum_{i=1}^{m} E_i = E_{\rm tot} $$

[FACT] 4$\pi$ 探测器的关键要求：**效率接近 100%**。当前主流是 Ba$F_{2}$ 晶体阵列：

- **Karlsruhe（42 模块）**：截锥金字塔排列（富勒烯型几何），各模块对样品覆盖相同的立体角
- **ORNL / FZ Rossendorf**：六边形 Ba$F_{2}$ 圆柱阵列
- **DANCE（LANSCE，162 模块）**：最先进的 4$\pi$ 阵列

[FACT] Ba$F_{2}$ 相比早期液体闪烁体的优势：
- $\gamma$ 能量分辨率更好
- 本底更低
- 可分离快慢成分（快成分用于能谱，慢成分用于总能量）

**（b）低中子灵敏探测器（Moxon-Rae 型 / PHWT）**：

[FACT] **Pulse Height Weighting Technique（PHWT）** 将"探测效率随沉积能量线性变化"这一要求，从探测器设计后移到离线加权函数中：

$$ \varepsilon(E_i) = k E_i $$

通过离线加权函数实现。

[FACT] $C_{6}$$F_{6}$ 液闪 → $C_{6}$$D_{6}$ 液闪的改进：氘的 (n,$\gamma$) 截面远小于氢，大幅降低了中子散射本底。

[FACT] 当前 **PHWT 的系统误差已降至 <2%**（Abbondanno et al., 2004b），远低于早期 20% 的水平。

**（c）关键改进——6LiH 吸收壳**：

[FACT] 样品散射中子被 Ba$F_{2}$ 晶体捕获产生 ~10% 的系统本底；用 6LiH 或 6Li 化合物吸收壳包裹样品可显著抑制这一本底（Reifarth et al., 2004b；Heil et al., 2001）。

### 2.2.4 数据采集（FADC 时代）

[FACT] 现代 (n,$\gamma$) 实验全部采用 **Flash Analog-to-Digital Converter (FADC)**：

- 采样整个探测器信号的波形，而非只记录幅度
- 允许离线重复分析、修正基线漂移、堆积、噪声
- 支持 n/$\gamma$ 鉴别（Marrone et al., 2006b）和 Ba$F_{2}$ 本征 $\beta$ 本底抑制（Reifarth et al., 2004b）

[FACT] n_TOF 的数据采集系统：8-bit FADC，采样率高达 **2 GHz**，每脉冲 8–16 MB 内存；峰值 8 MB/检测器/脉冲；0.4 Hz 重复率留出充裕的数字化与存储时间。

[FACT] **主要困难**：数据量巨大（TB 量级），需要大容量存储与高传输率。

### 2.2.5 激活法（Activation method）

[FACT] 激活法是 TOF 方法的**互补手段**：

$$ ^A_Z X + n \rightarrow ^{A+1}_Z X^* \xrightarrow{\beta^-} \text{放射性子核} $$

[FACT] 激活法的五大优势（原文逐条列出）：

1. **准恒星中子谱模拟**：实验室可用 ⁷Li(p,n)⁷Be、³H(p,n)³He、¹⁸O(p,n)¹⁸F 等反应模拟恒星中子能谱，MACS 可**直接在实验室测量**
2. **技术简单**：在小型静电加速器上即可进行
3. **灵敏度极高**：比 TOF 高几个数量级——因为可用 DC 模式、样品紧贴靶
4. **适合小样品**：sub-μg 样品、放射性同位素
5. **信号-本底比好**：放射性衰变产物特征明确，可同时研究多个反应

[FACT] 三种可模拟恒星能谱的反应：

| 反应 | 有效温度 kT | 对应 s 过程 | 中子强度（100 μA） |
|---|---|---|---|
| ⁷Li(p,n)⁷Be | 25 keV | ²²Ne($\alpha$,n)，AGB 23 keV | $10^9$ s⁻¹ |
| ³H(p,n)³He | 52 keV | 大质量星 C 壳层 90 keV（需外推） | $10^8$ s⁻¹ |
| ¹⁸O(p,n)¹⁸F | 5 keV | ¹²C($\alpha$,n)，AGB 8 keV | $10^5$ s⁻¹ |

[FACT] **激活法 vs TOF 的互补性（Table II）**：

- Fe 组元素（共振主导的小截面）：激活法更准确
- 重核（平滑截面）：TOF 通常更准确
- 无普适规则——8⁸Sr、¹⁹⁷Au 等反例

### 2.2.6 关键案例——Fe 到 Nb 的丰度修订

[FACT] 图 4 展示了 25 M☉ 大质量星壳层 C 燃烧后的 s 过程产额（Fe 到 Nb），对比新截面（Heil et al., 2008a,b）与旧截面（Bao et al., 2000）：

- **新截面显著更小**，表明旧 TOF 数据被中子灵敏度问题高估
- 截面修订在 C 壳层燃烧（$kT=90$ keV）高温阶段有强烈传播效应
- 这一修订影响整个银河系化学演化模型中的 weak s 成分

### 2.2.7 分支点与放射性同位素

[FACT] **分支点概念**（Ward et al., 1976）：当 $n_n\langle\bar{\sigma}v\rangle \approx \lambda_\beta$ 时，反应流在中子俘获与 $\beta$ 衰变之间分流。

[FACT] 重要的分支点：

| 分支点核 | 半衰期 | 对应 s-only 对 |
|---|---|---|
| ⁷⁹Se | $3.2\times10^5$ yr（地球）/ 恒星条件剧减 | ⁸⁰,⁸²Kr |
| ⁸⁵Kr | 10.7 yr | ⁸⁶,⁸⁷Sr |
| ¹²³Te | $1.5\times10^5$ yr | ¹²²,¹²⁴Te |
| ¹⁴⁸Pm | 5.37 d | ¹⁴⁸,¹⁵⁰Sm |
| ¹⁵¹Sm | 90 yr | ¹⁵¹Eu / ¹⁵²Sm |
| ¹⁷⁶Lu | 37.5 Gyr（基态） | ¹⁷⁶Hf |
| ¹⁸⁵W | 75.1 万 yr | ¹⁸⁶W / ¹⁸⁶Re |

[FACT] **151Sm 是半衰期 <100 yr 的分支点中唯一用 TOF 测得 MACS 的案例**（Wisshak et al., 2006c；Abbondanno et al., 2004a）。

[FACT] **60Fe**：仅 1.4 μg 样品、半衰期 6 min、截面 5.7 mb，需要 47 次重复辐照；MACS 测量成功（Uberseder et al., 2009）。

[FACT] **147Pm**：仅 28 ng（$1.1\times10^{14}$ 原子）样品、半衰期 2.6 yr（Reifarth et al., 2003）。

### 2.2.8 间接方法

[FACT] 对不稳定性核素，直接 (n,$\gamma$) 实验不可行，有以下间接途径：

- **($\alpha$,n) 逆反应 + 详细平衡（detailed balance）**：$^{185}{\rm W}(\alpha,n)^{188}{\rm Os}$
- **Surrogate 方法**（Escher et al., 2005）：利用复合核形成与衰变的独立性，通过替代直接反应产生复合核
- 关键挑战：**J 布居失配**（不同复合态布居）、预平衡反应、束流碎裂

## 2.3 关键公式

### 2.3.1 Maxwellian 平均截面（MACS）

[FACT] 中子在稠密恒星等离子体中迅速热化，能量分布为 Maxwell-Boltzmann 谱：

$$ \bar{v}\Phi(E_n) \propto E_n \exp\left(-\frac{E_n}{kT}\right) $$

[FACT] **Maxwellian 平均截面定义**（原文 Eq. 3）：

$$ \langle\bar{\sigma}\rangle_{kT} = \sqrt{\frac{2}{\pi}} \frac{\displaystyle\int_0^\infty \sigma(E_n)\, E_n\, e^{-E_n/kT}\, dE_n}{\displaystyle\int_0^\infty E_n\, e^{-E_n/kT}\, dE_n} $$

- 分母 = $(kT)^2$
- **物理意义**：实验中测量的 $\sigma(E_n)$ 按恒星中子谱 $E_n e^{-E_n/kT}$ 加权平均
- **对数表示**：$\langle\bar{\sigma}\rangle \propto 10^{\langle a \rangle}$，其中 $\langle a \rangle$ 是截面参数的平均

### 2.3.2 反应流（quasi-equilibrium）

[FACT] 经典模型中，在反应流平衡区间的 s 过程丰度（原文 Eq. 5）：

$$ \langle\bar{\sigma}\rangle_i N_{s,i} = {}^{56}{\rm Fe}_{\odot}\, f\, \rho_0\, \left(1 + \frac{\rho_0}{\langle\bar{\sigma}\rangle_i}\right)^{-1} $$

其中：
- $f$：被辐照的 $^{56}{\rm Fe}$ 分数（经验参数 $f \approx 0.04\%$）
- $\rho_0$：总中子暴露（平均 $15$ n/种子）
- $\langle\bar{\sigma}\rangle_i$：第 $i$ 个核素的 MACS

[FACT] 在 $\langle\bar{\sigma}\rangle_i \gg \rho_0$（远离 magic numbers）：$\langle\bar{\sigma}\rangle_i N_{s,i} \approx$ 常数
[FACT] 在 $\langle\bar{\sigma}\rangle_i \ll \rho_0$（magic numbers）：$N_{s,i} \approx {}^{56}{\rm Fe}_{\odot}\, f\, \rho_0$（饱和）

### 2.3.3 分叉比（Branching ratio）

[FACT] 分支点的丰度比直接反映中子密度（Table I 中列出）：

$$ B = \frac{\langle\bar{\sigma}\rangle_p N_p}{\langle\bar{\sigma}\rangle_f N_f} $$

- $p$：被部分绕过的同位素
- $f$：经历完整反应流的同位素

| s-only 对 | $\langle\bar{\sigma}\rangle$ (mb) | 丰度比 | 分支比 |
|---|---|---|---|
| ⁸⁰,⁸²Kr | 267 ± 14 / 90 ± 6 | 2.28 : 11.58 | 0.61 ± 0.05 |
| ¹²²,¹²⁴Te | 295 ± 3 / 155 ± 2 | 2.55 : 4.74 | 1.06 ± 0.02 |
| ¹²⁸,¹³⁰Xe | 262.5 ± 3.7 / 132.0 ± 2.1 | 1.92 : 4.08 | 0.96 ± 0.02 |
| ¹³⁴,¹³⁶Ba | 176.0 ± 5.6 / 61.2 ± 2.0 | 2.417 : 7.854 | 0.94 ± 0.04 |
| ¹⁴⁸,¹⁵⁰Sm | 241 ± 2 / 422 ± 4 | 11.24 : 7.38 | 0.88 ± 0.01 |

### 2.3.4 恒星增强因子（SEF）

[FACT] 当核素在恒星温度下被激发到激发态时，MACS 需要修正：

$$ {\rm SEF} = \frac{\langle\bar{\sigma}\rangle^*}{\langle\bar{\sigma}\rangle_{\rm lab}} $$

- $\langle\bar{\sigma}\rangle^*$：对热布居的激发态取平均的 MACS
- $\langle\bar{\sigma}\rangle_{\rm lab}$：实验室测量的基态 MACS

[FACT] SEF 的典型值：
- **主 s 过程**（AGB 星）：SEF < 10%
- **大质量星 C 壳层燃烧**：SEF > 40%，特别是重奇质量数核

[FACT] **¹⁸⁷Os 关键案例**：$kT=30$ keV 时只有 30% 布居基态，70% 在激发态（其中 47% 在第一激发态 9.75 keV）；SEF 修正对 Re/Os 核宇宙年代学至关重要。

### 2.3.5 中子俘获率

[FACT] 中子俘获率公式：

$$ \lambda_{n\gamma} = n_n \langle\bar{\sigma}v\rangle = n_n\, \bar{v}\, \langle\bar{\sigma}\rangle_{kT} $$

其中：
- $n_n$：中子密度
- $\bar{v}$：平均热速度
- $\langle\bar{\sigma}\rangle_{kT}$：Maxwellian 平均截面

[FACT] 与 $\beta$ 衰变率的竞争：

$$ \text{分支条件} \Longleftrightarrow n_n \langle\bar{\sigma}v\rangle \approx \lambda_\beta^* = \frac{\ln 2}{t_{1/2}^*} $$

$t_{1/2}^*$ 是恒星条件下的有效半衰期。

### 2.3.6 分支点对丰度比

[FACT] s-only 核素的丰度比在分支点两侧被分叉：

$$ \frac{N_p}{N_f} = \frac{\langle\bar{\sigma}\rangle_f}{\langle\bar{\sigma}\rangle_p} \cdot \left(1 - B\right) $$

## 2.4 关键参数

| 参数 | 数值 | 备注 |
|---|---|---|
| 主 s 过程有效温度 | $kT = 8–25$ keV | AGB 星 ¹²C($\alpha$,n)¹⁶O 源 |
| Weak s 过程 Core He 燃烧 | $kT = 26$ keV | 大质量星 |
| Weak s 过程 Shell C 燃烧 | $kT = 90$ keV | 大质量星 |
| 截面测量精度目标 | 1–5% | 目前已在部分核素实现 |
| 分支比精度（Table I） | 1–8% | 主要受 MACS 精度限制 |
| SEF 主 s 过程 | < 10% | AGB 星温度 |
| SEF C 壳层燃烧 | > 40% | 大质量星 |
| n_TOF 中子强度 | 300 n/质子 | 20 GeV 质子束 |
| n_TOF 飞行路径 | 185 m | 高能量分辨率 |
| DANCE 模块数 | 162 个 Ba$F_{2}$ | LANSCE |
| PHWT 系统误差 | < 2% | 最新水平 |
| ¹⁸⁷Os 第一激发态 | 9.75 keV | 47% 布居 |
| ⁶⁰Fe 截面 | 5.7 mb | 样品 1.4 μg |
| ¹⁴⁷Pm 样品 | 28 ng | 半衰期 2.6 yr |
| 6LiH 吸收壳抑制 | 显著 | 散射本底抑制 |
| 56Fe 辐照分数 | 0.04% | 经典模型 |
| 平均中子暴露 | 15 n/种子 | 经典模型 |

## 2.5 图表分析

### Figure 3 — 铋的 R-矩阵分析

**1. 目的**：展示 ²⁰⁹Bi 第二共振的 R-矩阵拟合，揭示先前数据中的中子灵敏度假性贡献。

**2. 坐标轴**：横轴为入射中子能量 $E_n$（keV），纵轴为共振产额（Yield）。

**3. 图中元素**：
- 数据点：实验产额
- 虚线：用 ENDF/B-VI.8 参数计算的产额（反映中子灵敏度影响）
- 实线：修正后的 R-矩阵拟合

**4. 关键观察**：修正后产额**显著低于**先前数据，证明中子散射本底被严重高估。

**5. 物理意义**：²⁰⁹Bi 是 s 过程的最后一个 s-only 核素，其截面精度直接影响 r-residual 方法得到的 r 过程分布。

### Figure 4 — 新截面下的 25 M☉ 恒星 s 产额

**1. 目的**：展示 new vs old (Bao et al., 2000) 截面在 25 M☉ 大质量星 shell C 燃烧后 s 过程产额（Fe–Nb）的差异。

**2. 坐标轴**：横轴为质量数 $A$，纵轴为新截面产额 / 旧截面产额。

**3. 关键观察**：
- **多数核素 < 1**：新截面比旧截面小
- **²⁰Ne → ⁹⁰Zr → ⁹⁸Mo 区间**：差异最大
- **误差带（虚线）**：来自 MACS 从 $kT=25$ keV 到 $kT=90$ keV 的外推

**4. 物理意义**：旧 TOF 数据被中子灵敏度问题系统性地高估，**weak s 产额需要整体下调**。这直接影响银河系化学演化中的 weak s 贡献。

### Figure 5 — 反应流平衡的示例

**1. 目的**：展示在经典模型中，$\langle\bar{\sigma}\rangle N_s$ 在 magic numbers 附近形成明显的阶梯（steps）。

**2. 坐标轴**：横轴 $A$，纵轴 $\langle\bar{\sigma}\rangle N_s$。

**3. 关键观察**：
- $A \approx 88, 140, 208$ 处的 magic neutron numbers（$N=50, 82, 126$）形成截面瓶颈
- 在 magic numbers 之间的区间，反应流接近平衡（常数）

**4. 作者的解释**：$\langle\bar{\sigma}\rangle N_s$ 曲线在 magic numbers 之间的平台是反应流达到平衡的直接证据。

### Figure 6 — 恒星 (n,$\gamma$) 截面的当前精度

**1. 目的**：展示 s 过程相关核素截面的当前不确定度。

**2. 坐标轴**：横轴 $A$，纵轴为相对不确定度（%）。

**3. 关键观察**：
- **$A=90–180$ 区间**：精度已达 1–5%（目标水平）
- **$A < 120$ 和 $A > 180$ 区间**：精度不足，仍需改进
- 数据基于 $kT = 30$ keV；其他温度需要外推，不确定度更大

**4. 物理意义**：Fe–Sr 区域（weak s）和重核区域的截面精度仍是未来实验的重点。

### Table I — s-only 核素对的分支比

**1. 目的**：通过 s-only 对给出 s 过程分支比的实验值。

**2. 列**：s-only 核素对、Maxwellian 平均截面（mb）、丰度比、分支比。

**3. 关键数值**（见 §2.3.3 公式表）。

## 2.6 作者的逻辑

[FACT] §II 的论证链：

```
s 过程建模需要完整的 (n,$\gamma$) 截面数据
  → 但实验不可能覆盖所有核素和能量
    → 因此必须发展多种实验方法（TOF / 激活法 / 4$\pi$ 量热 / PHWT）
      → 并对无法实验测量的核素发展理论计算（Hauser-Feshbach 统计模型）
        → 理论需要实验校准
          → 且必须将实验室基态测量修正到恒星激发态布居（SEF）
            → 最终形成 KADONIS 截面库（当前标准）
              → 剩余问题：不稳定核素、中子源反应、弱 s 过程重核
```

[FACT] 实验与理论的互锁关系是 §II 的核心逻辑：**实验精度提升揭示理论计算的系统性偏差；理论计算填补实验空白；二者不断迭代。**

## 2.7 我的理解

[INTERPRETATION] §II 最重要的认识是：**s 过程核物理不是单一学科的课题，而是"核物理实验 + 核结构理论 + 天体物理"三者紧密结合的范例**。

[INTERPRETATION] 三种实验方法（TOF / 4$\pi$ 量热 / 激活法）形成完整的互补体系：

- **TOF**：全能量覆盖、适合稳定核、精度 2–5%、需要大量样品
- **4$\pi$ 量热**：高灵敏度、适合分支点研究、Ba$F_{2}$ 阵列
- **激活法**：直接测 MACS、灵敏度最高（sub-μg）、适合不稳定核

[INTERPRETATION] **分支点是 s 过程的"温度计"**：分支比直接反映中子密度；不同分支点对不同中子密度区间敏感。这一诊断工具的物理基础是分支点核的半衰期与中子俘获率的竞争。

[CRITIQUE] **SEF 的精度风险**：原文说 SEF 在主 s 过程 <10%，但 ¹⁸⁷Os 案例说明**个别核素的 SEF 可以远超平均值**——¹⁸⁷Os 在 $kT=30$ keV 时只有 30% 布居基态。如果统计模型对低能激发态的布居预测不准，SEF 修正可能引入 >10% 的系统误差。

[CRITIQUE] **C 壳层燃烧 $kT=90$ keV 时的外推问题**：实验室最接近的模拟谱是 ³H(p,n)³He 的 52 keV；从 52 keV 到 90 keV 的外推完全依赖统计模型计算，这是 **weak s 过程丰度预测的最大不确定性来源**。

[CRITIQUE] **KADONIS 的版本管理**：Bao et al. (2000) 是第三版，V0.3 (Dillmann et al., 2009) 已是第三更新；未来版本会包含新测量的截面。使用 KADONIS 时需注意版本号，不同版本可能给出不同的推荐值。

## 2.8 潜在问题与值得关注的地方

### 8.1 中子灵敏度问题的系统性影响

[CRITIQUE] Ba$F_{2}$ 晶体的中子散射本底问题在 ²⁰⁹Bi、²⁰⁸Pb、⁹⁰Zr、¹³⁹La 等**中子魔法核**上表现最严重——它们的俘获-散射比极低。这意味着所有涉及中子魔法核的早期 TOF 数据都可能被高估，需要系统性地重新评估。

### 8.2 ¹³C($\alpha$,n) 和 ²²Ne($\alpha$,n) 中子源反应

[CRITIQUE] 这两个中子源反应本身在 Gamow 窗口（低能端）的截面**至今没有直接测量**。当前使用的是统计模型外推 + 高能端测量锚定，存在 ~30% 的系统误差。**这是整个 s 过程建模中最大的核物理不确定度**——因为中子源直接决定中子产量，而中子产量决定 s 过程效率。

### 8.3 Weak s 过程的截面不确定性传播

[CRITIQUE] 原文强调（§II.D.1）：**weak s 过程没有达到反应流平衡**，因此某个 MACS 的误差不仅影响该核素的丰度，还**沿整个反应链向更重的核素传播**。图 4 中 Fe 到 Nb 的系统性偏差就是这一传播效应的直接证据。

### 8.4 放射性同位素测定的瓶颈

[CRITIQUE] §II.D.2 指出，许多关键分支点核素无法用 TOF 或激活法测量，因为：
- 样品放射性太高（如 ⁷⁹Se）
- 样品量太少（如 ¹⁵¹Sm，丰度 <0.2%）
- 同位素富集技术不成熟

### 8.5 间接方法的理论依赖

[CRITIQUE] ($\alpha$,n) 逆反应和 surrogate 方法都**严重依赖理论假设**（光学势、复合核形成/衰变独立性、J 布居），因此精度天然低于直接测量。它们的价值在于提供"其他方法都做不到"的信息，而非高精度。

---

## §II 章节元数据

```yaml
---
chapter: 2
title: 'Nuclear Physics'
source_page: '159–166'
parent_doc: '0017_kaeppeler-2011'
parent_title: 'The s process: Nuclear physics, stellar models, and observations'
parent_authors: 'Kappeler, Gallino, Bisterzo, Aoki'
parent_year: 2011
parent_journal: 'Rev. Mod. Phys. 83, 157'
parent_doi: '10.1103/RevModPhys.83.157'
summary: '中子俘获截面测量与计算、Maxwellian 平均截面、恒星增强因子、分支点、β 衰变修正'
key_figures:
  - 'Fig. 3: 209Bi R-矩阵分析'
  - 'Fig. 4: 新 vs 旧截面下的 s 过程产额'
  - 'Fig. 5: 反应流平衡示例'
  - 'Fig. 6: 恒星 (n,gamma) 截面不确定度'
key_tables:
  - 'Table I: s-only 核素对的分支比'
  - 'Table II: TOF 与激活法 MACS 对比'
  - 'Table III: 重要分支点核素列表'
key_equations:
  - 'MACS 定义 (Eq. 3)'
  - '反应流 (Eq. 5)'
  - '分支比 B'
  - '恒星增强因子 SEF'
  - '中子俘获率 lambda_{ngamma}'
key_topics:
  - '脉动中子源（小型加速器 / 直线加速器 / 散裂源）'
  - 'TOF 与激活法'
  - '4$\pi$ 量热与 PHWT 探测器'
  - 'Hauser-Feshbach 统计模型'
  - 'Maxwellian 平均截面'
  - '恒星增强因子'
  - '分支点与放射性同位素'
  - 'KADONIS 截面库'
next_chapter: '03_stellar_models.md'
prev_chapter: '01_introduction.md'
---
```
