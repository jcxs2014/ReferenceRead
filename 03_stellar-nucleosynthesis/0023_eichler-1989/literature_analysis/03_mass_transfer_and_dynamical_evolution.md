# §3 质量转移与动力学演化

## [FACT] 潮汐瓣填满是次星先完成
- 对所有物态方程，**质量较小者（次星，secondary）半径 $R_2$ 较大**¹⁰。
- 因次星的**洛希瓣半径 $R_L$ 也较小**，故次星总是先填满其潮汐瓣 → 触发质量转移。

## [FACT] 稳定性判据
- 定义次星对洛希瓣的响应指数：
  $$ \zeta_2 \equiv \frac{\partial \ln R_2}{\partial \ln M_2}, \qquad \zeta_L \equiv \frac{\partial \ln R_L}{\partial \ln M_2} $$
- **稳定条件**：$\zeta_2 > \zeta_L$ — 质量转移在动力学上稳定。
- **不稳定条件**：$\zeta_2 < \zeta_L$ — 出现质量剥离式的失控。
- **判据的物理**：次星质量接近主星 → $\zeta_2 < \zeta_L$（不稳定）；初始质量比大 → 稳定的质量剥离过程。

## [FACT] 动力学不稳定情形
- Clark & Eardley (1977)¹ 讨论密近 NS 双星的演化。
- 对动力学不稳定的系统，**质量交换时标 $\Delta t_{\rm ex}$ 主导**引力波时标：
  $$ \Delta t_{\rm ex} \approx 6\ \text{ms}, \quad \text{取 } M_1 = 1.4\,M_\odot,\ M_2 = 1.2\,M_\odot $$
- 三维数值模拟（doubly-degenerate 双星¹¹）：较轻分量在**略多于 2 个轨道周期**（$\sim 4\ \text{ms}$）内完全耗散。
- 一旦质量转移时标短于引力波时标，质量损失迅速加速。

## [FACT] 次星坍缩成围绕主星的厚盘
- 次星被转化为**围绕主星旋转的厚轴对称盘**。
- 白矮星双星的类似构型由 Mochkovitch & Livio (1989)¹² 构造。
- Benz et al.¹³ 的计算：约 0.3% 的总质量逃逸系统。
- 本情形预期类似比例，因为该比例主要依赖两颗星表面势，正比于：
  $$ 1 - \frac{M_2 R_1}{M_1 R_2} $$

## [FACT] 角动量输运与时标
- 虽然总质量超钱德拉塞卡极限，**盘由离心力支撑** → 坍缩不立即发生。
- 动能/引力能比也指示稳定性。
- 盘的晚期演化**关键取决于角动量输运**。
- **简并物质粘滞**¹⁴（degenerate matter viscosity）：黏滞时标极长。
- **湍流粘滞**（Reynolds 数足够高时）：
  $$ \nu_{\rm turb} \approx (2\times10^9\ \text{cm}^2\text{s}^{-1})\, \frac{V_t}{10^8\text{cm s}^{-1}}\, \frac{l_t}{10^5\text{cm}}\, \left(\frac{\text{Re}_c}{5000}\right)^{-1} $$
  其中 $l_t, V_t$ 为湍流元尺度与速度，$\text{Re}_c$ 为临界 Reynolds 数。
- 相应黏滞时标：
  $$ \tau_{\rm vis} \approx 500\ \text{s}\, \left(\frac{R}{10^6\text{cm}}\right)^2 \left(\frac{\nu_{\rm turb}}{2\times10^9\ \text{cm}^2\text{s}^{-1}}\right)^{-1} $$

## [FACT] 稳定情形与次星最小质量爆炸
- 稳定情形（$\zeta_2 > \zeta_L$，大初始质量比），转移率趋近：
  $$ \dot{M}_2 \approx -\frac{2 M_2}{(\zeta_2-\zeta_L)\tau_{\rm gr}} $$
- 该吸积率极大，重新提出**角动量处置**与主星**能否容纳如此大质量流入**的问题。
- 另一种可能：中子星存在**最小质量下限**（低于它即不稳定于自由膨胀）；次星可被剥离到最小质量后爆炸¹⁶⁻¹⁸。

## [CRITIQUE] 本节局限
- 角动量输运机制（湍流 vs. 粘滞）高度不确定，直接影响演化时标。
- 三维数值模拟（Benz 等）仍局限在白矮星情形，外推至 NS 情形需谨慎。
