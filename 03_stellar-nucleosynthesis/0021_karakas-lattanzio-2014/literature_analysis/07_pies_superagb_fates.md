# 7. PIEs, Super-AGB 与最终命运（§3.8–3.10）

**上一章**: [06_nucleosynthesis_hbb_sprocess.md](06_nucleosynthesis_hbb_sprocess.md) · **下一章**: [08_uncertainties.md](08_uncertainties.md)

## 7.1 Proton Ingestion Episodes（PIEs）

[FACT] PIEs 发生于热脉冲期间：对流核外扩将 H 层卷入高温（T > 10⁸ K）He 燃烧区，部分 H 质子被 CNO 循环消耗（"proton ingestion"）。

### 7.1.1 1D PIEs 概览
[FACT] 1D 计算中，H 层卷入程度依赖对流超射参数；强超射 → 深 PIEs。

### 7.1.2 1D PIE 产额
[FACT] 强 PIEs 可产生 ¹³C、²⁶Al、²²Na 等；但对最终 WD 残骸组成影响有限。

### 7.1.3 多维 PIE 计算
[FACT] 3D 计算显示强对流混合可将更多 H 卷入 → 更强的 CNO 燃烧；但产额与 1D 差异取决于网格分辨率。

## 7.2 Super-AGB 恒星（3.9）

[FACT] Super-AGB：M ≈ 8–10M⊙，中心点燃 C 后继续演化到 ONe 核心 + He 壳燃烧（类似 AGB，但核心更热、质量更大）。

### 7.2.1 Super-AGB 演化
[FACT] 演化路径：C 核心 → Ne 燃烧 → ONe 核心 + O/Ne 壳 → AGB-like。

### 7.2.2 Super-AGB 的 TDU
[FACT] Super-AGB 亦发生 TDU，但由于 He intershell 更小且包络质量小，表面增丰有限。

### 7.2.3 Super-AGB 核合成
[FACT] 是 ²²Ne、²⁶Al 的少量贡献源，也可能通过电子俘获超新星（e- capture SNe）结束。

## 7.3 最终命运（3.10）

| 质量区间 | 残骸 |
|---------|------|
| < 8M⊙ | C-O 白矮星 |
| 8–10M⊙ | ONe 白矮星 或 e- capture SN → 中子星 |
| > 10M⊙ | 坍缩超新星 → 中子星/黑洞 |

## 7.4 PIE / Super-AGB 关键公式（LaTeX）

[FACT] **PIE 触发的 H 卷入深度条件**（T > 10⁸ K）：原文 p.54
$$ T_{\rm engulfed} \;>\; 10^{8}\,\mathrm{K}, \qquad \Delta M_{\rm H-ingested} \;\propto\; d_{\rm overshoot} $$

[FACT] **1D PIE 中表面 N 增丰**（CN 循环在卷入 H 上快速平衡）：原文 p.55
$$ \frac{^{14}\mathrm{N}}{^{12}\mathrm{C}}\bigg|_{\mathrm{post\text{-}PIE}} \;\gg\; \frac{^{14}\mathrm{N}}{^{12}\mathrm{C}}\bigg|_{\mathrm{pre\text{-}PIE}} $$

[FACT] **PIE 中 ²⁶Al 生成**：原文 p.55
$$ ^{25}\mathrm{Mg}(p,\gamma)^{26}\mathrm{Al}(\beta^+)\,^{26}\mathrm{Mg} $$

[FACT] **Super-AGB 最终核心质量**（决定命运分界）：原文 p.60
$$ M_{\rm core}^{\rm final} \;<\; M_{\rm Chandrasekhar} \;\approx\; 1.38\,M_\odot \quad \Longrightarrow \quad \text{ONe WD} $$
$$ M_{\rm core}^{\rm final} \;\gtrsim\; M_{\rm Chandrasekhar} \quad \Longrightarrow \quad e^-\text{-capture SN} \to \mathrm{NS} $$

[FACT] **e- capture 触发条件**（ONe 核致密化）：原文 p.60
$$ ^{24}\mathrm{Mg} + e^- \;\to\; ^{24}\mathrm{Na} + \nu_e \quad (\rho \gtrsim 4\times 10^9\,\mathrm{g\,cm^{-3}}) $$
$$ ^{20}\mathrm{Ne} + e^- \;\to\; ^{20}\mathrm{F} + \nu_e \quad (\rho \gtrsim 2\times 10^{10}\,\mathrm{g\,cm^{-3}}) $$

[FACT] **Super-AGB ²²Ne 累积产额**：原文 p.60
$$ X(^{22}\mathrm{Ne})_{\rm yield} \;\approx\; 10^{-3} \;\text{至}\; 10^{-2} \qquad (M \simeq 8\text{--}10\,M_\odot) $$
