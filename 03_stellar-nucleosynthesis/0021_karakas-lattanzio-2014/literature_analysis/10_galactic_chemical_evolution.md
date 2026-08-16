# 10. Galactic Chemical Enrichment（§5.2 银河化学增丰）

**上一章**: [09_yield_tables.md](09_yield_tables.md) · **下一章**: [11_conclusions.md](11_conclusions.md)

## 10.1 银河化学演化的多源模型

[FACT] 银河系化学演化由多源贡献共同塑造：
- **核心坍缩超新星**（Type II）：α-元素（O、Mg、Si、Ti）+ Fe-peak，时标 ≲ 10⁷ 年；
- **经典新星**（Romano & Matteucci 2003）：C、N、重元素，最早期；
- **快速旋转大质量恒星**：早期 C、N（Chiappini et al. 2003, 2006；Hirschi 2007）；
- **Type Ia SN**：Fe 主要来源，时标 0.1 Gyr 到几 Gyr（Matteucci & Greggio 1986；Bonaparte et al. 2013）；
- **低中质量 AGB 恒星**：C、N、F、Na、s-过程重元素，时标 10⁸–10¹⁰ 年。

[FACT] Travaglio et al. 2001a；Romano et al. 2010 是本文引用的化学演化框架。

## 10.2 AGB 在银河增丰中的角色

[FACT] 银河系 [C/Fe]、[N/Fe]、[Ba/Fe]、[Pb/Fe] 的 [X/Fe] vs [Fe/H] 演化曲线要求 AGB 贡献：
- ¹²C：AGB 是太阳邻域主要初级 C 源；
- ¹⁴N：AGB HBB 贡献中金属度下 ~50–60% 的初级 N；
- 重 s-过程元素（Ba、La、Pb）：AGB 主导；
- ²²Ne、²⁶Mg 富中子同位素：AGB 主要来源。

[FACT] Kobayashi et al. 2011b；Nomoto et al. 2013 提供更新的产额网格并用于化学演化模型。

## 10.3 观测驱动

[FACT] 当前/新一代观测巡天（SEGUE、GALAH、APOGEE、GAIA-ESO）提供银河系各区域数十万颗恒星光谱，将大幅检验 AGB 产额与化学演化模型的可靠性。

## 10.4 与引用相关

[FACT] **cowan-2021（03/0016）**：Cowan & Sneden 2021 综述 AGB s-过程与银河系 [Ba/Fe]、[Pb/Fe] 演化，明确引用本文 §3.7 讨论。

[FACT] **kaeppeler-2011（03/0017）**：Käppeler et al. 2011 (Rev. Mod. Phys.) s-过程综述引用本文 AGB s-过程产额模型。

## 关键数值

- AGB 对 ¹²C 银河贡献占比：~50–60%（太阳邻域）；
- AGB 对 s-过程 Ba 银河贡献占比：~80–100%；
- AGB 对 Pb 太阳系贡献：**91%**；
- AGB 对银河系尘埃贡献：~90%。

## 10.5 银河化学增丰关键方程（LaTeX）

[FACT] **封闭盒化学演化方程**（$Z$ 金属丰度，$R$ 回注率）：原文 p.72
$$ Z(t) \;=\; -\frac{y}{1-R}\,\ln\mu(t), \qquad \mu(t) = \frac{M_{\rm gas}(t)}{M_{\rm gas}(0)} $$

[FACT] **AGB 单核素产额定义**（恒星生命周期净注入）：原文 p.72
$$ m_i(Z) \;=\; m_i^{\rm surf}(t_{\rm end}) \;-\; m_i^{\rm initial} \qquad \Big[\mathrm{M_\odot}\Big] $$

[FACT] **银河系 [X/Fe] 时间积分**（多源贡献叠加）：原文 p.72
$$ \left[\frac{X}{\mathrm{Fe}}\right](t) \;=\; \log_{10}\!\frac{\dot{X}_{\rm CC-SN}+\dot{X}_{\rm Ia}+\dot{X}_{\rm AGB}+\cdots}{\dot{\mathrm{Fe}}_{\rm CC-SN}+\dot{\mathrm{Fe}}_{\rm Ia}+\cdots}\;-\;\left(\frac{X}{\mathrm{Fe}}\right)_\odot $$

[FACT] **AGB 延迟时间分布**（决定 [X/Fe] vs [Fe/H] 演化曲线的"膝"）：原文 p.72
$$ \tau_{\rm delay}(M,Z) \;\sim\; 10^{8}\text{--}10^{10}\,\mathrm{yr} \qquad (M \sim 1\text{--}4\,M_\odot) $$

[FACT] **AGB 贡献的太阳邻域比例**：原文 p.72
$$ f_{\rm AGB}(\,^{12}\mathrm{C}\,)_\odot \;\approx\; 50\text{--}60\%, \qquad f_{\rm AGB}(\,^{14}\mathrm{N}\,)_\odot \;\approx\; 50\text{--}60\% $$
$$ f_{\rm AGB}(\mathrm{Pb})_\odot \;\approx\; 91\%, \qquad f_{\rm AGB}(\mathrm{Ba/La})_\odot \;\approx\; 80\text{--}100\% $$

[FACT] **尘埃注入比例**：原文 p.3
$$ f_{\rm dust}(AGB) \;\approx\; 90\%, \qquad f_{\rm dust}(\text{massive}) \;\approx\; 10\% $$
