---
title: "§6 COSMIC-RAY-MODIFIED SHOCKS"
paper: "Caprioli & Spitkovsky 2014, ApJ 783, 91"
outline_ref: "§6 COSMIC-RAY-MODIFIED SHOCKS (§6.1 Upstream Precursor; §6.2 Modified Jump Conditions)"
---
> 上一章：[[02_cosmic-ray-origins/0016_caprioli-2014/literature_analysis/05_magnetic_field_amplification.md|05_magnetic_field_amplification]]
> 下一章：[[02_cosmic-ray-origins/0016_caprioli-2014/literature_analysis/07_dsa_versus_sda.md|07_dsa_versus_sda]]

#### 6.1 [FACT] 上游 precursor

- **[FACT]** 加速离子扩散到激波上游，形成 **CR 压主导的 precursor**（图 8）。
- **[FACT]** Precursor 尺度 $\sim$ 数十至上百 $c/\omega_p$，随加速强度增长。
- **[FACT]** 这是**首次**在自洽模拟中观测到 CR-modified shock 的全貌——此前（GS12）因能量守恒与盒尺寸限制未能清晰呈现。
- **[FACT]** Precursor 使激波**减速**，上游流被预热，从而**亚结构激波**（subshock）形成——下游密度跃升发生在子激波处，而非主激波处。

#### 6.2 [FACT] 修改的跃迁条件

- **[FACT]** 标准无 CR 激波总压缩比 $r_{\text{tot}} = 4$（强激波，$\gamma=5/3$）。
- **[FACT]** 有 CR 时：**子激波**压缩比 $r_{\text{sub}} < 4$（因上游已被预热）；**总压缩比** $r_{\text{tot}} = r_{\text{CR}} \times r_{\text{sub}} > 4$（CR 压提供额外压缩）。
- **[FACT]** 模拟实测（$M=30$ 平行）：$r_{\text{sub}} \approx 3.65$，$r_{\text{tot}} \approx 4.23$；与 Drury (1983), Jones & Ellison (1991) 的 CR 修正激波理论一致。
- **[FACT]** Figure 11：密度剖面（不同 $\vartheta$）。平行激波激波厚度更宽，$r_{\text{tot}} \approx 4.2$–$4.4$，系统大于极斜激波。

#### 6.3 [FACT] 谱指数对压缩比的敏感度

- **[FACT]** 非线性 DSA 预言谱可能呈 **concave**（凹）形状：高能粒子探测 $r_{\text{tot}} \approx 4.3 \Rightarrow E^{-1.43}$；低能粒子探测 $r_{\text{sub}} \Rightarrow E^{-1.5}$。
- **[FACT]** 两种谱斜率**难以分辨**（因 $E_{\max}$ 截断）——concave 效应在观测上尚未确认。
- **[FACT]** 历史上 SNR 观测从未**令人信服**地看到显著陡于/平于 $p^{-4}$ 的凹谱，即便在加速高效的源中（Caprioli 2012）。
- **[FACT]** 结论：向**相对论 regime** 扩展动力学模拟是**关键下一步**。

## 关键参数

| 参数 | 值 |
|---|---|
| $r_{\text{sub}}$（平行，$M=30$） | $\approx 3.65$ |
| $r_{\text{tot}}$（平行，$M=30$） | $\approx 4.23$ |
| $r_{\text{tot}}$（$M=30$ 极斜） | $\approx 4$（无 CR 修正） |
| 预言凹谱斜率（高能） | $E^{-1.43}$ |
| 标准 DSA 非相对论 | $E^{-1.5}$ |

## 我的理解 / Interpretation

**[INTERPRETATION]** §6 是**理论深度最厚的节**。CR 修正激波使 DSA 谱可能从 $p^{-4}$ 变凹——这是**非线性 DSA 的核心预言**，也是 Blasi 2013、Amato & Blasi 2014 关注的重点。作者指出模拟的相对论扩展是关键下一步——这一方向后来由 Blasi & D'Amico、Amato 等人继续推进。
