> 本章属于：Bhattacharjee & Sigl (1999), Phys. Rep. 320, 1–150
>
> 上一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/05_neutrinos_exotic_particles.md|05_neutrinos_exotic_particles.md]]
>
> 下一章：[[02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/07_source_search_transport.md|07_source_search_transport.md]]

---

# 6. Galactic & Extragalactic Magnetic Fields (§4.4, p. 27–30)

## 6.1 本节核心内容

- **同步辐射与级联**：EGMF 通过同步冷却抑制 EM cascade；临界转移能量 E_tr ~ $10^{20}$ (B/$10^{-10}$ G)⁻¹ eV。
- **带电强子偏转与延迟**：给出偏转角、延迟时间与能量/磁场关系的解析公式。
- **磁聚焦与多像**：EGMF 可产生类似引力透镜的多像效应。
- **源位置约束**：GZK 距离 <~50 Mpc + 偏转角 <~几度 → 到达方向应指向源。
- **Faraday rotation 约束**、宇宙大尺度结构约束（void, sheets, filaments）。

## 6.2 §4.4.1 Synchrotron Radiation & EM Cascades

### 6.2.1 同步辐射能量损失率 (公式 28) [FACT]

```
dE/dt = −(4/3) $\sigma_{\rm T}$ (B²/8$\pi$) (q m_e/m)^4 (E/m_e)²
```
- UHE 质子：**可忽略**。
- UHE 电子：同步损失在转移能量
```
E_tr ~ $10^{20}$ (B/$10^{-10}$ G)⁻¹ eV
```
以上占主导。

**物理图像**：当 E > E_tr，电子几乎瞬间通过同步辐射损失能量 → cascade 发展被阻断 → $\gamma$ 传播由 PP/DPP 吸收主导 → 可观测通量由"直接"（first-generation）$\gamma$ 决定 → 简化为式 (12) 用 l(E) 代替 l_E(E)。

### 6.2.2 同步辐射光子能量 (公式 29) [FACT]

```
E_syn ≃ $6.8\times10^{13}$ (E/$10^{21}$ eV)² (B/$10^{-9}$ G)  eV
```
- 经典极限下有效（E_syn ≪ E）。
- 约束来源：当 E_syn 落入已有 diffuse $\gamma$ 观测窗口时：
  - EGRET ~ 1 GeV [185]
  - HEGRA 上界 50–100 TeV [257]
  - CASA-MIA $6\times10^{14}$ – $6\times10^{16}$ eV [258]
- **具体例子**：强 discrete UHE $\gamma$ 源（如拓扑缺陷，近单能注入谱，EGMF ~$10^{-9}$ G）→ 在某些 E > ~$10^{16}$ eV 处预言 $\gamma$ 通量 > 带电 CR 通量 → **已被排除** [259]。

## 6.3 §4.4.2 Deflection and Delay of Charged Hadrons

### 6.3.1 单场偏转角 (公式 30) [FACT]

回旋半径 r_g ≃ E/(q e B_⊥)，在均匀场 B 传播距离 d：
```
$\theta$(E,d) ≃ d/r_g ≃ 0.52° · q · (E/$10^{20}$ eV)⁻¹ · (d/1 Mpc) · (B_⊥/$10^{-9}$ G)
```

### 6.3.2 随机场 rms 偏转角 (公式 31) [FACT]

磁场特征：rms 强度 B + 关联长度 l_c；d ≳ l_c 时：
```
$\theta$(E,d) ≃ (2 d l_c/9)^(1/2) / r_g
       ≃ 0.8° · q · (E/$10^{20}$ eV)⁻¹ · (d/10 Mpc)^(1/2) · (l_c/1 Mpc)^(1/2) · (B/$10^{-9}$ G)
```
- 数值系数来自解析处理 [260]。

**两种极限** [FACT]：
- **d·$\theta$ ≪ l_c**（相干）：所有能量粒子"看到"同一磁场实现 → 偏转一致，源像保持紧密 → 偏转方向偏离视线方向（coherent deflection）。
- **d·$\theta$ ≫ l_c**（漫散射）：源像被抹平，扩展范围 ~ $\theta$(E,d)，**但中心对准真实源方向**。
- **d·$\theta$ ≃ l_c**：可能产生**多像**（类似引力透镜）。

### 6.3.3 平均时间延迟 (公式 32) [FACT]

```
$\tau$(E,d) ≃ d·$\theta^{2}$/4 ≃ $1.5\times10^{3}$ q² · (E/$10^{20}$ eV)⁻² · (d/10 Mpc)² · (l_c/1 Mpc) · (B/$10^{-9}$ G)²  yr
```

**Bursting source 效应** [FACT]：由于 $\tau$ ∝ E⁻²，观测窗口内的瞬时谱与长时间平均谱不同，在
```
$\tau$($E_{0}$, d) ≃ (观测时刻 − 零延迟到达时刻)
```
处出现**谱峰 $E_{0}$**；高能粒子已过，低能粒子未至。

**谱宽度**：
- d < 相互作用长度 且 d$\theta$ ≪ l_c → 谱宽 ≪ $E_{0}$。
- 其他情形 → 谱宽 ~ $E_{0}$。

## 6.4 §4.5 Constraints on EHECR Source Locations

### 6.4.1 距离-角度约束 [FACT]

- **核子/核/$\gamma$ > 几十 EeV 起源距离 ≲ 50 Mpc**（GZK / 光致分裂 / PP-DPP）。
- 结合公式 (31) → 到达方向应**在几度内指向源** [12]。
- 银河盘内偏转可"反演修正"（银河磁场图的计算 [264,265]）。

### 6.4.2 Faraday Rotation 约束 (公式 33) [FACT]

**原版本**：B l_c^(1/2) ≲ $10^{-9}$ G Mpc^(1/2) [262,263]。

**修正版**（用 $\Omega_{\rm b}$ h² ≃ 0.02 替代 closure density，未结构宇宙）：
```
B ≲ $3\times10^{-7}$ ($\Omega_{\rm b}$ h²/0.02)⁻¹ (h/0.65) (l_c/Mpc)⁻^(1/2)  G
```
→ 更强偏转。

**大尺度结构修正**（Lyman-$\alpha$ forest 建模 + 磁通冻结）[267]：
```
B ≲ $10^{-9}$ – $10^{-8}$ G     (公式 34)
```
- 关联尺度从 Hubble 到 1 Mpc。
- sheets 和 voids 内最大场可达 ~$\mu$G [268,267,269]。

### 6.4.3 结论 [FACT]

- 若本地大尺度结构不强磁化 → UHE 核子偏转仍在度级。
- 但**超星系面强磁化**、或**近邻星团**（场强 $10^{-6}$ G [262–263,270]）、或**重核（如 Fe）** → 可能强烈偏转 [26]。
- 强磁化下，EGMF 磁透镜效应可影响 UHECR 源位置 [311,316]。

## 6.5 §4.6 Source Search for EHECR Events

### 6.5.1 单事件关联 [FACT]

**Fly's Eye 300 EeV 事件**（$3.2\times10^{20}$ eV）[26]：
| 候选源 | 距离 | 到达方向偏离 |
|---|---|---|
| Cen A | ~3 Mpc | ~136° |
| Virgo A | 13–26 Mpc | ~87° |
| M82 | 3.5 Mpc | ~37° |
| **MCG 8-11-11** (Seyfert) | 62–124 Mpc | **~10°** |
| **3C134** (FR II radio gal.) | 30–500 Mpc（不确定） | **~10°** |

- **3C147** (quasar, z~0.5) 在 Fly's Eye 事件误差箱内 → 曾建议为**中微子源** [72]。
- 中微子假设问题：$\sigma_\nu$N 在 $10^{20}$ eV 大气相互作用概率 ~$10^{-5}$。

**AGASA 最高能事件**：
- 中微子假设：**3C33** (FR II, ~300 Mpc)。
- 核子假设：**NGC 315** (FR I, ~100 Mpc)。
- 银晕 Fe 初级 + 扩展银晕磁场 → 银道面起源可能 [273]。

### 6.5.2 统计关联 [FACT]

| 数据 | 关联对象 | 结果 |
|---|---|---|
| Haverah Park + AGASA + VR + Yakutsk | Supergalactic Plane | **~3$\sigma$** 正相关（E > $4\times10^{19}$ eV）[79] |
| SUGAR 南半球 | 同 | 无显著相关 [80] |
| AGASA（最新）[81,83] | 20% EHECR 彼此 + SG 面 | 部分相关；其余各向同性 |
| 组合分析 [274,275] | 同 | 一致，但未定论 |
| CFA Redshift Catalog [278] | 50 Mpc 内星系 | 到达方向一致 |

**争议** [FACT]：
- [276] 指出 Haverah Park SG 面关联"过强"（对 Local Supercluster 之外的星系而言）→ [277,271] 提议大尺度结构中存在 $\mu$G 级场，沿 sheets/filaments 对齐 → **聚焦效应**。

### 6.5.3 GRB 关联 [FACT]

- 两最高能量事件在 BATSE GRB 误差箱内 [279]，但大样本无显著结果 [280]。
- 若 GRB 为银河尺度 → 反证 GRB 关联；若河外 → 需考虑大时间延迟（见 §5.3）。

### 6.5.4 其他关联 [FACT]

- Yakutsk EAS: UHECR (0.8–4)×$10^{19}$ eV 与**银道面脉冲星沿磁感线方向**统计显著相关 [283]。

## 6.6 [CRITIQUE] 1999 年后进展

- [FACT] **2017 年 Pierre Auger**：UHECR 到达方向与**近邻（~100 Mpc）AGN 分布**显著相关（2017, Nature 551, 56; 2018, PRD 98, 102003），但**与 star-forming galaxies (GWCR 样本) 相关性更强**（2020, Nature 583, 39）。
- [CRITIQUE] 这支持了 §5.2.1 中"射电星系/AGN 热斑"作为 UHECR 加速器的 Bottom-up 模型，与 Bhattacharjee & Sigl 1999 年的预期一致。
- [FACT] **EGMF 强度**：至今无直接测量；最新估计来自 FRB 偏振（FRB 190520B, 2020）→ EGMF ~ 0.1–1 nG，与公式 (34) 一致。

## 6.7 关键数值速查

| 量 | 值 |
|---|---|
| E_tr (同步冷却转移能) | $10^{20}$ (B/$10^{-10}$ G)⁻¹ eV |
| E_syn 典型值 | $6.8\times10^{13}$ (E/$10^{21}$ eV)² (B/$10^{-9}$ G) eV |
| $\theta$ (均匀场) | 0.52° q (E/$10^{20}$ eV)⁻¹ (d/1 Mpc) (B/$10^{-9}$ G) |
| $\theta$ (随机场) | 0.8° q (E/$10^{20}$ eV)⁻¹ (d/10 Mpc)^(1/2) (l_c/1 Mpc)^(1/2) (B/$10^{-9}$ G) |
| $\tau$ (随机场) | $1.5\times10^{3}$ q² (E/$10^{20}$ eV)⁻² (d/10 Mpc)² (l_c/1 Mpc) (B/$10^{-9}$ G)² yr |
| EGMF (Faraday, 原) | Bl_c^(1/2) ≲ $10^{-9}$ G Mpc^(1/2) |
| EGMF (修正) | B ≲ $10^{-9}$ – $10^{-8}$ G |
| 源距离约束 | ≲ 50 Mpc (对核子/核/$\gamma$ > 几十 EeV) |