---
title: "4. Methods — X 射线数据处理与理论建模"
paper: "Giuffrida et al. 2022, SN 1006 as a Galactic particle accelerator"
outline_ref: "§4 Methods"
original_sections: ["§4.1 X-ray data analysis (Chandra)", "§4.2 X-ray data analysis (XMM-Newton)", "§4.3 Modeling the shock modification"]
---

> 上一章：`03_discussion.md`
> 下一章：`97_quality_check.md`

## 4.1 [FACT] Chandra 数据处理

- **软件**：CIAO 4.12 + CALDB 4.9.0
- **mosaicking**：CIAO `merge_obs`，vignetting 修正
- **能段**：0.5–1 keV（热发射，绿）；2.5–7 keV（非热发射，浅蓝）
- **光谱提取**：`specextract`，背景来自 SNR 外无点源区域（同 chip）
- **分箱**：optimal binning（Kaastra & Bleeker 2016）；cross-check 用 25 counts/bin
- **拟合**：XSPEC 12.10.1f，$\chi^2$ 统计，0.5–5 keV

## 4.2 [FACT] 热 ISM 与同步辐射建模

**热 ISM**：XSPEC `NEI` 模型（非平衡电离等温等离子体），AtomDB 3.0.9

- 单电离参数 $\zeta$
- $kT$ 在所有区域固定为区域 0 的最佳拟合值 $1.35$ keV
- $N_H$ 固定为 $7 \times 10^{20}$ cm$^{-2}$

**同步辐射**（区域 +2, +3, +4, +5）：

- 损失主导电子谱（Zirakashvili & Aharonian 2010）——特别适合 SN 1006
- 交叉验证：指数截断幂律（XSPEC/SRCUT）结果一致
- 归一化和截断能量自由变化

**F-test**：热区（区域 0, -1, -2, -3, +1）添加非热成分**不显著改善拟合**（归一化 $< 99\%$ CL 与 0 一致）。

## 4.3 [FACT] 体积计算

投影区域到 $0''.2 \times 0''.2$ 像素网格（@ 2.2 kpc $\approx 6.3 \times 10^{15}$ cm），对每像素沿视线计算球壳弦长作为深度，求和：

$$V = \sum_{\rm pixels} A_{\rm pix} \times \ell_{\rm chord}$$

激波前球半径在区域内略有变化（$R_{\min} = 14''.40$ 在区域 +5 到 $R_{\max} = 14''.550$ 在区域 0），但使用统一中心。

**精度验证**：对规则区域，数值法 vs 解析法差异 $< 0.4\%$。

**PSF 泄漏修正**：XMM-Newton EPIC 的 FWHM $\sim 6''$ 导致约 7% ISM 发射泄漏到区域外，已按均匀分布修正。

## 4.4 [FACT] XMM-Newton 数据处理

- **软件**：SAS V18.0.0
- **事件筛选**：ESPFILT 去除软质子，MOS PATTERN $\le 12$，pn PATTERN $\le 4$，FLAG = 0
- **净曝光**：MOS1 89 ks, MOS2 94 ks, pn 51 ks
- **提取**：区域 3 和区域 4-5（合并）
- **拟合**：MOS 和 pn 同时拟合，$\chi^2$ 统计，0.5–5 keV

## 4.5 [FACT] 激波修改建模（公式 1）

**基本框架**（Caprioli et al. 2018, 2020; Haggerty & Caprioli 2020）：

$$r_t = f(\xi_c, \xi_B, \theta_{Bn})$$

其中 $\xi_c$ 和 $\xi_B$ 是 CR 压和磁场压相对上游 ram 压的归一化比例。

**角度依赖模型**（三成分：热注入 $p$、种子再加速 $\xi_s$、磁场放大 $\xi_B$），原文公式 1 为平滑阶跃函数（arctan 形式）：

$$\xi_i(\theta_{Bn}) = \xi_i^{(0)} \left[\frac{1}{2} - \frac{1}{\pi} \arctan\left(\frac{\theta_{Bn} - \theta_i}{\Delta_i}\right)\right]$$

参数：

| 成分 | $\xi^{(0)}$ | $\theta_i$（截断中心） | $\Delta_i$（截断宽度） |
|------|-------------|------------------------|------------------------|
| 热注入 $p$ | $12\%$ | $45°$ | $20°$ |
| 再加速 $\xi_s$ | $6\%$ | $70°$ | $20°$ |
| 磁场 $\xi_B$ | $5\%$ | $70°$ | $20°$ |

**总效率**：$\xi_{\rm tot} = p + \xi_s = 18\%$（加上 He 核加速后合理）。

## 4.6 [FACT] Table 3 — XMM-Newton 先前结果更新

先前东南 limb 的 8 个区域密度更新（Miceli et al. 2012 → 本文）：

| 区域 | $\theta$ 范围 | 更新后 $n_{ISM}$ (cm$^{-3}$) |
|------|-------------|-------------------------------|
| a | $53°$–$63°$ | — |
| b | $58°$–$73°$ | $0.206 \pm 0.13$ |
| c | $65°$–$80°$ | $0.197 \pm 0.08$ |
| d | $73°$–$88°$ | $0.189 \pm 0.07$ |
| e | $80°$–$96°$ | $0.169 \pm 0.08$ |
| f | $88°$–$103°$ | $0.150 \pm 0.06$ |
| g | $96°$–$112°$ | $0.152 \pm 0.08$ |
| h | $104°$–$120°$ | $0.199 \pm 0.11$ |

**更新后确认**：东南 limb 密度在 $\theta \approx 90°$ 有极小值，向两侧升高——与新的 Chandra + 东北 limb 数据一致。

## 4.7 [INTERPRETATION] 方法学评价

本文方法学的**关键突破**在于 Chandra + XMM-Newton 的互补性利用：

- **Chandra 空间分辨率**：排除抛射物污染，这是 Miceli 2012 无法做到的
- **XMM-Newton 光谱灵敏度**：提供精确的 $n_{ISM}$ 估计，覆盖 Chandra 无法覆盖的准平行区

这种"高空间分辨率 + 高光谱灵敏度"的组合策略，为后续类似研究（如 Tycho、Cas A 的 X 射线激波修改分析）提供了可复用的方法论模板。