> 本章属于：**The Astrophysics of Ultrahigh Energy Cosmic Rays** (Kotera & Olinto, 2011)
>
> 上一章：`01_1_introduction.md`
>
> 下一章：`03_3_propagation.md`

# §2 Cosmic Ray Observations at Ultrahigh Energies

## 1. 本节核心内容

系统综述 UHECR 三大可观测：能谱 (§2.1)、到达方向各向异性 (§2.2)、成分 (§2.3)。以 HiRes + Auger 联合为主，AGASA 为历史对照。结论：谱形支持河外起源 + GZK 截断；存在 hint 级各向异性；成分证据 (Auger) 指向重核，与 HiRes 结果有张力。

## 2. 原文内容

**宇宙线能谱的 broken power law**：
$$J(E) = J_0 \left(\frac{E}{E_0}\right)^{-s(E)}, \qquad s(E)=\begin{cases}2.7 & E\text{<}E_\mathrm{knee}\ (\approx 1\text{ PeV})\\ 3.0 & E_\mathrm{knee}\text{<}E\text{<}E_\mathrm{ankle}\ (\approx 3\text{ EeV})\\ 2.6 & E_\mathrm{ankle}\text{<}E\text{<}E_\mathrm{GZK}\ (\approx 30\text{ EeV})\end{cases}$$
积分通量 $I(>E) = \int_E^\infty J(E')\,dE' = \frac{J_0\,E_0^{s}}{s-1}\left(\frac{E_0}{E}\right)^{s-1}$（$s>1$）。

**Auger 曝光量**：$L = A_\mathrm{eff}\,\Omega\,T$，其中 $A_\mathrm{eff}\approx 3000\text{ km}^2$，$\Omega = 2\pi\text{ sr}$（南半天球），$T$ 为运行时间；单位 Linsley（1 L = 1 km²·sr·yr）。

## §2.1 Spectrum

[FACT] 观测站历史：AGASA (100 km², 1.6×10³ L₁)；HiRes (荧光望远镜，~3200 L₁)；Fly's Eye 首测 320 EeV 事件 (Linsley 1963, Bird et al. 1994)；Pierre Auger Observatory (2008 完工, 3000 km², 1.5 km 间距水切伦科夫阵列 + 4 台荧光望远镜, 18 国合作)；Telescope Array (762 km², 1.2 km 间距, Utah, 3 台荧光)。

[FACT] 宇宙线能谱近似为 broken power law $E^{-s}$：
- < knee (~1 PeV): s ≈ 2.7
- knee → ankle (~3 EeV): s ≈ 3
- 踝点以上: s ≈ 2.6
- > 30 EeV: 通量抑制 (GZK)

能量损失的 GZK 特征可用 $\lambda(E) = \epsilon(E) / \left|\mathrm{d}E/\mathrm{d}t\right|$ 表达：当光致π产生的能量损失率 $-\mathrm{d}E/\mathrm{d}t|_\pi \propto E$ 超过宇宙膨胀红移损失率 $\dot{E}_\mathrm{cosm}=HE$ 时（$E\gtrsim 50$ EeV），$\lambda$ 骤降 → 通量陡降。

**Heaviside 型注入 + GZK 截断近似**：观测谱可参数化为
$$E^{2.7}\,J(E) \propto E^{2.7-s_0}\left(1 + \frac{E}{E_\mathrm{cut}}\right)^{-\gamma},$$
混合/Fe 模型：$s_0\approx 2.1,\,E_\mathrm{cut}\sim 10^{20}\text{ eV},\,\gamma\approx 1.5$；dip 模型 $s_0\approx 2.0$ 但在 $E\sim 4\times10^{18}$ eV 处引入额外 "dip"。

## §2.2 Anisotropies

**点源角分辨的 rigidity 依赖**：对 rigidity $\mathcal{R}=E/Z$ 粒子，穿过 $D$ 距离、磁场 $B$、相干长度 $l_B$ 后的均方偏转角近似
$$\langle\theta^2\rangle \simeq 4.6\left(\frac{B}{10^{-9}\text{ G}}\right)^2\left(\frac{l_B}{10\text{ kpc}}\right)\left(\frac{D}{100\text{ Mpc}}\right)\left(\frac{100\text{ EeV}}{Z\,\mathcal{R}}\right)^2,$$
在 $D\sim 100$ Mpc、$B\sim 10^{-9}$ G 下质子偏转 ≲10°，Fe (Z=26) 偏转 ≲2°/26 ≈ 0.1°——**偏转角随 Z 增大反而减小**，但成分变重对能量损失的惩罚更大。

[FACT] 拟合模型 (Kotera et al. 2010b)：
- **混合/Fe 主导模型** (Allard et al. 2007)：踝点是银河→河外转换；SFR 演化；注入 s ≈ 2–2.1
- **Dip 模型** (Berezinsky et al. 2006)：踝点是质子对产生传播损失 (Berezinsky & Grigorieva 1988)；注入 s 更软
- 质子主导 + 硬注入：踝点处转换 (Wibig & Wolfendale 2004)

## §2.2 Anisotropies

[FACT] GZK 视界 ~100 Mpc：trans-GZK 事件可观测源必须在此距离内 (Harari et al. 2006; Allard et al. 2007)。轻核在 CMB/IR-UV 光子上迅速光致离解；只有 protons 与 iron 能存活到 ~100 Mpc。

[FACT] Auger 2007 首次：27 个 ≥57 EeV 事件与 VCV AGN 目录 (z < 0.018, d < 75 Mpc) 在 3.1° 内相关，20/27 相关，>99% CL。HiRes 北天 13 个事件与 isotropy 一致 (Abbasi et al. 2008c)。

[FACT] 2010 更新 (Abreu et al. 2010)：69 个 ≥55 EeV 事件；20/27 旧事件相关 vs 12/42 新事件相关 → 相关性减弱；38% 相关率，5σ 需再 4 年 Auger 数据。

[FACT] 替代目录：Swift-BAT AGN (Tueller et al. 2010)、2MRS 星系 (Huchra et al. 2005, 22000 星系 <200 Mpc)；Auger 事件与 2MRS 分布比 isotropy 更契合，但源类识别尚难。

[FACT] **Cen A 聚集**：Auger 事件在 Cen A 方向 (3.8 Mpc) 聚集；可能是最近 AGN，也可能是 Centaurus 星系团。高统计量才能区分。

## §2.3 Composition

[FACT] Xmax (g/cm²) 是最佳成分指标：Xmax ∝ ln(E/A)。质子 Xmax 深于铁同能量。质子 showers 涨落更大 → RMS(Xmax) 也是成分指标。μ 子数：质子 showers μ 子少于重核 showers。

**Xmax 与 RMS 解析关系**：
$$X_\mathrm{max} \approx X_0 \ln\!\left(\frac{E}{E_\mathrm{cr}(A)}\right), \qquad \sigma(X_\mathrm{max})^2 \approx \eta^2 \sigma_\mathrm{fluct}^2$$
其中 $X_0 = 80\text{ g/cm}^2$ 为海平面空气辐射长度，$E_\mathrm{cr}(A) \sim A\cdot E_\mathrm{cr}(1)$。对质子 showers 涨落因子 $\eta_p^2\approx 2.4$，对 Fe $\eta_\mathrm{Fe}^2 \approx 2.4/36$，故同能下质子 showers 的 Xmax 离散显著大于铁。

**μ 子数经验公式**（Heinz & Rathgeb 1998，被 Auger 广泛引用）：
$$N_\mu \approx 0.92\,\frac{E}{E_0}\left(\frac{E}{A\,E_0}\right)^{0.85-1}, \qquad E_0 \simeq 800\text{ TeV}$$
质子 showers $N_\mu \propto E^{0.85}$；重核 $N_\mu \propto E$，因此 μ 子数 / 能量比是成分判别的强判据。

**Rigidity (刚度)**：
$$\mathcal{R} = \frac{p}{Ze} \approx \frac{E}{Z}$$
Galactic 截断为 rigidity cutoff（而非 energy cutoff）→ 膝点随 A 平移 → 重核膝点在 $A\times E_\mathrm{knee}(p)$ 处。

[FACT] 膝点到踝点以下：轻→重的趋势，符合 rigidity 依赖的银河宇宙线 Emax / 银河磁场约束 (Lemoine 2005; Hillas 2006)。

[FACT] Auger 3754 事件 (≥1 EeV)：~1 EeV 处轻核主导，与 HiRes 815 事件 (Abbasi et al. 2010) 一致。**10 EeV 以上出现重核趋势到 40 EeV**（Xmax 与 RMS(Xmax) 同时），窄 RMS 排除"多核混合"解释 → 重核主导。

[FACT] 拟合问题：重核注入需硬注入谱 (s ≈ 1.6) 与 N/Si 主导 (Hooper & Taylor 2010)。替代解释 (Allard et al. 2008; Aloisio et al. 2009)：质子 Emax 低，30 EeV 以上陡降其实是 Fe Emax ≈ GZK，"巧合"。

[FACT] 光子分数上限 → 排除暗物质衰变 / 拓扑缺陷模型。初粒子非光子 (Abraham et al. 2008; 2009c) 非中微子 (Abraham et al. 2009a; Abbasi et al. 2008a)。

## 3. 关键公式

- 谱指数：dN/dE ∝ E⁻ˢ，s ∈ {2.7 (膝点下), 3 (膝-踝), 2.6 (踝以上)}
- Xmax ∝ ln(E/A)
- Rigidity：R = p/Z ≈ E/Z
- Auger 事件计数：27 (原始)/69 (更新) ≥55 EeV

## 4. 关键参数

| 数值 | 单位 | 含义 |
|------|------|------|
| 30 EeV | 能量 | GZK 截断起点 |
| 142 EeV | 能量 | Auger 最高能事件 (2010) |
| 320 EeV | 能量 | Fly's Eye 历史最高 (1994) |
| 1.3×10⁴ L | 曝光 | Auger (Abraham et al. 2010b) |
| 3000 km² | 面积 | Auger 阵列 |
| 3.1° | 角 | Auger-VCV 相关窗口 |
| 38% | 相关率 | Auger 69 事件 / VCV |
| 3.8 Mpc | 距离 | Cen A |
| ~100 Mpc | 距离 | GZK 视界 |
| 22% | 系统误差 | Auger 能量刻度 |

## 5. 图表分析

- **Fig 2 (E³·flux)**：HiRes + Auger 数据 vs 混合 / Fe / dip 模型拟合。混合和 Fe 模型用 SFR 演化 + 硬注入 s≈2-2.1；dip 模型用软注入。两模型拟合相同观测谱但成分预测不同。
- **Fig 4 (存活率)**：proton >40, 60, 100 EeV + He, CNO, Fe >60 EeV 的存活率 vs 距离。trans-GZK 只有 p 与 Fe 存活到 ~50-100 Mpc。
- **Fig 5 (Auger 69 事件 Aitoff)**：叠加 2MRS <200 Mpc 22000 星系密度图，|b|>10°；事件明显偏向高密度区，但无显著单源。
- **Fig 6 (Xmax + RMS vs E)**：Auger 3754 事件 + MC 模拟（proton 蓝、Fe 红，多 hadronic model）。10 EeV 以上明显向 Fe 端移动。

## 6. 作者的逻辑

观测现状 → 谱 (已确定 GZK 截断) → 各向异性 (已见 hint，但源未识别) → 成分 (Auger 见重核，与 HiRes 张力) → 三个观测的交叉信息 → 引出 §3 传播物理 (解释观测) → §6 多信使 (解开谜题)。

## 7. 我的理解

[INTERPRETATION] 作者对"Auger 重核 vs HiRes 轻核"张力持**开放**立场，明确给出两种合理但"令人失望"的替代解释：(1) 质子 Emax 低 + Fe Emax 巧合 ≈ GZK，(2) 100 TeV c.m. 以上强子相互作用变化。这是对观测不自信的诚实表达，也是综述的学术价值——把不同解释的代价摆出，让未来数据裁决。

## 8. 潜在问题与值得关注的地方

- [CRITIQUE] 38% 相关率本身不高，且依赖 VCV 这个"汇编目录"而非仪器巡天。
- [CRITIQUE] 40 EeV 以上 Auger 数据量有限，"重核"判读高度依赖 hadronic model 外推 (EPOS/Sibyl/QGSJET)——2017 以后 Auger 用 QGSJETII-4 更新后，趋势部分保留但减弱。
- [FACT] 作者明确说"the situation is currently unclear"——这是 2011 年的真实状态。
- [FACT] Auger-North、TALE、JEM-EUSO、AMIGA、HEAT 是后续观测路线图。
