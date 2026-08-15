# 2. The bases of the SNR paradigm

> 本章属于：The Origin of Galactic Cosmic Rays（Blasi, 2013, arXiv:1311.7346）
>
> 上一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/01_introduction.md|01_introduction.md]]
>
> 下一章：[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/03_test_particle_dsa.md|03_test_particle_dsa.md]]

## 2.1 本节核心内容

- 用 B/C 比例推得银河系 CR 逃逸时间 $\tau_{\rm esc}$(E)，导出扩散系数 D(E) 与能量（刚度）的依赖。
- 由 SN 率 R_SN、单次 SN 能量 E_SN、源处注入谱，反推出在地球处测到的质子能谱，进而求得所需的总加速效率 $\xi_{\rm CR}$。
- 结论：$\xi_{\rm CR}$ ≈ $2.5\times10^{-3}$ 仅计质子；含重核后 $\xi_{\rm CR}$ ≈ 5–10%，与 10% 的"10% 定律"吻合。

## 2.2 原文内容（要点摘录）

- [FACT] "the ratio of boron and carbon fluxes is related to the grammage traversed by CRs, X(E) = n̄·$\mu$·v·$\tau_{\rm esc}$(E)。"
- [FACT] "For particles with energy per nucleon of 10 GeV/n the measured B/C corresponds to X ~ 1 g cm$^{-2}$."
- [FACT] "$\tau$* ~ 90 · (H/3 kpc) Myr" (Eq. 1) — 比弹道时间大三至四个量级，"the strongest evidence so far for diffusive motion of CRs in the Galaxy."
- [FACT] D(E) = $3\times10^{28}$ (H/3 kpc) cm$^{2}$/s 在 10 GeV。
- [FACT] 高刚度 B/C 数据与 X(R) ∝ R$^{-}$$\delta$ 一致，$\delta$ = 0.3–0.6。
- [FACT] 单次 SN 动能 E_SN = $10^{51}$·$E_{51}$ erg。
- [FACT] 注入谱形式 N(p) = $\xi_{\rm CR}$·E_SN / m$^{2}$ · I($\gamma$) · (p/m)$^{-}$ᵞ，其中 I($\gamma$) ≈ 2(3−$\gamma$)($\gamma$−2)/(4−$\gamma$)。
- [FACT] 地球处质子通量：J(E) = (c/4$\pi$) · N(E)·R_SN / ($\pi$ R_d$^{2}$·(2H)) · $\tau_{\rm esc}$(E)$^{-1}$ = $8\times10^{5}$·$\xi_{\rm CR}$·I($\gamma$) · (R_SN/30 yr$^{-1}$) · (E/m)$^{-}$ᵞ$^{-}$ᵟ · (E*/m)ᵟ m$^{-2}$s$^{-1}$sr$^{-1}{\rm Ge}$V$^{-1}$（Eq. 2）
- [FACT] 归一化到 10 GeV 通量后得到 $\xi_{\rm CR}$ ≈ $2.5\times10^{-3}$ · I($\gamma$)$^{-1}$ · (E*/m)ᵞ$^{-2}$ · (R_SN/30 yr$^{-1}$)$^{-1}$（Eq. 3）。
- [FACT] "$\xi_{\rm CR}$ ≃ 2–3% ... the total CR acceleration efficiency is somewhat higher than the estimate in Eq. 3 ... between 5% and 10% for the bulk of SNRs."

## 2.3 关键公式

**Eq. 1**（逃逸时间）
$$\tau^* = \frac{X(E^*)}{\bar n \mu c} = 90 \left(\frac{H}{3 \text{kpc}}\right) \text{Myr}$$

其中 X~1 g/cm$^{2}$、$\mu$ ≈ 1.4 m_p、n̄ = n_disc·h/H = $5\times10^{-2}$ · (n_disc/1 cm$^{-3}$)·(H/3 kpc)$^{-1}$ cm$^{-3}$。

**Eq. 2**（地球处 CR 质子谱）
$$J(E) = \frac{c}{4\pi}\frac{N(E) R_{\text{SN}}}{\pi R_d^2 \cdot 2H \cdot \tau_{\text{esc}}(E)} = 8 \times 10^5 \xi_{\text{CR}} I(\gamma) \left(\frac{R_{\text{SN}}}{30\,\text{yr}^{-1}}\right) \left(\frac{E}{m}\right)^{-\gamma-\delta}\left(\frac{E^*}{m}\right)^{\delta} \,\text{m}^{-2}\,\text{s}^{-1}\,\text{sr}^{-1}\,\text{GeV}^{-1}$$

**Eq. 3**（所需 CR 加速效率）
$$\xi_{\text{CR}} \approx 2.5 \times 10^{-3} \frac{1}{I(\gamma)} \left(\frac{E^*}{m}\right)^{\gamma-2}\left(\frac{R_{\text{SN}}}{30\,\text{yr}^{-1}}\right)^{-1}$$

**Eq. 5–6**（ISM 声速、Mach 数 — 出现在 §3，但属本节基础）
$$c_s = \sqrt{\gamma_g kT/m_p} \approx 11 \left(\frac{T}{10^4 \text{K}}\right)^{1/2} \text{km/s}$$
$$\mathcal{M}_s = V_{\text{ej}}/c_s \approx 900 E_{51}^{1/2} M_{\text{ej},\odot}^{-1/2} (T/10^4\text{K})^{-1/2}$$

## 2.4 关键参数

| 参数 | 数值 |
|------|------|
| X(10 GeV/n) | ~1 g/cm$^{2}$ |
| n_disc | ~1 cm$^{-3}$（标准） |
| h（盘面半厚度） | 150 pc |
| H（晕厚度） | ~3 kpc |
| $\mu$ | ~1.4 m_p |
| $\tau_{\rm esc}$(10 GeV) | ~90 (H/3 kpc) Myr |
| D(E=10 GeV) | $~3\times10^{28}$ (H/3 kpc) cm$^{2}$/s |
| R_SN | ~30 yr$^{-1}$ |
| E_SN | $10^{51}$ erg |
| R_d（盘面半径） | 10 kpc |
| $\xi_{\rm CR}$（仅质子） | 2–3% |
| $\xi_{\rm CR}$（含重核） | 5–10% |

## 2.5 图表分析

参见 `09_figures_tables.md`（Figure 2 B/C ratio、Figure 3 Proton spectrum）。

## 2.6 作者的逻辑

- **链路**：B/C ratio（观测）→ $\tau_{\rm esc}$（传播）→ D(E) 与 $\delta$ → 用 SN 率 + 注入谱反演 $\xi_{\rm CR}$。
- [INTERPRETATION] 作者用一条完整的能量预算推导说明 SNR 在**能量上**足以支持作为 CR 主源——这构成 SNR 范式的第一根支柱（"能量学论证"）。
- [INTERPRETATION] 这里刻意把 $\xi_{\rm CR}$ 与注入谱斜率 $\gamma$ 分离，因为下一节（§3）就要讨论 $\gamma$ 的具体预测。

## 2.7 我的理解

- [FACT] 作者用 "escape time normalized to B/C at E* makes J(E) independent of H" 强调了一个**重要的不敏感性**：简单扩散模型里 CR 通量和 grammage 都按 H/D(E) 标度，因此 halo 大小可以被消去。
- [INTERPRETATION] $\xi_{\rm CR}$ ≈ 10% 的"10% 定律"是 SNR 范式的**能量锚点**，但并非直接观测——它是推导值，受 SN 率、源分布、传播模型影响。

## 2.8 潜在问题与值得关注的地方

- [CRITIQUE] $\delta$ = 0.3–0.6 范围过宽，源自 B/C 在高能段的斜率不确定。作者在此未展开，但对后续 §6.2 的**各向异性论证**（需要 $\delta$ ≈ 0.7 才能匹配 NLDSA 硬谱）有直接影响。
- [CRITIQUE] 银河系 SN 率 R_SN = 30 yr$^{-1}$ 存在系统性不确定性（±30%），直接影响 $\xi_{\rm CR}$ 反演。
- **信息缺失**：作者未讨论源分布的径向依赖（如内盘密度高）对 $\xi_{\rm CR}$ 估算的影响。