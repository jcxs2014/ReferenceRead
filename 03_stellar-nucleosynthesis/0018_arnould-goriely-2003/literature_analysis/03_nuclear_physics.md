---
title: '§3 The nuclear physics of relevance to the p-process'
paper: 03_stellar-nucleosynthesis/0018_arnould-goriely-2003/literature_analysis/00_overview.md
chapter: 3
status: completed
read_date: '2026-08-16'
---

# §3 p 过程相关的核物理

> 本章是 p 过程物理的**核心支柱**，涵盖反应网络中每一类反应的实验与理论现状，以及不确定性的系统评估。

## 3.1 中子俘获与光致反应：实验现状（§3.1）

- 中子俘获（n,γ）截面已被较系统测量（尤其对 s 过程关键同位素），但许多 p 过程相关的**缺中子同位素**的中子俘获截面仍属空白。
- 光致分解（γ,n）、(γ,p)、(γ,α) 截面通常通过**直接反应**（E1 巨共振、集体激发）或**详细平衡**从对应的 (n,γ)、(p,γ)、(α,γ) 逆反应推算。
- 关键光致分解：**12C(γ,α), 12C(γ,n), 12C(γ,p), 16O(γ,α), 20Ne(γ,α), 22Ne(γ,α)** 等对反应网络入口极为敏感。

## 3.2 带电粒子俘获：实验现状（§3.2）

- (p,γ)、(d,γ)、(³He,γ)、(α,γ) 反应在低 A 端（Z<50 附近）和接近质子滴线处对 p 过程丰度起决定作用。
- 许多关键率无法直接测量（需要缺中子放射性靶或束流），必须依赖理论外推。
- **12C(α,γ)16O** 是本章最重要的反应之一，虽然它主要决定恒星演化中的 O/Ne 比，但它通过影响 O/Ne 层的化学成分间接决定 p 过程种子丰度。

## 3.3 反应率的理论评估：统计模型（§3.3）

作者详细阐述了**Hauser-Feshbach 统计模型**框架：

### 3.3.1 一般框架
反应率 ⟨σv⟩ = 积分 σ(E) · v · Maxwell-Boltzmann 分布 dE。σ(E) 通过 HF 模型计算，包含：
- 入射通道的复合核形成概率
- 各退激通道的分支比

### 3.3.2 基态性质（§3.3.2）
- 结合能：来自核质量表（Goriely-Hubin-Sarbach 或 FRDM 液滴模型外推）
- 自旋与宇称：决定低能截面的能级分布
- 同位旋：影响 (p,γ) 与 (n,γ) 的关系

### 3.3.3 核能级密度（§3.3.3）
- **Back-shifted Fermi gas 模型**是主流选择
- 替代方案：constant-temperature 模型、超级形变模型
- 不同模型之间的差异是反应率不确定性的主要来源之一

### 3.3.4 光学势（§3.3.4）
- 中子光学势、质子光学势、α 光学势：参数化形式（Koning-Delaroche 等）
- 影响复合核形成的穿透概率

### 3.3.5 γ 射线强度函数（§3.3.5）
- E1、M1 跃迁强度；KMF（Kramers-Migdal-Feshbach）与 GN（Generalized Lorentzian）模型
- 与 M1 "剪式共振"、巨偶极共振相关

## 3.4 测量率与计算率的对比（§3.4）

- 作者将理论计算与已有实验数据对比，总体一致性在**因子 2–3** 内，但对某些关键反应（如 12C(γ,α)）差异可达**一个数量级**。
- 这决定了 p 过程丰度的绝对不确定性约 **2×–5×**，远大于天体物理参数变化的影响（见 §5.5）。

## 3.5 反应率不确定性的系统评估（§3.5）

- 用**不同组核输入（质量表、能级密度、光学势、γ 强度函数）**计算同一反应的率，将离散范围视为不确定性区间。
- 作者给出 ~50 个关键反应的**不确定性因子表**：大多数在 2–3 之间，少数（如 12C(γ,α)、¹²C(γ,n)）达 5–10。
- **关键结论**：核物理不确定性是 p 过程预测丰度的**主导误差源**，远大于天体物理参数（爆炸能量、恒星质量）的影响。

## 3.6 p 过程反应网络（§3.6）★

> **本文最核心的建模产物**：Goriely & Arnould 反应网络。

- **物种数**：数万至数十万种核素
- **反应通道**：数千万级（含 (γ,n)、(γ,p)、(γ,α)、(n,γ)、(p,γ)、(d,γ)、(³He,γ)、(α,γ) 等）
- **求解器**：刚性 ODE 求解器（如 Gear's method），在温度-密度演化时间轴上积分
- **关键物理假设**：
  - 温度、密度作为时间函数由天体物理模型（§4–5）提供
  - 电子俘获、β⁺ 衰变在低温时重要
  - 网络收敛性检验：增加物种与反应数目直到丰度变化 <1%
- **与太阳 p 核素丰度的对比**：图 3.6 类图将模型预测丰度与太阳观测值并置，显示大部分 p 核素在 2× 以内，但 138La、180Ta(m)、轻 Mo/Ru 明显偏离（见 §6）。

---

## 分章索引
- 上：02_observed_abundances.md
- 下：04_pre_sn_production.md


---

## 3.7 关键公式补充（FACT+LaTeX，原文页码已注）

> **FACT 补充**：§3 是 p 过程核物理的核心章节。以下公式在原文 §3.1–3.6 的正文与图注中被逐一定义（p.13–25），是 Hauser-Feshbach 统计模型的反应率、能级密度与光学势的完整解析骨架。

### 3.7.1 光子通量与光致分解率（原文 p.14，§3.1）
- 黑体光子通量（每 keV 单位能量）：$\dot{n}(\varepsilon)=\dfrac{2\varepsilon^{2}}{\pi^{2}\hbar^{3}c^{3}}\,\dfrac{1}{\exp(\varepsilon/kT)-1}$（Planck 分布积分得反应率，原文 p.14 Eq.(1) 图注）
- 光致分解反应率：$\langle\lambda\rangle_{\gamma}=N_A\int_{E_{\mathrm{thr}}}^{\infty}\dot{n}(\varepsilon)\,\sigma_{\gamma,n}(\varepsilon)\,d\varepsilon$（原文 p.14）
- 阈值下截面线性外推：$\sigma_{\gamma,n}(\varepsilon)\propto(\varepsilon-E_{\mathrm{thr}})/E_{\mathrm{thr}}$，$\varepsilon\to E_{\mathrm{thr}}^{+}$（原文 p.14 Fig. 11 图注）

### 3.7.2 巨共振与 γ 强度函数（原文 p.14–15，§3.1）
- 巨偶极共振 Lorentz 截面：$\sigma_{\gamma}(E)=\sigma_0\,\dfrac{E\,\Gamma_{\mathrm{GDR}}^{2}}{(E^{2}-E_{\mathrm{GDR}}^{2})^{2}+E^{2}\Gamma_{\mathrm{GDR}}^{2}}$（原文 p.14）
- 总强度求和规则：$\int\sigma_{\gamma}(E)\,dE=\dfrac{60\pi^{2}\hbar^{2}}{m_pc^{2}}\,\dfrac{NZ}{A}\;\mathrm{MeV\cdot mb}$（WDR 求和规则，原文 p.14）
- 光强函数：$f_{\gamma}(E_{\gamma})=\dfrac{\sigma_{\gamma}(E_{\gamma})}{4\sqrt{3}\pi^{2}\hbar c\,E_{\gamma}^{2}}$（原文 p.14–15）

### 3.7.3 Hauser-Feshbach 截面（原文 p.16–18，§3.3.1–3.3.2）
- HF 反应截面（$I+j\to L+k$）：$\sigma_{jk}(E)=\dfrac{\pi}{k^{2}}\sum_{J}\dfrac{2J+1}{(2J_I+1)(2J_j+1)}\,T_i^{J}\,\dfrac{T_k^{J}}{T_{\mathrm{tot}}^{J}}$（原文 p.16–17）
- 穿透系数定义：$T_c^{J}=1-\left|\dfrac{\mathcal{G}_{l_c}^{\pm}}{H_{l_c}^{-}}\right|^{2}$，其中 $\mathcal{G}^{\pm}=f+ig$（原文 p.17）
- 玻尔复合核假设：$T_{\mathrm{tot}}^{J}=\sum_{c}T_c^{J}$（原文 p.17，含弹性增强修正）

### 3.7.4 反应率与麦克斯韦-玻尔兹曼积分（原文 p.17–18，§3.3.1）
- 反应率：$\langle\sigma v\rangle=\sqrt{\dfrac{8}{\pi\mu(kT)^{3}}}\int_0^{\infty}\sigma(E)\,E\,\exp(-E/kT)\,dE$（原文 p.17）
- 激发态恒星反应率（Boltzmann 权重求和）：$\langle\lambda\rangle_I^{\star}=\sum_J\,(2J_I+1)\,\langle\lambda\rangle_{I,J}\,\exp(-E_J/kT)\Big/\,g_I(T)$（原文 p.17）
- 配分函数：$g_I(T)=(2J_I+1)\sum_J\exp(-E_J/kT)$（原文 p.17）

### 3.7.5 互反定理（原文 p.18，§3.3.1）
- 互反关系：$\langle\lambda\rangle_{\gamma,n}=\dfrac{2(2J_L+1)}{(2J_I+1)}\exp(-S_n/kT)\,\langle\lambda\rangle_{n,\gamma}$（原文 p.18 Eq.(5) 上下文）
- 等价表述（粒子数守恒）：$N_I\langle\lambda\rangle_{\gamma}=\sum_J N_L^{J}\langle\lambda\rangle_{L,J\to I}^{J}$（原文 p.18）

### 3.7.6 激发态光致分解（原文 p.18–19，§3.3.2）
- 总光致分解率（含激发态）：$\langle\lambda\rangle_{\gamma}=\dfrac{\sum_J(2J+1)\langle\lambda\rangle_J\exp(-E_J/kT)}{(2J_0+1)\sum_J\exp(-E_J/kT)}$（原文 p.18 Eq.(6)）

### 3.7.7 核能级密度（原文 p.19，§3.3.3）
- Back-shifted Fermi gas 模型：$\rho(\varepsilon^{*})=\dfrac{\exp[2\sqrt{a\varepsilon^{*}}]}{12\sqrt{2}\,a^{1/2}(\varepsilon^{*})^{5/4}\,\sigma}$（原文 p.19）
- 单粒子能级密度（Fermi gas）：$g=\dfrac{A\pi^{2}}{6S_{n,\mathrm{lab}}}$，$a=g/4$（原文 p.19）
- 常数温度模型：$\rho(\varepsilon^{*})\propto\exp(\varepsilon^{*}/T_0)$（原文 p.19）

### 3.7.8 光学势与穿透概率（原文 p.19–21，§3.3.4）
- 中子光学势：$V_n(r)=V_0+\mathcal{W}_v f(r,a_v)+4a_s\,\mathcal{W}_s\,f'(r,a_s)+V_{\mathrm{so}}\,f'(r,a_{\mathrm{so}})\dfrac{1}{r}\dfrac{d}{dr}$（原文 p.19–20）
- 库仑修正（带电粒子）：$V_c(r)=Z_1Z_2e^{2}/r$（$r>R$）；$V_c(r)=\dfrac{Z_1Z_2e^{2}}{2R}\left(3-(r/R)^{2}\right)$（$r\le R$）（原文 p.20）
- 库仑势垒高度：$V_B=\dfrac{Z_1Z_2e^{2}}{r_B}$，$r_B=r_0(A_1^{1/3}+A_2^{1/3})$（原文 p.20）

### 3.7.9 E1 强函数（原文 p.21–22，§3.3.5）
- 广义 Lorentz 强函数（GN）：$f_{E1}(E)=\dfrac{1}{15\pi^{2}\hbar c}\sum_i\dfrac{NZ}{A}\,\dfrac{\sigma_{E1,i}\Gamma_i}{E}\,\dfrac{E\Gamma_i+E_{G,i}\Gamma_{\mathrm{ph}}(E)}{(E^{2}-E_{G,i}^{2})^{2}+(E\Gamma_i)^{2}}$（原文 p.21–22）
- 简化单 Lorentz 强函数：$f_{E1}(E)=\dfrac{1}{15\pi^{2}\hbar c}\dfrac{NZ}{A}\,\dfrac{\sigma_0\Gamma}{E}\,\dfrac{E\Gamma+E_G\Gamma_{\mathrm{ph}}}{(E^{2}-E_G^{2})^{2}+(E\Gamma)^{2}}$（原文 p.22）
- QRPA 微观强度（原文 p.22–23）：$\sigma_{\gamma n}(E)$ 通过 B(E1) 跃迁与微观单粒子态直接计算

### 3.7.10 反应网络 ODE（原文 p.24–25，§3.6）
- 丰度演化：$\dfrac{dY_i}{dt}=\sum_j\bigl(\lambda_{j\to i}\,Y_j-\lambda_{i\to j}\,Y_i\bigr)+\lambda_{\beta,\mathrm{in}}\,Y_k-\lambda_{\beta,\mathrm{out}}\,Y_i$（原文 p.24–25）
- 网络规模：$N_{\mathrm{nuc}}\gtrsim 2\times10^{4}$，$N_{\mathrm{rxn}}\gtrsim 2\times10^{7}$（原文 p.24–25）
- 网络收敛判据：$\max_i\left|\dfrac{Y_i^{(N+1)}-Y_i^{(N)}}{Y_i^{(N)}}\right|<10^{-2}$（原文 p.25）


### 3.7.11 关键 FACT 汇总（原文 p.13–25）
- **[FACT]** HF 截面对穿透系数的依赖 $\sigma_{jk}\propto T_i\,T_k/T_{\mathrm{tot}}$ 决定了 §3.5 全部 50 个关键反应率不确定性的来源（原文 p.16–17）。
- **[FACT]** 互反定理（原文 p.18 Eq. 5）使 (n,γ) 实验可直接推断 (γ,n) 恒星率，是本综述核物理建模的关键桥梁。
- **[FACT]** Back-shifted Fermi gas 模型（原文 p.19）是作者反应网络的标准能级密度选择，$a=g/4$ 中 $g$ 用实验 $S_n$ 定标。
- **[FACT]** 库仑势垒 $V_B\propto Z_1Z_2/A^{1/3}$ 是低 A 端 p 过程为何需要带电粒子俘获而非光致分解的根本原因（原文 p.20）。
- **[FACT]** 广义 Lorentz 强函数 GN 是 §3.3.5 的核心强函数模型（原文 p.21–22），决定 (n,γ) 与 (γ,n) 的恒星率。
- **[FACT]** 反应网络规模 $N_{\mathrm{nuc}}\gtrsim 2\times10^{4}$、$N_{\mathrm{rxn}}\gtrsim 2\times10^{7}$ 是本文 p 过程建模量级的定量声明（原文 p.24–25）。
