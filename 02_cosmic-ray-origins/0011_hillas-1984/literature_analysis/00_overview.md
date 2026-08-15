---
title: The Origin of Ultra-High-Energy Cosmic Rays
authors: A. M. Hillas (University of Durham)
year: '1984'
journal: Ann. Rev. Astron. Astrophys. 22, 425 (1984)
pages: '425-444'
doi: 10.1146/annurev.aa.22.090184.002245
category: 宇宙线起源
status: completed
read_date: '2026-08-15'
lastread: '2026-08-15'
tags: []
citations: []
path: 02_cosmic-ray-origins/0011_hillas-1984/literature_analysis/00_overview.md
---
> 状态：**精读完成**（2026-08-15）
> ★ **UHECR 起源判据**——Hillas 判据（Hillas 1984）是争议主题 4（SNR 范式）的核心理论判据；提出 PeVatron 概念

# 00. Overview — Hillas (1984) 精读笔记

## 基本信息

| 字段 | 内容 |
|---|---|
| **Title** | The Origin of Ultra-High-Energy Cosmic Rays |
| **Authors** | A. M. Hillas (University of Durham) |
| **Journal** | Ann. Rev. Astron. Astrophys. 22, 425 (1984) |
| **DOI** | 10.1146/annurev.aa.22.090184.002245 |
| **Year** | 1984 |
| **Pages** | 425-444（20 pages） |

## [FACT] 论文内容

### 核心问题
哪些天体能够将宇宙线粒子加速到 >10^18 eV（UHECR）？文章提出**Hillas 判据**：加速区域的大小 $L$ 和磁场 $B$ 必须满足 $BL \gtrsim 10^{15}$ V，才能克服辐射损失实现有效加速。

### Hillas 判据推导
粒子在加速区被磁场约束，gyroradius $r_g = E/(ZeB)$。有效加速要求 $r_g \lesssim L$，即：
$$BL \gtrsim 
rac{E}{Ze} pprox 10^{15} \,	ext{V}$$
其中 $E$ 以 EeV 为单位，$B$ 以 μG 为单位，$L$ 以 pc 为单位。

### 已知加速源评估
| 天体 | B (μG) | L (pc) | BL | 能达 EeV? |
|---|---|---|---|---|
| SNR（典型） | 100 | 3 | 300 | ~10^15 eV（PeVatron） |
| AGN hotspot | 10^4 | 10^6 | 10^10 | >>10^20 eV ✓ |
| GRB | 10^10 | 10^8 | 10^18 | >>10^20 eV ✓ |
| 银河系内 | ~3 | ~30 | 90 | ~10^17 eV 上限 |

### 关键洞察
- **PeVatron**：银河系内 SNR 最多只能将 CR 加速到 ~10^15 eV（PeV），无法解释 >10^18 eV 的 UHECR
- **河外起源必然**：>10^19 eV 的 UHECR 必须是 AGN 或 GRB 加速的
- **Hillas 图**：以 log B vs log L 为坐标的天体分布图，直观显示哪些源能达到 UHECR 能量

## [INTERPRETATION] 物理意义

### 为什么 Hillas 判据重要
这是第一个系统性回答"什么天体能加速到 UHECR"的理论框架——不是解释 CR 的谱指数，而是给出能量上限的几何约束。

### 与 DSA 的关系
Hillas 1984 时 DSA 刚被提出（Bell 1978 / BO 1978），但 Hillas 判据独立于 DSA 的具体机制——它只要求"粒子被约束在加速区"，是任何加速机制的必要条件。

### 后续影响
- 1987 年 BE 1987 综述直接引用本文作为 UHECR 起源的理论框架
- 2013 年 Auger 实验发现" dipole  anisotropy"指向银河系中心方向——部分与 Hillas 图矛盾（AGN 预期在银河系外）
- 2021 年 T Prize → TA 2023 Amaterasu 事件进一步挑战"AGN 中心"模型

## [CRITIQUE] 批判性分析

### 优点
1. **框架通用性**：不依赖 DSA 具体参数，只用 gyroradius 约束
2. **预测性**：明确排除银河系内 SNR 作为 UHECR 来源
3. **图表直观**：Hillas 图成为领域标准工具

### 局限
1. **忽略能量损失时间尺度**：Hillas 判据只检查"能否约束"，未考虑同步辐射、逆康普顿等能量损失
2. **磁场估计不确定性大**：许多天体 B 和 L 的估计误差可达 2-3 个量级
3. **不解释谱指数**：只回答能量上限，不解释观测到的幂律谱

## 前序阅读 / 关联论文

| 关系 | 论文 | 说明 |
|---|---|---|
| 加速机制基础 | **Bell 1978 / BO 1978 / BE 1987** | DSA 奠基三件套 |
| 后续验证 | **Alves Batista et al. 2019** | UHECR 开放问题，含 Hillas 图讨论 |
| 观测挑战 | **Telescope Array 2023** | Amaterasu 事件（EeV 级）|

## 关键词

`Hillas criterion` `UHECR` `PeVatron` `AGN` `GRB` `gyroradius` `diffusive shock acceleration`
