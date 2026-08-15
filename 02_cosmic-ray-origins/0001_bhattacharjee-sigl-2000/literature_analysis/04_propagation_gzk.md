> 本章属于：Bhattacharjee & Sigl (1999), *Phys. Rep.* 320, 1–150
>
> 上一章：`03_bulk_origin_general.md`
>
> 下一章：`05_neutrinos_exotic_particles.md`
---

# 4. Propagation and Interactions of Ultra-High Energy Radiation (§4, p. 16–40)

[FACT] §4 是全文核心技术章节，跨越 p. 16–40，共 8 个子节（4.1–4.8），涵盖：核子与 GZK 截断（§4.1）、UHE 光子与 EM 级联（§4.2）、UHE 中微子与\"奇特\"粒子（§4.3，含 4.3.1/4.3.2/4.3.3）、EHECR 谱与图像中的磁场印记（§4.4，含 4.4.1/4.4.2）、EHECR 源位置约束（§4.5）、EHECR 事件源搜索（§4.6）、UHECR 传播详细计算（§4.7，含 4.7.1/4.7.2）、异常运动学与量子引力效应（§4.8）。

[INTERPRETATION] §4 逻辑链：**粒子种类 → 传播与相互作用 → 磁场效应 → 观测约束**。作者按粒子分节：带电强子（4.1）→ 光子（4.2）→ 中微子与奇特粒子（4.3）→ 磁场对所有粒子的统一效应（4.4–4.6）→ 传播方程精确化（4.7）→ 超越标准模型的推广（4.8）。

---

## 4.1 Nucleons, Nuclei, and the Greisen-Zatsepin-Kuzmin Cutoff

> **核子、原子核与 Greisen-Zatsepin-Kuzmin 截断**

[FACT] §4.1 首先建立适用于所有粒子种类的河外传播**一般记号与公式**（公式 7–12），随后详述 GZK 效应并列举其他核子损失机制。

[FACT] **相互作用长度 (公式 7)**：
$$
l(E)^{-1} = \int d\epsilon\cdot n_b(\epsilon)\cdot\int_{-1}^{+1}d\mu\cdot\frac{(1-\mu\beta\beta_b)}{2}\cdot\sigma(s)
$$
- $n_b(\epsilon)$：背景粒子单位能量数密度
- $\beta_b = (1-m_b^2/\epsilon^2)^{1/2}$；$\beta = (1-m^2/E^2)^{1/2}$
- $\mu$：入射动量夹角余弦；$\sigma(s)$：总截面

[FACT] **质心能量平方 (公式 8)**：
$$
s = m_b^2 + m^2 + 2\epsilon E(1-\mu\beta\beta_b)
$$

[FACT] **能量衰减长度 (公式 9)**：引入**非弹性度** $\eta(s)$：
$$
\eta(s) \equiv 1 - \frac{1}{\sigma(s)}\int dE'\cdot E'\cdot\frac{d\sigma}{dE'}(E',s)
$$
$E'$ 为\"leading particle\"（携带最多能量的反冲粒子）的归一化能量。

[FACT] **CEL 近似下的\"扩散方程\" (公式 10)**：
$$
\partial_t n(E) = -\partial_E[b(E)\cdot n(E)] + \Phi(E)
$$
- $b(E) = E/l_E(E)$：能量损失率；$\Phi(E)$：本地注入谱
- 适用条件：leading 与 non-leading 粒子性质不同，且 $\eta(s)\ll 1$

[FACT] **河外各向同性源的积分公式 (公式 11, 12)**（物质主导平坦宇宙 $\Omega_0=1$）：
$$
j(E) = \frac{3}{8\pi t_0}\int_0^{z_{i,\max}}dz_i\cdot(1+z_i)^{-11/2}\cdot\frac{dE_i(E,z_i)}{dE}\cdot\Phi(E,z_i)
$$
- $t_0$：宇宙年龄；$E_i(E,z_i)$：注入红移 $z_i$ 处的注入能量，满足 $dE/dt = b(E)$
- 均匀 $\Phi(E)$ 时简化为 (公式 12)：
$$
j(E) \simeq \frac{1}{4\pi}\cdot l_E(E)\cdot\Phi(E)
$$
（前提是 $l_E(E)\ll$ 视界尺寸，可忽略红移演化）

---

[FACT] **GZK 阈值** — Greisen (1966) 与 Zatsepin–Kuzmin (1966) 独立指出：质子在静止系中 CMB 光子能量可超过 **photo-pion 产生**阈值：
$$
E_{\rm lab,thr}^{\gamma} \equiv m_\pi + \frac{m_\pi^2}{2m_N} \simeq 160\ {\rm MeV}
$$
对应质子阈值（对背景光子 $\epsilon$，公式 13）：
$$
E_{\rm th} = \frac{m_\pi(m_N+m_\pi/2)}{\epsilon} \simeq 6.8\times10^{16}\cdot\left(\frac{\epsilon}{{\rm eV}}\right)^{-1}\ {\rm eV}
$$
- CMB 典型 $\epsilon\sim 10^{-3}$ eV → **GZK cutoff** 出现在数十 EeV（~$5\times10^{19}$ eV）处，质子相互作用长度降至 **~6 Mpc**。

[FACT] **截面特征 (Fig. 8)**：
- 阈值附近：显著的 $\Delta$(1232) **单 $\pi$ 共振**
- 高能极限：$\sigma$ 随 $s$ 对数增长
- 第一共振之后：由多重 $\pi$ 产生 $N\gamma_b \to N(n\pi)$, $n>1$ 主导

[FACT] **其他损失机制**：

**质子-对产生 (PPP, $p\gamma_b\to p\,e^+e^-$)** — 公式 14：
$$
E_{\rm th} = \frac{m_e(m_N+m_e)}{\epsilon} \simeq 4.8\times10^{14}\cdot\left(\frac{\epsilon}{{\rm eV}}\right)^{-1}\ {\rm eV}
$$
CMB 中 PPP 发生于 $E\sim 5\times10^{17}$ eV。首个天体物理讨论：Blumenthal [158]。核电荷 $Z$ 情形：PPP 截面 $\sim Z^2\times$ triplet pair production 截面。

**红移**：PPP 阈值附近的下一个主要损失机制。

**中子 $\beta$-衰变 ($n\to p\,e^-\bar\nu_e$)** — 公式 15：
$$
R_n = \tau_n\cdot E/m_N \simeq 0.9\cdot(E/10^{20}\ {\rm eV})\ {\rm Mpc}
$$
$\tau_n = 888.6\pm 3.5$ s；对 $E\lesssim 10^{20}$ eV 的中子主导损失。

**核的光致分裂（Giant Dipole Resonance）**：
- 对 $E\gtrsim 10^{19}$ eV 的核是主导损失
- 早期估算：衰减长度 ~几 Mpc
- **Mrk 421, Mrk 501** 多 TeV $\gamma$ 观测 [163,164] → IRB 比先前假设低约 **10 倍** → 核衰减长度增加
- 最新 MC 模拟 [167–169]：降低 IRB 后，CMB 成为主导 → **$E\sim 2\times10^{20}$ eV 处衰减长度 ~10 Mpc**
- 意味着：若最高能事件为重核，加速器距离不能超过几十 Mpc

[FACT] [作者强调] **GZK 的物理论证**：
> "Even for conventional local sources, the maximal energy to which charged primaries can be accelerated is expected to be limited ... and it is generally hard to achieve energies beyond the cutoff energy."
> "a cutoff is expected at least for extragalactic nucleon primaries irrespective of the production mechanism."

[INTERPRETATION] 这是 §2.3 中\"最高能过量事件\"为什么是 UHECR 物理最核心谜题的关键：若 GZK 是\"与加速机制无关\"的必然结果，而观测到 >$10^{20}$ eV 事件超出 GZK 预期 → 必须用新物理（新粒子、新传播机制或 top-down 场景）解释。

---

## 4.2 UHE Photons and Electromagnetic Cascades

> **超高能光子与电磁级联**

[FACT] §4.2 转向 UHE 光子。主导过程是 **Pair Production (PP)** 与 **Inverse Compton Scattering (ICS)**；二者循环形成 EM cascade，堆积谱呈 E$^{-1.5}$ 特征并在 ~100 GeV 以下堆积。§4.2 还讨论 URB、EGMF 抑制、高 QED 过程（DPP、TPP）以及一系列可忽略过程。

[FACT] **主导过程**：
- **PP**：$\gamma\gamma_b\to e^+e^-$
- **ICS**：$e\,e^++\gamma_b\to$ 更高能 $\gamma$

阈值（公式 16）：
$$
E_{\rm th} = \frac{m_e^2}{\epsilon} \simeq 2.6\times10^{11}\cdot\left(\frac{\epsilon}{{\rm eV}}\right)^{-1}\ {\rm eV}
$$

高能极限截面（公式 17）：
$$
\sigma_{\rm PP} \simeq 2\,\sigma_{\rm ICS} \simeq \frac{3}{2}\,\sigma_{\rm T}\cdot\frac{m_e^2}{s}\cdot\ln\!\left(\frac{s}{2m_e^2}\right)\quad (s\gg m_e^2)
$$

[FACT] **级联发展** — Klein-Nishina 极限下：PP 产生的 $e^+/e^-$ 携带大部分原始 $\gamma$ 能量 → ICS 非弹性度 ~1 → upscattered $\gamma$ 又成 leading → **反复 PP–ICS 循环** → EM cascade。
- 能量衰减长度 > 相互作用长度（有效穿透更深，见 Fig. 11, 12）
- **级联堆积谱**：$E^{-1.5}$ 特征谱 [35, 182–184]
- 完全发展级联能量在 **~100 GeV 以下堆积** → 受 EGRET diffuse $\gamma$-ray 数据约束

[FACT] **通用射电背景 (URB)**：
- 关键背景：$\epsilon\lesssim 10^{-6}$ eV（~100 MHz），即**射电背景**
- URB 的河外成分不确定（银河 vs 河外难以分开）
- 1 MHz 以下 URB 因 free-free 吸收指数截断，截断位置 **0.1–2 MHz 不确定**
- Fig. 10 比较理论 [175] vs 早期理论 [174] vs 观测 [173]

[FACT] **EGMF 对级联的影响**：
- 河外磁场抑制级联发展（通过 $e^+e^-$ 同步冷却）
- 同步冷却时标 < ICS 时标 → 级联停止 → UHE $\gamma$ 通量由\"直接\"$\gamma$（起源 < 吸收长度）主导
- 强 EGMF 效应：**高能端通量降低、~几十–几百 GeV 通量升高**

[FACT] **高 QED 过程**：

**双对产生 (DPP, $\gamma\gamma_b\to e^+e^-e^+e^-$)** — 公式 18：
$$
\sigma_{\rm DPP} \simeq \frac{172\,\alpha^4}{36\pi m_e^2} \simeq 6.45\ \mu{\rm barn}\quad (s\gg m_e^2)
$$
DPP 主导 PP 的能区：**$E>10^{21}$–$10^{23}$ eV**（强 URB 时取较高值）。

**三对产生 (TPP, $e\gamma_b\to e\,e^+e^-$)** — 公式 19, 20：
$$
\sigma_{\rm TPP} \simeq \frac{3\alpha}{8\pi}\,\sigma_{\rm T}\cdot\left(\frac{28}{9}\ln(s/m_e^2)-\frac{218}{27}\right)
$$
$$
\eta \simeq 1.768\cdot(s/m_e^2)^{-3/4}\quad (s\gg m_e^2)
$$
尽管 $\sigma_{\rm TPP}\sim\sigma_{\rm ICS}$ 在 $E\sim 10^{17}$ eV 已可比，但 $\eta\lesssim 10^{-3}$ → 能量衰减直到 **~$10^{22}$ eV** 才重要。主要影响：产生大量次级电子，把它们带到 UHE 以下。若 $B_{\rm rms}>\sim 10^{-12}$ G → 同步冷却主导 TPP → 可忽略。

[FACT] **其他可忽略过程**：
- $\mu^+\mu^-$, $\tau^+\tau^-$, $\pi^+\pi^-$ 对产生（~比 $e^+e^-$ 小 10×）
- 双 Compton 散射（$\alpha^3$ 阶，UHE 下 <10%）
- $\gamma\gamma_b\to\gamma\gamma$（$z>\sim 100$ 时才重要）
- Bethe-Heitler 对产生
- $\gamma B\to e^+e^-$（银河系强度 ~$10^{-6}$ G 需 $E>\sim 10^{24}$ eV；EGMF 下更高）

---

## 4.3 Propagation and Interactions of Neutrinos and \"Exotic\" Particles

> **中微子与\"奇特\"粒子的传播与相互作用**

[FACT] §4.3 讨论电中性、与 CMB/IRB 相互作用极弱或无相互作用的粒子，作为 EHECR 候选源——它们不受 GZK 截断约束。分为 4.3.1 中微子、4.3.2 超对称粒子、4.3.3 其他奇特粒子。

### 4.3.1 Neutrinos

> **中微子**

[FACT] UHE 中微子主要与**宇宙 relic 中微子背景 (RNB)** 相互作用。中微子-UHE 中微子 (E) 与 relic 中微子 ($\epsilon$) 的平均 CM 能量平方（公式 21）：
$$
\langle s\rangle \simeq (45\ {\rm GeV})^2\cdot\left(\frac{\epsilon}{10^{-3}\ {\rm eV}}\right)\cdot\left(\frac{E}{10^{15}\ {\rm GeV}}\right)
$$
- 相对论 relic $\nu$：$\epsilon\simeq 3T_\nu(1+\eta_{\rm b}/4)$，$T_\nu\simeq 1.9(1+z)$ K = $1.6\times10^{-4}(1+z)$ eV
- 非相对论 relic $\nu$ ($m_\nu\lesssim 20$ eV)：$\epsilon\simeq\max[3T_\nu,\ m_\nu]$

[FACT] **主导相互作用**：
- t-channel W$^\pm$：$\nu_i+\bar\nu_j\to l_i+\bar l_j$
- s-channel Z$^0$：$\nu_i+\bar\nu_i\to f\bar f$
- t-channel Z$^0$：$\nu_i+\bar\nu_j\to \nu_i+\bar\nu_j$

s-channel Z$^0$ 微分截面（公式 22）：
$$
\frac{d\sigma}{d\mu} = \frac{G_F^2\,s}{4\pi}\cdot\frac{M_Z^2}{(s-M_Z^2)^2+M_Z^2\Gamma_Z^2}\cdot[g_L^2(1+\mu^*)^2+g_R^2(1-\mu^*)^2]
$$
t-channel 截面（公式 23）：
$$
\sigma_{\rm t}(E,\epsilon)\sim\min\left[10^{-34},\ 3\times10^{-39}\cdot\left(\frac{\epsilon}{10^{-3}\ {\rm eV}}\right)\cdot\left(\frac{E}{10^{20}\ {\rm eV}}\right)\right]\ {\rm cm}^2
$$

[FACT] **中微子-核子截面 (公式 24)**：
$$
\sigma_{\nu N}(E)\sim 10^{-31}\cdot(E/10^{20}\ {\rm eV})^{0.4}\ {\rm cm}^2\quad (E\gtrsim 10^{15}\ {\rm eV})
$$
尽管 $\sigma_{\nu N}>\sigma_{\nu\nu}$(RNB)，但 RNB 粒子数密度比重子密度高 **~$10^{10}$** → RNB 相互作用仍占主导（除 GUT 尺度能量外）。

[FACT] **其他中微子相互作用**：
- **$\nu+\gamma\to lW^+$** [197]：W$^\pm$ 产生阈值以上可与 $\nu\nu$ 过程可比，但永远不主导
- **$\gamma+\nu\to\gamma+\gamma+\nu$** [198]：$\sigma\simeq 9\times10^{-56}(s/{\rm MeV}^2)^5\ {\rm cm}^2$（valid up to $s\lesssim 10$ MeV$^2$）；若 $s^5$ 行为持续到 $s\sim$ 几百 MeV$^2$，则在 $E\sim 3\times10^{17}(\epsilon/10^{-3}\ {\rm eV})$ eV 开始主导 [199]

[FACT] **Z-burst 情景**：若 relic 中微子质量 ~1 eV（热暗物质，可能聚集在星系团/银晕），在
$$
E = M_Z^2/(2m_\nu) = 4\times10^{21}\ ({\rm eV}/m_\nu)\ {\rm eV}
$$
处 Z$^0$ 共振湮灭概率增大；Z$^0$ 衰变产物主要核子 (~$E_\nu/5$) 和 $\gamma$ (~$E_\nu/40$)。若 UHE $\nu$ 是加速质子的次级产物 → 需加速至 ≥ 几 $10^{22}$ eV → 更可能来自 non-acceleration (top-down) 场景。

**关键约束**：
- Z$^0$ 湮灭主要由**非聚集的** RNB 主导（而非银晕内聚集的），除非新 $\nu$ 源 [204]
- EGRET diffuse $\gamma$-ray (~10 GeV) 约束：若 X 粒子只衰变到 $\nu$：$f_\nu\gtrsim 20\ (l_\nu/5\ {\rm Mpc})^{-1}$；若 $L_\gamma\sim L_\nu$（多数模型）：$f_\nu\gtrsim 10^3\ (l_\nu/5\ {\rm Mpc})^{-1}$
- Z-burst 要求源对加速质子**光学厚**

[FACT] **中微子振荡 (Super-K 结果 [212])**：$\mu$–$\tau$ 近最大混合，$|\Delta m^2|\simeq 5\times10^{-3}$ eV$^2$：
$$
L_{\rm osc} = 2E/|\Delta m^2| = 2.6\times10^{-6}\,(E/{\rm PeV})\,(|\Delta m^2|/5\times10^{-3}\ {\rm eV}^2)^{-1}\ {\rm pc}
$$
银河系 halo 中的 RNB 势引起的共振转换可能影响 UHE $\nu$ 味组成 [224]；长基线对 $\nu$ 衰变敏感 [225]。

[FACT] **Neutrino Detection**：通过 CC 反应产生的 $\mu$ 子探测。折叠 quark-$\nu$ 基本截面与核子内 parton 分布函数 (PDF)。对 $x\simeq M_W^2/(2m_N E)$ 的 parton 最敏感。

**中微子-核子 CC 截面 (公式 25)**：
$$
\sigma_{\nu N}(E) \simeq 2.36\times10^{-32}\cdot(E/10^{19}\ {\rm eV})^{0.363}\ {\rm cm}^2\quad (10^{16}\ {\rm eV}\lesssim E\lesssim 10^{21}\ {\rm eV})
$$
- CTEQ4-DIS 参数化 [227]；非主导 $1/x$ 对数贡献 [231]：与 [227,230] 差异 <1.5 倍（至 $10^{21}$ eV）
- NC 截面比 CC 小 2–3 倍
- Glashow 共振：$\bar\nu_e e\to W^-$，$E = 6.3\times10^{15}$ eV

[FACT] **地球衰减**：>~100 TeV 中微子在地球内开始被吸收（$\sigma$ 随 E 增长）。**$\tau$ 中微子再生**：$\tau$ 中微子能量到 ~100 PeV 仍可穿透地球，因为 $\tau$ 衰变再产生 $\tau$ 中微子。PeV 能量处**"double-bang"事件** [222]：第 1 个 bang（CC 产生 $\tau$）；第 2 个 bang（$\tau$ 在 ~100 m 外衰变）。各向同性 10 TeV–10 PeV $\nu$ 流可作为地球密度分布的探针（中微子吸收层析 [234]）。

[FACT] **新物理增强的中微子截面**：

**Generation Symmetry 情景** [235–236]：引入破缺 SU(3) 规范对称（与 QCD 颜色 SU(3) 对偶）；三族轻子/夸克代表 generation 对称量子数；中微子与夸克有效强相互作用 → 有效截面 ~几何核子截面。约束：FCNC 实验 → 新相互作用尺度 >~100 TeV。

**大额外维度 (ADD) 情景** [237–242]：$n$ 个额外紧致维度，量子引力尺度 $M_{4+n}\sim$ TeV。Bulk graviton (KK 模式) 交换增强两粒子截面（公式 26）：
$$
\sigma_{\rm g} \simeq \frac{4\pi s}{M_{4+n}^4} \simeq 10^{-27}\cdot(M_{4+n}/{\rm TeV})^{-4}\cdot(E/10^{20}\ {\rm eV})\ {\rm cm}^2
$$
- 中微子 $\sigma_{\nu N}>10^{-27}$ cm$^2$ 开始在大气中作用 → 中微子成为 EHECR 事件候选
- 具体信号：IceCube/水冰中微子望远镜 E > $E_c$ 处无事件；Pierre Auger E > $E_c$ 处谱硬化
- 超新星约束 [240]：$M_6\gtrsim 50$ TeV, $M_7\gtrsim 4$ TeV, $M_8\gtrsim 1$ TeV ($n=2,3,4$) → 若中微子作 EHECR 候选，需 **$n\ge 4$**
- 额外维度半径 (公式 27)：
$$
r_n \simeq M_{4+n}^{-1}\left(M_{\rm Pl}/M_{4+n}\right)^{2/n} \simeq 2\times10^{-17}\cdot({\rm TeV}/M_{4+n})\cdot(M_{\rm Pl}/M_{4+n})^{2/n}\ {\rm cm}
$$
对应上限：$r_6\lesssim 3\times10^{-4}$ mm, $r_7\lesssim 4\times10^{-7}$ mm, $r_8\lesssim 2\times10^{-8}$ mm

### 4.3.2 Supersymmetric Particles

> **超对称粒子**

[FACT] **轻 quasi-stable gluino**：若 gluino 质量 ~0.1–1 GeV [245]，最轻 gluino-baryon $uds\tilde g$ 记作 **S$^0$**，可长寿命或稳定。

**有效 GZK 阈值提高** [246]：阈能被抬高（$m_{S^0}$ 代替 $m_N$ 代入公式 13）；截面峰值位置抬高 $(m_{S^0}/m_N)\cdot(m^*-m_{S^0})/(m_\Delta-m_N)$ 倍（质量间距比 $\gtrsim 2$）；有效 GZK 阈值**提高几个量级** → **源可远 15–30 倍**于核子情形。

**观测关联** [FACT, Farrar & Biermann [247]]：5 个最高能量 CR 事件到达方向与 $z=0.3$–2.2 致密类星体可能相关。但统计分析受 Hoffman [248] 批评，Farrar & Biermann [249] 回应。

[FACT] **加速器约束**：[245] 的轻 gluino 情景已被加速器约束否定 [250,251]。"可调节"gluino 质量情景 [243] 仍可能：候选 R$^0$ (glueballino $\tilde g\tilde g$)、$\tilde\rho$（isotriplet $\tilde g\!-\!(u\bar u - d\bar d)_8$）。EAS 组成约束 [254]：**初级粒子静止质量 <~50 GeV**；Auger 数据可降至 ~10 GeV。S$^0$ 需作为加速质子与物质作用的次级产物 → 质子需加速至 ≥ $10^{21}$ eV。次级过程也产生 $\nu$ 和 $\gamma$ → 可通过 EGRET/GLAST/HEGRA/WHIPPLE/VERITAS 约束。质子→R-hadron 分支比 >~0.01（粗略估计）。

### 4.3.3 Other Particles

> **其他奇特粒子**

[FACT] **uuddss H-dibaryon**：QCD instanton 诱导 uds-uds 束缚态，$M_H\simeq 1700$ MeV [255]。性质类似 S$^0$：中性、自旋 0。**有效 GZK 截断 ~$7.3\times10^{20}$ eV**（比核子高），可作为高红移源的 EHECR 事件候选。

---

## 4.4 Signatures of Galactic and Extragalactic Magnetic Fields in UHECR Spectra and Images

> **银河系与河外磁场在 UHECR 谱与图像中的印记**

[FACT] §4.4 讨论 EGMF 在 UHE 光子与强子传播中的两类主导效应：同步冷却对 EM 级联的抑制（§4.4.1），以及偏转 + 延迟对带电强子图像与时间结构的影响（§4.4.2）。

[INTERPRETATION] §4 逻辑链的收束点：**磁场是 UHECR 源定位的放大器也是混淆器**——它压制 EM 级联从而保护部分 UHE $\gamma$（§4.4.1），它抹平源像但保留中心指向（§4.4.2），它把\"几百 Mpc 内是否存在强源\"的问题转化为\"偏转角 + 延迟时间\"的联合测量（§4.5–4.6）。

### 4.4.1 Synchrotron Radiation and Electromagnetic Cascades

> **同步辐射与电磁级联**

[FACT] §4.4.1 给出同步冷却的**能量损失率 (公式 28)**：
$$
\frac{dE}{dt} = -\frac{4}{3}\,\sigma_{\rm T}\,\frac{B^2}{8\pi}\left(\frac{q\,m_e}{m}\right)^4\left(\frac{E}{m_e}\right)^2
$$
- UHE 质子：$m$ 极大 → 同步损失**可忽略**
- UHE 电子：同步损失在**转移能量**以上占主导

[FACT] **转移能量（同步冷却）**：
$$
E_{\rm tr} \sim 10^{20}\left(\frac{B}{10^{-10}\ {\rm G}}\right)^{-1}\ {\rm eV}
$$
[INTERPRETATION] 当 $E>E_{\rm tr}$，电子几乎瞬间通过同步辐射损失能量 → EM cascade 发展被阻断 → $\gamma$ 传播由 PP/DPP 吸收主导 → 可观测通量由\"直接\"（first-generation）$\gamma$ 决定 → 简化为式 (12) 用 $l(E)$ 代替 $l_E(E)$。

[FACT] **同步辐射光子能量 (公式 29)**：
$$
E_{\rm syn} \simeq 6.8\times10^{13}\left(\frac{E}{10^{21}\ {\rm eV}}\right)^2\left(\frac{B}{10^{-9}\ {\rm G}}\right)\ {\rm eV}
$$
- 经典极限下有效（$E_{\rm syn}\ll E$）
- **约束来源**：当 $E_{\rm syn}$ 落入已有 diffuse $\gamma$ 观测窗口时——EGRET ~1 GeV [185]；HEGRA 上界 50–100 TeV [257]；CASA-MIA $6\times10^{14}$–$6\times10^{16}$ eV [258]

[FACT] **强离散 UHE $\gamma$ 源**（如拓扑缺陷，近单能注入谱，EGMF ~$10^{-9}$ G）在某些 $E>\sim 10^{16}$ eV 处预言 $\gamma$ 通量 > 带电 CR 通量 → **已被排除** [259]。

**关键公式**：
$$
\boxed{E_{\rm tr}\sim 10^{20}\left(\frac{B}{10^{-10}\ {\rm G}}\right)^{-1}\ {\rm eV}\ ;\quad E_{\rm syn}\simeq 6.8\times10^{13}\left(\frac{E}{10^{21}\ {\rm eV}}\right)^2\left(\frac{B}{10^{-9}\ {\rm G}}\right)\ {\rm eV}}
$$

### 4.4.2 Deflection and Delay of Charged Hadrons

> **带电强子的偏转与延迟**

[FACT] 回旋半径 $r_g\simeq E/(q\,e\,B_\perp)$。均匀场 $B$ 中传播距离 $d$ 的**单场偏转角 (公式 30)**：
$$
\theta(E,d) \simeq \frac{d}{r_g}\simeq 0.52°\cdot q\cdot\left(\frac{E}{10^{20}\ {\rm eV}}\right)^{-1}\left(\frac{d}{1\ {\rm Mpc}}\right)\left(\frac{B_\perp}{10^{-9}\ {\rm G}}\right)
$$

[FACT] 磁场特征为 rms 强度 $B$ + 关联长度 $l_c$；$d\gtrsim l_c$ 时的**随机场 rms 偏转角 (公式 31)**：
$$
\theta(E,d) \simeq \frac{(2\,d\,l_c/9)^{1/2}}{r_g}\simeq 0.8°\cdot q\cdot\left(\frac{E}{10^{20}\ {\rm eV}}\right)^{-1}\left(\frac{d}{10\ {\rm Mpc}}\right)^{1/2}\left(\frac{l_c}{1\ {\rm Mpc}}\right)^{1/2}\left(\frac{B}{10^{-9}\ {\rm G}}\right)
$$

[FACT] **三种极限行为**：
- **$d\theta\ll l_c$**（相干）：所有能量粒子\"看到\"同一磁场实现 → 偏转一致，源像保持紧密 → 偏转方向偏离视线方向（coherent deflection）
- **$d\theta\gg l_c$**（漫散射）：源像被抹平，扩展范围 $\sim\theta(E,d)$，**但中心对准真实源方向**
- **$d\theta\simeq l_c$**：可能产生**多像**（类似引力透镜）

[FACT] **平均时间延迟 (公式 32)**：
$$
\tau(E,d) \simeq \frac{d\,\theta^2}{4}\simeq 1.5\times10^3\,q^2\cdot\left(\frac{E}{10^{20}\ {\rm eV}}\right)^{-2}\left(\frac{d}{10\ {\rm Mpc}}\right)^2\left(\frac{l_c}{1\ {\rm Mpc}}\right)\left(\frac{B}{10^{-9}\ {\rm G}}\right)^2\ {\rm yr}
$$

[FACT] **Bursting source 效应**：$\tau\propto E^{-2}$ → 观测窗口内的瞬时谱与长时间平均谱不同，在 $\tau(E_0,d)\simeq$（观测时刻 − 零延迟到达时刻）处出现**谱峰 $E_0$**；高能粒子已过，低能粒子未至。

[FACT] **谱宽度**：$d<$ 相互作用长度且 $d\theta\ll l_c$ → 谱宽 $\ll E_0$；其他情形 → 谱宽 $\sim E_0$。

**关键公式**：
$$
\boxed{\theta\simeq 0.8°\cdot q\left(\frac{E}{10^{20}\ {\rm eV}}\right)^{-1}\left(\frac{d}{10\ {\rm Mpc}}\right)^{1/2}\left(\frac{l_c}{1\ {\rm Mpc}}\right)^{1/2}\left(\frac{B}{10^{-9}\ {\rm G}}\right)\ ;\quad \tau\propto E^{-2}}
$$

---

## 4.5 Constraints on EHECR Source Locations

> **EHECR 源位置约束**

[FACT] §4.5 综合偏转几何与 GZK 距离给出对源位置的联合约束。

**距离–角度约束**：
- 核子/核/$\gamma$ > 几十 EeV 起源距离 $\lesssim 50$ Mpc（GZK / 光致分裂 / PP-DPP）
- 结合公式 (31) → 到达方向应**在几度内指向源** [12]
- 银河盘内偏转可\"反演修正\"（银河磁场图的计算 [264,265]）

**Faraday Rotation 约束**：
- **原版本**：$B\,l_c^{1/2}\lesssim 10^{-9}$ G Mpc$^{1/2}$ [262,263]
- **修正版**（用 $\Omega_{\rm b}h^2\simeq 0.02$ 替代 closure density，未结构宇宙）：
$$
B \lesssim 3\times10^{-7}\left(\frac{\Omega_{\rm b}h^2}{0.02}\right)^{-1}\left(\frac{h}{0.65}\right)\left(\frac{l_c}{{\rm Mpc}}\right)^{-1/2}\ {\rm G}
$$
- **大尺度结构修正**（Lyman-$\alpha$ forest 建模 + 磁通冻结）[267]（公式 34）：
$$
B \lesssim 10^{-9}\text{–}10^{-8}\ {\rm G}
$$
关联尺度从 Hubble 到 1 Mpc；sheets 和 voids 内最大场可达 $\sim\mu$G [268,267,269]

[FACT] **结论**：若本地大尺度结构不强磁化 → UHE 核子偏转仍在度级；但**超星系面强磁化**、或**近邻星团**（场强 $10^{-6}$ G [262–263,270]）、或**重核（如 Fe）** → 可能强烈偏转 [26]。强磁化下，EGMF 磁透镜效应可影响 UHECR 源位置 [311,316]。

**关键公式**：
$$
\boxed{B\,l_c^{1/2}\lesssim 10^{-9}\ {\rm G\,Mpc}^{1/2}\ ;\quad B\lesssim 10^{-9}\text{–}10^{-8}\ {\rm G}\ ;\quad d_{\rm src}\lesssim 50\ {\rm Mpc}}
$$

---

## 4.6 Source Search for EHECR Events

> **EHECR 事件的源搜索**

[FACT] §4.6 汇总 1998 年前后的单事件关联与统计关联尝试。

**Fly's Eye 300 EeV 事件**（$3.2\times10^{20}$ eV）[26]：

| 候选源 | 距离 | 到达方向偏离 |
|---|---|---|
| Cen A | ~3 Mpc | ~136° |
| Virgo A | 13–26 Mpc | ~87° |
| M82 | 3.5 Mpc | ~37° |
| **MCG 8-11-11** (Seyfert) | 62–124 Mpc | **~10°** |
| **3C134** (FR II radio gal.) | 30–500 Mpc（不确定） | **~10°** |

- **3C147** (quasar, $z\sim 0.5$) 在 Fly's Eye 事件误差箱内 → 曾建议为**中微子源** [72]
- 中微子假设问题：$\sigma_{\nu N}$ 在 $10^{20}$ eV 大气相互作用概率 $\sim 10^{-5}$

[FACT] **AGASA 最高能事件**：中微子假设 → **3C33** (FR II, ~300 Mpc)；核子假设 → **NGC 315** (FR I, ~100 Mpc)。银晕 Fe 初级 + 扩展银晕磁场 → 银道面起源可能 [273]。

[FACT] **统计关联**：

| 数据 | 关联对象 | 结果 |
|---|---|---|
| Haverah Park + AGASA + VR + Yakutsk | Supergalactic Plane | **~3$\sigma$** 正相关（E > $4\times10^{19}$ eV）[79] |
| SUGAR 南半球 | 同 | 无显著相关 [80] |
| AGASA（最新）[81,83] | 20% EHECR 彼此 + SG 面 | 部分相关；其余各向同性 |
| 组合分析 [274,275] | 同 | 一致，但未定论 |
| CFA Redshift Catalog [278] | 50 Mpc 内星系 | 到达方向一致 |

[CRITIQUE] [276] 指出 Haverah Park SG 面关联\"过强\"（对 Local Supercluster 之外的星系而言）→ [277,271] 提议大尺度结构中存在 $\mu$G 级场，沿 sheets/filaments 对齐 → **聚焦效应**。

[FACT] **GRB 与其他关联**：两最高能量事件在 BATSE GRB 误差箱内 [279]，但大样本无显著结果 [280]。若 GRB 为银河尺度 → 反证 GRB 关联；若河外 → 需考虑大时间延迟（见 §5.3）。

[FACT] **Yakutsk EAS**：UHECR $(0.8\text{–}4)\times10^{19}$ eV 与**银道面脉冲星沿磁感线方向**统计显著相关 [283]。

**关键参数**：转移能量 $E_{\rm tr}\sim 10^{20}(B/10^{-10}\ {\rm G})^{-1}$ eV；均匀场偏转角 $0.52°\,q(E/10^{20}\ {\rm eV})^{-1}(d/{\rm Mpc})(B_\perp/10^{-9}\ {\rm G})$；随机场延迟 $\tau\sim 1.5\times10^3\,q^2\,(E/10^{20}\ {\rm eV})^{-2}(d/10\ {\rm Mpc})^2(l_c/{\rm Mpc})(B/10^{-9}\ {\rm G})^2$ yr；源距离约束 $\lesssim 50$ Mpc。

---

## 4.7 Detailed Calculations of Ultra-High Energy Cosmic Ray Propagation

> **超高能宇宙线传播的详细计算**

[FACT] §4.7 系统给出多粒子耦合传播方程、各类粒子求解方法、以及用 angle-time-energy 图像反演 EGMF 与源参数的方法。

### 4.7.1 Average Fluxes and Transport Equations in One Dimension

> **一维平均通量与传输方程**

[FACT] 对一组粒子种类 $i$，局域能量密度 $n_i(E)$ 的演化（公式 35）：
$$
\partial_t n_i(E) = -n_i(E)\!\int\!d\!\epsilon\,n_b(\!\epsilon\!)\!\int_{-1}^{+1}\!d\mu\,\frac{1-\beta_b\beta_i}{2}\!\sum_j \sigma_{i\to j}\!\bigl[s\!=\!\epsilon E(1-\beta_b\beta_i)\bigr]
$$
$$
+\!\int\!dE'\!\int\!d\!\epsilon\,n_b(\!\epsilon\!)\!\int_{-1}^{+1}\!d\mu\!\sum_j \frac{1-\beta_b\beta'_j}{2}\,n_j(E')\frac{d\sigma_{j\to i}}{dE}\!\bigl[s\!,\,E\bigr] + \Phi_i
$$
- 第一项：species $i$ 通过相互作用**损失**；第二项：其他 species $j$ 通过相互作用**产生** $i$；第三项：注入

[FACT] **求解方法**：

| 粒子 | 求解方法 | 参考 |
|---|---|---|
| 核子/核 | CEL 近似 [288,289] 或精确 Boltzmann 方程 [290,156,291]；Monte Carlo [292,26,293,294]；核光致分裂 MC [25,167,169] | |
| EM cascade | Hybrid MC + matrix doubling [296] 或隐式数值 [156,205,206]；能量覆盖 100 MeV – $10^{16}$ GeV (GUT scale) | [259,295] |
| 中微子 | 完整 Boltzmann 方程 [195]；规范流量 [196]；半解析 [298] | |
| 全耦合 | [205,206] 集成代码：nucleons + $\gamma$ + e + $\nu$ 联立 | |

[CRITIQUE] **CEL 近似的局限**：
- 对 PPP（小非弹性度）：**优秀**
- 对 $\pi$ 产生（大非弹性度，随机性）：CEL 在 GZK 截断**正下方**产生更尖锐的堆积谱（\"pile-up\"）vs 精确解 [290]
- CEL 对连续源分布或远距离 discrete 源**仍可工作**（多次 $\pi$ 产生事件平均下）

**关键公式**：
$$
\boxed{\partial_t n_i(E) = -\text{loss}(n_i) + \text{gain}(n_j\to n_i) + \Phi_i\;\;{\rm (Eq.\ 35)}}
$$

### 4.7.2 Angle-Time-Energy Images of Ultra-High-Energy Cosmic Ray Sources

> **超高能宇宙线源的角度–时间–能量图像**

[FACT] **强偏转 (Diffusion 近似)**：大尺度磁场（$10^{-8}\text{–}10^{-6}$ G，如星系团内）→ 扩散近似适用。能量损失–扩散方程（公式 36）：
$$
\partial_t n(r,E) = -\partial_E\bigl[b(E)\,n(r,E)\bigr] + \nabla\!\cdot\!\bigl[D(r,E)\,\nabla n(r,E)\bigr] + \Phi(E)
$$
- 若 $D(r,E)$ 不依赖 $r$ → **Syrovatskii 解析解** [300]
- 应用于 EGMF ~几$\times 10^{-8}$ G，$E$ 至 $\sim 10^{20}$ eV
- 但在 UHECR 实际应用中，**扩散近似与 rectilinear 之间的过渡区**是典型情况，此方程适用性有限

[FACT] **各向异性 (公式 37)**：
$$
\delta(E) = \frac{3\,D(r,E)}{n(r,E)}\,|\nabla n(r,E)|
$$

[FACT] **小偏转 (Monte Carlo, 3D)**：磁场建模为 Gaussian 随机场，零均值，功率谱 $B^2(k)\propto k^{n_{\rm H}}$ for $k<k_c$，$k_c=2\pi/l_c$。MC 流程：傅里叶生成磁场网格实现 → 注入粒子 $E$ 对数均匀分布 → 求解运动方程（含 $\pi$ 产生 + PPP）→ 记录到达能量、时间、方向 → 40000 粒子 → time-energy histogram → Poisson 抽样模拟观测事件。

[FACT] **关键参数与 likelihood**：$\tau_{100}$（$E=100$ EeV 处磁偏转延迟，公式 32）；$T_S$（源发射时间尺度，$T_S\ll 1$ yr = burst，$T_S\gg 1$ yr = 连续源）；$\gamma$（注入谱微分指数）；$N_0$（源到探测器的总 fluence）。

[FACT] **EGMF 约束 (公式 38，来自 AGASA 200 EeV 事件对分析)**：
$$
B \lesssim 2\times10^{-11}\left(\frac{l_c}{1\ {\rm Mpc}}\right)^{-1/2}\left(\frac{d}{30\ {\rm Mpc}}\right)^{-1}\ {\rm G}
$$
- 若证实，比 Faraday rotation 强两个量级

[FACT] **五种 generic time-energy 图像情形**（按 $\tau_E$ vs $T_S$ vs 实验寿命）：
- $\tau_E\ll T_S$：距离由 pion 产生特征（GZK cutoff 以上）确定，误差 $\sim 2\times$
- $T_S\ll\tau_E<$ 实验寿命：磁场强度可从 time-energy 图像得到
- $T_S\gg\tau_E\gg$ 实验寿命：只能给磁场下限（与 Faraday 结合可得数量级估计）
- $T_S\sim\tau_E$：最佳参数估计情况

[FACT] **发射时间尺度可探测范围 (公式 39)**：
$$
3\times10^3\left(\frac{\Delta\theta}{1°}\right)^2\left(\frac{d}{10\ {\rm Mpc}}\right)\ {\rm yr} \lesssim T_S\simeq\tau_E\lesssim 10^4\text{–}10^7\left(\frac{E}{100\ {\rm EeV}}\right)^{-2}\ {\rm yr}
$$

[FACT] **一般情形：扩散 vs rectilinear 的过渡区**（Monte Carlo 推广到任意偏转 [311]）：Supergalactic Plane 建模为厚度几 Mpc、密度高斯剖面的 sheet；Kolmogorov 谱 $n_{\rm H}=-11/3$（Kraichnan 谱 $n_{\rm H}=-7/2$ 也考虑）。

[FACT] **扩散系数 (公式 40)**：
$$
D(E) \simeq \frac{1}{3}\,r_g(E)\,B\!\int_{1/r_g}^{\infty}\!dk\,k^2\,\langle B^2(k)\rangle
$$
- Kolmogorov 谱下：扩散区（$\tau_E\gtrsim d$）：$D(E)\propto E^{1/3}$（$r_g<L/2\pi$）→ $\tau_E\propto E^{-1/3}$；Bohm 扩散（$r_g>L/2\pi$）：$D(E)\propto E$ → $\tau_E\propto E^{-1}$；Rectilinear：$\tau_E\propto E^{-2}$

[FACT] Fig. 19 显示 bursting source 上 $\tau$–$E$ 关系的三个 regime；Fig. 20：最优场强（源 $d=10$ Mpc, $B_{\rm max}=10^{-7}$ G）对 $E>10$ EeV 数据的最佳拟合；有效回旋半径 ~解析估计的 10×；不同磁场实现间谱涨落显著。

[FACT] **现代 AGASA 数据启示**：最新 AGASA 数据显示 EHECR **各向同性** [83]。单一源 + 强场解释 → GZK 以上通量被过度抑制 → **需要连续源分布** [314]。弥漫源分布 + Supergalactic Plane 关联 + **$B\gtrsim 0.05\,\mu$G** → 可解释大尺度各向同性 + 小尺度聚团 [316]。Fig. 24：$B_{\rm max}=0.05$ 和 0.5 $\mu$G 均能很好地拟合数据。

**关键公式**：
$$
\boxed{B\lesssim 2\times10^{-11}\left(\frac{l_c}{{\rm Mpc}}\right)^{-1/2}\left(\frac{d}{30\ {\rm Mpc}}\right)^{-1}\ {\rm G}\ ;\quad D(E)\propto E^{1/3}\ ({\rm Kolmogorov}),\ E,\ E^{-2}\ ({\rm Bohm/rect})}
$$

---

## 4.8 Anomalous Kinematics, Quantum Gravity Effects, Lorentz symmetry violations

> **异常运动学、量子引力效应与 Lorentz 对称性破缺**

[FACT] §4.8 转向超出标准模型的传播效应：Lorentz 不变性破坏、量子引力色散、快子中微子。

[FACT] **Lorentz Invariance Violation (VLI) 约束**：若 $10^{20}$ eV 事件是质子 → $(c_p-c)<10^{-23}$（否则质子会在 ~几百 cm 内通过 Cherenkov 辐射损失能量）。VLI 可避免 GZK 截断（微小偏离下，阈值升高）。**VPE (Violation of Equivalence Principle) 等效** → 质子与光子的引力耦合差异 $<10^{-19}$（比 Eötvös 实验精确 5 个量级）。

[FACT] **量子引力色散关系**：

**色散 (公式 41)**：
$$
c^2k^2 \simeq E^2 + \chi\,\frac{E^3}{E_0}
$$
对应光子群速度 $\partial E/\partial k = c[1 - \chi\,E/E_0 + \mathcal{O}(E^2/E_0^2)]$。$\chi=\pm 1$；$E_0$ = 量子引力尺度。

**阈值 (公式 42)**：
$$
\epsilon \simeq \frac{E}{4}\cdot\frac{m_e^2}{E_1 E_2 + \theta_1\theta_2} + \chi\,\frac{E^2}{4E_0}
$$
- **$\chi<0$ ($c_\gamma>c_p$)**：$E>E_c$ 时光子可自发衰变 → 河外光子传播受阻 → 观测 >20 TeV 河外光子 [328,329] 约束 **$E_0\gtrsim M_{\rm Pl}$** 或 $(c_i^2-c^2)>\sim-2\times10^{-17}$
- **$\chi>0$**：$E>E_c$ 时 $\epsilon$ 增长 → 光子传播不受阻 → 可观测 >100 TeV 来自 >100 Mpc 的河外光子

[FACT] **时间色散**：
$$
\Delta t \simeq \frac{d}{c}\left(\frac{E}{E_0}\right) \simeq 1\left(\frac{d}{100\ {\rm Mpc}}\right)\left(\frac{E}{{\rm TeV}}\right)\left(\frac{E_0}{M_{\rm Pl}}\right)^{-1}\ {\rm s}
$$
- Mrk 421 >2 TeV $\gamma$ 在 300 s 内到达 → $E_0>4\times10^{16}$ GeV [331]
- HEGRA 若观测到 >200 TeV GRB $\gamma$ 在 200 s 内 → $E_0\simeq M_{\rm Pl}$

[FACT] **快子中微子 (Kostelecký [333])**：$\nu_e$ 为 tachyon。核内质子可衰变 $p\to n+e^++\nu_e$，阈值 $E_{\rm th}=m(A,Z)[m(A,Z\pm 1)+m_e-m(A,Z)]/|m_{\nu_e}|$。自由质子：$E_{\rm th}\simeq 1.7\times10^{15}/(|m_{\nu_e}|/{\rm eV})$ eV。Ehrlich [334] 主张 $m_{\nu_e}^2\simeq -(0.5\ {\rm eV})^2$ 可同时解释 knee 与高能端。

[CRITIQUE] 与氚 $\beta$ 衰变实验最佳拟合值 $m_{\nu_e}^2<0$ 一致（但最可能是实验未解决的系统问题），不过 $|m_{\nu_e}^2|$ 值通常比 fit knee 所需大。预测 knee 附近有 neutron 谱线 [336]。

**关键参数**：$(c_p-c)<10^{-23}$；$(g_p/g_\gamma)-1<10^{-19}$；$E_0>4\times10^{16}$ GeV (Mrk 421)；$M_{\rm Pl}=2.4\times10^{18}$ GeV；$\tau_E\propto E^{-2}/E^{-1}/E^{-1/3}$ (rectilinear/Bohm/Kolmogorov)。

**引用页码**：*Phys. Rep.* 320 (1999), pp. 16–40。