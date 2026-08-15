> 本章属于：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/00_overview.md|Bhattacharjee & Sigl (1999), *Phys. Rep.* 320, 1–150]]
>
> 上一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/02_observed_cosmic_rays.md|02_observed_cosmic_rays]]
>
> 下一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/04_propagation_gzk.md|04_propagation_gzk]]
---

# 3. Origin of Bulk of the Cosmic Rays: General Considerations (§3, p. 10–16)

[FACT] §3 为后续 §5（加速起源, bottom-up）与 §6（衰变起源, top-down）做一般性铺垫，共 3 个子节：能量学（§3.1）、银河 vs 河外起源（§3.2）、加速机制与可能源（§3.3）。

[INTERPRETATION] 作者的意图：膝点以下 CR 起源已基本解决（SNR + DSAM），但 UHECR（>~$10^{17}$ eV）是完全未解决的独立问题。

---

## 3.1 Energetics

> **能量学**

[FACT] 银河 CR 能量密度主要集中于 1–10 GeV 能量区间。E ≲ 1 GeV 与太阳活动正相关（太阳起源）；E > 1 GeV 与太阳活动**反相关** → 太阳系外起源（屏蔽效率随太阳风增强）。

[FACT] **银河 CR 穿越星际气体的平均柱密度 (公式 3)**：
$$
X(E) = \rho_{\rm g}\cdot t_{\rm CR}(E) \simeq 6.9\cdot\left(\frac{E}{20Z\ {\rm GeV}}\right)^{-0.6}\ {\rm g\,cm}^{-2}
$$
- $\rho_{\rm g}$：星际气体平均密度；$Z$：CR 平均电荷数
- 数据来源：银河 CR 次级/初级丰度比 [114]

[FACT] **银河系总 CR 光度**：
$$
L_{\rm CR} = \frac{4\pi}{c}\int dE\int dV\,t_{\rm CR}(E)^{-1}\,E\,j(E)
$$

| 量 | 值 |
|---|---|
| $u_{\rm CR}$（CR 能量密度） | ~1 eV cm$^{-3}$ |
| $M_{\rm g}$（银河气体总质量） | ~$4.8\times10^9\ M_\odot$ |
| $L_{\rm CR}$ | ~$1.5\times10^{41}$ erg s$^{-1}$ |
| $L_{\rm CR}/L_{\rm SN}$（占超新星动能比） | ~10% |

[FACT] 结论：从能量学看，超新星可解释膝点以下 CR 的大部分能量。

[FACT] **能量密度等价关系 (公式 5)**：
$$
u_{\rm CR} \sim \frac{B^2}{8\pi} \sim \frac{1}{2}\,\rho_{\rm g}\,v_t^2
$$
- $B \sim 10^{-6}$ G（银河磁场）；$v_t$：气体湍流速度
- 物理解释：相对论性 CR、磁场与气体流动之间的压力平衡
- [INTERPRETATION] 若此关系在河外空间也成立 → 河外 CR 能量密度会明显小于银河系 → 进一步支持银河起源

---

## 3.2 Galactic versus Extragalactic Origin of the Bulk of the CR

> **银河系 vs 河外起源**

[FACT] **三大支持银河起源的证据**：

1. **能量学**（§3.1）：$L_{\rm CR} \sim 10\%\,L_{\rm SN}$。
2. **SMC $\gamma$ 射线上界** [FACT]：CR 与气体相互作用产生 $\pi^0$ 衰变 $\gamma$ 射线 [118]；SMC 观测上界比\"宇宙 CR 密度均匀\"假设下的预言低一个量级 [119] → SMC 处 CR 密度比本地银河低至少几倍 → CR 不是宇宙均匀的。
3. **银河系 CR 梯度**：若银河起源，CR 强度应随银心距离下降 → 反映在次级 $\gamma$ 射线中 [120–122]；观测结果尚不完全确定 [123]。
4. **各向异性**：<$10^{14}$ eV 各向异性 ~$10^{-3}$，统计显著，基本能量无关 → Compton-Getting 效应 [126]；>$10^{18}$ eV 无显著与银道面相关的各向异性 → **暗示高能端河外起源**。
5. **电子成分**：>~$10^{11}$ eV 电子因同步辐射/IC 损失，射程 < $t_{\rm CR}$ → 无可置疑的银河起源（占强子流 ~1%）。

[FACT] **Leaky Box 模型**：用 CR 保留时间 $t_{\rm CR}$ 代替扩散项；拟合得到 $t_{\rm CR} \sim 10^7$ yr（E < $10^{16}$ eV），能量依赖弱。
- 膝点解释：磁去约束效应（磁约束减弱 → 逃逸加速 → 谱变陡）；或最大加速能量 ∝ Z（电荷）→ 谱变陡。
- 另有解释：膝点可能由**单一强源**贡献 [127]。

---

## 3.3 Acceleration Mechanisms and Possible Sources

> **加速机制与可能源**

[FACT] 存在两种主要加速机制：

**（1）直接加速（电场）**：如旋转磁中子星（脉冲星）、吸积盘磁场。缺点：难以自然产生幂律谱；细节争议多。Colgate [128] 反驳：幂律谱不必然来自 Fermi 加速，只要\"少数粒子的能量份额增加\"配合\"剩余粒子数份额显著减少\"即可。

**（2）统计 (Fermi) 加速**：
- **二阶 Fermi (1949)**：CR 与随机运动磁云碰撞 → 平均能量增益 ∝ $(u/c)^2$；效率低；加速时间 ≫ 逃逸时间 (~$10^7$ yr)；谱指数依赖云速度 → 多源叠加不再幂律。
- **一阶 Fermi（DSAM, Diffusive Shock Acceleration Mechanism）** [FACT]：粒子与激波面前后多次穿越；每次穿越的平均能量增益 ∝ $u$（激波相对速度一阶项）；**DSAM 的关键特征**：谱指数只依赖**激波压缩比**，与激波速度无关；已被太阳系 bow shock 原位观测强力支持 [130–132]。

[FACT] **加速最大能量 $E_{\rm max}$ 的 Hillas 限制**：加速位点处粒子存在 $E_{\rm max}$，受以下任一限制：
- 源尺寸限制：源 > 粒子回旋半径
- 时间限制：加速时间 < 激波寿命 < 最短能量损失时间

[FACT] **SNR 加速的旁证**：B/C 比例在恒星大气中随金属丰度不变 → C、N、O 的 CR 必须通过散裂在 SNR 中产生 [133]。SNR 中观测到 X 射线同步辐射，电子能量 ~100 TeV → 支持 SNR 加速 [138]。SNR 质子与周围物质作用产生 $\pi^0$ → 次级 $\gamma$ 射线（预言 [139–144]），但观测上尚无确凿探测 [145,146]。**SNR 情形不能解释 UHECR**，UHECR 应作为独立成分存在。

[FACT] **替代模型综述**：

| 模型 | 主张 | 备注 |
|---|---|---|
| Biermann [16] | 全部来自一阶 Fermi：SNR（ISM，$10^{15}$ eV）、SNR（恒星风，$10^{17}$ eV）、射电星系热斑（最高） | 声称通过所有观测检验 |
| Colgate [128] | 扭曲磁场的重联加速，可作用到最高能 | 谱指数不确定 |
| Plaga [148] | 全部宇宙线河外起源，银河\"磁通陷阱\"积累 | 称 SMC $\gamma$ 射线不是合适检验 |
| Dar et al. [149] | 全部银河系起源，\"微类星体\"（microblazars） | 同源可产生河外 GRB |
| 真空涨落加速 [150–152] | 极推测 | 预言 E$^{-1}$ 硬谱 → 高能端通量过度预言 [FACT, Eq. 6] |

[FACT] **真空涨落加速率 (公式 6)**：
$$
\Omega \equiv \frac{dE}{dt} \simeq \frac{3}{5\pi}\,\Gamma^2\,\omega_0/ m_N \lesssim 10^{13}\ {\rm eV\,s}^{-1}
$$
- $\Gamma = 2e^2/3m_N$（辐射阻尼常数）；$\omega_0$ 小于夸克 Compton 频率

[CRITIQUE] 1999 年后，**Auger 数据**（2017 起）显示 UHECR 谱在 ~$5\times10^{19}$ eV 处有明显陡化（与 GZK 一致），且 E > $5.7\times10^{19}$ eV 事件的到达方向与**近邻星团（尤其是 Centaurus A）**有显著相关——部分支持 §5.2.1 中的射电星系/AGN 类 Bottom-up 模型。Top-down 场景（§4.3、§6–7）对观测约束越来越严格（IceCube 未发现对应中微子，Fermi-LAT 对 diffuse $\gamma$-ray 有更强限制）。

**引用页码**：*Phys. Rep.* 320 (1999), pp. 10–16。