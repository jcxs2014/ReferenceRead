---
title: "97. Quality Check — Gabici 2019"
---

## Completeness Check

| 要求 | 状态 | 说明 |
|------|------|------|
| 所有章节覆盖 | ✅ | §1 Introduction, §2 Orthodoxy (2.1-2.5), §3 Observations (3.1-3.3.5), §4 Open Problems (4.1-4.3), §5 Conclusions |
| 所有图表覆盖 | ✅ | Fig 1 (PAMELA/AMS02 CR flux H-O), Fig 2 (p/e-/e+ spectra), Fig 3 (dipole anisotropy), Fig 4 (angular power spectrum), Fig 5 (hadronic CR spectral index vs R), Fig 6 (emissivity vs R) |
| 所有公式覆盖 | ✅ | 公式 (1) D₀, 公式 (2) dipole, 公式 (3) Emax Hillas |
| 所有数值覆盖 | ✅ | 见下 |
| 与 00_overview 无逐字重复 | ✅ | 00 为元数据 + 一句总览 |

## 关键数值校验

- 局部 CR 能量密度 $w_{\rm CR} \approx 1$ eV/cm³ ✅
- CR 总能量 $W_{\rm CR} \approx 10^{55}$ erg ✅
- 所需注入功率 $P_{\rm CR} \approx 10^{41}$ erg/s ✅
- SN 动能注入率 $\sim 10^{42}$ erg/s → 需 $\sim 10\%$ 效率 ✅
- CR 谱指数 $\alpha \approx 2.7$（多 GeV 至数 PeV）✅
- B/C 推出 grammage $\Lambda \approx 10$ g/cm² ✅
- ¹⁰Be 半衰期 $\sim 1.4$ Myr ✅
- 银河驻留时间 $\tau_{\rm esc} \approx 10$–$20$ Myr ✅
- 盘内驻留时间 $\tau_{\rm esc,disk} \approx$ few Myr ✅
- 扩散系数 $D_0 \approx 3 \times 10^{28}$ cm²/s, $\delta \approx 0.3$–$0.6$ ✅
- 偶极各向异性 $\sim 10^{-4}$（几十 TeV）✅
- H/He 谱斜率差 $\Delta\alpha \approx 0.1$ ✅
- 硬变刚度 $\sim 300$ GV, $\Delta\alpha \approx 0.13$ ✅
- streaming instability 增长率=非线性阻尼率在 $R \approx 200$–$300$ GV ✅
- $e^-+e^+$ 断点 $E_b = (53 \pm 8)$ GeV (Fermi-LAT) ✅
- $e^-$ 谱 1 TeV 处变陡 $\alpha = -3.04 \to -3.78$ (H.E.S.S.) ✅
- 20 TeV $e^-$ 源距离 $\lesssim 100$ pc ✅
- $e^+$ 分数上升 $\sim 8$ GeV ✅
- $e^+$ 分数下降 $\sim 400$–$500$ GeV ✅
- AMS02 $e^+$ 至 1 TeV: $E_s = 810^{+310}_{-180}$ GeV ✅
- π⁰ 衰变峰 $E_\gamma = m_{\pi^0}/2 = 67.5$ MeV ✅
- Fermi-LAT Pass 8 极限 $\sim 100$ MeV ✅
- H.E.S.S. 银盘巡天 8 SNR（$35° < l < 65°$, $|b| < 3°$）✅
- GeV 超量 $\sim 3$ GeV 球对称 ✅
- Fermi 气泡 $\sim 10$ kpc 上下，$E^{-2}$ 谱（1–100 GeV）✅
- 发射度下降 20–40%（$R > 5$ kpc）✅
- 膝区 $\sim$ few PeV，$E^{-3}$ ✅
- 踝区 $\sim 3 \times 10^{18}$ eV ✅
- 第二膝 $\sim 10^{17}$ eV ✅
- Emax Hillas: $E_{\max} \approx Z (R_{\rm sh}/3 \; {\rm pc})(u_{\rm sh}/1000 \; {\rm km/s})(B_{\rm up}/\mu G)$ TeV ✅
- ¹⁰Be 当前仅测至 $\sim 1$ GeV/n ✅
- B/C 当前测至 1 TeV/n ✅
- HESS 银心 PeVatron（inner $\sim 10$ pc）✅
- 60Fe 半衰期 $\sim 2.6$ Myr ✅
- 22Ne 过量 $\sim 5\times$ ✅

## 分章内容独立性确认

| 分章 | 独有内容 |
|------|---------|
| 01 | 问题定义、论文结构、库内关联 |
| 02 | 三支柱详细论证（含 π 峰辨析） |
| 03 | 11 项观测异常（子节 3.1.1–3.3.5） |
| 04 | 三困难（膝区/踝区/化学组成）+ 60Fe |
| 05 | 6 经典问题 + 11 新谜题 + 10 未来观测 + 替代范式 |

## LaTeX 规范自检

- 公式：$...$ 包裹 ✅（$\sim$, $\lesssim$, $\Delta$, $\tau$, $\alpha$ 等均正确）
- 核素：¹⁰Be, ⁶⁰Fe, ²²Ne 保留 Unicode ✅
- 单位：erg/s, cm³, Myr, GV, TeV 直接书写 ✅
- 无"需人工确认""待补充"占位符 ✅