> 本章属于：Solar System Abundances and Condensation Temperatures of the Elements (Lodders 2003)
>
> 上一章：`02_abundance_selection.md`
>
> 下一章：`04_major_trace_condensation.md`

# 3. Condensation Temperatures of the Elements（§ 3.1 计算方法精读）

## 3.1 本节核心内容
作者介绍 CONDOR 化学平衡代码的计算原理、两种冷凝温度的定义（appearance condensation temperature vs 50% condensation temperature），以及关键数学框架。所有计算都在总压 **p = 10⁻⁴ bar** 下进行——这是 1 AU 附近太阳星云的特征总压。

---

## 3.2 为什么选两套丰度表都算冷凝温度

[FACT] 作者明确说明：
- **太阳系（原始）丰度**：用于模拟太阳系星云及其他太阳金属度系统的化学；
- **太阳大气丰度**：作为其他恒星丰度归一化的标准参考，也需要自洽的冷凝温度。

[FACT] 大气金属度比太阳系低 ~16%，因此两套冷凝温度差约 **~10 K**。

---

## 3.3 CONDOR 代码（§ 3.1）

[FACT] CONDOR（Lodders & Fegley 1993, 1995, 1997; Fegley & Lodders 1994）同时处理：
- **2000 种气相物种**（分子、自由基、原子、离子）
- **1600 种凝聚相**
- **所有 83 种天然元素**

**优势**：所有元素化学同时求解——这至关重要，因为微量元素化学受主量元素化学强烈影响。

---

## 3.4 关键公式（§ 3.1）

### 3.4.1 元素总摩尔分数（式 7）

[FACT] 以 Al 为例：
$$X_{\text{Al}} = \frac{n(\text{Al})}{n(\text{H} + \text{H}_2 + \text{He})}$$
（实际分母还包含 CO、H₂O、N₂、Ne、离子等，但作者为清晰略去）

### 3.4.2 元素全分压（式 8）

$$P_{\text{Al}} = X_{\text{Al}} P_{\text{tot}} = P_{\text{Al}} + P_{\text{AlO}} + P_{\text{AlOH}} + \cdots$$

### 3.4.3 热力学活动表达的 Al 平衡（式 9）

[FACT]
$$P_{\text{Al}} = X_{\text{Al}} P_{\text{tot}} = a_{\text{Al}} \left[ K_{\text{Al}} + K_{\text{AlO}} f_{\text{O}_2}^{0.5} + K_{\text{AlOH}} (f_{\text{O}_2} f_{\text{H}_2})^{0.5} + \cdots \right]$$

其中 a_Al 是 Al 的热力学活动度，K_i 是 Al 各气体物种从参考态形成的平衡常数，f 是各元素的活动度/逸度。

[FACT] **CONDOR 中 Al 的质量平衡求和实际包含 ~80 种含 Al 气体**，最重要的有 Al、AlOH，其次 Al₂O、AlH、AlF、AlCl。

[FACT] **热力学数据源**：JANAF 表（Chase 1999）、Gurvich, Veyts & Alcock (1989)，及 Fegley & Lodders (1994)、Lodders & Fegley (1993) 列出的原始文献。

### 3.4.4 收敛准则

[FACT] 迭代求解所有元素耦合非线性方程组；**收敛要求：每个元素计算丰度与输入丰度一致到 1 part in 10¹⁵**。

### 3.4.5 凝聚相稳定性（式 10–11）

[FACT] 以刚玉（corundum）为例：
$$2\text{Al}(g) + 1.5\text{O}_2 = \text{Al}_2\text{O}_3(s) \quad \text{（式 10）}$$

[FACT] 热力学活动：
$$a_{\text{Al}_2\text{O}_3} = a_{\text{Al}}^2 \cdot f_{\text{O}_2}^{1.5} \cdot K_{\text{Al}_2\text{O}_3} \quad \text{（式 11）}$$
**当某纯相（Fe 金属、刚玉、FeS）的 a 达到 1 时，该相开始冷凝**——这就是"appearance condensation temperature"。

### 3.4.6 铁冷凝与蒸气压关系（式 13–15）

[FACT]
$$\text{Fe}(g) = \text{Fe}(metal) \quad \text{（式 13）}$$
$$\log K_{\text{Fe}} = \log(a_{\text{Fe}}/P_{\text{Fe}}) = A + B/T \quad \text{（式 14）}$$
$$-\log P_{\text{Fe}} = A + B/T \quad \text{（式 15）}$$

[FACT] 冷凝温度 = 气体分压 Pi = 凝聚相蒸气压 Pvap 时的温度。即**饱和比 S = Pi/Pvap = 1 = 活动度 aᵢ**。

### 3.4.7 氧逸度 fO₂ 的表达式（式 12）

[FACT]
$$P_{\text{O}} = X_{\text{O}} P_{\text{tot}} = 2 f_{\text{O}_2} + f_{\text{O}_2}^{0.5}[K_{\text{CO}} a_{\text{C}} + K_{\text{H}_2\text{O}} a_{\text{H}_2} + K_{\text{SiO}} a_{\text{Si}} + \cdots]$$

[FACT] 因太阳 O/C ≈ 2、O/Si ≈ 14，SiO 对 fO₂ 的贡献远小于 CO 和 H₂O；**H₂O/H₂ 比是 fO₂ 的便捷代理**。

[FACT] 本文 H₂O/H₂ ≈ **5.0 × 10⁻⁴**，约为 Anders & Grevesse (1989) 值（9.2 × 10⁻⁴）的一半 → **新 fO₂ 更低 → 所有氧化物/硅酸盐冷凝温度降低**。

---

## 3.5 两类冷凝温度的物理意义

### 3.5.1 Appearance Condensation Temperature（"冷凝温度"）

[FACT] 某元素/化合物首次从气相析出固相的温度。用于主量元素（Al、Fe 等）和最难熔元素。

### 3.5.2 50% Condensation Temperature

[FACT] 50% 的元素在固相、50% 在气相时的温度。对**微量元素**更有意义——因为其化学由主相宿主决定，50% T 是挥发性的更好指标。

[FACT] **关键特性**：微量元素的 50% T 与**其自身的总丰度无关**，而取决于主量宿主相的可用量与相对丰度。

[FACT] **固溶体活动系数**（Kornacki & Fegley 1986）：为处理非理想固溶体，采用活动系数修正，这是 Lodders & Fegley 一系列工作的核心方法。

### 3.5.3 平衡冷凝的适用与不适用

[FACT] **平衡冷凝适用**：太阳星云、原恒星与行星盘、质量损失巨星的星风（气相始终与固相平衡）。

[FACT] **平衡冷凝不适用**：巨行星、棕矮星、冷恒星的**大气**——重力沉降把主冷凝物移出冷气体层，阻止次级冷凝物形成。

---

## 3.6 元素分类（按冷凝行为）

[FACT] § 3.2–3.3 采用以下地质亲和性分类：
- **Lithophile**（亲石）：进入硅酸盐/氧化物（REE、Sc、Y、Zr、Hf、Ba、Sr、V、Nb、Ta、Th、U、Be、B、Li、Mn、Zn、Na、K、Rb、Cs）
- **Siderophile**（亲铁）：进入 Fe 合金（Co、Ni、Cr、Cu、As、Au、Ag、Bi、Ge、Pb、Pd、Sb、Sn、Te）
- **Chalcophile**（亲硫）：进入 FeS（troilite）（Cd、In、Se、Tl、Hg）
- **Atmophile**（亲气）：H、C、N、O、惰性气体

---

## 3.7 关键参数表

| 参数 | 值 | 说明 |
|------|----|------|
| 总压 P_tot | 10⁻⁴ bar | 1 AU 附近太阳星云 |
| 气相物种数 | 2000 | CONDOR |
| 凝聚相物种数 | 1600 | CONDOR |
| 收敛精度 | 10⁻¹⁵ | 元素丰度 |
| 计算元素数 | 83 | 全部天然元素 |
| 平衡常数据源 | JANAF / Gurvich | |
| 热力学活动系数 | Kornacki & Fegley 1986 | 非理想固溶体 |

---

## 3.8 我的理解

[INTERPRETATION] CONDOR 的核心是"同时求解所有元素的耦合质量守恒"，这是把微量元素的宿主相效应纳入自洽框架的关键。相比以往逐元素计算的方法，能自动处理：
1. 主量元素冷凝 → 微量元素化学随之改变
2. 氧逸度 fO₂ 的全局变化（因 C、N、O 下调）影响所有氧化物冷凝
3. 微量元素在多个可能宿主相间的分配

[CRITIQUE] CONDOR 是**热力学平衡**计算——对动力学效应的处理仅在§ 3.4（冰的冷凝）中通过"替代反应路径"粗略考虑。对于 10⁻⁴ bar 下真实星云的动力学、过饱和度、颗粒-气体耦合等，需要更专门的模型（Fegley 2000 综述）。
