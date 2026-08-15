# 8. VIII Piecing the Puzzle（拼图：宇宙学、结构形成与数值模拟）

> 本章属于：[Bertone & Hooper, History of Dark Matter, Rev. Mod. Phys. 90, 045002 (2018)]
>
> 上一章：[[03_stellar-nucleosynthesis/0013_bertone-hooper-2018/literature_analysis/07_dark_matter_particles.md|07_dark_matter_particles.md]]
>
> 下一章：[[03_stellar-nucleosynthesis/0013_bertone-hooper-2018/literature_analysis/09_hunt_for_dm.md|09_hunt_for_dm.md]]

---

## 8.1 A. Discrepancies at all scales

### 8.1.1 Finzi 1963 — 被忽视的先驱

- [FACT] Arrigo Finzi 1963 首篇**统一**讨论：Zwicky 1933（星系团）、van de Hulst 1957（M31 自转曲线）、银河系质量。
- [FACT] 提出对"重子暗物质"候选**逐一排除**。
- [FACT] 大胆建议：修改牛顿引力 → F ∝ r⁻³/²（即 MOND 的先驱！）。
- [FACT] 被忽略——50 年仅 ~50 次引用。
- [FACT] Sanders 2010 认为其结论**太激进**。

### 8.1.2 1974 两篇关键论文（回顾）

- [FACT] Einasto-Kaasik-Saar 1974（4 月 10 日）："Dynamic evidence on massive coronas of galaxies" —— 用 $10^{5}$ 星系对得出**星系总质量超恒星质量 10 倍**；并指出此可解释**星系团**质量差异。
- [FACT] Ostriker-Peebles-Yahil 1974（5 月 28 日）："The size and mass of galaxies, and the mass of the universe" —— 无新观测，综合已有自转曲线、星系对、矮星系、本星系群。引言原句：
  > "There are reasons, increasing in number and quality, to believe that the masses of ordinary galaxies may have been underestimated by a factor of 10 or more... the mean density of the Universe would have been underestimated by the same factor."

### 8.1.3 Faber-Gallagher 1979

- [FACT] 综述"Masses and mass-to-light ratios of galaxies" 固化观点：暗物质宇宙中**普遍存在且证据增强**。
- [FACT] 术语"massive envelope"（大质量包壳）。

## 8.2 B. Cosmology

### 8.2.1 Gott-Gunn-Schramm-Tinsley 1974 — "An unbound universe"

- [FACT] 结论：宇宙密度**不超过临界密度 1/10**。
- [FACT] 原文：
  > "A variety of arguments strongly suggest that the density of the universe is no more than a tenth of the value required for closure. Loopholes in this reasoning may exist, but if so, they are primordial and invisible, or perhaps just black."
- [FACT] 讨论低质量中微子（Cowsik-McClelland）但亦排除。

### 8.2.2 暴胀（Inflation）与平坦宇宙

- [FACT] 1980s 初暴胀（Guth 1981；Guth-Pi 1982；Hawking 1982；Linde 1982；Starobinsky 1982；Bardeen-Steinhardt-Turner 1983）首次给出**总量子密度预测**与**密度扰动谱**。
- [FACT] 由此开启与"平坦宇宙理论指令"的 10 年纠结（Davis et al. 1985）。
- [FACT] 星系团观测暗示 $\Omega$_m 远不足以闭合宇宙（White et al. 1993）。
- [FACT] 1998 宇宙加速膨胀发现（Riess 1998；Perlmutter 1999）——**暗能量**补齐差量。

### 8.2.3 Peebles 1982a — CMB 涨落约束

- [FACT] 指出若宇宙**只有重子物质**，CMB 涨落 ~$10^{-4}$ 无法形成观测结构；若**非重子弱相互作用粒子**占主导，密度涨落可在退耦前增长。
- [FACT] 此与后续数值模拟工作快速确立 **CDM 范式**。

## 8.3 C. Numerical Simulations

### 8.3.1 模拟史

| 年份 | 事件 |
|------|------|
| 1941 | Erik Holmberg 用 74 灯泡 + 光电池 + 电流计模拟双星系引力相互作用（模拟计算机先驱） |
| 1953 | Pasta-Ulam 用 Los Alamos 计算机首次做引力系统数值实验 |
| 1960s-1970s | N 从 ~100 增至 ~1000（von Hoerner, Aarseth, Peebles 1970, White 1976） |
| 1970 | Miller-Prendergast-Quirk、Hohl 1971：旋支盘**不稳定**（形成 bar、演化到椭球） |
| 1973 | Ostriker-Peebles：**嵌入大质量晕的旋转盘可稳定** |
| 1974 | Press-Schechter：首次尝试模拟宇宙膨胀背景下结构形成 |
| 1979-1983 | Aarseth-Turner-Gott 等大规模改进 |
| 1982 | **CfA 红移巡天**（Davis et al. 1982）首次给出大规模三维星系分布——首次可对比模拟输出 |

### 8.3.2 冷 vs 热暗物质（Hot vs Cold）

- [FACT] 粒子初始速度分布决定结构形成序列。
- [FACT] **热暗物质**（如标准模型中微子）：退耦温度 ≫ 质量 → 相对论 → 先形成**大尺度**结构，再碎片化（**top-down**）。
- [FACT] **冷暗物质**（如中性微子）：退耦温度 < 质量 → 非相对论 → 自由流长度短，可形成**低质量晕**（典型中性微子 ~$10^{-3}$ – $10^{-9}$ M⊙），**自下而上合并（hierarchical）**。
- [FACT] **白-Frenk-Davis 1983** 结合 CfA 巡天判定**标准模型中微子无法主导暗物质**。
- [FACT] **Blumenthal-Faber-Primack-Rees 1984**：
  > "a universe with ~10 times as much cold dark matter as baryonic matter provides a remarkably good fit to the observed universe. This model predicts roughly the observed mass range of galaxies, the dissipational nature of galaxy collapse, and the observed Faber-Jackson and Tully-Fisher relations."
- [FACT] **Davis-Efstathiou-Frenk-White 1985**：首次 CDM 宇宙学模拟，与 CfA 巡天相似。

### 8.3.3 NFW 普适晕密度分布（1996）

- [FACT] Navarro-Frenk-White 1996（ApJ 462, 563）——分析 CDM 模拟生成晕。
- [FACT] 关键句：
  > "The spherically averaged density profiles of all our halos can be fit over two decades in radius by scaling a simple universal profile. The characteristic overdensity of a halo, or equivalently its concentration, correlates strongly with halo mass in a way which reflects the mass dependence of the epoch of halo formation."
- [FACT] 该公式至今是**间接探测**主要基准（尽管内区因重子物理不准确）。

### 8.3.4 当代前沿

- [FACT] 现代模拟挑战：实现**重子物理**（气体流体演化、恒星形成、超新星/黑洞反馈）。
- [FACT] 尺度问题：亚秒差距（恒星形成）到 Gpc（宇宙结构）——用 **subgrid 参数**处理。
- [FACT] 例：Eagle 模拟（Schaye et al. 2015）——subgrid 参数拟合星系质量函数、中心黑洞-星系质量关系。

## 8.4 [CRITIQUE]

- [CRITIQUE] CDM 范式成功建立，但近 15 年出现若干"小尺度危机"：**missing satellites**（矮星系数量模拟多于观测）、**too-big-to-fail**（模拟中最大子晕比观测中亮）、**cusp-core**（NFW 中心尖峰 vs 观测核心）——作者在本综述中**未讨论**，仅聚焦于早期建立过程。
- [CRITIQUE] 2018 年时暗能量 + CDM 的 $\Lambda$CDM 范式已成标准宇宙学模型；作者未花篇幅讨论 $\Lambda$CDM 自身的理论困难（如**巧合问题**、**宇宙学常数问题**）。

## 8.5 关键数值与公式

| 量 | 值 | 来源 |
|-----|-----|------|
| CDM/baryon 质量比 | ~10 | Blumenthal et al. 1984 |
| 中性微子小晕质量范围 | ~$10^{-3}$ – $10^{-9}$ M⊙ | 综述 |
| CDM 冷暗物质密度参数 | $\Omega$_c h² ≈ 0.12（文中未直接给，可从 $\Omega$_b 对比得） | 综述 |