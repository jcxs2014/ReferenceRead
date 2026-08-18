> 本章属于：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/00_overview.md|Particle Acceleration by Astrophysical Shocks（Blandford & Ostriker 1978）]]
>
> 上一章：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/02_strong_shock_acceleration.md|02_strong_shock_acceleration]]
>
> 下一章：[[02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/04_extragalactic_radio_sources.md|04_extragalactic_radio_sources]]
>
> 总览：`00_overview.md`

# 3. Acceleration of Cosmic Rays — 超新星遗迹中的宇宙线加速

## 3.1 本节核心内容

BO 在 §III 中将 §II 的理论应用到**银河系超新星遗迹（SNR）**，论证：

1. **Adiabatic decompression 问题如何规避**：此前方案（Kulsrud & Zweibel 1975）指出，直接关联于超新星的加速过程会面临灾难性绝热膨胀——SNR 膨胀时粒子能量 $\propto 1/R$ 衰减。BO 的方案中粒子被散射在激波附近反复穿越，不直接"跟随"膨胀气体，从而规避此问题。
2. **Alfvén 波自激发的可行性**：宇宙线 streaming 产生的 Alfvén 波能否提供 §II 所需的散射？
3. **能量可行性**：单次穿越是否足以解释已知宇宙线能量？
4. **谱指数修正**：为什么观测到 $s \approx 4.5$ 而非 $4$？
5. **高能截断**：最高能宇宙线能否在 SNR 中加速到 $10^{18}$ eV？

## 3.2 原文内容

### 3.2.1 规避绝热膨胀问题

Kulsrud & Zweibel (1975) 指出，直接关联于超新星的加速过程会导致粒子能量在 SNR 膨胀过程中大幅衰减。BO 的方案中，粒子被 Alfvén 波散射困在激波附近，反复穿越激波——这一过程是**局部的**，不依赖于 SNR 的整体膨胀，因此不受绝热膨胀影响。

### 3.2.2 Alfvén 波自激发

宇宙线以超过 Alfvén 速度的速度在背景介质中 streaming 时，会激发 Alfvén 波（Kulsrud & Pearce 1969）：

$$\nu_{\rm growth} \propto n_p \, c \, p^{1/2} \, \epsilon^{-1} \, R^{-1}$$

其中 $n_p$ 为动量大于 $p$ 的宇宙线数密度，$\epsilon$ 为背景介质密度，$R$ 为 SNR 半径。

**条件**：增长率 $\gamma_{\rm growth} > u_-/R$（即波增长率快于 SNR 膨胀率）时，自激发成立。

### 3.2.3 能量可行性

BO 给出简洁的能量估算：

$$E_{\rm injected} = \varepsilon V_{\rm cool} w_{\rm cr} \approx 10^{50} \text{ erg SN}^{-1}$$

对于超新星率 $\dot{n}_{\rm SN} \approx 10^{-18} \text{ cm}^{-3} \text{ yr}^{-1}$（即每 60 年一次），注入率：

$$\dot{E} \approx 10^{-18} \text{ erg cm}^{-3} \text{ yr}^{-1}$$

与已知宇宙线能量密度 $w_{\rm cr} \approx 10^{-12} \text{ erg cm}^{-3}$ 对比，加速时间尺度 $\sim 10^6$ yr——与银河系宇宙线停留时间相当。

### 3.2.4 谱指数修正

理想强激波 $r = 4$ 给出 $s = 4$，观测约 $4.5$。BO 给出两个修正机制：

1. **效率损失**：当激波逐渐变为 Alfvénic 时，一部分原本注入 CR 的能量被 Alfvén 波带走（损失率 $\sim w/u_-$）。
2. **压缩比降低**：激波变 Alfvénic 后，$r < 4$，谱变陡。

设 $s = 4.5$，对应 $r = 3$，则：

$$q = \frac{3 \times 3}{3 - 1} = 4.5$$

CR 能量密度增幅 $\sim 2$，可补偿绝热膨胀损失。

### 3.2.5 高能截断

粒子 Larmor 半径超过 SNR 半径时逃逸：

$$r_L \approx R \implies E_{\rm max} \sim 10^{18} \text{ eV}$$

因此 SNR 中 DSA **无法加速到 $10^{18}$ eV 以上**，无法解释 UHECR。

## 3.3 关键公式

### 自激发增长率

$$\gamma_{\rm growth} \propto n_p \, c \, p^{1/2} \, \epsilon^{-1} \, R^{-1}$$

### 能量注入

$$E_{\rm injected} = \varepsilon \cdot V_{\rm cool} \cdot w_{\rm cr} \approx 10^{50} \text{ erg}$$

### 加速时间

$$t_{\rm acc} = \frac{w_{\rm cr}}{\dot{E}} \sim 10^6 \text{ yr}$$

### 高能截断

$$r_L = \frac{pc}{ZeB} \approx R_{\rm SNR} \implies E_{\rm max} \sim 10^{18} \text{ eV}$$

### 谱指数修正

$$s = \frac{3r}{r-1} = 4.5 \implies r = 3$$

## 3.4 关键参数

| 参数 | 值 | 来源 |
|---|---|---|
| SNR 半径（Alfvénic 转变前） | $R > 100$ pc | 估算 |
| 超新星率 | $10^{-18} \text{ cm}^{-3} \text{ yr}^{-1}$ | 银河系 |
| Alfvén 速度 | $50 \text{ km s}^{-1}$ | ISM |
| 高能截断 | $\sim 10^{18}$ eV | $r_L = R$ |
| 自激发适用上限 | $\sim 300$ GeV | 低密度 ISM |
| CR 能量密度 | $10^{-12} \text{ erg cm}^{-3}$ | 观测 |
| 电子/质子比 | $\sim 0.03$（3 GeV 处）| Wentzel 1974 |

## 3.5 图表分析

本文无 Figure。

## 3.6 作者的逻辑

```
§II 给出普适机制（DSA + 幂律谱）
→ §III 应用到 SNR
→ 问题：Alfvén 波来自哪里？→ streaming 自激发
→ 问题：能量够吗？→ $10^{50}$ erg/SN 足够
→ 问题：为什么观测 s=4.5 而非 4？→ 激波变 Alfvénic + r 降低
→ 问题：能加速到多高？→ ~$10^{18}$ eV（SNR 尺度）
→ 结论：SNR DSA 可解释银河系宇宙线（至膝点）
```

## 3.7 我的理解

> **分析 / Interpretation**：§III 的论证结构是"可行性论证"——每个潜在问题都被单独处理，给出数值估算。BO 没有给出完整数值模拟（他们引用"will be described elsewhere"），但在 4 页内完成了所有关键论证，效率极高。

### 与 Bell 1978 的差异

Bell 1978 的 §2（Particle Acceleration at a Shock Front）给出了完整的测试粒子处理，包括分布函数的具体形式和能量损失的讨论。BO 的 §II 更简洁，侧重于物理图像而非数学完整；§III 则给出了 Bell 没有的"自激发"论证和能量估算。

> **分析 / Interpretation**：两篇论文互为补充——Bell 提供完整理论框架，BO 提供应用可行性论证。

## 3.8 潜在问题与值得关注的地方

1. **自激发的适用能量范围**：BO 指出自激发 Alfvén 波在低密度 ISM 中只对 $\lesssim 300$ GeV 的粒子有效。更高能粒子需要预存湍流或 Wentzel (1977) 提出的相位各向异性机制。这是一个**重要的未解决问题**。

2. **电子/质子比的解释**：BO 假设电子和质子的动量分布有相同的谱指数 $s \approx 4.5$，通过 equipartition 解释观测到的 $e^-/p^+ \sim 0.03$。这个假设需要更仔细的处理。

3. **最高能宇宙线的来源**：$10^{18}$ eV 以上 SNR DSA 无法加速，必须另有机制——BO 当时尚未讨论 UHECR 的候选源（AGN、GRB 等）。

## 3.9 [FACT]/[INTERPRETATION]/[CRITIQUE] 标注

**[FACT]** §III 的能量可行性论证（BO Eq. 9–12）：SNR 动能 $10^{51}$ erg 中 $10\%$ 转化为 CR 能量 → $10^{50}$ erg / 粒子平均能量 $10^{14}$ eV → $10^{54}$ 个粒子/m³（银河系总 CR 能量 $10^{39}$ erg 需要 $10^{45}$ 个粒子）。原文 Eq. 11 的 $n_{\rm CR} \sim 10^{-10}$ cm$^{-3}$ 是正确的量级估算。[FACT]

**[INTERPRETATION]** §III 的 10% 效率估算存在假设依赖性：原文 Eq. 10 取 $V_{\rm SNR} \sim 10^{57}$ cm³（Sedov 阶段），但 Eiley 阶段的 SNR 体积小 100 倍。若 CR 加速主要发生在 Eiley 阶段，则 $10\%$ 效率要求可能更易满足（或更难——取决于早期密度）。[INTERPRETATION]

**[CRITIQUE]** §III 对 SNR 作为 CR 唯一源的论证依赖一个隐含假设：SNR 的每次爆发都贡献相似能量。但实际上 Core-collapse SN（Type Ib/Ic/II）和 Type Ia 的动力学环境差异巨大（wind bubble vs uniform ISM），加速效率可能差异 10 倍以上。BO 的"平均 10%"是一个过于简化的处理，忽略了 SN 类型的分散性。[CRITIQUE]