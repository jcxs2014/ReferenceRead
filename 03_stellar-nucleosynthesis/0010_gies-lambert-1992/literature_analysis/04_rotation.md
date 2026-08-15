# 4. Projected Rotational Velocities — 投影自转速度

> 本章属于：Gies & Lambert (1992) — ApJ 387:673
>
> 上一章：[[03_stellar-nucleosynthesis/0010_gies-lambert-1992/literature_analysis/03_stellar_parameters.md|03_stellar_parameters.md]]
>
> 下一章：[[03_stellar-nucleosynthesis/0010_gies-lambert-1992/literature_analysis/05_lte_abundances.md|05_lte_abundances.md]]

---

## 4.1 研究动机

[FACT] 若**旋转混合**是 CN-cycled 产物出现在热星表面的原因，那么丰度与自转周期可能存在相关。因此作者决定测量全样本的 V sin i 以建立一个**同质化的** V sin i 集。

---

## 4.2 方法 — Cross-correlation

[FACT] 方法：用每颗星的光谱与 **$\gamma$ Peg (HD 886)**（样本中谱线最锐的星之一）做交叉相关，测 FWHM。

[FACT] **三个谱带**：
- 4627–4717 Å（O II 区）
- 4999–5050 Å（N II 区）
- 5120–5163 Å（C II 区）；最热与最冷的星此带因 C II 太弱而不用

### 式 (3) — 交叉相关函数

$$r(\tau) = \frac{1}{n}\sum_j s_j \, c_{j+\tau}$$

其中 s 是待测光谱，c 是标准 $\gamma$ Peg 光谱，n 是谱带内的数据点数。

### 式 (4) — 校正半宽

$$H_c = (H_{\text{test}}^2 - H_{\gamma\text{Peg}}^2)^{1/2}$$

$H_{\text{test}}$ 是交叉相关函数的半宽，$H_{\gamma\text{Peg}}$ 是 $\gamma$ Peg 自相关的半宽除以 $\sqrt{2}$。

[FACT] 每个星取三个谱带半宽的**平均与标准差**作为最终 V sin i。

---

## 4.3 标定 — 从半宽到 V sin i

[FACT] 步骤：
1. 以最锐谱星 **HD 35299** 作为零旋转代表，其测得的半宽（13.1 km s⁻¹）代表仪器 + 内禀展宽（微观/宏观湍流）的总贡献；
2. 以 HD 35299 的半宽构造**标准 Gaussian 轮廓**；
3. 假设 HD 35299 的微湍流/宏湍流展宽对全样本是合理近似（**对超巨星此假设很差**，因超巨星宏湍流展宽大，Ebbets 1979）；
4. 用 **Gray (1976)** 方法，线性 limb-darkening 系数 **$\epsilon$ = 0.28**（Wade & Rucinski 1985 给出的主序中温星合理值），构造旋转展宽线轮廓网格；
5. 每条模型轮廓与标准 Gaussian 卷积，再归一化到相同 EW；
6. 计算模型交叉相关函数的 FWHM；
7. 用半宽-vs-V sin i 标定曲线插值得到 V sin i。

[FACT] 对超巨星的限制：因其宏湍流展宽显著大于 HD 35299，本文方法**略高估**它们的 V sin i（< 10 km s⁻¹）。

---

## 4.4 结果（Table 1）

[FACT] V sin i 范围（表 1）：~2 km s⁻¹（HD 184171）到 ~75 km s⁻¹（HD 24131）。多数在主序 B 星典型范围 20–50 km s⁻¹。

[FACT] **异常案例**：
- **HD 214993**（12 Lac）：4670 Å 区呈中等宽度且中心附近有微弱红移发射反转；其他两区（不同夜观测）呈锐线无反转 → **$\beta$ Cep 变星**，已知 line profile variable（Smith 1977）；
- **HD 22951**：5025 Å 区 He I $\lambda$$\lambda$5015、5047 出现**延展的红翼**（其他线无此翼）→ 可能有双星伴星。

---

## 4.5 Figure 8 — V sin i 与前人比较

[FACT]
- **Slettebak et al. (1975)**（5 颗填充圆）：本文 V sin i 与其系统一致；
- **Uesugi & Fukuda (1970)**（空心圆）：总体一致；
- **HD 24131** 例外：本文 V sin i = 75 km s⁻¹，目录值 140 km s⁻¹ —— 显著差异。

[CRITIQUE] HD 24131 的差异暗示其 V sin i 可能是时变的，或目录值有问题。该星是本文样本中**最快自转的星**，后续 § 7.3 中其低 C 丰度被特别讨论（"the most rapidly rotating and shallow-lined star in our sample"，C 基于仅 4 条线，内部误差 0.43 dex）。

---

## 4.6 关键数值

| 项目 | 值 |
|------|-----|
| 标准星 | HD 886 ($\gamma$ Peg) |
| 谱带 | 4627–4717, 4999–5050, 5120–5163 Å |
| 零旋转基准 | HD 35299，半宽 13.1 km s⁻¹ |
| Limb-darkening | $\epsilon$ = 0.28 |
| V sin i 范围 | 2 – 75 km s⁻¹ |
| 超巨星 V sin i 误差 | 可能高估 < 10 km s⁻¹ |
| 异常：HD 24131 | 本文 75 vs 目录 140 |
| $\beta$ Cep：HD 214993 | Line profile 时变 |

---

## 4.7 我的理解 [INTERPRETATION]

[INTERPRETATION]
1. 用 $\gamma$ Peg 作为标准是经典 cross-correlation 策略，避免直接用理论谱的模型依赖；
2. 用 HD 35299 半宽作零旋转基准很巧妙——它把仪器 + 内禀展宽**经验性扣除**，避免了从仪器理论函数拟合的模型误差；
3. 三带独立测量再平均，提供了每个星的**内部一致性检验**（HD 214993 与 HD 22951 的异常正是靠这个暴露出来的）；
4. 但 $\epsilon$ = 0.28 固定值对所有 T_eff 都一样，忽略了热端 (O 星) 与冷端 (B3) 的 limb-darkening 差异——可能引入系统误差。

---

## 4.8 潜在问题 [CRITIQUE]

[CRITIQUE]
1. 假设 HD 35299 的宏湍流展宽对**所有星**代表，这在超巨星与 B3 冷星中可能不成立——超巨星宏湍流可达 ~20 km s⁻¹（Ebbets 1979），与 HD 35299 的 ~13 km s⁻¹ 差异会引入 2–5 km s⁻¹ 系统偏移；
2. 谱带选择避开 C II 在热/冷端的弱线区，但未说明 O II 与 N II 带在极端温度是否也变弱——可能引入温度依赖的 V sin i 系统误差；
3. 未讨论**恒星风**对线宽的影响——大质量 B 星有微弱星风，可能贡献额外的不对称展宽。