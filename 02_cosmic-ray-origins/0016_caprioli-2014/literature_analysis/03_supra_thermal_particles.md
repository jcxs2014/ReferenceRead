---
title: "§3 SUPRA-THERMAL PARTICLES"
paper: "Caprioli & Spitkovsky 2014, ApJ 783, 91"
outline_ref: "§3 SUPRA-THERMAL PARTICLES"
---
> 上一章：[[02_cosmic-ray-origins/0016_caprioli-2014/literature_analysis/02_diffusive_shock_acceleration.md|02_diffusive_shock_acceleration]]
> 下一章：[[02_cosmic-ray-origins/0016_caprioli-2014/literature_analysis/04_acceleration_efficiency.md|04_acceleration_efficiency]]

#### 3.1 [FACT] Supra-thermal "桥"（Figure 2）

- **[FACT]** 远离下游：Maxwellian 与 $p^{-4}$ 尾之间边界**很尖锐**。
- **[FACT]** 紧邻激波后（图 2 红曲线）：存在"桥"——约一个能量量级的 supra-thermal 粒子，从 $\sim$ few $E_{\text{sh}}$ 到 $\sim 10 E_{\text{sh}}$，拟合为 $\propto E^{-3}$。
- **[FACT]** 该桥在下游 $\gtrsim 3000 \, c/\omega_p$ 后逐渐消失；热与非热谱清晰分离。

#### 3.2 [FACT] 注入动量与泄漏模型

- **[FACT]** Supra-thermal 区对理解热化及**粒子注入**（DSA 参与条件）关键——后激波存在 mildly non-thermal 粒子池。
- **[FACT]** 过去对 DSA 非线性背反作用综述：Drury (1983); Jones & Ellison (1991); Malkov & Drury (2001)。
- **[FACT]** 非线性 DSA 及唯象模型需要知道**注入粒子分数**（$\eta$），只能由自洽动力学模拟提供。
- **[FACT]** 常见假设：激波为无穷薄过渡（各向同性化+注入同时发生）。
- **[FACT]** **热泄漏模型**（thermal leakage）：Maxwellian 尾部的粒子若靠近激波、gyroradius 足够大，能在一个轨道内重穿激波（Ellison et al. 1981; Malkov 1997; Kang et al. 2002; Blasi et al. 2005）。
- **[FACT]** 替代观点：多数粒子被**激波面反射**（Guo & Giacalone 2013）——"泄漏"概念可能误导。

#### 3.3 [FACT] 注入阈值与注入分数

- **[FACT]** 定义注入能量 $E_{\text{inj}}$（图 2 下）为热与非热分界。注入动量：
$$p_{\text{inj}} = \xi_{\text{inj}} \, p_{\text{th}}, \quad p_{\text{th}} = \sqrt{2 m k_B T_d}$$
- **[FACT]** 强激波：$p_{\text{th}} = \frac{4\gamma\sqrt{\gamma-1}}{(\gamma+1)^2} m v_{\text{sh}} \approx 0.77 \, m v_{\text{sh}}$（$\gamma = 5/3$）。
- **[FACT]** 从图 2 推断 $E_{\text{inj}} \approx 4$–$5 \, E_{\text{sh}}$，因此 $\xi_{\text{inj}} \approx 3$–$3.5$。
- **[FACT]** 注入分数：
$$\eta \approx \frac{4\pi p_{\text{inj}}^3 f_{\text{th}}(p_{\text{inj}})}{n} \propto \xi_{\text{inj}}^3 \exp(-\xi_{\text{inj}}^2)$$
- **[FACT]** 对 $p^{-4}$ 谱 CR，每十倍能量贡献近常数——真实 SNR 谱延伸若干量级 $\Rightarrow$ 真实归一化小 $\sim \log_{10}(p_{\max}/p_{\text{inj}}) \approx 5$–$10$ 倍。
- **[FACT]** $\xi_{\text{inj}}$ 增加 0.2–0.5 即可补偿模拟能量范围的有限。
- **[FACT]** 结论：**平行非相对论激波注入 $\sim 10^{-3}$–$10^{-4}$ 的粒子进入 DSA**；$p_{\text{inj}} \approx 3$–$4 \, p_{\text{th}}$。
- **[FACT]** 注入机制留待后续论文讨论。

## 关键参数

| 参数 | 值 |
|---|---|
| $E_{\text{inj}} / E_{\text{sh}}$ | 4–5 |
| $\xi_{\text{inj}} = p_{\text{inj}} / p_{\text{th}}$ | 3–3.5 |
| $p_{\text{th}} / m v_{\text{sh}}$ | 0.77（强激波，$\gamma=5/3$） |
| $\eta$（注入粒子分数） | $\sim 10^{-3}$–$10^{-4}$ |
| supra-thermal 桥谱指数 | $\propto E^{-3}$ |

## 我的理解 / Interpretation

**[INTERPRETATION]** §3 处理 DSA 中最棘手的**注入问题**。作者给出可**外推到真实 SNR**的校准：虽然模拟只做 2 个量级，但 $\xi_{\text{inj}}$ 的微小上修 + 谱能量归一化修正，让 $\eta \approx 10^{-3}$–$10^{-4}$ 是合理的自洽推断。这一 $\xi_{\text{inj}} \approx 3$–$3.5$ 已直接喂入 Amato-Blasi 2014 等非线性 DSA 模型。
