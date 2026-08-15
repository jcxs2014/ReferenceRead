---
chapter: 4
title: Observational signatures
pages: "140–187"
sections:
  - "4.1 Cosmic ray propagation in the Milky Way"
  - "4.2 Cosmic ray driven/aided outflows in the Milky Way"
  - "4.3 Non-thermal emission from galaxies"
  - "4.4 Observational signatures of cosmic ray feedback in the CGM"
  - "4.5 Observational evidence for cosmic rays in galaxy groups and clusters"
  - "4.6 Cosmic rays from AGN jets in galaxy groups and clusters"
  - "4.7 Current and future multi-messenger observatories"
related_chapters:
  prev: 03_astrophysical_systems
  next: 05_open_questions_and_future_directions
status: done
---

> 本章属于：Cosmic ray feedback in galaxies and galaxy clusters (Ruszkowski & Pfrommer 2023)
>
> 上一章：`03_astrophysical_systems.md`
>
> 下一章：`05_open_questions_and_future_directions.md`

# 4. Observational signatures — CR 反馈的观测证据

## 4.1 本节核心内容

[FACT] §4 Observational signatures 覆盖 pp. 140–187，是 §2 Physics 和 §3 Astrophysical systems 建立的**物理预期与实际观测的直接对照**。七个子节依次覆盖：

1. §4.1 CR propagation in the Milky Way（银河系 CR 传播）
2. §4.2 CR-driven/aided outflows in the Milky Way（银河系 CR 驱动外流）
3. §4.3 Non-thermal emission from galaxies（星系非热辐射）
4. §4.4 Observational signatures in the CGM（CGM 观测特征）
5. §4.5 Observational evidence in galaxy groups and clusters（星系团/星系群观测证据）
6. §4.6 Cosmic rays from AGN jets（AGN 喷流 CR）
7. §4.7 Current and future multi-messenger observatories（多信使观测台）

[INTERPRETATION] §4 的**观测尺度上升**结构与 §3 严格对应：银河系内（§4.1–§4.2）→ 河外星系（§4.3）→ CGM（§4.4）→ 星系团（§4.5–§4.6）→ 未来观测展望（§4.7）。每一个 §4.X 都是对 §3 对应子节的**观测验证**。

## 4.2 原文内容

### 4.2.1 §4.1 Cosmic ray propagation in the Milky Way (pp. 140–147)

[FACT] §4.1 从**rigidity（刚性）**的定义开始：

$$
R \equiv \gamma_g B = \frac{pc}{Ze}
\quad \text{(Eq. 70)}
$$

- $R$：粒子刚性（单位 Volt），e.g. 10 GeV 质子对应 $R = 10$ GV
- $p$：动量
- $Z$：电荷数
- $e$：基本电荷

[FACT] §4.1.1 讨论 **Boron-to-Carbon（B/C）比**作为 CR 传播约束的核心工具：

- **Primary CR**（如 C、O）：直接来自加速源
- **Secondary CR**（如 Li、Be、B）：由 C、O 与 ISM 氢发生 **spallation（碎裂）** 反应产生
- B/C 比随能量/刚性变化反映 CR 在银河系中的 residence time 和扩散系数

[FACT] B 的产生率（Eq. 71）：

$$
Q_B(E) = n_{\text{ISM}}\,\bar{c}\,\sigma_B\,n_C
\quad \text{(Eq. 71)}
$$

- $\sigma_B$：C → B spallation 截面
- $n_{\text{ISM}}$：ISM 平均数密度

[FACT] 稳态下 B 密度满足：

$$
\frac{n_B}{\tau_B} = Q_B(E) \quad \Rightarrow \quad \frac{n_B}{n_C} \propto R^{-0.33}
$$

AMS 和 CALET 合作观测得到 B/C 比的刚性依赖：$R^{-0.33}$（Fig. 37 左），与 Kolmogorov turbulence 下的扩散系数 $D \propto R^{1/3}$ 一致。

[FACT] **Leaky box 模型**（一维扩散方程，Eq. 74）：

$$
\frac{\partial f_0(p,z)}{\partial t} = \frac{\partial}{\partial z}\left[\mathcal{D}(p)\frac{\partial f_0(p,z)}{\partial z}\right] + Q(p)\,\delta(z)
\quad \text{(Eq. 74)}
$$

- $f_0(p,z)$：CR 分布函数的各向同性部分
- $\mathcal{D}(p)$：扩散系数（假设与 $z$ 无关）
- $Q(p)\,\delta(z)$：盘平面源项

[FACT] 稳态解（Eq. 75–78）给出 B/C 比与扩散系数的关系：

$$
\frac{n_B(p)}{n_C(p)} \propto \frac{\mathcal{D}(p)}{v\,\tau_{\text{sp}}}
\quad \Rightarrow \quad
\mathcal{D}(p) \propto R^{1/3}
$$

[FACT] 观测约束的扩散系数典型值：

| 参数 | 数值 | 单位 |
|------|------|------|
| $\mathcal{D}_0$（1 GV） | $\sim 3\times 10^{28}$ | cm$^2$ s$^{-1}$ |
| 散射晕高度 $H$ | $\sim$ kpc | kpc |
| B/C 指数（AMS） | $-0.33$ | — |

[FACT] §4.1.2 讨论了**CR residence time**的推断：通过比较 primary 与 secondary CR 通量（He、C、O vs. Li、Be、B），在 Fig. 37 右中给出 CR 在银河系中的 residence time 谱。

[FACT] 注 23 指出扩散系数对 halo 高度 $z$ 的依赖在 §4.4 讨论；注 24 定义 scattering halo 包含 ISM 和 inner CGM，其中 CR 散射率足够高、扩散系数足够低以保证 CR 有从 halo 返回盘的非零概率。

### 4.2.2 §4.2 Cosmic ray driven/aided outflows in the Milky Way (pp. 147–153)

[FACT] §4.2.1 从**最大的大尺度结构**到**最小尺度**逐层审视银河系中心外流的观测证据（Fig. 38）：

- **eROSITA bubbles**（Predehl et al. 2020）：$|b| \lesssim 80^\circ$ 的双极 X 射线结构，由 ROSAT（Snowden et al. 1997）首先发现，暗示气泡周围气体受激波压缩。
- **Fermi Bubbles**（Su et al. 2010）：嵌入 eROSITA bubbles 中的双极 γ 射线气泡，延伸至 $|b| \lesssim 60^\circ$；γ 射线谱有近似平坦的强度分布和锐利的边缘，高能截止约 100 GeV；HAWC 观测在 1–100 TeV 区间给出 upper limits 一致。
- **Loop I**：在 Fermi Bubble 东侧延伸至 $b \sim 70^\circ$ 的射电结构；在 $|b| \lesssim 30^\circ$ 与 North Polar Spur（X 射线）空间重合。
- **S-PASS 偏振（2.3 GHz）**：揭示高度有序的 $|b| \lesssim 50^\circ$ 大尺度双极瓣，暗示磁场由银河系中心外流塑造（Carretti et al. 2013）。
- **Microwave Haze**（WMAP/Planck）：在 $|b| \lesssim 35^\circ$ 与 γ 射线气泡空间相关，但随离银河系中心距离衰减。
- **ROSAT 1.5 keV**：在 $|b| \lesssim 20^\circ$（距盘 3 kpc）与 γ 射线气泡边缘的空间相关，指示中心起源的外流（Bland-Hawthorn & Cohen 2003；Bland-Hawthorn et al. 2019）。
- **XMM-Newton "chimneys"**（Ponti et al. 2019）：亚 kpc 尺度上从盘连接到 Fermi Bubbles 的管状结构。
- **MeerKAT 双极 bubbles**（Heywood et al. 2019）：由数 Myr 前的能量事件形成，可能关联于喷流（Cecil et al. 2021）。

[FACT] 这些爆发可能把银河系中心的 CR 能量密度提升至比盘平均高**三个数量级**（Oka et al. 2019，基于 H₃⁺ 吸收线测量），形成强的 CR 压力梯度驱动外流（Yusef-Zadeh & Wardle 2019）。

[FACT] MeerKAT 射电谱指数图（Fig. 39）显示银河系中心 $\sim 420$ pc × 260 pc 区域内多个 SNR、垂直于盘方向的窄射电线丝、以及 Sgr A 的强辐射。

### 4.2.3 §4.3 Non-thermal emission from galaxies (pp. 153–163)

[FACT] §4.3 指出，**最直接的星系 feedback 约束方式**是观测河外星系的**非热射电（synchrotron）和 γ 射线发射**。通过**FIR-radio correlation**（van der Kruit 1971, 1973；Condon 1992；Bell 2003），可以测量：

- CR 电子辐射损失的**calorimetric 能量分数**
- 剩余用于驱动 plasma wave 的能量（无碰撞阻尼后传递给 background plasma）

[FACT] 射电偏振 + Faraday rotation 提供**磁场三维拓扑**信息；**边缘观测星系（edge-on galaxies）** 的偏振射电显示**极向磁场**连接盘与 halo（Tüllmann et al. 2000；Heesen et al. 2009；Damas-Segovia et al. 2016；Krause et al. 2020）。

[FACT] SOFIA/HAWC+ 偏振热尘埃观测结合 potential field 外推显示 M82 和 NGC 253 的超风区存在大尺度有序极向场（Jones et al. 2019；Lopez-Rodriguez et al. 2021）。

[FACT] **FIR-radio correlation 的物理本质**：
- 略微 super-linear
- 跨越五个量级的总光度
- 存在到 100 pc 尺度的 local correlation（Beck & Golla 1988；Murphy et al. 2008）

[FACT] §4.3.2 讨论**γ 射线发射在河外星系的物理分解**：
- **银河系**：GeV γ 射线主要由 hadronic（$\pi^0$ decay）主导，数十 GeV 以上可能转为 leptonic IC
- **河外恒星形成星系**：γ 射线同样主要由 hadronic pion decay 主导
- **FIR-γ 射线相关性（GeV 能量）**：直接探测 CR 离子 calorimetry，可用于 CR feedback 校准

[FACT] **3D MHD-CR 模拟中的射电 synchrotron 建模**（Werhahn et al. 2021c，Fig. 41）：
- 强 bremsstrahlung 损失使 synchrotron 谱显著平坦化
- 在高 star-formation rate 下，**secondary electrons** 主导 synchrotron 总发射，从而保证 FIR-radio correlation 的线性

[FACT] CR 传播代码 CRPropa（Dörner et al. 2023）和 GALPROP（Martin 2014；Buckman et al. 2020）用于从 CR 分布计算 3D synchrotron 发射。

### 4.2.4 §4.4 Observational signatures of CR feedback in the CGM (pp. 163–172)

[FACT] §4.4 讨论 CGM 中的 CR 反馈观测线索：

[FACT] **冷气体在 CGM 中的观测证据**：Werk et al. (2014)、McQuinn & Werk (2018) 的 cool photoionized low ions 丰度观测表明，CGM 中冷气体（$T \sim 10^4$ K）可能贡献**最多 50%**的星系重子质量预算。

[FACT] **冷相–热相 pressure 平衡的观测约束**：观测到的冷相电子数密度可能低于维持冷/热 CGM 热压力平衡所需值，暗示 CGM 中存在**非热压力支撑**（如 CR、磁场）。

[FACT] 这些非热压力支撑约束可能代表 **upper limits**，因为 CGM 气体具有高度 clumpy 和多相电离条件。

[FACT] **CR 在 CGM 中的作用（与 §3.4 对照）**：
- 调节冷气体质量
- 通过 streaming 在冷云遇到磁瓶颈时产生压力梯度，加速云团
- 通过辐射冷却避免 destructive streaming heating

[FACT] **Accretion mode transition**（Dekel & Birnboim 2006）：
- 热模式（hot mode）：$M_h \gtrsim 10^{11.5}\,M_\odot$，吸积气体被激波加热
- 冷模式（cold streams）：$M_h \lesssim 10^{11.5}\,M_\odot$，冷流穿透热 halo 供星

[FACT] 冷/热模式的转换可被恒星反馈（Faucher-Giguère et al. 2016；Fielding et al. 2017b）和 AGN 反馈（Nelson et al. 2019）进一步影响。

### 4.2.5 §4.5 Observational evidence for cosmic rays in galaxy groups and clusters (pp. 172–180)

[FACT] §4.5 综述星系团和星系群中 CR 的观测证据：

[FACT] **星系团中的 CR 观测主要手段**：
- **X 射线成像**（Chandra, XMM-Newton, eROSITA）：探测 ICM 温度/密度/熵 profile
- **射电 halo 和 relic**：星系团合并驱动的大尺度非热射电发射
- **γ 射线**（Fermi-LAT, HESS, MAGIC, VERITAS）：探测 CR 离子与 ICM 的 hadronic 相互作用
- **中微子**（IceCube）：未来对 hadronic γ 射线源的直接探测

[FACT] **射电 halo**：弥漫双极射电发射，与星系团合并有关，反映 CR 电子与大尺度湍流的相互作用；谱指数 $\alpha \sim 0.7–0.9$（$S_\nu \propto \nu^{-\alpha}$）。

[FACT] **射电 relic**：更狭长的射电结构，位于星系团合并前沿，反映激波加速的 CR 电子。

[FACT] γ 射线观测对 CR 离子密度给出**上限约束**：Fermi-LAT 对 cool core 星系团给出 CR-to-thermal pressure ratio $X_{\text{cr}} \lesssim 10^{-2}$（Ackermann et al. 2010, 2014a；Aleksic et al. 2010, 2012；Arlen et al. 2012）。

[FACT] 中微子观测尚未检测到星系团中的 CR 信号，给出 upper limits 约束 CR 密度。

### 4.2.6 §4.6 Cosmic rays from AGN jets in galaxy groups and clusters (pp. 180–185)

[FACT] §4.6 讨论 AGN 喷流作为星系团 CR 源的重要性：

[FACT] **AGN 喷流加速 CR**：喷流内部激波和磁重联可以加速 CR 到 TeV–EeV 能量。这些 CR 通过以下途径离开喷流并扩散到 ICM：
- 喷流端部（lobe 端）扩散
- 喷流–ICM 界面的 Kelvin-Helmholtz 不稳定性
- lobe 中的 CR streaming

[FACT] **AGN lobe 中的 CR 观测**：射电观测直接揭示 lobe 的 CR 电子分布；lobe 中 CR 压力可达 ICM 热压力的 10–30%。

[FACT] **AGN CR 对星系团冷却流的影响**（与 §3.5 对照）：CR 从 lobe 扩散到 ICM 后，通过 streaming instability 加热 ICM，可能部分或全部解决 cool core 的冷却流问题。

### 4.2.7 §4.7 Current and future multi-messenger observatories (pp. 185–187)

[FACT] §4.7 综述当前和未来多信使观测平台：

| 平台 | 类型 | 能量/波段 | 探测目标 |
|------|------|-----------|----------|
| Fermi-LAT | γ 射线卫星 | 100 MeV–300 GeV | π⁰ 衰变 γ 射线 |
| eROSITA | X 射线卫星 | 0.3–10 keV | ICM 成像、气泡 |
| CTA | γ 射线地面阵列 | 20 GeV–300 TeV | hadronic γ 射线 |
| SKA | 射电望远镜 | MHz–GHz | 射电 halo/relic、polarization |
| IceCube-Gen2 | 中微子 | TeV–EeV | 中微子（hadronic CR） |
| LHAASO | γ 射线/CR 地面阵列 | TeV–EeV | 高能 γ 射线 |

[FACT] 多信使观测的核心价值：**同时观测**同一 CR 源的 γ 射线、中微子、射电发射，能分离 leptonic vs. hadronic 过程，从而直接约束 CR 离子密度。

## 4.3 关键公式

$$
\boxed{R \equiv \gamma_g B = \frac{pc}{Ze}}
\quad \text{(Eq. 70, rigidity)}
$$

$$
\boxed{\frac{\partial f_0(p,z)}{\partial t} = \frac{\partial}{\partial z}\left[\mathcal{D}(p)\frac{\partial f_0(p,z)}{\partial z}\right] + Q(p)\,\delta(z)}
\quad \text{(Eq. 74, leaky box 1D diffusion)}
$$

$$
\boxed{\mathcal{D}(p) \propto R^{1/3}}
\quad \text{(观测推断，AMS B/C 比)}
$$

$$
\boxed{\frac{n_B}{n_C} \propto R^{-0.33}}
\quad \text{(AMS B/C 幂律拟合)}
$$

$$
\boxed{X_{\text{cr}} \equiv \frac{u_{\text{cr}}}{u_{\text{th}}} \lesssim 10^{-2} \;\;\text{(cool core 星系团, γ 射线上限)}}
$$

## 4.4 关键参数

| 参数 | 数值 | 单位 | 出处 |
|------|------|------|------|
| 1 GeV 质子刚性 | 10 | GV | §4.1 |
| B/C 幂律指数 | $-0.33$ | — | §4.1 (AMS) |
| 扩散系数 $\mathcal{D}_0$（1 GV） | $\sim 3\times 10^{28}$ | cm$^2$ s$^{-1}$ | §4.1 |
| 散射晕高度 $H$ | kpc 量级 | kpc | §4.1 |
| Fermi Bubble 纬度范围 | $|b| \lesssim 60^\circ$ | ° | §4.2 |
| eROSITA Bubble 纬度范围 | $|b| \lesssim 80^\circ$ | ° | §4.2 |
| Fermi Bubble γ 射线截止 | $\sim 100$ | GeV | §4.2 |
| CR 能量密度提升（Galactic Center） | 3 个数量级 | × | §4.2 |
| CGM 冷气体重子占比 | 最多 50% | — | §4.4 |
| Cool core 团 CR-to-thermal 上限 | $\lesssim 10^{-2}$ | — | §4.5 |
| Halo 射电 relic 谱指数 | $\alpha \sim 0.7–0.9$ | — | §4.5 |
| Halo 质量转换阈值 | $\sim 10^{11.5}$ | $M_\odot$ | §4.4 |

## 4.5 图表分析

**Figure 37**（AMS B/C 比 + 主/次 CR 通量，约 p. 142）— §4.1.1 的核心观测证据：

### 1. 图的目的
通过 AMS 观测数据确定 CR 在银河系中的传播性质，特别是扩散系数的刚性依赖。

### 2. 坐标轴
- 左：B/C 比 vs. 刚性 $R$（GV，对数）
- 右：主/次 CR 通量 $\times R^{2.7}$ vs. $R$（对数）

### 3. 图中元素
- 左：AMS 数据点 + $R^{-1/3}$ 拟合虚线（从 65 GV 开始）
- 右：He、C、O（primary）vs. Li、Be、B（secondary），按 $R^{2.7}$ 归一化

### 4. 关键观察
- B/C 比在 $R > 65$ GV 时精确符合 $R^{-1/3}$
- Primary 和 Secondary 通量有相同的刚性依赖，但绝对值不同（传播效应）

### 5. 数值信息
- B/C 拟合指数：$-0.33 \pm 0.01$
- 扩散系数 $\mathcal{D}_0(1\,\text{GV}) \sim 3\times 10^{28}$ cm$^2$ s$^{-1}$

### 6. 作者的解释
图 37 支持"CR 在银河系中扩散系数 $\propto R^{1/3}$"的经典预期，来自 Kolmogorov turbulence。

### 7. 与正文的关系
图 37 是 §4.1 的直接证据，也是 leaky box 模型的验证。

### 8. 物理意义
- 验证 §2.5 中 Kolmogorov turbulence 下的扩散系数预期
- 为 §3.3 的 CR 传输系数模拟提供观测约束

### 9. 需要注意的问题
[CRITIQUE] $R^{-1/3}$ 拟合仅在 $R > 65$ GV 时成立；低能端受到 solar modulation 的修正，拟合范围的选择对 $\mathcal{D}_0$ 有系统影响。

**Figure 38**（Fermi Bubbles + eROSITA Bubbles overlay，约 p. 148）— §4.2.1 的核心观测证据：

### 1. 图的目的
展示 γ 射线 Fermi Bubbles 与 X 射线 eROSITA Bubbles 的空间重合，暗示银河系中心存在大尺度外流。

### 2. 关键观察
- eROSITA bubbles（cyan）$|b| \lesssim 80^\circ$
- Fermi Bubbles（red）$|b| \lesssim 60^\circ$
- 空间重合指示共同的外流起源

### 3. 物理意义
支持 §3.2 CR 驱动银河风的观测证据——银河系中心可能存在 CR/AGN 驱动的大尺度风。

### 4. 需要注意的问题
[CRITIQUE] 空间重合不直接证明物理因果；射电观测（S-PASS polarization）提供磁场拓扑的证据，但 CR 密度分布的定量约束仍依赖 γ 射线建模。

**Figure 40**（空间分辨射电 synchrotron 图，约 p. 154）— §4.3 的射电观测核心：

### 1. 图的目的
展示空间分辨的射电 synchrotron 图与 star formation 区域的对应，用于约束 CR 传输和能量损失。

### 2. 关键观察
- 射电发射与 star formation 区域高度空间对应
- 射电 halo 延伸到盘以上 kpc 尺度
- 射电 polarized emission 揭示极向磁场结构

## 4.6 作者的逻辑

```
§4.1 [银河系内 CR 传播] B/C 比 → D ∝ R^{1/3} → Leaky box 模型验证
  → §4.2 [银河系外流] Fermi/eROSITA bubbles + MeerKAT 偏振 → CR 驱动风证据
    → §4.3 [河外星系] FIR-radio correlation + γ 射线 → CR calorimetry
      → §4.4 [CGM] 冷气体吸收线 + 非热压力约束 → CR 在 CGM 中的作用
        → §4.5 [星系团] 射电 halo/relic + γ 射线上限 → CR 在 ICM 中
          → §4.6 [AGN 喷流] lobe CR 观测 + 扩散 → CR 从 AGN 到 ICM
            → §4.7 [未来] CTA, SKA, IceCube-Gen2 → 多信使 CR 探测
```

[INTERPRETATION] §4 的论证链是"观测证据从近到远、从单一波段到多信使"：**每一节都对应 §3 的一个物理预期**。整体逻辑是让读者相信"CR 反馈的每一个物理预言都有对应的观测手段"。

## 4.7 我的理解

### 4.7.1 [INTERPRETATION] §4.1 B/C 比的深层含义

B/C 比的 $R^{-1/3}$ 幂律不仅是"验证扩散系数"，还隐含以下物理：
- **Kolmogorov turbulence** 的假设：只有当 ISM turbulence 为 Kolmogorov 谱时，$D \propto R^{1/3}$ 才成立
- **Scattering halo 的几何假设**：$H$ 与刚性无关
- **Steady state 假设**：CR 注入率和扩散率在观测时间尺度上不变

[CRITIQUE] 如果 ISM turbulence 偏离 Kolmogorov（如 Kraichnan $\sim R^{1/2}$），则 B/C 拟合结果需要修正。文献中（Strong et al. 2007；Génolini et al. 2021）对此有不同处理。

### 4.7.2 [CRITIQUE] Fermi Bubbles 的 CR 驱动论

[CRITIQUE] §4.2 明确指出 Fermi bubbles 的高能截止（$\sim 100$ GeV）和谱的"approximately independent of latitude"。但如果 Fermi bubbles 由 AGN 喷流驱动（而非 CR streaming），则其观测特征与纯 CR 驱动模型不同：

- AGN 喷流模型：高能电子通过 synchrotron + IC 加速
- CR streaming 模型：CR 离子通过 streaming instability 加热

[CRITIQUE] 目前观测（γ 射线 + X 射线 + 射电 polarization）**无法区分**这两种机制，需要中微子（IceCube-Gen2）的探测来分离 hadronic（CR 驱动）和 leptonic（喷流驱动）成分。

### 4.7.3 [INTERPRETATION] FIR-radio correlation 作为 CR feedback 校准工具

FIR-radio correlation 的物理链条：

$$
\text{Star formation} \rightarrow \text{SNR DSA} \rightarrow \text{CR electrons} \rightarrow \text{Synchrotron}
$$

$$
\text{Star formation} \rightarrow \text{UV} \rightarrow \text{Dust} \rightarrow \text{FIR}
$$

[INTERPRETATION] FIR-radio correlation 是"通过射电非热辐射直接测量 CR 电子能量"的唯一观测手段，因此也是校准 CR feedback 模型的**基础工具**。其略微 super-linear 的特征（Fig. 41 建模解释）说明：在低 SFR 星系中 CR 电子的同步辐射损失更大，而在高 SFR 星系中 CR 电子更容易逃逸到 halo。

### 4.7.4 §4 与 §3 的严格对应

| §3 物理预期 | §4 观测验证 |
|-------------|------------|
| §3.2 CR 驱动银河风 | §4.2 Fermi/eROSITA bubbles + MeerKAT |
| §3.3 宇宙学 CR 风 | §4.3 河外 FIR-radio correlation |
| §3.4 CGM 冷气体 | §4.4 吸收线 + 非热压力 |
| §3.5 AGN CR 加热 | §4.5–§4.6 γ 射线 halo + AGN lobe CR |

## 4.8 潜在问题与值得关注的地方

### 4.8.1 [CRITIQUE] CR 观测的"leptonic vs. hadronic"混淆

[CRITIQUE] §4 反复提到"CR 离子（protons）通过 π⁰ 衰变产生 γ 射线"和"CR 电子通过 IC/synchrotron 产生 γ 射线/射电"。在实际观测中：

- 射电：纯粹 leptonic（synchrotron）
- 弥漫 γ 射线：leptonic + hadronic 混合，需要多波段分解

[CRITIQUE] 论文承认"γ 射线观测只能给出 CR-to-thermal pressure ratio 的 **upper limit**"（§4.5，$X_{\text{cr}} \lesssim 10^{-2}$），因为 leptonic 和 hadronic 成分的分解仍不确定。

### 4.8.2 [CRITIQUE] Scattering halo 的几何假设

[CRITIQUE] Leaky box 模型假设散射晕是高度对称的（$H$ 与方位角无关）。但 S-PASS 和 Fermi bubbles 观测显示银河系中心存在**强各向异性结构**，散射晕可能不是简单的圆柱几何。这影响 $\mathcal{D}_0$ 的精确数值。

### 4.8.3 [CRITIQUE] 星系团射电 halo 的加速机制

[CRITIQUE] 射电 halo 的射电电子加速机制仍不确定：

- **DSA 模型**：星系团合并激波加速 CR 电子
- **Re-acceleration 模型**：湍流中的二次 Fermi 再加速预存的 CR 电子

两种模型预言不同的 halo 半径–光度关系，论文在 §4.5 中未给出明确的判断。

### 4.8.4 §4 与 §5 的接口

[INTERPRETATION] §4 观测中留下的**未解决问题**在 §5 Open questions 中将系统列出：

- CR 离子密度直接测量的困难（§5.1）
- CR 传输系数的时变与空间变化（§5.1）
- AGN–CR 耦合的定量模型（§5.2）
- 多信使观测的区分能力（§5.2）

---

## 元数据

```yaml
chapter: 4
pages: "140–187"
subsections: ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7"]
key_formulas:
  - "R = pc/(Ze) [Eq. 70, rigidity]"
  - "∂f₀/∂t = ∂/∂z [D(p) ∂f₀/∂z] + Q(p)δ(z) [Eq. 74]"
  - "D(p) ∝ R^{1/3} (AMS B/C)"
  - "n_B/n_C ∝ R^{-0.33} (AMS)"
keywords:
  - B/C ratio
  - Fermi Bubbles
  - eROSITA Bubbles
  - FIR-radio correlation
  - Galactic outflow
  - multi-messenger
references_internal:
  prev_chapter: 03_astrophysical_systems
  next_chapter: 05_open_questions_and_future_directions
```

**引用页码**：全文引用基于 *A&A Reviews 31:4 (2023)*，pp. 140–187。
