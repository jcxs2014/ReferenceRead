# 7. H$\alpha$ line as a cosmic ray calorimeter in SNRs

> 本章属于：The Origin of Galactic Cosmic Rays（Blasi, 2013, arXiv:1311.7346）
>
> 上一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/06_indirect_evidence.md|06_indirect_evidence.md]]
>
> 下一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/08_conclusions.md|08_conclusions.md]]

## 7.1 本节核心内容

- 部分电离介质中 Balmer 线的三重结构：窄线（~21 km/s, 上游气体温度）、宽线（~几百–几千 km/s, 下游离子温度）、中间线（~100–300 km/s, 前驱区预热离子）。
- **CR 加速的两个可观测特征**：(1) 宽 Balmer 线变窄（下游温度被 CR 压力降低）；(2) 窄 Balmer 线变宽（CR 前驱区湍流加热中性氢）。
- 部分电离介质中的**中性回流（neutral return flux）**：改变激波结构，使压缩比 r<4 即使对强激波；软化低能粒子谱。
- **SNR 0509–67.5** 是首个可靠测量到异常宽 Balmer 线的 SNR（LMC 内）；**RCW86** 结果被部分撤回；**SN1006** NW 边缘表明 Balmer 观测也可用于**测量碰撞less 激波性质**。

## 7.2 原文内容

### §7 引言

- [FACT] "H$\alpha$ optical emission from Balmer dominated SNR shocks is a powerful indicator of the conditions around the shock (Chevalier and Raymond, 1978; Chevalier et al, 1980)."
- [FACT] Balmer 线产生机制：中性 H 穿越碰撞less 激波，与热离子/电子碰撞被激发到 n=3，再跃迁到 n=2。
- [FACT] 中性原子**不直接受激波加热**（电磁作用），仍保持上游温度。
- [FACT] 电荷交换反应形成**热原子群**（下游热离子捕获快速中性原子电子），其 Balmer 发射对应下游离子温度的多普勒展宽。
- [FACT] **窄线**来自下游直接穿越的中性 H（宽度反映上游温度，$10^{4}$ K 时 ~21 km/s）。
- [FACT] **宽线**来自经历电荷交换的中性 H（宽度反映下游离子温度）——"basically the only method to do so" 测量下游离子温度。
- [FACT] CR 加速的两现象：
  1. 下游气体温度低于无加速情形（因 CR 压力替代部分热能）→ 宽 Balmer 线变窄。
  2. CR 前驱区减速并加热上游离子 → 电荷交换传递能量给中性 H → 窄 Balmer 线变宽。

### §7.1 Test particles in partially ionized media

- [FACT] **中性回流（neutral return flux）**（Blasi et al. 2012）：下游电荷交换产生的热原子以高速运动，部分可穿越激波回到上游，在上游几倍电荷交换/电离路径长度内沉积能量动量。
- [FACT] 结果：上游等离子体被加热并减速 → **激波 Mach 数降低** → 压缩比 r<4（即使是强激波）。
- [FACT] 中性回流在 V_sh ≲ 3000 km/s 时重要；对更快激波，电荷交换截面急剧下降，主要变为电离。
- [FACT] 后果：低能粒子（扩散长度 < 电荷交换/电离路径长度）的谱**显著变软**；高能粒子不受影响。
- [FACT] 若激波速度 ~1000 km/s，谱可变得极陡，粒子能量含量被注入能量而非粒子质量主导 ——"for all practical purposes, corresponds to not having particle acceleration."
- [FACT] **中间 Balmer 线**：在激波前 ~几倍碰撞长度内的离子被中性回流预热，与之电荷交换产生的 H$\alpha$ 线宽 ~100–300 km/s。
- [FACT] 观测证据：Ghavamian et al. (2000) 可能有初步观测到中间线。

### §7.2 NLDSA in partially ionized media

- [FACT] Morlino et al. (2013c) 完整发展了部分电离介质中的 NLDSA，使用**混合方法**：中性氢由 Boltzmann 方程处理（因其相空间分布**非麦克斯韦**），离子由流体方程，加速粒子由非线性 PDE。
- [FACT] 耦合迭代求解后返回：粒子谱、所有热力学量、磁场分布、中性 H 相空间分布。
- [FACT] **Fig. 14 计算示例**（V_sh=4000 km/s，n=0.1 cm⁻³，p_max=50 TeV/c）：
  - 无加速时：宽线/窄线宽正常。
  - 有加速（$\xi_{\rm inj}$=3.5）：宽线变窄，窄线变宽。
  - 湍流加热 $\eta_{\rm TH}$ 越大，中间线越明显（几百 km/s 宽）。
- [FACT] 观测难点：窄线与宽线**所需速度分辨率差别很大**，通常只测量其中一种；中间线被"吸收"到宽或窄组分中。

### SNR 0509–67.5（LMC 内）

- [FACT] 距离 50 ± 1 kpc（精确）。
- [FACT] Helder et al. (2010, 2011) 在 SW 和 NE 边缘分别测得宽 Balmer 线 FWHM = 2680 ± 70 km/s 和 3900 ± 800 km/s。
- [FACT] 激波速度：整体平均 V_sh=6000±300 km/s；NE 部分 V_sh=6600±400 km/s；SW 边缘 Helder 用 V_sh=5000 km/s。
- [FACT] Helder 使用 van Adelsberg et al. (2008) 计算推断加速效率——但 Morlino et al. (2013a) 指出其对快激波的**中性氢分布函数假设**可能严重高估 $\xi_{\rm CR}$。
- [FACT] SW 边缘实际速度可能 ~4000 km/s（形态学判断）——比 Helder 用的 5000 km/s 低。
- [FACT] **修正后**（Morlino et al. 2013b，Fig. 15）：若 V_sh=4000 km/s、h_N=10%、$\beta_{\rm down}$≪1（快激波时电子-离子未平衡），测得 FWHM 支持 **$\xi_{\rm CR}$ ~ 10–20%**。
- [FACT] 参数 $\beta_{\rm down}$ = T_e/T_p 是关键不确定性：$\beta_{\rm down}$=1（完全平衡）时即使 V_sh=4000 km/s，测得 FWHM 仍与无加速兼容；$\beta_{\rm down}$ ≪ 1 时才支持高效加速。

### RCW86

- [FACT] Helder et al. (2009) 报告宽 Balmer 线 FWHM = 1100 ± 63 km/s，V_sh = 6000 ± 2800 km/s，推断 **$\xi_{\rm CR}$ ~ 80%**——异常高。
- [FACT] Helder et al. (2013) **基本撤回**先前结果：细化区域研究后 V_sh 更低；仅有若干区域有**边际证据**支持粒子加速。
- [FACT] RCW86 形态复杂、距离不确定 → $\xi_{\rm CR}$ 估算难度高。

### 其他观测

- [FACT] 多个 SNR 的窄 Balmer 线异常展宽（Sollerman et al. 2003）：宽度 30–50 km/s → 激波前温度 ~25,000–50,000 K。
- [FACT] 若为 ISM 平衡温度，则**没有原子氢存在**——说明激波前有某种**前驱区加热**，最可能是 CR 前驱区。
- [FACT] SN1006 NW 边缘（Nikolić et al. 2013）：**亮 Balmer 源但不加速粒子**（无同步辐射 X 射线）——宽 Balmer 线与激波速度一致，无加速效应。
- [FACT] SN1006 观测展示 Balmer 线**测量碰撞less 激波性质**的潜力。

### 观测建议

- [FACT] 最重要的测量：在同一位置**同时测量窄/宽（中间）Balmer 线宽度**；同步测热 X 射线约束电子温度。
- [FACT] 目前尚无任何天体具备这种精度。

## 7.3 关键公式

本节以**半解析/数值模型**为主，无独立封闭公式。核心物理量：

- Balmer 窄线宽：$\Delta$v_narrow ~ √(2kT_upstream/m_H) ~ 21 km/s (T_up = $10^{4}$ K)
- Balmer 宽线宽：$\Delta$v_broad ~ √(2kT_downstream/m_H)
- 中性回流激波预热距离：~几倍 $\lambda_{\rm cx}$ + $\lambda_{\rm ion}$
- 中间线宽度：~100–300 km/s

## 7.4 关键数值

| 物理量 | 数值 |
|--------|------|
| Balmer 窄线宽度（$10^{4}$ K） | ~21 km/s |
| Balmer 中间线宽度 | ~100–300 km/s |
| 中性回流重要 V_sh 阈值 | ≲ 3000 km/s |
| 中性氢质量分数 h_N（SNR 0509 采用） | 10% |
| SNR 0509 距地 | 50 ± 1 kpc（LMC）|
| SNR 0509 SW FWHM | 2680 ± 70 km/s |
| SNR 0509 NE FWHM | 3900 ± 800 km/s |
| SNR 0509 V_sh（SW） | 4000–5000 km/s |
| SNR 0509 支持 $\xi_{\rm CR}$ | ~10–20%（$\beta_{\rm down}$ ≪ 1 时）|
| RCW86（初测）FWHM | 1100 ± 63 km/s |
| RCW86（初测）V_sh | 6000 ± 2800 km/s |
| RCW86（初测）$\xi_{\rm CR}$ | ~80%（后被撤回）|
| Sollerman 等观测窄线宽 | 30–50 km/s → T_前置 ~25,000–50,000 K |

## 7.5 图表分析

参见 `09_figures_tables.md`（Figure 13 部分电离介质谱斜率、Figure 14 Balmer 线形状、Figure 15 SNR 0509 FWHM-$\xi_{\rm CR}$ 关系）。

## 7.6 作者的逻辑

- 从 Balmer 线**物理机制**（§7 引言）→ 中性回流**改变激波结构**（§7.1）→ NLDSA 在此框架下的**完整数值模型**（§7.2）→ **两个真实 SNR 的应用**（SNR 0509、RCW86）→ Balmer 观测的**前景与局限**。
- [INTERPRETATION] 本节的核心科学主张是：Balmer 线是**唯一**可直接测量下游离子温度的方法，因而也是**唯一**可直接约束 CR 加速效率的观测手段。

## 7.7 我的理解

- [FACT] Balmer 线的**"CR calorimeter"**功能是本文的重要卖点——作者反复强调这是"unique tool to measure the CR acceleration efficiency"。
- [CRITIQUE] 但作者也承认**$\beta_{\rm down}$ 的不确定性**是最大障碍：若电子-离子平衡（$\beta_{\rm down}$=1），SNR 0509 的 FWHM 与无加速兼容；只有 $\beta_{\rm down}$ ≪ 1 时才支持 10–20% 加速效率。这一不确定性**无法通过 Balmer 观测单独解决**，需要 X 射线热辐射的独立测量。
- [CRITIQUE] RCW86 案例展示了**观测结论的可撤回性**：初测与修正结果相差 80% → 10%，是 CR 观测中系统误差的一个生动案例。
- [INTERPRETATION] 中间 Balmer 线的预言是**2012 年 Blasi et al. 的新结果**，在 2013 年时尚未被清晰观测到——这是本文对观测界的直接预言。

## 7.8 潜在问题与值得关注的地方

- **潜在不一致性**：SNR 0509 的 SW 边缘速度在不同文献中不一致（Helder 用 5000 km/s；Morlino 用 4000 km/s），直接影响 $\xi_{\rm CR}$ 推断。
- [CRITIQUE] §7.2 的数值计算需要**中性氢的相空间分布**——这比传统"中性氢作为流体"的假设更严格，但**观测上无直接方法约束中性氢相空间分布**。
- **信息缺失**：作者未讨论**光学厚效应**、**散射对 Balmer 线形状的影响**——这些都是 Balmer 建模中的经典问题。
- [CRITIQUE] 中间 Balmer 线（~100–300 km/s）在观测上极难分辨：它夹在窄线与宽线之间，且**无标准方法分离**。作者仅在 §7.2 末尾指出"needs proper convolution with velocity resolution"—这是**技术难题**，不是简单"看观测"能解决的。