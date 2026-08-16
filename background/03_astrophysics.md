---
title: 03_astrophysics
category: 背景知识
status: completed
read_date: '2026-08-12'
lastread: '2026-08-12'
tags:
- '03'
- astrophysics
citations: []
path: background/03_astrophysics.md
---
# 03. 天体物理背景知识体系 — 太阳丰度、恒星核合成与暗物质

> **范围**：本文件综合 `03_stellar-nucleosynthesis/` 下 7 篇精读论文 + `04_experiments/` 下 4 篇实验文献的知识要点（2026-08-16 补入实验观测节 §11.5），
> 面向"太阳丰度作为核合成/化学演化基准"的研究主题，抽取**跨论文的共享概念、
> 关键数值、核心公式与方法论**，并按主题域重组为可复用的背景知识体系。

**论文清单**：

| 编号 | 论文 | 主题域 |
|------|------|--------|
| 0007 | Grevesse & Sauval 1998 (GS98), SSR 85, 161 | 标准太阳组成 |
| 0008 | Lodders 2003, ApJ 591, 1220 | 太阳系丰度 + 冷凝温度 |
| 0009 | Asplund et al. 2009 (AGSS09), ApJ 702, L1 | 3D non-LTE 太阳光球丰度 |
| 0010 | Gies & Lambert 1992, ApJ 387, 673 | 早 B 型星 CNO 丰度 |
| 0011 | Kewley et al. 2001, ApJS 132, 37 | 星暴星系诊断图与 W-R 物理 |
| 0012 | Dieterich et al. 2014, AJ 147, 94 | 氢燃烧极限（恒星/褐矮星边界） |
| 0013 | Bertone & Hooper 2018, RMP 90, 045002 | 暗物质历史综述 |

---

## 1. 太阳化学组成的演化（GS98 → Lodders 2003 → AGSS09）

太阳丰度是**整个天体物理的基准输入**——它决定恒星模型、核合成产额、
星系化学演化和系外行星形成模型。20 年间这一基准经历了三次重大修订。

### 1.1 太阳丰度的历史时间线

```
A&G 1989        Z/X = 0.0267,  O = 8.86, C = 8.52, Fe = 7.50       [旧基准]
  → GS98 (Grevesse & Sauval 1998)
      X = 0.735, Y = 0.248, Z = 0.017, Z/X = 0.023
      O = 8.83, C = 8.52, N = 7.97, Ne = 8.08, Fe = 7.50
      [解决 Fe I/Fe II 不一致：Anstee-O'Mara 碰撞展宽 + 新经验模型]
  → AGS05 (Asplund, Grevesse & Sauval 2005)
      Z/X = 0.0165,  C、O、Ne 更低
  → Lodders 2003（本文 0008）
      大气: X=0.7491, Y=0.2377, Z=0.0133, Z/X=0.0177
      原始: $X_{0}$=0.7110, $Y_{0}$=0.2741, $Z_{0}$=0.0149, $Z_{0}$/$X_{0}$=0.0210
      O = 8.69, C = 8.39, N = 7.83 (大气)
      [Allende Prieto et al. 2001, 2002 NLTE 下调 C、O]
  → GS02 (Grevesse & Sauval 2002)  Z/X = 0.0208
  → AGSS09 (Asplund et al. 2009, 本文 0009)
      X = 0.7381, Y = 0.2485, Z = 0.0134, Z/X = 0.0181
      原始: $X_{0}$=0.7154, $Y_{0}$=0.2703, $Z_{0}$=0.0142
      O = 8.69, C = 8.43, N = 7.83, Ne = 7.93, Fe = 7.50
      [3D 流体动力学 + non-LTE 全元素同质重测]
  → AAF21 (Asplund, Amarsi & Frey 2021)  O = 8.69 (部分上调回 Lodders 2003)
```

### 1.2 三次修订的关键差异

| 量 | A&G 1989 | GS98 | Lodders 2003 | AGSS09 |
|----|----------|------|--------------|--------|
| X (H 质量分数) | 0.70 | 0.735 | 0.7491 (大气) / 0.7110 (原始) | 0.7381 / 0.7154 |
| Y (He 质量分数) | 0.28 | 0.248 | 0.2377 / 0.2741 | 0.2485 / 0.2703 |
| Z (金属质量分数) | 0.02 | 0.017 | 0.0133 / 0.0149 | 0.0134 / 0.0142 |
| Z/X | 0.0267 | 0.023 | 0.0177 / 0.0210 | 0.0181 |
| A(O) | 8.86 | 8.83 | 8.69 | 8.69 |
| A(C) | 8.52 | 8.52 | 8.39 | 8.43 |
| A(N) | 8.17 | 7.97 | 7.83 | 7.83 |
| A(Ne) | 8.01 | 8.08 | — | 7.93 |
| A(Fe) | 7.50 | 7.50 | — | 7.50 |
| A(Si) | 7.51 | 7.55 | — | 7.51 |

**关键趋势**：20 年间 Z/X **下降 ~30%**（从 0.027 到 0.018），O 下降 ~0.17 dex。
这是 1D LTE → 3D non-LTE + 更精确原子数据 + 更准确的不透明度导致的**系统性下修**。

### 1.3 两次方法论革命

**革命 1 (GS98)**：Fe 丰度争议终结
- 历史：Oxford（Blackwell 等）Fe I 线给出 A(Fe)=7.63 > 陨石 7.50；Kiel-Hannover 与陨石一致
- 根因：Holweger-Müller 1974 半经验模型在 log $\tau$ ≈ −3 层偏热 ~200 K，
  使低激发 Fe I 线形成区温度偏高 → 低估 Fe 丰度
- 解决：Anstee-O'Mara 精确计算 s-p, p-s, p-d 与中性 H 的碰撞展宽截面；
  构造"新模型"在 log $\tau$ ≈ −3 层降温 200 K，低激发线丰度**上移**到陨石值
- 结论：Fe I/Fe II 自洽，A(Fe) = **7.50 ± 0.05**，与陨石 Fe=7.50 精确一致

**革命 2 (AGSS09)**：3D non-LTE 系统性重测
- 3D 模型（Trampedach et al. 2009）全面优于 1D Holweger-Müller：
  - 中心-边缘变化自然出现，H$\alpha$/H$\beta$ 线无自由参数复现
  - 金属线线型自然复现，无需微湍流/宏观湍流参数
  - Fe I/Fe II 一致（无激发势趋势）
- Fe 丰度之争在 3D 模型下彻底解决：log $\epsilon$_Fe = 7.50
- Li 太阳亏缺 ~150×（陨石 vs 光球差 2.21 dex）→ 需对流区底部额外混合
- Be、B 通过 UV "missing opacity" 修正回到陨石值

### 1.4 太阳丰度的"五个用途"（GS98 §3）

1. **太阳内部模型 & 大气模型的基准**：不透明度（Fe 在核心，O、Ne 在对流区底）
2. **核合成理论必须复现的基准**：s、r、p、rp 过程的太阳中子俘获元素
3. **星系化学演化的锚点**（Pagel 1997）
4. **所有其他恒星的比较参考点**
5. **太阳系其他天体（月、行星、彗星、陨石）的校准靶**

### 1.5 AGSS09 vs 日震的张力（AGSS09 的"遗产"）

- SSM 用 AGSS09 后：
  - **R_BCZ（对流区底半径）偏浅**：SSM 0.725 R☉ vs 日震 0.7133 R☉
  - **Y_S（表面 He 质量分数）偏低**：SSM 0.238 vs 日震 0.249
  - **声速偏差**在 R < 0.71 R☉ 处最严重
- 需 **不透明度 +10–20%** 才能恢复吻合，但**无原子物理支持**
- 剩余可能性：内部重力波（Arnett, Meakin & Young 2005）
- 判断：**AGSS09 与标准太阳模型中至少一个有误**——至今未解的开放问题

### 1.6 丰度标度公式

$$A(\mathrm{El}) = \log(N_{\mathrm{El}} / N_{\mathrm{H}}) + 12.0 \quad \text{[天文对数标度]}$$

$$\log\varepsilon_X = \log\varepsilon_{\mathrm{H}} + \log(N_X / N_{\mathrm{H}})$$

**陨石换算（以 Si 归一）**：
$$\log\varepsilon_X = 1.51 + \log N_X \quad [N_X \text{为陨石质量分数}]$$

**He 与 Z/X 关系**：
$$Y = \frac{4 N_{\mathrm{He}}}{N_{\mathrm{H}} + 4 N_{\mathrm{He}}}$$
例：$N_{\mathrm{He}}/N_{\mathrm{H}} = 0.085 \rightarrow Y \approx 0.254$

---

## 2. 太阳丰度 vs 陨石（CI 碳质球粒陨石）的一致性

陨石是**唯一能"称量"太阳**的独立手段。CI 陨石保留原初太阳星云几乎所有元素
（**仅损失最挥发元素**），是光球丰度的独立校验。

### 2.1 太阳 vs 陨石的对比模式

| 陨石缺失 | 原因 |
|---------|------|
| H, He, C, N, O, Ne, Ar | 挥发元素，球粒陨石形成时蒸发流失 |
| As, Se, Br, Kr, Te, I, Xe, Cs, Ta, Re, Hg, Bi, Th | 同上 |

| 太阳侧缺失 | 原因 |
|---------|------|
| As, Se, Br, Kr, Te, I, Xe, Cs, Ta, Re, Hg, Bi, Th | 光球光谱中谱线不足以测量 |

| 太阳侧方括号（非光球测量） | 来源 |
|---------|------|
| He | 太阳黑子 / 日震 / 太阳风 |
| F, Cl | 日冕 / 太阳风 |
| Ne | 新兴活动区光球物质 / SEP |
| Ar | 日冕 / SEP |

### 2.2 关键一致性数据

- AGSS09：**45 元素均值差 0.00 ± 0.05 dex**（仅 10/57 超出合并不确定度）
- 41/56 可比元素在 15% 内一致（Lodders 2003）
- 太阳 vs 陨石几乎一致→ **光球丰度代表原初太阳星云**，仅挥发元素除外
- **Lu 案例**：早期光球 Lu 丰度比陨石大 4×，新测 Lu II 跃迁概率后下降到陨石水平
  → "太阳几乎从不出错，出错的是旧的原子数据"

---

## 3. 太阳 He、Li-Be-B 与 CNO 的专题

### 3.1 太阳氦

He 不出现在光球光谱（He I 5876/6678/7065 在光球不显著），且在陨石中损失。

| 来源 | A_He / Y | 备注 |
|------|---------|------|
| 日震反演（Dziembowski 1998）| Y = 0.248 ± 0.002 | **最准，采用值** |
| 原太阳（初始）| $Y_{0}$ = 0.275 ± 0.01 | 含对流区底部沉降 |
| 标准太阳模型校准 | Y = 0.27 ± 0.01 | 原太阳星云 |
| AGB 模型（含迁移） | Y = 0.275（Gabriel 1997） | 初始丰度 |

**A_He = 10.93 ± 0.004**（现今对流区顶部，GS98 采用）

### 3.2 Li-Be-B 悖论

- **Li 消耗 160 倍**：原始 A(Li) ≈ 3.31（陨石）vs 光球 A(Li) = 1.10
  → 10^(3.31-1.10) ≈ 162× 消耗
- **Be 与 B 基本未被破坏**
- 传统对流模型无法重现 Li 耗损而不消耗 Be
- 解决：**对流区底部以下微弱混合**（Blöcker 1998; Vauclair 1998; Zahn 1998）
- Li、B 丰度因 NLTE 效应（Carlsson et al. 1994）小幅下调

### 3.3 CNO 的核合成意义

- **金属性贡献**：O 47%, C 17%, N 5%
- 底部对流区不透明度主要贡献者
- C/N/O 是 **CNO 循环的平衡产物**：
  - $C_{1}$$^{2}$ → $N_{1}$$^{3}$（慢步骤，$^{12}{\rm C}$(p,$\gamma$)$^{13}{\rm N}$）
  - 循环平衡时：C↓↓, N↑↑, O 不变
- AGSS09 直接影响恒星演化模型中的 CNO 初始丰度假设
- **C/O 比**：AGSS09 C/O = 10^(8.43-8.69) = 0.28 < 1 → **太阳是富 O 型**
- 太阳中微子（Borexino, SNO+）将直接测量 $^{13}{\rm N}$、$^{15}{\rm O}$ 通量（CNO 循环）

---

## 4. 太阳系丰度与冷凝温度（Lodders 2003）

### 4.1 关键创新：区分"大气"与"太阳系"丰度

- **大气丰度** = 太阳光球光谱现今观测值
- **原始太阳（=太阳系）丰度** = 4.55 Gyr 前的原初值
- **沉降修正公式**（式 5）：A(El)$_{0}$ = A(El) + 0.074
  - 由 Boothroyd & Sackmann (2003) SSM 标度关系推导
  - 太阳金属度比原初**低 16%**（重元素沉降）

### 4.2 冷凝温度（$10^{-4}$ bar 下）

| 相 | 50% 冷凝温度 |
|----|-------------|
| A$l_{2}$$O_{3}$ | 1677 K |
| Fe（金属铁）| 1357 K |
| Troilite（FeS）| 704 K（分水岭）|
| Magnetite（F$e_{3}$$O_{4}$）| 371 K |
| $H_{2}$O 冰 | 182 K |
| C$O_{2}$ | 73 K |
| $N_{2}$ | 58 K（动力学）/ 131 K（平衡）|
| C（石墨）| 626 K（动力学）/ 41 K（平衡）|

### 4.3 太阳系 vs 太阳大气冷凝

- **太阳系 T = 大气 T + ~10 K**（因金属度高 16%）
- 冰/岩石比：A&G 1989 为 **2.09** → Lodders 2003 **1.17**（↓44%）
- 总冷凝质量：A&G 1989 1.903% → Lodders 2003 太阳系 **1.487%**（↓22%）
- **直接影响**：外太阳系化学、巨行星形成、彗星模型

---

## 5. 早 B 型星 CNO 与 CN-cycle 混合（Gies & Lambert 1992）

### 5.1 问题：Lyubimkov 1984 主张 vs 标准图景

- Lyubimkov 主张主序 B 星已普遍显示 CN-cycle 表面产物（N↑, C↓, He↑）
- 与主流观点（Gehren 1985：B 星 ≈ 太阳丰度）矛盾
- 与标准演化模型矛盾（第一次 dredge-up 前不出现 CN-cycled 表面）

### 5.2 方法

| 环节 | 技术 |
|------|------|
| 观测 | McDonald 2.1 m + coudé；Reticon 1728 px；S/N=300 |
| T_eff / log g | Strömgren [c1] + Balona c$^{0}$ + H$\beta$ 轮廓迭代 |
| LTE 丰度 | Kurucz 1979 大气 + WIDTH6 |
| Non-LTE 丰度 | Becker & Butler (1988) 表 + Auer & Mihalas (1973) He 幂律 |
| 温度修正 | $\Delta$T = f·T_eff, f = 0.034 ± 0.015 |

### 5.3 结果

- 非超巨星 B 星 ≈ 太阳 ≈ Orion 星云（$\Delta$ log $\epsilon$ ≈ 0）
  - log $\epsilon$(He) ≈ 11.00（与太阳一致）
  - log $\epsilon$(C) ≈ 8.15（略低于太阳 8.43）
  - log $\epsilon$(N) ≈ 8.15（略低于太阳 7.83-8.4）
  - log $\epsilon$(O) ≈ 8.80（与太阳 8.69 一致）
- **Lyubimkov 主张不成立**：log g=3.5 + $\xi$=10 的假组合可产生 0.90 dex 假增
- **$\rho$ Leo (HD 91316)** 最 N 富集 +0.60 dex → **定量匹配 Maeder-Meynet 演化轨**
  - 预测 He +0.10、C −0.10、O −0.04 → 观测一致 → **部分 CN-cycle 混合**
- **超巨星**：5 颗全 N 富集，但 C/N 远未达 CN-cycle 平衡 → **部分混合**
  - 重要意义：蓝超巨星可在红巨星之前出现显著混合 → SN 1987A 前身星

### 5.4 关键物理

**CN-cycle 平衡**：$\mathrm{C/N} = (^{12}\mathrm{C}/^{14}\mathrm{N})_{\mathrm{eq}} \approx$ 很小
**部分混合**：C/N 介于初始与平衡之间
**检验方法**：同时测量 He、C、N、O，与 Maeder-Meynet 演化轨对比

---

## 6. 星暴星系诊断图与 W-R 物理（Kewley et al. 2001）

### 6.1 核心图像

- 诊断图（BPT 图）：log([O III]$\lambda$5007/H$\beta$) vs log([N II]/H$\alpha$) 或 [S II]/H$\alpha$ 或 [O I]/H$\alpha$
- **诊断图对 1–4 Ry 区间（54–756 eV）EUV 谱指数最敏感**
- > 4 Ry 光子（>756 eV）对 [N II]/H$\alpha$ 贡献小
- **星暴（非 H II 区）必须用连续恒星形成模型**——瞬时模型产生"禁带"

### 6.2 PEGASE vs STARBURST99 差异

| | PEGASE（Padova + PNN）| STARBURST99（Geneva + Lejeune）|
|--|---------------------|------------------------------|
| 演化轨 | Padova | Geneva |
| 大气 | Clegg & Middlemass PNN | Lejeune W-R |
| 1-4 Ry EUV | **最硬** | 较软 |
| He II $\lambda$4686 预测 | −6（错误）| −1.7（与观测一致）|

- **PEGASE 是唯一覆盖所有观测点的模型**，但仅因 PNN 大气硬 EUV
- **Schmutz W-R 大气物理上更合理**，但需连续金属不透明度补充硬 EUV

### 6.3 关键参数

| 量 | 值 |
|----|----|
| W-R 星发射测度 | ∫ n$^{2}$ dr ∝ (Ṁ/v∞)$^{2}$ · $R_{3}$$^{-3}$ |
| 星暴年龄（动态平衡）| ≈ 6 Myr (PEGASE) / 8 Myr (STARBURST99) |
| 氢燃烧寿命 | $\tau$ ≈ 4.5 (M/40 $M_\odot$)$^{-0.43}$ Myr |
| 全星系 SFR | ~3.4 $M_\odot$/yr |
| 1 kpc 视场 SFR | ~0.07 $M_\odot$/yr (FIR) vs ~0.04 $M_\odot$/yr (H$\alpha$) |

### 6.4 Kewley 极端星暴分类线（公式 5–7）

**Kewley 理论分类线**（矩形双曲线，PEGASE 最硬 EUV 网格的折回边）：

$$\log([\mathrm{O\ III}]/\mathrm{H}\beta) \leq \frac{0.61}{\log([\mathrm{N\ II}]/\mathrm{H}\alpha) - 0.47} + 1.19 \quad [\mathrm{N\ II}\ \text{线}]$$

$$\log([\mathrm{O\ III}]/\mathrm{H}\beta) \leq \frac{0.72}{\log([\mathrm{S\ II}]/\mathrm{H}\alpha) - 0.32} + 1.30 \quad [\mathrm{S\ II}\ \text{线}]$$

$$\log([\mathrm{O\ III}]/\mathrm{H}\beta) \leq \frac{0.73}{\log([\mathrm{O\ I}]/\mathrm{H}\alpha) + 0.59} + 1.33 \quad [\mathrm{O\ I}\ \text{线}]$$
- 分类模糊率：理论 6% vs Veilleux-Osterbrock 1987 半经验 16%
- **已被 SDSS、zCOSMOS、MANGA 等大型巡天广泛采用**

### 6.5 化学演化相关经验关系

**He/H 与金属丰度**：
$$\mathrm{He/H} = 0.081 + 0.026 \cdot (Z/Z_\odot)$$

**N/H 经验关系**：
$$\log(\mathrm{N/H}) = -4.57 + \log(Z/Z_\odot) \quad \text{for } Z/Z_\odot \geq 0.23$$
$$\log(\mathrm{N/H}) = -3.94 + 2\log(Z/Z_\odot) \quad \text{for } Z/Z_\odot < 0.23$$
N 从初级 $\rightarrow$ 次级 的转折点 = $0.23\ Z_\odot$

### 6.6 SNR 对诊断图的贡献

- H$\beta$ 贡献 16–20%，但 [O III]/H$\beta$ 仅 ~2%（可忽略）
- **不足以解释星暴-AGN 诊断图差异**
- 冷却时标：$\tau$_cool ≈ 200 · $v_{100}$$^{-4.4}$ · Z · n yr

---

## 7. 氢燃烧极限（Dieterich et al. 2014）

### 7.1 关键发现

- **2MASS J0523−1403**（L2.5 矮星）：
  - T_eff = 2074 ± 27 K
  - log L/L☉ = −3.898 ± 0.021
  - R/R☉ = 0.086 ± 0.003
  - V−K = 9.42
- 半径-温度/光度图上的**局部半径极小值**
- 半径极小 = **电子简并开始的物理标志** → 几乎模型无关的恒星/褐矮星边界
- 所有 6 个主流演化模型预言的氢燃烧极限温度**比本文低 ~400 K**

### 7.2 方法学要点

- 色温插值法：对 20 种颜色各自拟合 (obs−synth) 残差随 T_eff 的插值至 0
- 迭代 SED 拟合：模板 × 9 阶 poly 修正 → 迭代至 < 2% 波段残差
- CHARA 干涉测量半径校准：平均 |残差| = 3.4% → 方法系统误差 < 5%
- **VRI 光学测光对 cool atmosphere T_eff 测定不可或缺**——纯红外颜色不收敛

### 7.3 太阳金属丰度的影响

- 演化模型普遍预言 T_H-burning limit 比观测低 ~400 K
- **太阳金属丰度下调 22%**（AGSS09 vs 旧值）→ 可定量解释部分偏差
- Caffau et al. 2011 太阳金属丰度修订是关键输入
- 这是**太阳丰度直接影响恒星演化模型**的具体实证案例

### 7.4 变率

- I 波段变率：36+9/−7%（15 mmag 阈值，36 目标中 13 变）
- **在 T_eff ≈ 2100 K 附近出现变率尖峰**（未定因）
- 与 Khandrika 2013 的 36+7/−6% 一致

---

## 8. 暗物质（Bertone & Hooper 2018）

### 8.1 暗物质证据的多尺度汇聚

| 尺度 | 关键观测 | 年代 |
|------|---------|------|
| 太阳邻域 | Oort 1932 总密度 0.092 $M_\odot$/pc$^{3}$ | 1932 |
| 星系团 | Zwicky 1933 Coma 视向速弥散 1000 km/s vs 80 km/s 预期 | 1933 |
| 星系团 M/L | Zwicky 1937 Coma M/L ≈ 500（修正 $H_{0}$ 后仍高 ~60）| 1937 |
| 本星系群 | Kahn-Woltjer 1959 timing argument | 1959 |
| 旋涡星系 | Freeman 1970 首次明确"必须存在额外物质" | 1970 |
| HI 自转 | Bosma 1978 25 星系平坦到光学区外 | 1978 |
| 星系团维里 | 大 M/L（100–800）| 1930s-1950s |
| 微引力透镜 | EROS < 8%（排除 MACHO）| 1993+ |
| CMB | $\Omega$_b h$^{2}$ = 0.02225 ± 0.00016 | Planck 2015 |
| 引力透镜 | Bullet Cluster 2006（暗物质与重子空间分离）| 2006 |

### 8.2 关键公式

**维里定理（Zwicky 1933）**：
$$\sigma_v^2 = \frac{GM}{2R} \quad \Rightarrow \quad M = \frac{2R\sigma_v^2}{G}$$

**自转曲线**：
$$v_{\mathrm{circ}}^2(r) = \frac{GM(<r)}{r}$$
平坦旋转曲线 $\Rightarrow M(<r) \propto r$ — 暗晕存在的直接证据

**MOND 加速度标度**：
$$a_0 \approx 1.2 \times 10^{-10}\ \mathrm{m/s^2}$$
精确预测 Tully-Fisher 关系 $\alpha = 4$

**微透镜时标**：
$$t \approx 130\ \mathrm{d} \times (M/M_\odot)^{0.5}$$

**R 宇称（SUSY）**：
$$P_R = (-1)^{2s + 3B + L}$$
标准模型粒子 $P_R = +1$；超伴 $P_R = -1$ $\rightarrow$ LSP 稳定 $\rightarrow$ 暗物质候选

**Peccei-Quinn 轴子质量**：
$$m_a \sim \frac{\lambda_{\mathrm{QCD}}^2}{f_{\mathrm{PQ}}}, \quad \lambda_{\mathrm{QCD}} \sim 200\ \mathrm{MeV}$$

**WIMP 热遗迹丰度**：
$$\Omega h^2 \approx \frac{0.1}{\langle\sigma v\rangle}$$
$$\langle\sigma v\rangle \sim 10^{-26}\ \mathrm{cm^3/s} \quad \text{[WIMP 奇迹]}$$

### 8.3 候选体谱系

| 候选体 | 机制 | 质量范围 | 现状 |
|--------|------|---------|------|
| 中微子（热）| 标准模型遗迹 | ≲ eV | **排除**（White-Frenk-Davis 1983）|
| 重中微子 | 稳定重轻子 | 1–15 GeV | 排除 |
| 惰性中微子 | 振荡产生 | keV | 严格 Dodelson-Widrow 已排除 |
| 轴子 | PQ 机制 | $10^{-6}$ – $10^{-4}$ eV | ADMX 已覆盖 1.9–3.3 $\mu$eV |
| 中性微子 | SUSY LSP | GeV–TeV | **35 年主流候选**；LHC 无发现 |
| 引力微子 | SUSY 引力伴 | ≪ eV 或 ≫ TeV | 宇宙学 gravitino problem |
| 单极子/宇宙弦 | 大统一遗迹 | 各种 | 约束严格 |
| 夸克 nuggets | 假真空相变 | 厘米尺度 | 约束严格 |

### 8.4 宇宙学观测约束

- **$\Omega$_b h$^{2}$ = 0.02225 ± 0.00016**（Planck 2015，<1% 精度）
- **重子物质 < 20% 宇宙物质** → **暗物质必为非重子**
- **MACHO 双重排除**：
  1. EROS 微透镜 < 8%（排除 0.1–10 $M_\odot$）
  2. BBN + CMB 重子预算
- **MOND**：星系尺度成功（Tully-Fisher）；**星系团与 CMB 强冲突**；
  Bullet Cluster 2006 是最大挑战

### 8.5 探测实验

| 实验 | 类型 | 状态 |
|------|------|------|
| DAMA (1998-) | 直接 | 9×9.7 kg NaI(Tl)；报道年调制（有争议）|
| XENON1T / XENONnT | 直接 (LZ 2022, PandaX-4T) | 大幅压缩 WIMP 截面参数空间 |
| Fermi dwarf galaxies | 间接 | 排除 < 100 GeV 多数 WIMP |
| ADMX | 轴子 | 覆盖 1.9–3.3 $\mu$eV |
| ATLAS/CMS mono-X | LHC | 无发现 |

### 8.6 "WIMP 时刻"现状（2018 视角）

- Bertone 2010（Nature）："WIMP 时刻已到"——要么发现要么范式衰落
- **2018 年现实**：直接探测 20 年 null 结果 + LHC 无 SUSY → 参数空间**大幅压缩**
- **SUSY 吸引力非暗物质驱动**——还解决电弱等级问题 + 规范耦合统一
- WIMP 范式面临衰落；非 WIMP 候选体（fuzzy dark matter、dark photon、hidden valley）正在兴起

---

## 9. 跨论文共享概念与方法论

### 9.1 太阳丰度是"基准输入"的共同认知

所有 7 篇论文共享一个核心假设：**太阳化学组成是恒星物理、核合成、星系化学
演化和宇宙学的基准输入**。具体体现：

- **GS98**：构建 SAD（Standard Abundance Distribution）；直接支撑恒星模型
- **Lodders 2003**：区分大气 vs 太阳系丰度，给出冷凝温度基准
- **AGSS09**：3D non-LTE 系统性重测，Z 下降 30% 影响所有下游
- **Gies & Lambert 1992**：B 星 CNO 检验 CN-cycle 混合，用太阳丰度为参考
- **Kewley 2001**：星暴星系诊断图与 W-R 星 C/N/O 核合成产物的释放
- **Dieterich 2014**：太阳金属丰度直接决定演化模型的氢燃烧极限位置
- **Bertone & Hooper 2018**：$\Omega$_b h$^{2}$ 约束与太阳邻域密度（Oort 1932）

### 9.2 关键交叉引用链

```
GS98 Fe=7.50
  └→ AGSS09 Fe=7.50 (3D 确认)
        └→ 陨石 Fe=7.50 (完美一致)

AGSS09 Z=0.0134
  └→ 恒星模型 → 需 +10-20% 不透明度（未解）
        └→ 日震 R_BCZ 张力

Lodders 2003 沉降修正 +0.074 dex
  └→ 原太阳 vs 光球差 16% 金属度

AGSS09 Z/X=0.0181  vs  Lodders 2003 Z/X=0.0177
  └→ Dieterich 2014 演化模型偏差 ~400 K

AGSS09 CNO
  └→ Gies & Lambert 1992 B 星 CNO 检验
  └→ Kewley 2001 W-R 星 N 初级/次级转折点
  └→ Borexino SNO+ CNO 中微子

GS98 Y=0.248
  └→ Lodders 2003 Y=0.2377 (偏低)
  └→ AGSS09 Y=0.2485 (回到 GS98 值)
```

### 9.3 方法论对比

| 方法 | 论文 | 作用 |
|------|------|------|
| 1D 半经验光球模型 | GS98 | Fe 丰度（被 3D 取代）|
| Anstee-O'Mara 碰撞展宽 | GS98 | 解决 Fe 争议 |
| 3D 流体动力学 + non-LTE | AGSS09 | 系统性重测 |
| SSM 标度法 | Lodders 2003 | 反推原太阳丰度 |
| CONDOR 平衡冷凝 | Lodders 2003 | 83 元素冷凝温度 |
| LTE + non-LTE 双通道 | Gies & Lambert 1992 | B 星 CNO |
| Maeder-Meynet 演化轨对比 | Gies & Lambert 1992 | CN-cycle 混合定量 |
| 双代码交叉验证（PEGASE/STARBURST99）| Kewley 2001 | 诊断图鲁棒性 |
| 色温插值 + 迭代 SED | Dieterich 2014 | 几乎模型无关 T_eff |
| 半径极小判据 | Dieterich 2014 | 恒星/褐矮星边界 |
| 维里定理 + 多尺度综合 | Bertone & Hooper 2018 | 暗物质证据 |

---

## 10. 关键数值速查表

### 10.1 太阳丰度数值

| 量 | A&G 1989 | GS98 | Lodders 2003 (大气) | AGSS09 |
|----|---------|------|---------------------|--------|
| X | 0.70 | 0.735 | 0.7491 | 0.7381 |
| Y | 0.28 | 0.248 | 0.2377 | 0.2485 |
| Z | 0.02 | 0.017 | 0.0133 | 0.0134 |
| Z/X | 0.0267 | 0.023 | 0.0177 | 0.0181 |
| A(He) | 10.93 | 10.93 | 10.899 | 10.93 |
| A(H) | 12.00 | 12.00 | 12.00 | 12.00 |
| A(Li) | — | 1.10 | — | 1.10 |
| A(Be) | — | 1.40 | — | 1.40 |
| A(B) | — | 2.55 | — | 2.55 |
| A(C) | 8.52 | 8.52 | 8.39 | 8.43 |
| A(N) | 8.17 | 7.97 | 7.83 | 7.83 |
| A(O) | 8.86 | 8.83 | 8.69 | 8.69 |
| A(Ne) | 8.01 | 8.08 | — | 7.93 |
| A(Na) | 6.24 | 6.33 | — | 6.33 |
| A(Mg) | 7.55 | 7.58 | — | 7.58 |
| A(Al) | 6.45 | 6.47 | — | 6.45 |
| A(Si) | 7.51 | 7.55 | — | 7.51 |
| A(S) | 7.17 | 7.33 | — | 7.18 |
| A(Ca) | 6.35 | 6.30 | — | 6.34 |
| A(Fe) | 7.50 | 7.50 | — | 7.50 |
| 12C/13C | — | — | — | 86.8 ± 3.8 |
| D/H | — | — | — | (2.0±0.2)×$10^{-5}$ |

### 10.2 核合成相关基准

| 量 | 值 | 来源 |
|----|----|------|
| 太阳 s 过程 Ba | 2.13 | AGSS09 |
| 太阳 Eu | 0.31 | AGSS09 |
| 太阳 Pb | 1.95 | AGSS09 |
| 太阳 Th | 0.09 | AGSS09 |
| C/O 比（数密度）| 0.28 | AGSS09 |
| CNO 循环平衡 N↑ | — | 恒星演化 |
| N 初级/次级转折点 | 0.23 Z☉ | Kewley 2001 |

### 10.3 暗物质关键数值

| 量 | 值 |
|----|----|
| $\Omega$_b h$^{2}$ (Planck 2015) | 0.02225 ± 0.00016 |
| 重子占宇宙物质 | < 20% |
| MOND $a_{0}$ | 1.2 × $10^{-10}$ m/s$^{2}$ |
| WIMP $\sigma$v | ~$10^{-26}$ cm$^{3}$/s |
| Coma M/L (Zwicky 1937) | ≈ 500 |
| Oort 1932 太阳邻域 | 0.092 $M_\odot$/pc$^{3}$ |
| 暗物质上限 (Oort) | ≤ 0.05 $M_\odot$/pc$^{3}$ |
| EROS MACHO | < 8% |

---

## 11. 开放问题与研究前沿

### 11.1 太阳物理

1. **AGSS09 vs 日震张力**（AGSS09 的"遗产"）：不透明度缺口无原子物理支持
2. **AGSS09 vs LPG2009 vs GS02** 的 Z/X 之争（0.0181 vs 0.0141 vs 0.0208）
3. **太阳中微子（Borexino, SNO+）** 直接测量 CNO 循环中微子通量 → 检验 CNO 丰度
4. **3D MHD 模型**（含磁场）对丰度的影响
5. **OPAL vs OP 不透明度**最新比较

### 11.2 恒星核合成与化学演化

1. **AGSS09 的 C/O 比**（0.28）对巨行星大气化学与系外行星形成的影响
2. **太阳 s/r 过程混合比**：Ba, La, Ce, Eu, Pb 与陨石一致 → 可靠基准
3. **Th、U** 作为核合成 + 银河年龄的关键探针
4. **SN Ia vs SN II 对太阳 Fe 的贡献比例**
5. **B 星 CN-cycle 混合的普遍性**（Gies-Lambert 选择偏差：V sin i < 100 km/s）

### 11.3 暗物质

1. **WIMP 范式衰落**：直接探测 30 年 null + LHC 无发现
2. **非 WIMP 候选体**：fuzzy dark matter、dark photon、hidden valley、asymmetric DM
3. **$\Lambda$CDM 小尺度危机**：missing satellites, cusp-core, too-big-to-fail
4. **$H_{0}$ tension**：Planck 67.4 vs 局部 74 km/s/Mpc
5. **$\sigma$$_{8}$ tension**：CMB vs 弱引力透镜
6. **DAMA 年调制信号**的争议

---


## 11.5 现代观测实验（04 域，2021 后）

库内实验域 4 篇观测为天体物理背景提供**实测锚点**：

- **LHAASO 2021（Nature 594:33）**：12 个银河系源 >100 TeV γ、最高 **1.4 PeV**（J2032+4102）——首次 background-free 证实 PeVatron，直接约束 SNR/脉冲星风云的粒子加速上限（与 §11.2 核合成-宇宙线交叉相关）。
- **AMS-02 2015（PRL 114:171103）**：质子谱 1 GV–1.8 TV，谱指数 >100 GV 变硬（99.9% 排除单幂律）——约束传播与源谱，是丰度/核合成背景下"宇宙线成分"的精密测量。
- **IceCube 2013（Science 342:1242856）**：28 起高能中微子（~4σ 超出大气背景）——多信使探针，与 §8 暗物质（WIMP 湮灭产生中微子）和 UHECR 起源关联。
- **HESS 2016（Nature 531:476）**：银河中心扩散 γ + Sgr A\*，PeVatron 质子加速证据——银河中心 CR 密度探针。

**与本节主题的联系**：γ/中微子通道是"丰度-核合成"之外观测宇宙线的窗口；IceCube 中微子与 §8 暗物质间接探测同通道竞争；LHAASO/HESS 的 PeVatron 判读依赖 SNR 模型（caprioli-2014 效率 ~10–20%）。

## 12. 建议的文献阅读顺序

### 入门（建立丰度概念框架）

1. **Grevesse & Sauval 1998 (GS98)** — 标准太阳组成的权威综述，建立基准
2. **Asplund et al. 2009 (AGSS09)** — 现代太阳丰度的最新权威

### 太阳系与行星科学

3. **Lodders 2003** — 太阳系丰度与冷凝温度的完整基准
4. **Palme & O'Brien 2007** — CI 陨石综述

### 恒星演化与核合成

5. **Gies & Lambert 1992** — B 星 CNO 与 CN-cycle 混合的观测证据
6. **Maeder & Meynet** 演化轨系列 — CN-cycle 定量匹配

### 星系化学与诊断图

7. **Kewley et al. 2001** — 星暴星系诊断图与 W-R 物理
8. **Kennicutt 1998** — SFR 定标
9. **Famaey & McGaugh 2012** — MOND 综述

### 暗物质

10. **Bertone & Hooper 2018** — 暗物质历史综述（本文）
11. **Sanders 2010**（Cambridge UP）— 暗物质历史专著
12. **Trimble 2013** — 天体物理视角补充

---

## 13. 与核合成研究的具体联系

| 核合成主题 | 关键输入 | 相关论文 |
|-----------|---------|---------|
| **主序核合成（pp, CNO 循环）** | 太阳 CNO 初始丰度 | AGSS09, Gies-Lambert 1992 |
| **氦燃烧（3$\alpha$, $\alpha$+$\alpha$）** | 太阳 He 丰度 | GS98, AGSS09 |
| **碳燃烧 / 氧燃烧 / 硅燃烧** | Fe = 7.50 基准 | AGSS09 |
| **s 过程（热/弱/主/极强）** | 太阳 Ba, La, Ce, Eu | AGSS09 + 陨石 |
| **r 过程** | 太阳 Eu, Os, Ir, Pt | AGSS09 + 陨石 |
| **rp 过程 / p 过程** | 太阳 Mo, Ru, Ag, In | AGSS09 + 陨石 |
| **大质量星核合成产物释放** | W-R 星质量损失 | Kewley 2001 |
| **星系化学演化** | C/O 比, [Fe/H] 演化 | AGSS09, Kewley 2001 |
| **低质量恒星演化** | 太阳 Z/X = 0.018 | AGSS09 → Dieterich 2014 |
| **暗物质与核合成** | $\Omega$_b h$^{2}$, 原初核合成 | Bertone-Hooper 2018 |

---

## 14. 元数据

- **来源**：本文件综合 `03_stellar-nucleosynthesis/` 下 7 篇论文的精读分析
- **生成方式**：基于各论文 `literature_analysis/` 目录下的分析文件
- **覆盖论文**：GS98, Lodders 2003, AGSS09, Gies-Lambert 1992, Kewley 2001,
  Dieterich 2014, Bertone & Hooper 2018
- **面向主题**：太阳丰度作为核合成/化学演化基准
- **最后更新**：2026-08-12

