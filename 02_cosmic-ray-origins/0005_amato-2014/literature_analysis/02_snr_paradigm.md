# 2. SNR 范式的基础（Bases of the SNR Paradigm）

> 本章属于：The origin of galactic cosmic rays (Blasi 2013 §2)
>
> 上一章：[[02_cosmic-ray-origins/0005_amato-2014/literature_analysis/01_introduction.md|01_introduction.md]]
>
> 下一章：[[02_cosmic-ray-origins/0005_amato-2014/literature_analysis/03_test_particle_dsa.md|03_test_particle_dsa.md]]

## 2.1 核心逻辑

**[FACT]** Blasi §2 用一段"能量守恒 + 传播时标"的推理建立 SNR 范式：

1. **B/C 比 → 传播时标** → 支持"扩散传播"（diffusive propagation）假设；
2. **B/C 比 + 银河系几何 + CR 通量 → 单个 SN 需提供的加速效率 $\xi$_CR**；
3. 结论：**~5–10%** 的爆发动能必须转化为 CR 粒子 → SNR 加速机制必须是**非线性的**（test-particle 假设失效）。

## 2.2 B/C 比作为传播示踪（Blasi §2）

**[FACT]** 主要公式（Blasi 式 (1)）：

$$\tau_{esc}(E) = \frac{H^2}{D(E)} = \tau_* \left(\frac{E}{E_*}\right)^{-\delta}$$

其中：
- grammage $X(E) = \bar{n}\mu v \tau_{esc}(E)$
- 对 10 GeV/n 的粒子：$X \sim 10$ g/cm²
- 银河盘厚 $h = 150$ pc，晕高 $H$（典型 3 kpc）
- 平均密度 $\bar{n} \approx 5 \times 10^{-2} (H/3\,\mathrm{kpc})^{-1}$ cm⁻³
- 平均质量 $\mu \approx 1.4 m_p$（$n_{He} \approx 0.15 n_H$）

**[FACT]** 10 GeV 质子的典型逃逸时标（Blasi 式 (1)）：

$$\tau_* \sim 90 \left(\frac{H}{3\,\mathrm{kpc}}\right)\,\mathrm{Myr}$$

→ 比弹道传播时标**大 3 个数量级以上**，这是**扩散运动的"最强证据"**。

**[FACT]** 10 GeV 的扩散系数（Blasi）：

$$D(E) \simeq 3\times 10^{28} \left(\frac{H}{3\,\mathrm{kpc}}\right)\,\mathrm{cm^2\,s^{-1}}$$

**[FACT]** B/C 高能行为与 power law $X(R) \propto R^{-\delta}$ 一致，**$\delta$ = 0.3 – 0.6**。

## 2.3 单个 SNR 贡献的 CR 质子通量（Blasi 式 (2)）

**[FACT]** Blasi 给出 CR 质子在地面观测的通量：

$$J(E) = \frac{c}{4\pi} \frac{N(E) R_{SN}}{\pi R_d^2 H} \tau_{esc}(E)$$

$$= 8\times 10^5\, \xi_{CR}\, I(\gamma) \left(\frac{R_{SN}}{30\,\mathrm{yr^{-1}}}\right)\left(\frac{E}{m}\right)^{-\gamma-\delta} \left(\frac{E_*}{m}\right)^\delta \,\mathrm{m^{-2}\,s^{-1}\,sr^{-1}\,GeV^{-1}}$$

其中：
- $R_d = 10$ kpc（银河盘半径）
- $I(\gamma)$ 是归一化积分 $I(\gamma) \approx \frac{2(3-\gamma)(\gamma-2)}{4-\gamma}$
- 逃逸时标以 $E_*$ 处归一 → 通量**不依赖于晕高 H**（因为 CR 通量和 grammage 都 ∝ H/D）

## 2.4 加速效率 $\xi$_CR 的直接约束（Blasi 式 (3)）

**[FACT]** 以 10 GeV 处 $E_*^2 J(E_*) \approx 2\times 10^3$ GeV m⁻² s⁻¹ sr⁻¹ 归一：

$$\xi_{CR} \approx 2.5\times 10^{-3}\, \frac{(E_*/m)^{\gamma-2}}{I(\gamma)} \left(\frac{R_{SN}}{30\,\mathrm{yr^{-1}}}\right)^{-1}$$

**[FACT]** 对典型参数：
- **$\xi$_CR ~ 2–3%**（仅计质子）
- 计入重核贡献：总效率 **5–10%**
- 对个别 SNR 可更高或更低，取决于爆发环境

**[INTERPRETATION]** 5–10% 的加速效率是 SNR 范式的关键定量约束：**非线性**理论（NLDSA）是必需的。

## 2.5 逃逸时间 vs 传播时标的张力

**[FACT]** 若 $\xi$_CR ~ 10%，粒子对激波有动力学反作用，会改变：
- 压缩比 R（因此谱斜率 $\alpha$ 不再是简单的 p⁻⁴）
- 亚激波结构（subshock）
- 前置区（precursor）
→ 见第 4 章 NLDSA 部分。

**[CRITIQUE]** 从 B/C 反推 $\delta$ 时，**$\delta$ = 0.3–0.6 的不确定性**（约 2 倍）反映了 B/C 高能测量的误差（Blasi Fig.2）。这直接影响对**注入谱斜率 $\gamma$_inj** 的推断（Amato §5 进一步讨论）。

## 2.6 文献未明确说明

- **[FACT]** 未给出具体 B/C 数据点的数值表格（Blasi Fig.2 只是定性展示）
- **[FACT]** 未讨论 B/C 系统误差（如电离损失、低能太阳调制的复杂解调）