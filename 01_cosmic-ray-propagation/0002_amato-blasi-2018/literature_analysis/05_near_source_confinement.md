> 本章属于：[[01_cosmic-ray-propagation/0002_amato-blasi-2018/literature_analysis/00_overview.md|Cosmic ray transport in the Galaxy: A review（Amato & Blasi 2018）]]
>
> 上一章：[[01_cosmic-ray-propagation/0002_amato-blasi-2018/literature_analysis/04_self_generated_transport.md|04_self_generated_transport]]
>
> 下一章：[[01_cosmic-ray-propagation/0002_amato-blasi-2018/literature_analysis/06_cr_induced_galactic_winds.md|06_cr_induced_galactic_winds]]
>
> 总览：`00_overview.md`

# 5. Near-Source Confinement — 源附近的传播

## 5.1 本节核心内容

§5 讨论 CR 在其**源附近**（$\sim 100$ pc）的传播——自生波在此处密度足够高，非线性效应主导，粒子被强烈禁闭。

关键结论：**源附近的自生波禁闭**可以贡献可观的碎裂克质量（$\Lambda_{\rm src} \sim 0.15$ g/cm$^{2}$），与传播途中的克质量可比——这对 B/C 比率的解释有重要影响。

## 5.2 自生波在源附近的增强

**物理基础**：

在源附近，CR 密度远高于银河系平均密度，因此：
- CR 密度大 → 自生波的生长率 $\gamma_{\rm CR} \propto J_{\rm CR}$ 高
- CR 梯度大 → 更有效的共振激波
- 自生波主导散射（而非背景湍流）

**结果**：源附近扩散系数 $D_{\rm sg}$ 远小于银河系平均扩散系数 $D_{\rm gal}$，粒子被**强烈禁闭**。

## 5.3 D'Angelo et al. (2016) 模型

D'Angelo et al. (2016) 系统研究了四种 ISM 相场景下源附近的自生波效应：

| 场景 | $n_n$ | $n_i$ | IND 效果 | 源附近克质量 |
|---|---|---|---|---|
| (1) 完全电离 | 0 | 0.45 cm$^{-3}$ | 无 | **$\sim 0.15$ g/cm$^{2}$**（最大值）|
| (2) 部分中性 | 0.05 cm$^{-3}$ | 0.45 cm$^{-3}$ | 部分抑制 | $\sim 0.1$ g/cm$^{2}$ |
| (3) 更多中性 | 0.03 cm$^{-3}$ | 0.45 cm$^{-3}$ | 显著抑制 | $\sim 0.05$ g/cm$^{2}$ |
| (4) 稀薄完全电离 | 0 | 0.01 cm$^{-3}$ | 无 | 小（密度低）|

**核心结论**：
- **无中性氢时**：自生波完全有效，CR 在源附近禁闭 $\sim 10$ Myr（100 pc 区域），源区克质量与传播克质量相当
- **有中性氢时**：IND 抑制自生波，禁闭减弱，源区克质量变得微不足道

> **分析 / Interpretation**：源区克质量的物理意义是——**如果存在**，意味着 B/C 比率中的部分二级粒子产生于源附近，而非传播途中。这将改变我们对碎裂截面的约束。

## 5.4 自生波禁闭时间

**停留时间**（在源附近 $L_c$ 尺度内）：

$$\tau_{\rm ss} \sim \frac{L_c^2}{D_{\rm sg}}$$

对比晕尺度停留时间：

$$\tau_H \sim \frac{H^2}{D_{\rm gal}}$$

如果 $\tau_{\rm ss} \gtrsim \tau_H \cdot (h_d/H) \sim 10^{-2} \tau_H$，则源附近积累的可观克质量与传播途中相当。

**AMS-02 观测约束**：

添加源区克质量 $\Lambda_{\rm src} \sim 0.15$ g/cm$^{2}$ 后，B/C 比率在**高刚度**（$> 100$ GV）处拟合更好——与 Aloisio et al. (2015) 的结果一致。

## 5.5 离子-中性阻尼（IND）的作用

IND 对自生波的抑制机制：

**阻尼率**：

$$\gamma_{\rm IND} \propto n_n \cdot v_{\rm drift}$$

其中 $n_n$ 是中性氢密度，$v_{\rm drift}$ 是离子-中性漂移速度。

**临界密度**：$n_n \sim 0.03$ cm$^{-3}$（Ferrière 1998 模型对 WIM 中残余中性的上限）。

> **分析 / Interpretation**：IND 的关键角色——它决定了**自生波是否能在源附近有效生长**。如果 ISM 大部分中性（如冷中性介质），自生波被抑制，源附近禁闭效应消失。

## 5.6 关键公式

| 公式 | 出处 | 物理意义 |
|---|---|---|
| $D_{\rm sg}(p) \propto p^2$（NLD 主导）| §4/§5 | 源附近扩散系数 |
| $\tau_{\rm ss} \sim L_c^2/D_{\rm sg}$ | §5 | 源附近停留时间 |
| $\Lambda_{\rm src} \sim 0.15$ g/cm$^{2}$ | §5 | 源区碎裂克质量（D'Angelo 2016）|
| $\gamma_{\rm IND} \propto n_n$ | §5 | IND 阻尼率 |
| $n_n \lesssim 0.03$ cm$^{-3}$ | §5 | WIM 中性氢上限 |

## 5.7 关键参数

| 参数 | 值 | 出处 |
|---|---|---|
| 源附近尺度 $L_c$ | $\sim 100$ pc | §5 |
| 源附近克质量 | $\sim 0.15$ g/cm$^{2}$ | §5（完全电离情形）|
| ISM 中性密度上限（WIM）| $\lesssim 0.03$ cm$^{-3}$ | §5 |
| WIM 温度 | $\sim 10^6$ K | §5 |
| 禁闭时间（完全电离）| $\sim 10$ Myr | §5 |

## 5.8 作者的逻辑

```
§4 建立银河系尺度自生波传播
→ §5 聚焦源附近（密度高，自生波更强）
→ 自生波主导散射 → D_sg ≪ D_gal
→ 粒子被禁闭在源附近 → 源区碎裂克质量
→ 源区克质量与传播克质量可比 → 影响 B/C 解释
→ IND 决定自生波能否生长（中性氢是关键）
```

## 5.9 潜在问题与值得关注的地方

1. **ISM 相的不确定性**：如果实际 ISM 中性成分比模型假设多，自生波效应被抑制，源区克质量不显著。

2. **$\Lambda_{\rm src} \sim 0.15$ g/cm$^{2}$ 的观测约束**：这个值需要与 B/C 高刚度数据仔细比对。

3. **SNR 膨胀效应**：CR 在 SNR 膨胀过程中被绝热损失——本文未详细处理，D'Angelo et al. (2016) 也未完全处理。