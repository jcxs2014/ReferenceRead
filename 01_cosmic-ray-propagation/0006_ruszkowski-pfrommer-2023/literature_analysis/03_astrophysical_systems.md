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

[FACT] §3 Astrophysical systems 覆盖 pp. 61–139，是论文从"物理基础"（§2）到"观测证据"（§4）之间的桥梁。五个子节按**尺度从内到外、机制从基础到综合**排列：

1. §3.1 Cosmic ray ionization（CR 在 ISM 中的电离效应）
2. §3.2 Cosmic ray-driven galactic winds（CR 驱动银河风）
3. §3.3 Cosmological effects of CR-driven winds（宇宙学尺度 CR 风的影响）
4. §3.4 Thermal instability and CRs in the CGM and ICM（热不稳定性 + CR 在 CGM/ICM）
5. §3.5 Impact of CRs from AGN in massive hot halos（AGN CR 在大质量晕中的影响）

[INTERPRETATION] §3 的结构逻辑是"从局部到整体"：§3.1 从 ISM 内部的微观电离效应出发，§3.2 上升到星系尺度的风，§3.3 拉到宇宙学 halo 尺度，§3.4 讨论 CGM/ICM 的多相气体热力学，§3.5 讨论 AGN 驱动的 CR 反馈——从"小尺度 CR 效应"逐步推进到"大质量晕的加热问题"。

## 3.2 原文内容

### 3.2.1 §3.1 Cosmic ray ionization (pp. 62–68)

[FACT] §3.1 聚焦**低能 CR（$E \lesssim 1$ GeV）在 ISM 中的电离效应**，其核心动机是：此类电离对维持 ISM 中磁场与等离子体的耦合（magnetic field–plasma coupling）和复杂的 ISM 化学至关重要。

[FACT] 巨分子云（GMC）中恒星形成率受**引力与非热压力（湍动 + 磁场）竞争**控制（Crutcher 2012）。磁场对星际等离子体的耦合程度取决于气体的电离度。观测到的分子云电离度虽低，但仍足以让磁场部分耦合到气体上，从而支持磁制动（magnetic braking）、减缓恒星形成、在行星盘上运作 MRI（magneto-rotational instability）。

[FACT] 这些电离度显著超过**仅靠 UV 光致电离**所能产生的水平（因分子云有很高的 column density，McKee 1989），强烈暗示额外电离来自能穿透云的低能 CR。

[FACT] 低能 CR（$E \lesssim 1$ GeV）的**电离 + 加热**双重作用：
- 电离：维持磁场–气体耦合
- 加热：维持分子云在观测到的温度水平
- 化学：提供离–中反应（ion-neutral reactions）所需的电离，这些反应比中性–中性反应快得多（Bergin & Tafalla 2007）

[FACT] 低能 CR 通过 **spallation（碎裂）** 反应产生轻元素 Li、Be、B：CNO 核被低能 CR 撞击后碎裂。这是宇宙中 Li/Be/B 丰度异常高于恒星内部反应所能解释的水平的原因。

[FACT] CR 谱的低能端因**太阳调制（solar modulation）** 而衰减，周期约 11 年。Voyager 探测器飞越 heliopause 之后首次获得不受调制影响的低能 CR 直接测量（Cummings et al. 2016；Stone et al. 2019）。

[FACT] 低能 CR 谱还可以通过**γ 射线间接约束**：
- pp 碰撞阈值：$E_{\text{thr}} \approx 280$ MeV（Kinematic threshold $2m_p = 2m_p + m_{\pi^0}$）
- 银河系盘面上 $\gtrsim 100$ MeV 的弥漫 γ 射线主要由 pp → $\pi^0$ → $\gamma\gamma$ 过程主导

[FACT] IC 散射的估计光子能量公式：

$$
E_{\text{ph}} \approx 5\,E_{1}^2\,\varepsilon_{1}\,\text{MeV}
$$

其中 $E_1$ 为 CR 电子能量（单位 GeV），$\varepsilon_1$ 为种子光子能量（单位 eV）。

[FACT] 同步辐射特征频率：

$$
\nu_{\text{ph}} \approx 320\,E_1^2\,B_{10}\,\text{MHz}
\quad \text{(Eq. 51)}
$$

其中 $B_{10}$ 为以 $10^{-10}$ G 为单位的磁场强度。

### 3.2.2 §3.2 Cosmic ray-driven galactic winds (pp. 68–112)

[FACT] §3.2 开篇指出，大尺度 late-type 星系外流（galactic winds）在宇宙中普遍观测到（Rupke et al. 2005；Heckman & Thompson 2017；Veilleux et al. 2020），在解决恒星形成熄灭（quenching）、CGM 金属富化、"missing baryon problem"方面起到关键作用。

[FACT] 驱动 galactic winds 的机制分类：
- **Energy-driven**（Chevalier & Clegg 1985）：SN 爆炸提供热能驱动外流
- **Momentum-driven**（Murray et al. 2005）：辐射压驱动外流
- **CR-driven**（§3.2 主题）：CR 压力梯度驱动外流

[FACT] 论文指出前两类在正常盘星系中不足以驱动主导外流，并存在"overcooling problem"（注入热能被辐射带走）和辐射压与多相气体耦合不足的问题。

[FACT] **Breitschwerdt et al. (1991) 磁通管模型**（论文 Eq. 62）：沿磁通管的等熵质量守恒 + 动量守恒：

$$
u^2 - c_{\text{eff}}^2\,\frac{d\ln u}{d\ln z} = c_{\text{eff}}^2\,\frac{d\ln A}{d\ln z} + z\,g_z(z)
\quad \text{(Eq. 62)}
$$

- $u$：气体速度
- $A(z)$：磁通管截面积
- $g_z(z)$：重力加速度（负值）
- $c_{\text{eff}}$：含热压 + CR 压 + 波压贡献的有效声速

[FACT] Eq. 62 与**Parker 太阳风方程**、de Laval nozzle 方程的相似性被明确指出。当亚音速流经过"喷嘴"最窄处（即 Eq. 62 右端为零的点）时，流必须加速到超音速。

[FACT] 论文指出**热驱动风的根本困难**：等熵热驱动风膨胀时密度下降，有效声速按 $c_{\text{eff}}^2 \propto \rho^{2/3}$ 下降，比引力势 $\Phi \propto -v_{\text{circ}}^2 / r$ 更快。因此热驱动风难以达到临界点并加速到超音速。

[FACT] **CR 驱动风的关键优势**：对于 sub-Alfvénic 流，CR 以 Alfvén 速度 $v_A \sim B^{-1/2}$ 沿磁场 streaming，CR 压力随密度按 $P_{\text{cr}} \propto (\rho\,v_A\,A)^{-4/3} \propto \rho^{2/3}$ 变化（来自 CR transport Eq. 22 的强耦合极限，Breitschwerdt et al. 1991 Appendix B），从而 $c_{\text{eff}}^2 \propto \rho^{-1/3}$。此时 Eq. 62 右端可变为正，CR 加速流能够达到超音速（Mao & Ostriker 2018）。

[FACT] 银河系条件下，纯 CR 驱动的稳态风解可以给出质量损失率 $\dot{M} \sim \mathcal{O}(1)\,M_\odot\,\text{yr}^{-1}$。CR 驱动的动能功率与 CR 注入功率比较：

$$
\frac{1}{2}\,\rho_0\,v_0\,v_{\text{esc}}^2\,A_{\text{disk}} \sim \frac{u_{\text{cr}}\,V_{\text{disk}}}{\tau_{\text{esc}}}
\quad \text{(Eq. 63)}
$$

由此给出单位面积的质量损失率：

$$
\dot{m}_{\text{cr}} \approx \frac{2\,u_{\text{cr}}\,h_{\text{disk}}}{v_{\text{esc}}}
\quad \text{(Eq. 64)}
$$

[FACT] §3.2 讨论了两种 wind 模型：
- **磁通管模型**（Flux-tube）：模拟盘的局部外流，包含自洽的 CR 谱计算（Ptuskin et al. 2008；Recchia et al. 2016, 2017）
- **球对称风模型**：克服磁通管只能模拟局部外流的局限，考虑整个星系的全局风解

[FACT] **Time-dependent wind solutions**（Dorfi & Breitschwerdt 2012；Dorfi et al. 2019）：多次恒星反馈在风中的压力波动会叠加成 forward/reverse shock，能 in situ 通过 first-order Fermi 过程再加速 CR，可能把 CR 加速到 Knee（$\sim 3\times 10^{15}$ eV）甚至 Ankle（$\sim 10^{18}$ eV）以上。

[FACT] §3.2 还讨论了两类重要效应：
- **CR spectrum self-consistent computation**：通过平衡 streaming instability 增长率与非线性 Landau damping 率来自洽计算扩散系数；但此类研究一般发现 CR 谱与观测不一致（快 advection 使 $E \gtrsim 200$ GeV 谱比观测更硬）。
- **Ion-neutral friction**：在盘附近显著改变 CR 传播，可能修正 CR 谱预测。

### 3.2.3 §3.3 Cosmological effects of cosmic ray-driven winds (pp. 112–120)

[FACT] §3.3 讨论 CR-driven winds 在宇宙学模拟中的整体影响。核心发现：

[FACT] CR 传输系数（$\mathcal{D}$）对质量外流率的影响呈**非单调关系**：外流率随 $\mathcal{D}$ 增加而上升，达到峰值后再下降。峰值出现在 $\mathcal{D} \sim 3\times 10^{29}$ cm$^2$ s$^{-1}$ 附近，此时 CR 在星系中停留时间足够长以驱动气体，但也足以在气体加速之前逃逸。

[FACT] 在**最大质量晕（$10^{12}\,M_\odot$）**中，增加 $\mathcal{D}$ 导致更大的总外流率和更热的外流。这与 zoom-in 模拟中 cold gas 因 ion-neutral friction 和 Alfvén 速度增加而表现出局部传输加速的趋势一致（Farber et al. 2018）。

[FACT] **Gray approximation（"单能量流体"）**的局限性：大多数 CR 反馈模型使用单动量积分的 CR 流体。该近似在时标竞争（注入 + 传输 vs. 损失）满足稳态条件时成立；但 Werhahn et al. (2021a) 的后处理分析表明，在盘以上（above disk）的动力学区域该假设失效。

[FACT] **多能量 CR 流体模型**（Miniati 2001；Yang & Ruszkowski 2017；Girichidis et al. 2019, 2022；Ogrodnik et al. 2021）：
- 恒星形成率和星系形态受多能量 CR 建模影响有限
- **矮星系**的质量加载因子（mass loading factor）可下降至灰色模型的 1/4（Girichidis et al. 2023）
- 银河系质量星系中，多能量 CR 模型产生更多 fountain flow 中的冷气体

[FACT] 银河系质量（$M_h \sim 10^{12}\,M_\odot$）星系中，**CR 压力梯度本身不足以维持持续外流**，CR 传输完全靠扩散。而**较小质量晕**（$M_h \lesssim 3\times 10^{11}\,M_\odot$）中，强大的 CR 驱动外流主要以 advection 方式传输 CR。

[FACT] 能量加权 CR 扩散系数在不同区域的空间变化可达两个数量级：
- 盘和风区：$1\times 10^{28}$–$3\times 10^{28}$ cm$^2$ s$^{-1}$（GeV CR）
- CGM：可达 $3\times 10^{29}$ cm$^2$ s$^{-1}$（TeV CR 主导）

### 3.2.4 §3.4 Thermal instability and CRs in the CGM and ICM (pp. 120–127)

[FACT] §3.4 的**核心论点**：CGM 和 ICM 中观测到大量冷气体（$T \sim 10^4$ K），这些冷气体可贡献 CGM 总重子质量预算的**最多 50%**（Werk et al. 2014）。CR 在塑造 CGM/ICM 冷相的性质方面可能起**基础性作用**：

1. 解决"即使 CGM/ICM 中有大量冷气体，恒星形成仍被抑制"的谜题
2. 调节冷气体总量
3. 塑造冷气体云的形态与特征尺寸
4. 为冷气体线辐射提供激发源

[FACT] 冷气体在 CGM 中的**两种解释路径**：
- **路径 1（外流起源）**：冷气体被热/快的银河外流从 halo 中心"挖掘"出来。主要挑战是加速云团的存活时间（cloud crushing time vs. acceleration time）。CR 通过 pressure gradient 加速云团，避免 destructive streaming heating。
- **路径 2（原位 condensation）**：冷气体通过热不稳定性在原位 condensation 形成，被 AGN 或 CR 加热调节

[FACT] **Cloud survival mechanisms**：
- **磁 draping（magnetic draping）**：磁场包裹云团，将风–云之间的动量耦合限制为不完全（drag 只增加约 2.5 倍，Dursi & Pfrommer 2008）
- **CR 加速云团**（Wiener et al. 2017a；Thomas et al. 2021）：CR 沿其压力梯度 streaming，在冷云团遇到磁瓶颈时产生跨云团的 CR 压力梯度，加速云团
- **快速辐射冷却再生长**（Gronke & Oh 2018）：云团在被完全破坏前通过辐射冷却重新生长
- **Shattering into cloudlets**：小云团增加表面积，增大 drag force

### 3.2.5 §3.5 Impact of cosmic rays from AGN in massive hot halos (pp. 127–139)

[FACT] §3.5 指出，**$M_\odot$ 尺度以上的晕中，恒星反馈失效**（恒星–晕质量比低，CGM 密度/压力升高），AGN 驱动的 CR 加热成为主导。radio AGN 在 $M_\star > 10^{11}\,M_\odot$ 的星系中几乎普遍存在（Sabater et al. 2019）。

[FACT] **Cooling catastrophe**：若没有加热机制，$T \sim 1$ keV 气体的有效冷却时标远短于晕的年龄，气体可快速失去压力支撑，以 $\sim 10^{2-3}\,M_\odot\,\text{yr}^{-1}$ 的速率向中心坍缩，远超观测约束（Peterson & Fabian 2006）。

[FACT] AGN 反馈的自我调节证据：观测的辐射冷却率与产生 X-ray cavity 所需的 AGN 功率之间有强相关（Churazov et al. 2000；Birzan et al. 2004；Rafferty et al. 2006；Werner et al. 2019）。Ruszkowski & Begelman (2002) 表明 AGN 功率足以提供全局热稳定加热。

[FACT] AGN 能量热化（thermalization）的四种主要候选机制：
1. 声波和弱冲击的耗散（Fabian et al. 2003；Ruszkowski et al. 2004a, b）
2. 内部重力波的激发和湍流耗散（Zhuravleva et al. 2014；Li et al. 2020a）
3. AGN lobe 热等离子体与周围介质的 uplift/mixing（Churazov et al. 2001；Hillel & Soker 2017；Yang & Reynolds 2016a）
4. CR 从 AGN cavity 逃逸并加热 CGM/ICM（Guo & Oh 2008；Pfrommer 2013；Ruszkowski et al. 2017a；Ehlert et al. 2018）

[FACT] §3.5 强调**自调节（self-regulation）**是所有成功 AGN 反馈模型的核心要求：AGN 输出必须"足够温柔"，以避免在 cool core 中产生大幅度的温度和熵扰动（Voit et al. 2017）。

## 3.3 关键公式

$$
\boxed{u^2 - c_{\text{eff}}^2\,\frac{d\ln u}{d\ln z} = c_{\text{eff}}^2\,\frac{d\ln A}{d\ln z} + z\,g_z(z)}
\quad \text{(Eq. 62, galactic wind)}
$$

$$
\boxed{\dot{m}_{\text{cr}} \approx \frac{2\,u_{\text{cr}}\,h_{\text{disk}}}{v_{\text{esc}}}}
\quad \text{(Eq. 64, CR-driven mass loss per unit area)}
$$

$$
\boxed{E_{\text{ph}} \approx 5\,E_1^2\,\varepsilon_1\,\text{MeV}}
\quad \text{(IC photon energy estimate)}
$$

$$
\boxed{\nu_{\text{ph}} \approx 320\,E_1^2\,B_{10}\,\text{MHz}}
\quad \text{(Eq. 51, synchrotron freq.)}
$$

$$
\boxed{P_{\text{cr}} \propto \rho^{2/3} \;\;\text{(thermally driven)},\;\; P_{\text{cr}} \propto \rho^{2/3} \;\;\text{(CR-driven, streaming)}}
\quad \text{导致 } c_{\text{eff}}^2 \propto \rho^{-1/3}\text{（CR）vs. } c_{\text{eff}}^2 \propto \rho^{2/3}\text{（thermal）}
$$

$$
\boxed{t_{\text{cool}}^{\text{ICM}} \sim 10^{10}–10^{11}\,\text{yr} \gg t_{\text{dyn}}^{\text{cluster}} \sim 10^{9}\,\text{yr}}
$$

## 3.4 关键参数

| 参数 | 数值 | 单位 | 出处 |
|------|------|------|------|
| 冷气体在 CGM 中的质量占比 | 最多 50% | — | §3.4 |
| CR 冷却时标（ISM, GeV） | $\sim 10^{9}$ | yr | §2.4/§3.1 |
| CR 冷却时标（ICM） | $\sim 10^{10}–10^{11}$ | yr | §2.4 |
| pp 碰撞阈值 | $\sim 280$ | MeV | §3.1 |
| 银河系 CR 驱动风质量损失率 | $\mathcal{O}(1)$ | $M_\odot$ yr$^{-1}$ | §3.2 |
| CR 驱动风峰值扩散系数 | $\sim 3\times 10^{29}$ | cm$^2$ s$^{-1}$ | §3.3 |
| 盘内 CR 扩散系数 | $1–3\times 10^{28}$ | cm$^2$ s$^{-1}$ | §3.3 |
| CGM CR 扩散系数 | $\sim 3\times 10^{29}$ | cm$^2$ s$^{-1}$ | §3.3 |
| Halo 质量阈值（热/冷吸积转换） | $\sim 10^{11.5}$ | $M_\odot$ | §3.3 |
| Halo 质量阈值（恒星→AGN 反馈） | $\sim 10^{12}$ | $M_\odot$ | §3.5 |
| AGN 加热冷却时标 | $\ll 10^{9}$ | yr（ICM） | §3.5 |
| ICM 冷却流坍缩率 | $10^{2}–10^{3}$ | $M_\odot$ yr$^{-1}$ | §3.5 |

## 3.5 图表分析

**Figure 2**（Halo mass vs. stellar-to-halo mass, 约 p. 128）— §3.5 中讨论 AGN 加热的触发 halo 质量范围：

### 1. 图的目的
展示 stellar-to-halo mass ratio 在 $M_h \sim 10^{12}\,M_\odot$ 处达到峰值，对应 AGN 反馈开始主导的 halo 质量阈值。

### 2. 坐标轴
- 横轴：$M_h$（halo mass，对数，$\sim 10^{10}–10^{13}\,M_\odot$）
- 纵轴：$M_\star/M_h$（stellar-to-halo mass ratio，对数，$\sim 10^{-3}–10^{-1}$）

### 3. 关键观察
- 峰值出现在 $M_h \sim 10^{12}\,M_\odot$ 附近（Moster et al. 2010）
- 大质量晕（$> 10^{12}\,M_\odot$）中恒星质量占比下降，恒星反馈效率下降

### 4. 作者的解释
§3.5 直接引用此图论证"AGN CR 加热在此 halo 质量范围内成为主导"。

### 5. 物理意义
- 为 §3.5 的 AGN–CR 反馈论证提供**质量尺度边界**
- 与 §3.2（恒星反馈主导的低质量晕）形成对照

## 3.6 作者的逻辑

```
§3.1 [ISM 电离] CR 电离维持磁场–气体耦合 → 支持恒星形成调节
  → §3.2 [银河风] CR 压力驱动外流（Eq. 62/63/64）→ 解决恒星形成熄灭
    → §3.3 [宇宙学尺度] CR 传输系数影响质量加载因子
      → §3.4 [CGM/ICM 冷相] 热不稳定性 + CR 塑造冷气体
        → §3.5 [大质量晕 AGN] AGN CR 加热解决冷却流问题
```

[INTERPRETATION] §3 的五个子节形成一个**尺度上升 + 机制升级**的链式结构：从"CR 电离 ISM"（微观、$10^1$–$10^2$ pc）→ "CR 驱动风"（星系尺度，kpc）→ "宇宙学 halo 中的 CR 风"（$\sim 100$ kpc）→ "CGM/ICM 冷相"（$\sim$ Mpc）→ "AGN 加热的星系团"（$\sim$ Mpc）。

## 3.7 我的理解

### 3.7.1 CR 驱动风与热驱动风的**关键物理差别**

[INTERPRETATION] Eq. 62 揭示了 CR 驱动风的核心优势：

| 特性 | 热驱动风 | CR 驱动风 |
|------|----------|----------|
| $c_{\text{eff}}^2$ 与密度关系 | $c_{\text{eff}}^2 \propto \rho^{2/3}$ | $c_{\text{eff}}^2 \propto \rho^{-1/3}$ |
| 膨胀时行为 | $c_{\text{eff}}^2$ 快速下降 | $c_{\text{eff}}^2$ 缓慢上升 |
| 能否达到临界点 | 否（被引力势压过） | 是（Eq. 62 右端变正） |
| 能量储存时标 | $\sim 10^7$ yr（辐射冷却） | $\sim 10^9$ yr（CR 冷却） |

[INTERPRETATION] 这正是"CR 反馈是慢热机制"（overview §INTERPRETATION）的物理根源：**CR 的冷却时标远长于热能**，因此 CR 能在膨胀风中的低密度区域仍然维持足够的压力支撑，推动风加速到超音速。

### 3.7.2 [CRITIQUE] 关于 CR 驱动风的速度

[CRITIQUE] 论文指出 Ptuskin et al. (2008) 和 Recchia et al. (2016, 2017) 等研究在自洽计算 CR 谱时发现：**快 advection 导致 CR 谱在 $E \gtrsim 200$ GeV 时比观测更硬**。这暗示"CR 驱动风的能量预算"可能需要更多来自 GeV 区间 CR 的贡献，而 TeV 区间 CR 的约束更强。

[CRITIQUE] 作者指出"ion-neutral friction"和"非平衡 CR 传输"能显著修正结果（Thomas et al. 2023），但这些修正尚未系统纳入 galactic wind 模拟，属于未来工作方向。

### 3.7.3 [CRITIQUE] AGN 加热机制的**未定问题**

[CRITIQUE] §3.5 列举了四种 AGN 能量热化机制（声波耗散、重力波湍流耗散、lobe 混合、CR 加热），但明确承认"which of the above processes represents the dominant mode of heating in massive halos"仍是开放问题。

[CRITIQUE] 作者强调**自调节**（self-regulation）是成功 AGN 反馈模型的核心要求，但没有给出"CR 加热是否比声波耗散更易实现自调节"的定量比较。

### 3.7.4 §3 与 §4 的接口

[INTERPRETATION] §3 中建立的物理预期（galactic winds 速度、CR 谱、AGN 加热率、冷气体质量占比）在 §4 Observational signatures 中将逐一与**实际观测**对照：

- §3.2（wind）→ §4.2（银河系外流观测：Fermi bubbles, eROSITA bubbles）
- §3.3（cosmological winds）→ §4.3（extragalactic non-thermal emission）
- §3.4（CGM/ICM 冷相）→ §4.4（CGM 观测特征）
- §3.5（AGN CR）→ §4.5–§4.6（星系团 CR 观测 + AGN jet CR）

## 3.8 潜在问题与值得关注的地方

### 3.8.1 CR spectrum in wind 的观测约束

[CRITIQUE] §3.2 明确提到 Ptuskin et al. (2008) 和 Recchia et al. (2016, 2017) 的 CR 谱计算与观测不一致（too hard at $\gtrsim 200$ GeV）。这是一个**尚未解决的理论问题**：如果 CR 驱动风模型不能自洽地复现观测到的 CR 谱，其对外流动力学的定量预测也存在系统误差。

### 3.8.2 Cloud survival 的定量标准

[CRITIQUE] §3.4 讨论了冷云团在 CGM 中的四种存活机制，但每种机制的**定量适用条件**（如"CR 加速是否比 radiative cooling 快"）没有统一给出。这给 CGM 冷气体质量占比（up to 50%）的预测引入了较大的模型不确定性。

### 3.8.3 Gray CR 近似 vs. 多能量 CR 流体

[CRITIQUE] §3.3 讨论了 gray approximation 的局限性，并引用 Girichidis et al. (2023) 指出矮星系中 mass loading factor 可下降 4 倍。这意味着：

- 当前多数 cosmological simulations 的 CR 反馈结果**可能高估了矮星系的 outflow 效率**
- 未来模拟需要使用**多能量 CR 流体**以获得可靠的矮星系反馈预测

### 3.8.4 AGN–CR 耦合的观测区分

[CRITIQUE] §3.5 承认 AGN 加热的四种机制难以通过当前观测（X-ray 温度和熵 profile）区分。需要**多信使**观测（γ 射线、中微子、CR 直接测量）才能分离各机制的贡献。这为 §4.7 Current and future multi-messenger observatories 做了铺垫。

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
  - "ν_ph ≈ 320 E_1² B_10 MHz (synchrotron)"
keywords:
  - galactic winds
  - Breitschwerdt flux tube
  - CGM/ICM cold phase
  - AGN thermalization
  - self-regulation
  - cloud survival
  - gray approximation
references_internal:
  prev_chapter: 02_physics
  next_chapter: 04_observational_signatures
```

**引用页码**：全文引用基于 *A&A Reviews 31:4 (2023)*，pp. 61–139。
