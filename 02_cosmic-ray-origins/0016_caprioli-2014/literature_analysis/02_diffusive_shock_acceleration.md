---
title: "§2 DIFFUSIVE SHOCK ACCELERATION"
paper: "Caprioli & Spitkovsky 2014, ApJ 783, 91"
outline_ref: "§2 DIFFUSIVE SHOCK ACCELERATION"
---
> 上一章：[[02_cosmic-ray-origins/0016_caprioli-2014/literature_analysis/01_introduction.md|01_introduction]]
> 下一章：[[02_cosmic-ray-origins/0016_caprioli-2014/literature_analysis/03_supra_thermal_particles.md|03_supra_thermal_particles]]

#### 2.1 [FACT] 模拟设置

- **[FACT]** Hybrid 代码为自开发（Spitkovsky 2005, PoP），求解非相对论离子 Vlasov 方程 + 电子流体的 MHD；电子是冷流体，绝热跟随离子并维持准电中性。
- **[FACT]** 平行激波模拟盒 $(L_x, L_y) = (10^5, 10^2) [c/\omega_p]^2$，离子 skin depth 每 cell 2 个、每 cell 4 macro-particles；$\Delta t = 5\times10^{-3} \omega_c^{-1}$；演化至 $t = 2500 \, \omega_c^{-1}$。
- **[FACT]** 本文统一用 $M \equiv M_A \approx M_s$ 表示激波强度（声马赫与阿尔芬马赫相当）。
- **[FACT]** 激波产生方式：超音速流冲击反射壁（图左），反射流与入射流相互作用形成激波并向右传播；模拟中下游流体静止。
- **[FACT]** Mach 数参考系变换：激波参考系 $\tilde{M}$ 与本文 $M$ 关系（方程 1）
$$\tilde{M} = \frac{M}{\sqrt{1+\frac{1}{r(\tilde{M})}}}, \quad r = \frac{(\gamma+1)\tilde{M}^2}{(\gamma-1)\tilde{M}^2+2}$$
  强激波 $r=4$ 时 $\tilde{M} = 5M/4$。

#### 2.2 [FACT] DSA 谱在下游被恢复（Figure 1）

- **[FACT]** Figure 1：下游离子能量谱随时间演化。低能区：Maxwellian（dashed），晚期 $T \approx 80\%$ 的无 CR 强激波预期温度。
- **[FACT]** 高能区：$f(E) \propto E^{-1.5}$，$E \gtrsim 3 E_{\text{sh}}$，其中
$$E_{\text{sh}} = \tfrac{1}{2} m v_{\text{sh}}^2 = \tfrac{1}{2} m M^2 v_A^2$$
- **[FACT]** 谱 $E^{-1.5}$ 对应动量空间 $p^{-4}$——**与 DSA 强激波非相对论预言一致**。
- **[FACT]** DSA 机制：粒子在激波上下游扩散往返，每次经历一阶 Fermi 加速；谱仅依赖 $r$。
- **[FACT]** 谱从 $f(p) \propto p^{-4}$ 换算：
$$4\pi p^2 f(p) \, dp = f(E)\,dE \implies f(E) = 4\pi p^2 f(p) \frac{dp}{dE}$$
  非相对论 $E=p^2/2m \Rightarrow dp/dE \propto E^{-1/2} \Rightarrow f(E) \propto E^{-1.5}$；相对论 $E\propto p \Rightarrow f(E) \propto E^{-2}$。

#### 2.3 [FACT] 谱的时间演化

- **[FACT]** 低能 Maxwellian 峰值与 $p^{-4}$ 尾随时间几乎不变。
- **[FACT]** 高能截断 $E_{\max}$ 指数截断 $\propto \exp(-E/E_{\max})^\tau$，$\tau \sim 1.5$，随时间向高能移动。
- **[FACT]** 大盒子保证 $E_{\max}(t)$ 至 $t \approx 2000 \omega_c^{-1}$ 不被有限尺寸人工限制，仅由加速时间决定。

## 关键参数

| 参数 | 值 | 单位/说明 |
|---|---|---|
| $(L_x, L_y)$ | $(10^5, 10^2)$ | $[c/\omega_p]^2$ |
| cells per ion skin depth | 2 | |
| particles per cell | 4 | macro-particles |
| $\Delta t$ | $5\times10^{-3}$ | $\omega_c^{-1}$ |
| 演化至 $t$ | $2500$ | $\omega_c^{-1}$ |
| $M$（声/阿马赫） | 20 | 主模拟 |
| 下游温度 | $0.8 \times T_{\text{strong shock, no CR}}$ | 减少 ~20% 因注入非热 |

## 我的理解 / Interpretation

**[INTERPRETATION]** §2 是**结果的核心展示**：图 1 就是整篇的"招牌图"。作者强调这是**首次**在自洽模拟中得到跨越近 3 个量级的 DSA 幂律——之前的模拟要么盒子太小，要么时间太短。$T_{\text{down}} < T_{\text{strong shock}}$ 说明 ~20% 能量被注入非热粒子，与 Bell 1978 的解析图景一致。

## 关键公式

- (1) $\tilde{M} = M / \sqrt{1+1/r(\tilde{M})}$
- (2) $E_{\text{sh}} = \tfrac{1}{2} m M^2 v_A^2$
- (3) $4\pi p^2 f(p) dp = f(E) dE$
