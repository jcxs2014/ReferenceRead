---
title: "§1 Detector and Method"
paper: "hess-2016"
section: 1
nav_prev: ""
nav_next: "02_diffuse_emission_observations.md"
---
上一章：`00_overview.md` — 概述
下一章：`02_diffuse_emission_observations.md` — Detector and Method

# §1 Detector and Method — HESS 望远镜阵列与观测模式

## [FACT] 1.1 HESS 探测系统

HESS（High Energy Stereoscopic System）位于纳米比亚，是四台 13 米成像大气切伦科夫（IACT）望远镜组成的阵列。各台望远镜从不同视角同时记录大气簇射产生的契伦科夫光，立体成像实现精确方向重建和能量测量。

关键参数（原文 p.36–37，Methods 部分）：

- **能量范围**：100 GeV – 数十 TeV
- **角度分辨率**：~0.1°（对点源）
- **能量分辨率**：~15%
- **巡天灵敏度**：1% Crab Nebula（1 小时观测）

观测策略：2014–2015 年对银河系中心分子云区域累计 ~254 小时的深观测，获得迄今最深的 VHE γ射线图像。

## 观测对象：银河系中心分子云

银心分子云区（Central Molecular Zone, CMZ）：
- 分子氢总质量：~3 × 10$^{7}$ M☉（原文 p.37）
- 密度：n ~ 10$^{2}$–10$^{4}$ cm$^{-3}$（局部）
- 延伸范围：l ≈ ±0.5°，|b| ≈ ±0.3°（银经 ±0.5°，银纬 ±0.3°）
- 中心距离：d = 8.5 kpc（原文 p.37）

[FACT] CMZ 分子氢面密度在 Sgr A* 附近最高，向外递减，分布与 HESS γ射线亮度强相关（原文 p.37，Fig. 1）。

## [FACT] 1.2 γ射线 vs 宇宙线信号

VHE γ射线探测有两种产生机制（原文 p.34）：

1. **强子过程（Hadronic）**：质子-质子碰撞 → $\pi^{0}$ 衰变 → γ射线（能量 ~质子能量的 ~1/20）
2. **轻子过程（Leptonic）**：高能电子逆康普顿散射（IC）

判据（原文 p.34）：电子在 CMZ 强辐射场中快速损失能量（10 TeV 电子冷却时间 ~1 年 << 传播时间），因此电子无法产生覆盖 ~70 pc 尺度的弥散 γ射线辐射 → **轻子机制被排除**，强子机制主导。

[FACT] 多 TeV 电子辐射寿命 << CMZ 传播时间 → 轻子机制被排除（原文 p.34，Methods）。