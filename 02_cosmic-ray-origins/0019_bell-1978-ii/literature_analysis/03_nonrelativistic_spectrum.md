# 03. Acceleration of Non-relativistic Particles and the Resulting Energy Spectrum
> 本章属于：[[02_cosmic-ray-origins/0019_bell-1978-ii/literature_analysis/00_overview.md|The acceleration of cosmic rays in shock fronts — II]]
> 上一章：[[02_cosmic-ray-origins/0019_bell-1978-ii/literature_analysis/02_acceleration_shock_front.md|02_acceleration_shock_front]]
> 下一章：[[02_cosmic-ray-origins/0019_bell-1978-ii/literature_analysis/04_cosmic_ray_generation.md|04_cosmic_ray_generation]]

> **本节核心**：将 I 中相对论粒子的 DSA 推导延伸至**非相对论 regime**，讨论 $v_s/v$ 量级修正项如何改变谱指数，并在 $T_i \sim 10$ keV 注入能量下给出完整的非相对论粒子能谱。

## 3.1 非相对论性扩展的必要性（[FACT]）

**I 的假设回顾**：bell-1978 (I) 推导幂律谱时，假设粒子速度 $v \approx c$（相对论极限），使得：
1. 逃逸概率 $\eta = 4u_2/v \to 4u_2/c$（与能量无关）
2. 单次循环能量增长 $\Delta E/E \to 4(u_1-u_2)/c$（与能量无关）
3. 推导出**精确幂律谱** $N(E) \propto E^{-\mu}$

**本文 §3 的扩展**：注入粒子（§2）能量仅 $T_i \sim 10$ keV，对应质子速度：
$$v_p = \sqrt{2T_i/m_p} \approx \sqrt{2 \times 1.6\times10^{-8} / 1.67\times10^{-24}} \approx 1.4 \times 10^9 \text{ cm/s} \sim 0.05 c$$

- 此时 $v_s/v \sim 700/14000 \sim 0.05$，**不可忽略**
- I 中忽略的 $v_s/v$ 量级项在此 regime 变得重要
- **谱指数不再是常数**——能量越低越偏离 I 的幂律预测

> **[INTERPRETATION]**：这是从 DSA 数学推导到真实物理的第一个关键修正——**注入区段的谱行为**决定了加速后整体能谱的形态。

## 3.2 非相对论性逃逸概率（[FACT]）

**关键方程**：本文给出（OCR 提取）一次穿越-回穿越循环中粒子逃逸比例：
$$\delta = \frac{4u_1}{v}$$

其中 $u_1$ 为**上游**流速（注意：与 I 中 $\eta = 4u_2/v$ 用下游速度的区别）。

**物理理由**：非相对论 regime 下，粒子往返穿越激波时，**上游穿越**主导逃逸过程——粒子从下游返回上游后被对流带回时，逃逸概率由上游流速决定。

**对比**：
| 项 | I（相对论） | II (§3)（非相对论） |
|----|-----------|-------------------|
| 逃逸速度 | $v \approx c$ | $v \ll c$（$v$ 显含能量） |
| 逃逸率 | $\eta = 4u_2/c$（常数） | $\delta = 4u_1/v$（$\propto 1/\sqrt{E}$） |
| 与能量关系 | 无关 | 强相关 |

## 3.3 非相对论能量增长（[FACT]）

### 3.3.1 单次循环的能量变化

**相对论极限（I）**：
$$\frac{\Delta E}{E} = \frac{4(u_1-u_2)}{c}$$

**非相对论极限（本文）**：
$$\frac{\Delta E}{E} = \frac{4(u_1-u_2)}{v}$$

**关键差异**：$v$ 不再是 $c$，而是粒子的**瞬时速度**，随能量变化。

### 3.3.2 能量演化方程

对注入能量 $T_i$ 的粒子，第 $l$ 次循环后的能量 $E_l$ 满足：
$$\frac{dE}{dl} = \frac{4(u_1-u_2)}{v} E = \frac{4(u_1-u_2)}{\sqrt{2E/m_p}} E = 4(u_1-u_2)\sqrt{\frac{m_p E}{2}}$$

**解**：
$$\frac{dE}{\sqrt{E}} = 4(u_1-u_2)\sqrt{\frac{m_p}{2}} \, dl$$
$$2\sqrt{E_l} - 2\sqrt{E_0} = 4(u_1-u_2)\sqrt{\frac{m_p}{2}} \, l$$

$$\sqrt{E_l} = \sqrt{E_0} + 2(u_1-u_2)\sqrt{\frac{m_p}{2}} \, l$$

> **批注**：非相对论 regime 下能量**线性增长**（不是指数增长！），这是与相对论 regime 的本质区别。

## 3.4 非相对论谱指数（[FACT]）

### 3.4.1 逃逸概率的能量依赖

$$P(\text{survive } l \text{ cycles}) = (1-\delta)^l = \left(1 - \frac{4u_1}{v}\right)^l$$

在 $v = \sqrt{2E/m_p}$ 下：
$$\delta = 4u_1 \sqrt{\frac{m_p}{2E}} \propto E^{-1/2}$$

### 3.4.2 谱指数修正

**有效谱指数**：由于 $\delta$ 与 $E^{-1/2}$ 成正比（不是常数），非相对论 regime 下谱不再是精确幂律。

**本文给出**（OCR 摘要）：非相对论谱指数修正为
$$\mu_{\rm NR} = \mu_{\rm I} + \Delta\mu(T)$$

其中 $\Delta\mu(T)$ 在低能端**为正**——谱在低能端变陡。

### 3.4.3 $T_i \sim 10$ keV 的具体谱

**计算示例**：本文给出 $T_i \sim 10$ keV（$v_s \sim 700$ km/s）的粒子能谱——这是注入区段的**实际可观测能量范围**。

> **物理意义**：在注入能量附近，DSA 加速机制**已经开始工作但尚未完全建立幂律**——此时谱行为由非相对论修正主导。

## 3.5 注入能量 $T_i$ 的物理意义（[FACT]）

**注入能量的推导**：
- I 要求粒子速度 $v > v_s$ 才能被激波"捕获"
- 具体阈值由粒子穿越激波时不被对流带回下游的条件给出
- 本文给出 $T_i \approx 4 m_p v_s^2$

**与观测的对比**：
| 系统 | $v_s$ | $T_i$ |
|------|-------|-------|
| 地球弓激波 | 400 km/s | $\sim 2$ keV |
| 年轻 SNR | 700 km/s | $\sim 10$ keV |
| Cas A | $\sim 5000$ km/s | $\sim 500$ keV |

> **观测支持**：地球弓激波上游超热质子能量 $\sim 1$–$10$ keV，与 $T_i$ 估算一致。

## 3.6 加速时间尺度（[FACT]）

**相对论极限**：
$$t_{\rm acc} = \frac{3}{u_1-u_2} \frac{E}{E} \cdot \frac{c}{4} = \frac{3c}{4(u_1-u_2)}$$

（与能量无关，这是相对论 DSA 的核心性质）

**非相对论极限**：
$$t_{\rm acc} \sim \frac{l_{\rm escape} \cdot \lambda}{v^2} \sim \frac{v}{u_1-u_2} \cdot \frac{v}{u_1-u_2}$$

其中 $l_{\rm escape} \sim v/u_1$ 为逃逸前平均循环数。

> **物理含义**：非相对论粒子的加速时间**随能量增长**——低能粒子被快速加速到 $T_i$ 以上，但高能端渐近于相对论极限。

## 3.7 [INTERPRETATION] 谱形态的综合图像

**从注入到相对论的完整谱图像**：

```
低能端 (E < T_i)    注入区段 (E ~ T_i)     幂律区 (E >> T_i)
    |                      |                    |
 热分布               非相对论修正谱        精确幂律 E^{-μ}
(T < T_i)         (μ_NR > μ, 变陡)        (μ = 2-2.5)
    |                      |                    |
    |   注入阈值           |   交叉能量        |
    ▼                      ▼                    ▼
```

**关键参数**：
- $T_i$：注入阈值（本文 §2 给出 $\sim 4m_p v_s^2$）
- $E_{\rm cross}$：非相对论到相对论的过渡能量（$v \approx c$ 时）
- $E_{\rm crit}$：加速上限（I §3 给出 $\sim 3.5$ TeV）

## 3.8 [CRITIQUE] 非相对论扩展的局限

1. **准弹性散射假设**：本文仍假设粒子散射是弹性的——非相对论 regime 下库仑碰撞可能导致能量损失
2. **各向同性散射**：非相对论粒子的拉摩半径更小，散射各向异性更强
3. **未处理波激发率**：低能粒子激发 Alfvén 波的效率低于相对论粒子——§3 未讨论这一耦合
4. **数值因子**：$\Delta\mu(T)$ 的精确形式依赖注入细节，本文只给出量级估算

## 3.9 关键方程汇总

| 编号 | 方程 | 意义 |
|------|------|------|
| 逃逸 | $\delta = 4u_1/v$ | 非相对论逃逸率 |
| 能量增长 | $\Delta E/E = 4(u_1-u_2)/v$ | 非相对论能量增益 |
| 注入阈值 | $T_i \approx 4 m_p v_s^2$ | 注入最小能量 |
| 谱修正 | $\mu_{\rm NR} = \mu + \Delta\mu(T)$ | 非相对论谱指数修正 |

## 3.10 与 §4 的衔接

| 问 | 答 | 节 |
|---|---|---|
| 非相对论谱行为 | $\mu_{\rm NR}$ 在低能端变陡 | §3 |
| 注入粒子能谱 | $T_i \sim 10$ keV 起，幂律渐近 | §3 |
| SNR 宇宙线总产生率 | 用 §3 谱积分 | §4 |

下一节（§4）将 §2-§3 的注入和非相对论机制**综合应用于 SNR**，估算宇宙线产生总量。
