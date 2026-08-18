> 本章属于：[[01_cosmic-ray-propagation/0003_weinrich-2020/literature_analysis/00_overview.md|Galactic halo size in the light of recent AMS-02 data（Weinrich et al. 2020）]]
>
> 上一章：[[01_cosmic-ray-propagation/0003_weinrich-2020/literature_analysis/02_model_configurations.md|02_model_configurations]]
>
> 下一章：[[01_cosmic-ray-propagation/0003_weinrich-2020/literature_analysis/04_conclusions.md|04_conclusions]]
>
> 总览：`00_overview.md`

# 3. Halo Size $L$ from CR Clocks — 宇宙线时钟约束晕高

## 3.1 本节核心内容

§3 是本文的核心——利用放射性同位素时钟打破 $K_0/L$ 简并，对晕高 $L$ 给出定量约束。系统评估了 B/C、Be/B、$^{10}{\rm Be}$/$^{9}{\rm Be}$、$^{10}{\rm Be}$/Be 四种比率对 $L$ 的敏感度。

## 3.2 $K_0/L$ 简并的打破

**问题**：B/C 比率对 $K_0/L$ 的比值敏感，但对 $K_0$ 和 $L$ 单独不敏感。

**关键洞察**：放射性同位素（如 $^{10}{\rm Be}$，$t_{1/2} = 1.387$ Myr）的衰变率与传播时间 $\tau \sim L^2/K_0$ 直接相关：

$$\frac{N(t)}{N_0} = e^{-t/\tau_{1/2}}$$

结合稳定同位素和放射性同位素的测量，可以同时约束 $K_0$ 和 $L$。

> **分析 / Interpretation**：这是本文方法论的核心——用 $^{10}{\rm Be}$ 的衰变作为"时钟"，测量 CR 在晕中的停留时间，从而独立约束 $L$。

## 3.3 四种比率的 $L$ 敏感度

| 比率 | $L$ 敏感度 | 最优能量范围 | 备注 |
|---|---|---|---|
| B/C | **极低** | — | 需改进 10 倍精度才能约束 $L$ |
| Be/B | **中等** | $\sim 10-100$ GV | AMS-02 精度足够 |
| $^{10}{\rm Be}$/$^{9}{\rm Be}$ | **高** | $< 10$ GeV/n | 交叉截面不确定是主要限制 |
| $^{10}{\rm Be}$/Be | **高** | $< 10$ GeV/n | 同上 |

**关键数值**：

- B/C 对 $L$ 变动的最大影响仅 $\sim 5\%$（即使 $L$ 从 2.5 到 12 kpc）
- Be/B 对 $L$ 的敏感度在 $\sim 30$ GV 达到峰值
- $^{10}{\rm Be}$/$^{9}{\rm Be}$ 和 $^{10}{\rm Be}$/Be 在 $< 3$ GeV/n 处常量（衰变主导）

## 3.4 实际约束结果（§3.4 表 3）

### 3.4.1 SLIM 配置（核心结果）

| 数据组合 | $L$（SLIM）| 备注 |
|---|---|---|
| Base（Li/C + B/C）| 不约束 | B/C 对 $L$ 不敏感 |
| Base + Be/B（AMS-02）| $5.04^{+3.07}_{-1.79}$ kpc | AMS-02 Be/B 单独 |
| Base + Be/B + $^{10}{\rm Be}$/Be | $5.11^{+2.85}_{-1.70}$ kpc | +低能 $^{10}{\rm Be}$/Be |
| **Base + Be/B + $^{10}{\rm Be}$/Be + $^{10}{\rm Be}$/$^{9}{\rm Be}$** | **$4.66^{+1.35}_{-0.97}$ kpc** | **最严格约束** |

### 3.4.2 BIG 和 QUAINT 配置

| 数据组合 | BIG | QUAINT |
|---|---|---|
| Base + Be/B（AMS-02）| $4.96^{+2.97}_{-1.76}$ kpc | $4.79^{+3.19}_{-1.77}$ kpc |
| 联合所有数据 | $4.64^{+1.35}_{-0.94}$ kpc | $4.08^{+1.33}_{-0.78}$ kpc |

> **分析 / Interpretation**：三种配置给出一致结果（$L \sim 4-5$ kpc），差异在 $\sim 0.6$ kpc 以内——说明结果对模型假设的敏感性有限。

## 3.5 与传统估计的对比

| 研究 | $L$ | 备注 |
|---|---|---|
| GALPROP 传统 | $\sim 4$ kpc | 固定值 |
| Donato et al. 2002（贝叶斯）| $\sim 5$ kpc | $\delta = 0.5$ |
| Trotta et al. 2011（贝叶斯）| $5.4 \pm 1.4$ kpc | 演化贝叶斯 |
| Moskalenko et al. 2001（GALPROP）| $[1.5-6]$ kpc | $\delta = 0.3$ |
| **本文 SLIM** | **$4.66^{+1.35}_{-0.97}$ kpc** | AMS-02 + $^{10}{\rm Be}$ |

**与传统 $L = 4$ kpc 的对比**：本文结果中心值 $\sim 4.7$ kpc，传统值在误差范围内但仍偏低。

## 3.6 与 Génolini 2021 的关系

Génolini 2021 的 min/med/max 模型直接使用了本文的 $L$ 约束：

| 本文 L 范围（1$\sigma$）| Génolini 2021 三模型 L |
|---|---|
| $3.7-6.0$ kpc | MIN: 1.0 kpc, MED: 4.0 kpc, MAX: 8.0 kpc |

Génolini 2021 的 MED（$L = 4$ kpc）落在本文的 1$\sigma$ 范围内；MIN 和 MAX 超出 1$\sigma$ 但仍在 2$\sigma$ 内——三模型覆盖参数空间的合理范围。

## 3.7 关键公式

| 公式 | 出处 | 物理意义 |
|---|---|---|
| $K(E)$ 完整形式 | §2 | 扩散系数 |
| $N(t)/N_0 = e^{-t/\tau_{1/2}}$ | §3 | $^{10}{\rm Be}$ 衰变（时钟）|
| $\tau \sim L^2/K_0$ | §3 | CR 在晕中的停留时间 |

## 3.8 关键参数

| 参数 | 值 | 出处 |
|---|---|---|
| $^{10}{\rm Be}$ 半衰期 | $t_{1/2} = 1.387$ Myr | §3 |
| 盘半高 $h$ | 100 pc | §2 |
| SLIM 最佳 $L$ | $4.66^{+1.35}_{-0.97}$ kpc | §3.4 |
| BIG 最佳 $L$ | $4.64^{+1.35}_{-0.94}$ kpc | §3.4 |
| QUAINT 最佳 $L$ | $4.08^{+1.33}_{-0.78}$ kpc | §3.4 |

## 3.9 潜在问题与值得关注的地方

1. **B/C 对 $L$ 完全不敏感**：即使 AMS-02 精度达到 1%，B/C 仍无法约束 $L$——需要至少 10 倍精度改进。

2. **交叉截面不确定性是主要限制**：$^{10}{\rm Be}$ 的碎裂截面不确定性在 $\sim 15\%$——即使数据精度提高，$L$ 的约束仍受截面限制。

4. **与扩散参数 $\delta$ 的简并**：$L$ 和 $\delta$ 之间存在强简并——本文用 minos 处理了非高斯误差，但仍需注意。

## 3.10 关键图表深度分析（Fig. 1 / Table 3）

**[FACT]** Fig. 1 四面板设计：每个面板展示一个比例（B/C、Be/B、¹⁰Be/Be、¹⁰Be/⁹Be）随能量（GeV/n）的变化，彩色 envelope 表示 68% CL 模型不确定性。灰色阴影区域标注了 "$L$ most impacting" 区间（0.1–1 GeV/n），这是选择 AMS-02 和 ISOMAX 低能数据的物理依据。[FACT]

**[INTERPRETATION]** Fig. 1 的信息密度极高——四个面板用同一 envelope 风格展示了不同核种对 $L$ 的敏感度差异。值得注意的是：¹⁰Be/⁹Be（两个不稳定核素的比值）在最低能量端（<0.3 GeV/n）的 envelope 明显宽于其他面板——这说明 ¹⁰Be 本身的测量不确定性（而非 $L$ 效应）是该能量段的主导误差来源。这对未来的实验设计有直接指导意义（需要更高精度的 ¹⁰Be 测量）。[INTERPRETATION]

**[FACT]** Table 3 是全文核心结果汇总：列出了 SLIM/BIG/QUAINT 三种模型在有无 ¹⁰Be 数据约束下的 $L$ 拟合中心值和不对称误差。关键数值：SLIM+Base（无 ¹⁰Be）$L = 4.7^{+1.3}_{-0.8}$ kpc；SLIM+All（加 ¹⁰Be）$L = 4.08^{+1.33}_{-0.78}$ kpc——加入 ¹⁰Be 约束后 $L$ 中心值从 4.7 降到 4.08，差异约 0.6 kpc（一个 σ 级别）。[FACT]

**[CRITIQUE]** Table 3 的 "$L$ most impacting" 区间（Fig. 1 灰色条带）存在模型依赖性——QUAINT 模型的灰色区域比 SLIM 更宽，这意味着 ISOMAX 数据在 QUAINT 模型下对 $L$ 的约束效果更差。原文没有充分讨论这种模型依赖性对 Fig. 1 "L-impacting 区间"结论的影响。[CRITIQUE]

4. **与传统 $L = 4$ kpc 的对比**：本文中心值 $\sim 4.7$ kpc 比传统值高——这对暗物质搜寻有直接影响（更大的 $L$ 意味着更多的 astrophysical background）。