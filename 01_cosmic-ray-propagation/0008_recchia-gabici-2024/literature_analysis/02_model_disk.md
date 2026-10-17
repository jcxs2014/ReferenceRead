# 2. Model of cosmic-ray propagation in the disk

> 本章属于：[Origin of the spectral features observed in the cosmic-ray spectrum](https://doi.org/10.1051/0004-6361/202349005)
>
> 上一章：`01_introduction.md`
>
> 下一章：`03_results.md`

---

## 2.1 Propagation setup

> **传播设置**

**[FACT]** CR 在 ISM 中的扩散传播由与湍流银河磁场的相互作用决定。CR 随机运动被认为是由于对等离子体波的散射，最显著的是磁流体动力学（MHD）不可压缩阿尔芬波和压缩（快、慢）磁声波涨落，在共振尺度 $\lambda \sim r_L$ 处。

**[FACT]** MHD 湍流在星际空间中普遍存在，由天体物理源在 $\approx 10$-100 pc 尺度上产生。为了能有效散射 CR，这种湍流必须级联到共振尺度（亚 PV 粒子的 $\ll$pc），而不被阻尼或变得对散射无效。

**[FACT]** 各种研究表明，与阿尔芬湍流相关的散射由于级联的各向异性而受到高度抑制，而磁声波模式可以在 CR 扩散中起主导作用。

**[FACT]** 或者，CR 也可以产生等离子体波，例如通过在共振尺度激发阿尔芬波，尽管这种效应可能在几百 GeV 以上无效。

**[FACT]** 同时，湍流还受到各种阻尼过程的影响，如部分电离介质中的离子-中性阻尼和非线性朗道阻尼。这些效应在 GD 中通常非常重要，而在 GH 中影响较小（那里离子-中性阻尼不起作用）。

---

### 2.1.1 Transport equation

> **输运方程**

**[FACT]** 考虑 CR 的相空间密度 $f_\alpha(z, p)$ 作为粒子动量 $p$ 和位置 $z$ 的函数，其中 $\alpha$ 为质量数 $A_\alpha$、原子序数 $Z_\alpha$ 的核。由于每个核子的动能 $E_k$ 在散裂过程中大致守恒，我们用粒子通量 $I_\alpha(z, E_k) = A_\alpha c p^2 f_\alpha(z, p)$ 表达输运方程：

$$-\frac{\partial}{\partial z}\left[D_\alpha \frac{\partial I_\alpha}{\partial z} - u I_\alpha\right] - \frac{du}{dz} \frac{I_\alpha}{3} \frac{\partial \ln(I_\alpha p)}{\partial \ln p} = -\frac{I_\alpha}{\tau_r} - 2 h_d n_d v(E_k) \sigma_\alpha(E_k) \delta(z) I_\alpha + c A p^2 q_{0\alpha} \delta(z) + \sum_{\beta>\alpha} 2 h_d n_d v(E_k) \sigma_{\beta\alpha}(E_k) \delta(z) I_\beta(E_k, z)$$

**[FACT]** 左边第一项描述扩散-平流输运，第二项代表绝热损失。右边第一项描述放射性衰变（对 $^{10}$Be 相关），第二项描述核 $\alpha$ 散裂为更轻的核，第三项描述来自 SNR 和其他天体物理源的注入，第四项描述更重的核 $\beta$ 散裂对核 $\alpha$ 的贡献。

**[FACT]** 为简化输运方程的求解，假设粒子注入和核的散裂或产生发生在非常薄的气体盘中（氢密度 $n_d = 1$ cm$^{-3}$，半高 $h_d = 150$ pc，半径 $R_d = 15$ kpc），因此输运方程中的相应项可以近似为 delta 函数 $\propto \delta(z)$。

**[FACT]** 在方程 (17) 中忽略电离损失，因为它们只在 $R \lesssim$ 几 GV 相关（Evoli et al. 2019），其中观测谱受太阳调制影响很大。

---

### 2.1.2 Injection spectrum

> **注入谱**

**[FACT]** 来自给定类别 $i$ 的天体物理源的核 $\alpha$ 的注入谱 $q^i_{0\alpha}$ 建模为幂律（在刚性-动量中）加上在给定刚性 $R_{\max,i}$ 处的截断：

$$q^i_{0\alpha} = \frac{\epsilon_\alpha L_i}{\pi R_d^2} \frac{G(\gamma)}{c (m_p c)^4} \left(\frac{p}{m_p c}\right)^{-\gamma} e^{-R/R_{\max,i}}$$

其中 $\epsilon_\alpha L_i$ 是分配给类型 $\alpha$ 的 CR 核的平均源光度分数，$G(\gamma)$ 是归一化因子。

**[FACT]** $\epsilon_\alpha$ 通过在参考刚性（如 $R = 50$ GV）处拟合给定核的 AMS02 通量来确定。

**[FACT]** 遵循第 1 节的讨论，假设大部分 CR 在典型 SNR 中加速，到典型截断刚性 $R_{\max}^{\rm bulk} = 50$ TV，选择这个值是为了再现 DAMPE 数据中 multi-TV 范围的谱变陡。

**[FACT]** 然后假设只有一类源的子类能将粒子加速到 PeV 能量。这个群体注入的 CR 谱为：

$$q^{\rm PeV}_{0\alpha} = \epsilon^{\rm PeV}_{\rm bulk} \left[\frac{\epsilon_\alpha E_{\rm SN} R_{\rm SN}}{\pi R_d^2} \frac{G(\gamma)}{c (m_p c)^4} \left(\frac{p}{m_p c}\right)^{-\gamma}\right] e^{-R/R_{\max}^{\rm PeV}}$$

其中 $R_{\max}^{\rm PeV} = 5$ PV，$\epsilon^{\rm PeV}_{\rm bulk} \approx 0.15$ 是典型 SNR 总能量输入的归一化因子。

**[FACT]** 总注入谱为：

$$q_{0\alpha} = q^{\rm bulk}_{0\alpha} + q^{\rm PeV}_{0\alpha}$$

---

### 2.1.3 Spallation and production cross section

> **散裂与产生截面**

**[FACT]** 假设 CR 核与 ISM 介质相互作用，ISM 主要由氢（H）和氦（He）组成（$f_{\rm He} \approx 10\%$）。

**[FACT]** 对于比 He 重的 CR 核，总散裂截面 $\sigma_\alpha(E_k) = \sigma_\alpha^{\rm H} + f_{\rm He} \sigma_\alpha^{\rm He}$ 采用 Tripathi et al. (1999) 的参数化。对于 He 核，采用 Coste et al. (2012) 的截面。

**[FACT]** 对于产生截面 $\sigma_{\beta\alpha}(E_k) = \sigma_{\beta\alpha}^{\rm H} + f_{\rm He} \sigma_{\beta\alpha}^{\rm He}$，通常采用 GALPROP 代码提供的 OPT22 参数化。对于 $^4$He $\to ^3$He 通道，使用 Coste et al. (2012) 的截面。对于 CNO 核产生 Li、Be、B，采用 Evoli et al. (2019) 的结果。

**[CRITIQUE]** 需要指出的是，给定核由更重核散裂产生的能量依赖性受到相当大的不确定性影响，通常在 $\sim 20\%$ 左右，但通常更大。这些不确定性涉及给定产生截面的数据质量和数量，以及评估所有可能产生通道（包括幽灵核）贡献的困难。

---

### 2.1.4 Antiprotons

> **反质子**

**[FACT]** 次级 $\bar{p}$ 在 CR 质子和 He 与 ISM（H 和 He 靶）相互作用中的产生按照 Korsmeier et al. (2018) 处理。方程 (17) 的最后一项可以重写为：

$$2 h_d n_d v(E_k) \delta(z) Q_{\bar{p}}(E_k)$$

其中 $Q_{\bar{p}}(E_k)$ 是 $\bar{p}$ 源项：

$$Q_{\bar{p}}(E_k) = \sum_{i=p,{\rm He}} \sum_{j={\rm H},{\rm He}} \int_{E_{\rm th}}^\infty dE_k^i f_j I_i(E_k^i) \frac{d\sigma_{ij}}{dE_k}(E_k^i, E_k)$$

**[FACT]** 对于方程 (17) 中的 $\sigma_\alpha(E_k)$，使用 $\bar{p}$-$p$ 相互作用的总非弹性截面，可以计算为 Workman et al. (2022) 提供的总截面和弹性截面之差。

---

### 2.1.5 Diffusion and advection

> **扩散与平流**

**[FACT]** 定义 GD（下标 $h$）和 GH（下标 $H$）中的扩散系数和平流速度：

$$D = \begin{cases} D_h & \text{if } 0 < z \leq h \\ D_H & \text{if } h < z \leq h + H \end{cases}$$

$$u = \begin{cases} 0 & \text{if } 0 < z \leq h \\ u & \text{if } h < z \leq h + H \end{cases}$$

**[FACT]** GD 假设半高 $h = h_d = 150$ pc，粒子输运为刚性无关的，扩散系数 $D_h = D_{\rm eff,\perp}^{\rm collisionless}$（方程 13 中定义）。

**[FACT]** GH 假设半高 $H = 4$ kpc，银河风速度 $u = 40$ km/s，粒子（刚性依赖）扩散系数为：

$$D_H(R) = D_0 \left(\frac{R}{\rm GV}\right)^\delta$$

其中 $D_0 = 10^{28}$ cm$^2$/s，$\delta = 0.7$。

**[FACT]** 在距离 $z = H + h \equiv H^*$ 之外，CR 假设自由逃逸：

$$I_\alpha(H^*, E_k) = 0$$

---

### 2.1.6 Analytic solution for stable nuclei

> **稳定核的解析解**

**[FACT]** 在附录 B 和 C 中，我们推导了方程 (17) 在盘中的解析解 $I_\alpha^0(E_k)$，针对稳定和不稳定核，条件如方程 (24, 25, 27) 所指定，忽略绝热损失（见附录 A 的讨论）。

**[FACT]** 这里报告稳定核的解并讨论其主要特征：

$$I_\alpha^0(E_k) = \frac{\tau_\alpha^{hH}}{1 + \frac{n_d}{h_d} \frac{h}{v(E_k) \sigma_\alpha \tau_\alpha^{hH}}} \times \left[\frac{1}{2h} Q_{\alpha,\rm src} + \frac{n_d}{h_d} \frac{h}{v(E_k)} Q_{\alpha,\rm spall}\right]$$

其中：

$$Q_{\alpha,\rm src} \equiv c A p^2 q_{0\alpha}, \quad Q_{\alpha,\rm spall} \equiv \sum_{\beta>\alpha} v(E_k) \sigma_{\beta\alpha}(E_k) I_\beta(E_k)$$

分别是来自源的注入和来自更重核散裂的注入（每个 ISM 原子）。

**[FACT]** $\tau_\alpha^{hH}$ 可以解释为 GD 中的停留时间，由 GD 本身的扩散和 GH 中散射诱导的反复穿越组成：

$$\tau_\alpha^{hH} \equiv \frac{h^2}{D_h} + \frac{h}{H} \frac{D_H}{1 - \exp\left(-\frac{u H}{D_H}\right)} \frac{u H}{D_H}$$

**[FACT]** 定义 grammage：

$$X_\alpha(E_k) = \left(\frac{n_d}{h_d} h\right) \mu v(E_k) \tau_\alpha^{hH}$$

和临界 grammage $X_\alpha^{\rm cr} \equiv \mu/\sigma_\alpha$，其中 $\mu = 1.4 m_p$ 是 ISM 气体的平均质量。

**[FACT]** 用 grammage 表示，方程 (28) 可以重写为：

$$I_\alpha^0(E_k) = \frac{1}{1 + \frac{X_\alpha(E_k)}{X_\alpha^{\rm cr}}} \times \left[\frac{\tau_\alpha^{hH}}{2h} Q_{\alpha,\rm src} + \frac{X_\alpha(E_k)}{\mu v(E_k)} Q_{\alpha,\rm spall}\right]$$

**[FACT]** 解可以如下理解。考虑纯初级 CR 质子（$\sigma_\alpha = 0$）的情况，通量变为：

$$I_\alpha^0(E_k) = \frac{Q_{\alpha,\rm src}}{2} \left[\frac{h}{D_h} + \frac{H}{D_H} \frac{1 - \exp\left(-\frac{u H}{D_H}\right)}{\frac{u H}{D_H}}\right]$$

**[FACT]** 考虑到 $D_H \propto R^\delta$ 随刚性增加，而 $D_h$ 假设为常数，GD 中的停留时间（方程 30）预计在高刚性时由 GD 中的扩散主导，使得 $h/D_h > H/D_H$（即在过渡刚性 $R^*$ 以上）：

$$R^* = \left[80 \left(\frac{H}{4~{\rm kpc}}\right) \left(\frac{h}{150~{\rm pc}}\right) \left(\frac{D_m}{1~{\rm pc}}\right) \frac{10^{28}~{\rm cm}^2/{\rm s}}{D_0}\right]^{1/\delta}~{\rm GV}$$

**[FACT]** 取方程 (34) 中的参考值，过渡预期在：
- $\approx 6$ TV（$\delta = 0.5$）
- $\approx 2$ TV（$\delta = 0.6$）
- $\approx 500$ GV（$\delta = 0.7$）
- $\approx 200$ GV（$\delta = 0.8$）

**[FACT]** 因此，如果 GH 中扩散系数的斜率 $\delta \gtrsim 0.6$（Evoli et al. 2019），在 $R \gtrsim 100$ GV $-$ TV 时，传播对 CR 盘中分布的影响 smoothly 变得与刚性无关。相应地，grammage 将趋于方程 (15) 中报告的常最小值：

$$X_\alpha(R \gg R^*) \to \frac{n_d \mu c h^2}{D_h} = X_{\min}$$

**[FACT]** 在 $R \sim R^*$ 以下，GD 中的停留时间由 GH 中扩散诱导的反复穿越主导，通常平流在 $R \lesssim 10$ GV 时主导。平流（$uH \gg D_H$）和扩散（$uH \ll D_H$）极限情况为：

$$I_\alpha^0 \to \begin{cases} \frac{Q_{\alpha,\rm src}}{2u} & \text{advection limit} \\ \frac{Q_{\alpha,\rm src} H}{2 D_H} & \text{diffusion limit} \end{cases}$$

**[FACT]** 最后，需要注意的是，GH 中的扩散方程只在刚性 $R_H^{\rm mfp}$ 以下有效，使得扩散平均自由程小于扩散晕的大小，即 $\lambda_{\rm mfp} \lesssim H$，其中：

$$\lambda_{\rm mfp} \equiv \frac{3 D_H(R)}{c} \approx 0.3 \left(\frac{D_0}{10^{28}~{\rm cm}^2/{\rm s}}\right) \left(\frac{R}{\rm GV}\right)^\delta~{\rm pc}$$

这给出：

$$R_H^{\rm mfp} = \left[12 \times 10^3 \left(\frac{H}{4~{\rm kpc}}\right) \frac{10^{28}~{\rm cm}^2/{\rm s}}{D_0}\right]^{1/\delta}~{\rm GV}$$

对于 $\delta = 0.5$-0.8，$R_H^{\rm mfp}$ 的值为：
- $\approx 150$ PV（$\delta = 0.5$）
- $\approx 6$ PV（$\delta = 0.6$）
- $\approx 700$ TV（$\delta = 0.7$）
- $\approx 100$ TV（$\delta = 0.8$）

**[FACT]** 因此，在高刚性时，GH 中的粒子并不真正扩散，而是自由逃逸。我们通过对方程 (28) 取 $H \to 0$ 极限来处理这种情况，这对应于将自由逃逸边界 $H^* \to h$。

---

## 2.2 Results

> **结果**

**[FACT]** 本节描述计算的主要结果。CR 通量使用方程 (28) 评估，设置如第 3 节所述。

**[FACT]** 对于方程 (21) 的注入谱，假设质子斜率 $\gamma_p = 4.35$，氦 $\gamma_{\rm He} = 4.3$，所有其他核 $\gamma_n = 4.33$。

**[FACT]** 太阳调制效应通过力场近似（Gleeson & Axford 1968）考虑，调制势 $\Phi_{\rm mod} = 450$ MV。

**[FACT]** 计算中采用的相关物理参数总结在表 1 中。

**[FACT]** 由于本文的主要目的是在大量 CR 数据上展示所提场景的合理性，没有尝试对数据进行精确拟合，这留待未来工作。这里寻求的是与数据的定性良好一致。

**[FACT]** 参数不应被视为最佳拟合值，而是基准设置。

**[FACT]** 虽然在 $R \gtrsim 10$ GV 时通常获得与数据的良好一致（在上述意义上），在低刚性域中一致倾向于较差，尽管在大多数情况下相当可观。

**[FACT]** 低刚性时 CR 通量的适当估计应考虑电离损失，以及更精细的平流建模（包含绝热损失）。此外，为了保持自由参数数量有限，所有核的太阳调制谱使用相同的 $\Phi_{\rm mod}$ 计算。然而，不同数据集是在不同收集的，因此对不同数据集使用略微不同的调制势值也可能影响低刚性时与数据的一致。

---

### 2.2.1 Protons, helium, and antiprotons

> **质子、氦和反质子**

**[FACT]** 图 4 显示了 1-$10^5$ GV 范围内质子和 He 通量（主要由 $^4$He 加上少量次级 $^3$He 组成）以及相应的 p/He 比。

**[FACT]** 在 $R \lesssim 10$ GV 时，（未调制的）解由平流主导，如图 5 中 grammage 的平坦化所示。这导致低 $R$ 时 CR 通量的硬化。

**[FACT]** 在 $R \approx 10$-几百 GV 范围内，CR 通量主要受 GH 中陡的刚性依赖扩散 $D_H \propto R^{0.7}$ 影响，这反映在 grammage 的幂律下降中。

**[FACT]** 在几百 GV 以上，grammage 平滑地开始变浅，如第 3.6 节所述，导致 CR 谱的 gentle 渐进硬化，与数据良好一致。这种谱的平滑变浅是方程 (30) 中 $h/D_h$ 项变得与 $H/D_H$ 相当然后更大的结果，这种转变发生在 $\approx 1$-2 个 $R$ 的十年内，围绕 $\approx 1$ TV。

**[FACT]** 图 5 中 grammage 的斜率在 $\approx 400$ GV 处为 $\sim 0.33$，在 $\approx 1$ TV 处为 $\sim 0.3$。这至少定性地解释了为什么在几 TV 以下使用斜率 $\approx 4.3$ 的注入谱与数据找到良好一致。

**[FACT]** DAMPE 报告的 $\approx 15$ TV 处的谱变陡是大多数 SNR 以典型截断刚性 $R_{\max}^{\rm bulk} \approx 50$ TV 加速粒子的结果。这种变陡也可以在 CREAM 和 CALET 数据的 p 谱中识别，而在 He 情况下情况不太清楚，特别是由于三个实验报告的谱之间存在相当大的差异。

**[FACT]** 在 1-$10^5$ GV 整个范围内，我们获得与 AMS02 和 DAMPE 数据的非常良好一致，特别是在 $R \gtrsim 10$ GV 时，太阳调制不重要。我们对 p/He 比的预测在 $R \lesssim 1$ TV 时与 AMS02 数据紧密匹配，在更高 $R$ 时与 NUCLEON 数据匹配。

**[FACT]** 图 6 显示了图 4 中的质子和 He 通量作为总能量 $E_{\rm TOT}$ 的函数，范围为 $10^3$-$10^8$ GeV。红曲线对应于第 3 节中描述的两类源的预期贡献（即 $R_{\max}^{\rm bulk} = 50$ TV 的典型 SNR 和 $R_{\max}^{\rm PeV} = 5$ PV 的 PeV 源）。

**[FACT]** 作为比较，还显示了蓝曲线，对应于 $\ln(R_{\max})$ 在 $\ln(R_{\max}^{\rm bulk})$-$\ln(R_{\max}^{\rm PeV})$ 范围内的均匀分布，CR 光度随 $\ln(R_{\max})$ 线性递减。

**[FACT]** 考虑到 multi-PeV 域中不同数据集之间的相当大系统学，可以看到我们的模型能够很好地再现数据，从 $R \gtrsim 10$ GV 到 multi-PeV 域。

**[FACT]** 这个结果是 $\approx 10$ TV 以上 CR 经历的刚性无关传播（见图 5）与能够达到非常高能量的源的较小 CR 光度与大多数源相比的组合，尽管当前数据不允许明确区分双群体场景和 $R_{\max}$ 分布与 CR 光度递减的情况。

**[FACT]** 如果假设大部分 SNR 将粒子加速到 knee，具有刚性无关的传播，在这样的高能量下我们会得到非常硬的 CR 谱，会 largely 超过数据。为了解释 DAMPE 数据中的变陡而不影响低能量下的 CR 通量，我们将被迫在 $R \approx 20$ TV 处引入传播机制的变化，除了解释 $R \approx 300$ GV 处硬化所需的变化之外。

**[FACT]** 在图 2 中，我们显示了我们对 $\bar{p}$ 通量和 $\bar{p}/p$ 比的预测与 AMS02 数据的比较。为了突出 $\bar{p}$ 产生截面中的典型不确定性（Korsmeier et al. 2018），我们在预测通量周围放置了 10%（黄色）和 20%（绿色）的带。对于这两个量，我们获得与数据的 excellent 一致。

**[FACT]** 这个结果可以解释如下。首先，在 p-p 碰撞中产生的反质子（来自 p-He、He-p 和 He-He 通道的不可忽略贡献）具有宽能量分布。这种过程涉及的运动学显著重塑了 $\bar{p}$ 产生谱 $Q_{\bar{p}}$，使其比父 p（和 He）通量 appreciably 更硬。其次，反质子像质子一样在 ISM 中传播（除了 $\bar{p}$ 散裂的作用），因此我们期望反质子平衡谱的斜率 $\gamma_{\bar{p}} \approx \gamma_{Q_{\bar{p}}} + \gamma_X$。硬的 $Q_{\bar{p}}$ 和 grammage $X$ 的渐进变浅的组合使得 $|\gamma_{\bar{p}} - \gamma_p| \lesssim 0.15$ 在 $R = 30$-1000 GV 范围内，这转化为 $\bar{p}/p$ 比在该刚性范围内的非常温和的下降。

---

### 2.2.2 LiBeB and CNO nuclei

> **LiBeB 和 CNO 核**

**[FACT]** 图 7 左面板显示了 C、N 和 O 通量。O（主要是 $^{16}$O、$^{17}$O、$^{18}$O）和 C（主要是 $^{12}$C、$^{13}$C）主要是初级的，在低刚性时有少量（分别为百分之几和 $\lesssim 20\%$）来自更重核的次级贡献。大部分次级 C 来自 O 的散裂。对于这两个核，我们很好地再现了 AMS02 数据。

**[FACT]** 此外，向平坦 grammage 的渐进转变（如上所述）在 $\sim$TV 刚性以上产生相当硬的谱，与 CREAM 和 NUCLEON 实验一致。然而，我们注意到高 $R$ 时数据集之间的 sizable 差异。C/O 比也与 AMS02 数据良好一致，如图 1 所示。

**[FACT]** 氮（$^{14}$N、$^{15}$N）部分是初级的，部分是次级的（主要来自 O 的散裂）。在这种情况下，我们也获得与 AMS02 数据的良好一致，特别是我们再现了谱的高 $R$ 硬化。

**[FACT]** 图 7 右面板显示了 Li（$^6$Li、$^7$Li）、Be（$^7$Be、$^9$Be、$^{10}$Be）和 B（$^{10}$B、$^{11}$B）通量。采用第 3 节中指定的产生截面，黄色和绿色带分别代表 10% 和 20% 的产生截面不确定性。主要产生通道（在 $E_k \gtrsim 10$ GeV/n 时 $\gtrsim 80\%$）来自 CNO 核的散裂。

**[FACT]** 采用采用的截面，我们得到的 Li、Be 和 B 通量形状与 AMS02 数据良好一致；特别是，我们很好地再现了 $\approx$TV 周围的渐进变浅。然而，我们的 Li 和 Be 通量 systematically 高于数据，B 通量 systematically 低于数据。

**[FACT]** 考虑到产生截面的大不确定性，我们还显示了 Li 通量乘以 $f_{\rm Li} = 0.92$、Be 通量乘以 $f_{\rm Be} = 0.9$、B 通量乘以 $f_{\rm B} = 1.1$ 的情况，这与 AMS02 数据良好匹配。

**[FACT]** 通过这样的重新归一化，我们还发现 B/C 和 B/O 比（图 1）以及 Be/C、Be/O 和 Be/B 比（图 8）与 AMS02 数据非常一致。我们特别注意到 B/C 的高 $R$ 变浅与 grammage 变浅相关。

**[FACT]** 然而，在 B 的情况下，应该考虑到一个 caveat。确实，$^{10}$B 从 $^{10}$Be 的衰变中接收贡献，与散裂贡献相反，它不集中在盘中，而是空间 extended 的。另一方面，这种贡献对 B 通量的相关性可以通过比较 Evoli et al. (2020) 图 4 中的点线（对应于假设稳定 $^{10}$Be 的情况）和 Be/B 数据来估计。该图显示这种效应预计在 $\sim 10$ GV 处达到最大，在 100 GV 以上变得完全无关。

**[FACT]** $^{10}$Be 是长寿命不稳定同位素（半衰期 1.39 Myr），在确定银河系中 CR 停留时间方面非常重要。在附录 C 中，我们推导了不稳定核的输运方程解，采用与稳定核相同的 GD-GH 设置。

**[FACT]** $^{10}$Be 在估计晕大小中的重要性可以从单晕的极限情况理解，如附录 C 中推导的。在这种极限下，不稳定同位素的通量缩放为：

$$I_\alpha^0 \propto \begin{cases} \frac{H}{D} & \text{for } \tau_{\rm diff} \ll \tau_r \\ \frac{\tau_r}{\sqrt{D \tau_r}} & \text{for } \tau_{\rm diff} \gg \tau_r \end{cases}$$

其中 $\tau_{\rm diff} = H^2/D$ 是扩散时间尺度，$\tau_r$ 是衰变时间尺度。

**[FACT]** 我们注意到前一种极限对应于稳定同位素的情况，在足够高的能量下达到，因为衰变时间随总能量增加，$\tau_r \propto E$。因此，稳定同位素的通量对比率 $H/D$ 敏感，而不是对两个量分别敏感。相反，测量不稳定同位素或同一核的稳定与不稳定同位素的比率提供了额外信息，允许确定 $H$ 的值。

**[FACT]** $^{10}$Be 与稳定同位素 $^9$Be 的比率趋于：

$$\frac{^{10}{\rm Be}}{^9{\rm Be}} \propto \begin{cases} \text{const} & \text{for } \tau_{\rm diff} \ll \tau_r \\ \frac{\sqrt{D \tau_r}}{H} & \text{for } \tau_{\rm diff} \gg \tau_r \end{cases}$$

**[FACT]** 在图 8 中，我们显示了我们对 $^{10}$Be/$^9$Be 的预测，使用表 1 中的基准参数，特别是 $H = 4$ kpc（红曲线），与最近的 AMS02 初步数据和来自各种其他实验的数据（Maurin et al. 2023）比较。我们还考虑了产生截面中的大不确定性，并显示了当每个同位素的截面分别增加或减少 10%（黄色）、20%（绿色）和 30%（粉色）时比率的变化。

**[FACT]** 鉴于低 $E_k$ 处数据的大 spread，我们的基准结果与这些数据 compatible，但 substantially 大于 AMS02 数据。虽然截面不确定性可以缓解这种不匹配，但通过将晕大小增加到 $H = 6$-8 kpc 可以实现与 AMS02 数据的更好一致，如青色和紫色曲线所示。

**[FACT]** 应该指出的是，考虑到与我们处理低刚性 CR 和忽略 $^{10}$Be 到 $^{10}$B 的空间 extended 衰变相关的 caveats，晕大小的估计不应被视为最佳拟合，而应被视为所提场景中的合理范围。

**[FACT]** 所有其他通量不会受到 $H \to x H$ 重新缩放的影响，前提是（保持 $h$ 和 $D_H$ 固定）：

$$n_d \to n_d/x, \quad D_h \to D_h/x, \quad u \to u/x$$

---

### 2.2.3 Heavy nuclei

> **重核**

**[FACT]** 在图 9 中，我们显示了 Ne、Mg、Si 和 Fe 通量的结果。对于 Fe，我们只考虑同位素 $^{56}$Fe 并视为纯初级。

**[FACT]** 通常，始终牢记数据集之间的差异，我们获得与 AMS02 和 NUCLEON 数据的非常良好一致，Fe 的情况除外，其中 NUCLEON 数据 systematically 远低于 AMS02 数据。

**[FACT]** 这些核的次级贡献（图中的蓝曲线）可能被 somewhat 低估，考虑到从 $^{56}$Fe 开始的许多碎裂通道和每个通道可能的（未知）系统学。例如，在 Si 和 Mg 的情况下，通过将次级通量分别乘以 1.2 和 2 可以获得与数据的更好一致（绿色虚线）。

**[FACT]** 在图 10 中，我们显示了 F、Na、Al 和 S 通量与 AMS02 数据的比较。考虑到产生截面的不确定性，特别是对于主要是次级的 F，我们很好地再现了数据。

**[FACT]** 作为我们方法和所考虑的产生通道的一致性检查，在图 B.1 和图 B.2 中，我们显示了 Ar、Ca、Cl、Cr、K、Mn、P、Sc、Ti 和 V 通量的预测。对于这些核，数据主要在 $E_k \lesssim 50$ GeV/n 时可用，而更高能量数据（如果存在）显示大不确定性（Maurin et al. 2023）。
