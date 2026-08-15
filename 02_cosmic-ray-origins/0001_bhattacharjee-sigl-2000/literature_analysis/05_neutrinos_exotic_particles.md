> 本章属于：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/00_overview.md|Bhattacharjee & Sigl (1999), *Phys. Rep.* 320, 1–150]]
>
> 上一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/04_propagation_gzk.md|04_propagation_gzk]]
>
> 下一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/06_magnetic_fields_constraints.md|06_magnetic_fields_constraints]]
---

# 5. Origin of UHECR: Acceleration Mechanisms and Sources (§5, p. 40–48)

[FACT] §5 聚焦"bottom-up" 路径：以 DSAM (Diffusive Shock Acceleration Mechanism) 为基准估计最大可加速能量，用 Hillas 判据筛选候选源（AGN / 射电星系 / 脉冲星），并以 GRB 作为可能的极端候选，共 3 个子节（5.1–5.3）。

[INTERPRETATION] §5 是 §3 一般性讨论的"具体候选源"实现——把 §3 中"激波压缩比决定谱指数""Hillas 判据筛源"两条原理应用到具体天体物理环境。

---

## 5.1 Maximum Achievable Energy within DSA Mechanism

> **DSA 机制内可加速的最大能量**

[FACT] DSAM 加速机制的简单模型推导，给出 $E_{\rm max}$ 的"benchmark"估计（公式 43–50）。

[FACT] **基本框架 (公式 43–46)**：
$$
\frac{dE}{dt} = \frac{E}{T_{\rm acc}} \qquad (43)
$$
$$
q = 1 + T_{\rm acc}/T_{\rm esc} \qquad (44)
$$
$$
T_{\rm acc} = \frac{3}{(u_1-u_2)}\cdot\left(\frac{D_1}{u_1}+\frac{D_2}{u_2}\right) \qquad (45)
$$
$$
D_1, D_2 \sim \lambda/3 > gE/(3ZeB) \qquad (46)
$$
- 非相对论激波 $g=1$；相对论激波 MC 模拟 $g\simeq 40$ [342]，但有额外的 ~10× 补偿因子（高倾角）和 ~13.5×（平行）

[FACT] **最小 $T_{\rm acc}$ (公式 47)**：
$$
T_{\rm acc} \gtrsim \frac{g}{2.25}\cdot\frac{E}{ZeB}
$$

[FACT] **谱指数 (公式 48)**：
$$
q(E>E_{\rm diff}) \sim 1 + \frac{E}{2.25\,E_{\rm diff}}, \qquad E_{\rm diff}\equiv ZeBR/g
$$

[FACT] **最大能量（$q=3$ 时, benchmark 估计, 公式 49）**：
$$
E_c \equiv E_{q=3} \sim 10^{17}\cdot Z\cdot(R/{\rm kpc})\cdot(B/\mu{\rm G})\ {\rm eV}
$$
- 假设 $B$ 平行激波法线

[FACT] **倾斜磁场额外漂移加速 (公式 50)**：
$$
E_{\rm max} = Ze\,u_1\,B\,R \sim 10^{18}\cdot Z\,u_1\cdot(R/{\rm kpc})\cdot(B/\mu{\rm G})\ {\rm eV}
$$
- 比 (49) 高 ~10×（$u_1\to c$ 时），但需要特殊条件（plasma 效应使 E 场更小）

[FACT] **谱斜率**：
- 简单 DSAM：$q=(r+2)/(r-1)$，$r<4\to q>2$（典型 ~2.3–2.4）
- 强激波 back-reaction：$q=1.5$（harder）[337]
- 超相对论激波 ($\Gamma\to\infty$)：$q\simeq 2.2$（softer）[338]
- 相对论 blast wave：第一次 crossing ~$\Gamma^2$ 能量增益，后续 cycles ~2× [339]

---

## 5.2 Source Candidates for UHECR

> **UHECR 的候选源**

[FACT] 无论具体加速机制如何，只有满足**Hillas 判据**的天体物理源才能承担 UHECR 加速。

**Hillas 判据 (公式 51)**：
$$
(B/\mu{\rm G})\cdot(R/{\rm kpc}) > 2\cdot(E/10^{18}\ {\rm eV})\cdot 1/(Z\,\beta)
$$
- 加速区尺寸 $R>$ 回旋半径 $2\,r_g$
- **Hillas 图 (Fig. 25)**：只有 AGN、射电星系、脉冲星等少数源满足 ~$10^{20}$ eV 加速条件

### 5.2.1 AGNs and Radio-Galaxies

> **AGN 与射电星系**

[FACT] **支持 AGN 作为 UHECR 源的证据**：
1. **Mrk 421, Mrk 501** (BL Lac) 在 >10 TeV $\gamma$ 被观测 → 可由质子光 $\pi$ 产生解释（vs IC）
2. EGRET diffuse $\gamma$-ray 能量密度 ~ E$^{-2}$ 质子注入谱到 $10^{20}$ eV 所需能量 → 支持河外质子加速

[FACT] **反对 AGN 核心作为 EHECR 源 (Norman et al. [13])**：
- AGN 核心典型 $R\sim 0.02$ pc, $B\sim 5$ G → 公式 (49)：$E_c\sim 10^{19}$ eV
- **主要问题**：中心引擎内辐射场强烈 → 加速质子通过 photo-pion 严重衰减
- 同时考虑加速与能量损失 → 质子或核在 **$E>\sim 10^{16}$ eV 无法逃出核心**
- 中子假设也不行（中子本身也受 photo-pion 衰减）

[FACT] **FR-II 射电星系 hot spots** — **最有希望的加速器**：
- Hot spot 周围 soft photon 密度低 → photo-pion 损失不显著
- 若 $B$ 场足够强 → **$E_{\rm max}$ 可达 ~$10^{21}$ eV**
- 但**主要问题**：hot spot 距地球大 cosmological 距离 >100 Mpc [26] → GZK 效应使其粒子无法存活
- **结论**：射电星系 hot spots 可能是 UHECR (>$10^{17}$ eV) 源，但**难以解释 $10^{20}$ eV 以上事件**

[FACT] **Boldt–Ghosh [27] 建议**：自旋超大质量黑洞（不活跃 quasar 遗迹）事件视界附近加速 → $E_{\rm max}\sim 10^{21}$ eV；本地 50 Mpc 内足够多候选 → 可解释 EHECR 通量。

[FACT] **Waxman-Bahcall Bound [218]**：比较 UHECR 通量 (E ~$10^{19}$ eV) → 对 diffuse $\nu$ 通量给出更强上界。Mannheim, Protheroe, Rachen [353] 声称存在 loophole（仅 $10^{16}$–$10^{18}$ eV 适用）；Bahcall & Waxman [352] 反驳 → 认为 bound **robust**。**不适用于**：对质子光学厚的源（如 AGN 核心）；**不适用于 top-down**（$\nu$ 是初级而非次级）。

### 5.2.2 Pulsars

> **脉冲星**

[FACT]
- **简单脉冲星直接加速**：~$10^{21}$ eV 势差，但 **pair-cascade 短路** → 实际 <$10^{15}$ eV
- **吸积盘**：能量损失限制 ~$10^{15}$ eV
- **Magnetar** (SGR 1900+14)：表面 $B\sim 10^{15}$ G → 能量预算提高 2–3 个量级，但损失问题未解决
- **Fe 离子 MHD 风** [355]：新形成强磁化脉冲星（初始 $P<4(B_s/10^{13}\ {\rm G})^{1/2}$ ms）→ 可加速 Fe 离子 >$10^{20}$ eV，预言 EHECR 组成以 Fe 为主（可检验）

### 5.2.3 Other Candidate Sources

> **其他候选源**

| 源 | $E_{\rm max}$ | 备注 |
|---|---|---|
| 银河风终止激波 | 可能达 UHE | 依赖 $B$ |
| 星系碰撞激波 | ~UHE | [357] |
| 星系团吸积/合并激波 | UHE | [358,359] |
| 结构形成大尺度激波 | UHE | [13] |

[FACT] 一般难以超过 $10^{20}$ eV。

---

## 5.3 A Possible Link Between GRBs and Sources of $E>10^{20}$ eV Events

> **GRB 与 $E>10^{20}$ eV 事件源的关联可能性**

[FACT] **基本动机**：
- UHECR 所需能量释放率 ~ GRB $\gamma$ 辐射率 [361,362]
- 预言谱与观测谱 E > ~$10^{19}$ eV 一致（质子注入 E$^{-2.3\pm 0.5}$ [288]，Fermi 加速）
- **主要问题**：GZK 距离内 (<50 Mpc) 宇宙学 GRB 率 ~**每世纪一次** → 观测 UHECR 时间窗内概率极低，除非磁场导致 > 百年时间延迟

[FACT] **磁场下限 (公式 52)**：
$$
B \gtrsim 10^{-10}\cdot(E/10^{20}\ {\rm eV})\cdot(d/30\ {\rm Mpc})^{-1}\cdot(l_c/1\ {\rm Mpc})^{1/2}\ {\rm G}
$$
- $N$ 个不同到达方向 → bound 增强 $N^{1/2}$ 倍
- 最近观测各向同性 [8] + EGMF 上界 [363] → 已构成挑战
- GRB 距离标度变大 → 能量要求更苛刻 [363]

[FACT] **Dissipative Wind Model**：光 + $e^+e^-$ + 少量重子风 → 超相对论 Lorentz 因子 $\gamma\gg 1$。耗散半径 $r_d$ 处 internal shock → 部分动能转 $\gamma$ 射线（GRB）。耗散产生 near-equipartition 磁场 → 二阶 Fermi 加速。

**三重条件**：
1. **加速时间 < 膨胀时间 (公式 53)**：
$$
B \gtrsim (E/{\rm erg}) \simeq 3\times10^4\cdot(E/10^{20}\ {\rm eV})\cdot(r_d/10^{13}\ {\rm cm})^{-1}\ {\rm G}
$$
2. **$\pi$ 产生损失 < 加速 (公式 54)**：
$$
B \gtrsim 20\cdot(L_\gamma/10^{51}\ {\rm erg/s})\cdot(r_d/10^{13}\ {\rm cm})^{-2}\cdot(\gamma/300)^{-2}\ {\rm G}
$$
3. **同步损失 < 加速 (公式 55)**：
$$
B \lesssim 3\times10^5\cdot(\gamma/300)^2\cdot(E/10^{20}\ {\rm eV})^{-2}
$$

**同时满足**：需 $r_d>10^{12}(\gamma/300)^{-2}(E/10^{20}\ {\rm eV})^3$ cm（公式 56），以及 **$\gamma>40\,(E/10^{20}\ {\rm eV})^{3/4}\,(t_{\rm GRB}/{\rm s})^{-1/4}$**。

[FACT] **次级产物**：
- **$\nu$ 通量**：~$10^{14}$ eV，数十事件/km$^3$ 中微子望远镜 [365,370]；>$10^{19}$ eV 可被 AIRWATCH/MASS 探测 [366]
- **MACRO 上界**：每个 GRB $0.87\times10^{-9}$ cm$^{-2}$ $\mu$ 通量 [372]
- **同步辐射信号**：~1% 总 burst 能量在 10 MeV（GLAST 可探测）；数百 GeV（IACT 可探测）；~TeV afterglow [367–369]
- 若 GeV cascade 解释 diffuse $\gamma$-ray → 每个 GRB 释放 ~$10^{56}$ erg，$\gamma>500$

[FACT] **Waxman-Bahcall 与 Top-down 的区别**：
- Bottom-up（AGN/Radio/GRB）：$\nu$ 是次级产物，受 diffuse GeV $\gamma$-ray background 约束
- Top-down：$\nu$ 是初级，通量可显著高于核子 → 但仍受 diffuse GeV $\gamma$ 约束（§4.3.1）

[CRITIQUE] 与 1999 年后对照：
- [FACT] **AGN 核心 vs hot spot** 的争论在 Auger 时代得到部分澄清：UHECR 到达方向与**近邻 AGN/星暴星系**的相关（Auger 2017–2020），暗示**河外离散源是 UHECR 主要成分**
- [FACT] **Fe 组成**：Auger 显示 E > ~$10^{19.5}$ eV 组成**变重**（倾向 Fe），支持 §5.2.2 中 magnetar Fe 风模型或类似的重核加速源
- [CRITIQUE] **GRB-UHECR 关联**：Auger 未发现显著 GRB 关联；IceCube 也未发现 UHE $\nu$ 与 GRB 关联 → 弱化了 §5.3 的 GRB 情景

---

## 关键数值速查

| 量 | 值 |
|---|---|
| DSAM $E_c$ (benchmark, 公式 49) | $10^{17}\,Z\,(R/{\rm kpc})(B/\mu{\rm G})$ eV |
| 漂移加速 $E_{\rm max}$ (公式 50) | $10^{18}\,Z\,u_1\,(R/{\rm kpc})(B/\mu{\rm G})$ eV |
| Hillas 判据 (公式 51) | $B(\mu{\rm G})\cdot R({\rm kpc}) > 2\cdot(E/10^{18}\ {\rm eV})/(Z\beta)$ |
| AGN 核心 $E_c$ | ~$10^{19}$ eV（但损失使可逃出 <$10^{16}$ eV） |
| FR-II hot spot $E_{\rm max}$ | 可达 ~$10^{21}$ eV（若 $B$ 足够） |
| GRB 条件 $\gamma >$ | $40\,(E/10^{20}\ {\rm eV})^{3/4}\,(t_{\rm GRB}/{\rm s})^{-1/4}$ |

**引用页码**：*Phys. Rep.* 320 (1999), pp. 40–48。