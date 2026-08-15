---
chapter: 7
title: "Transport Equations, Images and Quantum-Gravity Effects"
pages: "31–40"
sections:
  - "4.7.1 One-Dimensional Boltzmann Equation"
  - "4.7.2 Angle-Time-Energy Images"
  - "4.8 Anomalous Kinematics, Quantum Gravity Effects, Lorentz symmetry violations"
related_chapters:
  prev: 06_magnetic_fields_constraints
  next: 08_acceleration_sources
status: done
---

> 本章属于：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/00_overview.md|Bhattacharjee & Sigl (1999), *Phys. Rep.* 320, 1–150]]
>
> 上一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/06_magnetic_fields_constraints.md|06_magnetic_fields_constraints]]
>
> 下一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/08_acceleration_sources.md|08_acceleration_sources]]

# 7. Transport Equations & Quantum-Gravity Effects (§4.7–4.8, p. 31–40)

[FACT] §4.7–4.8 覆盖 pp. 31–40，是全文最"计算"化的章节。§4.7 系统给出粒子种类耦合 Boltzmann 方程、求解方法，以及 angle-time-energy 图像分析（Monte Carlo + 扩散近似 + rectilinear）；§4.8 转向新物理：Lorentz invariance violation、量子引力色散、快子中微子。

[INTERPRETATION] §4.7 把 EHECR 传播问题归约为"三种典型磁场强度区间"（rectilinear / transition / diffusion）+ "三种源时标区间"（burst / quasi-continuous / steady）的**联合参数扫描**，从而把观测到的角度-能量-时间图像映射为 $(B, l_c, d, T_S)$ 的约束。§4.8 则展示：若在 EHECR 尺度出现 Lorentz 对称性微破缺，几乎所有 GZK 分析都要重写。

---

## 4.7 Detailed Calculations of Ultra-High Energy Cosmic Ray Propagation

[FACT] §4.7 系统给出多粒子耦合传播方程、各类粒子求解方法、以及用 angle-time-energy 图像反演 EGMF 与源参数的方法。

### 4.7.1 One-Dimensional Boltzmann Equation

> **一维 Boltzmann 方程**

[FACT] 对一组粒子种类 $i$，局域能量密度 $n_i(E)$ 的演化（公式 35）：

$$
\partial_t n_i(E) = -n_i(E)\!\int d\!\epsilon\,n_b(\!\epsilon\!)\!\int_{-1}^{+1}\!d\mu\,\frac{1-\beta_b\beta_i}{2}\!\sum_j \sigma_{i\to j}\!\bigl[s\!=\!\epsilon E(1-\beta_b\beta_i)\bigr]
$$
$$
+\!\int dE'\!\int d\!\epsilon\,n_b(\!\epsilon\!)\!\int_{-1}^{+1}\!d\mu\!\sum_j \frac{1-\beta_b\beta'_j}{2}\,n_j(E')\frac{d\sigma_{j\to i}}{dE}\!\bigl[s\!,\,E\bigr] + \Phi_i
$$

- 第一项：species $i$ 通过相互作用**损失**；第二项：其他 species $j$ 通过相互作用**产生** $i$；第三项：注入。

[FACT] **求解方法**：

| 粒子 | 求解方法 | 参考 |
|---|---|---|
| 核子/核 | CEL 近似 [288,289] 或精确 Boltzmann 方程 [290,156,291]；Monte Carlo [292,26,293,294]；核光致分裂 MC [25,167,169] | |
| EM cascade | Hybrid MC + matrix doubling [296] 或隐式数值 [156,205,206]；能量覆盖 100 MeV – $10^{16}$ GeV (GUT scale) | [259,295] |
| 中微子 | 完整 Boltzmann 方程 [195]；规范流量 [196]；半解析 [298] | |
| 全耦合 | [205,206] 集成代码：nucleons + $γ$ + e + $ν$ 联立 | |

[CRITIQUE] **CEL 近似的局限**：
- 对 PPP（小非弹性度）：**优秀**。
- 对 $π$ 产生（大非弹性度，随机性）：CEL 在 GZK 截断**正下方**产生更尖锐的堆积谱（"pile-up"）vs 精确解 [290]。
- CEL 对连续源分布或远距离 discrete 源**仍可工作**（多次 $π$ 产生事件平均下）。

**关键公式**：

$$
\boxed{\partial_t n_i(E) = -\text{loss}(n_i) + \text{gain}(n_j\to n_i) + \Phi_i \;\;{\rm (Eq.\ 35)}}
$$

### 4.7.2 Angle-Time-Energy Images

> **角度–时间–能量图像**

[FACT] **强偏转 (Diffusion 近似)**：大尺度磁场（$10^{-8}\text{–}10^{-6}$ G，如星系团内）→ 扩散近似适用。能量损失–扩散方程（公式 36）：

$$
\partial_t n(r,E) = -\partial_E\bigl[b(E)\,n(r,E)\bigr] + \nabla\!\cdot\!\bigl[D(r,E)\,\nabla n(r,E)\bigr] + \Phi(E)
$$

- 若 $D(r,E)$ 不依赖 $r$ → **Syrovatskii 解析解** [300]。
- 应用于 EGMF ~几$\times 10^{-8}$ G，$E$ 至 $\sim 10^{20}$ eV。
- 但在 UHECR 实际应用中，**扩散近似与 rectilinear 之间的过渡区**是典型情况，此方程适用性有限。

[FACT] **各向异性（公式 37）**：

$$
\delta(E) = \frac{3\,D(r,E)}{n(r,E)}\,|\nabla n(r,E)|
$$

[FACT] **小偏转 (Monte Carlo, 3D)**：磁场建模为 Gaussian 随机场，零均值，功率谱 $B^{2}(k) \propto k^{n_{\rm H}}$ for $k < k_c$，$k_c = 2\pi/l_c$。MC 流程：傅里叶生成磁场网格实现 → 注入粒子 $E$ 对数均匀分布 → 求解运动方程（含 $π$ 产生 + PPP）→ 记录到达能量、时间、方向 → 40000 粒子 → time-energy histogram → Poisson 抽样模拟观测事件。

[FACT] **关键参数与 likelihood**：$\tau_{100}$（$E = 100$ EeV 处磁偏转延迟，公式 32）；$T_S$（源发射时间尺度，$T_S \ll 1$ yr = burst，$T_S \gg 1$ yr = 连续源）；$\gamma$（注入谱微分指数）；$N_0$（源到探测器的总 fluence）。

[FACT] **EGMF 约束（公式 38，来自 AGASA 200 EeV 事件对分析）**：

$$
B \lesssim 2\times10^{-11}\left(\frac{l_c}{1\,{\rm Mpc}}\right)^{-1/2}\left(\frac{d}{30\,{\rm Mpc}}\right)^{-1}\,{\rm G}
$$

- 若证实，比 Faraday rotation 强两个量级。

[FACT] **五种 generic time-energy 图像情形**（按 $\tau_E$ vs $T_S$ vs 实验寿命）：
- $\tau_E \ll T_S$：距离由 pion 产生特征（GZK cutoff 以上）确定，误差 $\sim 2\times$。
- $T_S \ll \tau_E < $ 实验寿命：磁场强度可从 time-energy 图像得到。
- $T_S \gg \tau_E \gg$ 实验寿命：只能给磁场下限（与 Faraday 结合可得数量级估计）。
- $T_S \sim \tau_E$：最佳参数估计情况。

[FACT] **发射时间尺度可探测范围（公式 39）**：

$$
3\times10^{3}\left(\frac{\Delta\theta}{1°}\right)^{2}\left(\frac{d}{10\,{\rm Mpc}}\right)\,{\rm yr} \lesssim T_S \simeq \tau_E \lesssim 10^{4}\text{–}10^{7}\left(\frac{E}{100\,{\rm EeV}}\right)^{-2}\,{\rm yr}
$$

[FACT] **一般情形：扩散 vs rectilinear 的过渡区**（Monte Carlo 推广到任意偏转 [311]）：Supergalactic Plane 建模为厚度几 Mpc、密度高斯剖面的 sheet；Kolmogorov 谱 $n_{\rm H} = -11/3$（Kraichnan 谱 $n_{\rm H} = -7/2$ 也考虑）。

[FACT] **扩散系数（公式 40）**：

$$
D(E) \simeq \frac{1}{3}\,r_g(E)\,B\!\int_{1/r_g}^{\infty}\!dk\,k^{2}\,\langle B^{2}(k)\rangle
$$

- Kolmogorov 谱下：扩散区（$\tau_E \gtrsim d$）：$D(E) \propto E^{1/3}$（$r_g < L/2\pi$）→ $\tau_E \propto E^{-1/3}$；Bohm 扩散（$r_g > L/2\pi$）：$D(E) \propto E$ → $\tau_E \propto E^{-1}$；Rectilinear：$\tau_E \propto E^{-2}$。

[FACT] Fig. 19 显示 bursting source 上 $\tau$–$E$ 关系的三个 regime；Fig. 20：最优场强（源 $d=10$ Mpc, $B_{\rm max} = 10^{-7}$ G）对 $E > 10$ EeV 数据的最佳拟合；有效回旋半径 ~解析估计的 10×；不同磁场实现间谱涨落显著。

[FACT] **现代 AGASA 数据启示**：最新 AGASA 数据显示 EHECR **各向同性** [83]。单一源 + 强场解释 → GZK 以上通量被过度抑制 → **需要连续源分布** [314]。弥漫源分布 + Supergalactic Plane 关联 + **$B \gtrsim 0.05\,\mu$G** → 可解释大尺度各向同性 + 小尺度聚团 [316]。Fig. 24：$B_{\rm max} = 0.05$ 和 0.5 $\mu$G 均能很好地拟合数据。

**关键公式**：

$$
\boxed{B \lesssim 2\times10^{-11}\left(\frac{l_c}{\rm Mpc}\right)^{-1/2}\left(\frac{d}{30\,{\rm Mpc}}\right)^{-1}\,{\rm G}\;,\quad D(E)\propto E^{1/3}\text{ (Kolmogorov)},\ E,\ E^{-2}\text{ (Bohm/rect)}}
$$

---

## 4.8 Anomalous Kinematics, Quantum Gravity Effects, Lorentz symmetry violations

[FACT] §4.8 转向超出标准模型的传播效应：Lorentz 不变性破坏、量子引力色散、快子中微子。

### 4.8.1 Lorentz Invariance Violation (VLI) 约束

> **Lorentz 不变性破坏约束**

[FACT] 若 $10^{20}$ eV 事件是质子 → $(c_p - c) < 10^{-23}$（否则质子会在 ~几百 cm 内通过 Cherenkov 辐射损失能量）。VLI 可避免 GZK 截断（微小偏离下，阈值升高）。**VPE (Violation of Equivalence Principle) 等效** → 质子与光子的引力耦合差异 $< 10^{-19}$（比 Eötvös 实验精确 5 个量级）。

### 4.8.2 量子引力色散关系

> **量子引力色散关系**

[FACT] **色散（公式 41）**：

$$
c^{2}k^{2} \simeq E^{2} + \chi\,\frac{E^{3}}{E_0}
$$

- 对应光子群速度 $\partial E/\partial k = c\bigl[1 - \chi\,E/E_0 + \mathcal{O}(E^{2}/E_0^{2})\bigr]$。
- $\chi = \pm 1$；$E_0$ = 量子引力尺度。

[FACT] **阈值（公式 42）**：

$$
\epsilon \simeq \frac{E}{4}\cdot\frac{m_e^{2}}{E_1 E_2 + \theta_1\theta_2} + \chi\,\frac{E^{2}}{4 E_0}
$$

- **$\chi < 0$ ($c_\gamma > c_p$)**：$E > E_c$ 时光子可自发衰变 → 河外光子传播受阻 → 观测 > 20 TeV 河外光子 [328,329] 约束 **$E_0 \gtrsim M_{\rm Pl}$** 或 $(c_i^{2} - c^{2}) > \sim -2\times10^{-17}$。
- **$\chi > 0$**：$E > E_c$ 时 $\epsilon$ 增长 → 光子传播不受阻 → 可观测 > 100 TeV 来自 > 100 Mpc 的河外光子。

[FACT] **时间色散**：

$$
\Delta t \simeq \frac{d}{c}\left(\frac{E}{E_0}\right) \simeq 1\left(\frac{d}{100\,{\rm Mpc}}\right)\left(\frac{E}{\rm TeV}\right)\left(\frac{E_0}{M_{\rm Pl}}\right)^{-1}\,{\rm s}
$$

- Mrk 421 > 2 TeV $γ$ 在 300 s 内到达 → $E_0 > 4\times10^{16}$ GeV [331]。
- HEGRA 若观测到 > 200 TeV GRB $γ$ 在 200 s 内 → $E_0 \simeq M_{\rm Pl}$。

### 4.8.3 快子中微子

> **快子中微子**

[FACT] **Kostelecký [333]**：$ν_e$ 为 tachyon。核内质子可衰变 $p \to n + e^{+} + ν_e$，阈值 $E_{\rm th} = m(A,Z)\bigl[m(A,Z\pm 1) + m_e - m(A,Z)\bigr]/|m_{ν_e}|$。

[FACT] 自由质子：$E_{\rm th} \simeq 1.7\times10^{15}/(|m_{ν_e}|/{\rm eV})$ eV。Ehrlich [334] 主张 $m_{ν_e}^{2} \simeq -(0.5\,{\rm eV})^{2}$ 可同时解释 knee 与高能端。

[CRITIQUE] 与氚 $β$ 衰变实验最佳拟合值 $m_{ν_e}^{2} < 0$ 一致（但最可能是实验未解决的系统问题），不过 $|m_{ν_e}^{2}|$ 值通常比 fit knee 所需大。预测 knee 附近有 neutron 谱线 [336]。

**关键参数**：$(c_p - c) < 10^{-23}$；$(g_p/g_\gamma) - 1 < 10^{-19}$；$E_0 > 4\times10^{16}$ GeV (Mrk 421)；$M_{\rm Pl} = 2.4\times10^{18}$ GeV；$\tau_E \propto E^{-2}/E^{-1}/E^{-1/3}$ (rectilinear/Bohm/Kolmogorov)。

---

## 元数据

```yaml
chapter: 7
pages: "31–40"
subsections: ["4.7.1", "4.7.2", "4.8.1", "4.8.2", "4.8.3"]
key_formulas:
  - "∂_t n(r,E) = -∂_E[b(E)n] + ∇·[D ∇n] + Φ (Eq. 36)"
  - "B ≲ 2×10$^{-11}$ (l_c/Mpc)$^{-1}$/$^{2}$ (d/30 Mpc)$^{-1}$ G (Eq. 38)"
  - "c$^{2}$k$^{2}$ ≃ E$^{2}$ + χ E$^{3}$/E$_{0}$ (Eq. 41)"
keywords:
  - CEL approximation
  - angle-time-energy image
  - Kolmogorov turbulence
  - Lorentz invariance violation
  - quantum gravity dispersion
  - tachyon neutrino
references_internal:
  prev_chapter: 06_magnetic_fields_constraints
  next_chapter: 08_acceleration_sources
```

**引用页码**：全文引用基于 *Phys. Rep.* 320 (1999), pp. 31–40。