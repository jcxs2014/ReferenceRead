---
chapter: 3
title: Astrophysical systems
pages: "61–139"
sections:
  - "3.1 Cosmic ray ionization"
  - "3.2 Cosmic ray-driven galactic winds"
  - "3.3 Cosmological effects of cosmic ray-driven winds"
  - "3.4 Thermal instability and cosmic rays in the CGM and ICM"
  - "3.5 Impact of cosmic rays from AGN in massive hot halos"
related_chapters:
  prev: 02_physics
  next: 04_observational_signatures
status: done
---

> 本章属于：Cosmic ray feedback in galaxies and galaxy clusters (Ruszkowski & Pfrommer 2023)
>
> 上一章：`02_physics.md`
>
> 下一章：`04_observational_signatures.md`

# 3. Astrophysical systems — CR 反馈在星系/星系团中的动力学表现

## 3.1 本节核心内容

[FACT] §3 Astrophysical systems 覆盖 pp. 61–139，是论文从"物理基础"（§2）到"观测证据"（§4）之间的桥梁。五个子节按尺度从内到外、机制从基础到综合排列：§3.1 CR ionization → §3.2 CR-driven galactic winds → §3.3 Cosmological effects → §3.4 Thermal instability in CGM/ICM → §3.5 AGN CR in massive halos。

[INTERPRETATION] §3 的结构逻辑是"从局部到整体"：§3.1 从 ISM 内部的微观电离效应出发，§3.2 上升到星系尺度的风，§3.3 拉到宇宙学 halo 尺度，§3.4 讨论 CGM/ICM 的多相气体热力学，§3.5 讨论 AGN 驱动的 CR 反馈——从"小尺度 CR 效应"逐步推进到"大质量晕的加热问题"。

## 3.2 原文内容

### 3.2.1 §3.1 Cosmic ray ionization (pp. 62–68)

[FACT] §3.1 聚焦**低能 CR（$E \lesssim 1$ GeV）在 ISM 中的电离效应**，其核心动机是：此类电离对维持 ISM 中磁场与等离子体的耦合（magnetic field–plasma coupling）和复杂的 ISM 化学至关重要。

[FACT] 巨分子云（GMC）中恒星形成率受**引力与非热压力（湍动 + 磁场）竞争**控制（Crutcher 2012）。磁场对星际等离子体的耦合程度取决于气体的电离度。观测到的分子云电离度显著超过仅靠 UV 光致电离所能产生的水平（McKee 1989），强烈暗示额外电离来自能穿透云的低能 CR。

[FACT] 低能 CR 通过 **spallation（碎裂）** 反应产生轻元素 Li、Be、B：CNO 核被低能 CR 撞击后碎裂。这是宇宙中 Li/Be/B 丰度异常高于恒星内部反应所能解释的水平的原因。

[FACT] CR 谱的低能端因**太阳调制（solar modulation）** 而衰减，周期约 11 年。Voyager 探测器飞越 heliopause 之后首次获得不受调制影响的低能 CR 直接测量（Cummings et al. 2016；Stone et al. 2019）。

[FACT] pp 碰撞阈值：$E_{\text{thr}} \approx 280$ MeV（kinematic threshold $2m_p = 2m_p + m_{\pi^0}$）。银河系盘面上 $\gtrsim 100$ MeV 的弥漫 γ 射线主要由 pp → $\pi^0$ → $\gamma\gamma$ 过程主导。

[FACT] IC 散射的估计光子能量：

$$
E_{\text{ph}} \approx 5\,E_1^2\,\varepsilon_1\,\text{MeV}
$$

其中 $E_1$ 为 CR 电子能量（GeV），$\varepsilon_1$ 为种子光子能量（eV）。

[FACT] 同步辐射特征频率：

$$
\nu_{\text{ph}} \approx 320\,E_1^2\,B_{10}\,\text{MHz}
\quad \text{(Eq. 51)}
$$

### 3.2.2 §3.2 Cosmic ray-driven galactic winds (pp. 68–112)

[FACT] §3.2 开篇指出，大尺度 late-type 星系外流（galactic winds）在宇宙中普遍观测到（Rupke et al. 2005；Heckman & Thompson 2017；Veilleux et al. 2020），在解决恒星形成熄灭（quenching）、CGM 金属富化、"missing baryon problem"方面起到关键作用。

[FACT] 驱动 galactic winds 的机制分类：
- **Energy-driven**（Chevalier & Clegg 1985）：SN 爆炸提供热能
- **Momentum-driven**（Murray et al. 2005）：辐射压
- **CR-driven**（§3.2 主题）：CR 压力梯度

[FACT] **Breitschwerdt et al. (1991) 磁通管模型**（论文 Eq. 62）：

$$
u^2 - c_{\text{eff}}^2\,\frac{d\ln u}{d\ln z} = c_{\text{eff}}^2\,\frac{d\ln A}{d\ln z} + z\,g_z(z)
\quad \text{(Eq. 62)}
$$

- $u$：气体速度；$A(z)$：磁通管截面积；$g_z(z)$：重力加速度；$c_{\text{eff}}$：含热压 + CR 压 + 波压的有效声速

[FACT] 论文指出**热驱动风的根本困难**：等熵热驱动风膨胀时 $c_{\text{eff}}^2 \propto \rho^{2/3}$ 下降比引力势 $\Phi \propto -v_{\text{circ}}^2/r$ 更快，热驱动风难以达到临界点并加速到超音速。

[FACT] **CR 驱动风的关键优势**：sub-Alfvénic 流中，CR 以 Alfvén 速度 streaming，CR 压力按 $P_{\text{cr}} \propto (\rho\,v_A\,A)^{-4/3} \propto \rho^{2/3}$ 变化（来自 Eq. 22 的强耦合极限），从而 $c_{\text{eff}}^2 \propto \rho^{-1/3}$。此时 Eq. 62 右端可变为正，CR 加速流能达到超音速。

[FACT] 银河系条件下纯 CR 驱动风 $\dot{M} \sim \mathcal{O}(1)\,M_\odot\,\text{yr}^{-1}$。CR 动能功率与 CR 注入功率比较：

$$
\frac{1}{2}\,\rho_0\,v_0\,v_{\text{esc}}^2\,A_{\text{disk}} \sim \frac{u_{\text{cr}}\,V_{\text{disk}}}{\tau_{\text{esc}}}
\quad \text{(Eq. 63)}
$$

$$
\dot{m}_{\text{cr}} \approx \frac{2\,u_{\text{cr}}\,h_{\text{disk}}}{v_{\text{esc}}}
\quad \text{(Eq. 64)}
$$

[FACT] Time-dependent wind solutions（Dorfi & Breitschwerdt 2012；Dorfi et al. 2019）：多次恒星反馈在风中形成 forward/reverse shock，能 in situ 通过 first-order Fermi 过程再加速 CR，可能把 CR 加速到 Knee（$\sim 3\times 10^{15}$ eV）甚至 Ankle（$\sim 10^{18}$ eV）以上。

### 3.2.3 §3.3 Cosmological effects of cosmic ray-driven winds (pp. 112–120)

[FACT] CR 传输系数（$\mathcal{D}$）对质量外流率呈**非单调关系**：峰值出现在 $\mathcal{D} \sim 3\times 10^{29}$ cm$^2$ s$^{-1}$ 附近。

[FACT] **Gray approximation 的局限性**：Werhahn et al. (2021a) 后处理分析表明，在盘以上的动力学区域该假设失效。

[FACT] **多能量 CR 流体模型**（Miniati 2001；Yang & Ruszkowski 2017；Girichidis et al. 2019, 2022；Ogrodnik et al. 2021）：
- 矮星系 mass loading factor 可下降至灰色模型的 1/4（Girichidis et al. 2023）
- 银河系质量星系中 CR 传输完全靠扩散

[FACT] 能量加权 CR 扩散系数空间变化可达两个数量级：
- 盘和风区：$1–3\times 10^{28}$ cm$^2$ s$^{-1}$（GeV CR）
- CGM：可达 $3\times 10^{29}$ cm$^2$ s$^{-1}$（TeV CR）

### 3.2.4 §3.4 Thermal instability and CRs in the CGM and ICM (pp. 120–127)

[FACT] §3.4 的**核心论点**：CGM 和 ICM 中观测到大量冷气体（$T \sim 10^4$ K），这些冷气体可贡献 CGM 总重子质量预算的**最多 50%**（Werk et al. 2014）。

[FACT] 冷气体在 CGM 中的**两种解释路径**：
- **路径 1（外流起源）**：冷气体被热/快的银河外流从 halo 中心"挖掘"出来
- **路径 2（原位 condensation）**：冷气体通过热不稳定性在原位形成

[FACT] **Cloud survival mechanisms**：
- 磁 draping（Dursi & Pfrommer 2008）：drag 只增加约 2.5 倍
- CR 加速云团（Wiener et al. 2017a；Thomas et al. 2021）：CR 在冷云遇到磁瓶颈时产生跨云 CR 压力梯度
- 快速辐射冷却再生长（Gronke & Oh 2018）
- Shattering into cloudlets

### 3.2.5 §3.5 Impact of cosmic rays from AGN in massive hot halos (pp. 127–139)

[FACT] **$M_\odot$ 尺度以上的晕中，恒星反馈失效**，AGN 驱动的 CR 加热成为主导。radio AGN 在 $M_\star > 10^{11}\,M_\odot$ 的星系中几乎普遍存在（Sabater et al. 2019）。

[FACT] **Cooling catastrophe**：若无加热，$T \sim 1$ keV 气体可快速坍缩到中心，速率 $\sim 10^{2-3}\,M_\odot\,\text{yr}^{-1}$，远超观测约束（Peterson & Fabian 2006）。

[FACT] AGN 能量热化的四种主要候选机制：
1. 声波和弱冲击的耗散（Fabian et al. 2003）
2. 内部重力波的激发和湍流耗散（Zhuravleva et al. 2014）
3. AGN lobe 热等离子体与周围介质的 uplift/mixing
4. CR 从 AGN cavity 逃逸并加热 CGM/ICM（Guo & Oh 2008；Pfrommer 2013；Ruszkowski et al. 2017a；Ehlert et al. 2018）

[FACT] §3.5 强调**自调节（self-regulation）**是所有成功 AGN 反馈模型的核心要求。

## 3.3 关键公式

$$
\boxed{u^2 - c_{\text{eff}}^2\,\frac{d\ln u}{d\ln z} = c_{\text{eff}}^2\,\frac{d\ln A}{d\ln z} + z\,g_z(z)}
\quad \text{(Eq. 62)}
$$

$$
\boxed{\dot{m}_{\text{cr}} \approx \frac{2\,u_{\text{cr}}\,h_{\text{disk}}}{v_{\text{esc}}}}
\quad \text{(Eq. 64)}
$$

$$
\boxed{E_{\text{ph}} \approx 5\,E_1^2\,\varepsilon_1\,\text{MeV}}
\quad \text{(IC)}
$$

$$
\boxed{\nu_{\text{ph}} \approx 320\,E_1^2\,B_{10}\,\text{MHz}}
\quad \text{(Eq. 51)}
$$

## 3.4 关键参数

| 参数 | 数值 | 单位 | 出处 |
|------|------|------|------|
| 冷气体在 CGM 中的质量占比 | 最多 50% | — | §3.4 |
| pp 碰撞阈值 | $\sim 280$ | MeV | §3.1 |
| 银河系 CR 驱动风质量损失率 | $\mathcal{O}(1)$ | $M_\odot$ yr$^{-1}$ | §3.2 |
| CR 驱动风峰值扩散系数 | $\sim 3\times 10^{29}$ | cm$^2$ s$^{-1}$ | §3.3 |
| 盘内 CR 扩散系数 | $1–3\times 10^{28}$ | cm$^2$ s$^{-1}$ | §3.3 |
| CGM CR 扩散系数 | $\sim 3\times 10^{29}$ | cm$^2$ s$^{-1}$ | §3.3 |
| Halo 质量阈值（热/冷吸积转换） | $\sim 10^{11.5}$ | $M_\odot$ | §3.3 |
| Halo 质量阈值（恒星→AGN 反馈） | $\sim 10^{12}$ | $M_\odot$ | §3.5 |

## 3.5 图表分析

**Figure 2**（Halo mass vs. stellar-to-halo mass，约 p. 128）— §3.5 讨论 AGN 加热的触发 halo 质量范围：

### 1. 图的目的
展示 stellar-to-halo mass ratio 在 $M_h \sim 10^{12}\,M_\odot$ 处达到峰值（Moster et al. 2010）。

### 2. 物理意义
- 为 §3.5 的 AGN–CR 反馈论证提供质量尺度边界
- 大质量晕中恒星反馈效率下降，AGN 反馈主导

## 3.6 作者的逻辑

```
§3.1 [ISM 电离] CR 电离维持磁场–气体耦合
  → §3.2 [银河风] CR 压力驱动外流（Eq. 62/63/64）
    → §3.3 [宇宙学尺度] CR 传输系数影响质量加载因子
      → §3.4 [CGM/ICM 冷相] 热不稳定性 + CR 塑造冷气体
        → §3.5 [大质量晕 AGN] AGN CR 加热解决冷却流问题
```

[INTERPRETATION] §3 形成"尺度上升 + 机制升级"的链式结构：从"CR 电离 ISM"（$\sim 10^1–10^2$ pc）→ "CR 驱动风"（kpc）→ "宇宙学 halo"（$\sim 100$ kpc）→ "CGM/ICM 冷相"（$\sim$ Mpc）→ "AGN 加热的星系团"（$\sim$ Mpc）。

## 3.7 我的理解

### 3.7.1 CR 驱动风与热驱动风的关键物理差别

[INTERPRETATION] Eq. 62 揭示了 CR 驱动风的核心优势：

| 特性 | 热驱动风 | CR 驱动风 |
|------|----------|----------|
| $c_{\text{eff}}^2$ 与密度关系 | $c_{\text{eff}}^2 \propto \rho^{2/3}$ | $c_{\text{eff}}^2 \propto \rho^{-1/3}$ |
| 膨胀时行为 | $c_{\text{eff}}^2$ 快速下降 | $c_{\text{eff}}^2$ 缓慢上升 |
| 能否达到临界点 | 否 | 是（Eq. 62 右端变正） |
| 能量储存时标 | $\sim 10^7$ yr | $\sim 10^9$ yr |

[INTERPRETATION] 这正是"CR 反馈是慢热机制"的物理根源：CR 的冷却时标远长于热能，因此 CR 能在低密度区域仍然维持足够的压力支撑。

### 3.7.2 [CRITIQUE] AGN 加热机制的未定问题

[CRITIQUE] §3.5 列举了四种 AGN 能量热化机制，但明确承认"which of the above processes represents the dominant mode of heating in massive halos"仍是开放问题。作者强调自调节是成功 AGN 反馈模型的核心要求，但没有给出"CR 加热是否比声波耗散更易实现自调节"的定量比较。

### 3.7.3 §3 与 §4 的接口

[INTERPRETATION] §3 中的物理预期（galactic winds 速度、CR 谱、AGN 加热率、冷气体质量占比）在 §4 Observational signatures 中将逐一与实际观测对照：

| §3 物理预期 | §4 观测验证 |
|-------------|------------|
| §3.2 CR 驱动银河风 | §4.2 Fermi/eROSITA bubbles + MeerKAT |
| §3.3 宇宙学 CR 风 | §4.3 河外 FIR-radio correlation |
| §3.4 CGM 冷气体 | §4.4 吸收线 + 非热压力 |
| §3.5 AGN CR 加热 | §4.5–§4.6 γ 射线 halo + AGN lobe CR |

## 3.8 潜在问题与值得关注的地方

### 3.8.1 CR spectrum in wind 的观测约束

[CRITIQUE] §3.2 指出 Ptuskin et al. (2008) 和 Recchia et al. (2016, 2017) 的 CR 谱计算与观测不一致（$E \gtrsim 200$ GeV 时 too hard）。"Ion-neutral friction"和"非平衡 CR 传输"能显著修正结果，但尚未系统纳入 galactic wind 模拟。

### 3.8.2 Gray CR 近似 vs. 多能量 CR 流体

[CRITIQUE] §3.3 讨论 gray approximation 的局限性。当前多数 cosmological simulations 的 CR 反馈结果可能高估了矮星系的 outflow 效率，未来模拟需要使用多能量 CR 流体。

### 3.8.3 AGN–CR 耦合的观测区分

[CRITIQUE] §3.5 承认 AGN 加热的四种机制难以通过当前观测（X-ray 温度和熵 profile）区分。需要多信使观测才能分离各机制的贡献。

---

## 元数据

```yaml
chapter: 3
pages: "61–139"
subsections: ["3.1", "3.2", "3.3", "3.4", "3.5"]
key_formulas:
  - "Eq. 62: galactic wind momentum equation"
  - "Eq. 64: CR-driven mass loss rate"
  - "E_ph ≈ 5 E_1² ε_1 MeV (IC)"
  - "ν_ph ≈ 320 E_1² B_10 MHz (synchrotron, Eq. 51)"
keywords:
  - galactic winds
  - Breitschwerdt flux tube
  - CGM/ICM cold phase
  - AGN thermalization
  - self-regulation
  - cloud survival
references_internal:
  prev_chapter: 02_physics
  next_chapter: 04_observational_signatures
```

**引用页码**：全文引用基于 *A&A Reviews 31:4 (2023)*，pp. 61–139。
