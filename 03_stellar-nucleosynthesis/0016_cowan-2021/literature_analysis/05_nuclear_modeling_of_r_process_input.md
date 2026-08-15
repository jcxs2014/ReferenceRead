---
title: '05. Nuclear Modeling of r-Process Input'
authors: J. J. Cowan, C. Sneden, J. E. Lawler et al.
year: '2021'
journal: Rev. Mod. Phys. 93, 015002 (2021)
category: 恒星核合成
chapter: §V
status: completed
read_date: '2026-08-15'
path: 03_stellar-nucleosynthesis/0016_cowan-2021/literature_analysis/05_nuclear_modeling_of_r_process_input.md
---

# §V. Nuclear Modeling of r-Process Input — 精读笔记

## §V.1 本节核心内容

§V 覆盖 §IV 中未测核素的理论输入，分四子节：

- **§V.A 核质量**——FRDM、HFB、Duflo-Zuker
- **§V.B β-decay 半衰期**——pn-QRPA、FRDM+QRPA
- **§V.C 中子俘获率**——TALYS、NON-SMOKER、Hauser-Feshbach
- **§V.D 裂变**——裂变势垒、fragment yields、neutron-induced fission

§V 的核心命题：**§IV 实验未覆盖的核素性质必须用核理论模型填充——这些模型的不确定度是 r 过程产额预测的"次级瓶颈"**。

## §V.2 原文内容（FACT 摘录）

### §V.A — Nuclear masses

> **[FACT]** **FRDM** (Möller et al. 2016)：宏观-微观模型。AME2020 基准上对已知核素质量预测误差 ~0.5 MeV。

> **[FACT]** **HFB** (Goriely et al. 2009, 2010, 2016)：基于 Skyrme / Gogny 的微观 HFB 模型。

> **[FACT]** **Duflo-Zuker** (1995)：半经验 shell-model。

> **[FACT]** 现代 mass 模型在已知区域 $\sigma \sim 0.3-1.0$ MeV；外推到极中子丰富核素时 ~2-3 MeV。

### §V.B — β-decay half-lives

> **[FACT]** 模型：
> - **Gross-Frenkel-Tueros**：基于 Gamow-Teller 巨共振
> - **pn-QRPA** (Möller et al. 2003, 2019)：FRDM 质量 + QRPA 跃迁矩阵元
> - **FRDM + QRPA**：当前最广泛使用

> **[FACT]** β-decay $T_{1/2}$ 预测不确定度：稳定线附近 ~10%；远离稳定线 ~30-50%。**P_n** 预测通常 ~50% 系统差。

### §V.C — Neutron captures

> **[FACT]** 中子俘获率计算方法：
> - **Hauser-Feshbach 统计模型**：$E_n \gg D_0$ 时适用
> - **TALYS** (Koning et al. 2008)：开源 Hauser-Feshbach
> - **NON-SMOKER** (Rauscher et al. 2001)：简化版统计模型

> **[FACT]** **关键限制**：r 过程等待点 magic N=50, 82, 126 处 Hauser-Feshbach 失效——需 direct capture 或实验（Oslo, surrogate）。

### §V.D — Fission

> **[FACT]** r 过程中的裂变途径：
> 1. **β-delayed fission**：β-decay 后 Z 过高 → 自发裂变
> 2. **Neutron-induced fission**：r 过程路径末端的 $A \sim 260$ 核在额外 n-capture 后裂变
> 3. **Spontaneous fission**：长寿命锕系

> **[FACT]** 裂变 fragment yield 分布：从单峰（symmetric, A ≈ 130）到双峰（asymmetric, A ≈ 110 + 140），由裂变势垒的 shell 修正决定（Kowal et al. 2019）。

## §V.3 关键公式

### FRDM 能量

$$E_{macro} = a_v A + a_s A^{2/3} + a_c \frac{Z^2}{A^{1/3}} + ...$$

### 壳修正（Strutinsky）

$$\delta E = \sum_i \epsilon_i - \int \bar{g}(\epsilon)\epsilon d\epsilon$$

### β-decay rate（allowed GT）

$$\lambda_\beta = \frac{G_F^2 |V_{ud}|^2 m_e^5 c^4}{2\pi^3 \hbar^7} f(Z,E_0) \langle\sigma\rangle^2 |M_{GT}|^2$$

### Hauser-Feshbach

$$\sigma_{n,\gamma}(E_n) = \frac{\pi \lambdabar^2}{(2I_a+1)(2I_A+1)} \sum_J (2J+1) \frac{T_n T_\gamma}{T_{total}}$$

### 裂变穿透率（WKB）

$$T_{fission} = \frac{1}{1 + \exp\left[2\int_{r_1}^{r_2} \sqrt{2\mu(V(r) - E)}/\hbar \, dr\right]}$$

## §V.4 关键参数 / 模型对比

| 模型 | 输入 | 预测对象 | 不确定度 |
|---|---|---|---|
| FRDM | AME 实验 mass | 全部核素 mass | ~0.5 MeV（已知区） |
| HFB-31/32 | HFB 计算 | 全部核素 mass | ~0.5-1.0 MeV |
| Duflo-Zuker | AME 拟合 + 微观 | mass | ~0.3-0.5 MeV |
| FRDM+QRPA | FRDM mass + QRPA | β-decay $T_{1/2}$ | ~10-50% |
| TALYS 1.9+ | 核质量 + 能级 | n-capture σ | ~30% |
| Kowal 2019 | HFB potential | 裂变 yields | 模型依赖 ~50% |

## §V.5 图表分析

### Figure 8 — 核质量模型预测对比

**1. 图的目的**：比较 FRDM / HFB / Duflo-Zuker 模型误差。

**2. 坐标轴**：横轴 $N$，纵轴 $Z$。

**3. 图中元素**：
- 蓝色方块：误差 < 0.5 MeV
- 红色方块：误差 > 0.5 MeV

**4. 关键观察**：
- 已知区域：99% 核素误差 < 0.5 MeV
- N = 50, 82, 126 区域：模型预测较准
- 远离稳定线：误差显著放大

**5. 数值信息**：
- FRDM (2016)：RMS ~0.6 MeV
- HFB-31：RMS ~0.5 MeV
- Duflo-Zuker：RMS ~0.4 MeV

**6. 作者的解释**：模型在已知区可靠，外推到 r 过程路径时不确定度显著增加。

**7. 与正文的关系**：§V.A 核心证据。

**8. 物理意义**：mass 是 r 过程路径的"地图"——mass 误差 1 MeV 可导致路径偏移 5-10 个质量单位。

**9. 需要注意的问题**：
- "已知区拟合优"不能保证外推精度
- 不同模型在 drip line 附近分歧可达 ~2-3 MeV

### Figure 9 — β-decay 半衰期模型预测 vs 实验

**1. 图的目的**：对比 Möller 2019 等模型的 β-decay $T_{1/2}$ 预测与实验值。

**2. 坐标轴**：横轴实验 $T_{1/2}$，纵轴预测 $T_{1/2}$（对数尺度）。

**3. 图中元素**：散点 + 误差棒 + 对角线。

**4. 关键观察**：大多数点落在对角线 ± 0.5 dex 内。

**5. 数值信息**：
- 已知区域：RMS ~0.3 dex
- 远离稳定线：RMS ~0.5-1.0 dex

**6. 作者的解释**：β-decay 模型对 r 过程模拟的关键影响——$T_{1/2}$ 错误 50% 可改变最终丰度 0.3-0.5 dex。

**7. 与正文的关系**：§V.B 定量证据。

**8. 物理意义**：β-decay 决定 r 过程路径上的"通过速率"。

**9. 需要注意的问题**：
- 实验测量的 $T_{1/2}$ 本身有 ~5-10% 系统差
- 部分核素的 GT 跃迁矩阵元难以精确计算

## §V.6 作者的逻辑

§V 逻辑是**"按网络方程的需求顺序"**：

1. **§V.A 核质量**——决定路径
2. **§V.B β-decay**——决定通过速率
3. **§V.C n-capture**——决定推进速率
4. **§V.D 裂变**——决定终点

## §V.7 我的理解 [INTERPRETATION]

### 模型选择的"工程哲学"

r 过程核数据建模有两种哲学：
1. **多模型平均**（如 REACLIB 的多模型加权平均）
2. **单一最佳模型**（如 FRDM+QRPA）

Cowan 2021 偏向**多模型对比**——展示 FRDM/HFB/Duflo-Zuker 的差异。

### 核数据缺口与 NSM 模拟的耦合

NSM ejecta 模拟高度依赖 §V 输入。"灵敏度测试"：
- mass 不确定度 1 MeV → 路径偏移 ~5 mass units
- β-decay $T_{1/2}$ 不确定度 50% → 最终丰度 0.3-0.5 dex
- n-capture rate 不确定度 30% → 第三峰形态 0.2 dex

### 裂变 recycling 的当代争议

§V.D 提及的"neutron-induced fission 在 r 过程末端的循环"是 NSM ejecta 模拟的核心：
- 裂变循环效率高：r 过程路径 $A \sim 260$ 全部裂变为 $A \sim 130$
- 裂变循环效率低：r 过程路径只到 $A \sim 200$，锕系产量高

## §V.8 潜在问题与值得关注的地方 [CRITIQUE]

### §V.8.1 优点
1. 模型覆盖全面
2. 不确定度量化
3. 物理量纲清晰

### §V.8.2 局限
1. FRIB 数据未整合
2. 理论-实验联合拟合未深入
3. 机器学习 mass 模型未提及
4. 裂变 yield 系统对比不充分
5. Ab-initio 方法未提及

## §V.9 关键术语

- **FRDM** (Finite-Range Droplet Model)
- **HFB** (Hartree-Fock-Bogoliubov)
- **QRPA** (Quasiparticle Random Phase Approximation)
- **Hauser-Feshbach**
- **TALYS**
- **GT 矩阵元** (Gamow-Teller matrix element)
- **Strutinsky 壳修正**
- **β-delayed fission**
- **裂变势垒** (fission barrier)
- **AME** (Atomic Mass Evaluation)

## §V.10 引用页码索引

| 主题 | 原文页码 | fulltext 行号 |
|---|---|---|
| §V 起始 | 015002-32 | 行 1829 |
| §V.A 核质量 | 015002-32 | 行 1900+ |
| §V.B β-decay | 015002-32 | 行 2013+ |
| §V.C 中子俘获率 | 015002-32 | 行 2114+ |
| §V.D 裂变 | 015002-32 | 行 2200+ |
| Fig. 8 (mass) | 015002-33 | 行 1950+ |
| Fig. 9 (β-decay) | 015002-34 | 行 2050+ |