---
title: "Precision Measurement of the Proton Flux in Primary Cosmic Rays from Rigidity 1 GV to 1.8 TV with the AMS-02 on the ISS"
authors: "M. Aguilar, D. Aisa, B. Alpat, et al. (AMS Collaboration)"
year: 2015
read_date: '2026-08-16'
lastread: '2026-08-16'
status: completed
journal: "Phys. Rev. Lett."
volume: "114"
pages: "171103"
doi: "10.1103/PhysRevLett.114.171103"
arxiv: "1501.02755"
category: "experiments"
sections: []
citations:
  - "[[0003_weinrich-2020]]"
  - "[[0005_genolini-2021]]"
  - "[[0004_mewaldt-2001-clocks]]"
---

# 0. 文献基本信息
> 论文：AMS-02 质子谱精确测量（PRL 114, 171103, 2015）

## 核心发现

AMS-02 在 ISS 上基于 **3 亿质子事例**，精确测量了刚性 **1 GV – 1.8 TV** 范围内宇宙线质子流强，给出了质子流强谱指数的详细刚性依赖——谱指数在刚性 >100 GV 以上逐步变硬（hardening），单一幂律在 99.9% C.L. 被排除。这为宇宙线源谱与传播模型提供高精度约束。

## 元数据校验（三源一致）

| 来源 | 作者 | 年份 | 期刊 |
|---|---|---|---|
| 任务上下文 | Aguilar et al. (AMS) | 2015 | PRL 114, 171103 |
| 目录名 | ams02-2015 | 2015 | — |
| PDF 第 1 页 | Aguilar, M. et al. (AMS Collaboration) | 2015 | Phys. Rev. Lett. 114, 171103 |

三源完全一致，无勘误。

## 文献定位

- **观测类型**：磁谱仪直接测量宇宙线初级成分质子（轨道平台）
- **核心约束**：刚性依赖的质子流强 $\Phi(R)$ 与谱指数 $\gamma(R)$——为银河系传播模型（diffusive reacceleration, Alfvén 湍流谱）提供数据输入
- **相关库内文献**：weinrich-2020（时钟方法测扩散）、genolini-2021（传播系数拟合）、mewaldt-2001-clocks（短寿命同位素对加速延迟的约束）
- **库内同主题实验**：hess-2016（VHE γ 射线、PeVatron）、icecube-2013（高能中微子）、lhaaso-2021（宇宙线膝区）

## 数据与时间线

- 观测窗口：**2011-05-19 至 2013-11-26**，共 30 个月（有效 $7.96\times10^{7}$ s）
- 原始事例：$4.1\times10^{10}$ 宇宙线事件
- 初级 $Z=+1$ 选例后：$3.0\times10^{8}$ 质子（含少量氘核污染）
- 刚性分辨率、接受度、触发效率、磁场、几何因子——全部来自 CERN SPS 束流测试 + ISS 原位监测

## 0.3 论文结构树（路径 B：八段模板，实验短篇 <20 页）

- `01_detector_and_method` — AMS-02 磁谱仪与质子选择方法
- `02_proton_flux_results` — 1 GV–1.8 TV 质子流强测量
- `03_spectral_index_anomaly` — 谱指数 $\gamma(R)$ 变硬现象
- `04_implications_for_cosmic_ray_physics` — 对宇宙线起源与传播的约束
- `05_background_and_systematics` — 背景与系统误差
- `06_statistical_power` — 统计能力与拟合质量
- `07_comparison_with_previous_experiments` — 与 ATIC-2 / BESS-Polar II / CREAM / PAMELA 对比
- `08_conclusions` — 结论
- `97_quality_check.md`、`98_vocabulary.md`、`99_final_summary.md`

## Figure 目录

| 编号 | 内容 |
|---|---|
| Fig. 1 | $1/R$ 分辨率（400 GeV/c 束流 vs MC），高斯核 + ~5% 非高斯尾 |
| Fig. 2 | 系统误差独立校验：（a）$\theta$ 角依赖（>30 GV）；（b）时间稳定性（>45 GV）；（c）L1 入口区；（d）内径迹 vs 全径迹 |
| Fig. 3 | （a）AMS 质子流强 $\times \tilde{R}^{2.7}$ vs 刚性；（b）AMS 与 ATIC-2/BESS-Polar II/CREAM/PAMELA 对比 |
| Fig. 4 | （a）AMS 数据 vs Eq.(3) 双幂律拟合（实线）与 $\Delta\gamma=0$ 情形（虚线）；（b）谱指数 $\gamma$ vs 刚性 |

## Table 目录

本论文无表格。流强 $\Phi_i$ 的逐 bin 表格与系统误差分量发布在 Supplemental Material (Ref. [25])。

## 关键数值（速查）

| 物理量 | 数值 | 出处 |
|---|---|---|
| 观测时间 | 30 个月（$7.96\times10^{7}$ s） | p.2 |
| 质子事件数 | $3.0\times10^{8}$ | p.2 |
| 测量刚性范围 | 1 GV – 1.8 TV | 全文 |
| Bin 数 | 72 | p.2 |
| 磁场中心 | 1.4 kG | p.2 |
| 磁场稳定度 | $-0.09\%$/°C | p.2 |
| 电荷分辨率 | $\Delta Z \simeq 0.05$（$\lvert Z\rvert=1$） | p.3 |
| 径迹坐标分辨率 | 10 μm | p.3 |
| MDR（最大可测刚性） | 2 TV（3 m 力臂 L1→L9） | p.3 |
| 触发效率 | 90%–95% | p.3 |
| 接受度修正 | 5%（1 GV）→ <2%（>10 GV） | p.4 |
| $\chi^2$/d.o.f.（Eq.3 拟合） | $25/26$ | p.6 |
| 归一化 $C$ | $0.4544\pm0.0004(\text{fit})^{+0.0037}_{-0.005}(\text{sys})\pm0.0027(\text{sol})$ | p.6 |
| 低刚性谱指数 $\gamma$ | $-2.849\pm0.007(\text{fit})^{+0.005}_{-0.004}(\text{sys})\pm0.004(\text{sol})$ | p.6 |
| 谱指数增量 $\Delta\gamma$ | $0.133^{+0.032}_{-0.030}(\text{fit})^{+0.046}_{-0.043}(\text{sys})^{+0.003}_{-0.005}(\text{sol})$ | p.6 |
| 转折刚性 $R_0$ | $336^{+68}_{-64}(\text{fit})^{+86}_{-76}(\text{sys})\pm1(\text{sol})$ GV | p.6 |
| 平滑度 $s$ | $0.024^{+0.020}_{-0.013}(\text{fit})^{+0.027}_{-0.016}(\text{sys})^{+0.006}_{-0.004}(\text{sol})$ | p.6 |
