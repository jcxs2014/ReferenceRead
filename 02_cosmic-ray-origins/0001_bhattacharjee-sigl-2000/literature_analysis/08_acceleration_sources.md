---
chapter: 8
title: "Bottom-up Acceleration and Sources"
pages: "40–48"
sections:
  - "5.1 Maximum Achievable Energy within Diffusive Shock Acceleration Mechanism"
  - "5.2 Source Candidates for UHECR"
  - "5.3 A Possible Link Between Gamma-Ray Bursts and Sources of E > 10²⁰ eV Events?"
related_chapters:
  prev: 07_source_search_transport
  next: 09_topdown_basic_fragmentation
status: done
---

> 本章属于：Bhattacharjee & Sigl (1999), *Phys. Rep.* 320, 1–150
>
> 上一章：`07_source_search_transport.md`
>
> 下一章：`09_topdown_basic_fragmentation.md`

# 8. Bottom-up Acceleration & Sources (§5, p. 40–48)

[FACT] §5 是全文对 bottom-up 加速场景最系统的回顾：从 DSAM 加速机制的基本推导出发，给出 $E_{\rm max}$ 的基准估计与 Hillas 判据，然后逐一检验 AGN / 射电星系 / 脉冲星 / GRB 等候选源的可行性。

[INTERPRETATION] §5 的核心论证线是：**Hillas 判据过滤 → 仅剩 AGN / 射电星系 / 脉冲星 → AGN 核心被能量损失排除 → FR-II hot spots 是最有希望但受距离约束 → 脉冲星除 magnetar 与 Fe 风模型外难以突破 $10^{15}$ eV → GRB 需大磁场延迟**。结论是 bottom-up 场景面临"动力学 + 距离"双重困难，为 §6 的 top-down 引出动机。

---

## 5.1 Maximum Achievable Energy within Diffusive Shock Acceleration Mechanism

[FACT] §5.1 系统推导 DSAM 最大能量。

### 5.1.1 基本框架

> **DSAM 基本框架**

[FACT] 加速基础方程（公式 43–46）：

$$
\frac{dE}{dt} = \frac{E}{T_{\rm acc}}\;\;\text{(43)},\qquad q = 1 + \frac{T_{\rm acc}}{T_{\rm esc}}\;\;\text{(44)}
$$
$$
T_{\rm acc} = \frac{3}{(u_1 - u_2)}\left(\frac{D_1}{u_1} + \frac{D_2}{u_2}\right)\;\;\text{(45)},\qquad D_{1,2} \sim \lambda/3 > \frac{gE}{3ZeB}\;\;\text{(46)}
$$

- 非相对论激波 $g=1$；相对论激波 MC 模拟 $g \simeq 40$ [342]，但有额外的 ~10× 补偿因子（高倾角）和 ~13.5×（平行）。

[FACT] **最小 $T_{\rm acc}$（公式 47）**：

$$
T_{\rm acc} \gtrsim \frac{g}{2.25}\cdot\frac{E}{ZeB}
$$

[FACT] **谱指数（公式 48）**：

$$
q(E > E_{\rm diff}) \sim 1 + \frac{E}{2.25\,E_{\rm diff}},\quad E_{\rm diff} \equiv \frac{ZeBR}{g}
$$

[FACT] **最大能量（$q=3$ 时，公式 49）—— benchmark 估计**：

$$
E_c \equiv E_{q=3} \sim 10^{17}\cdot Z\cdot\left(\frac{R}{\rm kpc}\right)\cdot\left(\frac{B}{\mu{\rm G}}\right)\,{\rm eV}
$$

- 假设 $B$ 平行激波法线。

[FACT] **倾斜磁场额外漂移加速（公式 50）**：

$$
E_{\rm max} = Ze\,u_1\,B\,R \sim 10^{18}\cdot Z\,u_1\cdot\left(\frac{R}{\rm kpc}\right)\cdot\left(\frac{B}{\mu{\rm G}}\right)\,{\rm eV}
$$

- 比 (49) 高 ~10×（$u_1 \to c$ 时），但需要特殊条件（plasma 效应使 $E$ 场更小）。

### 5.1.2 谱斜率

> **加速谱斜率**

[FACT] 简单 DSAM：$q = (r+2)/(r-1)$，$r<4 \to q>2$（典型 ~2.3–2.4）。强激波 back-reaction：$q = 1.5$（harder）[337]。超相对论激波（$\Gamma \to \infty$）：$q \simeq 2.2$（softer）[338]。相对论 blast wave：第一次 crossing ~ $\Gamma^2$ 能量增益，后续 cycles ~ 2× [339]。

**关键公式**：

$$
\boxed{E_c \sim 10^{17} Z\!\left(\frac{R}{\rm kpc}\right)\!\left(\frac{B}{\mu{\rm G}}\right)\,{\rm eV}\;(49),\quad E_{\rm max} \sim 10^{18} Z\,u_1\!\left(\frac{R}{\rm kpc}\right)\!\left(\frac{B}{\mu{\rm G}}\right)\,{\rm eV}\;(50)}
$$

---

## 5.2 Source Candidates for UHECR

[FACT] §5.2 用 Hillas 判据与能量损失论证系统筛选候选源。

### 5.2.1 Hillas 判据

> **Hillas 判据**

[FACT] **公式 51**：

$$
\left(\frac{B}{\mu{\rm G}}\right)\cdot\left(\frac{R}{\rm kpc}\right) > 2\cdot\left(\frac{E}{10^{18}\,{\rm eV}}\right)\cdot\frac{1}{Z\,\beta}
$$

- 加速区尺寸 $R > $ 回旋半径 $2\,r_g$。
- **Hillas 图 (Fig. 25)**：只有 AGN、射电星系、脉冲星等少数源满足 $\sim 10^{20}$ eV 加速条件。

### 5.2.2 AGN & Radio-Galaxies

> **AGN 与射电星系**

[FACT] **支持 AGN 作为 UHECR 源的证据**：
1. **Mrk 421, Mrk 501** (BL Lac) 在 > 10 TeV $γ$ 被观测 → 可由质子光 $π$ 产生解释（vs IC）。
2. EGRET diffuse $γ$-ray 能量密度 $\sim E^{-2}$ 质子注入谱到 $10^{20}$ eV 所需能量 → 支持河外质子加速。

[FACT] **反对 AGN 核心作为 EHECR 源**（Norman et al. [13]）：AGN 核心典型 $R \sim 0.02$ pc, $B \sim 5$ G → 公式 (49)：$E_c \sim 10^{19}$ eV。**主要问题**：中心引擎内辐射场强烈 → 加速质子通过 photo-pion 严重衰减。同时考虑加速与能量损失 → 质子或核在 **$E > \sim 10^{16}$ eV 无法逃出核心**。中子假设也不行（中子本身也受 photo-pion 衰减）。

[FACT] **FR-II 射电星系 hot spots** — **最有希望的加速器**：hot spot 周围 soft photon 密度低 → photo-pion 损失不显著；若 $B$ 场足够强 → **$E_{\rm max}$ 可达 $\sim 10^{21}$ eV**。**主要问题**：hot spot 距地球大 cosmological 距离 > 100 Mpc [26] → GZK 效应使其粒子无法存活。**结论**：射电星系 hot spots 可能是 UHECR ($> 10^{17}$ eV) 源，但**难以解释 $10^{20}$ eV 以上事件**。

[FACT] **Boldt–Ghosh [27] 建议**：自旋超大质量黑洞（不活跃 quasar 遗迹）事件视界附近加速 → $E_{\rm max} \sim 10^{21}$ eV；本地 50 Mpc 内足够多候选 → 可解释 EHECR 通量。

### 5.2.3 Waxman–Bahcall Bound

> **Waxman–Bahcall Bound**

[FACT] [218]：比较 UHECR 通量 ($E \sim 10^{19}$ eV) → 对 diffuse $ν$ 通量给出更强上界。Mannheim, Protheroe, Rachen [353] 声称存在 loophole（仅 $10^{16}\text{–}10^{18}$ eV 适用）。Bahcall & Waxman [352] 反驳 → 认为 bound **robust**。**不适用于**：对质子光学厚的源（如 AGN 核心）；**不适用于 top-down**（$ν$ 是初级而非次级）。

### 5.2.4 Pulsars

> **脉冲星加速**

[FACT]
- **简单脉冲星直接加速**：~$10^{21}$ eV 势差，但 **pair-cascade 短路** → 实际 $< 10^{15}$ eV。
- **吸积盘**：能量损失限制 ~$10^{15}$ eV。
- **Magnetar** (SGR 1900+14)：表面 $B \sim 10^{15}$ G → 能量预算提高 2–3 个量级，但损失问题未解决。
- **Fe 离子 MHD 风** [355]：新形成强磁化脉冲星（初始 $P < 4(B_s/10^{13}\,{\rm G})^{1/2}$ ms）→ 可加速 Fe 离子 $> 10^{20}$ eV，预言 EHECR 组成以 Fe 为主（可检验）。

### 5.2.5 其他候选源

> **其他候选源**

| 源 | $E_{\rm max}$ | 备注 |
|---|---|---|
| 银河风终止激波 | 可能达 UHE | 依赖 $B$ |
| 星系碰撞激波 | ~UHE | [357] |
| 星系团吸积/合并激波 | UHE | [358,359] |
| 结构形成大尺度激波 | UHE | [13] |

一般难以超过 $10^{20}$ eV。

**关键公式**：

$$
\boxed{(B/\mu{\rm G})\cdot(R/{\rm kpc}) > 2\,(E/10^{18}\,{\rm eV})/(Z\,\beta)\;\;{\rm (Eq.\ 51,\ Hillas)}}
$$

---

## 5.3 A Possible Link Between Gamma-Ray Bursts and Sources of $E > 10^{20}$ eV Events?

[FACT] §5.3 讨论 GRB 作为 EHECR 源的 dissipation wind 模型。

### 5.3.1 基本动机

> **GRB–UHECR 基本动机**

[FACT] UHECR 所需能量释放率 ~ GRB $γ$ 辐射率 [361,362]。预言谱与观测谱 $E > \sim 10^{19}$ eV 一致（质子注入 $E^{-2.3\pm 0.5}$ [288]，Fermi 加速）。**主要问题**：GZK 距离内 (< 50 Mpc) 宇宙学 GRB 率 ~**每世纪一次** → 观测 UHECR 时间窗内概率极低，除非磁场导致 > 百年时间延迟。

### 5.3.2 磁场下限

> **GRB 场景的磁场下限**

[FACT] **公式 52**：

$$
B \gtrsim 10^{-10}\cdot\left(\frac{E}{10^{20}\,{\rm eV}}\right)\cdot\left(\frac{d}{30\,{\rm Mpc}}\right)^{-1}\cdot\left(\frac{l_c}{1\,{\rm Mpc}}\right)^{-1/2}\,{\rm G}
$$

- $N$ 个不同到达方向 → bound 增强 $N^{1/2}$ 倍。
- 最近观测各向同性 [8] + EGMF 上界 [363] → 已构成挑战。
- GRB 距离标度变大 → 能量要求更苛刻 [363]。

### 5.3.3 Dissipative Wind Model

> **耗散风模型**

[FACT] 光 + $e^{+}e^{-}$ + 少量重子风 → 超相对论 Lorentz 因子 $\gamma \gg 1$。耗散半径 $r_d$ 处 internal shock → 部分动能转 $γ$ 射线（GRB）。耗散产生 near-equipartition 磁场 → 二阶 Fermi 加速。

[FACT] **三重条件**：
1. **加速时间 < 膨胀时间（公式 53）**：
$$
B \gtrsim \frac{E}{\rm erg} \simeq 3\times10^{4}\cdot\left(\frac{E}{10^{20}\,{\rm eV}}\right)\cdot\left(\frac{r_d}{10^{13}\,{\rm cm}}\right)^{-1}\,{\rm G}
$$
2. **$π$ 产生损失 < 加速（公式 54）**：
$$
B \gtrsim 20\cdot\left(\frac{L_\gamma}{10^{51}\,{\rm erg/s}}\right)\cdot\left(\frac{r_d}{10^{13}\,{\rm cm}}\right)^{-2}\cdot\left(\frac{\gamma}{300}\right)^{-2}\,{\rm G}
$$
3. **同步损失 < 加速（公式 55）**：
$$
B \lesssim 3\times10^{5}\cdot\left(\frac{\gamma}{300}\right)^{2}\cdot\left(\frac{E}{10^{20}\,{\rm eV}}\right)^{-2}
$$

[FACT] **同时满足**：需 $r_d > 10^{12}(\gamma/300)^{-2}(E/10^{20}\,{\rm eV})^{3}$ cm（公式 56），以及 **$\gamma > 40\,(E/10^{20}\,{\rm eV})^{3/4}(t_{\rm GRB}/{\rm s})^{-1/4}$**。

### 5.3.4 次级产物

> **GRB 次级产物**

[FACT]
- **$ν$ 通量**：~$10^{14}$ eV，数十事件/km$^{3}$ 中微子望远镜 [365,370]；> $10^{19}$ eV 可被 AIRWATCH/MASS 探测 [366]。
- **MACRO 上界**：每个 GRB $0.87\times10^{-9}$ cm$^{-2}$ $μ$ 通量 [372]。
- **同步辐射信号**：~1% 总 burst 能量在 10 MeV（GLAST 可探测）；数百 GeV（IACT 可探测）；~TeV afterglow [367–369]。
- 若 GeV cascade 解释 diffuse $γ$-ray → 每个 GRB 释放 ~$10^{56}$ erg，$\gamma > 500$。

### 5.3.5 Waxman–Bahcall 与 Top-down 的区别

> **Bottom-up 与 Top-down 的次级粒子区别**

[FACT] Bottom-up（AGN/Radio/GRB）：$ν$ 是次级产物，受 diffuse GeV $γ$-ray background 约束。Top-down：$ν$ 是初级，通量可显著高于核子 → 但仍受 diffuse GeV $γ$ 约束（§7.4）。

**关键公式**：

$$
\boxed{B_{\rm GRB} \gtrsim 10^{-10}\!\left(\frac{E}{10^{20}\,{\rm eV}}\right)\!\left(\frac{d}{30\,{\rm Mpc}}\right)^{-1}\!\left(\frac{l_c}{\rm Mpc}\right)^{-1/2}\!{\rm G}\;(52),\quad \gamma > 40\!\left(\frac{E}{10^{20}\,{\rm eV}}\right)^{3/4}\!\left(\frac{t_{\rm GRB}}{\rm s}\right)^{-1/4}}
$$

---

## 元数据

```yaml
chapter: 8
pages: "40–48"
subsections: ["5.1.1", "5.1.2", "5.2.1", "5.2.2", "5.2.3", "5.2.4", "5.2.5", "5.3.1", "5.3.2", "5.3.3", "5.3.4", "5.3.5"]
key_formulas:
  - "E_c ~ 10$^{17}$ Z (R/kpc)(B/μG) eV (Eq. 49)"
  - "E_max ~ 10$^{18}$ Z u$_{1}$ (R/kpc)(B/μG) eV (Eq. 50)"
  - "(B/μG)(R/kpc) > 2 (E/10$^{18}$ eV)/(Zβ) (Eq. 51, Hillas)"
  - "B_GRB ≳ 10$^{-10}$ (E/10$^{20}$ eV)(d/30 Mpc)$^{-1}$(l_c/Mpc)$^{-1}$/$^{2}$ G (Eq. 52)"
keywords:
  - diffusive shock acceleration
  - Hillas criterion
  - FR-II radio galaxy hot spot
  - Waxman-Bahcall bound
  - magnetar Fe wind
  - GRB dissipative wind
references_internal:
  prev_chapter: 07_source_search_transport
  next_chapter: 09_topdown_basic_fragmentation
```

**引用页码**：全文引用基于 *Phys. Rep.* 320 (1999), pp. 40–48。