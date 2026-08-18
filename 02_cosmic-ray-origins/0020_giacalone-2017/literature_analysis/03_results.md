> 上一章：[[02_numerical_model]]
> 下一章：[[04_implications]]
---
title: "§3 Results — Giacalone 2017"
section: '3. RESULTS'
---

## 3.1 背景场（Fig. 1, 2）

**[FACT] Fig. 1**：磁场强度随时间在某固定位置的变化。显示：
- 激波到达前：$|\mathbf{B}|$ 在均值 $B_0$ 附近振荡（湍流贡献）
- 激波通过后：磁场跃升（压缩）+ 下游湍流增强

**[FACT] Fig. 2**：$x$-$z$ 平面上磁场线投影。$L_c/V_{\text{sh}}t$ 从顶到底由大变小（$3 \to 0.3$）。
- **$L_c > R_{\text{sh}}$（顶三图）**：场线几乎直线，贯穿球面——磁场线漂移**非局地化**，粒子沿场线跨越整个球面
- **$L_c < R_{\text{sh}}$（底三图）**：场线弯曲复杂，局域 $\theta_{Bn}$ 涨落剧烈——**注入局地化**

**[FACT] 核心观察**：激波法向与磁场夹角沿激波面前后**变化巨大**（"varies considerably along the shock front"）——这是本文全部结果的几何根源。

## 3.2 能谱对比：球状 vs 平面（Fig. 3, 4）

**[FACT] Fig. 3**：$L_c/r_{g0} = 10^4$（Run 1, 黑直方）与 $10^5$（Run 2, 蓝），对比平面激波（绿）。
- 球面 & 平面在低能区一致
- 球面出现**bump-like feature**在 $E_R$ 附近，延伸到 $\sim 5 E_R$——单圈回旋（single gyro-orbit）效应
- 高于 $50$–$100\,E_R$：谱变陡——有限加速时间 + **局域加速率沿球面变化**

**[FACT] Fig. 4**：球状（$L_c/r_{g0}=10^5$）vs 平面 DSA 理论 $\kappa p^{-4}$。球面谱在高能端**更陡**于 $p^{-4}$，原因：
1. 上游粒子贡献（理论只含下游）
2. **加速率随 $\theta_{Bn}$ 变化**（非均匀减速谱）

**[FACT] 能谱形状随 $\theta_{Bn}$ 定性说明**（Jokipii 1982, 1987）：
$$\dot{E}\big|_{\theta=90°} \gg \dot{E}\big|_{\theta=0°}$$
加速在准垂直区最快，准平行区最慢。

## 3.3 粒子通量沿球面分布（Fig. 5）

**[FACT] Fig. 5**：粒子通量 $E>1000\,E_R$，归一化 $n_0 V_{\text{sh}}$，色标编码。
- **Ensemble 平均（左）**：明显**极区增强**——粒子"收集"在两极
- **Single realization（右）**：极区增强依然存在，但叠加随机局部增强（"patchy"）

**[FACT] 极区增强的物理机制**（本文核心结果之一）：
> "The particles 'collect' at the poles as they approximately adhere to magnetic field lines that move poleward from their initial encounter with the shock at the equator, as the shock expands. The field lines at the poles have been connected to the shock the longest."

**链条**：
1. 粒子初始在赤道（准垂直）被快速注入/加速
2. 磁场线压缩使粒子**沿激波面漂移**（$E \times B$ drift 与动生电场同向）
3. 随着激波向外膨胀，每条场线与激波的交点**平均向极区移动**
4. 粒子随之聚集到极区——**场线-激波连接时间最长**

## 3.4 加速率随 θ 变化（Fig. 6）

**[FACT] Fig. 6(a)(b)**：不同时刻的球状激波，标注场线-激波交点随时间向极移动。

**[FACT] Fig. 6(c)**：加速率 $\gamma(\theta)$ 解析式（Appendix B 导出）：
$$\gamma \propto \frac{1}{\cos^2\theta + \delta \sin^2\theta}$$
其中 $\delta = \kappa_\perp/\kappa_\parallel \ll 1$。

**图示**：
- $\theta \to 90°$：$\gamma \to \text{最大}$
- $\theta \to 0°$：$\gamma \to \delta \times$ 最大值（最小）
- 两个 $\delta$ 值（$\delta=0.01, 0.001$）曲线显示 $\delta$ 越小，$\theta=90°$ 处加速率优势越明显

## 3.5 能谱按最终/初始极角分类（Fig. 7, 8, 9）

**[FACT] Fig. 7**（$s^2=1$, Run 2）：
- **上图**（按末极角）：
  - 蓝：赤道末态（$\cos\theta_f \in (-0.1, 0.1)$）
  - 红：极区末态（$\cos\theta_f \in (0.8, 1)$）
  - **极区粒子数（积分）远大于赤道**——尽管单粒子能量未必更高
- **下图**（按初极角）：
  - 蓝：初在赤道
  - 红：初在极区
  - **最高能量粒子来自赤道初始位置**

**[FACT] Fig. 8**（$s^2=0.3$, Run 5）：
- 低能粒子（$E < 500\,E_R$）**极区主导**（比 $s^2=1$ 更明显）
- 原因：低湍流方差 → 低 $\kappa_\perp$ → 准垂直注入效率低（"fewer particles injected at quasi-perpendicular shock"）
- 但加速率在准垂直仍最高（$\propto 1/\kappa_\perp$）

**[FACT] Fig. 9**：能谱按**初始位置相对局部磁场**分类（$\cos\theta_{L,0}$，局部 $B$ 与 $\hat{n}$ 夹角）。
- 显示：即使按**局部** $\theta_{Bn}$ 分类，**准垂直初始粒子最终仍聚集到极区**——再次印证"场线连接时间"机制

## 3.6 关键数值总结

| 量 | 数值 |
|---|---|
| 能量守恒精度 | $< 10^{-5}\%$ |
| 单圈回旋特征能量 | $\sim E_R$ 到 $5\,E_R$ |
| 幂律区上限 | $50$–$100\,E_R$ |
| 低湍流方差 s² | 0.3 |
| 高湍流方差 s² | 1 |
| $L_c/r_{g0}$ | $10^4$, $10^5$ |
| 湍流波长范围 | $0.5\,r_{g0}$ 到 $10^6\,r_{g0}$ |
| 内激波流速度 | $(3/4)V_{\text{sh}}$ |
| 冷却时标（下游膨胀） | $\sim R_{\text{sh}}/V_{\text{sh}}$ |

## 3.7 核心结果一句话

**[FACT] 三合一**：
1. **加速位置**：准垂直（赤道）区加速**最快**
2. **最终聚集**：粒子收集到极区，极区**通量最高**
3. **机制**：场线随激波膨胀向极移动 + 粒子沿场线漂移

---

## 3.8 单圈回旋效应的物理机制（Fig. 3 bump-like feature 详解）

**[FACT]** 图 3 中 $E \approx E_{R}$ 到 $5\,E_{R}$ 出现 bump-like 特征：
- **机制**：粒子在激波前完成**单次完整回旋**（single gyro-orbit），在被下游流体带走之前沿激波面漂移
- **能量增益**：漂移方向与动生电场 $\mathbf{E} = -\mathbf{U} \times \mathbf{B}/c$ 同向，获得小量能量
- **非扩散效应**：原文强调 "This is a non-diffusive kinetic effect"

**[FACT]** 此特征在自洽 hybrid 模拟中**不出现**（Giacalone 2005b; Giacalone & Decker 2010）——因 hybrid 包含了 cross-shock potential。

**[INTERPRETATION]** Bump-like 特征的存在本身**佐证**了本文模型中 cross-shock potential 的缺失：它不是"噪声"，而是一个**可识别的模型简化特征**。在定量应用中应剔除该能量区。

## 3.9 能谱陡化机制（Fig. 4 定量分析）

**[FACT]** 图 4 显示球状激波高能端能谱**陡于**平面 DSA 理论 $\propto \kappa p^{-4}$：

1. **上游贡献**：理论只含下游粒子，模拟含上游粒子
2. **加速率沿球面变化**：$\gamma(\theta) \propto 1/(\cos^{2}\theta + \delta \sin^{2}\theta)$ 产生**不均匀谱**
3. **有限加速时间**：所有粒子的加速时间 $t - t_{0}$ 有上限

**[FACT]** 加速率公式（Appendix B）：

$$\gamma(\theta) \propto \frac{1}{\cos^{2}\theta + \delta\sin^{2}\theta}, \qquad \delta = \frac{\kappa_{\perp}}{\kappa_{\parallel}} \ll 1$$

**[INTERPRETATION]** 两个极限：
- $\theta \to 90°$：$\gamma \to 1/\delta$ —— 最大值
- $\theta \to 0°$：$\gamma \to 1$ —— 最小值
- 比值 $\gamma(90°)/\gamma(0°) = 1/\delta$，典型 $\delta = 0.01$–$0.001$ 给出 100–1000 倍差异

## 3.10 场线连接时间机制（Fig. 6 详解）

**[FACT]** 图 6 的核心几何论证：

**设** $T$ 为当前时刻，$T - \Delta T$ 为场线首次与激波接触的时刻。

- 场线与激波法向夹角 $\theta$
- 场线-激波连接时间：$\Delta T(\theta)$

**[FACT]** 连接时间比（图 6b）：

$$\frac{\Delta T(\theta)}{T} = \begin{cases} \approx 1, & \theta \to 0° \text{（极区）} \\ \to 0, & \theta \to 90° \text{（赤道）} \end{cases}$$

**[FACT]** 机制链条：
1. 场线初始（$t = 0$）与"假想"极小激波相交在赤道
2. 激波向外膨胀，场线与激波的交点**沿激波面向极移动**
3. 粒子**沿场线漂移**，保持与场线连接
4. 最终粒子聚集在极区 —— 场线-激波连接时间最长的位置

**[INTERPRETATION]** 该机制**独立于**加速率的 $\theta$ 依赖：
- 加速最快的地方 = 赤道（$\theta \approx 90°$，$\gamma$ 最大）
- 最终聚集的地方 = 极区（$\theta \approx 0°$，连接时间最长）
- 因此 **"加速位置" 与 "聚集位置" 分离** —— 这是本文最重要的发现

## 3.11 能谱按极角分类（Fig. 7 定量分析）

**[FACT]** 图 7（Run 2, $s^{2} = 1$, $L_{c}/r_{g0} = 10^{5}$）：

- **末极角 $\theta_{f}$**（上图）：
  - $\cos\theta_{f} \in (-0.1, 0.1)$（蓝，赤道末态）：粒子数少
  - $\cos\theta_{f} \in (0.8, 1)$（红，极区末态）：粒子数多
- **初极角 $\theta_{0}$**（下图）：
  - $\cos\theta_{0} \in (-0.1, 0.1)$（蓝，赤道初始）：最高能量粒子
  - $\cos\theta_{0} \in (0.8, 1)$（红，极区初始）：能量较低

**[FACT]** $E > 10^{4}\,E_{R}$ 的粒子几乎全部初始在赤道。

**[INTERPRETATION]** 此图直接验证"加速快 + 连接时间长"双重机制：
- **能量**：由加速率决定 → 赤道最快
- **数密度**：由连接时间决定 → 极区最长

**[CRITIQUE]** 图 7 的极区末态粒子**平均能量未必更高**，只是数量更多 —— 原文 Fig. 7 上图红色能谱的低能部分高于蓝色，但高能部分不一定。

## 3.12 弱湍流方差下注入效率（Fig. 8 定量分析）

**[FACT]** 图 8（Run 5, $s^{2} = 0.3$, $L_{c}/r_{g0} = 10^{5}$）：

- $5 < E/E_{R} < 500$ 的粒子**绝大多数初始在极区**
- 与图 7（$s^{2} = 1$）相比，赤道注入的粒子**更少**

**[FACT]** 物理原因：
- $s^{2}$ 减小 → $\kappa_{\perp}$ 减小（Giacalone & Jokipii 1999）→ 准垂直注入效率降低
- 但 $\kappa_{\perp}$ 减小 → $\gamma \propto 1/\kappa_{\perp}$ 增大 → 加速率**更高**

**[FACT]** 两个效应同时存在：
1. **注入率**：$\propto$ 跨场扩散（随 $s^{2}$ 减小而减小）
2. **加速率**：$\propto 1/\kappa$（随 $s^{2}$ 减小而增大）

**[INTERPRETATION]** 存在**权衡**（trade-off）：
- 低 $s^{2}$：注入难，但加速快
- 高 $s^{2}$：注入易，但加速慢
- 最终粒子分布取决于两者乘积

**[CRITIQUE]** 该 trade-off 未被量化为解析式；本文仅给出定性对比。

## 3.13 局域 vs 全局加速（Fig. 9 详解）

**[FACT]** 图 9（Runs 3, 6, 7）：按**局域** $\theta_{L,0}$ 分类，$\mu_{L,0} = \cos\theta_{L,0}$

**三幅图的 $L_{c}/R_{\text{sh}}$ 对比**：
- **左图**（Run 6, $L_{c}/r_{g0} = 10^{4}$, $V_{\text{sh}} t_{\text{max}}/L_{c} = 50$, 故 $R_{\text{sh}}/L_{c} = 50$，即 $L_{c}/R_{\text{sh}} = 0.02 \ll 1$）：
  - 局域准平行注入效率**明显高于**局域准垂直
  - 注入是**局地化的**
- **右图**（Run 7, $L_{c}/r_{g0} = 10^{6}$, $V_{\text{sh}} t_{\text{max}}/L_{c} = 0.5$, 故 $L_{c}/R_{\text{sh}} = 2 \gg 1$）：
  - 准平行与准垂直注入效率差异**消失**
  - 注入是**非局地化的**

**[FACT]** 物理机制：
- $L_{c}/R_{\text{sh}} \gg 1$：场线 meandering 跨越整个激波，粒子可"看到"多个 $\theta$ 区 → 平均化
- $L_{c}/R_{\text{sh}} \ll 1$：场线基本直线，粒子被局限在局域 $\theta$ 区

**[INTERPRETATION]** Fig. 9 直接验证 $L_{c}/R_{\text{sh}}$ 判据：

$$\text{Injection regime} = \begin{cases} \text{non-local}, & L_{c}/R_{\text{sh}} \gg 1 \\ \text{local}, & L_{c}/R_{\text{sh}} \ll 1 \end{cases}$$

**[CRITIQUE]** Run 7 的 $V_{\text{sh}} t_{\text{max}}/L_{c} = 0.5$ 意味着模拟时间**短**于一个 $L_{c}$ 穿越时间 —— 粒子加速时间不足，高能谱可能被低估。

## 3.14 低能粒子分布不对称（Fig. 5 上游扩散）

**[FACT]** 图 5 左上（Ensemble 平均）显示：
- 峰值强度在激波面（$r = 5 L_{c}$）
- 极区强度**向上游延伸更远** —— 扩散衰减尺度大

**[FACT]** 原因：$\kappa_{\parallel} \gg \kappa_{\perp}$，极区场线与激波法向近乎平行，粒子沿平行方向扩散更有效。

**[INTERPRETATION]** 这导致极区上游预加速区**更厚**，对观测而言，极区方向探测到的高能粒子信号**更强、更宽**。

## 3.15 能量谱公式化总结

**[FACT]** 最终能谱形状分段：

| 能量区间 | 主导物理 | 谱形 |
|---------|---------|------|
| $E < E_{R}$ | 绝热冷却（下游膨胀） | 陡降 |
| $E \approx E_{R}$–$5\,E_{R}$ | 单圈回旋 bump | 隆起 |
| $E_{R}$–$100\,E_{R}$ | 近似 DSA 幂律 | $\propto p^{-4}$（球面略陡） |
| $E > 100\,E_{R}$ | 有限加速时间 + $\gamma(\theta)$ 变化 | 陡于 $p^{-4}$，指数截断 |

**[CRITIQUE]** 上述谱形是**test-particle**近似下的结果；自洽模拟（含宇宙线反压）可能出现：
- 激波预压缩（cosmic-ray modified shock）
- 亚冲击（subshock）形成
- 谱幂律偏离 $p^{-4}$（Blasi 2013 综述）

## 3.6 关键结果细节补写（基于 fulltext 实测）

### 3.6.1 三个长度尺度的计算限制 [FACT]

- **回旋半径** $r_{g0} = V_{sh}/\Omega_0$（$\Omega_0$ 为粒子在平均场 $B_0$ 中的回旋频率）
- **磁场相干尺度** $L_c$
- **激波在模拟最长时间 $t_{max}$ 处的半径** $R_{sh}(t_{max})$

Giacalone 明确写出计算限制：$L_c/r_{g0} \le 10^6$，因为模拟最长时间同量级于 $10^6 \cdot \Omega_0^{-1}$，时间步需短于 $\Omega_0^{-1}$ 以保持能量守恒。

**[FACT]** 这一限制意味着**无法直接模拟真实的 SNR 激波**：典型 SNR 参数下，激波半径约为质子回旋半径的 $\sim 4 \times 10^9$ 倍——超出本文计算能力约 3 个数量级。Giacalone 在 §4 明确讨论了这一差距以及可能的扩展路径。

### 3.6.2 三个能量区间的物理特征 [FACT]

Figure 3 显示的能量谱（Run 1/2/4，$L_c/r_{g0} = 10^4$ / $10^5$ / $10^6$）具有三个清晰区间：

1. **$E < E_R$**（$E_R = \frac{1}{2}m_p V_{sh}^2$ 为激波冲压能量）：谱因**绝热冷却**下降（球面激波的膨胀效应）
2. **$E_R < E < 5 E_R$**：出现\"鼓包\"特征——粒子在激波前沿执行**单次回旋轨道**后漂移到下游，沿动生电场方向漂移获得额外能量
3. **$5 E_R < E < (50\text{–}100) E_R$**：近似幂律，斜率略缓于平面激波 DSA 理论预言（因为模拟谱包含上游粒子的贡献，而理论只预言下游）
4. **$E > 100 E_R$**：快速变陡——**有限的加速时间**效应；同时加速率沿激波面变化（赤道最快、极区最慢）也影响高能端形状

**[FACT]** 峰值恰好出现在 $E_R$——即注入能量，与激波冲压能量一致，是 DSA 测试粒子模拟中的典型非扩散动力学特征。

**[CRITIQUE]** 峰值 $E_R$ 附近的\"鼓包\"特征（单次回旋轨道能量增益）在**自洽混合模拟**（Giacalone 2005b；Giacalone & Decker 2010）中**不出现**——那些模拟包含了激波微结构（如跨激波电势 cross-shock potential），而本文简化模型未纳入。因此本文 $E < 5 E_R$ 的\"鼓包\"应视为**简化模型的伪影**，而非真实的物理特征。

**[CRITIQUE]** $E > 100 E_R$ 的快速变陡不仅源于有限加速时间，还源于本文**未包含粒子自身产生的磁扰动**（Bell 1978; Lee 1983; Bell 2004 的 streaming instability 与 Bell 2004 的 non-resonant Bell 模式均被排除）——这些不稳定会放大磁场、减小扩散系数、加速更快，从而**推迟**高能截断；本文的截断位置因此**系统性低估**了真实 SNR 的高能延伸。

### 3.6.3 球面 vs 平面激波谱对比 [FACT]

Figure 4 将球面激波（黑）与平面激波（平行红 / 垂直蓝）对比：

- **平面垂直**谱延伸至**最高能量**——加速率最快（Jokipii 1987）
- **平面平行**谱延伸最低
- **球面**谱介于两者之间，**略超**平面平行——因为球面激波各处的局部法向角 $\theta_B$ 覆盖 $0^\circ$–$90^\circ$，加速率沿面变化
- 平面情况下无绝热冷却（无膨胀）；球面情况下绝热冷却是决定最终谱的重要机制

**[INTERPRETATION]** 球面激波能量谱**不**延伸至垂直平面激波的最高能量，这一结论对 SNR 宇宙线起源有直接意义：即使 SNR 激波在赤道附近局部垂直，**球面几何 + 绝热冷却**仍会压低高能延伸——这解释了为什么纯 DSA + SNR 在 PeV 附近出现\"膝点\"（knee at $\sim 10^{15}$ eV）所需的**额外机制**（磁场放大、非稳态加速等）不能省略。

### 3.6.4 粒子通量的极区聚集 [FACT]

Figure 5 显示 $E > 1000 E_R$ 粒子的归一化通量 $I$ 在 $(x, z)$ 平面上的分布：

$$I(x, z) = \frac{4\pi}{n_0 V_{sh}} \int_{1000 E_R}^{\infty} dJ(x, z, E) \, dE$$

- 峰值通量在**激波处**（$R_{sh} = 5 L_c$）
- 沿激波面**非均匀**：**极区（pole）通量最高**，赤道最低
- 极区通量向上游延伸更远——因为**沿磁场方向的扩散系数 $\kappa_\parallel$ 大于垂直方向 $\kappa_\perp$**（Giacalone & Jokipii 1999），而极区磁场近似平行于激波法向（局部平行），扩散衰减尺度大

**[INTERPRETATION]** \"粒子聚集于极区\"的现象由**磁场线连接时间**决定：Giacalone 用 Figure 6 的几何分析证明，极区磁场线（$\theta \approx 0$）从激波首次扫过该点（在赤道）后就**一直与激波相连**，连接时间 $\Delta T \approx T$（总时间）；赤道磁场线（$\theta \approx 90^\circ$）则 $\Delta T \ll T$——只有在极区附近的短时段内才与激波接触。

**[INTERPRETATION]** 这一\"极区聚集\"是**粒子输运的几何效应**，而非加速机制差异——事实上极区加速率最慢（局部平行），但粒子**留存时间最长**；赤道加速率最快，但粒子很快被下游流带走。这暗示在真实 SNR 中，高能宇宙线在 SNR 壳层上的**角分布不均匀**——极区累积密度最高，赤道最低。

**[INTERPRETATION]** \"极区聚集\"的**观测意义**：如果这一几何效应在真实 SNR 中成立，则在观测上应看到**SNR 与分子云相互作用**产生的 $\gamma$ 射线辐射沿壳层的**不均匀角分布**（极区亮、赤道暗）——这一预言可与 Fermi-LAT 高分辨率观测（Ackermann et al. 2013）交叉检验。

**[CRITIQUE]** 本文\"粒子聚集于极区\"的结论依赖**各向同性注入 + 均匀平均磁场**的假设——真实 SNR 中，激波上游的磁场**结构**（HRI, High-Reconnection Rate 区域、剪切流等）和**各向异性注入**（Giacalone 2005b 已讨论）会显著改变极区/赤道通量比。本文未讨论这些真实效应，因此\"极区聚集\"的**定量预言**需谨慎应用。

### 3.6.5 $s^2$ 湍流强度变化的影响 [FACT]

Figure 8（Run 5，$s^2 = 0.3$ vs 默认 $s^2 = 1$）显示：

- 低湍流强度下，**加速效率降低**（最大能量下降）
- 出现更明显的\"聚集区域\"（ensemble average 图中），但 Giacalone 承认**未定量建立聚集区与磁场线连接时间的关联**

**[INTERPRETATION]** $s^2$ 参数化（湍流方差 / 平均场平方）本质上是**磁场扰动强度**的度量。$s^2$ 下降意味着**磁场线扭曲减弱**、**垂直扩散 $\kappa_\perp$ 下降**——粒子更严格地被束缚在磁场线上，加速效率因此下降（因为 DSA 加速率 $\propto \kappa_\parallel / r_G^2$ 主导，而 $s^2$ 下降使 $\kappa_\perp$ 降低，间接降低沿面混合效率）。

**[CRITIQUE]** Giacalone 未定量建立\"聚集区\"与磁场线连接时间的关联（原文明确承认），这使 $s^2 = 0.3$ 的\"聚集\"现象停留在**定性描述**层次——对于理解湍流强度对 SNR 高能宇宙线角分布的影响，这一缺口意味着 $s^2$ 的**定量效应**仍需后续模拟补上。

### 3.6.6 加速率沿激波面的变化 [FACT]

Figure 6(c) 显示 DSA 理论中的加速率 $t_{acc}^{-1}$（归一化到平行激波加速率）作为 $\theta_B$ 的函数：

- **$\theta_B \approx 0$（极区）**：加速率最低（局部平行）
- **$\theta_B \approx 90^\circ$（赤道）**：加速率最高（局部垂直），比极区快 $\sim (1 + \eta^2 \xi^2)$ 倍

公式（Appendix B 推导）：

$$t_{acc}^{-1}(\theta_B) \propto \frac{\sin^2 \theta_B + (1 + \eta^2) \sin^2 \theta_B \cos^2 \theta_B}{(\eta \sin \theta_B + \cos \theta_B)^2}$$

其中 $\eta = \kappa_A / \kappa_\parallel$，$\xi = \kappa_\perp / \kappa_\parallel$。

**[INTERPRETATION]** 加速率沿激波面的**强各向异性**（赤道/极区差数倍）解释了 Figure 7 中**不同极角带的能量谱差异**：赤道带谱延伸至更高能量，极区带谱截断能量低得多——尽管极区**累积强度**更高（因连接时间长），但极区粒子的**最高能量**仍低于赤道。

**[INTERPRETATION]** 这一\"赤道加速快、极区累积多\"的**张力**是球面激波 DSA 的核心物理：高能粒子**初始加速**于赤道（快加速率），但**输运**过程中随磁场线向极区漂移而**累积**——这是理解真实 SNR 中\"最高能量粒子来自赤道、最强辐射来自极区\"观测现象的理论基础。

### 3.6.7 单场实现 vs ensemble average [FACT]

Figure 5 左右面板对比：

- **左**（Run 2, Ensemble average）：每个粒子经历不同磁场实现
- **右**（Run 3, Single realization）：所有粒子在同一磁场中运动

结果：**\"聚集区\"的形态在 single realization 下呈现斑块状**（patchy），特征尺度与 $L_c$ 相当——这对应 Giacalone 2005b 和 Giacalone & Jokipii 2009 讨论的\"patchy injection\"现象。

**[CRITIQUE]** Ensemble average 掩盖了**单个磁场实现下的空间不均匀性**——真实 SNR 只有一次磁场实现，因此\"patchy\"结构在真实 SNR 中**必然存在**，其特征尺度由 $L_c$ 决定（约 pc 量级）。Giacalone 在 §4 讨论中承认这一点，但未定量讨论\"patchy\"对观测（如 $\gamma$ 射线）的累积影响。
