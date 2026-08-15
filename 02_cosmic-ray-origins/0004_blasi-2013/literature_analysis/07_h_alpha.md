---
chapter: 7
title: H$\alpha$ line as a cosmic ray calorimeter in SNRs
pages: "Blasi 2013, §7 (pp. 58–65)"
sections:
  - "7.1 Acceleration of test particles at shocks in partially ionized media"
  - "7.2 NLDSA in partially ionized media"
related_chapters:
  prev: 06_indirect_evidence
  next: 08_conclusions
status: done
---

> 本章属于：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/00_overview.md|The Origin of Galactic Cosmic Rays（Blasi, 2013, arXiv:1311.7346）]]
>
> 上一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/06_indirect_evidence.md|06_indirect_evidence]]
>
> 下一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/08_conclusions.md|08_conclusions]]


# 7. H-alpha observations

[FACT] 章节定位（原文）：\"H$\alpha$ optical emission from Balmer dominated SNR shocks is a powerful indicator of the conditions around the shock (Chevalier and Raymond, 1978; Chevalier et al, 1980) including the presence of accelerated particles.\"

[FACT] **Balmer 线产生机制**：中性 H 穿越碰撞less 激波，与热离子/电子碰撞被激发到 $n=3$，再跃迁到 $n=2$。

[FACT] **窄线 vs 宽线的物理根源**：
- **窄线**：中性 H **不直接受激波加热**（电磁作用对中性原子无效），保持上游温度，$10^4\,\mathrm{K}$ 时宽度 ~21 km/s
- **宽线**：经历**电荷交换**的中性 H —— 下游热离子捕获快速中性原子电子形成\"热原子群\"，其 Balmer 发射对应下游离子温度的**多普勒展宽**
- \"basically the only method to do so\" —— Balmer 宽线是**测量下游离子温度的基本唯一方法**，因为碰撞less 激波下电子温度**低于**质子温度

[FACT] **CR 加速的两个诊断信号**：
1. 下游气体温度低于无加速情形（CR 压力替代部分热能）→ **宽 Balmer 线变窄**
2. CR 前驱区减速并加热上游离子 → 电荷交换传递能量给中性 H → **窄 Balmer 线变宽**
- 原文（Heng 2010）：\"A narrower broad Balmer line and a broader narrow Balmer line are both signatures of CR acceleration at SNR shocks.\"

[FACT] 部分电离介质中 CR 加速的理论**仅有**最近被完整发展（Blasi et al. 2012；Morlino et al. 2012, 2013c），是**新的预测性领域**。

---

### 7.1 Acceleration of test particles at shocks in partially ionized media

> **部分电离介质中激波处 test-particle 的加速**

[FACT] **中性回流（neutral return flux）**——Blasi et al. (2012) 的新发现：下游电荷交换产生的热原子以高速运动，部分可穿越激波回到上游，在上游**几倍电荷交换/电离路径长度**内沉积能量动量。

[FACT] **后果**：上游等离子体被加热并减速 → **激波 Mach 数降低** → 压缩比 $r<4$（**即使是强激波**）。

[FACT] 中性回流在 $V_{\rm sh}\lesssim 3000\,\mathrm{km/s}$ 时重要；对更快激波，电荷交换截面急剧下降，主要变为电离。

[FACT] **谱的显著软化**：低能粒子（扩散长度 < 电荷交换/电离路径长度）的谱**显著变软**；高能粒子不受影响。

[FACT] 若激波速度 ~1000 km/s，谱可变得**极陡**，粒子能量含量被注入能量而非粒子质量主导 ——原文（\"for all practical purposes, corresponds to not having particle acceleration\"）：**对实际目的，等同于没有粒子加速**。

[FACT] **中间 Balmer 线**（原文）：\"an intermediate Balmer line, with a typical width of $\sim 100$–$300\,\mathrm{km/s}$\" ——由激波前 ~几倍碰撞长度内被中性回流预热的离子产生。Ghavamian et al. (2000) 可能有初步观测。

[FACT] Figure 13（Blasi et al. 2012，$\rho=0.1\,\mathrm{cm^{-3}}$, $B=10\,\mu$G, 电离分数 50%）：谱斜率随激波速度的演化——标准 $\sim 2$ 仅在 $V_{\rm sh}>3000\,\mathrm{km/s}$ 时恢复。

[CRITIQUE] 中性回流效应**可能**调和 §6.2 中的逃逸谱与 $\gamma$ 射线观测之间的矛盾，但**预期仅在 $V_{\rm sh}<3000\,\mathrm{km/s}$ 时才显著**——即对老 SNR 有意义，对年轻 SNR 有限。

---

### 7.2 NLDSA in partially ionized media

> **部分电离介质中的 NLDSA**

[FACT] Morlino et al. (2013c) 完整发展了部分电离介质中的 NLDSA，使用**混合方法**：
- **中性氢**：Boltzmann 方程（因其相空间分布**非麦克斯韦**，不能用流体描述）
- **离子**：流体方程
- **加速粒子**：非线性 PDE

[FACT] 耦合迭代求解后返回：粒子谱、所有热力学量、磁场分布、**中性 H 相空间分布**——从远上游到远下游。

[FACT] **Figure 14 计算示例**（$V_{\rm sh}=4000\,\mathrm{km/s}$, $n=0.1\,\mathrm{cm^{-3}}$, $p_{\max}=50\,\mathrm{TeV}/c$）：
- 无加速（黑线）：宽线/窄线宽正常
- 有加速（$\xi_{\rm inj}=3.5$）：**宽线变窄，窄线变宽**
- 湍流加热 $\eta_{\rm TH}$ 越大 → **中间线越明显**（几百 km/s 宽）
- 右图：窄 Balmer 线的 zoom-in 显示加速导致的**窄线展宽**

[FACT] **观测难点**：窄线与宽线**所需速度分辨率差别很大**，通常只测量其中一种；中间线被\"吸收\"到宽或窄组分中。\"an assessment of the observability of the intermediate Balmer component requires a proper convolution of the predictions with the velocity resolution of the instrument.\"

[FACT] **关键不确定性参数**：$\beta_{\rm down} = T_e/T_p$（下游电子-离子温度比）。

[FACT] **SNR 0509-67.5**（LMC 内，距离 $50\pm 1\,\mathrm{kpc}$）：
- Helder et al. (2010, 2011) 测得 SW 和 NE 边缘宽 Balmer 线 FWHM = $2680\pm 70\,\mathrm{km/s}$ 和 $3900\pm 800\,\mathrm{km/s}$
- 激波速度：整体平均 $V_{\rm sh}=6000\pm 300\,\mathrm{km/s}$；NE 部分 $6600\pm 400\,\mathrm{km/s}$；SW 边缘 Helder 用 $V_{\rm sh}=5000\,\mathrm{km/s}$
- Helder 使用 van Adelsberg et al. (2008) 计算推断加速效率——但 Morlino et al. (2013a) 指出其对快激波的**中性氢分布函数假设**可能**严重高估** $\xi_{\rm CR}$
- **SW 边缘实际速度可能 ~4000 km/s**（形态学判断）——比 Helder 用的 5000 km/s 低

[FACT] **修正后**（Morlino et al. 2013b，Figure 15）：若 $V_{\rm sh}=4000\,\mathrm{km/s}$、$h_N=10\%$、$\beta_{\rm down}\ll 1$（快激波时电子-离子未平衡），测得 FWHM 支持 **$\xi_{\rm CR}\sim 10$–$20\%$**。

[FACT] **参数不确定性**：$\beta_{\rm down}=1$（完全平衡）时即使 $V_{\rm sh}=4000\,\mathrm{km/s}$，测得 FWHM **仍与无加速兼容**；只有 $\beta_{\rm down}\ll 1$ 时才支持高效加速。Ghavamian et al. (2007, 2013) 支持 $\beta_{\rm down}\ll 1$。

[FACT] **RCW86**：
- Helder et al. (2009) 初测 FWHM = $1100\pm 63\,\mathrm{km/s}$，$V_{\rm sh}=6000\pm 2800\,\mathrm{km/s}$，推断 **$\xi_{\rm CR}\sim 80\%$** ——异常高
- Helder et al. (2013) **基本撤回**先前结果：细化区域研究后 $V_{\rm sh}$ 更低；仅有若干区域有**边际证据**支持粒子加速
- RCW86 形态复杂、距离不确定 → $\xi_{\rm CR}$ 估算难度高

[FACT] **其他窄线异常**（Sollerman et al. 2003）：多个 SNR 窄 Balmer 线宽度 30–50 km/s → 激波前温度 ~25,000–50,000 K ——若为 ISM 平衡温度则**没有原子氢存在**，说明激波前有某种**前驱区加热**，最可能是 **CR 前驱区**。

[FACT] **SN1006 NW 边缘**（Nikolić et al. 2013）：**亮 Balmer 源但不加速粒子**（无同步辐射 X 射线）——宽 Balmer 线与激波速度一致，**无需**加速粒子即可解释。SN1006 展示 Balmer 线**测量碰撞less 激波性质**的潜力。

[FACT] **观测建议**（原文）：\"Most important would be to have measurements of the width of the narrow and broad components (and possibly intermediate component) of the Balmer line at the same location in order to allow for a proper estimate of the CR acceleration efficiency. Co-spatial observation of the thermal X-ray emission would also provide important constraints on the electron temperature. So far, this information is not yet available with the necessary accuracy in any of the astrophysical objects of relevance.\"

[CRITIQUE] **$\beta_{\rm down}$ 的不确定性**是最大障碍：若电子-离子平衡（$\beta_{\rm down}=1$），SNR 0509 的 FWHM 与无加速兼容；只有 $\beta_{\rm down}\ll 1$ 时才支持 10–20% 加速效率。这一不确定性**无法通过 Balmer 观测单独解决**，需要 X 射线热辐射的独立测量。

[CRITIQUE] RCW86 案例展示了**观测结论的可撤回性**：初测与修正结果相差 80% → 10%，是 CR 观测中系统误差的生动案例。

**关键数值汇总**：

| 物理量 | 数值 |
|--------|------|
| Balmer 窄线宽度（$10^4\,\mathrm{K}$） | ~21 km/s |
| Balmer 中间线宽度 | ~100–300 km/s |
| 中性回流重要 $V_{\rm sh}$ 阈值 | $\lesssim 3000\,\mathrm{km/s}$ |
| 中性氢质量分数 $h_N$（SNR 0509 采用） | 10% |
| SNR 0509 距地 | $50\pm 1\,\mathrm{kpc}$（LMC） |
| SNR 0509 SW FWHM | $2680\pm 70\,\mathrm{km/s}$ |
| SNR 0509 NE FWHM | $3900\pm 800\,\mathrm{km/s}$ |
| SNR 0509 $V_{\rm sh}$（SW） | 4000–5000 km/s |
| SNR 0509 支持 $\xi_{\rm CR}$ | ~10–20%（$\beta_{\rm down}\ll 1$ 时） |
| RCW86（初测）FWHM | $1100\pm 63\,\mathrm{km/s}$ |
| RCW86（初测）$V_{\rm sh}$ | $6000\pm 2800\,\mathrm{km/s}$ |
| RCW86（初测）$\xi_{\rm CR}$ | ~80%（后被撤回） |
| Sollerman 等观测窄线宽 | 30–50 km/s → $T_{\rm 前置}\sim 25{,}000$–$50{,}000\,\mathrm{K}$ |

## 关键公式

本节以**半解析/数值模型**为主，无独立封闭公式。核心物理量：

- Balmer 窄线宽：$\Delta v_{\rm narrow} \sim \sqrt{2kT_{\rm upstream}/m_H}\sim 21\,\mathrm{km/s}$ ($T_{\rm up}=10^4\,\mathrm{K}$)
- Balmer 宽线宽：$\Delta v_{\rm broad} \sim \sqrt{2kT_{\rm downstream}/m_H}$
- 中性回流激波预热距离：~几倍 $\lambda_{\rm cx}+\lambda_{\rm ion}$
- 中间线宽度：~100–300 km/s

## 图表分析

参见 `09_figures_tables.md`（Figure 13 部分电离介质谱斜率、Figure 14 Balmer 线形状、Figure 15 SNR 0509 FWHM-$\xi_{\rm CR}$ 关系）。

---

## 元数据

```yaml
chapter: 7
title: H$\alpha$ line as a cosmic ray calorimeter in SNRs
pages: "Blasi 2013, §7 (pp. 58–65)"
subsections:
  - "7.1 Acceleration of test particles at shocks in partially ionized media"
  - "7.2 NLDSA in partially ionized media"
key_formulas:
  - "Δv_narrow ~ √(2kT_up/m_H) ~ 21 km/s (T_up=10^4 K)"
  - "Δv_broad ~ √(2kT_down/m_H)"
  - "β_down = T_e/T_p (关键不确定性参数)"
keywords:
  - Balmer line
  - H-alpha
  - CR calorimeter
  - neutral return flux
  - partially ionized media
  - SNR 0509-67.5
  - RCW86
  - SN1006
  - β_down
  - intermediate Balmer line
  - Morlino et al. 2013c
references_internal:
  prev_chapter: 06_indirect_evidence
  next_chapter: 08_conclusions
```

**引用出处**：Blasi, "The Origin of Galactic Cosmic Rays," *arXiv:1311.7346* (2013), §7（pp. 58–65）。