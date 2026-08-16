---
title: "§4 ACCELERATION EFFICIENCY"
paper: "Caprioli & Spitkovsky 2014, ApJ 783, 91"
outline_ref: "§4 ACCELERATION EFFICIENCY"
---
> 上一章：[[02_cosmic-ray-origins/0016_caprioli-2014/literature_analysis/03_supra_thermal_particles.md|03_supra_thermal_particles]]
> 下一章：[[02_cosmic-ray-origins/0016_caprioli-2014/literature_analysis/05_magnetic_field_amplification.md|05_magnetic_field_amplification]]

#### 4.1 [FACT] 效率参数空间（Figure 3）

- **[FACT]** 大盒子模拟 $(L_x, L_y) = (40000, 500) [c/\omega_p]^2$；2 cells per skin depth；4 particles/cell；$\Delta t = (0.01/M) \omega_c^{-1}$（恒 Courant）；演化至 $t = 200 \omega_c^{-1}$。
- **[FACT]** 参数：$\vartheta = 0°, 20°, 30°, 45°, 50°, 60°, 80°$；$M = 5, 10, 30, 50$。
- **[FACT]** 大盒子原因：filamentation 不稳定性需要（CS13）；大 $M$ 需要小步长以保证显式 hybrid 能量守恒。

#### 4.2 [FACT] 效率定义与主要发现

- **[FACT]** 加速效率 $\epsilon$ 定义为 $t = 200 \omega_c^{-1}$ 时下游能量密度中 $E \ge 10 E_{\text{sh}}$ 的粒子占比。
- **[FACT]** Figure 3：$\epsilon$ 随 $\vartheta$ 变化。**$\vartheta \gtrsim 45°$ 急剧下降**；最大效率出现在**快、平行**激波。
- **[FACT]** 收敛性检查：$E_{\max}$ 的指数截断形式在 $t = 200\omega_c^{-1}$ 与 $t = 400\omega_c^{-1}$ 之间已收敛；效率随时间的收敛在较后期 $t \gtrsim 200 \omega_c^{-1}$。
- **[FACT]** Mach 数依赖：$M \gtrsim 30$ 时 $\epsilon$ 几乎饱和。
- **[FACT]** 准平行强激波 $\epsilon \approx 10\%-20\%$；准垂直激波几乎为零。

## 关键数值（摘录自图 3 及正文）

| $\vartheta$ | $M=5$ | $M=10$ | $M=30$ | $M=50$ |
|---|---|---|---|---|
| 0° | ~10% | ~15% | ~17% | ~19% |
| 20° | ~5% | ~12% | ~15% | ~17% |
| 30° | ~2% | ~8% | ~12% | ~14% |
| 45° | ~1% | ~4% | ~8% | ~10% |
| 50° | ~0.5% | ~2% | ~4% | ~5% |
| 60° | ~0.3% | ~1% | ~2% | ~3% |
| 80° | ~0.1% | ~0.3% | ~0.7% | ~1% |

（具体数值为正文趋势的近似；原文以 Figure 3 曲线给出，此处用于量级参考。）

## 图表分析

### Figure 3
- **目的**：展示加速效率随激波倾角 $\vartheta$ 与 Mach 数 $M$ 的二维依赖。
- **横轴**：$\vartheta$（°）；**纵轴**：Efficiency (%)。
- **四条曲线**：$M = 5, 10, 30, 50$。
- **关键观察**：所有 Mach 数在 $\vartheta \approx 45°$ 处呈现"膝"；$M=5$ 全区间弱；$M=50$ 平行效率接近 20%。
- **作者解释**：快、平行激波效率最大；倾角是决定性因素，超过临界值后效率骤降。

## 我的理解 / Interpretation

**[INTERPRETATION]** §4 是**整篇论文定量最有用的节**：给出 $\epsilon(\vartheta, M)$ 的完整参数空间。这直接回答了 SNR 范式中的关键问题——**在什么条件下加速有效**。作者强调效率在 $\vartheta \approx 45°$ 附近出现"phase transition"——这一临界倾角与图 7 DSA/SDA 过渡完全一致。Baade & Zwicky 的 10% 能量学约束在**平行强激波**区段得到自洽支持。
