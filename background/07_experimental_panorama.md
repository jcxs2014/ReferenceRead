---
title: 07_experimental_panorama
category: 背景知识
status: completed
read_date: '2026-08-16'
lastread: '2026-08-16'
tags:
- '07'
- experiments
- multi-messenger
- panorama
citations:
  - '[[04_experiments/0001_lhaaso-2021/literature_analysis/00_overview|0001_lhaaso-2021]]'
  - '[[04_experiments/0002_ams02-2015/literature_analysis/00_overview|0002_ams02-2015]]'
  - '[[04_experiments/0003_icecube-2013/literature_analysis/00_overview|0003_icecube-2013]]'
  - '[[04_experiments/0004_hess-2016/literature_analysis/00_overview|0004_hess-2016]]'
path: background/07_experimental_panorama.md
---
# 7. 实验观测全景（现代天文台与多信使测量）

> 本综述整合 04 实验域首批 4 篇现代观测文献（LHAASO / AMS-02 / IceCube / HESS）的精确精读分析，覆盖伽马射线天文（PeV 能段）、精密带电粒子谱、天体物理中微子三大观测通道，以及它们对库内理论（DSA 加速、UHECR 起源、银河系 CR 传播）的约束。

## 7.1 四大实验总览

| 实验 | 类型 | 观测通道 | 能量/刚性范围 | 核心成就（本库精读） |
|---|---|---|---|---|
| **LHAASO**（2021, Nature 594:33） | 地面 EAS 阵列（KM2A） | γ 射线 | 0.1–1.4 PeV | 12 个银河系源 >100 TeV，最高 **1.4 PeV** 光子（J2032+4102），PeVatron 证实 |
| **AMS-02**（2015, PRL 114:171103） | 空间磁谱仪（ISS） | 带电粒子（质子） | 1 GV–1.8 TV 刚性 | 300 M 质子事例，谱指数 >100 GV 变硬，99.9% C.L. 排除单幂律 |
| **IceCube**（2013, Science 342:1242856） | 南极冰层切伦科夫 | 高能中微子 | 30 TeV–1 PeV+ | 28 起天体物理中微子候选（26 新增），~4σ 证据 |
| **HESS**（2016, Nature 531:476） | 地面成像大气切伦科夫 | γ 射线 | 0.1–数十 TeV | 银河中心扩散发射 + Sgr A* 点源，PeVatron 质子加速证据 |

## 7.2 LHAASO：银河系 PeV 光子源（Cao et al. 2021）

**探测器**：KM2A（1 km² 电磁阵列 5,195 EDs + 缪子阵列 1,188 MDs，MD 埋深 2.5 m/20 辐射长度屏蔽电磁分量），以 $N_\mu/N_e < 1/230$ 判选 γ 光子。CR 抑制达 $10^{-5}$ @1 PeV → **background-free 探测模式**（区别于 IACT 的模板减背景）。

**关键测量**：
- 308 天运行，**12 个源**共 >530 个 >100 TeV 光子，全部 ≥7σ
- 最高能量光子 **1.4 PeV**（来自 J2032+4102，γ Cygni 超新星遗迹候选）
- 10 个源的 SED 延伸到 >100 TeV（ΔlogE=0.2 分 bin，向前展开 + 最小 χ² 重建）

**科学意义**：
- 首次以 background-free 方式**证实银河系 PeVatron 存在**（此前只有 HESS 的谱外推证据）
- 12 源多为年轻超新星遗迹/脉冲星风云——支持 **SNR 是银河系 CR 加速源**（DSA 理论，Bell 1978）

## 7.3 AMS-02：精密质子谱与谱指数异常（Aguilar et al. 2015）

**探测器**：ISS 上 AMS-02 磁谱仪（1.4 kG 永磁 + 9 层硅径迹 + 4 层 TOF + ACC + RICH + TRD + ECAL），基于 **300 M 质子事例**。

**关键测量**：
- 质子流强 $\Phi(R)$：72 bin 覆盖 **1 GV–1.8 TV**，系统误差 <5%（中刚性端）
- 谱指数 $\gamma(R) = d\ln\Phi/d\ln R$：在 **>100 GV 以上逐步变硬**（谱指数随刚性上升而减小）
- 双幂律拟合 45 GV–1.8 TV：χ²/d.o.f. = 25/26，**99.9% C.L. 排除单幂律假设**

**科学意义**：
- 谱指数变硬是**模型无关**发现——约束源谱 $\gamma_{\rm inj}$、传播扩散系数 $K \propto R^\delta$ 的谱与能量依赖
- 与库内传播模型（weinrich-2020 晕大小、genolini-2021 参数化）直接对接

## 7.4 IceCube：天体物理中微子证据（Aartsen et al. 2013）

**探测器**：南极冰层 1 km³ 切伦科夫探测器（86 串 DOM，冰层作介质），探测高能中微子穿过冰层产生的级联/径迹事件。

**关键测量**：
- **28 起高能中微子候选事件**（30 TeV–1.2 PeV），其中 26 起新增（含 2 起此前报告的 PeV 事件）
- 大气中微子背景期望 ~10.6 起 → 超出 ~4σ（天体物理起源证据）

**科学意义**：
- **首个银河系外高能中微子源的间接证据**——中微子是唯一不受吸收/偏转的宇宙信使，直接探测 CR 加速位点
- 与 UHECR 起源（kotera-olinto-2011、alvesbatista-2019）的多信使关联（中微子 = 质子加速的伴生产物）

## 7.5 HESS：银河中心 PeVatron（H.E.S.S. 2016）

**探测器**：纳米比亚 4×12 m 成像大气切伦科夫望远镜（IACT），VHE γ 射线。

**关键测量**：
- 银河中心 **扩散 γ 射线发射**（0.1–40 TeV 能谱）延伸到 >10 TeV 且谱形态支持质子起源
- **Sgr A\* 点源** + 周围分子云（CNR）的 γ 发射——CR 与气体相互作用产生
- 谱指数与能量截断给出**质子加速到 PeV** 的证据（PeVatron）

**科学意义**：
- 与 LHAASO 2021 互为印证（一个外推、一个直接探测到 1.4 PeV 光子）
- 银河中心作为 CR 加速位点：Sgr A\* 冲击/超新星遗迹 + 中心分子云

## 7.6 对理论的约束（与库内理论连线）

| 观测 | 约束的理论 | 库内对应篇 |
|---|---|---|
| LHAASO 12 源 >100 TeV / 1.4 PeV | SNR DSA 加速上限、PeVatron 存在性 | bell-1978、caprioli-2014、giacalone-2017 |
| AMS-02 谱指数变硬 | 源谱/传播参数、CR 起源模型 | weinrich-2020、genolini-2021、mewaldt-2001 |
| IceCube 中微子 | UHECR 起源、多信使关联 | kotera-olinto-2011、alvesbatista-2019、bhattacharjee-sigl-2000 |
| HESS 银河中心 | 银河中心 CR 密度、PeVatron | gabici-2019（CR 海）、blasi-2013 |

**多信使闭环**：HESS 与 LHAASO 从 γ 射线侧证 PeVatron（加速位点）→ IceCube 从中微子侧探 CR 产物（>100 TeV 质子 pp/pγ 必然伴生中微子）→ AMS-02 从带电粒子侧约束传播谱（银河系内 CR 谱形态）——四通道共同拼出"源-加速-传播-观测"完整链条。

## 7.7 实验域精读文献（04 域）

- `0001_lhaaso-2021`：PeV γ 射线源（Nature 594, 33–36）
- `0002_ams02-2015`：精密质子谱（PRL 114, 171103）
- `0003_icecube-2013`：天体物理中微子证据（Science 342, 1242856）
- `0004_hess-2016`：银河中心 PeVatron（Nature 531, 476–479）

> 各篇完整精读见对应 `literature_analysis/`（路径 B 八段：探测器/测量/统计显著性/对照理论/系统误差/结论）。
