> 本章属于：Bhattacharjee & Sigl (1999), Phys. Rep. 320, 1–150
>
> 上一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/09_topdown_basic_fragmentation.md|09_topdown_basic_fragmentation.md]]
>
> 下一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/11_monopoles_vortons_necklaces.md|11_monopoles_vortons_necklaces.md]]

---

# 10. Cosmic Strings as X-Particle Sources (§6.4–6.5, p. 59–72)

## 10.1 本节核心内容

- 宇宙弦 (cosmic strings) 是 TD 家族中被研究最透彻的一类（数值与解析）。
- 从弦中释放 X 粒子的四种基本过程：
  1. 弦段**交叉/intercommuting**
  2. 闭合环最终**坍缩**
  3. **Cusp evaporation**
  4. 环**多重自相交/坍缩** (Bhattacharjee-Rana)
  5. **直接发射** (Vincent-Antunes-Hindmarsh [417] 争议结果)
- 超导弦 (SCS)：达到临界电流后放出超重费米子。
- **核心结论**：GUT 尺度弦 (~$10^{16}$ GeV) 在多数过程中 X 产额不足；但若为 ~$10^{13}$–$10^{14}$ GeV 的"轻"弦，可解释 EHECR 且不违反级联 $\gamma$ 限制。

## 10.2 §6.4.1 Cosmic String 演化与 Scaling

### 10.2.1 演化阶段 [FACT]

1. **形成后**：随机缠绕网络。
2. **摩擦主导期**（T > (G$\mu$)^(1/2) $\eta$）：
   - 弯曲弦段达终端速度 ∝ 1/r。
   - 弦被拉直、长度缩短 → $\xi_{\rm s}$ 增加 → $\rho_{\rm s}$ 下降。
3. **相对论期**：摩擦可忽略。
   - 情形(a) **Scaling 解**：$\xi_{\rm s}$/t = const → $\rho_{\rm s}$,scaling ∝ 1/t$^{2}$
   - 情形(b) $\xi_{\rm s}$ 增长慢于 t → 弦过早主导宇宙（被排除）。

### 10.2.2 Scaling 能量损失 [FACT]

```
$\rho$̇_s,total = −2(Ṙ/R) $\rho_{\rm s}$ + $\rho$̇_s,loss         (71)
```
- 辐射主导：$\rho$̇_s,loss = −$\rho_{\rm s}$/t
- 物质主导：$\rho$̇_s,loss = −(2/3) $\rho_{\rm s}$/t

### 10.2.3 环形成与小尺度结构 [FACT]

- **早期数值模拟**：大 (horizon-size) 环形成。
- **高分辨率模拟**：大量小尺度结构（kinks） → 环尺寸远小于 horizon。
- **稳定尺度 $\zeta$**：gravitational radiation 反作用稳定化 → $\zeta$ ~ $\Gamma$G$\mu$t（$\Gamma$ ~ 100）。

### 10.2.4 Scaling 弦的 loop distribution (公式 72–76) [FACT]

- Scaling 解：$\rho_{\rm s}$ = $\mu$/(x t)$^{2}$, x ∈ [0.3–0.7]（近期模拟 x ~ 0.3）。
- 环长度：L_b = K $\zeta$(t_b) = K $\Gamma$ G$\mu$ t_b （公式 72）
- 环诞生率（物质主导，公式 73）：
```
dn_b/dt = (2/(3 x$^{2}$)) ($\Gamma$ G$\mu$)$^{-1}$ K$^{-1}$ t$^{-4}$
```
- 环长度分布（公式 76）：
```
dn/dL (L, t) = [2/(3 x$^{2}$)] (K+1)/K · 1/(t$^{2}$ (L + $\Gamma$ G$\mu$ t)$^{2}$), L ≤ K$\Gamma$G$\mu$t
```

### 10.2.5 现代 loop 数量与尺度 (G$\mu$ = $10^{-6}$ 时) [FACT]

| 量 | 值 |
|---|---|
| 最丰环长度 | ~200 (G$\mu$/$10^{-6}$)($\Omega_{0}$h$^{2}$)^(−1/2) kpc |
| 数密度 | $~4.6\times10^{-6}$ (G$\mu$/$10^{-6}$)$^{-1}$($\Omega_{0}$h$^{2}$)^(3/2) Mpc$^{-3}$ |
| 典型间隔 | ~60 (G$\mu$/$10^{-6}$)^(1/3)($\Omega_{0}$h$^{2}$)^(−1/2) Mpc |

## 10.3 §6.4.2 Intercommuting 过程

### 10.3.1 机制 [FACT]

- 两条弦段交叉 → 重叠长度 ~w ~ $\eta^{\rm -1}$ → Higgs 相未定义 → 拓扑去除事件。
- 释放能量 ~$\mu$w ~ $\eta$ → 每个 intercommuting 释放 ~1 个 X 粒子。

### 10.3.2 速率估算 [FACT]

```
n_ic(t) = $\chi$/$\xi_{\rm s4}$          (77)
$\xi_{\rm s}$ ~ x t, x ~ 0.3–0.7
```
- **结论**：intercommuting 过程的 X 产额 **utterly negligible**，远不足以解释 EHECR 通量。

## 10.4 §6.4.3 Cusp Evaporation

### 10.4.1 机制 [FACT]

- **Cusp**：弦上某点瞬时以光速运动 → 曲率半径极小 → Nambu-Goto action 失效。
- 具有有限宽度 w 的真实弦在 cusp 附近 → 弦段重叠 → "蒸发"为 X 粒子。
- **Kink 碰撞**也可形成 cusp（沿相反方向传播的 kinks 相撞 [424]）。

### 10.4.2 Cusp 长度 [FACT]

**原始估计** [423]：
```
ℓ_c ~ $\zeta$^(2/3) w^(1/3)
```
**更一般估计** [425]：
```
ℓ_c ~ (L w)^(1/2)
```
比旧估计小 (w/L)^(1/6) → 对 GUT 尺度字符串 (~$10^{16}$ GeV)，w/L 为天文数字小量 → **ℓ_c 被严重压低**。

### 10.4.3 X 粒子数 [FACT]

- 单次 cusp 事件：~($\eta$$\zeta$)^(2/3)（长弦）或 ~($\eta$L)^(2/3)（闭环）。
- 对 GUT 尺度：$\eta$ ~ $10^{16}$ GeV，但 L/w ~ 极大 → cusp 效率低。
- **结论**：**cusp evaporation 不足以产生可观 EHECR 通量**。

## 10.5 §6.4.5 Collapse/Repeated Self-intersections

### 10.5.1 机制 [FACT]

- 大环 L/4 时刻坍缩为 double-line 配置 → 整体湮灭为 X 粒子。
- 或反复自相交分裂为越来越小的子环 → debris of tiny loops（~$\eta^{\rm -1}$ 尺度）→ X 粒子。
- **碎裂时间**：$\tau_{\rm debris}$ ~ L ≪ $\tau_{\rm grav}$ ~ ($\Gamma$G$\mu$)$^{-1}$L

### 10.5.2 速率 [FACT, 公式 84]

假设 f_X 的环能量转化为 X：
```
ṅ_X(t) = f_X · $\mu$/m_X · (2/(3 x$^{2}$)) t$^{-3}$          (84)
```

### 10.5.3 解释 EHECR 的条件 (公式 85)

```
f_X · $\eta_{16}$^(3/2) ≃ $2.8\times10^{-5}$            (85)
```
（$\eta_{16}$ = $\eta$/$10^{16}$ GeV, l(E_$\gamma$=300 EeV) = 50 Mpc）

### 10.5.4 级联 $\gamma$ 约束 (公式 86–88) [FACT]

- 注入 EHECR 能量的 EM 级联：
```
$\omega_{\rm cas}$ ≃ (1/2) m_X ṅ_X $t_{0}$            (86)
$\omega_{\rm cas}$ ≤ $2\times10^{-6}$ eV cm$^{-3}$              (87, [185])
```
- 导出（公式 88）：
```
f_X · $\eta_{162}$ ≤ $9.6\times10^{-6}$              (88)
```

### 10.5.5 允许窗口 [FACT]

联立 (85)+(88)：
```
$9.2\times10^{12}$ GeV <~ $\eta$ <~ $1.2\times10^{15}$ GeV
f_X ~ $2.8\times10^{-5}$ $\eta_{16}$^(−3/2)
f_X ∈ [$6.7\times10^{-4}$, 1]
```
- **m_X ≫ $10^{15}$ GeV 时 GUT-scale 弦难以同时满足**（违反 $\gamma$ 背景约束）。
- **$\eta$ ~ $10^{13}$ GeV 的"轻"弦**是自然候选。

### 10.5.6 数值模拟支持 [FACT]

- **Siemens-Kibble [431]**：环自相交概率随谐波数**指数增长**。
- Kinks 是高谐波配置 → 有 kink 的环高概率自相交 → f_X ~ few×$10^{-4}$ 是**合理的**。
- **Vilenkin [429]**：子环碎裂过程中部分能量转化为动能 → X 粒子可能**相对论性**（空间分散）。
- **Berezinsky-Blasi-Vilenkin [406]**：对 relativistic X 情形，某些 loop fragmentation 模型下无法同时满足 (85)+(88) → 但其他模型（如 Siemens-Kibble）可绕过。
- Bhattacharjee-Sigl [432]：f_X ~ 1 时（全部环碎裂为 X），若 $\eta$ ≲ $3.1\times10^{13}$ GeV 且 f_KE ≲ few%，可解释 EHECR 且不违反 $\gamma$ 约束。

### 10.5.7 轻弦的额外优势 [FACT]

- Loop 数密度 ∝ (G$\mu$)$^{-1}$ → $\eta$ = $10^{13}$ GeV 时（G$\mu$ ~ $10^{-12}$），与 $\eta$ = $10^{16}$ GeV 相比 loop 数密度**大 $10^{6}$ 倍**。
- GZK 半径 (50 Mpc) 内：
  - GUT 弦 (~$10^{16}$ GeV)：仅 ~2.4($\Omega_{0}$h$^{2}$)^(3/2) 个 loop。
  - 轻弦 (~$10^{13}$ GeV)：~ $2.4\times10^{6}$ 个 loop。
- **结论**：轻弦 ($\eta$ ~ few×$10^{13}$ GeV) 通过快速多重碎裂过程可**自然产生足够多 X 粒子**。

## 10.6 §6.4.6 Direct Emission 争议 [FACT]

- **Vincent-Antunes-Hindmarsh [417]**（新数值模拟）：若不人为设环尺寸截断 → 环主要在最小尺度 (~弦宽度 w) 上形成 → 立即坍缩为 X。
  - → **弦能量主要通过直接 X 粒子发射维持 scaling**，几乎无"大"环形成。
- 这**颠覆**了早期模拟结论（能量主要损失于引力辐射环）。
- 已被 **Moore-Shellard [434]** 质疑。
- **若 [417] 正确**：ṅ_X = (84) with f_X = 1 → 与 (68) 对比 → $\eta$ ≲ $10^{13}$ GeV（否则会超量产生 EHECR）。
  - → **GUT-scale 弦被排除**。
  - → 唯一预测：若长弦恰在 ~50 Mpc 内，EHECR 应呈**filamentary/linear 各向异性**（对应弦的空间分布）。

## 10.7 §6.5 Superconducting Cosmic Strings (SCS)

### 10.7.1 基本物理 [FACT]

- 弦携带**持续电流**：
  - 由弦内**带电费米子零模**（零模：弦内质量为零，弦外有质量 m_F）或**带电 Higgs 凝聚**承载。
  - 也可以来自 trapped 电荷（Kibble 机制）或不同电流弦段间 inter-commuting。
- **临界电流**：
  - 费米子情形：弦内 Fermi 动量 p_F 超 m_F → 费米子不再 trapped → 开始被释放。
  - 玻色子情形：弦内凝聚能量密度过高 → EM 对称性恢复 → 失去超导。
  - **上限**：J_c ≤ J_max ≃ e $\eta$（两种情形）。
- 弦外**X 粒子质量**：m_F = g $\eta$（g ~ Yukawa 耦合），可达 GUT 尺度 ~$10^{16}$ GeV。

### 10.7.2 OTW-SCS 演化场景 [FACT]

- **Ostriker-Thompson-Witten [421]**：原初磁场随宇宙膨胀 → 通过弦环的磁通变化 → 弦环上感应电流。
- 环振荡 → 电磁辐射 + 引力辐射损失 → 环缩小 → 电流 J ∝ L$^{-1}$ 增加 → 达到 J_c = J_s。
- 饱和环释放 X 粒子。

### 10.7.3 X 粒子发射率 [FACT, 公式 89–90]

**饱和环上费米子总数**：N_F = (m_F/$\pi$) L

**电磁辐射主导** (G$\mu$ ≲ $10^{-8}$ 或 g > 10(G$\mu$)^(1/2))：
```
Ṅ_F = (4/$\pi^{2}$) $\alpha_{\rm em}$ $\gamma_{\rm em}$ g$^{3}$ $\eta$            (89)
$\gamma_{\rm em}$ ≃ 100
```

**引力辐射主导** (g ≪ 10(G$\mu$)^(1/2))：
```
Ṅ_F = (g/$\pi$)($\Gamma$ G$\mu$) $\eta$            (90)
```

**条件**（产生 EHECR）：m_F = g$\eta$ ≥ $10^{12}$ GeV → $\eta$ ≥ $10^{12}$ GeV → G$\mu$ ≥ $10^{-14}$，且 $10^{-7}$(G$\mu$)$^{-}$^(1/2) ≤ g ≤ 1。

### 10.7.4 SCS 主要困难 [FACT]

- SCS 演化**高度不确定**（无详细数值模拟）。
- 若采用 **OTW 场景**（L_s 常数）：ṅ_X ∝ t$^{-4}$，HSW [393] 表明某些参数范围可产生可观测通量。
- 若 L_s 随时间增长（如 dynamos 增磁）：L_s($t_{0}$) 更小 → 当前 ṅ_X 不够。
- 若 L_s 随时间减小：早期注入能量过大 → **违反 CMB 畸变与 Big Bang 核合成** [437]。
- 其他不确定性：
  - 环可复杂折叠、增强电荷载体发射。
  - **Vorton 稳定性**：弦可能稳定为电流携带的小环（vorton，§6.6 讨论）。
  - 弦附近强磁场区域中 X 衰变产物能量严重降解 [440]（可能解决：若 X 寿命足够长可漂移到弱场区 [393]，或 AC 电流区 [406]）。
- **结论**：最简单 SCS 模型**一般无法产生足够 EHECR 通量** → 但**尚无定论**（SCS 物理远未完全理解）。

## 10.8 关键数值速查

| 量 | 值 |
|---|---|
| GUT 弦 $\mu$ | ~ ($10^{16}$ GeV)$^{2}$ ~ $10^{-6}$ M_Pl$^{2}$ |
| Scaling 解 x | 0.3–0.7（近期 ~0.3） |
| 小尺度结构 $\zeta$ | ~ $\Gamma$G$\mu$t, $\Gamma$ ~ 100 |
| 现代 loop 长度 | ~200 (G$\mu$/$10^{-6}$) kpc |
| Intercommuting X 数/事件 | ~1 |
| Cusp 长度 ℓ_c (旧) | ~ $\zeta$^(2/3) w^(1/3) |
| Cusp 长度 ℓ_c (新 [425]) | ~ (Lw)^(1/2) |
| Loop 碎裂 EHECR 条件 | f_X $\eta_{16}$^(3/2) ≃ $2.8\times10^{-5}$ |
| $\gamma$ 背景约束 | f_X $\eta_{162}$ ≤ $9.6\times10^{-6}$ |
| 允许 $\eta$ 窗口 | $9.2\times10^{12}$ – $1.2\times10^{15}$ GeV |
| Direct emission $\eta$ 上限 | ≲ $10^{13}$ GeV |
| SCS X 发射率 (EM 主导) | (4/$\pi^{2}$) $\alpha_{\rm em}$ $\gamma_{\rm em}$ g$^{3}$ $\eta$ |
| SCS X 发射率 (引力主导) | (g/$\pi$)($\Gamma$G$\mu$)$\eta$ |

## 10.9 [CRITIQUE] 与 1999 年后对照

- [FACT] **[417] direct emission 争议**：后续模拟（Moore-Shellard 2002+）倾向于支持传统 scaling + 大环形成图像，[417] 的结论被认为可能是模拟截断的人工产物。
- [FACT] **CMB anisotropy**（WMAP/Planck 数据）：对宇宙弦网络的约束比 1999 年时强得多 → G$\mu$ < $10^{-7}$ 量级（Planck 2015）→ 与本文 §6.4.6 讨论的 $\eta$ ≲ $10^{13}$ GeV 一致（G$\mu$ <~ $10^{-12}$）。
- [CRITIQUE] 本文作者（Bhattacharjee & Sigl）对"轻弦"情景的偏好，在 Planck 时代被**进一步支持**（因为 GUT-scale 弦被 CMB 约束排除）。