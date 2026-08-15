---
# 98. Vocabulary — 学术词汇与术语

## A. 学术逻辑词（本篇原文出现）

| 单词 | 词性 | 逻辑功能 | 中文 | 原文例句 | 逻辑说明 |
|------|------|----------|------|----------|----------|
| however | adv. | 转折 | 然而 | "However, cosmic ray physicists have found it more difficult to identify specific acceleration mechanisms." | 承认加速事实已知，转折指出机制未知 |
| consequently | adv. | 因果(结果) | 因此 | "acceleration in strong shocks is consequently an attractive possibility" | 幂律谱的普适性 → 需要普适机制 |
| thus | adv. | 因果(结论) | 因此 | "Thus if, on average, the fractional energy increase ... were $\epsilon$ ~ $10^{-1}$..." | 由能量密度和体积推出可行性 |
| nevertheless | adv. | 让步(然而) | 尽管如此 | "Nevertheless, we can demonstrate that SNRs are energetically capable..." | 承认谱指数偏差，但能量可行性仍成立 |
| whereas | conj. | 对比 | 而 | "quite unlike the situation in the Galaxy, whereas in extragalactic..." | 对比银河系和河外射电源 |
| thereby | adv. | 因果(由此) | 从而 | "...scattered by Alfvén waves ... thereby accelerated by the first-order Fermi process" | 散射 → 加速 的因果链 |
| hence | adv. | 因果(因此) | 因此 | "a general mechanism is at work, and ... hence acceleration in strong shocks" | 普适谱 → 激波加速为候选 |
| although | conj. | 让步 | 尽管 | "although most particles will be accelerated when the shock starts to become Alfvénic..." | 承认效率降低，但给出修正 |
| consequently | adv. | 因果 | 因此 | "the energy input rate is ... consequently giving an acceleration time of $10^{6}$ years" | 能量注入率 → 加速时间 |
| if | conj. | 条件 | 如果 | "if, on average, the fractional energy increase ... were $\epsilon$ ~ $10^{-1}$" | 设定假设推出结论 |
| so that | conj. | 结果 | 使得 | "so that they can be accelerated by the Fermi (1949) method" | 散射条件 → 可加速 |
| where | adv. | 定义/限定 | 其中 | "where K = D∥ cos²$\theta$" | 定义参数 K |
| which | pron. | 关系从句 | 即/它 | "which is more than sufficient to account for the known energy input requirements" | 指代能量注入量，评价其充分性 |
| for | prep. | 举例 | 例如 | "e.g., Wentzel 1964; Hudson 1965..." | 列举历史文献 |
| in this view | adv. | 框架引入 | 在这种观点下 | "in this view, high energy particles are a natural by-product" | 引入理论框架 |

**逻辑功能分类覆盖**：
- 转折：however
- 因果：consequently, thus, thereby, hence, so that
- 让步：although, nevertheless
- 对比：whereas
- 条件：if
- 举例：e.g., for instance
- 结论：thus, consequently

## B. 领域术语（本篇特有）

| 术语 | 中文 | 释义 | 首次出现章节 |
|------|------|------|-------------|
| Alfvén wave | Alfvén 波 | 磁流体中沿磁力线传播的横波，波速 $v_A = B/\sqrt{4\pi\rho}$；本文假设其散射粒子使其各向同性化 | §II |
| diffusive shock acceleration (DSA) | 扩散激波加速 | 粒子在激波面附近被 Alfvén 波散射反复穿越激波，获得能量；本文核心机制 | §II |
| first-order Fermi acceleration | 一阶 Fermi 加速 | 平均能量增益正比于 $u/c$（一阶量），区别于二阶 Fermi（$\propto (u/c)^2$）；本文提出的高效机制 | Abstract |
| second-order Fermi acceleration | 二阶 Fermi 加速 | 粒子在随机运动的散射中心间反射，平均能量增益 $\propto (u/c)^2$，效率远低于一阶 | §I |
| compression ratio | 压缩比 | $r = u_-/u_+ = \rho_+/\rho_-$；决定谱指数 $q = 3r/(r-1)$ 的唯一参数 | §II |
| pitch angle scattering | 方位角散射 | Alfvén 波使粒子绕磁力线的回旋方位角 $\phi$ 随机散射，导致扩散 | §II |
| diffusion coefficient | 扩散系数 | $D_\parallel = (v^2/4)\int \sin^3\phi \, d\phi / \nu$；粒子在激波附近的空间扩散速率 | §II |
| Larmor radius | Larmor 半径 | $r_L = pc/(ZeB)$；粒子在磁场中的回旋半径，决定粒子是否能被约束 | §II |
| adiabatic decompression | 绝热膨胀损失 | SNR 膨胀时粒子能量 $\propto 1/R$ 衰减；DSA 规避此问题的关键优势 | §III |
| streaming instability | streaming 不稳定性 | CR 以超 Alfvén 速度 streaming 时激发 Alfvén 波（Kulsrud & Pearce 1969）；自激发机制 | §III |
| power-law spectrum | 幂律谱 | 动量分布 $f(p) \propto p^{-q}$；观测显示 $4 < s < 5$；DSA 自然给出 | Abstract/§II |
| Alfvén speed | Alfvén 速度 | $v_A = B/\sqrt{4\pi\rho} \approx 50$ km/s（ISM 典型值）；CR 运动受限于此速度 | §I |
| equipartition | 等分 | 电子和质子能量密度接近相等；解释观测到的 $e^-/p^+ \sim 0.03$ | §III |
| synchrotron cooling | 同步辐射冷却 | 相对论电子在磁场中辐射损失能量的过程，冷却时间 $\propto 1/(\gamma B^2)$ | §IV |
| hot spot | 热点 | 射电星系中电子被持续加速的区域（如 Cygnus A）| §IV |
| Sedov solution | Sedov 解 | 超新星遗迹膨胀的自相似解，给出 $u_{\rm cool} \approx 120$ km/s | §I |
| remnant | SNR | 超新星遗迹 | §I |
| remnant age | SNR 年龄 | SNR 从爆发到冷却的时间，$\sim 10^{5.9}$ yr | §I |
| bow wave | 弓波 | 星系在星系团介质中运动或射电源束在星际介质中传播时产生的冲击波 | §IV |
| in situ acceleration | 原位加速 | 粒子在源内部（而非传输中）被加速；河外射电源中的主要机制 | Abstract/§IV |

## C. 长难句摘录

### C1. §II（推导核心句）

> "In a stationary solution, the flux $uf - \kappa\nabla f$ must be constant on either side of the shock; $f$ will approach asymptotic values $f_-(f_+)$ as the distance from the shock $x \to -\infty (+\infty)$."

**主干**：flux + must + be + constant；$f$ + will approach + values
**修饰**：In a stationary solution（条件状语），on either side of the shock（地点状语），as the distance from the shock $x \to -\infty$（时间状语从句）
**翻译**：在稳态解中，粒子能量通量 $uf - \kappa\nabla f$ 在激波两侧必须分别守恒；分布函数 $f$ 随距离激波 $x \to -\infty(+\infty)$ 而渐近趋于 $f_-(f_+)$。
**物理意义**：这是连接条件的来源——通量守恒要求 $f$ 在激波两侧有特定的渐近行为，由此得到幂律解。

### C2. §I（可行性论证句）

> "Thus if, on average, the fractional energy increase of a cosmic ray on passing through the strong shock were $\varepsilon \sim 10^{-1}$, the total energy input in this form would be $\varepsilon V_{\rm cool} w_{\rm cr} \sim 10^{50}$ ergs SN$^{-1}$, which is more than sufficient to account for the known energy input requirements."

**主干**：if + the energy increase were + $\varepsilon$，the input would be + $\varepsilon V w$；which + is + sufficient
**修饰**：on average（状语），on passing through the strong shock（时间状语），in this form（方式状语），which 引导的非限定关系从句（评价充分性）
**翻译**：因此，如果平均而言宇宙线穿越强激波时的能量增益为 $\varepsilon \sim 10^{-1}$，则以这种形式输入的总能量为 $\varepsilon V_{\rm cool} w_{\rm cr} \sim 10^{50}$ erg/SN，这完全足以满足已知的能量输入需求。
**逻辑功能**：假设条件句 + 因果推导 + 评价从句，完整的可行性论证结构。

### C3. §III（自激发条件句）

> "The condition that the amplitude of the turbulence be adequate to keep the scale length $L$ less than the remnant radius $R$ is simply that the growth time of the waves be small compared with the age of the supernova remnant, $R/u_-$."

**主干**：The condition ... is simply that + the growth time + be + small
**修饰**：that the amplitude ... be adequate（同位语从句），to keep $L$ less than $R$（目的不定式），compared with $R/u_-$（比较状语）
**翻译**：湍流振幅足以使扩散长度 $L$ 小于 SNR 半径 $R$ 的条件，仅仅是波的增时标远小于 SNR 年龄 $R/u_-$。
**物理意义**：这是自激 Alfvén 波可行性的核心判据——如果波增长快于 SNR 膨胀，则湍流能持续存在。