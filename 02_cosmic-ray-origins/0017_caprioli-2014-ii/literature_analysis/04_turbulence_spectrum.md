---
title: "§4 TURBULENCE SPECTRUM"
paper: "Caprioli & Spitkovsky 2014, ApJ 794, 46"
outline_ref: "§4 TURBULENCE SPECTRUM"
---
> 上一章：[[02_cosmic-ray-origins/0017_caprioli-2014-ii/literature_analysis/03_magnetic_field_amplification.md|03_magnetic_field_amplification]]
> 下一章：[[02_cosmic-ray-origins/0017_caprioli-2014-ii/literature_analysis/05_role_of_nrh_modes.md|05_role_of_nrh_modes]]

#### 4.1 [FACT] 谱的定义与测量（§4 引入）

- **[FACT]** §4 研究**中等大 $M$ 与非常大 $M$** 激波下游激波上游 precursor 内 DSA 加速粒子产生的磁湍流谱——两者磁场放大水平不同
- **[FACT]** 谱密度定义：对 $B_\perp(x)$ 在波数 $k$ 空间做傅里叶变换，记 $F(k)$ 为**单位对数带宽**波数 $k$ 的磁能密度，归一到初始能密度 $B_0^2/(8\pi)$：
$$\frac{B_\perp^2}{8\pi} = \frac{B_0^2}{8\pi}\int_{k_{\min}}^{k_{\max}} F(k)\frac{dk}{k} \qquad (3)$$
其中 $k_{\max}$ 由网格尺寸决定，$k_{\min}$ 由积分区间决定
- **[FACT]** $F(k)/k = |\tilde{B}_y(k)|^2 + |\tilde{B}_z(k)|^2$（非 $B_\perp(x)$ 的傅里叶变换，而是其分量之和）

#### 4.2 [FACT] $M=20$ 情况（Run B，图 6）——共振流不稳定性的完美符合

- **[FACT]** $t=2000\omega_c^{-1}$，激波在 $x_{\rm sh} \sim 10^4\,c/\omega_p$；在三个区域分别计算 $F(k)$：**下游**（$0 \le x \le x_{\rm sh}$）、**CR precursor**（$x_{\rm sh} \le x \le 2\times10^4$）、**远上游**（$2\times10^4 \le x \le 10^5$）
- **[FACT]** **CR precursor 谱**（品红色曲线）：$F(k) \propto k^{-1}$（由图 6 底符号定义，两竖直虚线之间，$E_{\rm sh}$ 与 $E_{\max} \sim 300 E_{\rm sh}$ 共振波数之间）
- **[FACT]** **松驰共振定义**：$k\,r_L(E,B_0) \sim 1$（忽略局地场与 $B_0$ 差异，以及仅 $p \perp B$ 分量参与共振）
- **[FACT]** $F(k)$ 在 $k \lesssim 1/r_L(E_{\rm sh})$ 与 $k \gtrsim 1/r_L(E_{\max})$ 偏离 $k^{-1}$——因 precursor 中无相应能量的共振离子
- **[FACT]** 除归一化外，**整个盒子** $F(k)$ 形状相似（图 6 不同曲线）
- **[FACT]** **远上游**（青色曲线）：高 $k$ 端在**对应 $E = 10 E_{\rm sh}$** 共振波数处陡化——与低能 CR 无法到达远上游一致

#### 4.3 [FACT] $M=80$ 情况（Run D，图 7）——NRH 信号的出现

- **[FACT]** $t=500\omega_c^{-1}$，$E_{\max} \sim 100 E_{\rm sh}$
- **[FACT]** 与 $M=20$ 相比**最大差异**：precursor 中 $F(k)$ **大 10 倍以上**（与 §3 磁场放大量级一致，$F \propto (B_{\rm tot}/B_0)^2$）
- **[FACT]** 大多数能量仍在共振波数之间（竖直虚线之间）
- **[FACT]** 峰值不在 $k\,r_L(E_{\max},B_0) \sim 1$，而略高——因 precursor 实际场为几个 $B_0$
- **[FACT]** **远上游**（青色）峰值波数比 precursor **大 2–3 倍**——**不能**归因于局地场显著大于 $B_0$，而是反映**远上游不稳定模式的性质与演化**（§5 讨论）
- **[FACT]** 远上游在 $1/r_L(100 E_{\max}) \le k \le 1/r_L(E_{\max})$ 处 $F(k) \gtrsim 0.1$：这些模式可能由**能量高于 $E_{\max}$ 的逃逸粒子**激发，或为**长波长不稳定性**（如 firehose，Blandford & Eichler 1987；Shapiro et al. 1998）

#### 4.4 §4.1 [FACT] 共振流不稳定性理论框架

- **[FACT]** 稳态增长/输运方程（McKenzie & Völk 1982）：
$$\partial_x\left[u(x) F(k,x)\right] = \Gamma(k,x) F(k,x) \qquad (4)$$
其中 $\Gamma(k,x)$ 是磁模式能量增长速率；不显式包含磁模式阻尼（通过加热 precursor 与气体压力平衡，Paper I §6.1）
- **[FACT]** Alfvén 波增长（共振流不稳定性；Skilling 1975b；Bell 1978；Achterberg 1983）：
$$\Gamma(k,x) = \frac{4\pi^2 v_A}{3 P_{w,0} F(k,x)} \int p^4 v(p) f(x,p)\,\delta(p-p_{\rm rk})\,dp \qquad (5)$$
其中 $P_{w,0} = B_0^2/(8\pi)$，$f(x,p)$ 为局部离子分布各向同性部分，$p_{\rm rk} = mc/k$ 为共振动量
- **[FACT]** 假设电磁与动能密度**等分**：$\Gamma(k,x) \simeq 2 u_x F(k,x)$；重写 (4)：
$$u_x(x)\,\partial_x P_w = v_A\, P(p_{\rm rk}, x) \qquad (6)$$
其中 $P(x,p) \equiv \frac{4\pi p^3 v(p) f(x,p)}{3}$ 为单位对数动量带宽 CR 压；$P_{\rm cr}(x) = \int_p^{\infty} P(p,x)\,dp$（公式 7）
- **[FACT]** 忽略 precursor 激波修正、假设 $P$ 与 $F$ 在无穷远消失 → 积分：
$$P_{w,0} F(k,x) = v_A P(p_{\rm rk}, x) \qquad (8)$$
- **[FACT]** **关键物理解读**：(8) 式表明**共振流不稳定性激发的磁湍流能谱，正比于对应共振动量处的 CR 能量密度**
- **[FACT]** 对 $f(p) \propto p^{-4}$ 非相对论粒子，$P(p) \propto p$，能量集中在高动量 → 对应波谱 $F(k) \propto k^{-1}$，与图 6 precursor 完美符合
- **[FACT]** $M=80$（图 7）$F(k) \propto k^{-1}$ 尺度**不明显**——因非热尾尚未完全发展（Part I），CR 谱比 $p^{-4}$ 更陡

#### 4.5 [FACT] Alfvén 速度在非线性区的影响

- **[FACT]** $B_{\rm tot}/B_0 \propto \sqrt{M_A}$ 的标度律暗示 SNR 激波 precursor 中应有共振流不稳定性
- **[FACT]** 但**尚不清楚** (8) 式中 $v_A$ 在非线性区是否仍用 $B_0$
- **[FACT]** 周期性盒子 PIC 模拟（Riquelme & Spitkovsky 2009）显示：非线性阶段 $v_A$ **与磁场成正比增长**，自生模式增强相速度
- **[FACT]** 该相速度增强可能解释 $\gamma$ 射线亮 SNR 的**陡离子谱**（Caprioli 2011, 2012）
- **[FACT]** 本文模拟**无定论**：需要强激波长时间运行以判定 CR 谱是否相对正则值 4 有约 10%–20% 的变陡

#### 4.6 §4.2 [FACT] 对激波倾角的依赖（图 8）

- **[FACT]** 所有运行 $M=10$，$(L_x, L_y) = (4\times10^4, 500)\,c/\omega_p$，$\Delta t = 10^{-3}\omega_c^{-1}$（Run E）
- **[FACT]** 上游厚度 $5000\,c/\omega_p$ 内计算 $F(k)$，$t=200\omega_c^{-1}$；$\vartheta = 0°, 45°, 80°$（$B_0 = (B_0\cos\vartheta, B_0\sin\vartheta, 0)$ 与 $v_{\rm sh}$ 夹角）
- **[FACT]** **$\vartheta = 0°$ 与 $\vartheta = 45°$**：相似，符合 $F(k) \propto k^{-1}$
  - 在 $\vartheta = 45°$：细丝化不稳定性**适度抑制**，$B_\perp/B_0$ 小于平行情况；但斜几何**促进高能粒子回流**，扩散时间减半，$E_{\max}$ 达到平行情况两倍 → 图 8 中 $\vartheta = 45°$ 曲线峰值波数低于 $\vartheta = 0°$
- **[FACT]** **$\vartheta = 80°$**：无加速离子上游传播，$F(k) \lesssim 10^{-3}$（$k\,r_L(E_{\rm sh}) \sim 1$）——**无有效磁湍流生成**

## 关键参数

| 参数 | 值 | 出处 |
|------|-----|------|
| $F(k)$ 在 $M=20$ precursor | $\propto k^{-1}$ | 图 6 |
| $F(k)$ 在 $M=80$ 远上游峰值 | 比 precursor 大 2–3×波数 | 图 7 |
| 共振条件 | $k\,r_L(E,B_0) \sim 1$ | §4 |
| $P_{w,0}$ | $B_0^2/(8\pi)$ | (5) |
| $F(k)$ 与 CR 谱关系 | $P_{w,0}F(k) = v_A P(p_{\rm rk}, x)$ | (8) |
| $\vartheta = 45°$ $E_{\max}$ 相比平行 | $\sim 2\times$ | §4.2 |
| $\vartheta = 80°$ $F(k)$ | $\lesssim 10^{-3}$ | §4.2 |

## 我的理解 / Interpretation

**[INTERPRETATION]** §4 通过 $F(k) \propto k^{-1}$ 的观测验证了**共振流不稳定性**是中等强度激波（$M \lesssim 30$）precursor 中 MFA 的主通道。(8) 式的物理解读极其简洁：**磁湍流谱是 CR 谱的镜像**——CR 谱越陡，波谱越陡。$M=80$ 远上游的"异常"峰值（§5 将证明是 NRH 模式）在此章已被明确标记为"非局地场效应"。
