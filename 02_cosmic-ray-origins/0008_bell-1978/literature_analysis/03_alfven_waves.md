# 03. Alfvén waves upstream of the shock（pp.152–156）
> 本章属于：[[02_cosmic-ray-origins/0008_bell-1978/literature_analysis/00_overview.md|The acceleration of cosmic rays in shock fronts — I]]
> 上一章：[[02_cosmic-ray-origins/0008_bell-1978/literature_analysis/00_overview.md|00_overview]]
> 下一章：[[02_cosmic-ray-origins/0008_bell-1978/literature_analysis/04_application_snr.md|04_application_snr]]

> **本节核心**：推导加速机制的**自洽性**——粒子如何激发它们自身散射所需的 Alfvén 波，以及能量上限 $E_{\rm crit}$ 的来源。

## 3.1 上游 Alfvén 波的产生（[FACT]）

**问题**：§2 假设了散射场存在，但散射场从哪里来？

**答案**：上游能量粒子以超 Alfvénic 流速（粒子速度 > Alfvén 速度）流出激波时，**激发 Alfvén 波**——波长 ≈ 粒子回旋半径。

> **物理过程**：粒子流 → 不稳定的反向流（resonant streaming instability）→ Alfvén 波湍流 → 散射粒子 → 粒子被束缚在激波附近 → 反复穿越加速

**闭合逻辑**：加速机制**自洽地产生自己所需的散射场**——这是本论文超越 1949 Fermi 概念的关键贡献。

## 3.2 粒子-波共同演化（[FACT]）

**扩散-对流-波方程**（方程 13-15）：

### 3.2.1 粒子扩散方程 (13)

$$\frac{\partial f}{\partial t} + u_1 \frac{\partial f}{\partial x} = \frac{\partial}{\partial x}\left(D(x)\frac{\partial f}{\partial x}\right) \tag{13}$$

$f$ 是粒子分布，与 §2 的 $n$ 概念类似但用动量空间分布。

### 3.2.2 扩散系数 (14)

$$D(x) = \frac{4}{3\pi}\frac{p\,v}{e\,B\,\mathcal{F}(x,p)} \tag{14}$$

**关键**：扩散系数 $D$ **反比于**波振幅 $\mathcal{F}$——波越强，散射越有效，粒子越难扩散。

> **这是自洽性方程**：$D$ 依赖 $\mathcal{F}$，$\mathcal{F}$ 又受粒子行为决定。

### 3.2.3 波演化方程 (15)

$$\frac{\partial \mathcal{F}}{\partial t} + u_1 \frac{\partial \mathcal{F}}{\partial x} - \sigma\mathcal{F} + \Gamma\mathcal{F} = 0 \tag{15}$$

- $\sigma$：波激发项（正贡献）
- $\Gamma$：波阻尼项（负贡献）

**关键非线性**：粒子驱动波 + 阻尼消耗波 = 平衡态。

## 3.3 波阻尼机制（[FACT]）

**3.3.1 中性粒子碰撞阻尼**

Kulsrud & Cesarksy 1971 模型：

$$\Gamma_n \propto n_H$$

**物理**：CR 粒子与中性氢碰撞时损失动量给波。

**3.3.2 声波损失**

Chin & Wentzel 1972、Skilling 1975b：

- 适用范围：波振幅较大、与离子声共振
- 特征：随波振幅增长而增强

## 3.4 临界能量 $E_{\rm crit}$（[FACT]）

**关键问题**：在什么能量下加速停止？

**自洽解**：在 $\mathcal{F}$ 平衡条件下，$D(x)$ 与 $x$ 关系导出**特征长度** $x_0$——加速区尺度。

**方程 (20)**（摘要）：特征长度与能量关系

$$x_0 \propto E^{1.5}$$

**自洽结论**：能量越高，加速区越大，达到 SNR 几何尺寸时被截断。

### 3.4.1 典型 SNR 参数下的 $E_{\rm crit}$

**方程 (23)** (摘要)：临界能量

$$E_{\rm crit} \sim 3.5 \times 10^{12}\ \text{eV} \tag{23}$$

**估算**（基于典型年轻 SNR 参数）：
- 激波速度 $v_s \sim 10^8$ cm/s
- 上游密度 $n_H \sim 1$ cm$^{-3}$
- 中性粒子碰撞率由 Kulsrud-Cesarksy 模型
- 磁场 $B \sim 10^{-5}$ G

> **物理含义**：在标准 SNR 环境下，加速上限约 3.5 TeV——超过此能量，谱指数变陡（"弯曲"）。

## 3.5 [INTERPRETATION] 本节的关键洞察

### 3.5.1 自洽性三件套

$$\text{粒子激发波} \xrightarrow{\text{通过 streaming instability}} \text{波散射粒子} \xrightarrow{\text{束缚粒子于激波}} \text{反复穿越加速}$$

**这是一个正反馈循环**，但被阻尼项稳定化。

### 3.5.2 为什么 $E_{\rm crit}$ 约 3.5 TeV——与"膝部"的关系

- 观测：宇宙线能谱在 $\sim 3 \times 10^{15}$ eV（**膝部**）变陡
- 本文 $E_{\rm crit} \sim 3.5 \times 10^{12}$ eV = 3.5 TeV — **比膝部低约 1000 倍**
- **解释**：本文是单个 SNR、单次加速的简单图像。要达到膝部能量，可能需要：
  1. 多 SNR 累积贡献
  2. 特殊环境（如超新星爆炸在致密星周介质中）
  3. 更复杂的非线性机制

**批注**：这一矛盾暗示 DSA 完整解释膝部需要 NLDSA 或多 SNR 累积——这是 1980s-2000s 的研究前沿。

## 3.6 [CRITIQUE] 本节局限

1. **极端参数假设**：$E_{\rm crit} \sim 3.5$ TeV 依赖典型 SNR 参数——实际 SNR 差异巨大（$n_H, v_s, B$ 均跨数量级变化）
2. **散射波来源**：本文假设"已存在"——但波激发方程形式上给出 $\sigma\mathcal{F}$ 项（粒子驱动）——**自洽性需要数值求解**，本文未给出具体数值结果
3. **多 SNR 问题**：单 SNR 上限 $\sim$ TeV，要达到 PeV 需要累积——但累积效率、能量释放、注入率等都未在本文范围
4. **非线性反馈**：本文 $D \propto 1/\mathcal{F}$ 隐含非线性——但仍在线性框架内求解

## 3.7 与实验观测的对接

### 3.7.1 早期验证（1978 年代）

- 地球弓激波：散射波存在 → 机制可行
- 卫星探测：电子能谱在某些 SNR 处有幂律形态

### 3.7.2 后续验证（1980s-2000s）

- 直接探测 CR 谱：$E^{-\mu}$ 形态在 $10^{10}$–$10^{15}$ eV 范围内确认
- $\gamma$ 射线观测：SNR 与 CR 加速的关联（如 IC 443）
- 同步辐射 X 射线：年轻 SNR 中电子加速到 TeV 能量

> **批注**：本文的"$\mu = 2.5$"预测在 1980 后逐步被观测支持，但膝部机制争论至 2000s。

## 3.8 §3 数学结构

- **第 3.1-3.2 节**：定性地建立粒子-波耦合
- **第 3.3 节**：列出阻尼机制（中性粒子摩擦、声波、Landau 等）
- **第 3.4 节**：解出自洽条件，得 $E_{\rm crit}$
- **第 3.5-3.7 节**：解释（理论 + 观测对接）

## 3.9 关键引用

- **Wentzel 1974**：Alfvén 波激发基础
- **Skilling 1975a, b, c**：粒子-波相互作用、波阻尼
- **Kulsrud & Cesarsky 1971**：中性粒子-波耦合
- **Chin & Wentzel 1972**：声波损失

## 3.10 与 Bell 系列后续论文的衔接

- **Bell 1978b (MNRAS 182, 443)** — Part II：非线效应 + 同步辐射
- **Bell 1978c** — Part III：激波正交（垂直）情形
- **Bell 2004** — Bell instability：解决了本文隐含的"波激发自洽性"问题

