> 本章属于：The Nine Lives of Cosmic Rays in Galaxies（Grenier, Black & Strong 2015）
>
> 上一章：[[02_cosmic-ray-origins/0006_grenier-2015/literature_analysis/02_direct_measurements.md|02_direct_measurements.md]]
>
> 下一章：[[02_cosmic-ray-origins/0006_grenier-2015/literature_analysis/04_crwanderers.md|04_crwanderers.md]]

# 3. ADVANCES IN COSMIC-RAY PROPAGATION

**[FACT]** 一次 CR 核子在 ISM 中通过散裂产生次级核子。次级产生率可用一次谱与散裂截面计算，因此次级/初级比是检验 CR 传播模型并约束传播过程中再加速程度的关键手段。次级也包括反质子和正电子。精确的反质子测量来自 BESS 与 PAMELA（见表 1）。

**[FACT]** B/C 随动量下降 → $D_{xx}(p)$ 随 $p$ 增大。将 $D_{xx}(p)$ 表示为幂律，指数范围 **0.3–0.8**（取决于模型）。该指数解释了 SNR 逃逸谱（$\sim 2.2$）与 ISM 观测谱（$\sim 2.7$）的差异。

**[FACT]** B/C 谱在 >20 GeV 处显示显著弯曲。三种可能解释：
1. 银盘与 halo 之间不同 MHD 湍流水平的扩散差异（Evoli & Yan 2014）；
2. 从 CR 自生成 Alfvén 波扩散 → 环境湍动扩散的转变（Aloisio & Blasi 2013）；
3. CR 源内部效应（银河系 CR 路过时的再加速、SNR 内部散裂）→ 探测平均停留时间和源内气体密度（Berezhko et al. 2003）。

**[FACT]** 放射性次级 **$^{10}{\rm Be}$**（半衰期 1.6 Myr）对银河系内停留时间敏感。$^{10}{\rm Be}/^{9}{\rm Be}$ 约束 **CR halo 标高高 4–10 kpc**（Strong 2007; Putze 2010; Trotta 2011）。ISOMAX 测量（Hams 2004）在 ≤2 GeV 给出略高于模型预测的 $^{10}{\rm Be}/^{9}{\rm Be}$ 值，但**尚未被重复**（第二次飞行失败）。

### 3.0.1 Parametric studies of cosmic-ray propagation

> **宇宙线传播的参数化研究**

**[FACT]** 使用 USINE 代码 + 贝叶斯 Markov 链蒙特卡洛技术的系统参数研究（Maurin et al. 2010; Putze et al. 2011; Lavalle et al. 2014）显示：

- $D_{xx}(p)$ 的很宽动量依赖范围都可拟合 B/C（部分因对流被包含在内，允许更大范围的模型）；
- 不同一次核子的谱差异**自然归因于传输效应**；
- 次级正电子排除 $D_{xx}(p)$ 非常陡峭的变。

**[FACT]** 这些分析及 Trotta et al. (2011) 的工作展示了贝叶斯方法在约束此类多参数问题的优势。

### 3.0.2 Diffusive reacceleration and alternatives

> **扩散再加速及替代方案**

**[FACT]** 扩散再加速 = 动量空间扩散，源于粒子在运动散射体上的动量获得与损失；因此 $D_{pp}$ 与 $D_{xx}$ 存在基本关系（Strong et al. 2007）。Thornbury & Drury (2014) 给出了再加速公式的清晰推导，并阐明其与原始 Fermi 二阶机制的关系。

**[FACT]** 再加速被频繁包含在模型中，因为它：
- 无需在 $D_{xx}(p)$ 中引入 ad-hoc 断点即可解释 B/C 的动量依赖；
- 与 Kolmogorov 湍流的 $D_{xx}(p) \propto p^{1/3}$ 一致。

**[CRITIQUE]** 再加速的重要性存在争议：
- 大再加速模型从 ISM 本身注入大量能量到 CR 中 → CR 加速不止来自 SNR 等标准源 → 能量来源问题未解；
- **同步辐射谱**（特别是低频）对 GeV 量级电子/正电子谱敏感，再加速水平常与低频频谱不兼容（§7.2 讨论）；
- **次级反质子**：拟合 B/C 的再加速模型在 <几 GeV 低估反质子。

**[FACT]** 无再加速模型的问题：需要在 $D_{xx}(p)$ 中引入非常大的断点（Strong & Moskalenko 1998），或额外的速度依赖（Ptuskin 2006），或 MHD 波耗散。

**[FACT]** B/C 对模型的约束对太阳调制水平敏感：通常采用 $\Phi \sim 500$ MV；若调制较低（Lave et al. 2013 用 250 MV），张力可缓解。

**[FACT]** 对流在 sub-GeV/n 能段起作用，给出与能量无关的逃逸时间。Voyager 1 数据被 Schlickeiser et al. (2014) 用作银河系风的证据（1D 传输模型）。

### 3.0.3 Secondary production in cosmic-ray sources

> **宇宙线源中的次级产生**

**[FACT]** 过去假设 B/C、正电子、反质子谱全部在 ISM 中产生；实际上有些次级在 CR 源内产生后初级逃逸 → 额外通量使图像复杂化。

**[FACT]** Berezhko & Ksenofontov (2014) 计算 SNR 中的反质子和 B 产生，与 PAMELA/AMS-02 对比。

**[FACT]** Mertsch & Sarkar (2014) 计算邻近遗迹中的次级正电子产生，并与 B 和反质子产生关联，可供未来数据检验。

## 3.1. Advances in Propagation Physics
**粒子传播物理的进展**

> **传播物理的进展**

**[FACT]** 关键发展：**显式计算磁化 ISM 中带电粒子轨迹**（Giacalone & Jokipii 1994, 1999），超越准线性理论近似。涉及 Lorentz 力与 Maxwell 方程：
- 湍动磁场建模为具有幂律谱的模式叠加，使用 Alfvén 波（时间依赖），加上规则场；
- 计算大量粒子轨迹 → 统计性质（扩散张量等）；
- **发现：垂直于磁场的扩散系数远小于平行的**。

**[FACT]** Casse et al. (2002) 扩展到更高能量和广泛环境（SNR, 超泡, 射电星系）。

**[FACT]** Lazarian & Yan (2014)：**超扩散（superdiffusion）**——因场线发散而比经典扩散快——在 CR 源区域可能重要。

### 3.1.1 Cosmic-ray penetration into molecular clouds

> **宇宙线对分子云的穿透**

**[FACT]** Fatuzzo et al. (2010) 与 Fatuzzo & Melia (2014) 在 MHD 湍动中做粒子轨迹数值实验，目标为获得扩散系数的标度关系。**结论**：强湍动下显著偏离准线性理论结果。

**[FACT]** 观测表明 >1 GeV CR 的扩散长度超过典型云尺寸（Abdo et al. 2010b; Ackermann et al. 2011b），但 <1 GeV 能区（对电离和化学关键、$\gamma$ 射线不可见）可被多种机制调节。

**[FACT]** 排除机制：
1. **共振散射在自生成的磁不规则性上**（CR streaming 激发）：Cesarsky & Volk (1978) 指出维持 Alfvén 波对抗中性电离摩擦所需功率过大；
2. **致密气体中增加的电离损失** → 净向内 CR streaming 通量 → 云边缘到云间介质连线上的 Alfvén 波阻止 CR 穿透 → 在几十 MeV 处压制通量数个量级（Cesarsky & Volk 1978; Skilling & Strong 1976）。
   - 但 Everett & Zweibel (2011) 预测在 GeV 能量处仅有 **7.5%** 的 CR 压力下降（即使热扩散电离层 → 冷致密云极端过渡）。

**[FACT]** 亚秒差距核心的磁场结构导致 CR **排除（磁镜）**或**聚集（磁聚焦）**：
- 排除主导多数核心构型 → 电离 CR 密度减少 2–4 倍（Padovani & Galli 2011）；
- 收缩前恒星核心中心离子化率可降至 $<10^{-18}$ s$^{-1}$（Padovani 2013）。

**[FACT]** CR 在致密核心间的磁场瓶中被困住 → 局部 $\gamma$-ray emissivity $q_\gamma^H$ 可能增加：
- 预测增加 3–5 倍（Cesarsky & Volk 1978）；
- 数值模拟表明 TeV 粒子有效散射于磁湍动 → 在云的均匀+湍动场中平滑扩散（Fatuzzo 2010）。

**[FACT]** >1 GeV 时所有聚集/排除过程均未在当前 $\gamma$ 射线数据中显示能量依赖特征 → **支持用 CR 强子作用 + $\gamma$ 射线示踪所有形式气体**。

## 3.2. Advances in Propagation Models
**传播模型的进展**

> **传播模型的进展**

**[FACT]** 主要工具：

| 代码 | 特点 |
|------|------|
| **GALPROP**（Strong 2007+） | 公共软件（galprop.stanford.edu）；经典，多数研究基于它；2D 圆柱对称性为主 |
| **DRAGON**（Evoli & Yan 2014; Gaggero et al. 2014） | 扩展到各向异性、空间依赖扩散，与 MHD 湍动水平相关（dragonproject.org） |
| **USINE** | 半解析；快速，适合参数探索（Putze 2011） |
| **PICARD**（Kissmann 2014; Werner 2013,2015） | 全 3D，10-pc 分辨率可处理螺旋结构 |

**[FACT]** 局限性：精度、速度、空间分辨率；需加入银河系风、边界条件、与河外介质连接等物理。

**[FACT]** Everet et al. (2012) 的 X 射线观测支持银河系风的存在。Uhlig et al. (2012) 研究了 CR streaming 驱动的银河系风。

**[FACT]** GALPROP 等仍是"唯象的"：参数化扩散/对流，未做物理层面处理；CR 作为测试粒子；未包含 CR 对 ISM 的动力学效应。

**[FACT]** 替代：**CR 相对论流体 + MHD 处理**（Hanasz 2009, 2012; Wóltański 2013）——用 PIERNICK 程序研究 **CR 驱动 dynamo** 生成银河系磁场。

**[FACT]** 100 pc 尺度：Girichidis et al. (2014) 用 FLASH 研究 SNR 逃逸 CR 对周围 ISM 的动力学影响（各向异性传播，周围气体被加速）。

**[FACT]** 核截面精度限制次级研究：
- Moskalenko (2011) 改进倡议；
- Coste et al. (2012) 处理轻核（$Z \le 2$）复杂过程；
- 反质子产生需改进（Kappl & Winkler 2014）；
- 强子 $\gamma$ 射线与轻子产生也有挑战（Dermer 2013a）。

## Figure 3 — 传播模型对比



**[FACT]** 目的：(a) 展示主核子谱 + B/C 传播模型的拟合；(b) B/C 随动量演化比较 3D 传播模型（不同 $D_{xx}$ 动量依赖）。

**[FACT]** 元素：
- **Panel (a)**：$E^3 J(E_{\rm kin})$ [GeV m$^{-2}$ s$^{-1}$ sr$^{-1}$] vs $E_{\rm kin}$ [GeV/nuc]；模型 = KOL（Kolmogorov 湍动）、KRA（Kraichnan 湍动）、PD（无再加速的纯扩散）；数据 = p PAMELA 09-10、p AMS-02 (preliminary)、He PAMELA 06-08；
- **Panel (b)**：B/C vs $E_{\rm kin}$；数据 = AMS-02 (preliminary)、PAMELA (preliminary)。

**[FACT]** 关键观察：
- 三个模型（KOL, KRA, PD）都能拟合 B/C 曲线；
- 说明 3D 扩散处理 + 源分布的螺旋结构可解释 AMS-02 与 PAMELA 数据；
- <几 GeV 处太阳调制对预测重要。

**[INTERPRETATION]** 说明参数简并：多种模型都能拟合 B/C，需要反质子、正电子等独立探针打破简并。

## 关键公式与量级



- $D_{xx}(p)$ 幂律指数：**0.3–0.8**
- $^{10}{\rm Be}$ 半衰期：**1.6 Myr**
- CR halo 标高：**4–10 kpc**
- 太阳调制 $\Phi$：**250–500 MV**
- Kolmogorov：$D_{xx} \propto p^{1/3}$
- Everett & Zweibel (2011)：GeV CR 压力下降 **7.5%**（极端过渡）