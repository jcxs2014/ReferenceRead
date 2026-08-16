> 本章属于：[[./00_overview.md|Busso, Gallino & Wasserburg (1999)]]
> 上一章：[[./03_agb_and_slow_n_capture.md|03 Agb And Slow N Capture]]
> 下一章：[[./05_radiative_13C_burning.md|05 Radiative 13C Burning]]

# 4. Evolution and Nucleosynthesis in Low-Mass AGB Stars

**本章作者**：M. Busso, R. Gallino, G. J. Wasserburg  
**原文映射**：Sec. 4. EVOLUTION AND NUCLEOSYNTHESIS IN LOW-MASS AGB STARS (p. 260–264)

sections:
  - 4.1 第一代低质量星核合成模型
  - 4.2 现代改进：低质量碳星的形成
  - 4.3 13C pocket 的形成机制（Iben & Renzini 1982a,b 方案）
  - 4.4 中子源之争：13C(α,n) vs 22Ne(α,n)

## 4.1 第一代低质量星核合成模型

[FACT] 1970s–1980s 的低质量 AGB 模型 (Hollowell & Iben 1988, 1989, 1990) 的核心要素：
- He 燃烧期间用 13C(α,n)16O 释放中子
- 13C 由半对流混合 / 超射 / He 闪后 H 摄取形成
- **13C 在对流脉冲期间燃烧**（旧假设）
- 13C 燃烧的能量被释放，触发对流
- 中子曝露分布近似指数

## 4.2 现代改进：低质量碳星的形成

[FACT] Straniero et al (1995, 1997) 用**高分辨率数值方案 + 改进不透明度 + 仅 Schwarzschild 判据** 重新做了低质量 AGB 模型：
- 第三次挖掘层 (TDU) 在 2-M☉ 模型中第 11 次脉冲后启动，在 3-M☉ 模型中第 9 次脉冲后启动
- **13C 在辐射条件下自然燃烧**——不需要对流脉冲介入
- 模型可以在适当光度下自洽形成**低质量碳星**，与观测吻合 (Wallerstein & Knapp 1998)

[FACT] H 重新点燃时 He 夹层温度快速达到 ~0.8–0.9 × 10⁸ K，13C 的 (α,n) 时标 τ₁₃,α 远小于脉冲间隔 (几万年前)。**13C pocket 中的 13C 在下一个脉冲到达前已被辐射燃烧干净**。

[INTERPRETATION] 这从根本上改变了中子曝露的**时间分布**：不再是对流脉冲内的瞬时爆发，而是长间隔辐射条件下的持续辐照。

## 4.3 13C pocket 的形成机制

[FACT] **Iben & Renzini (1982a,b) 半对流方案**：
1. 每次热脉冲冷却、膨胀阶段 → C 富物质进入低温区
2. C 的部分复合 (partial C recombination) 使局部不透明度急增
3. 可能形成**半对流层 (semiconvective layer)**
4. 少量氢被"挖掘 (dredged)"到富 C 区域
5. H 重新点燃时 12C(p,γ)13N(β+ν)13C(p,γ)14N 消耗所有 H
6. 留下 ~10⁻⁴ M☉ 的 13C (和 14N) pocket

[FACT] 该 pocket 在**下一个对流脉冲到来前**已被辐射燃烧——13C(α,n)16O 释放中子 (见 §5)。

[CRITIQUE] **13C pocket 的确切形成机制在 1999 年仍未解决**：
- 半对流混合参数化依赖不透明度与对流边界
- 超射 (overshooting) 尺度自由
- He 闪后 H 摄取方案（已被证伪，因能量释放问题 Bazan & Lattanzio 1993）
- 本文在 §8 结论中明确指出：13C pocket 至今仍"作为参数选择以拟合观测数据"

## 4.4 中子源之争：13C(α,n) vs 22Ne(α,n)

[FACT] 两种中子源在 AGB 中的相对重要性是本文的核心问题：
| 中子源 | 条件 | 中子密度 | 主导质量区 |
|---|---|---|---|
| 13C(α,n)16O | 辐射燃烧，T ~ 0.9 × 10⁸ K | ≤ 10⁷ cm⁻³ | A=85–209 主成分 |
| 22Ne(α,n)25Mg | 对流脉冲，T ~ 3 × 10⁸ K | ~5 × 10¹⁰ cm⁻³ | 分支点产物、60Fe、r 近邻同位素 |

[FACT] **13C pocket 在每次 TDU 后形成**——少量质子穿透到 He 夹层顶层 → H 重新点燃 → 12C(p,γ)13C 反应生成 13C pocket。

[FACT] **22Ne 由 H shell CNO 循环产生的 14N → He 壳 14N(α,γ)18F(β+)18O(α,γ)22Ne 链** 在 He 燃烧时积累。IMS 中 22Ne 源自动激活。

[FACT] 13C 反应率的实验更新 (Denker et al 1995) 使反应率比 Caughlan & Fowler (1988) 高 2 倍——对 s 过程结果有重要影响。



[FORMULAS] 13C pocket 与中子源方程：

- **13C 生成链**：$^{12}{\rm C}(p,\gamma)^{13}{\rm N}(\beta^+\nu)e^{+}^{13}{\rm C}(p,\gamma)^{14}{\rm N}$；在 $T\sim(0.8\text{-}0.9)\times10^8$ K 时全部 H 被烧光，残留 13C（原文 p.260）。
- **13C pocket 质量（ST）**：$M(^{13}{\rm C})\approx 3\times 10^{-6}\,M_{\odot}/{\rm pulse}$（Gallino et al 1998；原文 p.265）。
- **H 注入上界**：$X_{\rm H}\le 0.0015$，即 $N_{\rm H}/N_{^{12}{\rm C}}<0.1$（原文 p.265）。
- **13C 燃烧中子源反应**：$^{13}{\rm C}(\alpha,n)^{16}{\rm O}$，$Q=2.21\ {\rm MeV}$；$T\sim 0.9\times10^8$ K（原文 p.255）。
- **22Ne 生成链**：$^{14}{\rm N}(\alpha,\gamma)^{18}{\rm F}(\beta^+\nu)e^{+}^{18}{\rm O}(\alpha,\gamma)^{22}{\rm Ne}$（原文 p.260）。
- **22Ne 中子源反应**：$^{22}{\rm Ne}(\alpha,n)^{25}{\rm Mg}$，$Q=4.71\ {\rm MeV}$；$T\gtrsim 3\times10^8$ K（原文 p.255）。
- **13C 燃烧中子密度**：$N_n\lesssim 10^7\ {\rm cm^{-3}}$（原文 p.255）。
- **22Ne 燃烧中子密度**：$N_n\sim 5\times10^{10}\ {\rm cm^{-3}}$（原文 p.265）。
- **13C 对流燃烧（旧模型）的 Nn 上限**：$N_n\approx (4\text{-}10)\times10^8\ {\rm cm^{-3}}$（原文 p.262）。
- **22Ne 反应率更新**：$\lambda(^{22}{\rm Ne}(\alpha,n))\uparrow\times3$ 相对 Caughlan & Fowler 1988；排除 633 keV 共振（原文 p.265）。
- **13C 反应率更新**：$\lambda(^{13}{\rm C}(\alpha,n))\uparrow\times2$（Denker et al 1995；原文 p.260）。
- **混合长度参数**：$\alpha\equiv l/H_P=1.5\text{-}2.1$（太阳模型匹配要求；原文 p.251、p.263）。
- **3-M☉ TDU 触发核心质量**：$M_{\rm H}\gtrsim 0.63\,M_{\odot}$；C 星阶段在第 11–26 次脉冲出现（原文 p.263、p.249）。
- **2-M☉ 模型 TDU 起始脉冲数**：$N_{\rm TP}^{\rm TDU}\approx 11$（原文 p.263）。
- **3-M☉ 模型 TDU 起始脉冲数**：$N_{\rm TP}^{\rm TDU}\approx 9$（原文 p.263）。

## 4.5 与相关文献的交叉

- [[03_stellar-nucleosynthesis/0004_wallerstein-1997/literature_analysis/07_s_process.md|Wallerstein et al. 1997 §X]]：提供了 s 过程现象学框架
- [[03_stellar-nucleosynthesis/0005_champagne-wiescher-1992/literature_analysis/00_overview|Champagne & Wiescher 1992]]：13C(α,n)16O 反应率的实验
- [[03_stellar-nucleosynthesis/0021_karakas-lattanzio-2014/literature_analysis/00_overview|Karakas & Lattanzio 2014]]：继续完善低质量 AGB 演化与 13C pocket 建模