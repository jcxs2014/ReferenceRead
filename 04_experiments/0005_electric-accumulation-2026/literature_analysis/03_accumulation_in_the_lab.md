# 3. 带电压壳层 Accumulator

## 3.1 实验装置

[FACT] 实验装置（图 1）：一个开放球壳（半径 R₀），充电至固定电压 φ₀ < 0（相对于地），类似标准 Van de Graaff generator。这个"累积壳层"（accumulator shell）从周围环境捕获 mCPs，可独立于专用探测器的运行而提前收集粒子。

[FACT] 探测器放置于壳内腔体中，沉浸在更高的局部 mCP 密度 n_trap 中，从而增强对地球 mCP population 的探测灵敏度。

[INTERPRETATION] 关键设计思路：accumulator 本身不测量 mCP，而是先将其富集到一个高密度状态，再交给已有的探测技术来探测。富集过程（collection）和探测过程（detection）可以独立优化。

## 3.2 Accumulator 的核心机制

[FACT] 关键物理：壳层可以屏蔽普通荷电粒子（SM 离子）。在导体表面，核和电子波函数的分离一般产生 ~few eV 量级的电势垒。因此，电荷远大于 ~few × 10⁻²（300 K/eV）的室温粒子无法有效穿透金属屏障。这使得 accumulator 能够有效排除 SM 离子，同时允许 mCPs 扩散进入其内腔。

[INTERPRETATION] 这是一个巧妙的"区分原则"：mCP 与 SM 粒子的电荷比值（qχ/e ≪ 1）直接转化为它们穿透金属屏障能力的巨大差异。Accumulator 正是利用这一点来实现对 mCP 的选择性收集。

[FACT] 对于 Tχ/(e|φ₀|) ≪ qχ ≪ Tχ/eV（其中 Tχ 是 mCP 温度），mCPs 可以扩散进入充电壳层的内腔，通过与腔内物质的散射失去能量，被壳层的电势阱有效捕获。

[INTERPRETATION] 窗口条件 Tχ/(e|φ₀|) ≪ qχ 的含义：mCP 的热能量必须远小于其从壳层电势获得的能量，否则无法被有效捕获。上限 qχ ≪ Tχ/eV 来自另一个物理考量：太高的电荷会导致 mCP 在金属表面被直接反射而非进入腔内。

## 3.3 密度增长动力学

[FACT] 地面 mCPs 以由电加速速度 VE 决定的速率在壳层中积累。在时间 t 内积累的密度为：
$$n_{\\text{trap}} \\simeq 3 \\varepsilon_{\\text{trap}} n_\\chi V_E t / R_0$$

其中 ε_trap ≤ 1 是无量纲效率因子，对于充分碰撞热化的 mCP 供给是 O(1)。

[FACT] 加速速度 VE 与壳层表面电场 E₀ = φ₀/R₀ 的关系（附录 A 推导）：
$$V_E \\simeq \\frac{e q_\\chi E_0 / m_\\chi}{\\max\\left(\\sqrt{\\Gamma^{(\\text{air})}_p / p}, \;v_{\\text{th}} / (2R_0)\\right)}$$

其中 Γ^{(air)}_p 是 mCP-原子碰撞的动量交换率，v_th = √(3Tχ/mχ) 是 mCP 热速度。分母中的"max"：第一项适用于高碰撞情形（碰撞主导），第二项适用于弹道自由流情形。

[INTERPRETATION] VE 公式的两种极端物理：
- 碰撞主导（Γ^{(air)}_p ≫ v_th/R₀）：VE 是 mCP 在电场中加速下落与空气分子碰撞的终端速度
- 弹道自由流（Γ^{(air)}_p ≪ v_th/R₀）：VE ≃ v²_esc/v_th，这是 Sommerfeld 增强的捕获率——长程库仑势的共振效应，远超简单直流加速

## 3.4 效率因子分解

[FACT] 效率因子分解为：ε_trap = ε_room × ε_bound
- ε_room：实验室空间有限尺寸的影响（若 accumulator 放在室内）
- ε_bound：mCPs 散射并被电捕获的能力

[INTERPRETATION] 这一分解凸显了两个独立的物理约束：① mCPs 必须能从周围环境进入壳层（受房间尺寸、通风、墙壁扩散限制）；② 进入后必须能被有效捕获而不逃逸（受碰撞和势阱深度限制）。

## 3.5 A. 室内 vs 室外

[FACT] 为在 ~1 年时间尺度上最大化灵敏度，accumulator 最好放在室外，因为收集的 mCPs 总数最终受限于电场范围所决定的最大封闭空间。

[FACT] 对于室内情形（半径 R_room 的房间，墙壁厚度 ΔR_room，通风口面积 A_vent），mCPs 在时间 t 内被收集的上限为：
$$N_{\\text{trap}} \\lesssim n_\\chi 4\\pi R_{\\text{room}}^2 t \\left[ \\frac{R_{\\text{room}}}{3t} + \\frac{A_{\\text{vent}} V_{\\text{vent}}}{4\\pi R_{\\text{room}}^2} + \\frac{D^{(\\text{wall})}_\\chi}{\\Delta R_{\\text{room}}} + \\frac{V^{(\\text{air})}_g}{4}\\right]$$

其中：D^{(wall)}_χ = Tχ/(mχΓ^{(wall)}_p) 是 mCP 在墙中的扩散系数；V^{(air)}_g = g⊕/Γ^{(air)}_p 是 mCP 在地球重力场中的漂移速度。

[INTERPRETATION] 公式（10）的物理含义：每个 mCP 来源（房间内空气、通风口进入、墙壁扩散、重力沉降）都对总捕获量设置了上限。室内设计的本质是在这些约束之间找到平衡。

## 3.6 B. 电捕获机制

[FACT] 在时间 t 内，被电势 φ₀ 捕获的 mCPs 产生的过量密度由时间积分给出。

[INTERPRETATION] 电捕获的核心是 mCP 在静电势中的动力学：进入捕获区域的 mCP 如果能量低于势垒就会被反射；如果进入后通过碰撞损失能量，就无法克服势垒逃逸，形成准束缚态。

## 3.7 参考文献与图示

[FACT] 图 1 示意：外层大半径 R₀ 的"累积壳层"充电至强负电压 φ₀，吸引正电荷 mCPs（χ⁺），它们在壳内与任何物质散射后失去能量，被电势阱有效捕获，形成密度增强。图中将壳内物质模拟为实心球；真实实验中 mCP 探测器应放在壳内某处。

[FACT] 对于 mA' ≲ R⁻¹_⊙ ~ 10⁻¹⁶ eV 或 mA' ≲ R⁻¹_⊕ ~ 10⁻¹⁴ eV，mCPs 可与太阳风或地球的长程磁场有效耦合，减少其进入地球环境的能力。对于 mA' ≲ h⁻¹_atm ~ 10⁻¹² eV 且 qχ ≫ 10⁻⁷，大气电场的耦合反而可能增强正电荷 mCPs 在大气以下的捕获。

[CRITIQUE] 对长程电磁效应的处理高度依赖于具体模型参数（A' 质量和规范耦合）。本文选择对 mCP DM 的丰度保持模型无关态度，仅用局部地球密度 nχ 作为参数，规避了暗光子质量等不确定因素。
