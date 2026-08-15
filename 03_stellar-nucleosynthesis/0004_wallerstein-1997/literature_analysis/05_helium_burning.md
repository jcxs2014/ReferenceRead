> 本章属于：Synthesis of the elements in stars, forty years of progress (Wallerstein et al., 1997)
>
> 上一章：[[03_stellar-nucleosynthesis/0004_wallerstein-1997/literature_analysis/04_x_process_light_elements.md|04_x_process_light_elements.md]]
>
> 下一章：[[03_stellar-nucleosynthesis/0004_wallerstein-1997/literature_analysis/06_advanced_burning.md|06_advanced_burning.md]]

# 5. 氦燃烧

**本章作者**：Gerald M. Hale（Los Alamos National Laboratory）

## 5.1 总体框架

[FACT] 氦燃烧终止于 16O，因为：
- 16O($\alpha$,$\gamma$)20Ne 速率在 $T_{9}$ < 0.2 时远低于 12C($\alpha$,$\gamma$)16O（Fowler et al. 1975）
- 16O 阈值附近的能级具有错误的宇称/角动量 → 无法共振增强

[FACT] **12C($\alpha$,$\gamma$)16O 反应率是核天体物理当今最重要的未解决问题之一**：
- 决定 12C→16O 转化比例
- 决定大质量星抛射物与白矮星内部的 C/O 丰度比
- 决定大质量星后续重离子燃烧阶段的初始条件
- 许多更重元素（直至铁）的丰度都敏感依赖此速率（Weaver & Woosley 1993）

## 5.2 A. Triple-$\alpha$ capture

[FACT] **两阶段过程**：
1. 两个 $\alpha$ 粒子在 8Be 基态（非束缚，半衰期 $t_{1}$/₂ = 0.97×10^(-16) s）中短暂共存
2. 第三个 $\alpha$ 粒子在 8Be 衰变前被俘获，形成 12C** (Ex = 7.6542 MeV, J^$\pi$ = $0^{+}$)

[FACT] **Hoyle (1954) 的预言**：为解释观测到的 12C 丰度，必须存在 Ex ~ 7.65 MeV 的 $0^{+}$ 共振态——被实验验证，是核天体物理最杰出的成就之一

[FACT] **三 $\alpha$ 反应速率**：
$$r_{3\alpha} = \frac{N_\alpha^3}{3} \cdot 2^{33/2} \cdot \left(\frac{2\pi}{M_\alpha k T}\right)^{3/2} \cdot \frac{\Gamma_\alpha \Gamma_{rad}}{\Gamma} \exp\left(\frac{-Q}{kT}\right)$$

[FACT] 关键参数（Ajzenberg-Selove 1990）：
- Q = (M_12C** − 3M_$\alpha$)c² = 379.5 ± 0.3 keV
- $\Gamma$_$\gamma$ = (3.64 ± 0.50) meV
- $\Gamma$_pair = (60.5 ± 3.9) meV
- $\Gamma$_rad = $\Gamma$_$\gamma$ + $\Gamma$_pair << $\Gamma$_$\alpha$ ≈ $\Gamma$ → 速率仅依赖 $\Gamma$_rad

[FACT] **B2FH 时代低估此速率**：$\Gamma$_$\gamma$ = 1 meV（偏低）部分被当时较小的 Q 值（372 keV，而非 379.5 keV）的指数因子补偿

## 5.3 B. $\alpha$ + 12C capture

[FACT] 反应速率公式：
$$r_{\alpha+12C} = N_\alpha N_{12C} \langle \sigma_{cap} v \rangle_T$$

[FACT] 截面参数化：
$$\sigma_{cap}(E) = \frac{S_{cap}(E)}{E} \exp(-2\pi\eta)$$
- $\eta$ = $Z_{1}$$Z_{2}$e²/ℏv（Sommerfeld 库仑参数）
- S_cap(E) = S_E1(E) + S_E2(E)（E1 + E2 多极分量）

[FACT] **Gamow 能量**：在氦燃烧温度 $T_{9}$ = 0.2–0.6 下，$E_{0}$ = 0.3–0.9 MeV

[FACT] 由于库仑势垒大，直接测量无法延伸至 $E_{0}$，**必须靠理论外推**

### 5.3.1 1. E1 capture

[FACT] **E1 由以下决定**：
- 宽 $1^{-}$ 共振在 E = 2.4 MeV（Ex = 9.585 MeV）
- **亚阈值 $1^{-}$ 态**在 E = −245 keV（Ex = 7.11685 MeV）—— Dyer & Barnes (1974) 首次证明其重要性

[FACT] 直接测量（Dyer & Barnes 1974; Redder 1987; Kremer 1988; Ouellet 1992）覆盖 Ec.m. = 1.0–3.0 MeV

[FACT] Ouellet et al. (1996) 数据修正后，**所有测量指向亚阈值态与正能共振的相长干涉**（constructive interference）

**Table II: E1 外推值 S_E1($E_{0}$ = 0.3 MeV)**：

| 参考 | S_E1 (keV·b) | 方法 |
|---|---|---|
| Dyer & Barnes (1974) | 140^{−120}_{+140} (3-level R-matrix) | $\sigma$(90°) 测量 + E2 修正 |
| Redder et al. (1987) | 200^{−110}_{+270} (3-level R-matrix) | $\sigma$($\theta$) 测量，分离 E1/E2 |
| Kremer et al. (1988) | 10^{−10}_{+130} (3-level R-matrix + l=1 相移约束) | $\sigma$(90°) + $\gamma$ 反冲符合 |
| **Ouellet et al. (1996)** | **79 ± 16** | **R/K-matrix + $\beta$ 延迟 $\alpha$ 谱** |

[FACT] **16N $\beta$ 延迟 $\alpha$ 谱**（Buchmann 1993, Zhao 1993/1995, France 1997）：
- 谱的次极大反映亚阈值 $1^{-}$ 态的存在
- 谱公式：
$$\frac{dN_\alpha}{dE} = f_\beta(E) P_\alpha(E) \left|\sum_l B_l \sum_{l'} A_{ll'}(E) g_{l'\alpha}\right|^2$$
- 干涉极小不能单独固定截面中两个能级的干涉
- 但所有直接截面测量支持相长干涉

### 5.3.2 2. E2 capture

[FACT] **E2 由以下决定**：
- 亚阈值 $2^{-}$ 态在 E = −245 keV（Ex = 6.9171 MeV）
- 宽 $2^{-}$ 共振在 E = 4.36 MeV（Ex = 11.52 MeV）——远在阈值之上
- 窄共振（$\Gamma$ = 0.625 keV）在 Ex = 9.8445 MeV

[FACT] E2 强度近似中心在 Ex ≈ 15 MeV，展宽 ~15 MeV → E2 主导贡献来自**远距离能级和直接俘获**

**Table III: E2 外推值 S_E2($E_{0}$ = 0.3 MeV)**：

| 参考 | S_E2 (keV·b) | 方法 |
|---|---|---|
| Redder et al. (1987) | 96^{−30}_{+24} (direct capture + 单能级 Breit-Wigner) | $\sigma$($\theta$) |
| Ouellet et al. (1996) | 36 ± 6 | 微观团簇模型 |
| Trautvetter et al. (1996) | 14.5^{−14}_{+96} (R-matrix, 含 Ex < 11.52 MeV 的 $2^{-}$ 能级) | $\sigma$($\theta$) |

[FACT] **E2 干涉性质未确定**：亚阈值 $2^{-}$ 态与远距离能级/直接贡献的干涉是相长还是相消仍未知

[FACT] **16O Coulomb 离解**（Kiener et al. 1997）：通过 208Pb 靶上 16O 束的 Coulomb 离解提取 E2 截面——依赖理论分析，但定性一致

### 5.3.3 3. 推荐值

[FACT] **Ouellet et al. (1996) 被推荐为最佳值**：
- S_E1($E_{0}$ = 0.3 MeV) = (79 ± 16) keV·b
- S_E2($E_{0}$ = 0.3 MeV) = (36 ± 6) keV·b
- **S_cap($E_{0}$) = (120 ± 40) keV·b**（加上级联贡献 20 ± 9 keV·b）

[FACT] **不确定度仍 ~30%，远超天体物理应用的理想 10–15%**

[FACT] 其他分析给出更宽的 S_E1 范围：30–260 keV·b（E1）；S_E2：7–120 keV·b

[FACT] Weaver & Woosley (1993) 灵敏度研究：C/O 比与 S_cap 的变化高度敏感

## 5.4 本章要点总结

[FACT] **40 年后 B2FH 的核心问题仍未完全解决**：12C($\alpha$,$\gamma$)16O 反应率的不确定度仍是核天体物理最大单一不确定度

**核心数据**：
- S_cap(0.3 MeV) = 120 ± 40 keV·b
- E1 部分：79 ± 16 keV·b（Ouellet 1996，含 $\beta$ 延迟 $\alpha$ 谱约束）
- E2 部分：36 ± 6 keV·b

**未来方向**（1997 年视角）：
- 更多 $\beta$ 延迟 $\alpha$ 谱数据（TRIUMF vs Yale/UConn 的矛盾）
- 16O Coulomb 离解（Kiener et al. 1997 新方法）
- 改善 E2 外推（E2 是 E1 不确定度约一半但更困难）

[CRITIQUE] 1997 年后此问题继续进展：LUNA（地下实验室，Gran Sasso）后续实验进一步降低系统误差。但到本文写作时，C/O 比 ~0.3–0.8 的宽范围已足以影响几乎所有恒星演化预测。

# 6. 本章关键数值速查表

| 量 | 数值 |
|---|---|
| 8Be 半衰期 | 0.97×$10^{-16}$ s |
| 12C** 共振能 | Ex = 7.6542 MeV |
| Q(3$\alpha$) | 379.5 ± 0.3 keV |
| $\Gamma$_$\gamma$(7.65 MeV) | 3.64 ± 0.50 meV |
| $\Gamma$_pair(7.65 MeV) | 60.5 ± 3.9 meV |
| S_cap(0.3 MeV) 推荐值 | 120 ± 40 keV·b |
| S_E1(0.3 MeV) | 79 ± 16 keV·b |
| S_E2(0.3 MeV) | 36 ± 6 keV·b |
| Gamov 峰 ($T_{9}$=0.2–0.6) | $E_{0}$ = 0.3–0.9 MeV |
| 16O($\alpha$,$\gamma$)20Ne 相对速率 | << 12C($\alpha$,$\gamma$)16O ($T_{9}$ < 0.2) |