---
title: "97. Quality Check — Gabici et al. 2019"
---

## Completeness Check

| 要求 | 状态 | 说明 |
|------|------|------|
| 所有分章覆盖 | ✅ | 01–05 + 97/98/99 共 8 个分章 |
| 原文结构镜像 | ✅ | 5 章（§1–§5），与原文标题一一对应 |
| 所有公式覆盖 | ✅ | 见下 |
| 所有数值覆盖 | ✅ | 见下 |
| 所有图表覆盖 | ✅ | Fig 1–6 均有描述 |
| 无占位符 | ✅ | 无"需人工确认""待补充" |
| LaTeX 规范 | ✅ | 数学表达式 `$...$` 包裹，核素/单位 Unicode 保留 |
| 与 00_overview 无逐字重复 | ✅ | 00 为骨架总览，分章各章独立 |

## 关键数值校验

| 数值 | 分章位置 | 原文验证 |
|------|---------|---------|
| $w_{\rm CR} \approx 1$ eV/cm³ | 02_orthodoxy §2.1 | ✅ fulltext.txt 行 124 |
| $W_{\rm CR} \approx 10^{55}$ erg | 02_orthodoxy §2.1 | ✅ 行 186 |
| $P_{\rm CR} \approx 10^{41}$ erg/s | 02_orthodoxy §2.1 | ✅ 行 248 |
| grammage $\Lambda \approx 10$ g/cm² | 02_orthodoxy §2.2 | ✅ 行 241 |
| $\tau_{\rm esc} \approx 10$–$20$ Myr | 02_orthodoxy §2.2 | ✅ 行 307 |
| $D_0 \approx 3\times10^{28}$ cm²/s | 02_orthodoxy §2.2 公式(1) | ✅ 行 328 |
| $\delta \approx 0.3$–$0.6$ | 02_orthodoxy §2.2 | ✅ 行 349 |
| $\sim 10\%$ SN→CR 效率 | 02_orthodoxy §2.1 | ✅ 行 279 |
| 300 GV 硬变 | 03_observations §3.1.1 | ✅ 行 552 |
| $\Delta\alpha \approx 0.13$ | 03_observations §3.1.1 | ✅ 行 551 |
| H 比 He 谱软 $\Delta\alpha \approx 0.1$ | 03_observations §3.1.1 | ✅ 行 549 |
| $E^-$ 1 TeV 断点 $\alpha = -3.04 \to -3.78$ | 03_observations §3.1.3 | ✅ 行 846–847 |
| 20 TeV 电子 $<100$ pc 源 | 03_observations §3.1.3 | ✅ 行 853 |
| $e^+$ 分数 $>8$ GeV 上升 | 03_observations §3.1.4 | ✅ 行 884 |
| $e^+$ 分数 $>400$–$500$ GeV 下降 | 03_observations §3.1.4 | ✅ 行 900 |
| $e^+$ 至 1 TeV, $E_s = 810^{+310}_{-180}$ GeV | 03_observations §3.1.5 | ✅ 行 1091–1093 |
| $\pi^0$ 峰 $E_\gamma = m_{\pi^0}/2 = 67.5$ MeV | 02_orthodoxy §2.5 | ✅ 行 486 |
| Fermi 气泡 $\sim 10$ kpc, $E^{-2}$ | 03_observations §3.3.4 | ✅ 行 1549–1555 |
| 发射度 $R>5$ kpc 下降 20–40% | 03_observations §3.3.3 | ✅ 行 1467 |
| 膝区 few PeV, $E^{-3}$ | 04_open_problems §4.1 | ✅ 行 1649 |
| 踝区 $\sim 3\times10^{18}$ eV | 04_open_problems §4.2 | ✅ 行 1748 |
| 第二膝 $\sim 10^{17}$ eV | 04_open_problems §4.2 | ✅ 行 1779 |
| Hillas 公式 $E_{\max} \approx Z R_{\rm sh} u_{\rm sh} B_{\rm up}$ TeV | 04_open_problems §4.1 | ✅ 行 1672–1673 |
| $^{10}$Be 半衰期 $\sim 1.4$ Myr | 02_orthodoxy §2.2 | ✅ 行 301 |
| $^{60}$Fe 半衰期 $\sim 2.6$ Myr | 04_open_problems §4.3 | ✅ 行 1896 |
| $^{22}$Ne 过量 $\sim 5\times$ | 04_open_problems §4.3 | ✅ 行 1888 |
| DR 占 GeV CR 能量 30–50% | 03_observations §3.1.2 | ✅ 行 758–760 |
| streaming = 非线性阻尼 在 200–300 GV | 03_observations §3.1.1 | ✅ 行 723–725 |
| 局域 CR 质子谱比 AMS-02 高 1.4$\pm$0.5 倍 | 03_observations §3.3.5 | ✅ 行 1606 |
| SN 率 $\sim 3$/世纪 | 02_orthodoxy §2.1 | ✅ 行 276 |
| 银河系 SN 总注入率 $\sim 10^{42}$ erg/s | 02_orthodoxy §2.1 | ✅ 行 278 |

## 公式校验

| 公式 | 位置 | LaTeX 规范 |
|------|------|-----------|
| (1) $D_0 \approx 3\times10^{28}(\dots)^2(\dots)^{-1}$ cm²/s | 02_orthodoxy §2.2 | ✅ |
| (2) $\alpha = (3D_{\rm parallel}/c) \|\nabla n_{\rm CR}\|/n_{\rm CR}$ | 03_observations §3.2 | ✅ |
| (3) $E_{\max} \approx Z(R_{\rm sh}/3\;{\rm pc})(u_{\rm sh}/1000\;{\rm km/s})(B_{\rm up}/\mu G)$ TeV | 04_open_problems §4.1 | ✅ |

## 分章内容独立性

| 分章 | 独有内容 | 与 00_overview 重复度 |
|------|---------|---------------------|
| 01_introduction | 论文结构（5 章）、作者机构（法国/意大利）、核心问题定义 | 无重复 |
| 02_orthodoxy | 三支柱（2.1–2.3）+ γ 射线测试（2.4–2.5）+ pion bump 辨析 | 无重复 |
| 03_observations | 11 个异常子节（3.1.1–3.3.5）逐项展开 | 无重复 |
| 04_open_problems | 膝区定量三角困境、踝区、⁶⁰Fe 证据 | 无重复 |
| 05_conclusions | 6 经典问题 + 11 新谜题 + 10 未来观测 | 无重复 |