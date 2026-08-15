# 97. Quality Check — Completeness 自检
> 上一章：[[02_cosmic-ray-origins/0010_blandford-eichler-1987/literature_analysis/07_summary.md|07_summary]]
> 下一章：[[02_cosmic-ray-origins/0010_blandford-eichler-1987/literature_analysis/98_vocabulary.md|98_vocabulary]]

## 文献信息

| 字段 | 内容 |
|---|---|
| 标题 | Particle Acceleration at Astrophysical Shocks: A Theory of Cosmic Ray Origin |
| 作者 | Roger Blandford (Caltech), David Eichler (Maryland / Ben Gurion) |
| 期刊 | Physics Reports (Review Section of Physics Letters), 154, No. 1 |
| 年份 | 1987 |
| DOI | — |
| arXiv | — |
| 页数 | 75 页 (1-75) |
| 参考文献数 | 28 篇 |
| 类型 | 综述 |

## 文件清单

| 文件 | 行数 | 状态 |
|---|---|---|
| 00_overview.md | 144 | ✓ 元信息 + 摘要 + 结构表 |
| 01_introduction.md | 106 | ✓ §4 模板（8 子节）|
| 02_observational_background.md | 204 | ✓ 九类环境详述 + Figure 分析 |
| 03_diffusion_approximation.md | 217 | ✓ 完整数学推导（Vlasov → Fokker-Planck）|
| 04_test_particle_approximation.md | 179 | ✓ 测试粒子幂律推导 |
| 05_wave_spectrum.md | 162 | ✓ 波谱 + 自激发推导 |
| 06_nonlinear_theory.md | 175 | ✓ 非线性自洽理论 |
| 07_summary.md | 143 | ✓ 总结 + 未来方向 |
| 97_quality_check.md | — | ✓ 本文 |
| 98_vocabulary.md | 137 | ✓ A 逻辑词 + B 术语 + C 长难句 |
| 99_final_summary.md | 149 | ✓ 核心结论 + 数值速查 |

## 公式覆盖（对照 fulltext）

| 编号 | 公式 | 所在分章 | 状态 |
|---|---|---|---|
| 2.1 | $J(T) \propto T^{-2.7}$ | 02_observational | ✓ |
| 2.2 | $\lambda_{\rm esc} \sim 20\,T^{-0.5}$ g/cm$^{2}$ | 02_observational | ✓ |
| 2.3 | Sedov-Taylor 解 | 02_observational | ✓ |
| 3.1 | 相对论性 Vlasov 方程 | 03_diffusion | ✓ |
| 3.2 | $dN/dE \propto E^{-\gamma}$ | 03_diffusion | ✓ |
| 3.4 | Fokker-Planck 方程 | 03_diffusion | ✓ |
| 3.5 | Fokker-Planck 系数 | 03_diffusion | ✓ |
| 3.6 | 简化 FP 方程 | 03_diffusion | ✓ |
| 3.8 | 动量空间扩散方程 | 03_diffusion | ✓ |
| 3.12 | $V_A = B/\sqrt{4\pi\rho}$ | 03_diffusion | ✓ |
| 3.16 | 方位角扩散 $D_{\mu\mu}$ | 03_diffusion | ✓ |
| 3.20 | 垂直扩散 $D_\perp$ | 03_diffusion | ✓ |
| 3.21 | 磁场线游荡 | 03_diffusion | ✓ |
| 4.1 | Rankine-Hugoniot 跳跃条件 | 04_test_particle | ✓ |
| **核心** | **$q = 3r/(r-1)$** | **04_test_particle** | **✓** |
| — | $t_{\rm est} \sim r^2/(\nu u_-^2)$ | 04_test_particle | ✓ |
| 5.1 | $D_\parallel \propto v p^{2+\alpha}$ | 05_wave | ✓ |
| 5.2 | 线性化 Vlasov（波场中）| 05_wave | ✓ |
| 5.4 | 垂直电流 $j_\perp$ | 05_wave | ✓ |
| 5.6 | Plemelj 共振电流 | 05_wave | ✓ |
| 6.1 | $\rho u = C_1$ | 06_nonlinear | ✓ |
| 6.2 | $P + \rho u^2 = C_2$ | 06_nonlinear | ✓ |
| — | $r = r_{\rm prec} \times r_{\rm sub}$ | 06_nonlinear | ✓ |
| — | $\eta = P_{\rm cr}/P_{\rm tot}$ | 06_nonlinear | ✓ |

**公式覆盖**：24/24 ✓

## 图 / 表覆盖

| Figure | 内容 | 分析所在分章 | 状态 |
|---|---|---|---|
| Fig. 1 | 地球弓激波结构 | 02_observational | ✓ |
| Fig. 2 | 日球内加速位点 | 02_observational | ✓ |
| Fig. 3 | 银河系 CR 能谱 | 02_observational | ✓ |
| Fig. 4 | Tycho SNR X 射线 vs 射电 | 02_observational | ✓ |
| (本文更多 Fig 在 OCR 中被截断) | — | — | 已标注 |

## 数值信息检查

| 数值 | 值 | 状态 |
|---|---|---|
| 超新星能量 | $10^{51}$ erg | ✓ |
| 银河系 CR 能量密度 | $(1-2) \times 10^{-12}$ erg/cm$^{3}$ | ✓ |
| 银河系 CR 总功率 | $3 \times 10^{41}$ erg/s | ✓ |
| 单 SNR CR 注入 | $\sim 3 \times 10^{49}$ erg（$3\%$）| ✓ |
| CR 观测谱 | $T^{-2.7}$ | ✓ |
| 逃逸柱密度 | $\lambda \sim 20 T^{-0.5}$ g/cm$^{2}$ | ✓ |
| CR 年龄 | $\sim 20$ Myr | ✓ |
| SNR 加速半径 | $1-50$ pc | ✓ |
| SNR 高能截断 | $10^{15}$ eV | ✓ |
| Alfvén 速度 | $\sim 50$ km/s | ✓ |
| 压缩比（强激波）| $r = 4$ | ✓ |
| 谱指数（DSA 预测）| $q = 4$ | ✓ |
| 谱指数（观测）| $4.5$ | ✓ |

## 已知不足

1. **本文 OCR 质量中等**：部分公式符号（特别是张量记号）在 OCR 中变形，已在正文中标注
2. **§6 部分推导在 OCR 中不完整**：公式编号可能遗漏若干，但物理图像和关键结论已完整
3. **本文有 30+ 张 Figure**，OCR 仅保留了少数图的说明，部分图的分析基于说明文字而非图本身
4. **98_vocabulary.md**：B 类术语基于 OCR 文本提取，可结合 PDF 原版补充