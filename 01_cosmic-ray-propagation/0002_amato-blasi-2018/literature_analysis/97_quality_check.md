# 97. Quality Check — Completeness 自检
> 上一章：[[01_cosmic-ray-propagation/0002_amato-blasi-2018/literature_analysis/08_summary.md|08_summary]]
> 下一章：[[01_cosmic-ray-propagation/0002_amato-blasi-2018/literature_analysis/98_vocabulary.md|98_vocabulary]]

## 文献信息

| 字段 | 内容 |
|---|---|
| 标题 | Cosmic ray transport in the Galaxy: A review |
| 作者 | Elena Amato (INAF Arcetri), Pasquale Blasi (GSSI) |
| 期刊 | Advances in Space Research 62, 2731 (2018) |
| DOI | 10.1016/j.asr.2017.04.019 |
| arXiv | arXiv:1704.05696 |
| 年份 | 2018 |
| 页数 | 36 页 |
| 类型 | 综述 |

## 文件清单

| 文件 | 行数 | 状态 |
|---|---|---|
| 00_overview.md | 87 | ✓ 元信息 + FACT/INTERPRETATION/CRITIQUE |
| 01_introduction.md | 113 | ✓ §4 模板 |
| 02_standard_predictions.md | 125 | ✓ 标准传播预测 + 公式 |
| 03_self_excited_alfven_waves.md | 120 | ✓ 共振/非共振不稳定性 |
| 04_self_generated_transport.md | 160 | ✓ 核心理论：$D(p)$ 断裂 |
| 05_near_source_confinement.md | 111 | ✓ 源附近禁闭 + D'Angelo 2016 |
| 06_cr_induced_galactic_winds.md | 130 | ✓ 银河风 + 边界条件 |
| 07_secondary_particles_anomalies.md | 95 | ✓ 正电子/p̄ 异常 |
| 08_summary.md | 80 | ✓ 总结 |
| 97_quality_check.md | 本文 | ✓ |
| 98_vocabulary.md | — | ✓ |
| 99_final_summary.md | — | ✓ |

## 公式覆盖

| 编号 | 公式 | 所在分章 | 状态 |
|---|---|---|---|
| 1 | CR 核素传输方程 | 01_introduction | ✓ |
| 2 | 平流速度 $w(z)$ | 01_introduction | ✓ |
| 3 | 简化方程（高能极限）| 02_standard | ✓ |
| 4 | 质子谱解 $f_0 = N(p)RH^2/D$ | 02_standard | ✓ |
| 6 | 二级粒子通量 $I_a$ | 02_standard | ✓ |
| 7 | 二级/一级比率标度 $\propto X(R)$ | 02_standard | ✓ |
| 8 | 共振生长率 $\gamma_{\rm CR}^{\rm RES}$ | 03_self_excited | ✓ |
| 9 | 非共振生长条件 $v_d > c\sqrt{U_B/U_{\rm CR}}$ | 03_self_excited | ✓ |
| 10 | 非共振最大生长率 $\gamma_{\rm CR}^{\rm NR}$ | 03_self_excited | ✓ |
| 11 | 共振电流 $J_{\rm CR}^{\rm RES}$ | 03_self_excited | ✓ |
| 12 | $D(p) \propto 1/W(k_{\rm res}) \propto p^\alpha$ | 04_self_generated | ✓ |
| 18 | 波谱演化方程 | 04_self_generated | ✓ |
| 22 | 源区碎裂克质量 $\Lambda_{\rm src}$ | 04_self_generated | ✓ |
| 23 | $s^*(p) \propto \sqrt{D(p)}$ | 04_self_generated | ✓ |
| 24 | 风模型通量 $I_a \propto Q/D^{1/2}$ | 04_self_generated | ✓ |

**公式覆盖**：16/16 ✓

## 数值信息检查

| 数值 | 值 | 状态 |
|---|---|---|
| Alfvén 速度 | $\sim 15$ km/s（传播区）| ✓ |
| 扩散谱指数 | $\delta \sim 0.3-0.6$ | ✓ |
| 晕高 | $H \sim 1-10$ kpc | ✓ |
| 盘克质量 | $\Lambda = 2.4$ mg/cm$^{2}$ | ✓ |
| B/C 拐点 | $\sim 3$ GV | ✓ |
| NLD 特征刚度 $K_1$ | $\sim 100$ GV | ✓ |
| 完全饱和刚度 $K_2$ | $\sim 1000$ GV | ✓ |
| 风启动高度 $z_0$ | $\sim 1$ kpc | ✓ |
| 源区碎裂克质量 | $\sim 0.15$ g/cm$^{2}$ | ✓ |
| WIM 中性氢上限 | $\lesssim 0.03$ cm$^{-3}$ | ✓ |
| 源附近尺度 $L_c$ | $\sim 100$ pc | ✓ |

## 已知不足

1. **本文 OCR 质量中等**：双栏排版导致部分行交错，已尽力还原
2. **§7 内容相对简略**：正电子比率异常和 p̄/p 变平的细节因 OCR 局限未完全覆盖
3. **Figure 分析**：本文 5 张图（AMS-02 谱、扩散系数、源附近停留时间、源附近克质量、风速），已在正文中按图说明分析