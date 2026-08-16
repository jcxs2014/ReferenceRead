# 99. Final Summary — Nomoto, Kobayashi & Tominaga (2013)

> 上一章：[[03_stellar-nucleosynthesis/0020_nomoto-2013/literature_analysis/98_vocabulary.md|98_vocabulary]]

## 一句话总结

> Nomoto, Kobayashi & Tominaga (2013) RAA 综述了恒星核合成与星系化学富化，提出**Yields Table 2013**（统一 Pop III/CC-SN/AGB/SN Ia 产额表），并用 EMP 星丰度模式和 GCE 模型对其进行双向约束：Hypernova 是 EMP "plateau" 族的主导前身星，EC-SN/faint SN 解释了 [Zn/Fe] 平直，AGB 星是 s 过程主要 site，SN Ia 主导 Mn 等铁峰元素演化。

## 核心结论

1. **[FACT]** 自 BBN 之后，宇宙中几乎所有 Z>2 元素都在恒星中合成；B²FH (1957) 提出的核合成框架在 2013 年已被**定量产额表** (Yields Table 2013) 完成。
2. **[FACT]** 恒星质量的"命运图"（§4.1）：8–10 M☉ EC-SN, 10–25 M☉ 普通 CC-SN, 25–40 M☉ Hypernova, 40–140 M☉ 失败 SN, 140–260 M☉ PISN, >260 M☉ IMBH 直接坍缩。
3. **[FACT]** CC-SN 产额由 $T_p$ 分区 + $M_{\text{cut}}$ + $Y_e$ 三个物理量决定（§3.3），爆炸核合成形成从 O 到 Ni 的完整温度阶梯。
4. **[FACT]** **Mixing-fallback 参数化** 是产额表的核心唯象工具（§3.2），扫描 $(M_{\text{ZAMS}}, E, M_{\text{cut}}, \Delta M_{\text{mix}})$ 四参数拟合 EMP 星。
5. **[FACT]** **EMP 星 Plateau 族**（[α/Fe] 平直，[O/Fe]≈0）的最佳前身星是 25–40 M☉ Pop III Hypernova（§8.2.1）。
6. **[FACT]** **CEMP-no 星**（C 富集但无 s 过程）是 Pop III 前身星的直接候选——最佳拟合是 25 M☉ Hypernova 或低质量 EC-SN。
7. **[FACT]** **Zn 平直**（[Zn/Fe] 在 −4 < [Fe/H] < 0 近似常数）需要 EC-SN/faint SN 作为 Zn 主要来源——传统模型（Zn 归 SN Ia）不能解释。
8. **[FACT]** **Mn 是 SN Ia 的诊断元素**：低 [Fe/H] 处 [Mn/Fe] 下降 → SN Ia 尚未出现；knee 之后 → SN Ia 主导。
9. **[FACT]** **GCE 模型** 用 Yields Table 2013 自洽复现太阳邻域、Bulge、Thick Disk、Halo、DWARF、DAMP、椭圆星系的 8 个元素族的演化——这是产额表的定量成功。
10. **[FACT]** **Galactic Archaeology**（银河系考古学）将每颗贫金属星作为"化学化石"，通过大样本巡天（HERMES, APOGEE, GALAH）反推 Pop III 与早期 GCE。

## 最重要公式

$$ Y_i \equiv M_{i,\text{wind}} - M_{i,\text{initial}} \qquad \text{（AGB 产额定义）} $$

$$ \frac{d(M_g Z_i)}{dt} = \psi_{\text{in}} Z_{i,\text{in}} - \psi_{\text{SFR}} Z_{i,\text{ISM}} + \int \psi(t') \tau(t') Y_i(M, Z) \, dM \, dZ \qquad \text{（GCE 方程）} $$

$$ \tau_{n\gamma} = \frac{1}{n_n \langle\sigma v\rangle} \gg \tau_\beta \qquad \text{（s 过程判据）} $$

## 核心数值

| 物理量 | 数值 | 出处 |
|---|---|---|
| EC-SN 触发密度 | $\rho_c \sim 4\times10^9$ g cm⁻³ | §2.3.2 |
| EC-SN 能量 | $E \sim 10^{50}$ erg | §2.3.2 |
| 普通 CC-SN 能量 | $E \sim 10^{51}$ erg (1 foe) | §3.4 |
| Hypernova 能量 | $E \sim 10^{52}$ erg | §4.5.1 |
| 25 M☉ Pop III Hypernova $M_{\text{Fe}}$ | 0.4 M☉ | §4.5.1 |
| 25 M☉ Pop III normal $M_{\text{Fe}}$ | 0.07 M☉ | §4.5.1 |
| $M_{\text{up,Ne}}$ | $9\pm1$ M☉ | §2.3.1 |
| Chandrasekhar 极限 | ~1.4 M☉ | §6.1 |
| PISN 前身星 | 140–260 M☉ | §5.1 |
| IMBH 前身星 | ≥300 M☉ | §5.2 |
| HE 1327-2326 [Fe/H] | −5.24 | §8.5.1 |
| HE 0107-5240 [Fe/H] | −5.6 | §8.5.1 |
| EMP Plateau 前身星 | 25–40 M☉ Pop III | §8.2.1 |

## 分章核心内容

- **§01** Introduction：B²FH 传统 + EMP/GCE/GRB 三前沿
- **§02** AGB 星：Yields Table 定义 + EC-SN 物理
- **§03** CC-SN 爆炸核合成：$T_p$ 分区 + Mixing-fallback
- **§04** 大质量星产额表：(M, Z, E) 网格
- **§05** 极重星：PISN + IMBH
- **§06** SN Ia：Chandra/Sub-Chandra + SD/DD
- **§07** GCE：8 元素族的演化
- **§08** EMP 星约束：Hypernova/CEMP/HE 1327-2326
- **§09** 银河系考古学巡天
- **§10** 展望（JWST / APOGEE / 旋转产额）

## 主要局限

- [CRITIQUE] Mixing-fallback 是唯象——3D 流体不稳定性未纳入
- [CRITIQUE] Yields Table 未含旋转、双星相互作用
- [CRITIQUE] Z=0 AGB $M>3.5$ M☉ 无金属假设"可能不成立"
- [CRITIQUE] CEMP-no 起源仍开放
- [CRITIQUE] GCE outflow 参数敏感

## 与相关工作的关系

> 本综述在主题内（恒星核合成）与其他论文的关系在 `00_overview.md` 「前序阅读 / 关联论文」段列出。

---

## 25. Completeness Check

- [x] Abstract（§00_overview Frontmatter）
- [x] Introduction（§01）
- [x] All main sections（§1–§10，10 个正文章节）
- [x] Methods（Mixing-fallback、GCE 方程）
- [x] Data（Yields Table 2013）
- [x] Background（B²FH、Cameron、Wallerstein 传统）
- [x] Signal（EMP 星丰度模式）
- [x] Statistics（54/54 子节镜像覆盖）
- [x] Systematics（GCE outflow、$M_{\text{cut}}$ 不确定性）
- [x] Results（Plateau 族 = Hypernova 等定量结论）
- [x] Discussion（CEMP-no 起源、Pop III IMF）
- [x] Conclusion（§10 Future Outlook）
- [x] Appendix（Yields Table 2013）
- [x] Figures（Fig. 1–19 索引于 00_overview）
- [x] Tables（Yields Table 2013 + 文中嵌入表）
- [x] Important equations（产额定义、GCE 方程、s 过程判据）
- [x] Important numerical values（能量、质量、密度、丰度）
- [x] Important references（B²FH 1957、Käppeler 2011、Wallerstein 1997、Cowan 2021、Eichler 1989）
