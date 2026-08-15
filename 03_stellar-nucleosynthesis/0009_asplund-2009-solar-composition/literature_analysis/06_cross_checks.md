> 本章属于：[[03_stellar-nucleosynthesis/0009_asplund-2009-solar-composition/literature_analysis/00_overview.md|Asplund et al. (2009) AGSS09]]
>
> 下一章：[[03_stellar-nucleosynthesis/0009_asplund-2009-solar-composition/literature_analysis/07_figures_tables.md|07_figures_tables.md]]

# 6. Cross-Checks: Meteorites, Solar Neighborhood, Helioseismology, Neutrinos（§4）

## 6.1 §4.1 Meteorites（陨石）

### 6.1.1 方法

- [FACT] 最原始的是 **CI 碳质球粒陨石**（C1），只有 5 颗：Alais, Ivuna, Orgueil, Revelstoke, Tonk。
- [FACT] Orgueil 最大、被分析最多。
- [FACT] 优势：**质谱精度极高**（含同位素）。
- [FACT] 代价：**挥发元素 H, C, N, O, 惰性气体严重亏损**（恰好是丰度最高的元素）→ 陨石丰度必须以 **Si = $10^{6}$** 归一。

### 6.1.2 归一化

- [FACT] 陨石原数据：N_Si = $10^{6}$
- [FACT] 换算到天文标度：**log $\epsilon_{\rm X}$ = 1.51 + log N_X**（用本文光球 Si 归一，log $\epsilon_{\rm Si}$ = 7.51）
- [FACT] 归一化的元素选择：本文只用 Si；AG89 用 11 个元素；Lodders 2009 用 39 个元素。实践上结果差别不大，但引入任意性。

### 6.1.3 一致性检验

- [FACT] Fig 7：57 个非挥发元素中：
  - 均值差 **0.00 ± 0.05 dex**（45 个非挥发元素，光球不确定度 < 25%）
  - **只有 10/57 超出合并不确定度**（统计预期 ~18/57）→ 说明本文误差估计**略偏保守**。
- [FACT] **例外元素（>0.1 dex 偏差）** 10 个：Cl, Au, Tl（仍勉强一致）；W, Rb, Hf（混杂/连续谱放置）；Co（non-LTE 高估）；Rh, Ag, Pb（低激发态 neutral 线受 non-LTE 影响）。
- [FACT] 显著改进：W 与陨石的差从 AGS05 的 +0.49 dex 降到 +0.20 dex。
- [CRITIQUE] 需注意：陨石尺度以 Si 为锚点 → 一致性不能证明**没有**扩散（§3.11），因为所有重元素相对 Si 基本不变。

## 6.2 §4.2 Solar Neighborhood（太阳系近邻）

### 6.2.1 校正

为与"今日太阳"对比，必须校正：
- [FACT] **太阳内部扩散**：所有金属下沉 ~0.04 dex（Turcotte & Wimmer-Schweingruber 2002）→ 原太阳丰度 = 光球 + 0.04（Z > He 时）
- [FACT] **银河系化学富集**（4.56 Gyr）：0.05–0.15 dex（Chiappini, Romano & Matteucci 2003；Prantzos 2008），元素相关

### 6.2.2 太阳型矮星

- [FACT] 多数大样本研究（Bensby 2005；Fuhrmann 2008；Ramírez 2007；Reddy 2003 等）**相对太阳做差分**以消除 gf 不确定度 → 只能判断太阳是否"普通"。
- [FACT] Fuhrmann (2008) 25 pc 内体积完备样本：[Fe/H] = −0.02 ± 0.18
- [FACT] Holmberg, Nordström & Andersen (2008) 4–6 Gyr 等龄星 40 kpc 内：[Fe/H] = −0.00 ± 0.10
- [FACT] Meléndez et al. (2009) 11 颗 solar twins：23 个元素的 X/Fe 比都不差 0.06 dex
- [INTERPRETATION] **太阳是一颗普通的薄盘 G 型矮星**。

### 6.2.3 B 型主序星

- [FACT] 最精确的近邻 B 星 non-LTE 分析：**Przybilla, Nieva & Butler (2008)**（Table 5）。
- [FACT] 校正太阳扩散后，太阳与 B 星在 **O、Ne、Mg** 特别一致。
- [FACT] 仍存的差异：太阳 **C、N、Fe** 略**高于** B 星，与"银河系化学富集"预期相反。
- [CRITIQUE] 可能因：太阳/B 星分析有误，或真实存在"低金属气体晚期吸积到太阳邻域"。

### 6.2.4 H II 区（Orion 等）

- [FACT] 来自 Esteban et al. (2004, 2005)、García-Rojas & Esteban (2007)，外推到银河系半径 8 kpc。
- [FACT] 已知陷阱：
  1. 未观测到的电离态修正
  2. **温度涨落**效应
  3. **复合线**（许可）丰度通常显著大于**碰撞激发线**（禁线）
  4. **尘埃凝结**：C、O 在 Orion 尘埃修正约 0.1 dex；Mg、Fe 主要固相 → 无法测总丰度
- [FACT] 综合比较：太阳 vs H II 区**非常满意**（校正扩散 + 微小富集后）。

### 6.2.5 星际介质（ISM）

- [FACT] ISM 温度更低 → 尘埃凝结更多 → 是比 H II 区**更差**的化学量具。
- [FACT] 挥发元素气相丰度（Soia 2004 C, Jensen 2005 O, Jensen 2007 N）总体**支持**本文推荐值。
- [FACT] 旧的高 O（8.83–8.93）难以在尘埃中隐藏足够 O（Jensen 2007）。

### 6.2.6 银河化学演化模型

- [FACT] Chiappini, Romano & Matteucci (2003) 的模型预测 vs 观测：
  - O、Ne、Mg（静平衡燃烧 + SN II 抛射）：模型最可靠，与太阳和近邻一致。
  - Fe 等（爆炸燃烧 / SN Ia 贡献）：模型不确定。
- [FACT] 太阳近邻的**年龄-金属丰度关系**（Holmberg et al. 2008）：**0.018 dex/Gyr**，仅为模型预测的一半。
- [CRITIQUE] 可能解释：
  1. 太阳邻域恒星形成率比模型低；
  2. **近期银河系外原始气体内吸积**。

## 6.3 §4.3 Helioseismology — 全文最大张力

### 6.3.1 方法

- [FACT] 太阳 p-mode 振荡穿透深度不同 → 反演**内部声速剖面** c(r)，与 SSM 预测对比（Basu & Antia 2008 综述）。

### 6.3.2 关键事实

- [FACT] **GS98 化学组成 → SSM 声速与日震吻合极好。**
- [FACT] **AGS05 或 AGSS09 → 吻合被破坏**（Bahcall et al. 2005；Basu & Antia 2004, 2008；Delahaye & Pinsonneault 2006；Guzik, Watson & Cox 2005；Turck-Chièze et al. 2004）。
- [FACT] 作者原话："**'better is worse'**"——越精确的丰度，反而越不符。
- [FACT] 声速偏差最大位置：**对流区底部以下**（R ≈ 0.71 R⊙ 起），Fig 8。
- [FACT] AGSS09 相比 AGS05 略缓解（因 C、N、O、Fe、Ne 略上调），但**仍然显著**。

### 6.3.3 除了声速，还有两个偏差

- [FACT] **对流区底部深度**：SSM 给出 R_BCZ ≈ **0.725 R⊙**，日震测量 **0.7133 ± 0.0005 R⊙** → SSM 偏**浅**。
- [FACT] **校准 He 丰度**（匹配太阳质量、光度、温度、年龄）：SSM 给出 Y_S ≈ **0.238**，日震 **0.2485 ± 0.0034** → 偏差约 0.01。
- [FACT] **问题存在于对流包层、辐射内部、核心三个区域**（低阶 p-mode Chaplin 2007、g-mode García 2007）。

### 6.3.4 已提出/排除的解决方案

| 方案 | 来源 | 状态 |
|---|---|---|
| 不透明度 +10–20%（R = 0.4–0.7 R⊙, T = 2–$5\times10^{6}$ K） | Bahcall et al. 2005 | 需要大幅修正；Opacity Project 比 OPAL 大仅 ~3%，不太可能 |
| 不透明度 +12% | Serenelli et al. 2009 | 同样缺依据 |
| 更强元素扩散 | Asplund et al. 2004 | 需约 2× 预测值；能缓解声速但不能解决 He 和 BCZ |
| 晚期贫金属气体吸积 | Castro, Vauclair & Richard 2007 | 同样不能解 He / BCZ |
| **Ne 丰度 ×3（+0.5 dex）** | Antia & Basu 2005；Bahcall et al. 2005 | Drake & Testa (2005) 提出过高 Ne/O 但被证伪（§3.9） |
| **内部重力波能量沉积** | Arnett, Meakin & Young 2005 | 方向正确，但缺乏定量建模 |
| 光球丰度本身有误 | — | 作者最后说：若以上都不行，只能怀疑光球丰度，但找不到明显错误来源 |

### 6.3.5 综合判断

- [FACT] **这是 AGSS09 遗留的最大开放问题**。
- [FACT] 作者最后给出一个"可能性"声明：可能是**多个因素叠加**，但"这样的微调显得刻意"。

## 6.4 §4.4 Solar Neutrinos

- [FACT] 金属丰度 → 核心条件 → pp 链与 CNO 循环中微子通量。
- [FACT] 最敏感元素：C, N, O, Si, Fe（Bahcall & Serenelli 2005）。
- [FACT] Pena-Garay & Serenelli (2008) 用 SuperKamiokande I+II、SNO、Borexino 数据分析 GS98 vs AGS05 模型：
  - 现有数据给出的 **$^{7}{\rm Be}$、$^{8}{\rm B}$ 中微子通量介于两模型预测之间**
  - 作者推测太阳中微子会**偏向 AGSS09**（新丰度）。
- [FACT] **更直接检验**：测量 $^{13}{\rm N}$、$^{15}{\rm O}$ $\beta$-衰变中微子（分别来自 $^{12}{\rm C}$ + p、$^{14}{\rm N}$ + p）→ Borexino 未来几年 + SNO+（2011 后）有望给出明确答案。

## 6.5 §4 综合评价

- [FACT] **陨石**：与本文一致度极高（45 元素均值差 0.00 dex）。
- [FACT] **B 星、H II 区、ISM**：一致度非常好，支持本文推荐值。
- [CRITIQUE] **日震学**：显著不一致，是 AGSS09 的"阿喀琉斯之踵"。
- [FACT] **太阳中微子**：可能支持新丰度，但尚未有决定性检验。