---
title: "2. Energy Reconstruction & Event Reconstruction"
paper: "Telescope Array Collaboration 2023, Amaterasu event"
outline_ref: "§Methods: Analysis Procedure and Energy Reconstruction"
original_sections: ["Energetic particle on 27 May 2021; Supplementary: Analysis Procedure and Energy Reconstruction"]
---

> 上一章：`01_introduction.md`
> 下一章：`03_direction_and_lss.md`

## 2.1 [FACT] Table 1 — 重建事件属性

| 字段 | 值 |
|------|-----|
| 日期 | 2021-05-27 |
| UTC 时间 | 10:35:56 |
| 能量 | $244^{+29 (\rm stat.)}_{-29 (\rm stat.)} \; {}^{+51}_{-76} (\rm syst.)$ EeV |
| $S_{800}$ | $530 \pm 57$ m$^{-2}$ |
| 天顶角 | $38.6 \pm 0.4°$ |
| 方位角 | $206.8 \pm 0.6°$ |
| 赤经 (R.A.) | $255.9 \pm 0.6°$ |
| 赤纬 (Dec.) | $16.1 \pm 0.5°$ |

## 2.2 [FACT] Figure 1 — 事件可视化

Figure 1A：TA SD 地面投影，事件簇射轨迹方向（黑色箭头）。**簇射核心**位于 SD 西北边缘 $1.1$ km 处（相对 SD 中心 $(-9471 \pm 31$ m, $1904 \pm 23$ m)）。触发 **$23$ 个探测器**。

Figure 1B：每个 SD 站的 FADC 波形，信号单位为 MIP（Minimum Ionizing Particle）等效。距轴最近（$0.3$ km）的 SD0418 信号高达 $5581.2$ MIP；$1.1$ km 处 SD0417 为 $393.6$ MIP。

## 2.3 [FACT] 能量重建链

**步骤 1 — 侧向密度拟合**（补充材料公式 S1/S2）：

$$\rho(r) = A \left(\frac{r}{r_M}\right)^{-\delta_1} \left[1 + \left(\frac{r - r_0(\theta)}{1000}\right)^2\right]^{-\delta_2}$$

其中 $\delta_1 = 1.2$, $\delta_2 = 0.6$, $r_M = 91.6$ m（Molière 单位），$\delta(\theta) = 3.97 - 1.79(\sec\theta - 1)$。

**步骤 2 — 原始 SD 能量**：假设质子 + QGSJet-II-03 模型，$S_{800} = 530$ m$^{-2}$ → **$309^{+37}_{-37}$ EeV**（统计）。

**步骤 3 — FD 校准**：乘 $1/1.27$ → **$244$ EeV**（校准到 FD 量热计能量标度）。

## 2.4 [FACT] 系统误差来源

| 误差来源 | 大小 | 方向 |
|---------|------|------|
| 统计误差 | $\pm 29$ EeV | 对称 |
| 迁移效应（低能→高能） | $-3\%$ | 向下 |
| 初级粒子未知 | $-10\%$ | 向下 |
| 系统误差（合计） | $+51 / -76$ EeV | 不对称 |

**总能量范围**（$2\sigma_{\rm stat} + \sigma_{\rm syst}$）：

$$E_{\min} = 244 - 58 - 76 = 110 \text{ EeV}; \quad E_{\max} = 244 + 58 + 51 = 353 \text{ EeV}$$

## 2.5 [FACT] 初级粒子识别

| 检查 | 结果 |
|------|------|
| 远端（$> 2$ km）探测器波形含多个 $\mu$ 子峰 | 符合强子级联（$p$ 或重核），**排除光子** |
| 神经网络 $p$-$\gamma$ 分类器（Kalashev 2021; Kharuk 2021） | **以 $99.986\%$ 置信度排除光子**，支持质子 |
| 重核 vs 质子区分 | **无法区分**——FD 因月光过亮未运行 |

## 2.6 [FACT] 其他系统排除

- **无闪电/雷暴**：Vaisala 数据确认 2021-05-27 无雷电活动
- **能量与 LHC 对比**：$244$ EeV $= 2.44 \times 10^{11}$ GeV，是 LHC 质子能量（$7$ TeV）的 $\sim 3.5 \times 10^7$ 倍
- **质心能量**（若为质子，与大气核子碰撞）：$\sqrt{s} \approx 700$ TeV，远超 LHC 的 $14$ TeV

## 2.7 [FACT] 不同强子模型的敏感度（补充材料）

| 模型 | 质子 (EeV) | 铁核 (EeV) |
|------|-----------|-----------|
| QGSJet-II-03（默认） | 309 | — |
| QGSJet-II-04 | 300 | 272 |
| EPOS-LHC | 261 | 240 |

物种差异 $\sim 10\%$ → 对应 $-10\%$ 系统误差。校准到 FD 后物种差异由校准因子补偿，但**距离计算对物种敏感**。

## 2.8 [INTERPRETATION] 我的理解

能量重建链条的关键在于 **$1/1.27$ FD 校准因子**：将 SD 原始能量（$309$ EeV）下调到 FD 量热计标度（$244$ EeV）。这一因子在 9 年数据中验证无能量依赖性。

**关键张力**：即使取系统误差下限 $E_{\min} \approx 110$ EeV，仍远超 GZK 抑制起始能量（$\sim 50$ EeV）——但接近 Auger 观测到的第一个 UHECR 事件能量范围。