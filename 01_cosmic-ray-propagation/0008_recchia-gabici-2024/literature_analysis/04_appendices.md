# 4. Appendices

> 本章属于：[Origin of the spectral features observed in the cosmic-ray spectrum](https://doi.org/10.1051/0004-6361/202349005)
>
> 上一章：`03_conclusions.md`
>
> 下一章：`98_vocabulary.md`

---

## Appendix A: Advection and adiabatic losses

> **附录 A：平流与绝热损失**

**[FACT]** 在本节中，我们论证在输运方程中忽略绝热损失的选择，表明对于典型 CR 谱，这种项可以吸收到拟合 CR 数据所需的平流速度 $u$ 的值中。为了使结果更明显，我们限制在 GH 中质子的传播（因此可以忽略散裂），具有刚性依赖的扩散系数和指向远离银盘的恒定平流速度，即 $du/dz = 2u\delta(z)$。

**[FACT]** 我们求解分布函数 $f(p, z)$ 的输运方程：

$$-\frac{\partial}{\partial z}\left[D \frac{\partial f}{\partial z} - u f\right] - 2u \delta(z) \frac{1}{3p^2} \frac{\partial (f p^3)}{\partial p} = q_0 \delta(z)$$

自由逃逸条件为 $f(p, H) = 0$。

---

### A.1. Solution for z ≠ 0

> **A.1. $z \neq 0$ 的解**

**[FACT]** 方程 (A.1) 变为：

$$D \frac{\partial f}{\partial z} - u f = K = \text{const}$$

利用条件 $f(p, H) = 0$ 和 $f(p, 0) \equiv f_0$，得到：

$$f(p, z) = f_0 \frac{1 - e^{-\frac{u}{D}(H-z)}}{1 - e^{-\frac{uH}{D}}}$$

---

### A.2. Integration around z = 0

> **A.2. 在 $z = 0$ 周围的积分**

**[FACT]** 利用 $f_0$ 在 $z = 0$ 处的连续性和 $\left.\frac{\partial f}{\partial z}\right|_{0^+} = -\left.\frac{\partial f}{\partial z}\right|_{0^-}$，得到：

$$-2D \left.\frac{\partial f}{\partial z}\right|_{0^+} + 2u f_0 - \frac{2u}{3p^2} \frac{d(f_0 p^3)}{dp} = q_0$$

**[FACT]** 项 $D \left.\frac{\partial f}{\partial z}\right|_{0^+} = -u f_0 \frac{e^{-\frac{uH}{D}}}{1 - e^{-\frac{uH}{D}}}$ 可以使用方程 (A.3) 计算并代入方程 (A.4) 得到 $f_0$ 的微分方程：

$$2u f_0 \frac{e^{-\frac{uH}{D}}}{1 - e^{-\frac{uH}{D}}} - \frac{2}{3} u p \frac{df_0}{dp} = q_0$$

其解为：

$$f_0(p) = \frac{3}{2u} \int_p^\infty \frac{dp'}{p'} q_0(p') \exp\left[-3 \int_p^{p'} \frac{dp''}{p''} \frac{e^{-\frac{uH}{D(p'')}}}{1 - e^{-\frac{uH}{D(p'')}}}\right]$$

**[FACT]** 在平流主导域（低动量）和扩散主导域（高动量）可以得到两个重要的极限。

---

### A.3. Approximate solution

> **A.3. 近似解**

**[FACT]** 在平流主导极限（$uH \gg D$）下，解近似为：

$$f_0(p) \approx \frac{3}{2u} \int_p^\infty \frac{dp'}{p'} q_0(p')$$

**[FACT]** 在扩散主导极限（$uH \ll D$）下，解近似为：

$$f_0(p) \approx \frac{3}{2} \int_p^\infty \frac{dp'}{p'} q_0(p') \frac{D(p')}{p'}$$

---

## Appendix B: Analytic solution for stable nuclei

> **附录 B：稳定核的解析解**

**[FACT]** 在本节中，我们推导稳定核的输运方程 (17) 的解析解，采用与第 3 节相同的 GD-GH 设置。

---

### B.1. Solution z≠0

> **B.1. $z \neq 0$ 的解**

**[FACT]** 在 GH 中（$h < z \leq h + H$），输运方程 (17) 的解为：

$$I_\alpha(z, E_k) = I_\alpha^0(E_k) \frac{1 - e^{-\frac{u}{D_H}(H^*-z)}}{1 - e^{-\frac{uH}{D_H}}}$$

其中 $I_\alpha^0(E_k)$ 是盘中的通量（$z = 0$）。

---

### B.2. Integration around z= 0

> **B.2. 在 $z = 0$ 周围的积分**

**[FACT]** 利用盘中通量 $I_\alpha^0$ 在 $z = 0$ 处的连续性，得到：

$$I_\alpha^0(E_k) = \frac{\tau_\alpha^{hH}}{1 + \frac{n_d}{h_d} \frac{h}{v(E_k) \sigma_\alpha \tau_\alpha^{hH}}} \times \left[\frac{1}{2h} Q_{\alpha,\rm src} + \frac{n_d}{h_d} \frac{h}{v(E_k)} Q_{\alpha,\rm spall}\right]$$

这与方程 (28) 相同。

---

## Appendix C: Analytic solution for unstable nuclei

> **附录 C：不稳定核的解析解**

**[FACT]** 在本节中，我们推导不稳定核的输运方程 (17) 的解析解，采用与稳定核相同的 GD-GH 设置。

---

### C.1. Solution for z≠0

> **C.1. $z \neq 0$ 的解**

**[FACT]** 对于不稳定核，输运方程包含额外的衰变项 $-\frac{I_\alpha}{\tau_r}$。在 GH 中，解为：

$$I_\alpha(z, E_k) = I_\alpha^0(E_k) \frac{\sinh\left(\frac{H^*-z}{\lambda_\alpha}\right)}{\sinh\left(\frac{H}{\lambda_\alpha}\right)}$$

其中 $\lambda_\alpha = \sqrt{D_H \tau_r}$ 是衰变长度。

---

### C.2. Integration around z= 0

> **C.2. 在 $z = 0$ 周围的积分**

**[FACT]** 利用盘中通量 $I_\alpha^0$ 在 $z = 0$ 处的连续性，得到：

$$I_\alpha^0(E_k) = \frac{\tau_\alpha^{hH}}{1 + \frac{n_d}{h_d} \frac{h}{v(E_k) \sigma_\alpha \tau_\alpha^{hH}} + \frac{\tau_\alpha^{hH}}{\tau_r}} \times \left[\frac{1}{2h} Q_{\alpha,\rm src} + \frac{n_d}{h_d} \frac{h}{v(E_k)} Q_{\alpha,\rm spall}\right]$$

---

### C.3. Relevant limits

> **C.3. 相关极限**

**[FACT]** 不稳定核的解在两个极限下特别有意义：

1. **短寿命极限**（$\tau_r \ll \tau_{\rm diff}$）：衰变项主导，通量指数衰减。

2. **长寿命极限**（$\tau_r \gg \tau_{\rm diff}$）：衰变项可忽略，解退化为稳定核的情况。

**[FACT]** 在单晕极限下，不稳定同位素的通量缩放为：

$$I_\alpha^0 \propto \begin{cases} \frac{H}{D} & \text{for } \tau_{\rm diff} \ll \tau_r \\ \frac{\tau_r}{\sqrt{D \tau_r}} & \text{for } \tau_{\rm diff} \gg \tau_r \end{cases}$$

**[FACT]** $^{10}$Be 与稳定同位素 $^9$Be 的比率趋于：

$$\frac{^{10}{\rm Be}}{^9{\rm Be}} \propto \begin{cases} \text{const} & \text{for } \tau_{\rm diff} \ll \tau_r \\ \frac{\sqrt{D \tau_r}}{H} & \text{for } \tau_{\rm diff} \gg \tau_r \end{cases}$$

**[FACT]** 测量不稳定同位素或同一核的稳定与不稳定同位素的比率提供了额外信息，允许确定 $H$ 的值。
