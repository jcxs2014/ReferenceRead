> 上一章：[[00_overview]]
> 下一章：[[02_numerical_model]]
---
title: "§1 Introduction — Giacalone 2017"
section: '1. INTRODUCTION'
---

## 1.1 研究动机：DSA 的几何盲区

**[FACT]** 经典 DSA（Diffusive Shock Acceleration）理论（Axford 1977; Bell 1978; Blandford & Ostriker 1978; Blandford & Eichler 1987）假定**平面平行激波**——激波法向与均匀磁场平行，扩散系数各向同性，粒子谱简化为幂律 $p^{-r/(r-1)}$（强激波 $r=4$ 时 $p^{-4}$）。

**[FACT]** 但天体物理激波（SNR、CME、TS）**从来不是平面平行**：
- 激波是**弯曲的**（球面或椭球面），法向 $\hat{n}$ 沿表面随位置变化
- 背景磁场存在**湍流**，局部分布 $\mathbf{B}(\mathbf{r},t)$ 起伏
- 因此**局部激波-磁场夹角** $\theta_{Bn}$ 沿激波面连续变化

**[FACT]** 由此，沿激波面：
- **准平行区**（$\theta_{Bn} \approx 0°$）：粒子易穿越激波来回扩散，加速效率高
- **准垂直区**（$\theta_{Bn} \approx 90°$）：粒子难以横向穿越磁场，注入曾被认为低效

**[FACT]** 但**注入阈值**（Equation 1）与 $\theta_{Bn}$ 的关系：
$$E_{\text{inj}} \sim \frac{E_R}{2\left(1 + \dfrac{\kappa_\parallel}{A^2\kappa_\perp}\right)}$$
- $\theta = 90°$ 时：$E_{\text{inj}} = E_R/2\left(1 + \dfrac{\kappa_\parallel}{A^2\kappa_\perp}\right)$
- $\theta = 0°$ 时：$E_{\text{inj}} = 9 E_R$
- 两者差别在 $\kappa_\parallel / \kappa_\perp$ 比值上——**在强湍流中此比值可很小**，使得准垂直注入效率接近准平行

## 1.2 弯曲激波与湍流尺度竞争

**[FACT]** 弯曲激波的两个几何效应：
1. **平均场效应**：$\theta_{Bn}$ 沿球面变化，粒子加速率沿激波变化（Decker 1990; McComas & Schwadron 2006; Schwadron 2008; Guo 2010; Kota 2010; Schwadron 2015）
2. **磁场线漂移（meandering）**：由最大尺度湍流主导，引起 $\theta_{Bn}$ 沿激波面涨落，导致加速"**patchy**"（不均匀），特征尺度 $\sim L_c$（湍流相干尺度）

**[FACT]** 关键参数 $L_c/R_{\text{sh}}$：
- **$L_c \sim R_{\text{sh}}$**：注入**非局地化**——粒子沿场线漂移跨越不同 $\theta_{Bn}$ 区，注入效率在准垂直与准平行区相近
- **$L_c \gg R_{\text{sh}}$**：注入**局地化**——由局部 $\theta_{Bn}$ 决定
- **$L_c \ll R_{\text{sh}}$**：近似平面（经典 DSA 适用）

## 1.3 本文目标

**[FACT]** 明确陈述："It is the purpose of this study to address the physics of particle acceleration at a spherical shock moving into a quasi-uniform plasma..."

**目标**：
- 数值处理**真实三维球状几何**（不忽略任何空间坐标——对比 Jokipii 1993; Giacalone 1994; Jones 1998 中的 ignorable-coordinate 假设）
- 正确纳入**跨场线传输**（field-line meandering + 局域场线漂移）
- 应用目标：**SNR** 粒子加速（galactic cosmic ray production）

## 1.4 关键数值

| 量 | 数值 |
|---|---|
| DSA 强激波谱指数 | $p^{-4}$ |
| 注入阈值（$\theta=0°$） | $9\,E_R$ |
| 注入阈值（$\theta=90°$） | $E_R / 2(1 + \kappa_\parallel/(A^2\kappa_\perp))$ |
| 平行强激波能量通量分配 | $\sim 20\%$ 到超热粒子（Giacalone et al. 1997） |

## 1.5 论文在库内脉络中的位置

**[INTERPRETATION]** 本文在**几何 DSA** 脉络中承上启下：
- **承 Bell 1978**：把平面 DSA 推广到球面几何
- **启 Caprioli 2014**：为 PIC 模拟的 $\theta$ 依赖性提供**解析/数值背景**（$\gamma(\theta)$ 依赖；Caprioli 模拟的 7 个 $\theta$ 值即围绕本文讨论的几何）
- **区别于 Blasi 2013**：Blasi 侧重非线性 DSA，本文侧重**几何各向异性**

## 1.6 批判

**[CRITIQUE]** 引言将 "SNR 是 galactic CR 源" 视作**广泛接受**（"widely thought to be responsible"），但未明确引用最新观测证据（如 Fermi LAT 的 GeV γ-ray 观测）。该假设在 2017 年后进一步被证实，但若当时已有充分观测证据，语气可更肯定。
