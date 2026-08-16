---
title: "§2 Key Measurements"
paper: "lhaaso-2021"
section: 2
nav_prev: "01_detector_and_method.md"
nav_next: "03_scientific_implications.md"
---
上一章：`01_detector_and_method.md` — §1
下一章：`03_scientific_implications.md` — Key Measurements

# §02. Key Measurements — 12 个 UHE γ 源与 1.4 PeV 光子

>
>

---

## 2.1 标志性结果陈述

[FACT] **原文摘要（原文 p.18–24）**："we report the detection of more than **530 photons at energies above 100 teraelectronvolts and up to 1.4 PeV from 12 ultrahigh-energy γ-ray sources** with a statistical significance greater than **seven standard deviations**."

[FACT] **12 个 UHE γ 源**：全部 ≥7σ 显著性（原文 p.29），其中两个源探测到 >0.8 PeV 光子，**最高能光子来自 LHAASO J2032+4102，能量 1.4 PeV**（原文 p.29–30）。

> **核查（对照原文 PDF）**：
> - 1.4 PeV 表述：原文 p.29–30 明写 "the energy of the most energetic photon detected by LHAASO J2032+4102 is 1.4 PeV"；Table 1 中 LHAASO J2032+4102 的 E_max = 1.42 ± 0.13 PeV（原文 p.75）——两项独立表述一致。
> - 12 个源表述：原文 p.18 与 p.29 两处均写 "12 ultrahigh-energy γ-ray sources"，Table 1 恰好列出 12 行源（原文 p.63–77）。

---

## 2.2 Table 1：UHE γ 射线源完整数据（原文 p.63–80）

| # | 源名 | RA (°) | dec. (°) | 显著性 (×σ) | E_max (PeV) | Flux @100 TeV (CU) |
|---|---|---|---|---|---|---|
| 1 | LHAASO J0534+2202 | 83.55 | 22.05 | 17.8 | 0.88 ± 0.11 | 1.00(0.14) |
| 2 | LHAASO J1825-1326 | 276.45 | −13.45 | 16.4 | 0.42 ± 0.16 | 3.57(0.52) |
| 3 | LHAASO J1839-0545 | 279.95 | −5.75 | 7.7 | 0.21 ± 0.05 | 0.70(0.18) |
| 4 | LHAASO J1843-0338 | 280.75 | −3.65 | 8.5 | 0.26$^{+0.16}_{-0.10}$ | 0.73(0.17) |
| 5 | LHAASO J1849-0003 | 282.35 | −0.05 | 10.4 | 0.35 ± 0.07 | 0.74(0.15) |
| 6 | LHAASO J1908+0621 | 287.05 | 6.35 | 17.2 | 0.44 ± 0.05 | 1.36(0.18) |
| 7 | LHAASO J1929+1745 | 292.25 | 17.75 | 7.4 | 0.71$^{+0.16}_{-0.07}$ | 0.38(0.09) |
| 8 | LHAASO J1956+2845 | 299.05 | 28.75 | 7.4 | 0.42 ± 0.03 | 0.41(0.09) |
| 9 | LHAASO J2018+3651 | 304.75 | 36.85 | 10.4 | 0.27 ± 0.02 | 0.50(0.10) |
| 10 | **LHAASO J2032+4102** | 308.05 | 41.05 | 10.5 | **1.42 ± 0.13** | 0.54(0.10) |
| 11 | LHAASO J2108+5157 | 317.15 | 51.95 | 8.3 | 0.43 ± 0.05 | 0.38(0.09) |
| 12 | LHAASO J2226+6057 | 336.75 | 60.95 | 13.6 | 0.57 ± 0.19 | 1.05(0.16) |

[FACT] 单位说明（原文 p.78–80）：1 CU = Crab 星云在 100 TeV 的流量 = **6.1 × 10$^{-17}$ photons TeV$^{-1}$ cm$^{-2}$ s$^{-1}$**。

---

## 2.3 三个最亮源的 SED 与形貌（原文 Fig. 1, p.45–200）

对 LHAASO J1825-1326、J1908+0621、J2226+6057 这三个 >1 CU（@100 TeV）的源给出 SED 分析。

[FACT] **谱型**：>100 TeV 以上三源谱陡，简单幂律指数 Γ ≈ 3；但 10–500 TeV 段存在"渐变陡化"（gradual steepening），用对数抛物线 **dN/dE ∝ E$^{-\Gamma(E)}$** 拟合优于简单幂律（原文 p.51–56）。

[FACT] **对数抛物线拟合结果**（原文 Fig. 1 caption, p.190–200）：
- LHAASO J2226+6057：a=1.56, b=0.88, 幂律 Γ=3.01；AIC(LOG)=11.6, AIC(PL)=15.1
- LHAASO J1908+0621：a=2.27, b=0.46, 幂律 Γ=2.89；AIC(LOG)=24.4, AIC(PL)=30.1
- LHAASO J1825-1326：a=0.92, b=1.19, 幂律 Γ=3.36；AIC(LOG)=12.3, AIC(PL)=14.8（另一处写 AIC(PL)=14.8）

[FACT] **γ-γ 吸收**：三源即使最高能量处，对 CMB/ISRF 的 γ-γ 吸收效应也很小（原文 p.83–87）——证实 LHAASO 观测到的谱形主要是源内禀。

[FACT] **延展形貌**：三源 2D γ 辐射图像延展至少 1°（原文 p.95–97），意味着 γ 发射体占据银河系内 ≥10$^{4}$ pc$^{3}$ 的巨大区域。

[FACT] **PSF 大小**（68% containment）：J2226+6057 = 0.49°，J1908+0621 = 0.45°，J1825-1326 = 0.62°（原文 p.198–200）。

---

## 2.4 12 个源的空间分布

[FACT] **全部位于银河平面**（原文 p.36–37）。

[FACT] **100 TeV 处流量**：0.4 – 4 CU（原文 p.38–39）。

[FACT] **尺度-光度估计**（原文 p.40–43）：线性大小 l = 17.5 θ d (pc)，100 TeV 光度 L ≈ 10$^{32}$ (d/kpc)$^{2}$ × CU (erg s$^{-1}$)，θ ≈ 1°。

---

## 2.5 蟹状星云：唯一"已确认"源

[FACT] **LHAASO J2108+5157 = 蟹状星云**，能谱延伸至近 1 PeV，是"无模型依赖"的**蟹状星云作为电子 PeVatron** 的首个证据（原文 p.31–34）。

[FACT] 蟹状星云特点：自转能量损失功率 \$dot{L}_0$ ≈ **5 × 10$^{38}$ erg s$^{-1}$**，磁场 B ≈ **100 μG**，尺寸几 pc（原文 p.121–124）——与其他 PWN 相比极端。

---

## 2.6 主要潜在 counterparts

[FACT] 12 个源邻近区域内存在多种潜在 counterpart（原文 p.101–109, Extended Data Table 2）：脉冲星与脉冲星风星云（PWN）、超新星遗迹（SNR）、年轻大质量星团、H II 区。

[FACT] **LHAASO J2032+4102 ↔ 天鹅座 Cocoon ↔ Cygnus OB2**：位置重合，有 >1 PeV 光子；γ 图像不指向 OB2 亮区，排除纯轻子（逆康普顿）起源；被作为"大质量恒星作为强子 PeVatron"的证据（原文 p.157–167）。

[FACT] **LHAASO J1908+0621 ↔ PSR J1907+0602 + SNR G40.5-0.5**：PSR 自转能量损失功率仅蟹状星云的极小部分，星云磁场 <10 μG；轻子模型需电子加速到 1 PeV 并穿越数十 pc，困难；质子-环境气体 $\pi^{0}$ 衰变模型可拟合但需复杂质子谱（原文 p.110–147）。
