# 4. 非线性扩散激波加速（NLDSA）

> 本章属于：The origin of galactic cosmic rays (Blasi 2013 §4 & Amato 2014 §3)
>
> 上一章：`03_test_particle_dsa.md`
>
> 下一章：`05_magnetic_field_amplification.md`

## 4.1 需要 NLDSA 的三个物理原因（Blasi §4 首）

**[FACT]** Blasi 明确列出：

1. **加速粒子的动力学反作用**：ξ_CR ~ 10% → 加速粒子压力显著影响激波结构，通过改变压缩比 → 谱不再是单幂律，且依赖刚度。
2. **加速粒子诱导的等离子体不稳定性**：MFA（磁场放大）必须在**上游**发生（否则不能缩短加速时间），极可能是加速粒子自身驱动（streaming 不稳定）；因此扩散系数本身依赖于分布函数。
3. **放大磁场的动力学反作用**：100–1000 μG 场的磁压虽只是 ρv²_s 的 10⁻²–10⁻³，但可**超过**上游热压 → 影响压缩比 → 进一步耦合回分布函数。

**[INTERPRETATION]** 这三点构成"**三个非线性**"——粒子↔流体、粒子↔波、波↔流体。

## 4.2 加速粒子动力学反作用（Blasi §4.1 & Amato §3）

### 4.2.1 物理图像

**[FACT]** 加速粒子压力在上游建立"**前驱区**"（precursor）：
- 上游无穷远处流体速度 u₀；
- 加速粒子压力 P_c(z) 随距离向激波增大 → 流体减速 → 速度从 u₀ 逐渐降到 u₁（亚激波上游）；
- 在**亚激波**（subshock）处发生阶跃压缩 u₁→u₂；
- 总压缩比 R_tot = u₀/u₂ 可显著大于 4；亚激波压缩 R_sub = u₁/u₂ < 4。

**[FACT]** 图 7（Blasi Fig.7）：CR 修改的激波结构示意图，标注了 u₀、u₁、u₂、R_sub、R_tot。

### 4.2.2 守恒方程（Blasi 式 (53)-(67)）

**[FACT]** 三守恒方程 + 粒子输运方程 + 波能量方程：

**质量**（Blasi 式 (53)）：
$$\frac{\partial\rho}{\partial t} + \frac{\partial}{\partial z}(\rho u) = 0$$

**动量**（Blasi 式 (55)）：
$$\frac{\partial}{\partial t}(\rho u) = -\frac{\partial}{\partial z}\bigl(\rho u^2 + P_g + P_c\bigr)$$

**能量**（Blasi 式 (56) 及稳态式 (67)）：
$$\frac{\partial}{\partial t}\left(\frac{1}{2}\rho u^3 + \frac{P_g}{\gamma_g-1} + E_c\right) = -\frac{\partial}{\partial z}\left(\frac{1}{2}\rho u^3 + \frac{\gamma_g}{\gamma_g-1}u P_g + \frac{\gamma_c}{\gamma_c-1}u P_c\right) + \frac{\partial}{\partial z}\left(\bar{D}\frac{\partial E_c}{\partial z}\right)$$

其中 $E_c = P_c/(\gamma_c - 1)$ 是 CR 能量密度，γ_c 是 CR 的绝热指数。

**[FACT]** 粒子分布函数输运方程（Blasi 式 (61)）：
$$\frac{\partial f}{\partial t} + u\frac{\partial f}{\partial z} = \frac{\partial}{\partial z}\left(D\frac{\partial f}{\partial z}\right) + \frac{1}{3}\frac{du}{dz}\,p\frac{\partial f}{\partial p} + Q$$

**[FACT]** CR 能量密度与压力（Blasi 式 (62)-(63)）：
$$E_c(z) = \int_0^\infty dp\,4\pi p^2 T(p)\,f(p,z)$$
$$P_c(z) = \frac{1}{3}\int_0^\infty dp\,4\pi p^3 v(p)\,f(p,z)$$

**[FACT]** 含 CR 时稳态的 R_sub 与 R_tot（Blasi 式 (68)-(69)）：
$$R_{sub} = \frac{(\gamma_g+1)M_1^2}{(\gamma_g-1)M_1^2+2}$$
$$R_{tot} = \frac{M_0^2}{\left[(\gamma_g+1)R_{sub}^{\gamma_g} - (\gamma_g-1)R_{sub}^{\gamma_g+1}\right]/2}^{1/(\gamma_g+1)}$$

### 4.2.3 前置区的能量预算

**[FACT]** 前置区的能量学（Blasi 式 (70)）：

$$\xi_{CR}(z) \approx \frac{P_c(z)}{\rho_0 u_0^2} \approx 1 - \frac{u(z)}{u_0}$$

→ 上游气体减速的量直接对应被 CR 拿走的**动压份额**。

### 4.2.4 谱形状（Blasi Fig.8）

**[FACT]** 关键物理结果——**非线性谱不再单幂律**，而是**凹（concave）形**：
- 低能粒子扩散短、只看到亚激波 R_sub < 4 → 谱比 p⁻⁴ 更陡；
- 高能粒子扩散到前置区深处、看到 R_tot > 4 → 谱比 p⁻⁴ 更硬。

**[FACT]** Blasi Fig.8（Blasi et al. 2005）：M₀ = 10, 50, 100 三个 Mach 数下的粒子分布函数（热+非热）× p⁴ 图。p_max = 10⁵ GeV/c，ξ = 3.5。Mach 越高，凹性越强，下游热峰越左移（温度越低）。

**[FACT]** Amato 图 3（左：前置区速度/压力轮廓；右：下游谱）给出了相同物理图像。

### 4.2.5 数值方法（Blasi §4.1 尾）

**[FACT]** 三种主要数值方法：

| 方法 | 代表文献 | 特点 |
|---|---|---|
| 有限差分/差分格式 | Berezhko & Völk 1997, 2000; Zirakashvili & Ptuskin 2012 | 最好追踪时间演化 |
| Monte Carlo | Ellison & Eichler 1984; Knerr et al. 1996; Vladimirov et al. 2008 | 可处理非扩散效应 |
| 半解析 | Malkov 1997, 1999; Blasi 2002, 2004; Amato & Blasi 2005, 2006 | 快，易嵌入流体演化 |

**[FACT]** Amato 强调"thermal leakage"注入：$p_{inj} = \xi_{inj}\, p_{th,2}$，其中 $p_{th,2} = \sqrt{2m_p k_B T_2}$。典型 ξ_inj = 3.5。

**[FACT]** 新近 hybrid 模拟（Gargaté & Spitkovsky 2012; Caprioli & Spitkovsky 2013）显示注入概率可能与粒子动量**无关**——这与 thermal leakage 假设**矛盾**，是目前注入物理的最大不确定性。

## 4.3 关键预测汇总（Blasi §4 & Amato §4）

**[FACT]** 强加速 SNR 的四个可观测特征：

1. **R > 4**（已在 Tycho、SN1006 观测到 R ~ 7）；
2. **下游温度低于 Rankine-Hugoniot 预期**（在 RCW86 Hα 观测中首次得到支持）；
3. **凹形粒子谱**（少数 SNR 射电谱显示硬化）；
4. **放大磁场**（Chandra X 射线窄边缘 → ~100 μG）。

**[CRITIQUE]** 预测 #3（凹形谱，高能端比 E⁻² 硬）与观测到的 γ 射线谱（见第 7 章）存在**系统性张力**——几乎所有已测 SNR 的推断粒子谱比 E⁻² 更陡。
