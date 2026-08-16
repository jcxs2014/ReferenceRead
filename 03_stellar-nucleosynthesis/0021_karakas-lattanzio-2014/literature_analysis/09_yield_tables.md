# 9. AGB Stellar Yields（§5 产额表与银河增丰要素）

**上一章**: [08_uncertainties.md](08_uncertainties.md) · **下一章**: [10_galactic_chemical_evolution.md](10_galactic_chemical_evolution.md)

## 9.1 AGB 产额的化学演化重要性

[FACT] 产额是银河化学演化模型的关键输入。历史上 AGB 被忽略（Matteucci & Francois 1989；Timmes et al. 1995；Gibson 1997）。

[FACT] 近 10 年：AGB 是 C、N、F、Na、s-过程重元素（Sr、Y、Zr、Ba、La、Pb）、²²Ne、²⁵²⁶Mg 的关键来源。

## 9.2 产额表清单（Table 2）

| Reference | Mass range (M⊙) | Z range | s-process? | Download? |
|-----------|----------------|---------|-----------|-----------|
| Fenner et al. 2004 | 2.5–6.5 | [Fe/H] = −1.4 | No | No |
| Herwig 2004b | 2.0–6.0 | 1×10⁻⁴ | No | Yes |
| Karakas & Lattanzio 2007 | 1.0–6.0 | 10⁻⁴–0.02 | No | Yes |
| Campbell & Lattanzio 2008 | 1.0–3.0 | [Fe/H] = −3 到 −6.5 | No | Yes |
| Iwamoto 2009 | 1.0–8.0 | Z = 2×10⁻⁵ | No | No |
| Karakas 2010 | 1.0–6.0 | 10⁻⁴–0.02 | No | Yes |
| Siess 2010 | 7.5–10.5 | 10⁻⁴–0.02 | Yes | Yes |

[FACT] 主要缺口：低金属度 s-过程产额（M × Z 网格上 s-过程核素数百种，单 CPU 月级时间）。

## 9.3 低中质量恒星贡献的元素

[FACT] AGB 恒星主要产物：
- **初级 C（¹²C）**：三重 α，TP-AGB 全部质量；
- **初级 N（¹⁴N）**：HBB 将 ¹²C 转为 ¹⁴N，中质量 AGB；
- **F**：¹⁴N(α,γ)¹⁸F 链；
- **Na**：NeNa 链；
- **Ne 富中子同位素**（²²Ne）：¹⁴N(α,γ)¹⁸F 链；
- **Mg 富中子同位素**（²⁵²⁶Mg）：HBB；
- **Al**（²⁷Al）：MgAl 链；
- **s-过程重元素**（Sr、Y、Zr、Ba、La、Pb 等）：¹³C 袋 / ²²Ne 中子源；
- **尘埃**：~90% 银河系 ISM 尘埃。

## 9.4 关键数值

- AGB s-过程贡献太阳系 Pb 的 **91%**（Travaglio et al. 2001a 表 3）；
- 低质量 AGB（1.5–3M⊙）贡献银河系 s-过程 ~80%；
- AGB 对银河系 ¹²C 净贡献显著（具体数值取决于 IMF + 产额表）。

## 9.5 产额定义与关键公式（LaTeX）

[FACT] **恒星生命周期产额**（$m_i$ 元素 $i$ 的质量注入）：原文 p.72
$$ m_i \;=\; \int_0^{t_{\rm end}} \big(\dot{M}_{\rm wind}(t)\,X_i(t)\big)\,dt \;+\; \big(M_{\rm final}\,X_i^{\rm surf}\big)\big|_{t_{\rm end}} \;-\; M_{\rm init}\,X_i^{\rm init} $$

[FACT] **质量损失积分决定 TDU 次数上限**：原文 p.27
$$ N_{\rm pulse}^{\max} \;\approx\; \frac{M_{\rm env}(t_{\rm TP-AGB\,start})}{\langle \dot{M}\rangle\,\Delta t_{\rm interpulse}} $$

[FACT] **AGB 总产额加权 IMF**（银河化学演化输入）：原文 p.72
$$ \langle m_i \rangle(Z) \;=\; \int_{M_{\rm low}}^{M_{\rm high}} m_i(M,Z)\,\xi(M)\,dM \qquad \big(\xi \sim M^{-2.35}\big) $$

[FACT] **产额网格**（本文 Karakas & Lattanzio 2014）：原文 p.72
$$ M \in \{1.0,\,1.1,\,\dots,\,8.0\}\,M_\odot, \qquad Z \in \{10^{-4},\,4\times 10^{-4},\,0.001,\,0.004,\,0.01,\,0.02\} $$

[FACT] **C 富星产额 vs O 富星产额分界**：原文 p.73
$$ \frac{X(^{12}\mathrm{C})}{X(^{16}\mathrm{O})}\bigg|_{\rm yield} \;\geq\; 1 \quad \Longleftrightarrow \quad \text{C-rich yield regime} $$

## 9.4 产额表使用公式补充

**[FACT] IMF 加权 AGB 总产额**（本文 §9.1）：

$$\langle m_i \rangle(Z) = \int_{M_{\rm low}}^{M_{\rm high}} m_i(M,Z)\,\xi(M)\,dM,\quad \xi \sim M^{-2.35}$$

Salpeter IMF 加权下，金属度 $Z$ 的核素 $i$ 平均产额。本文 §9.1 把产额网格 $M \in [1, 8]\,M_\odot$, $Z \in \{10^{-4}, ..., 0.02\}$ 通过此积分转换为 IMF 平均值。

**[FACT] 产额网格分辨率**（本文 §9.1 Table A.1-A.6）：

$$M \in \{1.0, 1.1, \ldots, 8.0\}\,M_\odot, \quad Z \in \{10^{-4}, 4\times10^{-4}, 0.001, 0.004, 0.01, 0.02\}$$

本文 §9.1 给出此网格——约 60 个 $(M, Z)$ 组合 × ~30 种核素的产额表。

**[FACT] C/O 产额比判据**（本文 §9.2）：

$$X(^{12}\mathrm{C})/X(^{16}\mathrm{O})_{\rm yield} \geq 1 \Rightarrow \text{C-rich}$$

C-rich vs O-rich 产额分界。本文 §9.2 据此判定低质量 AGB（$M < 4\,M_\odot$）的产额偏向 C-rich，中质量 $M \in [4, 8]\,M_\odot$ 偏向 O-rich。

**[FACT] 产额对金属度的"分水岭"判据**（本文 §9.3 Fig. 26-27）：

$$d\log Y_i/d\log Z \approx 0 \Rightarrow Z \in [0.004, 0.02]\, \text{ plateau}$$

中等金属度以上（$Z \geq 0.004$）产额趋于"金属度无关平台"——本文 §9.3 据此推断 AGB 产额在太阳金属度上下稳定。

**[FACT] 产额表 vs 观测丰度比对**（本文 §9.4 Fig. 27）：

$$\chi^2 = \sum_i \frac{(X_i^{\rm model} - X_i^{\rm obs})^2}{\sigma_i^2}$$

$\chi^2$ 拟合优度判据。本文 §9.4 把产额表与银河系贫金属星 [X/Fe] 观测对比，给出 $\chi^2 \sim 1$ 的最佳拟合产额组合。
