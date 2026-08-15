# 5. LTE Abundances — LTE 丰度分析

> 本章属于：Gies & Lambert (1992) — ApJ 387:673
>
> 上一章：[[03_stellar-nucleosynthesis/0010_gies-lambert-1992/literature_analysis/04_rotation.md|04_rotation.md]]
>
> 下一章：[[03_stellar-nucleosynthesis/0010_gies-lambert-1992/literature_analysis/06_nlte_abundances.md|06_nlte_abundances.md]]

---

## 5.1 方法学

[FACT] 使用 **Kurucz (1979)** line-blanketed LTE 大气 + **Kurucz WIDTH6** 程序计算每条线的理论 EW，再反推丰度。

[FACT] 大气构造：用 § 3 确定的 T_eff 与 log g，在 Kurucz (1979) 太阳丰度大气表中**双线性插值**：
1. 取包围目标 (T_eff, log g) 的四个模型；
2. 转换到统一的 Rosseland 光学深度深度标度；
3. 对 log T、P、n_e 做双线性插值。

---

## 5.2 Table 4 — 原子数据

[FACT] 表 4 列出所有线的 log gf、参考文献、Tr（radiative damping, s⁻¹）、$\Gamma$S（quadratic Stark damping, s⁻¹）。

[FACT] **log gf 数据来源**：
- **K** = Kurucz & Peytremann (1975)；
- **W** = Wiese, Smith & Glennon (1966)（更高精度时采用）；
- **A** = Artru et al. (1981)（Si II $\lambda$$\lambda$5041, 5056 专用）。

[FACT] **辐射阻尼 Tr**：对 Einstein A 系数求和，取平均 T_eff = 25,000 K；数据不足时采用 Peters (1976) 或 Hardorp & Scholz (1970)。

[FACT] **Stark 阻尼 $\Gamma$S 来源**：
- He I：Konjevic, Dimitrijevic & Wiese 1984a
- C III、N III、Si II：Konjevic, Dimitrijevic & Wiese 1984b
- Ne I：Konjevic & Roberts 1976
- N II、O II、S II：Konjevic & Wiese 1976
- Si III：Dimitrijevic 1983
- Al III：Dimitrijevic & Konjevic 1981
- Si IV：Purić et al. 1983
- 数据缺失时用 Griem (1974) 表格与近似公式。

---

## 5.3 微湍流 $\xi$ 的确定

[FACT] 方法：对 C II、N II、O II（有时 S II）分别跑 WIDTH6 三个不同 $\xi$ 值，选**log $\epsilon$ vs EW 斜率为零**的 $\xi$。

[FACT] 再对所有物种的 $\xi$ 取**加权平均**（按线数加权）作为最终 $\xi$，用于所有线的丰度计算。

[FACT] **关键结果**：
- 非超巨星：⟨$\xi$(LTE)⟩ = **6.2 km s⁻¹**；⟨$\xi$(NLTE)⟩ = **5.0 km s⁻¹**
- 超巨星 LTE：⟨$\xi$(LTE)⟩ = **23 km s⁻¹** ← **超声速**
- 超巨星 NLTE：⟨$\xi$(NLTE)⟩ = **8.9 km s⁻¹** ← 亚音速

[FACT] 作者解释：超巨星 LTE $\xi$ 高达 23 km s⁻¹ 是"obviously supersonic"，应视为**non-LTE 偏离的信号**，而非真实微湍流。引入 non-LTE 后 $\xi$ 大幅降低。

[FACT] $\xi$ 随 T_eff 增加的趋势：
- ⟨$\xi$(NLTE)⟩ = 4 km s⁻¹ at T_eff = 17,000 K
- ⟨$\xi$(NLTE)⟩ = 6 km s⁻¹ at T_eff = 30,000 K

[FACT] 作者明确反驳 **Becker & Butler (1989)** 的观点（即"微湍流完全是 LTE 误用的伪像"）：
> "When LTE is replaced by NLTE, $\xi$ is reduced especially for the supergiants, but remains nonzero."

[FACT] 超巨星中 $\xi$ 的推导**不完全自洽**：大气模型本身依赖假设 $\xi$=2 km s⁻¹（Kurucz 1979），影响金属线总不透明度；Fitzpatrick (1991) 的自洽模型会是改进。

[FACT] **关键论据**（关于弱线抗微湍流）：
> 例：T_eff = 21,000 K, log g = 4, $\xi$ = 5 km s⁻¹ 的大气中，$\xi$ 误差 5 km s⁻¹ 导致：
> - N II $\lambda$4630（强线）丰度误差 **0.21 dex**；
> - N II $\lambda$5007（弱线）丰度误差 **0.10 dex**。

因此本文选弱线策略使最终丰度**大比例独立于 $\xi$ 的具体值**。

---

## 5.4 丰度平均与删选（Table 5）

[FACT] **表 5 LTE 平均丰度**（跨 2 页，p.684–686）：每颗星、每个离子（He I、He II、C II、C III、N II、N III、O II、Ne I、Al III、Si II、Si III、Si IV、S II、Fe II、Fe III）给出：
- 无权重平均 log $\epsilon$
- 标准差 $\sigma$
- 线数 n
- 温度尺度修正 $\Delta$（§ 7.1）

[FACT] **删选标准**（作者"attempted to exclude faulty or questionable EW data"）：
1. **EW < 5 mÅ** 的所有线；
2. 与同物种其他线**系统性不一致**的线：
   - N II $\lambda$5175
   - O II $\lambda$$\lambda$4705, 4710, 5160
3. **冷星中高阶电离线**（应极弱，观测到的可能是错认特征）：
   - C III $\lambda$4647 for T_eff < 23,000 K
   - C III $\lambda$4665 for T_eff < 29,000 K
   - N III for T_eff < 26,000 K
   - Si IV for T_eff < 29,000 K
4. **热星中低阶电离线**（应极弱）：
   - Si II for T_eff > 25,000 K
   - S II for T_eff > 24,750 K
   - Fe II for T_eff > 22,500 K
5. 与平均差 **> 2$\sigma$** 的丰度值；
6. 其他因过度弱和/或混合而视为易错的线（如 Si III $\lambda$4716.7 常与 S II $\lambda$4716.2 混合）。

[FACT] **电离态一致性检验**：不同电离态的丰度通常一致（支持 T_eff 赋值），**除超巨星外**；N I 与 N II 在同时可测的星中一致。

[FACT] **N I 三条线 $\lambda$$\lambda$8680, 8683, 8686**：在 10 颗星的子样本中搜索，对 HD 886、HD 29248、HD 31237 等**不可见**（给出上限）。

---

## 5.5 Table 6 — N I EW 与丰度（p.687）

[FACT] 对 5 颗星测了 N I $\lambda$$\lambda$8680, 8683, 8686 的 EW：
- HD 35468：N I $\lambda$$\lambda$8680 (16), 8683 (5:, 8.18), 8686 (7:, 8.68)，平均 log $\epsilon$(N) = 8.45，$\sigma$=0.26；
- HD 51309：96 (8.85), 55 (8.74), 30 (8.83)，平均 log $\epsilon$(N) = 8.81；与 LTE N II 值 8.53 差 $\Delta$ = 0.06；
- HD 52089：20 (9.11), 10: (9.01), 7: (9.27)，平均 log $\epsilon$(N) = 9.13；与 LTE N II 值 8.45 差 $\Delta$ = 0.11。

[FACT] 注：a = 基于超巨星的低温尺度（§ 5 讨论）。

[INTERPRETATION] N I 与 N II 大体一致（差 0.06–0.11 dex 在合理误差范围内），验证温度/重力。

---

## 5.6 Figure 9 — LTE vs NLTE $\xi$ 比较

[FACT] LTE $\xi$ 与 NLTE $\xi$ 的对比散点图：
- **填充圆** = 超巨星，**空心圆** = 其他星
- NLTE $\xi$ 一致低于 LTE $\xi$，尤其是超巨星

[INTERPRETATION] 超巨星 LTE $\xi$ 高达 ~20–30 km s⁻¹，而 NLTE $\xi$ 降至 < 10 km s⁻¹ —— 这是非 LTE 效应最强的恒星子集，也是本文必须用 NLTE 交叉验证的核心理由。

---

## 5.7 关键数值汇总

| 参数 | 值 |
|------|-----|
| 大气模型 | Kurucz (1979) LTE line-blanketed |
| 计算程序 | WIDTH6 |
| 原子数据源 | Kurucz & Peytremann 1975；Wiese, Smith & Glennon 1966；Artru et al. 1981 |
| Stark 阻尼平均 T_eff | 25,000 K |
| $\xi$ 确定判据 | log $\epsilon$ vs EW 斜率为 0 |
| 非超巨星 ⟨$\xi$(LTE)⟩ | 6.2 km s⁻¹ |
| 非超巨星 ⟨$\xi$(NLTE)⟩ | 5.0 km s⁻¹ |
| 超巨星 ⟨$\xi$(LTE)⟩ | 23 km s⁻¹（超声速） |
| 超巨星 ⟨$\xi$(NLTE)⟩ | 8.9 km s⁻¹（亚音速） |
| EW 阈值 | < 5 mÅ 剔除 |
| 删选标准 | 系统性不一致、错认、>2$\sigma$ |
| 弱线抗 $\xi$ 灵敏度 | N II $\lambda$5007 误差 0.10 dex for $\Delta$$\xi$=5 km s⁻¹ |

---

## 5.8 潜在问题 [CRITIQUE]

[CRITIQUE]
1. $\xi$ 由 log $\epsilon$ vs EW 斜率 = 0 反推，但 **Dufton, Durrant & Durrant (1981b)** 指出此法可能因曲线生长非线性导致 $\xi$ **高估 1–2.5 km s⁻¹** —— 即使扣除偏差，剩余 $\xi$ 仍显著非零；
2. 超巨星 $\xi$ 的自洽性问题（大气假设 $\xi$=2 vs 推得 $\xi$=23），作者承认但仍未完全解决；
3. 删选标准依赖"与其他线一致"，但若有真实丰度异常（如 CN-cycled 星），这些异常本身可能因被当作离群值而被剔除 —— 这是一个潜在**确认偏误**（尽管作者通过保留 N 富集星说明并未过度删选）；
4. 冷星的高电离线剔除与热星的低电离线剔除，用的是 T_eff 阈值，若 T_eff 本身有误差（2–4%），可能误判该线是否应保留。