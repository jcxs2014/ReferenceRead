---
title: "§5 Background and Systematics"
paper: "lhaaso-2021"
section: 5
nav_prev: "04_comparison_with_theory.md"
nav_next: "06_statistical_significance.md"
---
上一章：`04_comparison_with_theory.md` — §4
下一章：`06_statistical_significance.md` — Background and Systematics

# §05. Background and Systematics — 背景估计与系统误差

>
>

---

## 5.1 背景估计方法

[FACT] **直接积分法（direct integration method）**：由 Fleysher et al. 2003 和 Bartoli et al. 2013 发展，专为地面阵列 γ 探测设计（原文 p.351–352, refs 22–23）。

[FACT] 步骤（原文 p.349–356）：
1. 天图以 0.1°×0.1° 网格填充重建到达方向的事件 → "event map"
2. 用直接积分法估计每格残存 CR 背景事件数 → "background map"
3. event map 减 background map → "source map"
4. 平滑以匹配 KM2A 角分辨率
5. 假设 0.3° 高斯内禀延展，似然比检验估计 γ 事件超额的显著性

[FACT] **蟹状星云作为标准烛光**（ref 8，Aharonian et al. 2021）：校验 KM2A 性能、角分辨率、能量分辨率，以及 PSF 估计（原文 p.31–32, p.391–397）。

---

## 5.2 能量分辨率与非高斯尾巴

[FACT] **能量分辨率**（>100 TeV，<35° 天顶角）：**优于 14%**（原文 p.337–340）。

[FACT] **能量分辨函数的非高斯效应**：Monte Carlo 检验（10 TeV–2.5 PeV 的 12 个 bin）显示非高斯效应极小；主要效应是"高能 true 事件落入低能 bin"（能量被低估），反之不明显（原文 p.270–290）。

[FACT] **bin purity**：~100 TeV 处约 67%（与 14% 能量分辨率匹配），邻近 bin 贡献 ~33%（原文 p.284–290）。

[FACT] **spillover 效应**（蟹状星云 SED + 截断 E_cut 检验）：主要发生在相邻 bin，下一相邻 bin 贡献极小；**E > 400 TeV 时，即使相邻 bin 也 <1%**（原文 p.291–308）。

---

## 5.3 缪子 veto 与 CR 抑制

[FACT] **N_μ/N_e < 1/230 判别**（原文 p.343–347）：将 γ-like 事件纯度提高至 background-free。

[FACT] **1.4 PeV 光子的缪子 veto**：对 J2032+4102 的最高能光子，测得 N_μ/N_e = **1/941**（原文 p.386–390）——"rejects almost all CR background"。

---

## 5.4 γ-γ 吸收（系统效应）

[FACT] **γ-γ 对产生**（γγ → e$^{+}$e$^{-}$）：>100 TeV 来自 CMB，<100 TeV 来自 ISRF（原文 p.364–378）。

[FACT] 峰值波长 λ ≈ 1·[E_γ/(1 TeV)]$^{-1}$ μm。用 Popescu et al. 2017 的 ISRF 模型 + Moskalenko, Porter, Strong 2006 的银河系 γ-γ 光深计算（原文 p.374–383, refs 29–30）。

[FACT] **影响**：对三主要源，即使最高能量处吸收效应也很小（原文 p.83–87）；对数抛物线拟合的"吸收修正版"（dotted curves，原文 Fig. 1）与未修正版几乎重合。

---

## 5.5 SED 重建系统误差

[FACT] **源内禀延展估计**：通过蟹状星云 PSF 宽度平方差扣除得到，分别为 (0.30±0.06)°、(0.58±0.04)°、(0.36±0.06)°（原文 p.391–404）。

[FACT] **SED bin 定义**：10 TeV 至 1 PeV 共 10 个 Δ(logE)=0.2 bin（原文 p.397–404）。

[FACT] **SED 拟合方法**：向前展开 + 最小 $\chi^{2}$；对数抛物线 vs 简单幂律用 AIC（Akaike Information Criterion）比较（原文 p.190–200）。

---

## 5.6 Fermi LAT 交叉验证

[FACT] **LHAASO J1908+0621 的 GeV 段**：用 Fermi LAT Pass 8 数据（2008-08-04 至 2020-01-17，**11 年**）；10°×10° ROI；30–250 GeV 分 4 个 log-spaced bin；4FGL 目录 + 0.5° 附加分量的模型（原文 p.385–390）。

[FACT] 结果：在强子场景，若电子注入随 PSR J1907+0602 自转历史演化，α=1.75 幂律 + E=0.8 PeV 超指数截断可拟合 GeV–TeV 数据；$\pi^{0}$ 强子模型需复杂质子谱（broken PL + 指数截断）——轻子 vs 强子尚未唯一确定（原文 p.110–116, p.390）。

---

## 5.7 主要系统不确定

1. **源延展估计**的 PSF 依赖（用蟹状星云，假设 PSF 与源相同）
2. **能量分辨率非高斯尾巴**（1.4 PeV 光子通过 10,000 模拟事件验证，±10% 粒子总数 + ±2σ ED 数）
3. **γ-γ 吸收模型**（Popescu 2017 ISRF 模型的不确定性）
4. **轻子 vs 强子机制简并**（如 J1908+0621）
5. **源内 counterpart 多重候选**（Extended Data Table 2）
