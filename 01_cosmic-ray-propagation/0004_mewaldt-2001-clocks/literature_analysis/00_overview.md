---
title: Radioactive Clocks and Cosmic-ray Transport in the Galaxy
authors: R. A. Mewaldt, N. E. Yanasak, M. E. Wiedenbeck et al.（Caltech/JPL/Washington U/NASA Goddard）
year: '2001'
journal: Space Science Reviews 99, 137 (2001)
pages: '137-151'
doi: 10.1023/A:1013873705653
category: 宇宙线传播
status: completed
read_date: '2026-08-15'
lastread: '2026-08-15'
tags: []
citations: []
path: 01_cosmic-ray-propagation/0004_mewaldt-2001-clocks/literature_analysis/00_overview.md
---
> 状态：**精读完成**（2026-08-15）
> ★ **放射性时钟**——主题 1（传播参数）核验方法：用放射性同位素（Be-10/Al-26/Cl-36）约束 CR 在银河系停留时间

# 00. Overview — Mewaldt et al. (2001) 精读笔记

## 基本信息

| 字段 | 内容 |
|---|---|
| **Title** | Radioactive Clocks and Cosmic-ray Transport in the Galaxy |
| **Authors** | R. A. Mewaldt, N. E. Yanasak, M. E. Wiedenbeck et al.（Caltech/JPL/Washington U/NASA Goddard） |
| **Journal** | Space Science Reviews 99, 137 (2001) |
| **DOI** | 10.1023/A:1013873705653 |
| **Year** | 2001 |
| **Pages** | 137-160 |

## [FACT] 论文内容

### 核心问题
CR 中含有多种放射性同位素（Be-10、Al-26、Cl-36 等），其半衰期与 CR 在银河系的传播时间尺度相当。通过测量这些"时钟"的丰度比，可以直接约束 CR 的传播时间参数。

### 三种放射性时钟
1. **Be-10（半衰期 1.5 Myr）**：测量 Be-10/Be-9 比值，约束 CR 在传播过程中相对于 B/C 的额外损失
2. **Al-26（半衰期 0.7 Myr）**：Al-26/Al-27 比值，探测 freshly accelerated material 的成分
3. **Cl-36（半衰期 0.3 Myr）**：Cl-36/S 比值，短时间尺度过程的探针

### ACE 观测结果
ACE（Advanced Composition Explorer）高分辨率质谱仪使 Be-10/Be-9 测量精度大幅提升：
- Be-10/Be-9 ≈ 0.03（在 100-300 MeV/nuc 范围）
- 这要求 CR 在传播过程中有显著的二次 Be-10 产生（与星际介质碰撞）

### 传播时间约束
基于 Be-10 丰度，CR 在银河系的平均停留时间：
$$\tau_{esc} \approx \frac{10^7 \text{ yr}}{D_{xx}} \times 10^{28} \text{ cm}^2/\text{s}$$
其中 $D_{xx}$ 是扩散系数。

## [INTERPRETATION] 物理意义

### 为什么同位素时钟重要
与 B/C 比值不同，放射性同位素提供的是**绝对时间尺度**约束——不受传播模型参数化的影响，直接与物理时间挂钩。

### 与扩散模型的关系
- 纯扩散模型预测 Be-10/Be-9 偏高（传播时间太长）
- 需要再加速（reacceleration）或对流（convection）来降低 Be-10 丰度
- 这支持 Strong et al. 的"含再加速的扩散模型"

### 对 SNR 源的约束
Al-26/Al-27 高丰度要求 CR 源必须含有 freshly synthesized material——支持 SN 作为 CR 来源（SNR 中的 freshly accelerated material）。

## [CRITIQUE] 批判性分析

### 优点
1. **直接时间约束**：放射性半衰期是物理常数，不依赖模型
2. **多同位素交叉验证**：三种时钟相互印证
3. **ACE 数据质量**：高分辨率质谱使测量精度提升一个量级

### 局限
1. **星际介质组成不确定**：Be-10 产额依赖于ISM 的化学组成
2. **传播模型依赖**：最终约束仍需假设扩散-对流-再加速的相对权重
3. **仅银河系**：结果不直接适用于河外 CR 传播

## 前序阅读 / 关联论文

| 关系 | 论文 | 说明 |
|---|---|---|
| 传播模型 | **Strong et al. 2007** | GALPROP 扩散-再加速模型 |
| 传播参数 | **Amato & Blasi 2018** | 现代 DSA 传播综述 |
| B/C 约束 | **Génolini et al. 2021** | B/C 传播参数最新拟合 |

## 关键词

`radioactive clocks` `Be-10` `Al-26` `Cl-36` `ACE` `cosmic-ray age` `diffusive reacceleration`
