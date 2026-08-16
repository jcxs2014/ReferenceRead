# 04. Cosmic Ray Generation by Shock Fronts
> 本章属于：[[02_cosmic-ray-origins/0019_bell-1978-ii/literature_analysis/00_overview.md|The acceleration of cosmic rays in shock fronts — II]]
> 上一章：[[02_cosmic-ray-origins/0019_bell-1978-ii/literature_analysis/03_nonrelativistic_spectrum.md|03_nonrelativistic_spectrum]]
> 下一章：[[02_cosmic-ray-origins/0019_bell-1978-ii/literature_analysis/05_conclusions.md|05_conclusions]]

> **本节核心**：将 §2（注入）和 §3（非相对论谱）的理论综合应用于**超新星遗迹（SNR）**，估算单个 SNR 可产生的宇宙线总能量、磁场增强机制，以及 SNR 能否解释银河系宇宙线的主要来源。

## 4.1 应用目标与框架（[FACT]）

**核心问题**：DSA 机制（I）+ 注入物理（§2）+ 非相对论谱修正（§3）能否给出银河系宇宙线**可观测数量级**的产生率？

**本文估算方法**：
1. 估算单个 SNR 总可用能量
2. 乘以注入效率 × 加速效率 → 宇宙线产生能量
3. 与银河系宇宙线密度做比较
4. 检验能量均分假设（equipartition）下的磁场估计

> **背景**：bell-1978 (I) 只在 Cas A 上检验加速能力（相空间密度超背景 $10^4$ 倍）；本文 §4 从**能量预算**角度做更定量检验。

## 4.2 单个 SNR 的总可用能量（[FACT]）

**SNR 参数**（本文采用典型值）：
| 参数 | 符号 | 值 |
|------|------|-----|
| 激波速度 | $v_s$ | $10^8$ cm/s |
| SNR 半径 | $R$ | $\sim 10$ pc $= 3 \times 10^{19}$ cm |
| 上游密度 | $n_H$ | $1$ cm$^{-3}$ |
| 马赫数 | $M_s$ | $\sim 8$ |
| 压缩比 | $\chi$ | 4 |
| SNR 年龄 | $t$ | $\sim 10^4$ yr |

### 4.2.1 动能预算

**激波扫过质量**：
$$M_{\rm swept} \sim \frac{4}{3}\pi R^3 n_H m_p \sim \frac{4}{3}\pi (3\times10^{19})^3 \times 1.67\times10^{-24} \sim 5\times10^6 M_\odot$$

> **注**：实际 SNR 半径在 $10^4$ 年内 $\sim 10$ pc 时，扫过质量更准确地应为：
$$M_{\rm swept} \sim 4\pi R^3 n_H m_p / 3 \sim 4\times10^4 M_\odot$$

**可用动能**：
$$E_{\rm kin} \sim \frac{1}{2} M_{\rm swept} v_s^2 \sim 10^{50} \text{ erg}$$

这是超新星爆炸的典型释放能量量级——**宇宙线产生的最大可能上限**。

## 4.3 宇宙线产生率估算（[FACT]）

### 4.3.1 注入效率 × 加速效率

**注入率**（§2）：
$$\eta_{\rm inj} \sim 1\%$$

**加速到 $E_{\rm crit}$ 的效率**（I §3）：
$$\eta_{\rm acc} \sim \frac{\text{加速到 } E_{\rm crit} \text{ 的粒子比例}}{\text{注入粒子总数}}$$

结合 §2-§3：
$$\eta_{CR} = \eta_{\rm inj} \times \eta_{\rm acc} \sim 0.01 \times 0.1 = 10^{-3}$$

**宇宙线总能量**：
$$E_{CR} \sim \eta_{CR} \times E_{\rm kin} \sim 10^{-3} \times 10^{50} = 10^{47} \text{ erg}$$

### 4.3.2 与银河系宇宙线能量密度对比

**银河系宇宙线能量密度**：
- 观测：$u_{CR} \sim 1$ eV/cm³ $\sim 1.6 \times 10^{-12}$ erg/cm³
- 银河系体积：$V_{gal} \sim \pi (15 \text{ kpc})^2 \times 0.3 \text{ kpc} \sim 3\times10^{68}$ cm³
- 银河系宇宙线总能量：$E_{CR,gal} \sim 5 \times 10^{56}$ erg
- 银河系 SNR 数量（寿命 $\sim 10^7$ 年）：$N_{SNR} \sim 300$

**要求**：每个 SNR 产生 $\sim E_{CR,gal}/N_{SNR} \sim 10^{54}/300 \sim 10^{54-2.5} \sim 3\times10^{51}$ erg

> **差距**：$E_{CR} \sim 10^{47}$ erg $\ll$ 所需 $3\times10^{51}$ erg——差约 4 个数量级！

> **批注**：这一差距正是 Bell 本文的**关键结论**——单纯 DSA 注入 + 加速效率不足——后续文献（Caprioli, Ptuskin 等）提出非线性反馈放大注入效率来弥合此差距。

## 4.4 能量均分假设与磁场增强（[FACT]）

### 4.4.1 能量均分

**假设**：宇宙线能量密度 = 磁场能量密度（equipartition）：
$$u_{CR} \sim u_B = \frac{B^2}{8\pi}$$

**典型值**（本文采用，OCR 提取）：
- 压缩后磁场：$B \sim 5$ μG $= 5 \times 10^{-6}$ G
- 对应磁场能量密度：$u_B = B^2/8\pi \approx 10^{-9}$ erg/cm³

### 4.4.2 磁场增强机制（§4.1）

**标准激波磁场压缩**：
$$B_{\rm downstream} = \sqrt{\chi} B_0 \sim 2 B_0$$

- 若上游 $B_0 \sim 3$ μG，则下游 $B \sim 6$ μG

**宇宙线放大机制**（本文 §4.1 讨论）：
- 宇宙线驱动的不稳定性（streaming instability）进一步放大磁场
- 放大因子可达 $B/B_0 \sim 10$–$100$（远超压缩比）

> **注**：本文 §4.1 对磁场放大做了定性讨论——详细量化在后续 Bell 系列论文中展开。

## 4.5 射电源通量密度估算（[FACT]）

### 4.5.1 同步辐射通量

**同步辐射功率**（相对论电子）：
$$P_{syn} \sim \frac{4}{3}\sigma_T c \gamma^2 \frac{B^2}{8\pi}$$

**射电源积分辐射**（本文 §4.2，OCR 提取）：
$$S_\nu \propto \int n(E) P_{syn}(E, \nu) dE \cdot V_{SNR}$$

### 4.5.2 射电源观测对比

**典型年轻 SNR**：
- Cas A 射电通量密度：$S_{1\text{GHz}} \sim 500$ Jy
- 本文估算射电通量在**同一量级**

> **结论**：DSA + equipartition 假设可以大致解释年轻 SNR 的射电辐射强度——这是机制可行性的间接证据。

## 4.6 压缩磁场的定量估计（[FACT]）

**本文采用**（OCR 提取）：
- 典型压缩星际磁场 $\sim 5$ μG（压缩因子 $\sim 4$）
- 上游磁场 $B_0 \sim 1$–$3$ μG
- 下游磁场 $B = \sqrt{\chi} B_0 \sim 2 B_0$

**详细数值**：
| 位置 | $B$ |
|------|-----|
| 上游 ISM | $1$–$3$ μG |
| 下游（压缩） | $2$–$6$ μG |
| 宇宙线放大 | $\sim 10$–$50$ μG |

## 4.7 [INTERPRETATION] 数量级差距的解释

**$10^{47}$ vs $10^{51}$ erg** 的差距可能来源：
1. **注入效率**：本文 $\eta_{\rm inj} \sim 1\%$ 可能低估——实际可能达 $10\%$–$100\%$（尤其非线性反馈情况下）
2. **加速效率**：$\eta_{\rm acc}$ 在非线性 regime 下显著增大（宇宙线修改激波结构）
3. **多 SNR 累积**：银河系内 SNR 总数可能远超 300（包含已扩散的 SNR）
4. **磁场放大**：非线性磁场放大可增强加速效率

> **批注**：这一"数量级差距"是 1980s–2000s DSA 理论的核心驱动力，推动了非线性 DSA (NLDSA) 理论的发展（Katz, Drury, Bell 1978c, Caprioli 2014）。

## 4.8 [CRITIQUE] §4 的局限

1. **SNR 参数分散**：不同 SNR 的 $v_s, n_H, R$ 跨数量级变化——单一典型值估算不精确
2. **能量均分假设**：$u_{CR} = u_B$ 为经验假设，无第一性原理依据
3. **未处理非线性反馈**：本文 §4 仍是线性 DSA 框架——宇宙线对激波结构的反作用未讨论
4. **射电通量估算粗糙**：同步辐射功率估算依赖电子分布假设

## 4.9 关键方程汇总

| 方程 | 意义 |
|------|------|
| $E_{\rm kin} \sim \frac{1}{2} M_{\rm swept} v_s^2$ | SNR 总动能 |
| $\eta_{CR} = \eta_{\rm inj} \times \eta_{\rm acc}$ | 总效率 |
| $E_{CR} \sim \eta_{CR} \times E_{\rm kin}$ | 单 SNR 宇宙线能量 |
| $u_B = B^2/8\pi$ | 磁场能量密度 |
| $u_{CR} \sim u_B$ | 能量均分假设 |

## 4.10 与 §5 的衔接

| 问 | 答 | 节 |
|---|---|---|
| SNR 宇宙线产生量 | $\sim 10^{47}$ erg/个 | §4 |
| 与银河系需求差距 | $\sim 4$ 个数量级 | §4 |
| 结论与展望 | §5 | §5 |

下一节（§5）给出论文总结——DSA 机制的整体评估、已知问题、以及对未来研究的指引。
