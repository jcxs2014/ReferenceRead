# 8. Major Uncertainties（§4 主要不确定性）

**上一章**: [07_pies_superagb_fates.md](07_pies_superagb_fates.md) · **下一章**: [09_yield_tables.md](09_yield_tables.md)

## 8.1 Convection and the third dredge-up

### 8.1.1 对流边界判定
[FACT] 1D 恒星模型对流边界由 **Schwarzschild 判据** 判定；但实际恒星内部有混合层（convective overshoot、semiconvection）需要额外参数化。

[FACT] 对流超射（overshoot）的实现在不同恒星演化代码中差异巨大，直接影响：
- He 核心尺寸；
- ¹³C 袋深度与质量；
- λ（TDU 效率）；
- s-过程产额（对 Sr、Ba、Pb 特别敏感）。

### 8.1.2 对流引起的结构变化
[FACT] 对流边界附近的核反应区结构变化会反馈到 AGB 演化时标与产额。

## 8.2 Mass Loss（质量损失）

[FACT] AGB 质量损失率 $\dot{M}$ 决定恒星在包络耗尽前经历多少次 TDU。

[FACT] 参数化：
- Reimers (1975): $\dot{M} \propto L R / M$
- Blocker (1995): 用于 O 富星
- Vassiliadis & Wood (1994): Vw 关系（依赖包络质量）

[FACT] Spitzer 卫星观测揭示：低金属度下 C 富 AGB 的质量损失并不一定小于高 Z 值（因 C 富包络尘埃驱动更强）。

## 8.3 关键系统不确定性

| 参数 | 影响 | 当前状态 |
|-----|------|---------|
| 对流边界 (overshoot) | λ, ¹³C 袋, s-过程产额 | 未校准 |
| 半对流（semiconvection） | He 核尺寸 | 时标不确定 |
| 呼吸脉冲（breathing pulses） | He 核尺寸 | 观测不支持（Renzini & Fusi Pecci 1988） |
| 质量损失率 | TDU 次数 | 依赖经验公式 |
| ¹²C(α,γ)¹⁶O 反应率 | intershell C/O | 实验约束差 |

[CRITIQUE] 本文明确指出 §6 中的展望：对流与质量损失是所有 AGB 产额系统误差的两大主导源。
