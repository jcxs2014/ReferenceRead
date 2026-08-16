# 3. Evolution and Nucleosynthesis during the AGB Phase（AGB 阶段的演化与核合成）

**上一章**: [02_preagb.md](02_preagb.md) · **下一章**: [04_tdu.md](04_tdu.md) §3.3 TDU

## 3.1 The thermally-pulsing Asymptotic Giant Branch（TP-AGB）

[FACT] AGB 恒星结构：从外向内 — 对流包络 → H 燃烧壳 → He 燃烧壳（intershell）→ C-O 核心。

[FACT] **热脉冲（thermal pulses）机制**：He 壳以简并/近简并条件薄薄包裹 C-O 核，He 燃烧热核不稳定性导致周期性壳闪（shell flash）。每一次壳闪在 inter-pulse 期间后产生一次 **TDU（第三 dredge-up）**。

[FACT] Intershell 组成（壳闪后，典型值）：**~70–75% ⁴He + 20–25% ¹²C + 几% ¹⁶O**（图 14），外加 ²²Ne、¹⁷O、²³Na、²⁵²⁶Mg、¹⁹F 等微量。

[FACT] 质量越大 → He 壳越薄 → 壳闪幅度越大、频率越高；金属度越低 → He 壳略薄。

[FACT] 热脉冲核合成的两个主反应：
1. **三 α 过程**：3 ⁴He → ¹²C + γ（壳闪主要能源）；
2. **¹²C(α,γ)¹⁶O**：需 ¹²C 库激活，产能量少但决定 C/O 比。

## 3.2 Hot Bottom Burning（HBB, 热底燃烧）

[FACT] HBB 发生于 **M ≳ 4.5M⊙**（Z=0.02）AGB 恒星：对流包络底部温度足够高（T ≳ 3×10⁷ K）可点燃 pp 链和 CNO 循环。

[FACT] HBB 后果：把 TDU 送来的 ¹²C 烧成 ¹³C 和 ¹⁴N，因此大质量 AGB **永不成为 C 星**（图 21b, 6M⊙）；反而是 N 富集星。

[FACT] HBB 是银河系球状星团（GCs）第二代恒星 "异常 N、Na、Al" 增丰的潜在污染源（Gratton et al. 2004, 2012；Prantzos et al. 2007；Fenner et al. 2004；Karakas et al. 2006a；Ventura & D'Antona 2009）。

### 3.2.1 Dredge-up, HBB and the Brightest C Stars
[FACT] 最亮的 C 星必须满足：TDU 速率 > HBB 破坏速率；因此主要见于低金属度中质量 AGB 或高质量低金属度星。

### 3.2.2 Core-Mass vs Luminosity Relation
[FACT] **Paczynski 关系**：TP-AGB 光度几乎完全由 C-O 核质量决定。
$$L/L_{\odot} \approx 59200\left(M_c/M_{\odot} - 0.522\right) \quad \text{(Paczynski 1970)}$$
[FACT] M ≥ 4.5M⊙ 模型因 HBB 偏离该关系（图 18）。

## 关键定量事实

| 质量 M⊙ | Z | HBB? | C 星? | ¹²C/¹³C（tip） | N/O |
|--------|-----|------|-------|---------------|------|
| 3 | 0.02 | 否 | 是 | 119 | 0.40 |
| 6 | 0.02 | 是（强） | 否 | 保持 < 20 | 大 |
| 1 | 0.02 | 否 | 是 | ~25 | — |

## 3.3 关键反应公式（LaTeX）

[FACT] **Paczynski 核质量–光度关系**（TP-AGB 光度由 C-O 核质量 $M_c$ 决定）：原文 p.27
$$ \frac{L}{L_\odot} \;\approx\; 59200\left(\frac{M_c}{M_\odot} - 0.522\right) \qquad \text{(Paczynski 1970)} $$

[FACT] **TP-AGB 核质量增长**：每次 interpulse 期核质量增量 $\Delta M_c$ 由 H 壳燃烧率决定：原文 p.27
$$ \Delta M_c \;\approx\; \frac{L_{\mathrm{H-shell}}}{\varepsilon_H}\,\Delta t_{\mathrm{interpulse}} $$

[FACT] **HBB 判据**：包络底部温度 $T_{\rm base} \gtrsim 3\times 10^7$ K 点燃 pp + CNO（M $\gtrsim$ 4.5M$\odot$）：原文 p.20
$$ T_{\rm base} \;\gtrsim\; 3\times 10^{7}\,\mathrm{K}, \qquad M \gtrsim 4.5\,M_\odot \text{ (Z=0.02)} $$

[FACT] **HBB 寿命**：HBB 型 AGB 演化寿命仅 ~100 Myr：原文 p.4
$$ \tau_{\mathrm{HBB-AGB}} \;\approx\; 100\,\mathrm{Myr} $$

[FACT] **C 星条件（表面数比）**：原文 p.4
$$ \frac{n(^{12}\mathrm{C})}{n(^{16}\mathrm{O})} \;\geq\; 1 \qquad \Longleftrightarrow\qquad \text{carbon star} $$

[FACT] **HBB 破坏速率 vs TDU 注入速率**：最亮 C 星要求：原文 p.28
$$ \frac{dX(^{12}\mathrm{C})}{dt}\bigg|_{\mathrm{TDU}} \;>\; \frac{dX(^{12}\mathrm{C})}{dt}\bigg|_{\mathrm{HBB}\,\mathrm{burn}} $$
