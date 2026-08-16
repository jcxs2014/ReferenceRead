# 98. Vocabulary — 术语表

> 本章属于：[[00_overview.md]]
>
> 上一章：[[97_quality_check.md]]

---

## 探测器与仪器

| 术语 | 全称/中文 | 说明 |
|---|---|---|
| LHAASO | Large High Altitude Air Shower Observatory / 高海拔宇宙线观测站 | 位于稻城海子山（海拔 4,410 m），由 KM2A+WCDA+WFCTA 三套阵列组成 |
| KM2A | Kilometer Square Array / 平方公里阵列 | 表面宇宙线阵列，1 km²；含 ED 闪烁体 + MD 水中切伦科夫缪子 veto |
| ED | Electromagnetic detector / 电磁探测器 | 5,195 个塑料闪烁体计数器（15 m 网格） |
| MD | Muon detector / 缪子探测器 | 1,188 个地下水中切伦科夫探测器（30 m 网格，2.5 m 埋深） |
| WCDA | Water Cherenkov Detector Array / 水中切伦科夫探测器阵列 | 78,000 m²、4.5 m 水深；能量桥接 Fermi-LAT 与 KM2A |
| WFCTA | Wide Field-of-view Cherenkov Telescope Array / 广角切伦科夫望远镜阵列 | 18 台 16°×16° FoV 望远镜，50 TeV–100 PeV |
| PSF | Point Spread Function / 点扩展函数 | 源角分辨率度量，本文 68% containment = 0.45°–0.62° |
| N_μ/N_e | 缪子数/电磁粒子数比 | KM2A 的 γ/CR 判别量，cut <1/230 |

## 物理量

| 术语 | 说明 |
|---|---|
| PeVatron | PeV 能量加速器（10¹⁵ eV） |
| super-PeVatron | 加速至 >几 PeV 的源，膝区以上 CR 的可能来源 |
| CU | Crab Unit，蟹状星云在 100 TeV 的流量单位 = 6.1×10⁻¹⁷ photons TeV⁻¹ cm⁻² s⁻¹ |
| SED | Spectral Energy Distribution / 谱能量分布 |
| log-parabola | 对数抛物线谱 dN/dE ∝ E⁻Γ(E)，Γ(E)=a+b·logE |
| E_max | 最高能光子能量（表 1 中每个源） |
| E²dN/dE | 能量通量（积分灵敏度指标） |
| γ-γ absorption | γ-γ 对产生吸收，>100 TeV 主导于 CMB，<100 TeV 主导于 ISRF |
| π⁰ decay | 中性 π 介子衰变 γ，强子加速的"smoking gun" |
| Inverse Compton (IC) | 逆康普顿散射，轻子机制 UHE γ 的主要通道 |
| PWN | Pulsar Wind Nebula / 脉冲星风星云 |
| SNR | Supernova Remnant / 超新星遗迹 |
| DSA | Diffusive Shock Acceleration / 扩散激波加速（Bell 1978） |
| Hillas criterion | 加速极限判据 E_max ≲ ZeBLβ |
| knee | 银河宇宙线谱"膝区"（~3×10¹⁵ eV） |
| first/second knee | 初级/次级膝（CR 能谱拐点） |

## 方法学

| 术语 | 说明 |
|---|---|
| background-free | background 抑制至远低于 1 事件/观测时间 |
| direct integration method | 背景估计方法（Fleysher 2003; Bartoli 2013） |
| likelihood ratio test | 似然比检验（源+背景 vs. 背景-only 模型） |
| forward unfolding | 向前展开（用探测器响应矩阵重构真实谱） |
| AIC | Akaike Information Criterion / 模型选择判据 |
| TS | Test Statistic，√TS = σ |
| MC | Monte Carlo 模拟 |
| 4FGL | Fermi LAT 第八年源目录 |
| Pass 8 | Fermi LAT 数据处理版本 |

## 关键数值（供速查）

| 量 | 值 |
|---|---|
| 海拔 | 4,410 m |
| KM2A ED 网格 | 15 m |
| KM2A MD 网格 | 30 m |
| KM2A 面积 | 1 km²（+0.3 km² skirt） |
| ED 数 / MD 数 | 5,195 / 1,188 |
| MD 埋深 | 2.5 m（~20 辐射长度） |
| 有效运行时间 | 308.33 天（自 2019-12-27） |
| γ-like 事件数 | ~84,000 |
| 光子总数 >100 TeV | >530 |
| 最高能光子 | 1.4 PeV（J2032+4102） |
| 源数量 | 12 |
| 最低显著性 | 7σ |
| 角分辨率 >100 TeV | 15–20 角分 |
| 能量分辨率 >100 TeV | <14% |
| CR 抑制 @1 PeV | 10⁻⁵ |
| 积分灵敏度 | 10⁻¹⁴ erg cm⁻² s⁻¹ |
