---
chapter: 6
title: "Galactic & Extragalactic Magnetic Fields"
pages: "27–30"
sections:
  - "4.4.1 Synchrotron Radiation & EM Cascades"
  - "4.4.2 Deflection and Delay of Charged Hadrons"
  - "4.5 Constraints on EHECR Source Locations"
  - "4.6 Source Search for EHECR Events"
related_chapters:
  prev: 05_neutrinos_exotic_particles
  next: 07_source_search_transport
status: done
---

> 本章属于：Bhattacharjee & Sigl (1999), *Phys. Rep.* 320, 1–150
>
> 上一章：`05_neutrinos_exotic_particles.md`
>
> 下一章：`07_source_search_transport.md`

# 6. Galactic & Extragalactic Magnetic Fields (§4.4–4.6, p. 27–30)

[FACT] §4.4–4.6 覆盖 pp. 27–30，是全文最"可观测"的章节之一：讨论 EGMF 与银河磁场如何在 UHECR 谱与到达方向上留下可探测的印记。三个子节依次覆盖：**电磁级联与同步冷却**（§4.4.1）→ **带电强子偏转与延迟**（§4.4.2）→ **源位置约束与源搜索**（§4.5–4.6）。

[INTERPRETATION] §4 逻辑链的收束点是：**磁场是 UHECR 源定位的放大器也是混淆器**——它压制 EM 级联从而保护部分 UHE $γ$（§4.4.1），它抹平源像但保留中心指向（§4.4.2），它把"几百 Mpc 内是否存在强源"的问题转化为"偏转角 + 延迟时间"的联合测量（§4.5–4.6）。

---

## 4.4 Signatures of Galactic and Extragalactic Magnetic Fields in UHECR Spectra and Images

[FACT] §4.4 讨论 EGMF 在 UHE 光子与强子传播中的两类主导效应：同步冷却对 EM 级联的抑制（§4.4.1），以及偏转 + 延迟对带电强子图像与时间结构的影响（§4.4.2）。

### 4.4.1 Synchrotron Radiation & EM Cascades

> **同步辐射与电磁级联**

[FACT] §4.4.1 给出同步冷却的**能量损失率（公式 28）**：

$$
\frac{dE}{dt} = -\frac{4}{3}\,\sigma_{\rm T}\,\frac{B^2}{8\pi}\left(\frac{q\,m_e}{m}\right)^4\left(\frac{E}{m_e}\right)^2
$$

- UHE 质子：$m$ 极大 → 同步损失**可忽略**。
- UHE 电子：同步损失在**转移能量**以上占主导。

[FACT] **转移能量（同步冷却）**：

$$
E_{\rm tr} \sim 10^{20}\left(\frac{B}{10^{-10}\,{\rm G}}\right)^{-1}\,{\rm eV}
$$

[INTERPRETATION] 当 $E > E_{\rm tr}$，电子几乎瞬间通过同步辐射损失能量 → EM cascade 发展被阻断 → $γ$ 传播由 PP/DPP 吸收主导 → 可观测通量由"直接"（first-generation）$γ$ 决定 → 简化为式 (12) 用 $l(E)$ 代替 $l_E(E)$。

[FACT] **同步辐射光子能量（公式 29）**：

$$
E_{\rm syn} \simeq 6.8\times10^{13}\left(\frac{E}{10^{21}\,{\rm eV}}\right)^{2}\left(\frac{B}{10^{-9}\,{\rm G}}\right)\,{\rm eV}
$$

- 经典极限下有效（$E_{\rm syn} \ll E$）。
- **约束来源**：当 $E_{\rm syn}$ 落入已有 diffuse $γ$ 观测窗口时——EGRET $\sim 1$ GeV [185]；HEGRA 上界 50–100 TeV [257]；CASA-MIA $6\times10^{14}$ – $6\times10^{16}$ eV [258]。

[FACT] **强 discrete UHE $γ$ 源**（如拓扑缺陷，近单能注入谱，EGMF $\sim 10^{-9}$ G）在某些 $E > \sim 10^{16}$ eV 处预言 $γ$ 通量 > 带电 CR 通量 → **已被排除** [259]。

**关键公式**：

$$
\boxed{E_{\rm tr} \sim 10^{20}\left(\frac{B}{10^{-10}\,{\rm G}}\right)^{-1}\,{\rm eV}\;,\quad E_{\rm syn} \simeq 6.8\times10^{13}\left(\frac{E}{10^{21}\,{\rm eV}}\right)^{2}\left(\frac{B}{10^{-9}\,{\rm G}}\right)\,{\rm eV}}
$$

### 4.4.2 Deflection and Delay of Charged Hadrons

> **带电强子的偏转与延迟**

[FACT] 回旋半径 $r_g \simeq E/(q\,e\,B_\perp)$，在均匀场 $B$ 中传播距离 $d$ 的**单场偏转角（公式 30）**：

$$
\theta(E,d) \simeq \frac{d}{r_g} \simeq 0.52°\cdot q\cdot\left(\frac{E}{10^{20}\,{\rm eV}}\right)^{-1}\left(\frac{d}{1\,{\rm Mpc}}\right)\left(\frac{B_\perp}{10^{-9}\,{\rm G}}\right)
$$

[FACT] 磁场特征为 rms 强度 $B$ + 关联长度 $l_c$；$d \gtrsim l_c$ 时的**随机场 rms 偏转角（公式 31）**：

$$
\theta(E,d) \simeq \frac{(2\,d\,l_c/9)^{1/2}}{r_g} \simeq 0.8°\cdot q\cdot\left(\frac{E}{10^{20}\,{\rm eV}}\right)^{-1}\left(\frac{d}{10\,{\rm Mpc}}\right)^{1/2}\left(\frac{l_c}{1\,{\rm Mpc}}\right)^{1/2}\left(\frac{B}{10^{-9}\,{\rm G}}\right)
$$

[FACT] 三种极限行为：
- **$d\,\theta \ll l_c$**（相干）：所有能量粒子"看到"同一磁场实现 → 偏转一致，源像保持紧密 → 偏转方向偏离视线方向（coherent deflection）。
- **$d\,\theta \gg l_c$**（漫散射）：源像被抹平，扩展范围 $\sim \theta(E,d)$，**但中心对准真实源方向**。
- **$d\,\theta \simeq l_c$**：可能产生**多像**（类似引力透镜）。

[FACT] **平均时间延迟（公式 32）**：

$$
\tau(E,d) \simeq \frac{d\,\theta^{2}}{4} \simeq 1.5\times10^{3}\,q^{2}\cdot\left(\frac{E}{10^{20}\,{\rm eV}}\right)^{-2}\left(\frac{d}{10\,{\rm Mpc}}\right)^{2}\left(\frac{l_c}{1\,{\rm Mpc}}\right)\left(\frac{B}{10^{-9}\,{\rm G}}\right)^{2}\,{\rm yr}
$$

[FACT] **Bursting source 效应**：$\tau \propto E^{-2}$ → 观测窗口内的瞬时谱与长时间平均谱不同，在 $\tau(E_0,d) \simeq$（观测时刻 − 零延迟到达时刻）处出现**谱峰 $E_0$**；高能粒子已过，低能粒子未至。

[FACT] **谱宽度**：$d <$ 相互作用长度且 $d\theta \ll l_c$ → 谱宽 $\ll E_0$；其他情形 → 谱宽 $\sim E_0$。

**关键公式**：

$$
\boxed{\theta \simeq 0.8°\cdot q\left(\frac{E}{10^{20}\,{\rm eV}}\right)^{-1}\left(\frac{d}{10\,{\rm Mpc}}\right)^{1/2}\left(\frac{l_c}{1\,{\rm Mpc}}\right)^{1/2}\left(\frac{B}{10^{-9}\,{\rm G}}\right)\;,\quad \tau \propto E^{-2}}
$$

---

## 4.5 Constraints on EHECR Source Locations

[FACT] §4.5 综合偏转几何与 GZK 距离给出对源位置的联合约束。

### 4.5.1 距离–角度约束

> **距离与角度联合约束**

[FACT]
- 核子/核/$γ$ > 几十 EeV 起源距离 $\lesssim 50$ Mpc（GZK / 光致分裂 / PP-DPP）。
- 结合公式 (31) → 到达方向应**在几度内指向源** [12]。
- 银河盘内偏转可"反演修正"（银河磁场图的计算 [264,265]）。

### 4.5.2 Faraday Rotation 约束

> **法拉第旋转约束**

[FACT] **原版本**：$B\,l_c^{1/2} \lesssim 10^{-9}$ G Mpc$^{1/2}$ [262,263]。

[FACT] **修正版**（用 $\Omega_{\rm b}\,h^{2} \simeq 0.02$ 替代 closure density，未结构宇宙）：

$$
B \lesssim 3\times10^{-7}\left(\frac{\Omega_{\rm b}\,h^{2}}{0.02}\right)^{-1}\left(\frac{h}{0.65}\right)\left(\frac{l_c}{\rm Mpc}\right)^{-1/2}\,{\rm G}
$$

→ 更强偏转。

[FACT] **大尺度结构修正**（Lyman-$α$ forest 建模 + 磁通冻结）[267]（公式 34）：

$$
B \lesssim 10^{-9}\text{–}10^{-8}\,{\rm G}
$$

- 关联尺度从 Hubble 到 1 Mpc。
- sheets 和 voids 内最大场可达 $\sim \mu$G [268,267,269]。

### 4.5.3 结论

> **源位置约束的结论**

[FACT]
- 若本地大尺度结构不强磁化 → UHE 核子偏转仍在度级。
- 但**超星系面强磁化**、或**近邻星团**（场强 $10^{-6}$ G [262–263,270]）、或**重核（如 Fe）** → 可能强烈偏转 [26]。
- 强磁化下，EGMF 磁透镜效应可影响 UHECR 源位置 [311,316]。

**关键公式**：

$$
\boxed{B\,l_c^{1/2} \lesssim 10^{-9}\,{\rm G\,Mpc}^{1/2}\;,\quad B \lesssim 10^{-9}\text{–}10^{-8}\,{\rm G}\;,\quad d_{\rm src} \lesssim 50\,{\rm Mpc}}
$$

---

## 4.6 Source Search for EHECR Events

[FACT] §4.6 汇总 1998 年前后的单事件关联与统计关联尝试。

### 4.6.1 单事件关联

> **单事件关联尝试**

[FACT] **Fly's Eye 300 EeV 事件**（$3.2\times10^{20}$ eV）[26]：

| 候选源 | 距离 | 到达方向偏离 |
|---|---|---|
| Cen A | ~3 Mpc | ~136° |
| Virgo A | 13–26 Mpc | ~87° |
| M82 | 3.5 Mpc | ~37° |
| **MCG 8-11-11** (Seyfert) | 62–124 Mpc | **~10°** |
| **3C134** (FR II radio gal.) | 30–500 Mpc（不确定） | **~10°** |

- **3C147** (quasar, $z\sim 0.5$) 在 Fly's Eye 事件误差箱内 → 曾建议为**中微子源** [72]。
- 中微子假设问题：$\sigma_\nu N$ 在 $10^{20}$ eV 大气相互作用概率 $\sim 10^{-5}$。

[FACT] **AGASA 最高能事件**：中微子假设 → **3C33** (FR II, ~300 Mpc)；核子假设 → **NGC 315** (FR I, ~100 Mpc)。银晕 Fe 初级 + 扩展银晕磁场 → 银道面起源可能 [273]。

### 4.6.2 统计关联

> **统计关联尝试**

[FACT]

| 数据 | 关联对象 | 结果 |
|---|---|---|
| Haverah Park + AGASA + VR + Yakutsk | Supergalactic Plane | **~3$\sigma$** 正相关（$E > 4\times10^{19}$ eV）[79] |
| SUGAR 南半球 | 同 | 无显著相关 [80] |
| AGASA（最新）[81,83] | 20% EHECR 彼此 + SG 面 | 部分相关；其余各向同性 |
| 组合分析 [274,275] | 同 | 一致，但未定论 |
| CFA Redshift Catalog [278] | 50 Mpc 内星系 | 到达方向一致 |

[CRITIQUE] [276] 指出 Haverah Park SG 面关联"过强"（对 Local Supercluster 之外的星系而言）→ [277,271] 提议大尺度结构中存在 $\mu$G 级场，沿 sheets/filaments 对齐 → **聚焦效应**。

### 4.6.3 GRB 与其他关联

> **GRB 与其他关联**

[FACT] 两最高能量事件在 BATSE GRB 误差箱内 [279]，但大样本无显著结果 [280]。若 GRB 为银河尺度 → 反证 GRB 关联；若河外 → 需考虑大时间延迟（见 §5.3）。

[FACT] **Yakutsk EAS**：UHECR $(0.8\text{–}4)\times10^{19}$ eV 与**银道面脉冲星沿磁感线方向**统计显著相关 [283]。

**关键参数**：转移能量 $E_{\rm tr} \sim 10^{20}(B/10^{-10}\,{\rm G})^{-1}$ eV；均匀场偏转角 $0.52°\,q(E/10^{20}\,{\rm eV})^{-1}(d/{\rm Mpc})(B_\perp/10^{-9}\,{\rm G})$；随机场延迟 $\tau \sim 1.5\times10^{3}\,q^{2}\,(E/10^{20}\,{\rm eV})^{-2}(d/10\,{\rm Mpc})^{2}(l_c/{\rm Mpc})(B/10^{-9}\,{\rm G})^{2}$ yr；源距离约束 $\lesssim 50$ Mpc。

---

## 元数据

```yaml
chapter: 6
pages: "27–30"
subsections: ["4.4.1", "4.4.2", "4.5.1", "4.5.2", "4.5.3", "4.6.1", "4.6.2", "4.6.3"]
key_formulas:
  - "dE/dt = -(4/3) σ_T (B²/8π) (q m_e/m)^4 (E/m_e)^2"
  - "E_tr ~ 10²⁰ (B/10⁻¹⁰ G)⁻¹ eV"
  - "θ ≈ 0.8° q (E/10²⁰ eV)⁻¹ (d/10 Mpc)^½ (l_c/Mpc)^½ (B/10⁻⁹ G)"
  - "τ ∝ E⁻²"
  - "B l_c^½ ≲ 10⁻⁹ G Mpc^½"
keywords:
  - synchrotron cooling
  - EGMF
  - source deflection
  - Faraday rotation
  - MCG 8-11-11
  - Supergalactic Plane
references_internal:
  prev_chapter: 05_neutrinos_exotic_particles
  next_chapter: 07_source_search_transport
```

**引用页码**：全文引用基于 *Phys. Rep.* 320 (1999), pp. 27–30。