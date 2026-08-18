# 3. Test-Particle 扩散激波加速（DSA）

> 本章属于：[[02_cosmic-ray-origins/0005_amato-2014/literature_analysis/00_overview.md|The origin of galactic cosmic rays (Blasi 2013 §3 & Amato 2014 §2)]]
>
> 上一章：[[02_cosmic-ray-origins/0005_amato-2014/literature_analysis/02_snr_paradigm.md|02_snr_paradigm.md]]
>
> 下一章：[[02_cosmic-ray-origins/0005_amato-2014/literature_analysis/04_nl_dsa.md|04_nl_dsa.md]]

## 3.1 本节核心内容

Blasi §3 与 Amato §2 是**对同一段经典 test-particle DSA 理论**的两种讲解—— Blasi 更详尽（含无碰撞激波形成、粒子在磁场中的输运基本推导），Amato 更精炼（直接从 Fermi I 概念切入）。

## 3.2 SNR 动力学演化参数（Blasi §3）

**[FACT]** 抛射物质速度（Blasi 式 (4)）：

$$V_{ej} = 10000\, E_{51}^{1/2}\, M_{ej,\odot}^{-1/2}\,\mathrm{km/s}$$

**[FACT]** ISM 声速（Blasi 式 (5)）：

$$c_s = \sqrt{\frac{\gamma_g kT}{m_p}} \approx 11\left(\frac{T}{10^4\,\mathrm{K}}\right)^{1/2}\,\mathrm{km/s}$$

其中 $\gamma_{\rm g}$ = 5/3（绝热指数）

**[FACT]** 激波 Mach 数（Blasi 式 (6)）：

$$M_s = \frac{V_{ej}}{c_s} \approx 900\, E_{51}^{1/2}\, M_{ej,\odot}^{-1/2}\left(\frac{T}{10^4\,\mathrm{K}}\right)^{-1/2}$$

**[FACT]** Sedov-Taylor 半径与起算时刻（Blasi 式 (7)-(8)）：

$$R_{ST} \approx 2\, M_{ej,\odot}^{1/3}\left(\frac{n_{ISM}}{1\,\mathrm{cm^{-3}}}\right)^{-1/3}\,\mathrm{pc}$$

$$T_{ST} \approx 200\, M_{ej,\odot}^{5/6}\, E_{51}^{-1/2}\left(\frac{n_{ISM}}{1\,\mathrm{cm^{-3}}}\right)^{-1/3}\,\mathrm{yr}$$

**[FACT]** Amato 给出相同量级的结果（Amato 式 (5)）：$T_{ST} = 200\, M_{ej\odot}^{5/6} E_{51}^{-1/2} n_1^{-1/3}$ yr

## 3.3 无碰撞激波（Blasi §3.1）

**[FACT]** SNR 激波是**无碰撞激波（collisionless shocks）**——粒子间库仑碰撞不足以在激波宽度内热化等离子体，而是靠**集体电磁不稳定性**（Weibel、streaming 等）耗散。

**[FACT]** Alfvén Mach 数条件（Blasi 式 (9)）：

$$v \ll c \to M_A = \frac{v}{v_A} \ll 1.3\times 10^5\, n_{\mathrm{cm^{-3}}}^{1/2}\, B_{\mu G}^{-1}$$

**[FACT]** 热化时标层级（Spitzer 1962，Blasi 式 (10)-(12)）：

$$\tau_{eq} = \frac{3 m_1 m_2 k_B^{3/2}}{8(2\pi)^{1/2} n q^4 \ln\Lambda} \left(\frac{T_1}{m_1} + \frac{T_2}{m_2}\right)^{3/2}$$

典型：
- 电子-电子 $\tau_{ee} \approx 1200\,(n/\mathrm{cm^{-3}})^{-1} (T_e/10^8\,\mathrm{K})^{3/2}$ yr
- 质子-质子 $\tau_{pp} \approx 2.3\times 10^6\,(n/\mathrm{cm^{-3}})^{-1} (T_p/10^8\,\mathrm{K})^{3/2}$ yr

**[FACT]** 电子-质子热平衡时标**远超 SNR 年龄**（Blasi）→ 无碰撞激波后电子温度远低于质子温度：

$$kT_e \approx \frac{3}{2} m_e v^2 = \frac{m_e}{m_p} kT_p$$

**[FACT]** 强激波下游温度（Blasi 式 (21)）：

$$kT_2 = \frac{3}{16} m_p u_1^2 = 5.6\times 10^8 \left(\frac{V_{sh}}{5000\,\mathrm{km/s}}\right)^2\,\mathrm{K}$$

**[FACT]** 强激波下游的质子/电子温度：

- $kT_p \sim 15\, v_8^2$ keV（$v_{8}$ = V_sh/($10^{8}$ cm/s)）
- $T_e \sim 80\, v_8^2$ eV

## 3.4 粒子在磁场中的输运（Blasi §3.2）

**[FACT]** 均匀磁场 $B_{0}$ = $B_{0}$ẑ 中的粒子轨迹（Blasi 式 (22)-(24)）：

$$v_x(t) = v_\perp \cos(\Omega t + \phi)$$
$$v_y(t) = -v_\perp \sin(\Omega t + \phi)$$
$$v_z(t) = v_\parallel = v\mu = \mathrm{const}$$

回旋频率 $\Omega = qB_0/(mc\gamma)$

**[FACT]** 引入 Alfvén 波扰动（$\delta$B 沿 x̂ 偏振），共振散射率（Blasi 式 (28)）：

$$\left\langle \frac{\Delta\mu\,\Delta\mu}{\Delta t} \right\rangle_\phi = \pi \Omega^2 \left(\frac{\delta B}{B_0}\right)^2 \frac{(1-\mu^2)}{\mu}\,\delta\!\left(k - \frac{\Omega}{v\mu}\right)$$

**[FACT]** 空间扩散系数（Blasi 式 (32)）：

$$D(p) = \frac{1}{3} v(v\tau) \simeq \frac{1}{3}\, r_L\, v\, \left(\frac{k\,P(k)}{B_0^2/8\pi}\right)^{-1} = \frac{1}{3}\, r_L\, v\, \frac{1}{F}$$

**[FACT]** 量级估计：H$^{2}$/D(p) ~ $10^{7}$ yr 对应 D ~ $10^{29}$ cm$^{2}$/s → $\delta$B/B ~ $6\times10^{-4}$（共振波长处），即**微量的 Alfvén 波功率即可满足银河系尺度上的 CR 约束**。

## 3.5 DSA 输运方程（Blasi §3.3 / Amato §2）

**[FACT]** 平行静止激波的扩散-对流方程（Blasi 式 (34)；Amato §3 引用同类方程）：

$$u\frac{\partial f}{\partial z} = \frac{\partial}{\partial z}\left(D\frac{\partial f}{\partial z}\right) + \frac{1}{3}\frac{du}{dz}\,p\frac{\partial f}{\partial p} + Q$$

各项含义：
- 左端：平流
- 右端第 1 项：空间扩散
- 右端第 2 项：流体压缩对粒子的效应
- Q：注入项

**[FACT]** 在激波处积分（Blasi 式 (36)）：

$$\left[D\frac{\partial f}{\partial z}\right]_2^1 + \frac{1}{3}(u_2-u_1)\,p\frac{df_0}{dp} + q_0(p) = 0$$

**[FACT]** 最终得到在激波面的分布函数（Blasi 式 (40)-(41)）：

$$f_0(p) = \frac{3r}{r-1}\,\frac{\eta n_1}{4\pi p_{inj}^2}\left(\frac{p}{p_{inj}}\right)^{-\frac{3r}{r-1}}$$

$$\boxed{\alpha = \frac{3r}{r-1}}$$

- r 为压缩比，强激波时 r → 4 → $\alpha$ → 4
- 动量谱 p$^{-4}$ 对相对论粒子等价于能量谱 E$^{-2}$
- 亚相对论：n($\epsilon$) ∝ $\epsilon^{\rm -3}$/$^{2}$
- 谱形状**不依赖于扩散系数**（test-particle 的核心结果）

**[FACT]** 压缩比（Blasi 式 (33)；Amato 式 (2)）：

$$r = \frac{4 M_s^2}{M_s^2 + 3} \xrightarrow{M_s\gg 1} 4$$

## 3.6 加速时间 vs 最大能量（Blasi §3.4 / Amato §2）

**[FACT]** 每次穿越激波的能量增益（Blasi 式 (44)）：

$$\left\langle \frac{\Delta E}{E}\right\rangle = \frac{4}{3}\beta$$

其中 $\beta$ = ($u_{1}$−$u_{2}$)/c → **一阶 Fermi 加速**（∝ $\beta^{1}$，对比二阶 Fermi 的 ∝ $\beta^{2}$）

**[FACT]** 加速时间（Blasi 式 (46)-(47)；Amato 式 (3)）：

$$\tau_{acc} = \frac{3}{u_1-u_2}\left(\frac{D_1}{u_1} + \frac{D_2}{u_2}\right) \approx \frac{3}{u_1-u_2}\int_0^p \frac{dp'}{p'}\left(\frac{D_1(p')}{u_1} + \frac{D_2(p')}{u_2}\right)$$

**[FACT]** 三种最大能量定义（Blasi §3.4）：

| 定义 | 条件 | 适用场景 |
|---|---|---|
| (1) 时标 | $\tau_{\rm acc}$(E_max) = $\tau_{\rm SNR}$ | 主要，粒子在 SNR 年龄内被加速 |
| (2) 逃逸 | D(p_max)/V_sh ≈ $\chi$ R_sh，$\chi$ < 1 | Sedov-Taylor 相 |
| (3) 几何 | r_L(p_max) = R_sh | 严格上界，高估 ~c/V_sh |

**[FACT]** 关键约束（Blasi 式 (48)-(50)）：

$$\frac{1}{3} r_L(p_{max}) c\, F(k_{min}) \approx \tau_{SNR}$$

$$r_L(p_{max}) = 1\,\mathrm{pc}\, \left(\frac{E}{10^{15}\,\mathrm{eV}}\right) B_{\mu G}^{-1}$$

**[FACT]** **PeVatron 条件**（Blasi）：为使 SNR 能到 $10^{15}$ eV，必须 $F(k_{min}) \gg 1$，即 $\delta$B/$B_{0}$ ≫ 1 → **必须磁场放大 ~10–100 倍**。若用 ISM 的 B/C 反推扩散系数，则 E_max 远不及 GeV。

**[FACT]** Amato 明确给出：若 ISM 湍流（Kolmogorov）不放大 → $E_{Max} \sim$ few GeV；若场放大到 $\delta$B ≈ $B_{0}$ → $E_{Max} \sim 10^4$–$10^5$ GeV，仍差 30–100 倍；因此**放大是必需的**。

## 3.7 Test-Particle 理论的已知局限（Blasi §3.4 尾）

**[FACT]** 三种已知偏离：
1. 稳态假设 → 无最大能量的问题；
2. $\delta$B/$B_{0}$ ≫ 1 时准线性理论失效；
**3. 各向异性/垂直扩散在 $\delta$B/$B_{0}$ → 1 时成为主导（NLGC 理论，Matthaeus 2003）。

**[CRITIQUE]** Test-Particle DSA 理论的三种局限并非平等——第1条（稳态假设）是根本性框架限制，导致无法处理时变演化 SNR（如爆发早期）；第2条（QLT 失效）是技术性假设，在强磁场放大（$\delta$B/$B_0$ ≫ 1）真实 SNR 中确实失效，但 Blasi 本人在 §3.1 已知这个问题；第3条（垂直扩散）则是一个至今未完全解决的开放问题——NLGC 理论本身在强各向异性条件下是否自洽仍有争议。[CRITIQUE]

**[INTERPRETATION]** 值得注意的是：Amato 2014 在 §2 中以更简洁的方式讨论同样的局限性，而 Blasi 2013 在 §3.4 用了更多篇幅展开这种"理论缺陷清单"。两篇综述都承认 test-particle 近似的局限，但都没有给出令人信服的替代方案——这恰恰说明 NLDSA 理论在强放大 Regimes 下的自洽性问题至今未解决。这也是为何 caprioli-2014 的 PIC 数值模拟如此重要：它不依赖于 QLT 近似。|

**[INTERPRETATION]** 这些局限正是**过渡到 NLDSA** 的动机，见第 4 章。