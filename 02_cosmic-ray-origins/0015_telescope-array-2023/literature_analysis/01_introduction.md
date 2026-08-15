---
title: "1. Introduction — UHECR 起源与 Amaterasu 事件"
paper: "Telescope Array Collaboration 2023, An extremely energetic cosmic ray observed by a surface detector array"
outline_ref: "§1 引言"
original_sections: ["§1 引言; The Telescope Array experiment; Energetic particle on 27 May 2021"]
---

> 下一章：`02_energy_reconstruction.md`

## 1.1 [FACT] 论文基本信息

| 字段 | 内容 |
|------|------|
| Title | An extremely energetic cosmic ray observed by a surface detector array |
| 期刊 | Science 380, 6629, 903–907 (2023) |
| DOI | 10.1126/science.abo5095 |
| arXiv | **2311.14231**（⚠️ 00_overview 中的 2306.16960 是错误 ID，已被重新分配为渔业论文） |
| 通信作者 | Toshihiro Fujii (toshi@omu.ac.jp)，Osaka Metropolitan University |
| 对应事件 | Amaterasu 事件，2021 年 5 月 27 日 |

## 1.2 [FACT] 科学背景

UHECR（Ultra-high-energy Cosmic Rays）定义：**能量 $> 10^{18}$ eV = $1$ EeV** 的带电粒子，比人造加速器（LHC 质子能量 $7$ TeV）高约 $10^5$ 倍。

**候选起源（Hillas 判据 Hillas 1984）**：
- 相对论喷流（AGN 相对论性外流）
- 伽马射线暴（GRB）
- 星系团大尺度吸积激波
- 超越标准模型的新物理（受 UHE 光子流量上限约束）

**关键物理限制**：带电粒子在银河系和河外磁场中偏转，到达方向不一定指向源——但**能量越高，偏转越小**，方向与源的关联越强。

## 1.3 [FACT] GZK 效应

$> 60$ EeV 的 UHECR 与 CMB 相互作用产生 GZK 抑制：
- **质子**：$\Delta$ 共振 $p + \gamma_{\rm CMB} \to \Delta^+ \to p + \pi^0$（或 $n + \pi^+$）
- **重核**：光致离解 $A + \gamma \to A' + N$

GZK 效应将最高能量粒子的起源限制在 **$50$–$100$ Mpc** 内（在此距离以上粒子被 CMB 吸收）。TA 合作组计算的传播距离：
- 铁核 $D_0 = 10.3^{+5.3}_{-3.0}$ Mpc
- 质子 $D_0 = 27.0^{+3.8}_{-3.0}$ Mpc

在此距离尺度上，宇宙**不均匀**——物质集中在星系团、纤维状结构和巨洞（voids）之间的 LSS 中。

## 1.4 [FACT] Telescope Array 实验概况

| 参数 | 值 |
|------|-----|
| 位置 | 美国犹他州，$39.30°$N, $112.91°$W，海拔 $1370$ m |
| 表面探测器 (SD) | $507$ 站，$1.2$ km 等边网格，总面积 $700$ km$^2$ |
| 探测器 | 每站两层 $3$ m$^2$ 塑料闪烁体 |
| 荧光探测器 (FD) | 直接测量 EAS 在大气中的发展，提供量热计能量测量 |
| 到达方向 | GPS 同步时间，SD 站间时差 → 精度 $1.5°$ |
| 能量分辨率 | SD $15\%$ 统计，$21\%$ 系统 |
| 运行时间 | $2008$ 年 5 月 – $2021$ 年 11 月，$13.5$ 年 |
| 暴露 | $1.6 \times 10^4$ km$^2$ sr yr（$> 100$ EeV 选择） |

## 1.5 [FACT] 能量与质量的测量方法

- **能量**：用 $800$ m 处的粒子密度 $S_{800}$ 作为能量指标，通过与 FD 量热计能量比对，校正因子 $1/1.27$
- **质量**：FD 通过 $X_{\max}$（EAS 最大发展深度，单位 g/cm$^2$）确定；TA 不做单事件质量确定
- SD 间接质量信息通过机器学习提取（Kharuk & Kalashev 2021 神经网络）

## 1.6 [FACT] 历史对比

| 年份 | 事件 | 能量 (EeV) | 探测器 | 半球 |
|------|------|-----------|--------|------|
| 1962 | Linsley | $\sim 10^2$ | 地面 | 北 |
| 1991 | Fly's Eye (Abu-Zayyad 1994) | 320 | FD | 北 |
| 1993 | Bird et al. (1995) | 213 | SD | 北 |
| 2001 | Hayashida/AGASA (2001) | 280 | SD | 北 |
| **2021** | **Amaterasu (TA)** | **244** | **SD + FD 校准** | **北** |

南半球（Auger）未发现有 $> 166$ EeV 的事件（但 Auger 与 TA 能量标度有差异 Verzi & Ivanov 2017）。