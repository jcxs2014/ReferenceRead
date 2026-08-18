# 02. Confrontation with Data — 第3章精读

> 本章属于：[[01_cosmic-ray-propagation/0001_strong-moskalenko-ptuskin-2007/literature_analysis/00_overview.md|Cosmic-ray propagation and interactions in the Galaxy (Strong, Moskalenko & Ptuskin, 2007)]]
>
> 上一章：[[01_cosmic-ray-propagation/0001_strong-moskalenko-ptuskin-2007/literature_analysis/01_theoretical_background.md|01_theoretical_background.md]]
>
> 下一章：[[01_cosmic-ray-propagation/0001_strong-moskalenko-ptuskin-2007/literature_analysis/03_figures.md|03_figures.md]]

---

## 3. Confrontation of Theory with Data（理论对数据的检验）

第3章是本文的核心实证章节，分 9 小节逐一讨论各类观测数据对传播模型的约束。

---

### 3.1 Stable Secondary/Primary Ratios（稳定次级/初级比）

#### 3.1.1 本节核心内容

B/C 比是传播模型拟合的核心参考量，因为 B 完全来自次级，且测量精度优于其他比值。

#### 3.1.2 B/C 为何重要

[FACT] "The reference ratio is almost always B/C because B is entirely secondary, the measurements are better than for other ratios and are available up to 100 GeV."

[FACT] C, N, O 是 B 的主要母核，因此产生截面比 Be 和 Li 的情况更准确 (122, 94)。

#### 3.1.3 经验逃逸长度模型

[FACT] 通常使用泄漏盒或加权板形式，经验刚度依赖为：
$$X(R) = \frac{\beta}{\beta_0} X_0 \quad \text{for } R < R_0$$
$$X(R) = \frac{\beta}{\beta_0} \left(\frac{R}{R_0}\right)^{-\alpha} X_0 \quad \text{for } R > R_0$$

[FACT] 在 $R_0$ 处的转折是必须的，因为 B/C 在低能时的下降比 $\beta$ 依赖（仅描述反应率的速率效应）更快。

[FACT] 典型拟合参数 (69)：
| 参数 | 值 |
|---|---|
| $\alpha$ | 0.54 |
| $X_0$ | 11.8 g cm$^{-2}$ |
| $R_0$ | 4.9 GV/c |
| 源谱刚度指数 | $-2.35$ |

[FACT] 源成分依赖 $X(R)$ 的形式和参数，且反之亦然（因为 B 由 C,N,O 等产生），因此过程是迭代的，从类太阳成分开始。

#### 3.1.4 模型对 B/C 和 Sub-Fe/Fe 的拟合

[FACT] Fig. 8 显示了 (69) 的 B/C 和 (Sc+Ti+V)/Fe（sub-Fe/Fe）拟合。

[FACT] "Clearly the models cannot be distinguished based on these types of data alone, and they can all provide an adequate fit." 即纯扩散、对流、湍流扩散、再加速等多种模型都能拟合 B/C 和 Sub-Fe/Fe。

[FACT] C 和 Fe 在 0.5–100 TeV 能区的注入谱指数为 2.3–2.4（Fig. 9）。

#### 3.1.5 Voyager 2 数据

[FACT] (123) 声称无 $X(R)$ 转折也能拟合 Voyager 2 外日球层 B/C、N/O 和 sub-Fe/Fe 数据（延伸至 1.5 GeV）+ HEAO3 数据。

[FACT] Voyager 2 是独特数据集（太阳调制低）。

#### 3.1.6 再加速方案

[FACT] 再加速（§2.5）在可接受水平下可重现 B/C，**无需扩散系数中的 ad-hoc 转折**。

[FACT] 一个关键优势：再加速所需的 $\alpha$ 值较小（0.3–0.4），与 Kolmogorov 湍流一致，有助于解决各向异性问题（§3.5）。

[FACT] 但再加速的**直接证据尚未确定**（§3.4 的 K-俘获同位素检验结果仍不明确）。

#### 3.1.7 波阻尼方案

[FACT] 波阻尼（§2.5）可满意地重现 B/C、质子和反质子（Fig. 10，75）。

[FACT] 结果：扩散系数在 $< 1.5$ GV 刚度时急剧上升。

[FACT] Kolmogorov 型依赖在此方案中不成功，Kraichnan 型效果更好，高刚度渐近 $D \sim R^{0.5}$。

#### 3.1.8 大 $\alpha$ 方案

[FACT] (68) 提出另一组参数：$\alpha = 0.7-0.9$，注入指数 $\approx 2.0$，基于多物种同时拟合，B/C 低能下降归因于对流。

[FACT] 但如此大的 $\alpha$ 会给各向异性带来问题（§3.5）。

#### 3.1.9 弱非线性输运

[FACT] 弱非线性输运理论 (124, 125) 解释了 B/C 在低能的下降。

#### 3.1.10 本地源模型

[FACT] 本地源模型 (104, 126)：部分初级 CR 有额外本地成分。由于次级通量必须来自整个银河系（本地次级可忽略），陡峭的本地初级源会使 B/C 在低能下降。

[FACT] 本地泡的存在（可能来自几百万年内的几次超新星）使其成为可能，但难以证明或反驳。

[FACT] (104) 声称若在此模型中拟合 B/C，则 sub-Fe/Fe 拟合不好；但 (126) 使用大尺度扩散模型找到了可接受的拟合。

> **分析 / Interpretation**：B/C 数据本身无法区分不同物理模型，这是本领域的核心困境。必须结合多种观测（放射性时钟、$\gamma$ 射线、反质子等）才能约束模型。作者倾向于再加速方案（与 Kolmogorov 谱一致），但对其他方案也给出公允评价。

---

### 3.2 Unstable Secondary/Primary Ratios: Radioactive Clocks（放射性时钟）

#### 3.2.1 本节核心内容

利用长寿命放射性次级核素（$^{10}{\rm Be}$ 等）作为"时钟"约束传播区域大小。

#### 3.2.2 五个关键放射性核素

| 核素 | 半衰期 | 备注 |
|---|---|---|
| $^{14}{\rm C}$ | 5730 y |  |
| $^{10}{\rm Be}$ | $1.51\times10^{6}$ y | 寿命最长、测量最好 |
| $^{26}{\rm Al}$ | $7.2\times10^{5}$ y |  |
| $^{36}{\rm Cl}$ | $3\times10^{5}$ y |  |
| $^{54}{\rm Mn}$ | $312\times10^{3}$ y |  |

#### 3.2.3 晕高度约束

[FACT] 基于这些同位素和更新截面 (128) 得到 $z_h = 4-6$ kpc，与其早期估计 (98, 67) 一致。

[FACT] Fig. 11 显示 $^{10}{\rm Be}$/$^{9}{\rm Be}$ 与模型的比较；ISOMAX $^{10}{\rm Be}$ 测量 (129) 至 2 GeV（因此衰变寿命更长）与拟合一致，但统计量不具强约束力。

#### 3.2.4 泄漏盒解释的误导性

[FACT] "The data are often interpreted in terms of the leaky-box model, but this is misleading (108, 131, 127)."

[FACT] 泄漏盒存活分数可转换为有物理意义的量 (131)：
- 简单扩散晕模型中：存活分数决定扩散系数
- 结合稳定次级/初级比：推导晕大小

[FACT] 典型结果：
| 物理量 | 值 |
|---|---|
| $D_{xx}$ | $(3-5)\times10^{28}$ cm$^{2}$/s（在 3 GV） |
| $z_h$ | 4 kpc |
| 泄漏盒"逃逸时间" | $\approx 10^7$ yr |
| 实际从源到达晕边界的时间 | 比上述约 10 倍大 |
| 泄漏盒"气体密度" | $\approx 0.3$ cm$^{-3}$ |
| 实际平均密度（4 kpc 晕） | $\approx 0.03$ cm$^{-3}$（差 10 倍） |

[FACT] 泄漏盒模型的"逃逸时间"和"气体密度"均比实际值高一个量级，因此**不能直接理解为物理量**。

#### 3.2.5 放射性核素与传播区域的组合

[FACT] "it is precisely the combination of stable and radioactive data which does allow this: the radioactives determine the diffusion coefficient, which then allows the size of the full propagation region to be determined from the stable secondary/primary ratio."

> **分析 / Interpretation**：这一逻辑是传播建模的核心策略：放射性时钟 → 局部扩散系数 → 晕大小。两个量通过组合稳定与放射性数据分别确定。

#### 3.2.6 本地泡效应

[FACT] (127) 指出本地泡对放射性核素解释的影响：如果放射性次级在气体耗竭区（本地泡）产生，它们会在到达地球前衰变，导致在简单扩散晕模型中**高估晕大小**。

[FACT] 如果本地扩散系数大于大尺度值，该效应会减弱。

[FACT] 实际情况更复杂：太阳约 $10^5$ 年前离开本地泡（在泡中停留数百万年），现在位于 CLIC（约 0.2 cm$^{-3}$ HI 密度，35 pc 范围）(86, 87, 134)。

[FACT] "This aspect of the problem for CR propagation has not yet been addressed."

---

### 3.3 K-capture Isotopes and Acceleration Delay（K-俘获同位素与加速延迟）

#### 3.3.1 本节核心内容

利用爆炸核合成产生的 K-俘获同位素（$^{59}{\rm Ni}$, $^{57}{\rm Co}$, $^{56}{\rm Ni}$）判断加速是否在衰变之前发生。

#### 3.3.2 关键数据

| 核素 | 半衰期 | 观察 |
|---|---|---|
| $^{59}{\rm Ni}$ | $7.6\times10^4$ y | 存在 |
| $^{57}{\rm Co}$ | 0.74 y | 存在 |
| $^{56}{\rm Ni}$ | 6 d | 缺失（符合预期，因为加速前就衰变） |

[FACT] 如果加速在衰变前发生，衰变被抑制（核被剥去电子）。$^{56}{\rm Ni}$ 缺失符合预期。

[FACT] (135) 使用 ACE 数据表明：合成与加速之间的延迟远长于 $^{59}{\rm Ni}$ 的衰变时间，除非超新星中产生大量 $^{59}{\rm Co}$。

[FACT] 结论：延迟 $\geq 10^5$ 年，与"超新星加速自身喷射物"的模型不一致，但与"加速已有星际物质"一致。

[FACT] TIGER 的 Co/Ni 数据 (136) 在 1–5 GeV/n 也支持加速延迟。

> **分析 / Interpretation**：这是一个非常关键的结论——它支持了**扩散加速模型**（DFA，激波加速 ISM 物质），而反对"喷射物加速模型"。但飞行中电子附着的复杂性使分析需谨慎。

---

### 3.4 K-capture Isotopes and Reacceleration（K-俘获与再加速检验）

#### 3.4.1 本节核心内容

利用 ACE 数据中多种 K-俘获同位素检验再加速模型。

#### 3.4.2 检验结果

[FACT] (137)：$^{51}{\rm V}$/$^{52}{\rm Cr}$ 与再加速模型更符合，但 $^{49}{\rm Ti}$/($^{46}$+$^{47}$+$^{48}{\rm Ti}$) 给出相反结果。

[FACT] (74)：V/Cr 比在轻微上更符合含再加速的模型，涉及 Ti 的比值无结论。

[FACT] (137) 使用 ACE 的 $^{37}{\rm Ar}$, $^{44}{\rm Ti}$, $^{49}{\rm V}$, $^{51}{\rm Cr}$, $^{55}{\rm Fe}$, $^{57}{\rm Co}$ 数据，结果不明确。

[FACT] "The main problem is the accuracy of the fragmentation cross-sections (126)."

> **分析 / Interpretation**：再加速的 K-俘获直接证据仍是**不明确的**，因为核碎裂截面的不确定性太大。这是当前实验和理论界需要解决的关键瓶颈。

---

### 3.5 Anisotropy（各向异性）

#### 3.5.1 本节核心内容

各向异性测量对扩散模型参数的约束。

#### 3.5.2 观测数据

[FACT] 各向异性的第一角向谐波幅度：
| 能量范围 | 各向异性幅度 | 数据来源 |
|---|---|---|
| $10^{12}$–$10^{14}$ eV | $\delta \sim 10^{-3}$ | (138, 139) |
| $10^{16}$–$10^{18}$ eV | $\sim$ 几个 % | 统计量不足 |

[FACT] $10^{13}$ eV 处 Super-Kamiokande-I 探测器 (140) 给出了二维各向异性映射，统计显著性 $>5\sigma$，最大超额方向约 $\alpha = 75°$, $\delta = -5°$。

#### 3.5.3 理论公式

[FACT] 扩散近似下的各向异性幅度：
$$\delta = -[3D\nabla f + u_p(\partial f/\partial p)] / vf$$
其中 $D$ 是扩散张量，$u \ll v$ 是冻结在背景介质中并产生对流项（Compton-Getting 项）的磁不均匀性的运动速度。

#### 3.5.4 Compton-Getting 各向异性

[FACT] 对于超相对论性 CR（幂律谱 $I(E) \sim p^2 f(p) \sim E^{-\gamma}$）：
$$\delta_{CG} = (\gamma + 2) u / c$$

[FACT] 太阳系相对于本地星际介质的运动产生 $\sim 4\times10^{-4}$ 的常数项，最大强度指向银河中心方向，但**与 $10^{12}$–$10^{14}$ eV 数据（指向反银心方向）不符**。

[FACT] 对流效应被扩散各向异性（由银河系 CR 的非均匀分布产生）压倒。

#### 3.5.5 模型计算与数据比较

[FACT] 计算表明（Fig. 12）：
- **含再加速的扩散模型**与数据在约 3 倍因子内一致
- **纯扩散模型**（$D \sim E^{0.54}$）预测 $E > 10^{14}$ eV 各向异性过大

[FACT] Vela SNR 在 $<6\times10^{13}$ eV（纯扩散）和 $<10^{14}$ eV（含再加速）主导各向异性。

[FACT] 计算假设各向同性扩散是"seriously simplifying assumption"。

> **分析 / Interpretation**：各向异性数据支持小 $\alpha$（$\sim 0.3$，含再加速方案），并排除大 $\alpha$（$\sim 0.54$，纯扩散方案）。这进一步支持再加速模型。

---

### 3.6 Diffuse Galactic Gamma Rays（弥散银河伽马射线）

#### 3.6.1 本节核心内容

$\gamma$ 射线为 CR 研究提供独立的间接约束，涉及整个银河系而非仅本地。

#### 3.6.2 $\gamma$ 射线产生机制

[FACT] $\gamma$ 射线（$>100$ MeV）由以下过程在星际介质中产生：
- CR 质子和 He 与气体（$\pi^0$ 衰变）
- 电子与气体（轫致辐射）
- 电子与星际辐射场（逆康普顿散射）

[FACT] $\gamma$ 射线是确定 CO-$H_{2}$ 关系的重要独立方法。

#### 3.6.3 观测历史

| 实验 | 年份 | 意义 |
|---|---|---|
| OSO-III | 1968 | 首次卫星观测 |
| SAS-2 | 1972 | 确认星际辐射 |
| COS-B | 1975–1982 | 发现 CR 分布不跟随 SNR，CO-$H_{2}$ 关系 |
| CGRO (EGRET, COMPTEL) | 1991–2000 | 高质量数据 |

[FACT] 从 COS-B 发现 CR 分布不跟随经典 SNR 分布，这对 SNR 起源是"问题"。

#### 3.6.4 GALPROP 模型预测 vs. 数据

[FACT] GALPROP 模型基于直接测得的 CR 谱 + 径向梯度，其 $\gamma$ 射线谱在 1 GeV 以上**低于 EGRET 数据**——但作为未拟合的预测，它证明了基本假设（$\gamma$ 射线产生于 CR 相互作用）正确。

[FACT] 因子 2 的差异揭示了剩余的不确定性。

#### 3.6.5 GeV 过剩问题

[FACT] "optimized" 模型对 CR 谱的修正在太阳系调制和 $>100$ pc 尺度空间涨落的合理范围内，但缺少详细论证，因此只是存在性证明。

[FACT] 其他更激进的 CR 谱修改方案：

**(i) 硬电子注入谱**：需要大涨落（能量损失 + SNR 的随机性），但所需变化比合理预期还大 (113)——不太可能。

**(ii) 硬质子谱**：可通过反质子数据排除——产生 $\gamma$ 射线的同样质子会产生太多反质子 (146, 113, 78)。

**(iii) SNR 射电谱指数分散**：可能暗示 CR 质子谱的分散 (147)，应也用反质子检验。

**(iv) 暗物质起源**：被追踪 (148)，但产生过多的 CR 反质子 (149)。

#### 3.6.6 角分布与 SNR 梯度问题

[FACT] 脉冲星的径向梯度比从 $\gamma$ 射线推导的大（Fig. 15）。

[FACT] 外银河中 SNR 的分布显示与脉冲星类似的梯度 (152)。

[FACT] 可能的解决方案：$H_{2}$/CO 比随银心距增加，与银河系金属丰度梯度相关 (144)——可允许 CR 源跟随脉冲星示踪的 SNR 分布。

[FACT] Fig. 16 显示基于该模型的经度和纬度剖面，与 EGRET 数据满意一致。

[FACT] 但 $H_{2}$/CO 变化的幅度或其与金属丰度的关系尚不确定。

#### 3.6.7 高纬度逆康普顿辐射

[FACT] 高纬度处逆康普顿贡献很大（Fig. 14, 16），这是预测在最高纬度处与 EGRET 一致的原因（气体相关的 $\pi$ 衰变辐射小）。

[FACT] $\gamma$ 射线同时约束质子和电子（不同的角分布可清楚区分）。

[FACT] "高纬度逆康普顿辐射是 CR 晕扩展到盘面以上几 kpc 的独立证据"——与 §3.2 放射性核素一致。

> **分析 / Interpretation**：$\gamma$ 射线数据对传播模型的约束比直接测量更严格，因为涉及整个银河系。GeV 过剩问题是本文发表时的未解之谜（后来的费米 GLAST 数据提供了更多线索），SNR 梯度的解释仍是开放问题。

---

### 3.7 Antiprotons and Positrons（反质子和正电子）

#### 3.7.1 反质子

##### 基本信息

[FACT] 反质子谱的独特形状：在约 2 GeV 处峰值，低能急降（次级产生的运动学结果）。

[FACT] 可能的初级来源：暗物质粒子湮灭、原初黑洞蒸发。

[FACT] 近年 BESS 仪器的大幅数据 (156–162)。

##### 不确定性来源（三重）

[FACT] 次级反质子通量计算的主要不确定性：
1. **截面不完整知识**：反质子产生、湮灭和散射
2. **传播参数和模型**
3. **日球层调制**

[FACT] 星际反质子通量只受截面和传播模型不确定性影响；最终与实验比较前必须修正太阳调制。

[FACT] CR 核谱仅在内日球层测量，但需要外日球层谱来正确计算反质子产生率。

##### 与模型的冲突

[FACT] (117) 近期表明：1995–1997 年太阳极小期的精确反质子测量 (158) 在约 2 GeV 处与现有传播模型在 $\sim 40\%$ 水平不一致（测量不确定度 $\sim 20\%$）。

[FACT] 基于本地 CR 测量、简单扩散能量依赖、全银河系均匀源谱的传统模型**无法同时重现次级/初级比和反质子通量**。

[FACT] 含再加速的模型（拟合次级/初级比）产生太少反质子（扩散系数太大）。

[FACT] 无再加速的模型可重现反质子通量，但不能解释次级/初级比的低能下降。

[FACT] 为同时一致，需要在扩散系数和注入谱中引入转折。

[FACT] 传播模型中的解决方案：扩散系数在几个 GeV 处的转折，解释为传播模式的变化 (117)。

##### 本地环境方案

[FACT] "新鲜未处理的"核素成分 (126)：初级 CR（C, O）有本地低能成分（本地泡产生），而次级 CR（B）在整个银河系产生。通过额外 C 源消除反质子数据拟合带来的 B 过剩。

[FACT] 一致的反质子通量可在再加速模型中获得，如果有额外的质子源 $\lesssim 20$ GeV (163)——这能量高于反质子产生阈值，有效产生 $\lesssim 2$ GeV 的反质子。

[FACT] 这一成分的强度和谱形状可通过结合反质子和弥散 $\gamma$ 射线的限制来推导。

##### 未来

[FACT] 需要 BESS-Polar 和 Pamela (164) 的更大统计量。

#### 3.7.2 正电子

[FACT] 1964 年发现 (165)。在 $\sim 1$ GeV 以上正电子/电子比 $\approx 0.1$。

[FACT] 次级正电子主要来自带电 $\pi^+$ 和 $K^+$ 的衰变。

[FACT] 计算结果与数据一致，表明大多数 CR 正电子是次级的 (166, 39)。

[FACT] 小部分可能来自原初源 (167)：脉冲星风 (168)、WIMP 湮灭 (169)。

[FACT] 星际空间 $\lesssim 1$ GeV 处次级正电子通量与电子通量可比，使正电子在 MeV 段弥散 $\gamma$ 射线中不可忽略 (113)。

[FACT] HEAT 数据 (42) 在 5–7 GeV 处显示 $\sim 3\sigma$ 超额，合并所有飞行在 $\sim 8$ GeV 处最显著。

[FACT] AMS, CAPRICE 和 HEAT 数据在误差范围内一致，但误差仍相当大。

---

### 3.8 Electrons and Synchrotron Radiation（电子与同步辐射）

#### 3.8.1 本节核心内容

CR 电子因其快速能量损失和与同步辐射的联系，需要单独处理。

#### 3.8.2 基本问题

[FACT] 电子低能密度（约核的 1%）"is not yet understood; standard SNR shock acceleration does not predict such a ratio and it is normally a free parameter in models."

#### 3.8.3 观测特征

[FACT] 直接测量从 MeV 到 TeV。

[FACT] 低能：太阳调制太大，星际通量真正未知。

[FACT] TeV 能区：统计量差，但有新实验进行中。

[FACT] 年轻 SNR 含 TeV 电子（通过非热 X 射线证明），可能高达 100 TeV (174)。

[FACT] 快速能量损失意味着 Loop 1、Vela、Cygnus Loop、MonoGem 等古老 SNR 在 $>100$ GeV 对本地电子谱有重要贡献，并在 $>1$ TeV 主导（Fig. 4, 37）。

#### 3.8.4 电子传播效应

[FACT] Fig. 13 展示：
- **低于 1 GeV**：星际谱比注入谱平坦（库仑损失）
- **中间能区**：谱与注入时相似
- **高能**：由于逆康普顿、同步辐射损失和能量依赖扩散而变陡

[FACT] 典型注入谱指数 2.4（与核相似），产生观测到的 3.3 高能斜率 (113)。

#### 3.8.5 同步辐射

[FACT] 同步辐射谱指数：
$$\beta_\nu = (\gamma - 1)/2$$
观测 $\beta_\nu = 0.6 - 1$（随频率增加），意味着 $\gamma = 2.4 - 3$（随能量增加）——满意一致。

[FACT] (175, 176) 建立了银河系同步辐射的详细几何模型。

[FACT] (81) 结合 $\gamma$ 射线和同步辐射数据，可独立确定磁场随银心距的变化。

#### 3.8.6 外星系同步辐射

[FACT] NGC891（边缘侧星系）有延伸到几 kpc 的非热晕 (179, 180)——支持银河系大晕的想法。

[FACT] 其他边缘侧星系确认大晕 (181)。

[FACT] 面侧星系（如 M51）显示明显的旋臂结构 (177)，但主要是磁场效应。

#### 3.8.7 射电/远红外关联

[FACT] "The tight radio-continuum/far-infrared correlation for galaxies" (184, 185, 186) 在星系内（$<100$ pc）和星系间均成立，跨越几个数量级的亮度。

[FACT] "CR calorimeter" (187) 是最简单解释——将 CR 产生和 UV（再处理为远红外）与恒星形成率关联。

> **分析 / Interpretation**：电子的快速能量损失使它们携带的是局部（时空）信息而非整个银河系的信息，这与核素完全不同。这也是为什么 $\gamma$ 射线在高纬度主要反映本地电子（逆康普顿）而非远处气体（$\pi^0$ 衰变）的原因。

---

### 3.9 Time- and Space-dependent Effects（时空依赖效应）

#### 3.9.1 本节核心内容

讨论稳态平滑传播假设的失效情形。

#### 3.9.2 电子的时空涨落

[FACT] $>100$ GeV 处电子快速能量损失 + 源的随机性产生空间和时间变化。

[FACT] 每个 SNR 源持续仅约 $10^4-10^5$ 年，因此在电子分布中留下印记。

[FACT] 导致高能 CR 电子密度大涨落，所以"the electron spectrum measured near the Sun may not be typical" (113)。

[FACT] (145, 188) 和 (37) 给出了局部 SNR 的统计计算。

#### 3.9.3 核素的涨落

[FACT] 对核素的影响小得多（因为本质上无能量损失），但仍可能重要 (189)。

[FACT] 这种效应可通过初级谱的变化影响 B/C (111, 116)。

[FACT] 本地泡也可影响 B/C 的能量依赖 (126)。

[FACT] SNR 注入谱的分散可能导致局部观测谱偏离平均 (147)。

---

### 4. Summary Points list（要点总结）

[FACT] 作者总结要点：

1. **考虑所有相关数据的重要性**：直接（粒子）和间接（$\gamma$ 射线、同步辐射）测量
2. **计算能力的提高使许多旧近似不再必要**
3. **新高精度数据需要详细数值模型**

---

### 5. Future Issues（未来问题）

[FACT] 作者列举的开放问题：

1. 次级/初级比能量依赖的解释——需要低能和高能的精确测量
2. 传播区域大小——延展晕的存在——需要宽能区的放射性物种测量
3. 扩散、对流和再加速的相对作用
4. 本地源对初级 CR 通量的重要性
5. $\gamma$ 射线中相对于本地观测 CR 预测的 GeV 过剩起源
6. CR 源分布：是否与 SNR 一致？
7. 正电子和反质子是否可由初级 CR 次级解释，还是存在（可能是外来的）过剩？

[FACT] 理论侧：银河系 CR 动力学模型与 CR 传播理论的关系。

[INTERPRETATION] §5 Future Issues 中作者列出的 7 个开放问题，15 年后（到 2022 年 AMS-02 全部数据、HERMES 等计划、CTA 开始运行）来看，绝大多数仍无决定性答案——特别是正电子超量、CR 源分布、扩散系数能量依赖。这本身就是本综述"前瞻性"的一个证据，同时也说明宇宙线传播是"慢烧"的领域：数据积累慢、模型改进慢、共识形成更慢。

[INTERPRETATION] "relative roles of diffusion, convection and reacceleration" 这一开放问题，实际上对应 §2 中传播方程 (1) 的三项主导物理。作者用"relative roles"这个措辞，暗示三项中任何一项的精确权重都尚未被定——这与 GALPROP 参数化中 $L_h$、$V_c$、$V_a$ 三个关键自由参数的经验性相印证。

[INTERPRETATION] "are positrons and antiprotons explained as secondaries from primary CR or is there a – perhaps exotic – excess?" 这一句在 2007 年写下时，尚未出现 Pamela (2008) 和 AMS-02 (2013) 的正电子超量数据。作者把"exotic"（指暗物质或原初黑洞）明确列为可能解释，显示该综述在理论上是"开放"的，没有预设立场——这是一种值得称赞的科学态度，也在 15 年后被历史所验证。

[CRITIQUE] §4 Summary Points 只列 3 条"要点"，过于简略——对于一个涵盖 189 篇文献、16 张 Figure 的综述而言，"要点"应当是方法论层面的总结，而非仅罗列"考虑所有数据""用数值模型""新数据需要新模型"这样的通用陈述。

[CRITIQUE] §5 Future Issues 的开放问题列表中没有提及"CR 与暗物质的相互作用"（尽管 §5.5 中已作为正电子超量的一种解释出现），也没有提及"多信使宇宙线"（中微子、引力波）——这两个方向在 2008–2017 年间成为宇宙线研究的核心，但 2007 年综述完全没有触及。

---

> 下一章：[[01_cosmic-ray-propagation/0001_strong-moskalenko-ptuskin-2007/literature_analysis/03_figures.md|03_figures.md]]