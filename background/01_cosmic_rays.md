---
title: 01_cosmic_rays
category: 背景知识
status: completed
read_date: '2026-08-12'
lastread: '2026-08-12'
tags:
- '01'
- cosmic
- rays
citations: []
path: background/01_cosmic_rays.md
---
# 1. 宇宙线物理（背景知识体系）

> 本综述整合 8 篇核心文献的精确精读分析，覆盖银河系宇宙线（GCR）传播、加速、观测约束、超高能宇宙线（UHECR）起源、以及宇宙线与星系的相互作用。主要参考文献包括 Strong, Moskalenko & Ptuskin (2007, RMP 79:2451)、Bhattacharjee & Sigl (1999, Phys. Rep. 320:1)、Al-Dargazelli et al. (1996)、Gaisser (1990)、Blasi (2013, A&AR 21:70)、Amato (2014, arXiv:1406.7714)、Grenier, Black & Strong (2015, ARA&A 53:199)、Biermann (1996, astro-ph/9609110)。

## 1.1 传播理论

### 1.1.1 传播方程

宇宙线传播的核心方程由 Strong, Moskalenko & Ptuskin (2007) 系统总结，描述单位动量 $p$ 的宇宙线密度 $\psi(\vec{r}, p, t)$ 的演化：

$$
\frac{\partial \psi(\vec{r}, p, t)}{\partial t} = q(\vec{r}, p, t) + \nabla \cdot (D_{xx} \nabla \psi - \vec{V} \psi) + \frac{\partial}{\partial p} p^2 D_{pp} \frac{\partial}{\partial p} \frac{1}{p^2} \psi - \frac{\partial}{\partial p} \left[ \dot{p} \psi - \frac{p}{3} (\nabla \cdot \vec{V}) \psi \right] - \frac{1}{\tau_f} \psi - \frac{1}{\tau_r} \psi
$$

各项物理意义：

| 项 | 符号 | 物理含义 |
|---|---|---|
| 源项 | $q(\vec{r}, p, t)$ | 初级注入 + 碎裂产生 + 衰变贡献之和 |
| 空间扩散 | $D_{xx}$ | 空间扩散系数，依赖 $(\vec{r}, \beta, p/Z)$，其中 $p/Z$ 为磁刚度 $R$ |
| 对流 | $\vec{V}$ | 银河风速度，向外平流 |
| 动量空间扩散（再加速） | $D_{pp}$ | 随机加速（见 §1.1.4） |
| 能量损失/增益 | $\dot{p} = dp/dt$ | 同步辐射、逆康普顿、电离、绝热损失 |
| 绝热项 | $\frac{p}{3}(\nabla \cdot \vec{V})\psi$ | 不均匀流中的绝热能量变化 |
| 碎裂 | $\tau_f$ | 由总碎裂截面和 $n(\vec{r})$ 决定 |
| 放射性衰变 | $\tau_r$ | 放射性同位素半衰期决定的衰变时标 |

Gaisser (1990) 给出与上述等价的平衡方程形式，用于反质子研究：

$$
\frac{dJ_{\bar{p}}(E)}{dt} = 0 = Q_{\bar{p}}(E) - \frac{1}{\tau_R(E)} J_{\bar{p}}(E) - \frac{1}{\tau_I} \left[ J_{\bar{p}}(E) + \int_0^{\infty} \frac{d\sigma_{\bar{p}}}{dE'}(E,E') J_{\bar{p}}(E') dE' \right] + B \int_0^{\infty} \frac{dP(E,E')}{dE} J_{\bar{p}}(E') dE'
$$

在稳态 ($\partial \psi / \partial t = 0$) 下，源分布一般假设为银河盘附近，径向分布类似超新星遗迹（SNR）的分布。

### 1.1.2 扩散系数 $D_{xx}$

从宇宙线数据拟合得到的典型值：

$$
D_{xx} \sim (3-5) \times 10^{28} \text{ cm}^2 \text{s}^{-1} \quad \text{at energy} \sim 1 \text{ GeV/n}
$$

**准线性理论（QLT）**：微观上扩散来自粒子在随机 MHD 波上的共振散射。共振条件为

$$
k_\parallel = \pm s / (r_g \mu), \quad s = 0, 1, 2, \dots
$$

一阶共振 $s=1$ 最重要，理论估计：

$$
D_{xx} \approx (\delta B_{\rm res}/B)^{-2} v r_g / 3
$$

其中 $r_g = p/(ZeB)$ 为回旋半径，$\delta B_{\rm res}$ 为共振波数 $k_{\rm res} = 1/r_g$ 处的随机场幅度。

**Kolmogorov vs. Kraichnan 谱**：

| 谱类型 | 指数 $a$ | 扩散标度 | 对应场景 |
|---|---|---|---|
| Kolmogorov | $1/3$ | $D_{xx} \sim R^{1/3}$ | 低能区、经验模型（含再加速） |
| Kraichnan | $1/2$ | $D_{xx} \sim R^{1/2}$ | 高能极限、plain diffusion 模型 |

经验拟合给出 $D_{xx}$ 随磁刚度按 $R^{0.3} - R^{0.6}$ 增加。Bhattacharjee & Sigl (1999) 在准线性框架下给出 ISM 中 $D(1\,{\rm GeV}) \sim 10^{29}$ cm$^{2}$/s 时共振尺度 $\delta B/B \sim 6 \times 10^{-4}$。

Biermann (1996) 采用 Kolmogorov 谱，得到相对论区逃逸时标 $\tau_{L,\rm gal} \propto E^{-1/3}$；在云捕获+非定态模型下，次级/初级比可达 $E^{-2/3}$，与 B/C $\sim E^{-0.6}$ 一致。

### 1.1.3 对流（银河风）

- **1-zone 模型**：对流和扩散处处存在；
- **2-zone 模型**：距盘面 $|z| < 1$ kpc 仅扩散，以外扩散+对流。

纯对流传输对次级/初级比没有能量依赖性，与观测矛盾。放射性同位素约束风速度 $< 10$ km s$^{-1}$ kpc$^{-1}$（线性增加风）。B/C 拟合需要约 $15$ km s$^{-1}$ 的恒定速度风。

自洽模型（Ptuskin et al.）：CR 和热气体驱动的银河风 2-zone 模型，外区对流速度高达 $100$ km s$^{-1}$，不与放射性核素冲突（因为约束仅适用于内区）。

Gaisser (1990) 讨论的 **Jokipii & Morrill (1987) 银河星风终止激波模型** 可加速到 $10^{19}–10^{20}$ eV。

### 1.1.4 再加速（动量空间扩散）

动量空间扩散系数通过 Alfvén 波与 $D_{xx}$ 关联：

$$
D_{pp} = \frac{p^2 V_a^2}{9 D_{xx}}
$$

其中 $V_a = B/\sqrt{4\pi \rho}$ 为 Alfvén 速度，ISM 中典型值 $V_a \sim 30$ km/s。

**再加速作为主加速机制的检验**：如果分布再加速在全部银河系体积内进行，高能粒子停留时间更长，次级丰度随能量增加，与观测矛盾——故分布再加速**不能**作为 1–100 GeV/n 的主加速机制。但低能区分布再加速可很强，解释次级/初级比在约 1 GeV/n 处的峰值。

**波阻尼效应**：在小尺度（$< 10^{13}$ cm）的 Kraichnan 非线性级联受到 CR 耗散影响，导致 $D_{xx}$ 在小刚度处急剧上升，自洽变化解释 $D_{xx} \sim R^{0.5}$ 的高能标度。

**K-俘获同位素检验**：$^{37}{\rm Ar}$、$^{44}{\rm Ti}$、$^{49}{\rm V}$、$^{51}{\rm Cr}$ 等通过电子俘获快速衰变，丰度对能量变化敏感。$^{51}{\rm V}$/$^{52}{\rm Cr}$ 与再加速模型更符合，但 $^{49}{\rm Ti}$/Ti 结果相反——**直接证据尚不明确**，主要困难在核碎裂截面精度。

### 1.1.5 能量损失

- **同步辐射**：电子在磁场中辐射，$\dot{E} \propto B^2 E^2$。同步辐射谱指数 $\beta_\nu = (\gamma - 1)/2$，观测 $\beta_\nu = 0.6-1$ 对应注入谱指数 $\gamma = 2.4-3$。
- **逆康普顿散射**：电子与 ISRF（星际辐射场，覆盖远红外到紫外）和 CMB 相互作用。高纬度处逆康普顿贡献很大，是 CR 晕延伸至盘面以上数 kpc 的独立证据。
- **电离损失**：$\sim n_e, n_H \cdot \beta^2 \cdot Z^2$，仅对亚相对论速度有效。质子谱在银河系中形成低能截止，H 的截止能 $\sim 100$ MeV，更重核相应更高。
- **绝热损失**：在膨胀激波或银河风中，$dE/dt \propto -\nabla \cdot \vec{V} \cdot E/3$。
- **电子能量损失特征**：Blasi (2013) 给出在 Bohm 极限下同步辐射损失时标 $\tau_{\rm syn} = 4 \times 10^{10} B^{-2}_{100} E^{-1}_{\rm TeV}$ s；最大电子能量 $E_{e,\max} \approx 34 B^{-1/2}_{100} V_{\rm sh,8}$ TeV。

电子总能量损失中约 **60% 在银河系内沉积**（Grenier 2015：银河系是"公平的电轻量热器"），而质子仅 **约 10% 通过强子反应损失**，大部分逃逸到星系际空间。

### 1.1.6 核碎裂与次级核产生

**碎裂（spallation）**：宇宙线核与 ISM 中 H、He 碰撞，碎裂产生轻次级核（B 来自 C, N, O 碎裂）。B/C 比观测给出 $X(R)$（逃逸长度）：

$$
X(R) = \frac{\beta}{\beta_0} X_0 \left(\frac{R}{R_0}\right)^{-\alpha}, \quad \text{典型：}\alpha = 0.54, X_0 = 11.8\ {\rm g/cm^2}, R_0 = 4.9\ {\rm GV}
$$

**三种碎裂位点**（Biermann 1996）：

1. **分子云壳层**：grammage $\sim 1$ g/cm$^{2}$，次级/初级比 $N_s/N_p \sim$ const.（Regime 1）
2. **星际云内（扩散主导）**：在云形成（引力坍缩快于 Alfvén 速度，CR 被捕获）的非定态框架下，$N_s/N_p \sim E^{-2/3}$（Regime 2，与观测 $\sim E^{-0.6}$ 一致）
3. **非扩散高能区（经典解）**：$N_s/N_p \sim E^{-1/3}$（Regime 3，从未成为主导）

Regime 1→2 切换在约 **20 GeV/n** 附近。

**反质子**：最小产生过程 $p + H \to p + p + p + \bar{p}$，阈值 **5.63 GeV**，截面在 100 GeV 约 1 mb，1 TeV 约 5 mb。源谱产额集中在 **1.5–15 GeV**。由于反质子产生截面能量依赖性远强于碎裂反应，反质子对源谱形状、再加速、传播的响应与次级核显著不同，形成**互补探针**。

**Li、Be、B 丰度**：这些元素在恒星内部被破坏（低聚变阈值），主要由 CR 散裂产生。$^{7}{\rm Li}$/$^{6}{\rm Li}$ 在星际介质中测得约 **2**（太阳系为 12.3），直接显示**最近散裂产生 Li** 的证据。

### 1.1.7 数值模型（GALPROP 等）

**GALPROP**（Strong & Moskalenko 1998, ApJ 509:212）：
- 在空间网格上数值求解传播方程 (1)，支持 2D（轴对称）或完整 3D；
- 从最重初级核（如 $^{64}{\rm Ni}$）开始，逐步向下计算碎裂源项，直至质子、次级电子/正电子和反质子；$^{10}{\rm B}$ 通过 $^{10}{\rm Be}$ 衰变产生，需第二次迭代；
- 输入物理包括碎裂截面汇编、ISRF 模型、K-俘获与电子剥离过程；
- 输出：所有物种在网格上的谱 + $\gamma$ 射线和同步辐射全天图；
- 被 NASA 的 GLAST（费米）采纳为弥散银河 $\gamma$ 射线辐射的标准。

**已知局限**：能量低于 $10^{15}$ eV（无轨迹计算）；均匀的源丰度（无 superbubble 增强）；仅 $>10$ pc 尺度（无 clumpy ISM）；同步辐射中 B 场视为随机。

**解析与半解析方法**：
- **泄漏盒模型**：$G(x) \propto \exp(-x/X)$，平均 grammage 等于逃逸长度 $X$。
- **加权板方法**：核碎裂在板模型中求解，用 $G(x)$ 加权积分。在扩散系数可分离依赖能量和位置且无对流的特殊情况下严格。
- **显式解析解**：含能量损失和再加速，通过路径长度分布 (PLD)；无法正确处理电离损失。

Grenier (2015) 指出当前传播建模的四个警示：(1) $D_{xx}(p)$ 的动量依赖与源谱之间存在简并；(2) MHD 湍动水平强烈影响扩散性质；(3) 到达地球的核子 > 一半在 1–2 kpc 内产生；(4) 本地 ISM 特性（Gould Belt、空洞烟囱）可严重改变局部丰度。

## 1.2 加速机制

### 1.2.1 扩散激波加速（DSA）

**基本原理**：粒子在激波上下游来回穿越（"一阶 Fermi 加速"），单次循环的能量增益

$$
\left\langle \frac{\Delta E}{E} \right\rangle = \frac{4}{3} \beta, \quad \beta = V_{\rm sh}/c
$$

标度为 $\beta^1$，故称"一阶"；对比二阶 Fermi 加速的 $(V/c)^2$。

**DSA 传输方程**（Skilling 1975a，shock 静止、平行、定态）：

$$
u \frac{\partial f}{\partial z} = \frac{\partial}{\partial z}\left(D \frac{\partial f}{\partial z}\right) + \frac{1}{3}\frac{du}{dz} p \frac{\partial f}{\partial p} + Q
$$

注入项 $\delta$ 函数近似 $Q(p,z) = \eta n_1 u_1 / (4\pi p^2_{\rm inj}) \cdot \delta(p-p_{\rm inj})\delta(z)$。

**test-particle 动量谱**：

$$
f_0(p) = \frac{3r}{r-1} \eta n_1 \frac{1}{4\pi p^2_{\rm inj}} \left(\frac{p}{p_{\rm inj}}\right)^{-\frac{3r}{r-1}}
$$

其中 $r = u_1/u_2$ 为压缩比。强激波极限 $r \to 4$：

$$
\alpha = \frac{3r}{r-1} \xrightarrow{r \to 4} 4
$$

动量谱 $f(p) \propto p^{-4}$，在相对论下对应能量谱 $dN/dE \propto E^{-2}$。**谱与扩散系数 $D$ 无关**（"好消息"），但 $p_{\max}$ 由 $D$ 决定（"坏消息"）。

**压缩比**：$r = 4M_s^2/(M_s^2 + 3)$，强激波 $r \to 4$。

**加速时间**：

$$
\tau_{\rm acc} = \frac{3}{u_1 - u_2} \int_0^p \frac{dp'}{p'} \left[ \frac{D_1(p')}{u_1} + \frac{D_2(p')}{u_2} \right]
$$

**三种最大能量定义**（Blasi 2013）：
1. **时间约束**：$\tau_{\rm acc}(p_{\max}) \le \tau_{\rm SNR}$
2. **空间约束**：$D(p_{\max})/V_{\rm sh} \approx \chi R_{\rm sh}$（Sedov 阶段更严）
3. **几何约束**：$r_L(p_{\max}) = R_{\rm sh}$（作为上界）

回旋半径参考值：$r_L(p_{\max}) = 1\ {\rm pc} \cdot (E/10^{15}\ {\rm eV}) \cdot B^{-1}_{\mu}$。

**SNR 要达到 PeV 的 PeVatron 条件**：由于 $c/V_s \sim 100$ 而 $r_L/R_{\rm SNR} \sim 0.1$，必须 $\delta B/B_0 \gg 1$。即需要磁场放大（MFA）~10–100 倍。若 $D(E)$ 取 ISM 值 $3 \times 10^{28} (E/10\ {\rm GeV})^\delta$ cm$^{2}$/s，则加速时标远超自由膨胀期。

Bohm 极限下加速时标：$\tau_{\rm acc} \approx 3.3 \times 10^7 E_{\rm TeV} B^{-1}_{100} V^{-2}_{\rm sh,8}$ s。代入 $B = 100\ \mu$G，$T_s = 300$ yr：

$$
E_{\max} \approx 3 \times 10^5\ {\rm GeV} \cdot B_{100} \cdot (T_s/300\ {\rm yr}) \cdot (V_{\rm sh}/1000\ {\rm km/s})^2
$$

Blasi (2013) 明确指出："All parameters have to be chosen in the most optimistic way so as to maximize $E_{\max}$."

**Bhattacharjee & Sigl (1999) 的 benchmark 估计**：

$$
E_c \equiv E_{q=3} \sim 10^{17} \cdot Z \cdot (R/\text{kpc}) \cdot (B/\mu\text{G})\ {\rm eV}
$$

**Hillas 判据**（筛选候选源）：

$$
(B/\mu\text{G}) \cdot (R/\text{kpc}) > 2 \cdot (E/10^{18}\ {\rm eV}) \cdot 1/(Z\beta)
$$

**Gaisser (1990) 的加速上限**（最小散射长度近似）：

$$
E_{\max} \approx \frac{3 u_1 Z e B (\tau_u \tau_A)}{20 c} \sim 10^{14} Z\ {\rm eV} \quad (B = 3\ \mu\text{G}, u_1 = 10^9\ \text{cm/s}, \tau_A = 10^3\ \text{yr})
$$

### 1.2.2 非线性 DSA（NLDSA）

Test-particle 假设 $\xi_{\rm CR} \ll 1$（宇宙线能量份额）。实际上 SNR 中 $\xi_{\rm CR} \sim 10\%$（甚至到 $50\%$），必须考虑非线性效应。

**三条需要 NLDSA 的理由**：
1. **加速粒子对激波的动量反馈**：$\xi_{\rm CR} \sim 10\%$ → CR 压力改变压缩比，谱变为刚度依赖；
2. **CR 诱导的不稳定性（磁化放大）**：既是 X 射线窄边缘的原因，也是缩短加速时间的必要条件；
3. **放大磁场对激波的反向作用**：几百 $\mu$G 的磁场压力虽为 $\rho v_s^2$ 的 $10^{-2}-10^{-3}$，但可远大于上游热压，进而影响 $r$。

**Precursor + subshock 结构**：

CR 压力在上游造成**precursor**（流体减速），深度

$$
\xi_{\rm CR}(z) \approx P_c(z)/($\rho$_0 u_0^2) \approx 1 - u(z)/u_0
$$

守恒方程：质量 $ρu = $ const；动量 $ρu^2 + P_g + P_c = $ const；能量 $ρε + P_g + E_c = $ const（含 CR 能量通量）。CR 能量方程：

$$
\frac{\partial E_c}{\partial t} + \nabla \cdot \left(\frac{\gamma_c}{\gamma_c - 1} u P_c\right) = \nabla \cdot (\bar{D} \nabla E_c) + u \nabla P_c
$$

准稳态下子激波压缩比 $R_{\rm sub}$ 用 $M_1$ 表达；总压缩比 $R_{\rm tot} = u_0/u_1$。**典型结构**：$R_{\rm sub} < 4 < R_{\rm tot}$，CR 诱导 precursor 深度由 $ξ_{\rm CR}$ 决定。

**谱的凹性（concavity）**：低动量粒子经历的压缩因子接近 $R_{\rm sub} < 4$，高动量粒子接近 $R_{\rm tot} > 4$。因此谱在低能段更陡（接近 $R_{\rm sub}$），高能段更硬（接近 $R_{\rm tot}$），转折在 **~GeV/c**。

**计算 NLDSA 的三种方法**：有限差分（Berezhko & Völk；Zirakashvili & Ptuskin）；Monte Carlo（Ellison & Eichler；Knerr）；半解析（Malkov；Blasi 2002；Amato & Blasi）。

Amato (2014) 强调**逃逸粒子**的作用：高能粒子逃逸到 SNR 外部可形成"辐射型"激波行为，$R_{\rm tot}$ 甚至可达 7。逃逸谱（escape spectrum）通过逆问题方法从观测到的银河系总谱反推，给出源注入谱的形状。

### 1.2.3 磁场放大（MFA）

SNR X 射线窄边缘观测（$10^{-2}$ pc 宽度）反推 B 场达 **几百 $\mu$G**（ISM 背景 1–6 $\mu$G），为 MFA 提供了关键证据。

**四种 MFA 机制**：

| 机制 | 增长速率 | 尺度 | 适用性 |
|---|---|---|---|
| **共振 streaming 不稳定性** | $\omega_I = (\pi/8)\Omega_p^*(V_{\rm sh}/v_A)(n_{\rm CR}/n_i)$ | $k \sim 1/r_L$ | $\xi_{\rm CR} \ll 8 \times 10^{-4}$ 才有效；对 $\xi_{\rm CR} \sim 10\%$ 完全不成立 |
| **Bell 非共振小尺度模** | $\omega \propto k^{1/2}$，峰值在 $k^* r_{L,0} = 3\xi_{\rm CR}\gamma_{\min}/\Lambda \cdot (V_{\rm sh}/v_A)^2(V_{\rm sh}/c) > 1$ | $k r_{L,0} > 1$（远小于粒子 $r_L$） | 增长快，但不能共振散射；非线性演化形成 flux tubes |
| **Filamentation 不稳定性** | $J \times B$ 力排斥等离子体 | 大尺度磁通管 | Caprioli & Spitkovsky (2013)：可能产生自洽的 self-confinement；Bell et al. (2013)：Tycho 参数下可达 ~200 TeV |
| **大尺度 firehose 模** | $\Gamma_{\rm FH} \approx \xi_{\rm CR}^{1/2} V_{\rm sh}^2 k / c$ | $k \ll 1/r_{L,\max}$ | $\Gamma_{\rm FH} \cdot \tau_{\rm adv}(p_{\max}) \ll 1$，时间不够 |

**高 $\xi_{\rm CR}$ 极限**：$\omega_I \approx \omega_R = [(\pi/8)\Omega_p^* k V_{\rm sh} n_{\rm CR}/n_i]^{1/2}$，$F_{0}$ 上限

$$
F_0(k) = (\pi/6)^{1/2} (\xi_{\rm CR}/\Lambda)^{1/2} (c/V_{\rm sh})^{1/2} \le 1
$$

即"efficient CR acceleration reduces the growth of the waves and limits the value of the self-generated magnetic field to the same order of magnitude as the pre-existing magnetic field."

**磁动力学反作用**（Amato 2014 修订）：R_tot–R_sub 关系

$$
R_{\rm tot}^{\gamma_g+1} = \frac{M_0^2 R_{\rm sub}^{\gamma_g}}{2[\gamma_g+1 - R_{\rm sub}(\gamma_g-1)]/(1+\Lambda_B)}
$$

其中 $\Lambda_B = W[1 + R_{\rm sub}(2/\gamma_g - 1)]$，$W = P_{w,1}/P_{g,1}$。X 射线边缘反推 B 给出 $W \sim 1-10$ → 磁反作用重要，已显著改善谱的凹性。

Amato (2014) 特别讨论了"强流区"色散关系的完整推导——标准增长率公式在此处误用，需要修订。

### 1.2.4 PeVatron 条件

**PeVatron**（$E \ge 1$ PeV 加速器）：SNR 要达到 PeV 需满足：

1. **磁场放大**：$\delta B/B \gg 1$，Bohm 极限下；
2. **年龄-速度组合**：$E_{\max} \propto V_{\rm sh}^2 T_s$——年轻 SNR（如 Tycho, $V_{\rm sh} \sim 5000$ km/s）最优；
3. **注入效率**：$\xi_{\rm CR} \sim 10\%$ 已接近 test-particle 上限，必须用 NLDSA 处理。

Filamentation 不稳定性在 Tycho 参数下可达 ~200 TeV，距膝点差约一个量级。Blasi (2013) 指出 SNRs with even larger velocity (therefore much younger) may be responsible for acceleration of PeV CRs。

银河系 SN 供给功率 $\sim 3 \times 10^{42}$ erg/s（Gaisser 1990；Grenier 2015 给出总 CR 相关光度 $\sim 10^{41}$ erg/s），与观测 CR 能量密度 $\rho_E \approx 1$ eV/cm$^{3}$ 匹配。

## 1.3 观测约束

### 1.3.1 次级/初级比

**B/C 比**是传播模型拟合的核心参考量（B 完全为次级，测量精度优于其他比值，可延伸至 100 GeV）。C、N、O 是 B 的主要母核。

**Sub-Fe/Fe 比**（如 (Sc+Ti+V)/Fe）是独立约束。

经验逃逸长度模型：

$$
X(R) = \frac{\beta}{\beta_0} X_0 \left(\frac{R}{R_0}\right)^{-\alpha}
$$

典型拟合（Strong et al. 2007）：$\alpha = 0.54$，$X_0 = 11.8$ g cm$^{-2}$，$R_0 = 4.9$ GV，源谱刚度指数 $-2.35$。

**关键困境**：B/C 和 Sub-Fe/Fe 数据本身无法区分纯扩散、对流、再加速等多种模型——所有模型都能提供 adequate fit。必须结合多种观测才能约束模型。

**再加速方案**：再加速可重现 B/C 无需扩散系数中的 ad-hoc 转折；所需 $\alpha$ 值较小（0.3–0.4，与 Kolmogorov 湍流一致），有助于解决各向异性问题。

**观测到的低能下降**：B/C 在 1 GeV/n 以下的下降比仅 $\beta$ 依赖更快——这一现象是再加速或波阻尼方案的动机。

### 1.3.2 放射性时钟

利用长寿命放射性次级核素约束传播区域大小：

| 核素 | 半衰期 | 备注 |
|---|---|---|
| $^{14}{\rm C}$ | 5730 y | |
| $^{10}{\rm Be}$ | $1.51 \times 10^6$ y | 寿命最长、测量最好 |
| $^{26}{\rm Al}$ | $7.2 \times 10^5$ y | |
| $^{36}{\rm Cl}$ | $3 \times 10^5$ y | |
| $^{54}{\rm Mn}$ | $312 \times 10^3$ y | |

**核心约束**：基于这些同位素和更新截面，得到 **$z_h = 4-6$ kpc**。

**放射性时钟逻辑链**：
- $^{10}{\rm Be}$/$^{9}{\rm Be}$ 数据 → 局部扩散系数 $D_{xx} \approx (3-5) \times 10^{28}$ cm$^{2}$/s（在 3 GV）；
- 结合稳定次级/初级比 → 晕大小 $z_h \approx 4$ kpc；
- 泄漏盒"逃逸时间" $\approx 10^7$ yr（实际从源到晕边界时间约 10 倍）；
- 泄漏盒"气体密度" $\approx 0.3$ cm$^{-3}$（实际 4 kpc 晕的平均密度约 $0.03$ cm$^{-3}$）。

泄漏盒的"逃逸时间"和"气体密度"均比实际值高一个量级，**不能直接理解为物理量**。

**本地泡效应**：如果放射性次级在气体耗竭的本地泡产生，在到达地球前衰变 → 高估晕大小。

### 1.3.3 各向异性

**观测数据**：

| 能量范围 | 各向异性幅度 | 数据来源 |
|---|---|---|
| $10^{12}$–$10^{14}$ eV | $\delta \sim 10^{-3}$ | |
| $10^{16}$–$10^{18}$ eV | 几个 % | 统计量不足 |

**理论公式**（扩散近似）：

$$
\delta = -[3D \nabla f + u_p (\partial f / \partial p)] / vf
$$

**Compton-Getting 各向异性**（对于幂律谱 $I(E) \sim E^{-\gamma}$）：

$$
\delta_{\rm CG} = (\gamma + 2) u / c
$$

太阳系相对于本地 ISM 的运动产生 $\sim 4 \times 10^{-4}$ 的常数项，最大强度指向银河中心方向，但**与 $10^{12}$–$10^{14}$ eV 数据（指向反银心方向）不符**——对流效应被扩散各向异性压倒。

**模型与数据的比较**：
- **含再加速的扩散模型**与数据在约 3 倍因子内一致；
- **纯扩散模型**（$D \sim E^{0.54}$）预测 $E > 10^{14}$ eV 各向异性过大。

各向异性数据支持小 $\alpha$（$\sim 0.3$，含再加速方案），排除大 $\alpha$（$\sim 0.54$，纯扩散方案）。

**Al-Dargazelli (1996)** 在 UHE 能区的各向异性分析中确认：银河面增强随能量增长，振幅略小；"hot spots"（$\ge 4$ 个 $E > 10^{19}$ eV 粒子在 6° 内）为 EG 源的直接证据，|b| > 20° 的 clusters 最可能来自 EG 源。

### 1.3.4 伽马射线

**产生机制**（>100 MeV）：
1. **$\pi^0$ 衰变**：CR 质子和 He 与气体碰撞产生 $\pi^0 \to 2\gamma$，示踪强子；
2. **逆康普顿散射**：电子与 ISRF 相互作用，示踪轻子；
3. **轫致辐射**：电子与气体相互作用。

**GALPROP vs. EGRET 数据**：基于直接测得的 CR 谱 + 径向梯度，模型 $\gamma$ 射线谱在 1 GeV 以上**低于 EGRET 数据约因子 2**——揭示剩余的不确定性。

**GeV 过剩问题**：可能的激进修正方案：
- (i) 硬电子注入谱——需要大涨落，不太可能；
- (ii) 硬质子谱——被反质子数据排除（会产生太多反质子）；
- (iii) 暗物质起源——产生过多 CR 反质子；
- (iv) SNR 射电谱指数分散。

**高纬度逆康普顿辐射**是 CR 晕扩展到盘面以上数 kpc 的独立证据，与放射性核素约束一致。

**Grenier (2015) 的更新**：Fermi-LAT 数据显示 $q_{\gamma,H}$（每 H 核的 $\gamma$ 射线 emissivity）在银河系内**相当均匀**（变化 <30%），外臂仅降 20–40%。这确认**长存 CR 梯度问题**——外银 $q_{\gamma,H}$ 梯度与 $^{10}{\rm Be}$/$^{9}{\rm Be}$ 允许的最大晕大小 $\sim 10$ kpc 之间勉强一致。

**Fermi Bubbles**：发现于 2010 年（Su 2010），两个 $\sim 50°$ 直径、边缘锐利的椭圆区，向银极延伸数 kpc。$\gamma$ 射线辐射功率 **$2 \times 10^{30}$ W**；与银河核球发出的巨射电瓣部分重叠，磁场高达 **1.5 nT**，将 $10^{48}$ J 输送到 halo。双锥外流速度 >900 km/s。粒子性质（强子/轻子）仍未知。

### 1.3.5 反质子与正电子

**反质子**：
- 反质子谱在约 2 GeV 处峰值，低能急降（次级产生的运动学结果）；
- 次级反质子通量计算主要不确定性：(1) 截面不完整知识；(2) 传播参数和模型；(3) 日球层调制；
- 反质子产生**阈值 5.63 GeV**（Gaisser 1990），截面在 100 GeV $\sim 1$ mb、1 TeV $\sim 5$ mb；
- 平衡解：$j^{(0)}(E) = \tau_R(E) Q_{\bar{p}}(E)$；
- 再加速模型（拟合 B/C）产生太少反质子；无再加速模型可重现反质子通量但不能解释次级/初级比低能下降——需要扩散系数和注入谱中的转折。

**正电子**：
- 1964 年发现，在 $\sim 1$ GeV 以上正电子/电子比 $\approx 0.1$；
- 次级正电子主要来自 $\pi^+$ 和 $K^+$ 的衰变；
- 计算与数据一致，表明大多数 CR 正电子是次级的；
- 小部分可能来自原初源：脉冲星风、WIMP 湮灭；
- HEAT 数据在 5–7 GeV 处显示 $\sim 3\sigma$ 超额（后续 AMS-02 确认正电子分数在 GeV 能区随能量上升，是范式转移的标志）。

### 1.3.6 K-俘获同位素

**加速延迟**：
- $^{59}{\rm Ni}$（半衰期 $7.6 \times 10^4$ y）：存在；
- $^{57}{\rm Co}$（0.74 y）：存在；
- $^{56}{\rm Ni}$（6 d）：缺失（符合预期，加速前就衰变）。

ACE 数据表明：**合成与加速之间的延迟 $\ge 10^5$ 年**，与"超新星加速自身喷射物"的模型不一致，但支持"加速已有星际物质"（DFA 模型）。Grenier (2015) 在星暴环境中也引用此结论：$^{59}{\rm Ni}$ 缺失 → SN 合成到重核加速之间 $\ge 0.1$ Myr。

**再加速检验**：$^{51}{\rm V}$/$^{52}{\rm Cr}$ 与再加速模型更符合，但 $^{49}{\rm Ti}$/Ti 相反；V/Cr 比在轻微上更符合含再加速的模型——**结果不明确**，主要困难在核碎裂截面精度。

## 1.4 超高能宇宙线（UHECR）

### 1.4.1 GZK 效应

**GZK 阈值**（Greisen 1966；Zatsepin–Kuzmin 1966）：质子在静止系中 CMB 光子能量超过 **photo-pion 产生**阈值：

$$
E_{\rm lab,thr}^\gamma \equiv m_\pi + m_\pi^2/(2m_N) \simeq 160\ {\rm MeV}
$$

对应质子阈值（对背景光子 $\varepsilon$）：

$$
E_{\rm th} = m_\pi (m_N + m_\pi/2) / \varepsilon \simeq 6.8 \times 10^{16} \cdot (\varepsilon/\text{eV})^{-1}\ {\rm eV}
$$

CMB 典型 $\varepsilon \sim 10^{-3}$ eV → **GZK 截断出现在 $\sim 5 \times 10^{19}$ eV**，此时质子相互作用长度降至 **$\sim 6$ Mpc**。

**截面特征**：阈值附近显著的 $\Delta(1232)$ 单 $\pi$ 共振；高能极限由多重 $\pi$ 产生 $N\gamma_b \to N(n\pi)$ 主导。

**其他损失机制**：

| 过程 | 阈值/特征 | 能量范围 |
|---|---|---|
| 质子-对产生 (PPP, $p\gamma_b \to pe^+e^-$) | $E_{\rm th} \simeq 4.8 \times 10^{14} \cdot (\varepsilon/\text{eV})^{-1}$ eV | $\sim 5 \times 10^{17}$ eV |
| 中子 $\beta$-衰变 | $R_n = \tau_n E/m_N \simeq 0.9 \cdot (E/10^{20}$ eV) Mpc | $E \lesssim 10^{20}$ eV |
| 核的光致分裂 (Giant Dipole Res.) | 衰减长度 $\sim 10$ Mpc at $E \sim 2 \times 10^{20}$ eV | $E \gtrsim 10^{19}$ eV 的核主导 |

**完全发展 EM 级联堆积能量**在 ~100 GeV，受 EGRET diffuse $\gamma$-ray 数据约束。级联特征谱 $E^{-1.5}$。

**2017 年 Pierre Auger 确认**：$E > 5 \times 10^{19}$ eV 处能谱陡化（与 GZK 预期一致）。

### 1.4.2 源模型（bottom-up）

**AGN & Radio-Galaxies**：
- **AGN 核心**：典型 $R \sim 0.02$ pc, $B \sim 5$ G → $E_c \sim 10^{19}$ eV，但中心引擎内辐射场强烈 → 质子通过 photo-pion 严重衰减 → **$E > 10^{16}$ eV 质子无法逃出核心**。
- **FR-II 射电星系 hot spots**：soft photon 密度低 → photo-pion 损失不显著 → 若 B 场足够强 $E_{\max}$ 可达 $\sim 10^{21}$ eV；但 hot spot 距地球大 cosmological 距离 > 100 Mpc → GZK 效应使其粒子无法存活。

**脉冲星**：简单脉冲星 pair-cascade 短路 → 实际 < $10^{15}$ eV；Magnetar 表面 B $\sim 10^{15}$ G 提升能量预算；**Fe 离子 MHD 风**：新形成强磁化脉冲星可加速 Fe 离子 > $10^{20}$ eV，预言 UHECR 组成以 Fe 为主。

**GRB**：耗散风模型需三重条件同时满足；$E > 40 \cdot (E/10^{20}\ {\rm eV})^{3/4} (t/s)^{-1/4}$；但 GZK 距离内 (< 50 Mpc) 宇宙学 GRB 率 $\sim$ **每世纪一次** → 概率极低。

**Al-Dargazelli (1996) 的碰撞星系模型**：
- 利用 AGASA 等实验的 UHECR 到达方向数据；
- 通过磁场传播偏转、CMB 相互作用限制、Tully 星表分层匹配；
- 论证 **10 Mpc 以内的碰撞星系** 是 UHECR 最强候选者；
- 银河晕磁场：$B \approx 2\ \mu$G（盘局部），反转长度 $\lambda \approx 0.2$ kpc；Giant Halo 延伸至 $\ge 100$ kpc；
- 河外采用 $B\lambda = 1\ \mu$G kpc（$λ \approx 100$ kpc）。

**Waxman-Bahcall Bound**：比较 UHECR 通量 → 对 diffuse $\nu$ 通量给出上界；**不适用于** top-down（$\nu$ 是初级而非次级）或 AGN 核心（质子光学厚）。

### 1.4.3 Top-down 模型

**基本思想**：超重 X 粒子（$m_X \gg 10^{11}$ GeV）衰变 → 无需加速。

**三条件**：(a) 近期衰变（源 < 100 Mpc）；(b) $m_X \gg 10^{11}$ GeV；(c) 数密度/衰变率足够大。

**X 粒子衰变链**：
$$
X \to (\text{夸克, 轻子}) \to [\text{强子化: jets of }\pi + \text{baryons}(N)]
$$
$$
\pi^0 \to 2\gamma, \quad \pi^\pm \to \mu^\pm \nu_\mu \to (e^\pm) + \nu_e + \bar{\nu}_\mu
$$

**强子化理论**：三阶段 factorization（parton cascade → 非微扰 confinement → 衰变）；LPHD 假设；MLLA 极限谱。Hill 谱在 $x \ll 1$ 时给出 $dN_h/dE \propto E^{-1.3}$（公式 61）或 $E^{-1.5}$（公式 62）——**硬谱**（$1 < \alpha < 2$），总能量由少数极高能粒子携带，可自然产生 EHECR，预测 GZK 截断后有"recovery"。

**注入谱**：若 $f_N \sim 3\%$（核子占强子数 3–10%）：
$$
\Phi_{\pi^0}/\Phi_N \simeq 10, \quad \Phi_{\pi^\pm}/\Phi_N \sim 20
$$

**关键 Top-down 标志**：$\gamma/\text{CR}$ 通量比 > 1 在足够高 EHECR 能区。

**衰变率基准**（$m_X = 10^{16}$ GeV 时）：
$$
(\dot{n}_X, 0)_{\rm EHECR} \simeq 10^{35}\ {\rm Mpc^{-3}\ yr^{-1}} \simeq 13\ {\rm AU^{-3}\ yr^{-1}}
$$

**拓扑缺陷 (TD) 作为 X 源**：
- **宇宙弦**：环坍缩、cusp evaporation、超导电弦载流子发射；
- **单极子**：Rubakov 湮灭 → 重子不对称；monopolonium 衰变；
- **Vortons**：拓扑缺陷片段；
- **Necklaces**：混合系统；
- GUT 破缺时 $\eta \sim 10^{16}$ GeV → $m_X \sim 10^{16}$ GeV；
- **SUSY 影响**：Berezinsky & Kachelriess 提出 LSP 可能带走 $\sim 40\%$ 的 jet 总能量。

**约束**（低能 diffuse $\gamma$-ray、原初核合成、CMB 谱畸变、中微子通量）。

## 1.5 宇宙线与星系

### 1.5.1 CR-ISM 相互作用

**电离与加热**（Grenier 2015，"宇宙线的九种角色"）：
- CR 核与电子与原子/分子碰撞电离：
$$
\text{CR} + \text{H} \to \text{H}^+ + e^- + \text{CR}, \quad \text{CR} + \text{H}_2 \to \text{H}_2^+ + e^- + \text{CR}
$$
- 释放电子典型动能 **35 eV**，几乎与 CR 能量无关；电子至少再电离 1 个原子/分子；
- 完全电离气体加热转化效率 **~100%**；中性气体 **~20%**（次级电离 + 束缚态激发）；
- CR 加热率 $\sim 10^{-27} (\zeta_H^{\rm CR} / 10^{-16})$ erg s$^{-1}$ 每 H；
- 暗 ISM 温度维持 $\sim 10$ K（高于 CMB 2.7 K）；电子分数 $x(e) < 10^{-7}$。

**电离率**：本地 ISM $\zeta_H^{\rm CR} \approx 1.4 \times 10^{-17}$ s$^{-1}$（外推 Voyager 1 到 1 MeV）；CR 能量密度 $\approx 1.9$ eV cm$^{-3}$。

**CR 诱导 UV 辐射**：$H_{2}$ 次级电子在云深处产生内部 UV 源（星光不穿透的区域），驱动 CR 诱导 UV 光解化学；速率与 $\zeta_{H_2}^{\rm CR}$ 线性相关。

**CR-ISM 化学链**（Grenier 2015，图 8）：
$$
\text{CR} + \text{H}_2 \to \text{H}_2^+ + e^- \xrightarrow{+\text{H}_2} \text{H}_3^+
$$
$$
\text{H}^+/\text{H}_3^+ + \text{O} \to \text{O}^+ \to \text{OH}^+ \to \text{H}_2\text{O}^+ \to \text{H}_3\text{O}^+
$$
O 离子序列效率由 $f(\text{H}_2)$ 限制。$H_{2}$O$^{+}$/OH$^{+}$ 比对 $f(\text{H}_2)$ 敏感 → 可作为分子分数探针。

**散裂与轻元素合成**：
- $^{6}{\rm Li}$、$^{9}{\rm Be}$、$^{10}{\rm B}$：主要由 ISM CR 散裂产生；
- $^{7}{\rm Li}$：散裂 + ($\nu$,'He') 超新星 + Big Bang + AGB + novae；
- $^{11}{\rm B}$：散裂 + ($\nu$,C) 超新星 + AGB + novae。

### 1.5.2 CR 驱动的星系风

**CR 取走超新星激波能量的 10%–50%**，调节其对 ISM 的反馈（Grenier 2015 角色 6）。

**Fermi Bubbles**：$\gamma$ 功率 $2 \times 10^{30}$ W；磁场 1.5 nT；双锥外流速度 >900 km/s；CR 压力对在内银河启动大规模风是必需的（Zweibel 2013）。

**CR-ISM 双向耦合**（Grenier 2015 角色 4）：CR 驱动 MHD 波，部分维持星际湍流；在恒星团附近，风驱动湍流可能严重降低 CR 扩散长度（扩散抑制/局部困住）。

### 1.5.3 星暴星系

**Cygnus X**（Fermi-LAT 首次观测）：3–6 Myr 年轻星团，Fermi-LAT 1–100 GeV 图像揭示"cocoon"结构。硬 $\gamma$ 射线需刚加速的 CR 核分布，谱 $\sim E^{-2.4}$，总能量 > 2 GeV/n 约 $10^{42}$ J。CR 扩散长度在 Cygnus X 约比银河 ISM 短 **50 倍**。

**正常星系**：Fermi-LAT 探测 M31、LMC、SMC。LMC、SMC 值低（分别 <30%、<15% 银河系）→ 确认星系内 GeV–TeV CR 产生。

**星暴星系**：
- Fermi-LAT 已探测 M82、NGC 253、NGC 1068、NGC 4945；
- 缩放律：电子量热效率大；质子量热效率 **<50%**；
- 至 TeV 的硬/平谱支持 CR 核的能量无关损失机制优于扩散损失；
- **CR 核主要由平流带离星暴核**（带走能量与轻子产生潜力）；
- Arp 220 中 $\zeta_{H_2}^{\rm CR} > 10^{-13}$ s$^{-1}$，比 CMZ 高 ~$10^2$ 倍。

**FIR–射电光度相关**（Helou 1985）：若星系是好电子量热器，超新星率可解释相关。类似：FIR–$\gamma$ 相关（若星系是好质子量热器）。

**Parizot et al. (2004)**：超泡中集体效应对于 CR 加速到膝能量重要。

---

## 关键公式汇总表

| 编号 | 公式 | 含义 | 出处 |
|---|---|---|---|
| 1 | $\frac{\partial \psi}{\partial t} = q + \nabla\cdot(D_{xx}\nabla\psi - \vec{V}\psi) + \frac{\partial}{\partial p}p^2 D_{pp}\frac{\partial}{\partial p}\frac{\psi}{p^2} - \frac{\partial}{\partial p}\left[\dot{p}\psi - \frac{p}{3}(\nabla\cdot\vec{V})\psi\right] - \frac{\psi}{\tau_f} - \frac{\psi}{\tau_r}$ | 传播方程（完整） | Strong 2007 |
| 2 | $D_{pp} = \frac{p^2 V_a^2}{9 D_{xx}}$ | 动量扩散-空间扩散关联 | Strong 2007 |
| 3 | $\alpha = \frac{3r}{r-1} \xrightarrow{r\to 4} 4$ | DSA 动量谱指数 | Blasi 2013 |
| 4 | $\langle \Delta E / E \rangle = \frac{4}{3} \beta$ | 单次循环能量增益（一阶 Fermi） | Blasi 2013 |
| 5 | $\tau_{\rm acc} = \frac{3}{u_1-u_2}\int_0^p \frac{dp'}{p'}\left[\frac{D_1(p')}{u_1}+\frac{D_2(p')}{u_2}\right]$ | 加速时间 | Blasi 2013 |
| 6 | $E_c \sim 10^{17} \cdot Z \cdot (R/\text{kpc}) \cdot (B/\mu\text{G})$ eV | DSA 最大能量 benchmark | Bhattacharjee & Sigl 1999 |
| 7 | $(B/\mu\text{G})(R/\text{kpc}) > 2(E/10^{18}\text{eV})/(Z\beta)$ | Hillas 判据 | Bhattacharjee & Sigl 1999 |
| 8 | $E_{\rm th} = m_\pi(m_N+m_\pi/2)/\varepsilon \simeq 6.8\times 10^{16}(\varepsilon/\text{eV})^{-1}$ eV | GZK 质子阈值 | Bhattacharjee & Sigl 1999 |
| 9 | $D_{xx} \approx (\delta B_{\rm res}/B)^{-2} v r_g / 3$ | QLT 扩散系数 | Strong 2007 |
| 10 | $D_{xx} \sim 3\times 10^{28}$ cm$^{2}$/s at 1 GeV/n | 经验扩散系数 | Strong 2007 |
| 11 | $X(R) = \frac{\beta}{\beta_0} X_0 (R/R_0)^{-\alpha}$, $\alpha=0.54$ | 逃逸长度拟合 | Strong 2007 |
| 12 | $\lambda_{\rm esc} = \lambda_{\rm esc}(4\text{GV})(R/4\text{GV})^{0.6}$ | Rigidity-dependent 逃逸（Gupta-Webber） | Gaisser 1990 |
| 13 | $N_s/N_p \sim E^{-2/3}$（Kolmogorov 非定态云捕获） | 次级/初级比 | Biermann 1996 |
| 14 | $\xi_{\rm CR} \approx P_c(z)/(ρ_0 u_0^2) \approx 1 - u(z)/u_0$ | NLDSA precursor 深度 | Blasi 2013 |
| 15 | $\omega_I \approx [\frac{\pi}{8}\Omega_p^* k V_{\rm sh} n_{\rm CR}/n_i]^{1/2}$ | 高 $\xi_{\rm CR}$ 共振增长率 | Blasi 2013 |
| 16 | $\omega_I = (\pi/8)\Omega_p^*(V_{\rm sh}/v_A)(n_{\rm CR}/n_i)$ | 低 $\xi_{\rm CR}$ 共振增长率 | Blasi 2013 |
| 17 | $k^* r_{L,0} = 3\xi_{\rm CR}\gamma_{\min}/\Lambda \cdot (V_{\rm sh}/v_A)^2(V_{\rm sh}/c)$ | Bell 非共振模峰值尺度 | Blasi 2013 |
| 18 | $D_{xx} \sim R^{1/3}$（Kolmogorov）或 $R^{1/2}$（Kraichnan） | 扩散标度 | Strong 2007 |
| 19 | $E_{\max} \approx 3\times 10^5 B_{100}(T_s/300)(V_{\rm sh}/1000)^2$ GeV | Bohm 极限 SNR $E_{\max}$ | Blasi 2013 |
| 20 | $j_\nu^{\rm syn} \propto \nu^{-\beta_\nu}$, $\beta_\nu = (\gamma-1)/2$ | 同步辐射谱指数 | Strong 2007 |
| 21 | $\tau_{\rm syn} = 4\times 10^{10} B^{-2}_{100} E^{-1}_{\rm TeV}$ s | 同步辐射损失时标 | Blasi 2013 |
| 22 | $Q_{\rm CR} \sim 3\times 10^{42}$ erg/s | 银河系 CR 供给功率 | Gaisser 1990 |
| 23 | $\dot{p} \propto -\nabla\cdot\vec{V} \cdot E/3$ | 绝热能量损失 | Strong 2007 |
| 24 | $\delta = -[3D\nabla f + u_p(\partial f/\partial p)]/vf$ | 各向异性（扩散近似） | Strong 2007 |
| 25 | $\delta_{\rm CG} = (\gamma+2)u/c$ | Compton-Getting 各向异性 | Strong 2007 |
| 26 | $\zeta_{H}^{\rm CR} \approx 1.4\times 10^{-17}$ s$^{-1}$ | 本地 ISM CR 电离率 | Grenier 2015 |
| 27 | $\zeta_{H_2}^{\rm CR} > 10^{-13}$ s$^{-1}$（Arp 220） | 星暴电离率 | Grenier 2015 |
| 28 | $(\dot{n}_X)_0 \simeq 10^{35}$ Mpc$^{-3}$ yr$^{-1}$ | Top-down 衰变率基准 | Bhattacharjee & Sigl 1999 |
| 29 | $\frac{p+H}{5.63\ {\rm GeV}} \to p+p+p+\bar{p}$ | 反质子产生阈值与最小过程 | Gaisser 1990 |
| 30 | $F_0(k) = (\pi/6)^{1/2}(\xi_{\rm CR}/\Lambda)^{1/2}(c/V_{\rm sh})^{1/2}$ | 高 $\xi_{\rm CR}$ 下的 $F_0$ 上限 | Blasi 2013 |

## 关键数值汇总表

| 物理量 | 数值 | 备注 |
|---|---|---|
| 空间扩散系数 $D_{xx}$（1 GeV/n） | $(3-5)\times 10^{28}$ cm$^{2}$/s | Strong 2007 |
| 银河系 CR 能量密度 | $\rho_E \approx 1$ eV/cm$^{3}$ | Gaisser 1990 |
| 银河系总 CR 光度 | $\sim 10^{41}$ erg/s | Grenier 2015 |
| 银河系 SN 供给功率 | $\sim 3\times 10^{42}$ erg/s | Gaisser 1990 |
| CR 加速效率 $\xi_{\rm CR}$ | $\sim 10\%$（甚至至 50%） | Blasi 2013 |
| 晕高度 $z_h$ | 4–6 kpc（$^{10}{\rm Be}$/$^{9}{\rm Be}$ 约束） | Strong 2007 |
| 10 GeV/n CR 银河系停留时间 | $\sim 10^8$ 年 | Grenier 2015 |
| 总遍历气体柱密度 $N_H$ | $\sim 3\times 10^{24}$ cm$^{-2}$ | Grenier 2015 |
| 逃逸长度 $X_0$ | 11.8 g/cm$^{2}$（at 4.9 GV） | Strong 2007 |
| B/C 逃逸指数 $\alpha$ | 0.54 | Strong 2007 |
| 观测微分谱指数 $\gamma$（10 GeV–TeV） | $\approx 2.7$ | Gaisser 1990 |
| 源谱指数 | $\approx 2.1$（$\gamma - \delta$） | Gaisser 1990 |
| 膝部能量 | $\sim 5\times 10^{15}$ eV（质子） | Gaisser 1990 |
| 踝部能量 | $\sim 3\times 10^{18}$ eV | Biermann 1996 |
| DSA 强激波谱指数 $\alpha$ | 4（$f(p)\propto p^{-4}$） | Blasi 2013 |
| 相对论 DSA 能量谱指数 | 2（$dN/dE \propto E^{-2}$） | Blasi 2013 |
| 压缩比 $r$（强激波） | 4 | Blasi 2013 |
| PeVatron 条件 | $\delta B/B \gg 1$（约 10–100 倍） | Blasi 2013 |
| SNR X 射线窄边缘 B | 300–1000 $\mu$G | Blasi 2013 |
| Bohm 极限 SNR $E_{\max}$ | $\sim 3\times 10^5$ GeV | Blasi 2013 |
| Filamentation 可达能量（Tycho） | $\sim 200$ TeV | Blasi 2013 |
| 反质子产生阈值 | 5.63 GeV | Gaisser 1990 |
| 反质子截面（100 GeV） | $\sim 1$ mb | Gaisser 1990 |
| 反质子截面（1 TeV） | $\sim 5$ mb | Gaisser 1990 |
| GZK 截断能量 | $\sim 5\times 10^{19}$ eV | Bhattacharjee & Sigl 1999 |
| GZK 质子相互作用长度 | $\sim 6$ Mpc | Bhattacharjee & Sigl 1999 |
| PPP 阈值 | $\sim 5\times 10^{17}$ eV | Bhattacharjee & Sigl 1999 |
| 核光致分裂长度（$2\times 10^{20}$ eV） | $\sim 10$ Mpc | Bhattacharjee & Sigl 1999 |
| FR-II hot spot $E_{\max}$ | $\sim 10^{21}$ eV | Bhattacharjee & Sigl 1999 |
| Top-down 衰变率基准（$m_X=10^{16}$ GeV） | $\sim 10^{35}$ Mpc$^{-3}$ yr$^{-1}$ | Bhattacharjee & Sigl 1999 |
| Hill 谱 $\alpha$（x≪1） | 1.3–1.5 | Bhattacharjee & Sigl 1999 |
| 核子占强子数 | 3–10% | Bhattacharjee & Sigl 1999 |
| 电子能量损失（银河系内） | 60% | Grenier 2015 |
| 质子能量损失（强子反应） | 10% | Grenier 2015 |
| 电子量热器效率（星暴星系） | 大（good calorimeter） | Grenier 2015 |
| 质子量热器效率（星暴星系） | <50% | Grenier 2015 |
| 本地 ISM CR 电离率 $\zeta_H^{\rm CR}$ | $1.4\times 10^{-17}$ s$^{-1}$ | Grenier 2015 |
| 暗云温度 | $\sim 10$ K | Grenier 2015 |
| 暗云电子分数 $x(e)$ | $< 10^{-7}$ | Grenier 2015 |
| CMZ $\zeta_{H_2}^{\rm CR}$ | $(2-7)\times 10^{-15}$ s$^{-1}$ | Grenier 2015 |
| Arp 220 $\zeta_{H_2}^{\rm CR}$ | $> 10^{-13}$ s$^{-1}$ | Grenier 2015 |
| Fermi Bubbles $\gamma$ 功率 | $2\times 10^{30}$ W | Grenier 2015 |
| Fermi Bubbles 磁场 | 1.5 nT | Grenier 2015 |
| Fermi Bubbles 双锥外流速度 | >900 km/s | Grenier 2015 |
| Cygnus X CR 谱指数 | $\sim E^{-2.4}$ | Grenier 2015 |
| Cygnus X CR 能量 | $\sim 10^{42}$ J (>2 GeV/n) | Grenier 2015 |
| Cygnus X 扩散长度抑制 | 50× vs ISM | Grenier 2015 |
| $q_{\gamma,H}$ 外臂降幅 | 20–40% | Grenier 2015 |
| 加速延迟（$^{59}{\rm Ni}$） | $\ge 10^5$ yr | Strong 2007; Grenier 2015 |
| 各向异性 $\delta$（$10^{12}$–$10^{14}$ eV） | $\sim 10^{-3}$ | Strong 2007 |
| Alfvén 速度（ISM） | $V_a \sim 30$ km/s | Strong 2007 |
| Kolmogorov 谱 $D_{xx}(R)$ 标度 | $R^{1/3}$ | Strong 2007 |
| Kraichnan 谱 $D_{xx}(R)$ 标度 | $R^{1/2}$ | Strong 2007 |
| 泄漏盒"气体密度"（非物理） | $\sim 0.3$ cm$^{-3}$ | Strong 2007 |
| 4 kpc 晕实际平均密度 | $\sim 0.03$ cm$^{-3}$ | Strong 2007 |
| AGN 核心 $E_c$ | $\sim 10^{19}$ eV（逃出 <$10^{16}$ eV） | Bhattacharjee & Sigl 1999 |
| 银河晕磁场（Bhattacharjee 2000） | $B \sim 2\ \mu$G（盘），$\sim 0.15\ \mu$G（65 kpc） | Al-Dargazelli 1996 |
| 反转长度 $\lambda$（银河局部） | $\sim 0.2$ kpc | Al-Dargazelli 1996 |
| 反转长度 $\lambda$（河外） | $\sim 100$ kpc | Al-Dargazelli 1996 |
| 银河风速度约束 | $< 10$ km s$^{-1}$ kpc$^{-1}$（线性） | Strong 2007 |
| 银河风拟合速度（恒定） | $\sim 15$ km s$^{-1}$ | Strong 2007 |
| Biermann 三源 wind-SN 膝下谱 | $E^{-2.67}$ | Biermann 1996 |
| Biermann 三源 wind-SN 膝上谱 | $E^{-3.07}$ | Biermann 1996 |
| Biermann 三源 ISM-SN 谱 | $E^{-2.75}$ | Biermann 1996 |
| Biermann 三源 射电星系热点谱（注入） | $E^{-2.0}$ | Biermann 1996 |
| 分子云壳层 grammage | $\sim 1$ g/cm$^{2}$ | Biermann 1996 |
| Biermann 三种 regime 切换（1→2） | $\sim 20$ GeV/n | Biermann 1996 |

