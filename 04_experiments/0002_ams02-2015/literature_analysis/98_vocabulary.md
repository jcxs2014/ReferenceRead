# 98. Vocabulary — 学术词汇与术语

## A. 学术逻辑词

| 单词 | 词性 | 逻辑功能 | 中文 | 原文例句 | 逻辑说明 |
|---|---|---|---|---|---|
| however | adv. | 转折 | 然而 | "However, ... does not fit the flux at 99.9% C.L." | 承认单幂律看似合理，再排除它 |
| thereby | adv. | 因果(由此) | 从而 | "... thereby providing submicron position measurements." | 20 束 IR 激光 → 亚微米测量精度 |
| consequently | adv. | 因果(结果) | 因此 | "consequently, the efficiency of the unbiased trigger" | 效率推论链 |
| nevertheless | adv. | 转折 | 然而 | "nevertheless the flux progressively hardens..." | 承认其他实验结果不一致，但 AMS 数据仍给出变硬 |
| consequently | adv. | 因果 | 因此 | — | — |
| owing to | prep. | 因果 | 由于 | "owing to the influence of the geomagnetic field" | 几何磁截止的物理来源 |
| whereas | conj. | 对比 | 而 | "A power law ..., whereas the flux deviates..." | 单幂律 vs 观测数据对比 |
| despite | prep. | 让步 | 尽管 | "despite different variations of the flux" | 承认前代实验差异，仍给出统一结论 |
| in particular | adv. | 举例 | 特别地 | "In particular, the spectral index progressively hardens..." | 从总体结论聚焦到核心发现 |
| accordingly | adv. | 因果 | 相应地 | "accordingly, the errors are accounted for..." | 系统误差处理与测量结果对应 |
| subsequently | adv. | 顺序 | 随后 | "Subsequently, at each iteration..." | unfolding 迭代算法步骤 |
| namely | adv. | 举例 | 即 | "namely, from the rigidity resolution function..." | 列举系统误差具体来源 |
| taken together | adv. | 结论 | 综合起来 | "Taken in quadrature and weighted..." | 系统误差合成方法 |
| most importantly | adv. | 递进 | 最重要的是 | "Most importantly, several independent analyses..." | 强调多重独立分析的可靠性 |
| in addition | adv. | 递进 | 此外 | "In addition, to select only primary cosmic rays..." | 补充选例条件 |

## B. 领域术语

| 术语 | 中文 | 释义 | 首现章节 |
|---|---|---|---|
| AMS-02 / Alpha Magnetic Spectrometer | AMS-02 | ISS 平台上的磁谱仪，本文核心探测器 | §1 |
| Rigidity $R$ | 刚性 | 动量/电荷比 $R = p/Z$，宇宙线磁场偏转的基本物理量 | §1 |
| TOF (Time of Flight) | 飞行时间 | 通过飞行时间测粒子速度，用于电荷/方向判别 | §1 |
| ACC (Anti-Coincidence Counter) | 反符合计数器 | 拒绝侧进宇宙线的辅助探测器 | §1 |
| ECAL (Electromagnetic Calorimeter) | 电磁量能器 | 17 辐射长度三维量能器，测量 $e^\pm$ 能量与簇射形状 | §1 |
| TRD (Transition Radiation Detector) | 过渡辐射探测器 | 区分 $e^\pm$ 与强子的辅助探测器 | §1 |
| RICH (Ring Imaging Čerenkov) | 环形切伦科夫探测器 | 利用切伦科夫辐射测粒子速度与质量 | §1 |
| MDR (Maximum Detectable Rigidity) | 最大可测刚性 | 由磁体强度、力臂、径迹精度决定的刚性上限（AMS-02 为 2 TV） | §1 |
| Unfolding | 解展（反卷积） | 用分辨率函数把测量分布反推回真值分布 | §1 |
| Geomagnetic cutoff | 几何磁截止 | 地球磁场对低刚性宇宙线的屏蔽效应 | §1 |
| IGRF | 国际地磁参考场 | 计算几何磁截止的标准地磁场模型 | §1 |
| Solar modulation | 太阳调制 | 太阳风对低能宇宙线在日球层内的减速效应 | §1–§6 |
| Force-field approximation | 力场近似 | 处理太阳调制的简化模型（Gleeson & Axford 1968） | §6 |
| Spectral index $\gamma$ | 谱指数 | 流强幂律拟合 $\Phi \propto R^\gamma$ 中的指数 | §2–§3 |
| Hardening | 变硬 | 谱指数绝对值减小（$\gamma$ 增大），高能段流强相对幂律预期升高 | §3 |
| Double power law | 双幂律 | 两段幂律通过平滑过渡函数连接的唯象模型 | §2 |
| Inelastic cross section | 非弹性截面 | 质子与探测器材料（碳/铝）发生非弹性作用的截面 | §5 |
| $\tilde{R}$ (tilde R) | 等效刚性 | Lafferty & Wyatt 1995 定义的径迹几何修正刚性 | §2 |
| Acceptance | 有效接受度 | 探测器对不同方向、不同刚性粒子的几何+物理响应积分 | §1 |
| Systematic error | 系统误差 | 不随事件数增大而减小的误差（本文按分项 quadrature 合并） | §5 |
| $\chi^2$/d.o.f. | 卡方/自由度 | 拟合优度度量，1 为理想值 | §6 |
| DSA (Diffusive Shock Acceleration) | 扩散激波加速 | SNR 加速宇宙线的主流机制（Drury 1983） | §4 |
| Kolmogorov turbulence | Kolmogorov 湍流 | 经典磁湍流能谱 $E(k) \propto k^{-5/3}$，对应 $\delta \approx 1/3$ | §4 |
| Alfvén waves | Alfvén 波 | 磁化等离子体中的低频波模，驱动宇宙线散射 | §4 |

## C. 长难句

**句 1**（原文 p.6，双幂律拟合结果）：

> "Fitting over the range 45 GV to 1.8 TV yields a $\chi^2$/d.o.f. = 25/26 with $C = 0.4544 \pm 0.0004(\text{fit})^{+0.0037}_{-0.005}(\text{sys}) \pm 0.0027(\text{sol})$ m$^{-2}$ sr$^{-1}$ sec$^{-1}$ GV$^{-1}$, $\gamma = -2.849 \pm 0.007(\text{fit})^{+0.005}_{-0.004}(\text{sys}) \pm 0.004(\text{sol})$, $\Delta\gamma = 0.133^{+0.032}_{-0.030}(\text{fit})^{+0.046}_{-0.043}(\text{sys})^{+0.003}_{-0.005}(\text{sol})$."

- **主干**：Fitting ... yields $\chi^2$/d.o.f. = 25/26 with parameters $C, \gamma, \Delta\gamma$
- **修饰**：三个误差项（fit/sys/sol）分别代表拟合统计+未关联系统、关联系统、太阳调制势
- **中文**：在 45 GV–1.8 TV 范围内拟合得到 $\chi^2$/d.o.f. = 25/26，归一化 $C = 0.4544 \pm 0.0004(\text{fit})^{+0.0037}_{-0.005}(\text{sys}) \pm 0.0027(\text{sol})$ m$^{-2}$ sr$^{-1}$ s$^{-1}$ GV$^{-1}$，谱指数 $\gamma = -2.849$，变硬幅度 $\Delta\gamma = 0.133$。

**句 2**（原文 p.7，结论段）：

> "In conclusion, knowledge of the rigidity dependence of the proton flux is important in understanding the origin, acceleration, and propagation of cosmic rays."

- **主干**：knowledge ... is important in understanding ...
- **修饰**：rigidity dependence 修饰 proton flux；origin/acceleration/propagation 三并列
- **中文**：总之，了解质子流强随刚性的变化对于理解宇宙线的起源、加速与传播至关重要。

**句 3**（原文 p.5，Fig.2 校验）：

> "The resulting uncertainty on the MDR was estimated to be 5%; the corresponding unfolding errors were obtained by varying the width of the Gaussian core of the resolution function by 5% and the amplitude of the non-Gaussian tails by ~20% ... and found to be 1% below 200 GV and 3% at 1.8 TV."

- **主干**：the unfolding errors were obtained ... and found to be ...
- **修饰**：by varying ... by 5% / by ~20% 描述方法；1% below 200 GV and 3% at 1.8 TV 描述结果
- **中文**：得到的 MDR 不确定度约为 5%；对应的 unfolding 误差通过对分辨率函数高斯核宽度变化 5%、非高斯尾幅度变化 ~20% 得到，结果在 <200 GV 为 1%，在 1.8 TV 为 3%。
