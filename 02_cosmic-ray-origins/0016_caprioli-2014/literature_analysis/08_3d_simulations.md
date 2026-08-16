---
title: "§8 3D SIMULATIONS"
paper: "Caprioli & Spitkovsky 2014, ApJ 783, 91"
outline_ref: "§8 3D SIMULATIONS"
---
> 上一章：[[02_cosmic-ray-origins/0016_caprioli-2014/literature_analysis/07_dsa_versus_sda.md|07_dsa_versus_sda]]
> 下一章：[[02_cosmic-ray-origins/0016_caprioli-2014/literature_analysis/09_conclusions.md|09_conclusions]]

#### 8.1 [FACT] 3D 模拟设置

- **[FACT]** 目的：排除 2D 结果的**降维假象**，特别是 cross-field diffusion（仅 3D 存在）对注入的作用（Baring et al. 1995; Giacalone & Ellison 2000）。
- **[FACT]** 参数：$M = 6$；$\vartheta = 0°, 45°, 80°$。
- **[FACT]** 盒子 $(L_x, L_y, L_z) = (2000, 200, 200) [c/\omega_p]^3$；2 cells per skin depth；8 particles/cell；$\Delta t = 0.01 \omega_c^{-1}$。

#### 8.2 [FACT] 3D 结果（Figure 13）

- **[FACT]** 加速效率随倾角的变化趋势**与 2D 一致**：$\epsilon_{\text{CR}} \approx 12\%, 3\%, 1\%$ 分别对应 $\vartheta = 0°, 45°, 80°$。
- **[FACT]** DSA 在极斜激波的**失效被 3D 确认**——尽管精确计入磁场拓扑。
- **[FACT]** 大量离子重穿激波经历 SDA，但**没有任何粒子**进入 DSA + 磁场放大的高效区。
- **[FACT]** $E_{\max}$ 在 3D 极斜情形同样不随时间增长。
- **[FACT]** 结论：2D 结果**稳健**；3D 并未带来定性新物理。

## 关键参数

| 参数 | 2D（主模拟） | 3D |
|---|---|---|
| Box | $(40000, 500)$ | $(2000, 200, 200)$ |
| Particles/cell | 4 | 8 |
| $\Delta t$ | $0.01/M \, \omega_c^{-1}$ | $0.01 \, \omega_c^{-1}$ |
| 主要参数空间 | $M=5,10,30,50$；7 倾角 | $M=6$；3 倾角 |
| 效率 $\vartheta=0°$ | ~15% | 12% |
| 效率 $\vartheta=45°$ | ~8% | 3% |
| 效率 $\vartheta=80°$ | ~1% | 1% |

## 我的理解 / Interpretation

**[INTERPRETATION]** §8 是**方法严谨性的保证**——3D 验证 2D 结果不因降维而失真，特别是排除了"cross-field diffusion 在 3D 下可能改变注入"这一潜在质疑。3D 与 2D 的一致性为整个工作的可靠性背书。
