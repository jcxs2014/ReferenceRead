> 本章属于：Synthesis of the elements in stars, forty years of progress (Wallerstein et al., 1997)
>
> 上一章：[[03_stellar-nucleosynthesis/0004_wallerstein-1997/literature_analysis/01_preface_introduction.md|01_preface_introduction.md]]
>
> 下一章：[[03_stellar-nucleosynthesis/0004_wallerstein-1997/literature_analysis/03_hydrogen_burning.md|03_hydrogen_burning.md]]

# 2. 恒星演化模型（Stellar Evolution, Iben, Jr.）

**本章作者**：Icko Iben, Jr.（芝加哥大学，恒星演化计算权威，是本文最重要的单作者章节之一）

## 2.1 A. Historical preliminary

[FACT] 自 B2FH 发表以来，恒星演化领域取得巨大进展。B2FH 原文承认"红巨星阶段以后的恒星演化整个理论问题被当前计算技术难以处理的问题所困扰"。

[FACT] 进展主要源于两个因素：
1. **计算机硬件革命**：速度与内存的惊人增长
2. **Henyey, Forbes & Gould (1964)** 引入的隐式松弛法（implicit relaxation method）求解恒星结构方程

[FACT] 但计算能力提升本身不够——输入物理必须完善：

**关键物理缺失清单（1957 年 vs 1997 年）**：
- **12C** 第二激发态 $\gamma$ 宽度：B2FH 时代不确定至少一个数量级（Hoyle 1954 预言的 7.65 MeV 态对 3$\alpha$ 过程至关重要）
- **强中微子损失**：中间质量恒星晚期演化中的中微子损失对初始质量—最终白矮星质量的映射至关重要。弱相互作用现代表述（Feynman-Gell-Mann 1958）在 B2FH 之后才建立；全计算至 1960s 末（Beaudet, Petrosian, Salpeter 1967; Festa & Ruderman 1969）
- **中性流中微子贡献**（~15–30%）：1967/1968 电弱统一理论（Weinberg/Salam）之后才引入，但 Dicus 1972 才开始计算
- **Rosseland 平均不透明度**：1955 年 Keller & Meyerott 只有 H+He 连续不透明度；Cox 1965 首次系统引入线跃迁；Iglesias, Rogers & Wilson 1990; Seaton 1994; Rogers & Iglesias 1992 之后才覆盖内部广泛条件的精确不透明度
- **电子热导率**：Hubbard & Lampe 1969（非相对论），Canuto 1970（相对论）
- **物态方程 (EOS)**：同期大幅改进
- **观测窗口**：探测器技术进步 + 太空望远镜，使红外、紫外、X 射线观测成为可能

## 2.2 B. Evolution of single stars that become white dwarfs

### 2.2.1 1. Overview（H-R 图总览）

[FACT] **Figure 1**（本文最重要的图）展示：
- 右半部分 (log T_eff ≤ 4.7)：初始质量 0.2, 1, 5, 25 $M_\odot$ 的模型单星演化轨迹，叠加真实亮星位置
- 粗线表示核心核燃烧阶段（时标 ~ 核时标）
- 0.6 $M_\odot$ 与 0.85 $M_\odot$ 虚线轨迹：AGB 超风阶段模型，展示类星体星云 (PN) 中心星的演化
- 左半部分：LMXB 的最大光度，恒定半径线 ~ 10^25 cm（相当 1.4 $M_\odot$ NS 或 10 $M_\odot$ BH 的半径）
- 星形符号：USXRs、新星后中心星、PN 中心星

[FACT] 主序寿命 $\tau$_MS ∝ M^(−2.25)：
- 1 $M_\odot$：~10^10 年（~1 Hubble 时间）
- 25 $M_\odot$：~7×10^6 年

[FACT] <0.8–1.0 $M_\odot$ 的恒星在主序寿命内不足以离开主序（因此 0.2 $M_\odot$ 轨迹极短）

[FACT] **He 核心燃烧阶段**：
- <2.3 $M_\odot$ 模型在此阶段 He 核质量几乎相同 → 光度几乎相同 (~50 L☉)，寿命 ~10^8 年
- He 燃烧时标 = 主序寿命的 ~25%（中质量）至 ~10%（大质量）

[FACT] **红巨星/超巨星序列**（Fig. 1 中最大号圆点）：
- (a) M ≤ 2.3 $M_\odot$：惰性电子简并 He 核 + H 燃烧壳层（RGB）
- (b) 2.3–20 $M_\odot$：核心 He 燃烧 + H 壳层燃烧的第一阶段
- (c) 具有 $\nu$ 冷却的 CO 核 (1–9 $M_\odot$) 或 ONe 核 (9–11 $M_\odot$) + 交替 H/He 壳层燃烧（AGB 星）

[FACT] **白矮星形成率**：~0.5–1 yr^(-1)，通过比较观测的 WD 数-光度分布与冷却模型得到；与 1–11 $M_\odot$ 恒星的形成率一致

[FACT] **质量损失 (Mass loss)**：
- Deutsch (1956) 观测到 $\alpha$ Her（M 超巨星）高质量损失率
- Hoyle (1956) 推测质量损失对巨/超巨星演化影响可能超过核过程
- Paczynski (1971a) 与 Härm & Schwarzschild (1975) 首次定量计算 AGB 质量损失

[FACT] **AGB 超风 (superwind)** 机制（Bowen 1988; Bowen & Willson 1991）：
1. 脉动 → 激波（难以计算，因为包层是强对流的）
2. 激波加热 → 大气膨胀
3. 脉动周期中的低温区域形成并生长尘埃颗粒
4. 辐射压驱动颗粒至超逃逸速度，颗粒拖曳气体逸出

[FACT] 当脉动周期 > 400 天时，质量损失率 ~10^(-5)–10^(-4) $M_\odot$/yr（比核燃烧处理物质速率大 10^2–10^3 倍）

[FACT] **WD 初始-最终质量关系**：WD 质量 ≈ 模型刚成为双壳层燃烧 AGB 星时的电子简并核质量 + 仅几个百分之一 $M_\odot$ 的核燃烧产物

[FACT] 银河系中观测到的 WD 质量分布在 ~0.55–0.65 $M_\odot$ 处峰值（Liebert & Bergeron 1995）

### 2.2.2 2. Nucleosynthesis and dredge-up prior to the AGB phase

[FACT] **四次主要挖掘 (dredge-up) 事件**（单星演化中发生的对流混合将内部核合成产物带至表面）：

**(i) 第一次挖掘 (First dredge-up)**：
- 发生在 H 燃烧消耗约 10% 星体质量（M < 2.3 $M_\odot$）或 0.1 $M_\odot$(M/$M_\odot$)^1.4（大质量）之后
- 对流包层向内挖掘 → 依次穿越：Li 破坏区 → 12C/13C 交换区 → 14N 生成区 →（大质量星）16O 破坏/14N 生成区
- 表面结果：Li 下降 → 12C/13C 比下降 → 12C 下降 → 14N 上升 →（大质量）16O 下降，14N 再上升
- [FACT] Iben (1964, 1965) 的预测与场巨星的 CNO 观测基本一致（Lambert & Ries 1981）
- [FACT] 但 <1.3 $M_\odot$ 巨星 Li 耗竭被低估多达两个数量级（Luck & Lambert 1982）——暗示**对流超射 (convective overshoot) 或差旋 (differential rotation) 比标准第一次挖掘更重要**

**(ii) He 闪 (Helium flash)**（<2.3 $M_\odot$）：
- He 核电子简并 → He 点火前核心达到 ~0.45–0.5 $M_\odot$ 时 He 闪
- 闪传播至中心解除简并 → 星体成为"clump" 星（Fig. 1 中 L~50L☉ 的重线段）

**(iii) 第二次挖掘 (Second dredge-up)**：
- 在 5–9 $M_\odot$ 模型中：He 燃烧壳层接近 H-He 不连续面时
- CO 核质量 >0.56–0.61 $M_\odot$ 后触发
- 鲜活的 4He 与 14N 被挖掘到表面

[FACT] **9–11 $M_\odot$ 大质量模型的第二次挖掘极为复杂**：CO 核部分简并 + C 燃烧闪 + He 燃烧闪，能量来源可来自 C 燃烧、He 燃烧或引力热能（gravothermal energy）
- 9 $M_\odot$ 模型：第一次 C 壳层闪 + 引力热能驱动挖掘（García-Berro et al. 1997）
- 10 $M_\odot$ 模型：C 燃烧晚期 + He 与 C 燃烧共同驱动（Ritossa et al. 1996）
- 10.5 $M_\odot$ 模型：三种能量源均起作用（Iben, Ritossa, García-Berro 1997）

### 2.2.3 3. Nucleosynthesis and dredge-up during the AGB phase

**这是论文中最关键、最具研究价值的章节之一**：

[FACT] **热脉冲 AGB (TPAGB) 星**：~97% 能在 Hubble 时间内离开主序的恒星都成为 AGB 星，经历 He 壳层闪（thermal pulses）

[FACT] **TPAGB 星的宇宙学重要性**：
- 寿命 ~10^5–10^6 年（极短）
- 产生宇宙中**大部分 12C** 与**大部分 s 过程同位素**
- 也产生大部分 14N（第一次、第二次挖掘 + 第三次挖掘中的 12C→14N）

[FACT] **He 壳层闪机制**：
- 与 WD 吸积氦引发 nova 爆发物理相同
- H 燃烧静止期向 CO/ONe 核上方沉积 He 的速率约为维持静止 He 燃烧所需速率的 1/10
- He 层增长、压缩、加热 → 最终 He 点火
- **He 燃烧速率 ∝ T^(40)**（对温度极敏感）
- 核能释放速率 > 热扩散速率 → 热核失控

[FACT] **He 壳层闪产生的对流区**从 He 燃烧区底部延伸至近 H-He 不连续面；熵壁垒（辐射压贡献显著）阻止其穿透至 H 富集物质

**中子源与 s 过程**：

[FACT] **闪前的 He 层**：14N 丰度 = 原始 CNO 元素丰度

[FACT] **闪初期**：14N 完全通过 14N($\alpha$,$\gamma$)18F($\beta$+,n)18O($\alpha$,$\gamma$)22Ne 转化为 22Ne

[FACT] **两个 s 过程中子源**：

| 中子源 | 触发条件 | 适用模型 | 关键数值 |
|---|---|---|---|
| **22Ne($\alpha$,n)25Mg** | 对流区底部温度 > 3.5×10^8 K | CO 核质量 ≥ 0.9 $M_\odot$ 的 AGB 星 | s 过程同位素丰度比太阳大几百倍 |
| **13C($\alpha$,n)16O** | 13C 口袋 (pocket) 形成后，~1.5×10^8 K | CO 核质量 < 0.9 $M_\odot$ 的 AGB 星 | 主要 s 过程中子源 |

[FACT] **B2FH 的历史性误差**：B2FH 猜测 21Ne($\alpha$,n)24Mg 可能是恒星中子源，**但完全没有考虑 22Ne($\alpha$,n)25Mg**（Cameron 1961 之后才被认识）

[FACT] **13C 口袋 (pocket) 的起源**（至今未完全解决的开放问题）：
1. Schwarzschild & Härm (1967)：对流壳层触及 H-He 不连续面 → 摄取 H → 与 12C 反应生成 13C → 内扩散至 ~1.5×10^8 K 产生中子。但含辐射压的计算未重现摄取。
2. Iben & Renzini (1982a,b); Hollowell & Iben (1989)：低金属丰度 AGB 星中，对流壳层消退后，**半对流混合 (semiconvective mixing)** 让 12C 与 1H 重叠 → 收缩加热 → 形成 13C 小口袋。但此机制在太阳金属丰度 AGB 星中不成立（Iben 1983）。
3. Straniero et al. (1995)：即使口袋形成，它可能在 H 燃烧静止期作为**局部中子源**，而非闪中对流壳层中的分布源；但两种情形产生的 s 过程丰度分布**基本相同**
4. **Blöcker et al. (1997) & Herwig et al. (1997)**：第三次挖掘过程中**对流超射 (convective overshoot) 超出对流包层底部**导致 13C 口袋形成——此机制后来被认识到实际上可从 Iben (1976) 图 9 中推断

[FACT] **第三次挖掘 (Third dredge-up)**：
- 发生在壳层闪的功率下降期
- He 燃烧产生的能量泄漏出富碳区域 → 增加穿过对流包层底部的能流 → 迫使包层底部向内（质量方向）移动进入部分 He 燃烧产物区
- 最初在无超射的大 CO 核模型中发现（Iben 1975a），后来在小 CO 核模型中借助对流超射重现（Iben & Renzini 1982; Iben 1983）

[FACT] **碳星 (Carbon stars) 的形成**：
- He 壳层闪 + 第三次挖掘 → 碳星（C > O 的恒星）
- 产生 s 过程同位素的超丰
- AGB 挖掘物质经历**仅部分 He 燃烧**，12C 质量丰度仅 ~0.15–0.25
- 这意味着 **12C($\alpha$,$\gamma$)16O / 3$\alpha$ 比率的不确定性对挖掘物质中 C 丰度的影响远小于对 C/O 比的影响**（重要结论）

[FACT] **3He 与 7Li 在中等质量星中的产生**：
- 3He 在主序星中心区域产生（Iben 1967b），比太阳低质量端（1–2 $M_\odot$）的 AGB 星保存并释放至 ISM——与类星体星云中高的 3He/H 比一致（Balsar et al. 1997）
- 7Li：高质 AGB 星中，3He + 4He → 7Be 在对流包层底部发生；若 7Be 能混合至较冷区域，7Be(e−,$\nu$)7Li 破坏 → Li 超丰（Cameron 1955; Cameron & Fowler 1971）
- [FACT] Sackmann & Boothroyd (1992) 构建 3–7 $M_\odot$ 演化模型，发现初始质量 **4–6 $M_\odot$** 的模型可重现 LMC 超锂巨星观测（Smith & Lambert 1989, 1990; Plez et al. 1993; Smith et al. 1995）

### 2.2.4 4. The born-again AGB phenomenon

[FACT] **后 AGB 星最终 He 壳层闪 (final helium shell flash)** 现象：
- Fujimoto (1977) 预言，Schönberner (1979) 数值模拟遇到，Iben et al. (1983, 1984) 用来解释 Abell 30 与 Abell 78 类星体星云中心的 He 富集、N 富集结（以 20–30 km/s 速度远离中心星）

[FACT] **最终闪 vs AGB 闪**：
- 闪时 He 层质量略小于 AGB 上触发闪所需质量（He 层部分简并 + 绝热压缩加热）
- 熵壁垒比 AGB 时小得多 → 对流壳层外缘穿透至 H 富集区
- H 被摄取、内扩散 → 与 12C 反应 → 注入熵使对流壳层分裂为两部分（下部 He 燃烧驱动，上部 H 燃烧驱动）

[FACT] **外层对流壳层组成**（质量分数）：
- 4He：76%
- 12C：20%
- 1H：仅几个百分之一
- 16O：痕量
- 随 H 燃烧进行，~5% 的 12C 转化为 14N

[FACT] 表面丰度 = 部分 He 燃烧产物与少量 H 富集物质混合后再经一次 H 燃烧的结果 → 高 L、低 T_eff → **"重生 AGB" (born again AGB)** 星的命名由来

[FACT] ~10% 后 AGB 星可能在 H 燃烧结束后经历最终 He 壳层闪；另有 ~15% 在 H 燃烧完成前经历最终闪。后一种情形下熵壁垒阻止 H 摄取。

[FACT] **Sakurai 天体**（Duerbeck & Benetti 1996）是已知的重生 AGB 星最新实例

### 2.2.5 5. Other mixing processes

[FACT] 除标准挖掘外，以下过程影响单星表面组成：
- **热与重力扩散 (Thermal & gravitational diffusion)**：Hyades 主序星 6400–7000 K Li 缺失（Boesgaard & Trippico 1986），可能由辐射轻浮力 (radiative levitation, Michaud 1986) 驱动
- **对流超射 (Convective overshoot)**：已在第三次挖掘中讨论
- **旋转诱导混合 (Rotation-induced mixing)**：M67 亚巨星中 Li 随离开主序的距离下降 → 暗示旋转混合至 Li 破坏温度（Deliyannis, King & Boesgaard 1996）
- **星风质量损失**：辐射风可移除后 AGB 星 H 富集表面层乃至 He 层（Iben & Tutukov 1996）；粒子扩散使除最轻同位素外的所有元素沉入 WD 内部

## 2.3 C. Evolution of massive single stars (NS/BH progenitors)

[FACT] 大质量星（>11 $M_\odot$）通过强烈的辐射星风 (radiative wind) 进行质量损失（Cassinelli 1979）：
- 质量损失率随初始质量与光度增加，可达 ~几 ×10^(−5) $M_\odot$/yr
- 对于 ≥30 $M_\odot$ 的星，质量损失时标与核燃烧寿命相当或更短——模型**必须**考虑质量损失

[FACT] **Wolf-Rayet (WR) 星**：
- 大质量星最终失去 H 富集包层，暴露完全 H 燃烧物质（WN 类：He+N 谱线）与部分 He 燃烧物质（WC 类：He+C+O 谱线）
- Langer (1989a,b) 的研究结论：
  - 核心质量范围：5 $M_\odot$ < M_WR < 20 $M_\odot$（与初始质量无关）
  - 质量损失率：Ṁ_WR ≈ (0.6–1.0)×10^(−7) (M_WR/$M_\odot$)^2.5 $M_\odot$/yr
  - 光度：4.8 ≤ log(L_WR/L☉) ≤ 5.5
  - 光球位于逃逸风内，核心边缘光学深度 ~10
  - WN 星初始质量 **远小于** WC 星前星

[FACT] **Humphreys-Davidson 禁区**：银河系中光度 >10^6 L☉ 且表面温度 <(1–3)×10^4 K 的恒星几乎不存在（Humphreys 1978; Humphreys & Davidson 1979, 1994）。De Jager (1984) 解释为光球不稳定性 → 质量损失率随光度急剧上升

[FACT] **初始质量 >50 $M_\odot$ 的单星在超新星爆发前不成为巨星**——这对大质量双星演化有重要含义

**SN 爆炸后的演化与核合成**：

[FACT] 大质量星内部演化（13 $M_\odot$ 以上）：
- 依次安静燃烧：C → Ne → O → Si
- 最终形成铁峰同位素（统计平衡态）的核心
- Fe-Ni 核收缩加热 → 部分光致分解为 $\alpha$ 粒子和中子
- 核心塌缩至核物质密度 → **SN II 爆炸**

[FACT] **SN 1987A 的关键证据**：
- 初始质量 ~20 $M_\odot$ 的星爆炸时，**~0.1 $M_\odot$ 的 56Fe 被抛射至 ISM**（Arnett et al. 1989 光变曲线分析）
- 56Ni → $\beta$ 衰变 → 56Co → $\beta$ 衰变 → 56Fe
- 激发态核能级退激产生的 $\gamma$ 射线帮助供能光变曲线
- [FACT] 这证明 **SN II 是宇宙中铁的强来源**

[FACT] **NS/BH 质量映射仍是未解决问题**：
- 核心坍缩—中子化—中微子捕获—核心反弹—包层抛射的物理尚未完全理论化
- 初始主序质量与最终 NS 或 BH 质量之间**没有安全的理论映射**
- 区分 NS 与 BH 的临界初始质量 M_crit 未知
- **本文采用具体假设**：M_crit = 40 $M_\odot$，M_NS = 1.4 $M_\odot$，M_BH = 10 $M_\odot$

[FACT] **SN 分类与演化联系**（Wheeler et al. 1995）：
- SN II：保留 H 富集包层的大质量星爆炸（红/蓝超巨星前星，如 SN1987A）
- SN Ib,c：先变为 WR 星再爆炸的大质量星
- SN Ia：可能涉及密近双星中 CO 白矮星爆炸

## 2.4 D. Close binary star evolution

### 2.4.1 1. Modes of mass transfer

[FACT] 密近双星演化三大机制：
1. **Roche 瓣充满 (Roche lobe filling)** → 物质转移
2. **共同包层 (Common Envelope, CE)**：供星质量 >> 吸星质量或供星有深对流包层时，吸星无法调节结构 → 物质填滿吸星 Roche 瓣 → CE 形成 → "鸡蛋搅拌器" 摩擦耗散 → CE 物质被驱散 → 轨道收缩
3. **角动量损失**：引力波辐射 (GWR) 或磁星风 (MSW)

[FACT] **CE 效率参数**：$\alpha$_CE = $\Delta$E_remove / $\Delta$E_bind
- 越小 → 轨道收缩越大
- 近几十年有争议（Iben & Livio 1993）
- 3D 光滑粒子流体动力学计算建议 $\alpha$_CE ≈ 1（Rasio & Livio 1996; Yorke et al. 1995）

[FACT] 银河系盘星出生函数（Iben & Tutukov 1984）：
$$\frac{d^3 n}{d \log A_0 \, dM_{10} \, dq_0} \sim 0.2 \, M_{10}^{-2.5} \, \text{yr}^{-1}$$
- 积分 $A_{0}$ = 10^−1–10^6, $M_{10}$ = 0.8–100, $q_{0}$ = 0–1 → n ≈ 1 yr^(−1)（银河系主序逃逸率）

[FACT] 轨道角动量守恒方程（保守转移）：
$$J_{orb} = M_{1f} M_{2f} \left(\frac{G A_f}{M_t}\right)^{1/2} = M_{10} M_{20} \left(\frac{G A_0}{M_t}\right)^{1/2}$$

### 2.4.2 2. Scenario modeling

#### a. 灾变变星 (CV) 与新星

[FACT] CV = WD + 低质量主序伴星（Roche 瓣充满）：
- 轨道周期 1.3–2 h：GWR 驱动质量转移，速率 (1–2)×10^(−10) $M_\odot$/yr
- 轨道周期 3–20 h：MSW 驱动，速率 10^(−9)–10^(−8) $M_\odot$/yr
- Porb ~ 3 h 时伴星完全对流 → MSW 消失 → 质量转移骤停 → GWR 收缩 → 再次 Roche 瓣充满

[FACT] **新星爆发 (Nova) 物理**：
- 吸积 H 富集物质在盘积累 → 部分扩散至 WD 表面 → 差旋产生 baroclinic 不稳定性（Fujimoto 1988, 1993）→ 强混合
- WD 吸积 ~10^(-5) $M_\odot$（Ṁ_WD ~ 10^(-9) $M_\odot$/yr 时）→ H 在吸积层底部点火
- 对流区向内扩展至 H 质量分数 ~0.01 的混合区，并向外扩展至表面 → 混合大量 CO/ONe 物质至外层
- 核能释放解除电子简并 → 包层膨胀至巨星尺度

[FACT] **L_max 与 M_WD 的关系**（Iben & Tutukov 1989）：
$$\frac{L_{max}}{L_\odot} = 46{,}000 \left(\frac{M_{WD}}{M_\odot}\right)^{0.26}$$
- Paczynski-Uus 关系（用于 PN 中心星）：L_max/L☉ = 59,000 (M_WD/$M_\odot$)^0.52
- 差异源于新星底层 WD 更冷、半径更小

[FACT] 银河系 CV 出生率 ~10^(−3) yr^(−1)

#### b. WD 合并：R CrB 星与 SN Ia

[FACT] **SN Ia 的"WD 合并"场景**（Iben & Tutukov 1984; Webbink 1984）：
- 椭圆星系（老年星群）中 SN Ia 发生，但 SN II 不发生 → 必须涉及双星
- 两颗中等质量主序星 → 两次 CE 事件 → 一对总质量 > Chandrasekhar 质量 (~1.4 $M_\odot$) 的 WD → GWR 使它们在 <Hubble 时间内合并 → 爆炸

[FACT] WD 合并时的物理（Tutukov & Yungelson 1979）：
- 质量比 <2/3 → 稳定质量转移
- 否则 → 低质量 WD 在动力学时标内转化为围绕更重 WD 的厚盘（Nomoto & Iben 1985; Saio & Nomoto 1985）
- 若角动量扩散足够快 → 塌缩后发生星体瓦解爆炸，将大量物质转化为铁峰元素（速度 ~10^4 km/s，与 SN Ia 观测一致）

[FACT] SN Ia 产生的同位素组合可解释某些其他类型 SN 不产生的同位素的丰度（Thielemann et al. 1997）

[FACT] **SN Ia 理论出生率 ~0.003 yr^(−1)**（Tutukov et al. 1992）与经验观测值一致（Baade & Minkowski 1957; van den Bergh 1987; van den Bergh & Tammann 1991）

[FACT] **8 个双 WD 系统已被发现，其中至少 3 个将在 <Hubble 时间内合并**

[FACT] **R CrB 星**（L > 7×10^3 L☉, T_eff ~ 7000 K, 极端 H 缺失，强 C 与 N 超丰）：
- 银河系估计 200–1000 颗
- 单星"重生"模型（Renzini 1990; Iben & MacDonald 1995）产生的核燃料太少、寿命太短
- **双星场景**（Webbink 1984; Iben & Tutukov 1984a,b, 1996a,b）：CO WD + He WD 合并 → 混合 → He 燃烧使 CO 核增长 → 若合并产物质量 >0.78 $M_\odot$ → 进入 R CrB 区域
- 燃料量为"重生"场景的 ~20 倍 → 预测银河系 200–600 个亮冷系统，与观测 200–1000 一致

[FACT] WD 2331+290 与 WD 0957-666 两个已知的将在 <Hubble 时间内合并的 WD 对，质量估计不排除 R CrB 演化

#### c. X 射线双星与脉冲星

[FACT] **LMXB** = NS 或 BH + 低质量主序/亚巨星供星：
- 理论出生率：~2×10^(−5) yr^(−1)（$\alpha$_CE=1）至 ~2×10^(−6) yr^(−1)（$\alpha$_CE=0.5）
- NS 吸积 ~0.01 $M_\odot$ → 自转周期降至毫秒范围 (<10^3×10^(-3) s) → 毫秒脉冲星 (MSP)
- 主序供星 → MSP + 供星被摧毁
- 亚巨星供星 → MSP + He WD 残余

[FACT] **HMXB** = NS 或 BH + OB 主序供星（吸积辐射星风）：
- 第一物质转移事件通常是保守的 → 轨道扩大
- 大质量供星 → 第一 CE 事件 → SNIb,c 爆炸 → 双星一般瓦解
- 最终：两颗高速 NS，自转 ~3 s 或更慢
- **Hulse-Taylor 脉冲星 (PSR 1913+16)** 是稀有的双 NS 保持束缚的例子

[FACT] **脉冲星出生率**：
- SNIb,c 在银河系的理论出生率 ~0.007 yr^(−1)
- 通过 HMXB 阶段形成 NS 的理论出生率 ~0.005 yr^(−1)
- 半经验脉冲星出生率 0.004–0.008 yr^(−1)（Lorimer et al. 1993）
- [FACT] **结论暗示：脉冲星主要由密近双星产生**

[FACT] **SN II 出生率**（单星或宽双星）~0.021 yr^(−1)（Tutukov & Yungelson 1993），与经验 SN II 出生率一致

## 2.5 本章要点总结

[FACT] Iben 的 Sec. III 是本文篇幅最大、最权威的章节，提供了所有核合成过程的"舞台"。

**核心结论**：
1. **40 年进展是巨大的**：输入物理（反应率、不透明度、中微子损失）+ 计算能力（Henyey-Forbes-Gould 方法）+ 观测窗口（太空望远镜）
2. **AGB 星是银河系中 12C 与 s 过程同位素的主要来源**——这是 B2FH 时代不充分的
3. **第三次挖掘与 13C 口袋**是现代 AGB 核合成模型的核心机制，但 13C 口袋的确切起源仍有多种竞争方案
4. **大质量星的初始质量–最终产物（NS/BH）映射仍未理论化**——需要假设（本文取 M_crit = 40 $M_\odot$）
5. **密近双星演化**产生了丰富的观测现象（CV, SN Ia, R CrB, LMXB, HMXB, MSP, 双 NS）
6. **SN 1987A 光变曲线分析**证明 SN II 是宇宙铁的主要来源（~0.1 $M_\odot$ 56Fe/颗）

[CRITIQUE] 
- 1997 年时 13C 口袋的起源仍有 3–4 种竞争方案，直到 2000 年代 Herwig 等人的三维计算才更完善地确立了"超射"机制。本文已提及 Blöcker & Herwig 1997 的"超射"结论，处于当时最新进展前沿。
- SN Ia 的"WD 合并"场景在本文写作时是主要模型，但现代（2010s 后）"双简并"vs"单简并"之争仍在进行，超软 X 射线源 (SSS) 作为前身星的模型也被提出（本文已提及）。

# 3. 本章关键数值速查表

| 量 | 数值 |
|---|---|
| 主序寿命指数 | M^(−2.25) |
| 1 $M_\odot$ 主序寿命 | ~10^10 yr |
| 25 $M_\odot$ 主序寿命 | ~7×10^6 yr |
| He 燃烧时标/主序寿命 | 10–25% |
| He 燃烧温度敏感性 | ∝ T^(40) |
| AGB 超风质量损失率 | 10^(−5)–10^(−4) $M_\odot$/yr |
| 触发超风的脉动周期 | > 400 d |
| WD 形成率 | ~0.5–1 yr^(−1) |
| WD 质量分布峰值 | 0.55–0.65 $M_\odot$ |
| 12C($\alpha$,$\gamma$)16O 速率确定性 | B2FH 后 40 年仍未确定 |
| CO 核质量 s 过程中子源阈值 | ≥ 0.9 $M_\odot$（22Ne 源） |
| 22Ne 源触发温度 | > 3.5×10^8 K |
| 13C 源触发温度 | ~ 1.5×10^8 K |
| 挖掘物质 12C 丰度 | 0.15–0.25（质量分数） |
| WR 星质量损失率 | ~10^(−7) $M_\odot$/yr |
| M_crit（NS/BH 分界）| 40 $M_\odot$（本文假设） |
| NS 平均引力质量 | 1.35 ± 0.27 $M_\odot$ |
| SN 1987A 56Fe 抛射量 | ~0.1 $M_\odot$ |
| CV 出生率 | ~10^(−3) yr^(−1) |
| SN Ia 出生率 | ~3×10^(−3) yr^(−1) |
| SN II 出生率 | ~2.1×10^(−2) yr^(−1) |
| 脉冲星出生率 | 0.004–0.008 yr^(−1) |
| R CrB 星银河系估计数 | 200–1000 |
| 已知将合并的 WD 对 | 8 个（3 个在 <Hubble 时间内） |
| 重生 AGB 星比例 | ~25% 后 AGB 星 |
| LMXB 理论出生率 | ~2×10^(−5) yr^(−1) |