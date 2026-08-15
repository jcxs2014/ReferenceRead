---
title: The acceleration of cosmic rays in shock fronts — I
authors: A. R. Bell (Mullard Radio Astronomy Observatory, Cavendish Laboratory, Cambridge)
year: '1978'
journal: Mon. Not. R. astr. Soc. 182, 147–156 (1978)
doi: 10.1093/mnras/182.2.147
arxiv: —（预印本时代前）
category: 02_cosmic-ray-origins
read_date: '2026-08-15'
lastread: '2026-08-15'
status: completed
pages: '147-156'
tags: [diffusive-shock-acceleration, first-order-fermi, test-particle, alfven-wave, spectral-index, power-law, snr]
citations: []
path: 02_cosmic-ray-origins/0008_bell-1978/literature_analysis/00_overview.md
---

# 0. 文献基本信息

> **PDF 文本层为空白**（NASA ADS 扫描版），精读基于 PDF 视觉读取（页 147–156）+ 已知物理推导交叉验证。
> 页码引用：MNRAS 182, 147–156（10 页）。

## 元数据

| 字段 | 内容 |
|---|---|
| **Author** | A. R. Bell（Mullard Radio Astronomy Observatory, Cavendish Laboratory, Cambridge CB3 0HE；现地址 GEC-Marconi Electronics, Chelmsford） |
| **Received** | 1977 June 23 |
| **Sumission** | Received ≈ published 1978 |
| **Series** | 本文是作者的系列三篇之 Part I（"I" 表系列首篇）。后续 Part II 为 MNRAS 182, 443–455（同期下两卷页码） |
| **状态** | 精读完成（视觉读取 PDF 全文 10 页） |

## 摘要（原文 Summary 翻译）

本文证明带电粒子可在天体激波前沿被加速到高能。快速粒子被它们**自身**激发向上游传播的 Alfvén 波散射阻挡，无法从激波逃离。这种散射把粒子束缚在激波附近，每次穿越激波都获得一阶 Fermi 加速，从而能量分布呈幂律，谱指数与银河宇宙线观测吻合。讨论仅限已相对论性粒子，从热能到相对论能的初始加速不在本文范围。

## 读完这张图能抓住什么（30 秒版本）

1. **问题**：第一次提出了一个**自洽**的激波加速机制——粒子被它们自己产生的波散射回激波，反复穿越获得能量。
2. **公式**：得出 $N(E) \propto E^{-\mu}$，其中 $\mu = \frac{2u_2+u_1}{u_1-u_2}$（强激波 $u_1/u_2 = 4$ → $\mu = 2$，考虑波速后 $\mu ≈ 2.5$）。
3. **地位**：与同月 Blandford & Ostriker 1978 共同构成「扩散激波加速（DSA）」概念的双源头；Blandford & Eichler 1987 综述中正式被命名为 DSA。

## 论文结构（4 节，10 页）

| 节 | 主题 | 页码 | 自身分章文件 |
|---|---|---|---|
| §1 | Introduction（背景、观测证据、平行激波假设、电子 vs 质子能量） | 147–148 | `01_introduction.md` |
| §2 | The energy spectrum（谱指数推导核心） | 148–152 | `02_energy_spectrum.md` |
| §3 | Alfvén waves upstream of the shock（波激发、阻尼、$E_{\rm crit}$） | 152–156 | `03_alfven_waves.md` |
| §4 | Application to SNR & conclusion | 156 | `04_application_snr.md` |

## 关键公式与物理（速查）

| 公式 | 含义 | 物理意义 |
|---|---|---|
| (1) | 扩散-对流方程 $\frac{\partial n}{\partial t} + u_2 \frac{\partial n}{\partial x} = \frac{\partial}{\partial x}\left(D(x)\frac{\partial n}{\partial x}\right)$ | 下游散射中心的密度演化 |
| (2) | 稳态解 $n(x,t) = A + B \exp\left[\int \frac{u_2}{D(x')}dx'\right]$ | 时间无关注入 |
| (3) | 逃逸概率 $\eta = 4u_2/v$ | 每次穿越激波从下游逃逸的概率 |
| (4) | 每次穿越能量增长 $E_{k+1} = E_k \left[\frac{1+v_{k1}(u_1-u_2)\cos\theta_{k1}/c^2}{1+v_{k2}(u_1-u_2)\cos\theta_{k2}/c^2}\right]$ | Lorentz 不变保持 |
| (5)-(7) | 多循环后 $\ln(E_l/E_0) = l \cdot \frac{4}{3}\frac{u_1-u_2}{c}$ | 平均对数增长 |
| (8) | $\ln P_l = l \ln(1-4u_2/c) = -\mu' \ln(E_l/E_0)$ | 循环 $l$ 次的概率 |
| (9) | $N(E)dE = \frac{\mu-1}{E_0}(E/E_0)^{-\mu}dE$ | **幂律谱**，谱指数 $\mu$ |
| (10) | $\mu = \frac{2u_2+u_1}{u_1-u_2}$ | 谱指数公式 |
| (11) | $u_1 = v_s - v_A,\ u_2 = v_s/\chi$ | 含 Alfvén 波速修正 |

## 谱指数的关键数值

| 情形 | $\chi$（压缩比） | $v_w$（波速） | $\mu$ | 物理 |
|---|---|---|---|---|
| 强激波 limit | 4 | $v_w \ll v_s$ | 2 | 理论上限（test-particle） |
| 强激波 + 波速修正 | 4 | $v_w = v_s/12$ | 2.5 | 与宇宙线谱匹配 |
| 地球弓激波（观测验证） | 3 | 0 | 2.5 | 实地测得 |

## 引用分析与历史定位

**前驱**：本文依赖 Wentzel 1974（Alfvén 波激发）、Jokipii 1966、Fisk 1971（地球弓激波类比）、Greenstadt 1975（直接观测）、Formisano 1974（地球弓激波数据）。

**同期独立**：Blandford & Ostriker 1978（同月 ApJ 221, L29）——同一机制独立提出。

**后续奠基**：
- Blandford & Eichler 1987（Phys. Reports 154, 1）——正式命名 "diffusive shock acceleration (DSA)"
- Bell 1978b, 1978c（MNRAS 182 续篇）——非线效应、激波修正
- Bell 2004（"Bell instability"）——解决了自洽散射波激发的理论缺口

**现代应用**：
- Blasi 2013 综述（A&ARv 21, 70）——把本文作为 NLDSA 出发点
- Amato 2014 综述（Int. J. Mod. Phys. D 23, 1430013）——讨论本文的 test-particle 局限与非线性扩展

## 批判性观点（详见各分章）

- **优点**：第一性原理推导、无唯参数、物理清晰、自洽求解
- **局限**：
  1. test-particle 极限（未考虑 CR 对激波结构的反馈）
  2. 散射波来源被假设存在（直到 Bell 2004 解决 Bell instability）
  3. 初始加速（热能→相对论）不在本文范围
  4. 扩散系数依赖波振幅 $\mathcal{F}$，无法自洽决定加速时间尺度
  5. 平行激波假设简化（1980s 后扩展到斜激波）