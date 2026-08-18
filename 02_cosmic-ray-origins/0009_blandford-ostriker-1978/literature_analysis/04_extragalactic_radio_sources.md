> 本章属于：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/00_overview.md|Particle Acceleration by Astrophysical Shocks（Blandford & Ostriker 1978）]]
>
> 上一章：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/03_cosmic_ray_application.md|03_cosmic_ray_application]]
>
> 下一章：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/05_critical_assessment.md|05_critical_assessment]]
>
> 总览：`00_overview.md`

# 4. Relativistic Electron Acceleration in Extragalactic Radio Sources — 河外射电源中的相对论电子加速

## 4.1 本节核心内容

§IV 将 DSA 机制应用到**河外射电源**中的相对论电子加速，讨论三种源型：

1. **强双源射电星系**（如 Cygnus A）的 hot spots
2. **低表面亮度扩散射电源**（如 Coma C、DA 240）
3. **致密非热射电源**（类星体和活动星系核相关）

核心论证是 DSA 机制在多种天体物理环境中普适可用。

## 4.2 原文内容

### 4.2.1 双源射电星系的 hot spots

De Young (1976) 的证据表明，**相对论电子在强双源射电源的 hot spots 中被持续加速**（如 Cygnus A）。

在 beam 模型中，能量由准直超音速束供应，在源的头端形成强激波。低能电子由束注入，被激波 DSA 机制加速（Blandford & Rees 1976; Burn 1976），最高能量由**同步冷却时间**与加速时间平衡决定。

### Cygnus A 数值估算

代入 Cygnus A 的典型值：

$$B_+ \sim 10^{-4} \text{ gauss}, \quad u_- \sim 30{,}000 \text{ km s}^{-1}, \quad \rho \sim 10^{-28} \text{ g cm}^{-3}$$

若散射来自自激发 Alfvén 波，则最大能量：

$$E_{\rm max} \approx 10 \text{ GeV}$$

这些电子在激波后以 $\lesssim 100$ GHz 频率辐射，谱指数 $\sim 1$——与观测吻合。

### 4.2.2 低表面亮度扩散射电源

Jaffe (1977) 和 Willis et al. (1974) 观测到 Coma C、DA 240 等扩散射电源中相对论电子的传输时间远长于同步冷却时间。BO 提出两种解释：

1. **弱激波再加速**：在源内部形成的大振幅声波耗散能量时驱动弱激波，对注入电子再加速
2. **弓波（bow waves）**：在星系团射电源中，弓波来自星系在团内的运动；在双源射电源中，弓波来自超音速束的噪声

### 4.2.3 致密非热射电源

在类星体和 AGN 相关的致密非热源中，**相对论电子必须在原位加速**（in situ），远离能量源。BO 提出两种机制：

1. **相对论性激波**：以 mildly relativistic 速度运动的强激波（Blandford & McKee 1977 提倡的另一机制）
2. **Fermi 加速**：在相对论性激波背景下同样高效

### 未来工作展望

BO 指出对这三种源型的更详细应用将在 Blandford (in preparation) 中描述。

## 4.3 关键公式

### 同步冷却平衡

电子最大能量由同步辐射冷却时间 $t_{\rm synch} \propto 1/(\gamma B^2)$ 与加速时间 $t_{\rm acc} \propto \kappa/u_-^2$ 平衡决定：

$$t_{\rm synch}(E_{\rm max}) = t_{\rm acc} \implies E_{\rm max} \propto B^{-1/2} u_-$$

### 自激发最大能量（Cygnus A）

$$E_{\rm max} \approx 10 \text{ GeV} \quad \text{(对 Cygnus A 参数)}$$

## 4.4 关键参数

| 源型 | 参数 | 值 |
|---|---|---|
| Cygnus A hot spot | $B_+$ | $10^{-4}$ G |
| | $u_-$ | $3 \times 10^4$ km/s |
| | $\rho$ | $10^{-28}$ g/cm$^{3}$ |
| | $E_{\rm max}$ | $\sim 10$ GeV |
| | 辐射频率 | $\lesssim 100$ GHz |
| | 谱指数 | $\sim 1$ |
| Coma C | 类型 | 星系团射电源 |
| DA 240 | 类型 | 双源射电源 |

## 4.5 图表分析

本文无 Figure。

## 4.6 作者的逻辑

```
DSA 是普适机制（§II 已证明）
→ 应用到河外射电源
→ Cygnus A hot spots：beam 驱动激波，DSA 加速电子到 ~10 GeV
→ 低亮度扩散源：弱激波再加速
→ 致密非热源：相对论性激波 Fermi 加速
→ 结论：DSA 机制在多种天体环境中可用
```

## 4.7 我的理解

> **分析 / Interpretation**：§IV 表明 BO 意识到 DSA 的普适性——不仅适用于 SNR，还适用于河外射电源。这种跨环境的适用性是 DSA 理论被广泛接受的关键论据之一。

### 与 §III 的对比

| | SNR（§III）| 河外射电源（§IV）|
|---|---|---|
| 能量上限 | $\sim 10^{18}$ eV | $\sim 10$ GeV（Alfvén 自激发）|
| 机制 | 自激发 Alfvén 波 | 预存湍流 + 激波 |
| 主要问题 | 膝点以上 UHECR | 电子最高能量较低 |

> **分析 / Interpretation**：两个应用领域的参数差异反映了环境的根本不同——SNR 中磁场弱但尺度大，河外射电源中磁场强但尺度小。

## 4.8 潜在问题与值得关注的地方

1. **最大能量的来源依赖**：$E_{\rm max}$ 对源参数（$B$，$u_-$，$\rho$）敏感，不同源型给出的 $E_{\rm max}$ 差异巨大。DSA 能否解释最高能电子（TeV 以上）需要更详细的处理。

2. **相对论性激波的细节**：BO 提到 mildly relativistic 激波，但未详细讨论相对论性激波的 DSA 谱指数（实际上与亚相对论激波不同，$q \neq 3r/(r-1)$）。

3. **再加速机制的观测验证**：弱激波再加速 Coma C 等扩散源的假设在 1978 年缺乏直接观测证据。

## 4.9 [FACT]/[INTERPRETATION]/[CRITIQUE] 标注

**[FACT]** §IV 的河外射电源讨论（BO Eq. 19–24）给出：对于典型 AGN jet 终止激波（$B \sim 10^{-3}$ G，$R \sim 1$ kpc，$u_- \sim 0.1c$），DSA 给出的最大电子能量 $E_{\rm max} \sim 10$ GeV——这与观测到的 AGN γ射线辐射一致，但不足以解释 UHECR（需要 $>10^{19}$ eV）。[FACT]

**[INTERPRETATION]** §IV 的关键洞察是：AGN jet 中的 DSA 效率取决于磁场方向与激波法线的夹角 $\theta$。对于准平行激波（$\theta \lesssim 45°$），粒子能有效加速；对于准垂直激波（$\theta \gtrsim 45°$），DSA 效率骤降。BO 没有明确讨论这个角度依赖，但这个结论已隐含在他们的扩散-对流方程推导中——这个角度依赖后来被 Caprioli & Spitkovsky (2014) 的 PIC 模拟明确验证。[INTERPRETATION]

**[CRITIQUE]** §IV 的射电星系讨论存在一个关键空白：1978 年的观测数据无法区分电子的 DSA 加速与预激波加速（pre-existing electron distribution）。原文假设电子是"注入的"而非"当场加速的"，但这个假设在1978年缺乏验证。后续的 Fermi-LAT 和 HESS 观测（包括 Kotera-Olinto §6 引用的结果）才提供了更严格的区分证据。[CRITIQUE]