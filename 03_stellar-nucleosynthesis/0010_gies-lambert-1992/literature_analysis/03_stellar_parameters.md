# 3. Effective Temperatures and Gravities — 温度与重力测定

> 本章属于：[[03_stellar-nucleosynthesis/0010_gies-lambert-1992/literature_analysis/00_overview.md|Gies & Lambert (1992) — ApJ 387:673]]
>
> 上一章：[[03_stellar-nucleosynthesis/0010_gies-lambert-1992/literature_analysis/02_observations.md|02_observations.md]]
>
> 下一章：[[03_stellar-nucleosynthesis/0010_gies-lambert-1992/literature_analysis/04_rotation.md|04_rotation.md]]

---

## 3.1 方法学概述

[FACT] 作者采用 **Brown et al. (1986)** 与 **Wolff (1990)** 的方法：
1. 用**测量 Balmer 跳变的色指数**作为 T_eff 指标；
2. 用 **H$\beta$ 谱线轮廓**作为 log g 指标；
3. 因为色指数与 H$\beta$ 宽度对 T_eff 和 log g 都有耦合依赖，用**迭代法**收敛。

[FACT] 迭代流程：
1. 用色指数 [c1] 与 Strömgren $\beta$ 的校准先给 T_eff 与 log g 初值；
2. 用该 T_eff 构建不同 log g 的 H$\beta$ 轮廓网格，与观测宽度最佳匹配得到新 log g；
3. 用新 log g 反推 T_eff；
4. 若两次 T_eff 差 > 50 K，回到步骤 2。

[FACT] 迭代通常 < 4 次收敛。

---

## 3.2 色指数与模型

[FACT] 色指数校准基于 **Kurucz (1979)** line-blanketed LTE 大气模型。

[FACT] **模型可靠性问题**：
> "These models are reasonably secure for main-sequence B stars, but their use for the O stars and supergiants is suspect because conditions in the stellar atmosphere become increasingly non-LTE at higher temperatures and lower gravities"（Lennon et al. 1990）

[FACT] 使用两个 Strömgren 色指数的去红化形式：

### 式 (1)
$$[c_1] = c_1 - 0.2(b-y)$$

用于 **Lester, Gray & Kurucz (1986)** 校准。对于超巨星低 log g，用 **Fitzpatrick (1991)** 从 Kurucz 模型计算的 [c1]。

### 式 (2)
$$c^0 = c_1 - 0.2\,E(b-y)$$
其中 $E(b-y) = (b-y) - (b-y)_0$；下标 0 表示去红化值。

$c^0$ 与 $E(b-y)$ 通过 Crawford (1978) 迭代法获得；普通星用 **Underhill & Doazan (1982) Table 2-3** 的经验关系，超巨星用 **Shobbrook (1976)** 关系。

[FACT] 色指数数据来源：
- **Hauck & Mermilliod (1980)**（主要来源）；
- **Oblak & Chareton (1980)**（HD 36959, 36960）；
- **Crawford, Barnes & Golson (1970)**（HD 51309）。

[FACT] 光谱双星的色指数**未做校正**。

[FACT] 两条校准给出的 T_eff "generally agreed within a few hundred degrees"，取**平均**作为最终 T_eff。

---

## 3.3 与 Code et al. (1976) 基准温度的校准

[FACT] 对 5 颗超巨星（Underhill et al. 1979 数据不完整），作者的 log g 分别来自：
- $\eta$ Ori (HD 51309)：Underhill et al. 1982，log g = 3.7；
- $\delta$ Oph (HD 61068)：Vogt & Penrod 1983，log g = 3.8；
- $\eta$ Cen (HD 180163)：光谱分类 B1.5 Ve，log g = 4.0；
- $\beta$ Cru、$\delta$ Sco、$\alpha$ Pav：用 Underhill et al. 1979 数据 + Maeder & Meynet (1987) 演化轨在理论 H-R 图中定位，分别得 log g = 3.6, 3.8, 4.0。

[FACT] **Figure 6**：本文色指数温度 vs Code et al. (1976) 基准温度。
- 除 Spica 外，Code et al. 温度**系统性偏高**；
- 校正因子：**1.042**（Lester et al. 1986 校准）与 **1.052**（Balona 1984 校准）；
- 最终所有温度都按 Code et al. 尺度归一。

[FACT] **误差估计**：
- 温度：2%–4%（从图 6 散布）；
- 重力：$\Delta$ log g = 0.1。

[FACT] 与 **Wolff (1990)** 比较（8 颗共同星，方法最相似）：
> ⟨log g(GL) − log g(Wolff)⟩ = 0.06，标准差 0.10 —— 与作者误差估计一致。

---

## 3.4 与其他研究的温度对比

[FACT] **Figure 7**：本文 T_eff vs：
- **Underhill et al. (1979)**（空心圆）：基于绝对测光 + 积分通量，大多数一致；
- **Wolff (1990)**（填充圆，8 星）：满意一致；
- **Kane et al. (1980)**（+ 号）：略高，基于 H-only blanketed 大气；
- **Kilian et al. (1991a)**（方块）：non-LTE Si 线，高 3.5%；
- **Grigsby (1990)**（三角）：line-blanketed non-LTE，热端偏低；
- **Kudritzki & Hummer (1990)**（方块）：Munich non-LTE 组，AE Aur (HD 34078) 与 10 Lac (HD 214680) 温度**显著偏高**。

[FACT] **超巨星问题**：Underhill et al. (1979) 给出的 5 颗超巨星温度比本文低 **~3000 K**；本文超巨星温度更接近 **Flower (1977)** 尺度。

[FACT] 作者**采用自己的超巨星温度**，但承诺在 § 5 讨论低温尺度会如何影响丰度结果（见 Table 8）。

---

## 3.5 关键数值汇总

| 项目 | 值 |
|------|-----|
| 迭代收敛 | < 4 次，判据 $\Delta$T < 50 K |
| 温度误差 | 2%–4% |
| 重力误差 | $\Delta$ log g = 0.1 |
| T_eff 范围（修正后） | ~16,500 – 34,400 K |
| log g 范围 | 2.10 – 4.36 |
| Lester/Gray/Kurucz 校正 | ×1.042 |
| Balona 校正 | ×1.052 |
| 与 Wolff 1990 比较 | $\Delta$ log g = 0.06 ± 0.10 |
| 超巨星 vs Underhill | $\Delta$T ≈ 3000 K |

---

## 3.6 我的理解 [INTERPRETATION]

[INTERPRETATION]
1. 作者把色指数（Balmer 跳变）与 H$\beta$ 轮廓两条独立温度/重力指标**耦合迭代**，这是 Balmer 大气参数测定的经典策略；比单纯用单一色指数更可靠；
2. 明确承认 Kurucz LTE 模型对 O 星和超巨星不牢靠——为后续 non-LTE 分析铺路；
3. 超巨星 T_eff 采用自己的（高于 Underhill ~3000 K），同时保留 Underhill 尺度下的丰度结果（Table 8），这种**保守双尺度**策略很稳健；
4. 温度校准的 1.042/1.052 因子 + § 7.1 中 3.4% 修正，合计约 **10%** T_eff 上移 —— 是后续丰度分析的关键参数。

---

## 3.7 潜在问题 [CRITIQUE]

[CRITIQUE]
1. 光谱双星的色指数未做校正——若伴星贡献显著（如 HD 31237 疑似 SB2），主星 [c1] 被伴星"稀释"，T_eff 被低估；
2. 超巨星的 log g 从理论 H-R 图与演化轨插值得到（如 $\delta$ Sco log g=3.8），依赖演化模型本身，与后续 § 7.3 用 Maeder & Meynet 演化轨推演年龄有**潜在循环依赖**；
3. 用"迭代收敛"判据 $\Delta$T < 50 K 未报告迭代失败案例，但实际数据中若 H$\beta$ 拟合不佳，可能收敛到次优解。