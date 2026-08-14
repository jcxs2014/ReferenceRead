# 7. Results and Discussion — 结果与讨论

> 本章属于：Gies & Lambert (1992) — ApJ 387:673
>
> 上一章：[[03_stellar-nucleosynthesis/0010_gies-lambert-1992/literature_analysis/06_nlte_abundances.md|06_nlte_abundances.md]]
>
> 下一章：[[03_stellar-nucleosynthesis/0010_gies-lambert-1992/literature_analysis/08_figures_tables.md|08_figures_tables.md]]

---

## 7.1 Temperature Scale — 温度尺度修正（§ 7.1）

### 7.1.1 现象

[FACT] 观察 non-LTE 与 LTE 的 C II、N II、O II 丰度随 T_eff 分布（图 11–13），发现**清晰的单调趋势**：
- **C II**：丰度随 T_eff 增加而**下降**；
- **N II**：同上；
- **O II**：同上。

[FACT] N II 趋势**可能**是演化效应（样本冷端偏向演化星），但 C II 与 O II 也显示同样趋势 → **不是演化**，而是 T_eff 尺度有系统偏差。

[FACT] **物理解释**：C II、N II、O II 每条线在观测 T_eff 范围内达到**最大 EW**；若 T_eff 被系统性低估，丰度会随 T_eff 单调下降（因为丰度 = 反推 EW，EW 在峰值温度附近的导数随温度单调变化）。

### 7.1.2 修正方法

#### 式 (7)

$$\Delta\log\varepsilon = \frac{\partial W_\lambda/\partial T_\text{eff}}{\partial W_\lambda/\partial\log\varepsilon}\,\Delta T_\text{eff}$$

偏导表达 EW 对温度与丰度的变化率。

[FACT] 最简单选择 ΔT_eff = 常数，但作者改用 **ΔT_eff = f · T_eff**（分数修正），因部分趋势在热端更陡。

#### 式 (8)

$$\log\varepsilon(T_\text{eff}) = \langle\log\varepsilon\rangle + f\left[\frac{\partial W_\lambda}{\partial T_\text{eff}}\frac{\partial\log\varepsilon}{\partial W_\lambda}\right]_{T_\text{eff}}$$

- 方括号项用 T_eff = 15,000–33,000 K 网格计算；
- 偏导基于 log g = 4.0、ξ = 5 km s⁻¹、太阳丰度的 EW 表（WIDTH6 LTE 或 Becker & Butler non-LTE）；
- 方括号项在**最大 EW 温度**处 = 0，因此该温度下的 log ε 定义了均值 ⟨log ε⟩；
- 用 Bevington (1969) CURFIT 做最小二乘拟合（去除超巨星）。

### 7.1.3 关键结果

[FACT] **最佳拟合分数修正**（Table 10）：

| 线物种 | f (LTE) | f (NLTE) |
|--------|---------|----------|
| He I   | —       | 0.025    |
| C II   | 0.042   | 0.054    |
| N II   | 0.025   | 0.049    |
| O II   | 0.016   | 0.024    |

[FACT] 平均取 **f = 0.034 ± 0.015** 用于最终修正，所有物种。

[FACT] 修正 T_eff 后的结果：
- 与 **Kilian et al. (1991a)** 的 non-LTE Si 线 T_eff 尺度**良好一致**；
- 修正后的 T_eff 列在 **Table 1**（最终 T_eff 是修正值）。

### 7.1.4 Figure 11–13 — 温度修正前后

[FACT] 三张图（non-LTE Fig. 11、LTE C II Fig. 12、LTE O II Fig. 13）：
- 横轴：T_eff (K)，范围 10,000–35,000 K
- 纵轴：log ε − log ε(太阳)
- 虚线：每个物种的最优 f 拟合
- 实线：统一 f = 0.034 的拟合

[FACT] **修正后丰度分布**（Figure 15）：
- 直方图展示修正后 log ε − log ε(太阳)，实心线 = LTE，阴影区 = non-LTE
- **N II 分布不对称**：在 N-rich 一侧有显著偏离均值的恒星 → 这些星的确有真实 N 富集，不是 non-LTE 假象

---

## 7.2 Comparison with H II Regions and the Sun（§ 7.2）

### 7.2.1 与 Orion Nebula 对比

[FACT] 表 12 汇总 Orion Nebula 的 5 项分析结果。

[FACT] 若采用 **Baldwin et al. (1991)** 的星云丰度：
- **Δ log ε = log ε(B 星) − log ε(Orion)**：
  - He：**+0.06**
  - C：**−0.13**
  - N：**−0.13**
  - O：**+0.10**
  - S：**+0.09**

[FACT] 这些差异**明显小于**热星丰度分析与气体丰度分析的联合不确定度。

[FACT] **尘埃效应**：Meyer (1989) 估计 **20% ± 5% 的 O 进入尘埃**；若对 Baldwin et al. 的 O 丰度应用此修正，星与星云丰度**几乎不可区分**。

[FACT] **Orion 关联星直接对比**（8 颗本文星属于 Orion 关联，Warren & Hesser 1978）：
- 均值：Δ log ε = **−0.01 (He)**、**−0.10 (C)**、**−0.28 (N)**、**+0.07 (O)**
- 即 **Δ log ε ≈ 0 在测量不确定度内**

### 7.2.2 其他元素

[FACT] **Ne**：基于一条弱线 Ne I λ6506.5，仅 11 颗星可用。修正后 LTE Ne 丰度 **log ε(Ne) = 8.41 ± 0.13**（基于 11 星）。Baldwin et al. (1991) 的 Orion 星云 Ne 显著高 Δ log ε = −0.63，但 Ferland (1991) 质疑其可靠性（H II 区 ionization 结构不自洽），Rubin et al. (1991) 用更高温源得到与 B 星一致的 Ne → **本文不赋予此差异天体物理意义**。

[FACT] **Al III**：
- Dufton et al. (1990)：log ε(Al) = 6.1 ± 0.4 与 6.2 ± 0.2（两个 OB 团）；
- Peters (1976)：γ Peg 八条 Al III 线得 6.47；
- Sadakane, Takada & Jugaku (1983)：Al II/III UV 共振线得 6.5（六颗 B9 正常星）。

[FACT] **Fe**：Orion 星云的 Fe 低是由于 H II 区内 Fe 进入尘埃，不影响 B 星 Fe 丰度。

[FACT] **与太阳差异**：太阳与 Orion 星云丰度可能有 Δ log ε 差异，来源可能是**银河系气体混合不均匀**（Boesgaard 1989、Nissen 1988）——年轻疏散星 [Fe/H] 散布 ±0.1 dex 在同一 age。若太阳从富金属气体形成，则可解释太阳与 Orion 差异。

---

## 7.3 Evolutionary Changes in Abundance（§ 7.3）

### 7.3.1 最 N 富集星：ρ Leo (HD 91316)

[FACT] **ρ Leo (HD 91316)** 是最 N 富集星：
- LTE N 丰度比 B 星均值高 **0.76 dex**
- non-LTE N 丰度比均值高 **0.60 dex**

[FACT] 用 **Maeder & Meynet (1988)** 模型推算，如此大的 N 富集应伴随：
- He **增加** 0.16 (LTE) / 0.10 (non-LTE) dex
- C **减少** 0.15 / 0.10 dex
- O **减少** 0.07 / 0.04 dex

[FACT] ρ Leo 的观测值：He 略高、C 略低、O 近均值（与 Maeder & Meynet 预测一致）。Walborn (1976) 已定性指出 ρ Leo 是中等 N 增强。

### 7.3.2 Figure 16 — C vs N anti-correlation

[FACT] 图 16：温度修正后 non-LTE **C 丰度** vs **N 丰度**。
- 填充圆 = 超巨星；
- 实线 = Maeder & Meynet (1988) 预测的 C 随 N 增大而下降（其初始丰度经 −0.49 与 −0.18 dex 调整以匹配观测 C II/N II 均值）；
- **边缘性证据**：在最 N-strong 的星中看到 C 下降趋势。

[FACT] 图 16 左下角低 C 点是 **HD 24131**（最快自转、浅线，C 仅基于 4 条线，内部误差 0.43 dex）。
[FACT] 最低 N 丰度孤立点是 **HD 31237**（疑似 SB2 系统）—— 认为其线因伴星连续谱通量增加而变弱。

### 7.3.3 Figures 17–20 — He/C/N/O 在 H-R 图中的分布

[FACT] 图 17–20 都以 log g vs log T_eff 为坐标，叠加 Maeder & Meynet (1988) 演化轨（标初始质量）。

- **Figure 17**：He 丰度（non-LTE），符号面积 ∝ He 线性丰度。超巨星 He 富集，但幅度不确定。
- **Figure 18**：C 丰度（LTE, C II）。超巨星略 C 贫。
- **Figure 19**：N 丰度（LTE, N II）。**演化星有 N 富集趋势，但并非所有演化星都 N 富集**。
- **Figure 20**：O 丰度（LTE, O II）。

[FACT] 结论性陈述：
> "although we find that some evolved stars do show CN-cycled N enrichment we cannot confirm Lyubimkov's (1984) claim that there is a systematic increase in N abundance with age among the B stars."

[FACT] 存在 N 正常丰度的演化星 → **CN-cycled 元素混合不是 B 星的普遍现象**。

### 7.3.4 Lyubimkov 假象的解释

[FACT] **对 Lyubimkov 的"事后解释"**：Lyubimkov 用了 Dufton & Hibbert (1981) 表，该表**只给出 log g = 4.0 且 ξ = 0** 的预测。在演化星中：
- **log g 更低**（演化星膨胀，表面重力下降）→ 线变强
- **ξ 更大**（演化星更强线，微湍流增大）→ 线变强

忽略这两个变化会**导致推导的 N 丰度随年龄"假性"增加**。

[FACT] **数值量化**（用 Becker & Butler 1988a 表，N II λ4630 线）：
- 太阳丰度，T_eff = 21,000 K, log g = 4, ξ = 0：Wλ = **57 mÅ**
- log g = 3.5：Wλ = **75 mÅ**（+32%）
- ξ = 5 km s⁻¹：Wλ = **69 mÅ**（+21%）
- ξ = 10 km s⁻¹：Wλ = **88 mÅ**（+54%）

假设 log g = 4、ξ = 0 时**推导的丰度增量**：
- log g → 3.5：**+0.32 dex**
- ξ → 5：**+0.22 dex**
- log g → 3.5 **且** ξ → 10：**+0.90 dex**

[FACT] **用本文自身数据重演**：对 16 颗 Lyubimkov 样本星（质量范围 8.5–13.0 M☉ 匹配 Lyubimkov 中质量组）：
- 用本文 N II λ4630 实测 EW + 本文 T_eff，**但** 假设 log g = 4、ξ = 0 推导 N 丰度；
- 用 Maeder & Meynet (1988) 演化轨插值推每星的年龄与质量；
- 得到 **N 丰度 vs 年龄**的斜率 = **0.035 dex per 10⁶ yr**（Figure 21，虚线）；
- **这一相关性正是 Lyubimkov 找到的方向**，但纯粹是**方法学伪相关**。

[FACT] 用**本文正确的非 LTE、温度修正** N 丰度（Figure 22）vs 年龄：**没有系统性相关**。

[FACT] 结论性陈述：
> "we can rule out a N enrichment with age of the magnitude suggested by Lyubimkov."

[FACT] 既然 CN-cycling 对 He 与 C 的预期变化比 N 小得多，Lyubimkov 对 He、C 富集的主张**应持怀疑**。

### 7.3.5 N-rich 星与 Maeder 湍流扩散

[FACT] **Maeder (1987a) 湍流扩散**：快速自转恒星可准同质演化，沿 HR 图向**更高光度 + 更高温**方向演化；即使在非同质路径上，中等自转星也可在核燃烧早期（H-gradient 屏障尚未建立）出现 CN-cycled 表面增强。

[FACT] Schönberner et al. (1988) 认为 **OBN 星**就是这种旋转诱导混合的直接结果，认为现 OBN 星当前慢转是因为**恒星风角动量损失导致的 spin-down**。

[FACT] 本文 N-strong 星：
- **富集程度不及 OBN 星**
- **中等自转**
- **甚至可以在主序附近找到**

[FACT] 作者推测：这些星是 Maeder (1987a) 预言的"a fraction of the normally redwards evolving stars [that] are expected to show CNO ratios intermediate between cosmic and [CN cycle] equilibrium values"。

### 7.3.6 超巨星 — 部分混合但未到红巨星

[FACT] 5 颗超巨星**全部**显示某种程度的 N（可能 He）富集，但 **C/N 比远未达到 CN-cycle 平衡值**。

[FACT] Maeder (1987b) 认为 20–40 M☉ 星**只有到红巨星阶段**才发生大规模 CN-cycled 表面混合；蓝超巨星若完全富集，则代表其正在 HR 图上 blueward loop 演化。

[FACT] **本文推论**：超巨星丰度显示**不完全混合** → 按 Maeder 判据，**尚未到过红巨星**；但 N 过富集又证明**某种混合已经发生**。

[FACT] **关键结论**：
> "it may be possible for a blue supergiant to show substantial mixing before the red supergiant phase, which may have important consequences for the interpretation of evolutionary status of the precursor star to SN 1987A"（Weiss, Hillebrandt & Truran 1988）

---

## 7.4 关键数值汇总

| 项目 | 值 |
|------|-----|
| 温度修正 | f = 0.034 ± 0.015 |
| 修正方法 | ΔT_eff = f · T_eff |
| 与 Orion Nebula 差异（Baldwin 1991） | He +0.06, C −0.13, N −0.13, O +0.10, S +0.09 |
| 与 Orion 星云直接比较（8 星） | Δ log ε ≈ 0 |
| ρ Leo N 富集 | +0.76 (LTE) / +0.60 (NLTE) |
| ρ Leo 预期 He/C/O 变化 | He +0.10, C −0.10, O −0.04 (NLTE) |
| Lyubimkov 假象：N II λ4630 Wλ | log g=4, ξ=0：57 mÅ |
| 演化到 log g=3.5 | Wλ=75 mÅ → 假增量 0.32 dex |
| 演化到 ξ=10 | Wλ=88 mÅ → 假增量 0.90 dex（组合） |
| Lyubimkov 假相关斜率复现 | 0.035 dex per 10⁶ yr |
| 与 Kilian et al. 1991a 一致性 | T_eff 修正后良好一致 |
| Ne 均值（11 星） | log ε(Ne) = 8.41 ± 0.13 |
| Si III 均值 | LTE 7.63 / NLTE 7.69 |
| Si IV 均值 | LTE 7.51 / NLTE 7.47 |
| Si II 异常 | 6.86（低于 Si III/IV 约 0.7–0.8 dex） |

---

## 7.5 我的理解 [INTERPRETATION]

[INTERPRETATION]
1. § 7.1 的温度修正方法**优雅且可操作**：用丰度随 T_eff 的趋势（曲线生长峰值效应）反推尺度误差；这一方法后来成为早型星丰度分析的常见手段；
2. § 7.3.4 对 Lyubimkov 的复现是**决定性的反证**——不是"用新数据反驳"，而是"用同一数据的正确处理复现伪相关"，这是最强的科学反驳形式；
3. ρ Leo 案例的定量一致性（+0.60 N → +0.10 He、−0.10 C、−0.04 O）**几乎完美匹配 Maeder & Meynet 预测**，是 N-rich 星 = 部分混合 CN-cycled 物质的强观测证据；
4. 超巨星结论（"blue supergiant 可在红巨星之前混合"）对 SN 1987A 前身星演化解释有**直接影响**——这是本文最具有**天体物理影响力**的推论之一。

---

## 7.6 潜在问题 [CRITIQUE]

[CRITIQUE]
1. 温度修正 f=0.034 假设对所有物种相同，但表 10 显示不同物种最佳拟合 f 在 0.016–0.054 之间变化，用单一 f 会引入物种间 ~0.02–0.04 dex 系统偏差；
2. 温度修正的偏导基于 log g = 4.0、ξ = 5 km s⁻¹、太阳丰度——对超巨星（log g 2–3.7，ξ 8–23）此近似**很差**，因此超巨星丰度"未修正"本身也是问题；
3. 若 He 富集影响大质量超巨星的温度/重力（Kudritzki et al. 1989 指出），则这些星的丰度**系统性**受影响；
4. N-rich 星的**选择偏差**：V sin i < 100 km s⁻¹ 的样本**天然排除最快转者**，而这些恰恰是 Maeder 湍流混合最强的子集——因此本文可能**低估**了旋转混合的普遍性；
5. C+N 守恒的定量检验在本文中**未系统展示**——只在 § 1 提及 Lyubimkov (1989) 的结论，本文自己的 C+N 分布未直接画出（仅间接在图 16 讨论 C vs N）。