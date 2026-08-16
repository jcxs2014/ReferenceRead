---
title: "§1 INTRODUCTION"
paper: "Caprioli & Spitkovsky 2014, ApJ 783, 91"
outline_ref: "§1 INTRODUCTION"
---
> 上一章：[[02_cosmic-ray-origins/0016_caprioli-2014/literature_analysis/00_overview.md|00_overview]]
> 下一章：[[02_cosmic-ray-origins/0016_caprioli-2014/literature_analysis/02_diffusive_shock_acceleration.md|02_diffusive_shock_acceleration]]

#### 1.1 [FACT] CR 起源的长历史

- **[FACT]** Baade & Zwicky (1934) 首先提议 **SNR 是宇宙线的加速源**，要求 SN 抛射动能的 $10\%-30\%$ 注入加速粒子。
- **[FACT]** 该能量学论证与 Fermi (1949, 1954) 加速机制结合，构成 70 年代末发展的 **扩散激波加速（DSA）** 理论基础：**Krymskii 1977; Axford et al. 1977; Bell 1978a, 1978b; Blandford & Ostriker 1978**。
- **[FACT]** DSA 最关键特征：粒子谱是**幂律**，谱指数仅依赖激波压缩比 $r$；对强激波 $r \to 4$，谱 $\propto p^{-q}$，$q = 3r/(r-1) \to 4$。
- **[FACT]** 银河 CR 谱观测（地球）：$E^{-2.7}$，从 GeV 到 $10^6$ GeV（质子），重核额外 $\times Z$。
- **[FACT]** 观测谱（$E^{-2.7}$）vs 源端预言（$E^{-2}$ 相对论极限）的差异由 **CR 传播（驻留时间随能量减小）+ 微分逃逸** 解释（Ptuskin & Zirakashvili 2005; Caprioli et al. 2011）。

#### 1.2 [FACT] SNR 加速的观测证据

- **[FACT]** SNR 无线电观测表明电子能量分布（1–10 GeV）与 DSA 预言一致（Trushkin 1998）。
- **[FACT]** SNR 的 $\gamma$ 射线常被解释为**强子起源**（Caprioli 2011; Ackermann et al. 2013），暗示核加速在 SNR 前向激波有效（如 Tycho 约 10%；Morlino & Caprioli 2012）。
- **[FACT]** 粒子加速理解受限于：CR 输运方程（数值 Berezhko & Völk 1997, 2004; Kang & Jones 1997, 2006; Kang et al. 2002; Zirakashvili & Aharonian 2010；解析 Malkov 1997; Blasi 2002; Amato & Blasi 2006; Caprioli et al. 2010a; Caprioli 2012）——但需要散射、注入、湍流激发的唯象输入。

#### 1.3 [FACT] 动力学模拟方法

- **[FACT]** 完整 PIC：Amano & Hoshino 2007, 2010; Riquelme & Spitkovsky 2011; Niemiec et al. 2012。
- **[FACT]** Hybrid（离子动力学 + 电子流体）：Winske 1985; Quest 1988; Giacalone et al. 1993; Bennett & Ellison 1995; Winske & Omidi 1996; Giacalone et al. 1997; Giacalone & Ellison 2000; Giacalone 2004; Lipatov 2002; Gargaté & Spitkovsky 2012; Guo & Giacalone 2013。
- **[FACT]** Vlasov–Fokker–Planck：Bell et al. 2013（不含自洽注入，但适合大尺度）。

#### 1.4 [FACT] 本文目标与改进

- **[FACT]** 用 hybrid 模拟检验 DSA 加速的离子谱，并调查加速与磁场放大有效的条件。
- **[FACT]** Hybrid 相比 PIC：不解析电子等离子体尺度，允许更大宏观系统，同时保留离子主导的激波动力学。
- **[FACT]** 相比 GS12 (Gargaté & Spitkovsky 2012) 的改进：
  - 大得多的计算盒、更长时间演化
  - 更大参数空间（激波强度 + 倾角）
  - 2D 与 3D 交叉验证
  - 长时间分辨率敏感性研究
  - 首次获得跨越 ~3 个能量量级的 $p^{-4}$ 幂律尾
  - **首次证据：CR 修正激波**（上游 precursor + 标准跃迁条件改变）

## 本节核心内容

介绍 CR 起源问题历史背景、DSA 理论基础、观测支持、各类模拟方法（PIC/hybrid/VFP）及其局限，并明确本文目标与对 GS12 的改进。

## 关键公式

- **[FACT]** DSA 谱指数：$q = 3r/(r-1)$；强激波 $r \to 4 \Rightarrow q \to 4$
- **[FACT]** 银河 CR 谱：$\propto E^{-2.7}$（观测）vs $E^{-2}$（源端相对论极限）
- **[FACT]** SNR 加速效率约束：$10\%-30\%$（Baade & Zwicky 1934 能量学要求）

## 我的理解 / Interpretation

本章建立整个工作的**问题框架**：为何需要 PIC/hybrid（传统方法依赖唯象输入，缺乏自洽），以及为何本文参数空间与时长是关键突破——不是新物理，而是**首次数值验证**。
