> 本章属于：Asplund et al. (2009) AGSS09
>
> 下一章：[[03_stellar-nucleosynthesis/0009_asplund-2009-solar-composition/literature_analysis/04_intermediate_ironpeak.md|04_intermediate_ironpeak.md]]

# 3. Light Elements: Li, Be, B, C, N, O（§3.1–3.4）

## 3.1 §3.0 光球丰度总述（前置）

- [FACT] 推荐值统一列于 **Table 1**（p.42）。
- [FACT] 定义：log ε_X = log(N_X / N_H) + 12，log ε_H = 12.00。
- [FACT] 作者**极其审慎**地选择谱线；可疑谱线会被剔除，以免增加离散度和偏高的混杂偏差。
- [FACT] 分析使用多个 1D + 3D 模型，并尽可能考虑 non-LTE。默认使用 **Trampedach et al. (2009) 3D 模型**。
- [FACT] 全部谱线列表在配套系列文章（A&A, Asplund et al. 2009a,b,c；Grevesse et al. 2009；Sauval et al. 2009；Scott et al. 2009b）。

## 3.2 §3.1 Lithium, Beryllium and Boron

### 3.2.1 Lithium

- [FACT] 太阳中 Li **比陨石值少 ~150 倍**（depletion 因子 ~150）。
- [FACT] Li I 670.8 nm 共振线极弱，且被 CN 和 Fe I 线严重混杂。
- [FACT] 推荐值来自 **Müller, Peytremann & de La Reza (1975)**，经 3D + non-LTE 修正（Asplund et al. 1999；Barklem, Belyaev & Asplund 2003）得到 log ε_Li = **1.05 ± 0.10**。
- [FACT] 太阳 Li 亏缺**无法用标准混合长对流模型解释**，需要**对流区以下的额外混合**（Brun, Turck-Chièze & Zahn 1999；Charbonnel & Talon 2005）。
- [INTERPRETATION] 太阳 Li 问题至今（~2009 年）仍是天体物理经典难题。

### 3.2.2 Beryllium

- [FACT] 早期 Chmielewski, Brault & Müller (1975) 认为 Be 亏缺约 2 倍；
- [FACT] Balachandran & Bell (1998) 指出 UV 中存在"missing opacity"，主要来自 Fe I 光致电离（Bell et al. 2001），重新分析后 Be 丰度**回到陨石值**：log ε_Be = **1.38 ± 0.09**（陨石 1.30 ± 0.03）。
- [FACT] Asplund (2004) 验证这一结论**不依赖** 1D/3D 模型选择；Be II 线**不受 non-LTE 影响**。

### 3.2.3 Boron

- [FACT] 唯一可用线 B I 249.7 nm 共振线（UV 区），同样受 missing opacity 困扰（Mg I 光致电离）。
- [FACT] Cunha & Smith (1999) 结合 3D + non-LTE 分析，给出 log ε_B = **2.70 ± 0.20**（陨石 2.79 ± 0.04）。
- [FACT] 3D 和 non-LTE 效应**量级相近、符号相反**，近似抵消。
- [CRITIQUE] 该值不确定性仍很大（0.2 dex），因 UV 密集混杂区。

## 3.3 §3.2 Carbon — 关键重元素之一

### 3.3.1 测定方法

- [FACT] 多种指示符：**[C I] 872.7 nm 禁线、C I 原子线、C₂ Swan 带、CH 电子/振转线、CO 分子**。
- [FACT] 推荐值 log ε_C = **8.43 ± 0.05**（Table 1），源自 Asplund et al. (2009a) 的 3D 结果（[C I] + C I + CH + C₂ 平均）。
- [FACT] 各种指示符高度一致（见 Table 2）：无明显的激发势或等值宽度趋势，**除了 C I 强线有弱趋势**（归因于强线 non-LTE 估计不足，Fabbian et al. 2006）。

### 3.3.2 与旧值对比

| 来源 | log ε_C | 方法 |
|---|---|---|
| AG89 | 8.56 ± 0.04 | HM 1D |
| Grevesse et al. (1991) | 8.60 ± 0.05 | HM |
| GS98 | 8.52 ± 0.06 | 修改温度 HM |
| AGS05 | 8.39 ± 0.04 | 3D |
| **AGSS09** | **8.43 ± 0.05** | 3D + non-LTE |

### 3.3.3 下修原因

- [FACT] 3D 模型比 HM 有更**冷的平均温度**（因温度不均匀性）→ 分子线丰度下降；
- [FACT] **Non-LTE 效应**显著影响 C I 线；
- [FACT] **新 gf 值**（Johansson et al. 2003 等）。
- [FACT] Scott et al. (2006) 用弱 CO 分子线 + 自洽 O 丰度确认低 C 值，并给出同位素比 **¹²C/¹³C = 86.8 ± 3.8**。

### 3.3.4 潜在问题

- [CRITIQUE] 只用了**1D non-LTE 修正**于 C I，但作者在 Asplund (2005) 中指出**3D 不均匀性会放大 non-LTE 效应**——完整 3D non-LTE 研究值得做。
- [CRITIQUE] 作者强调这一重要元素**需要独立 3D 模型组复核**（类比 O 的 Caffau et al. 2008a）。

## 3.4 §3.3 Nitrogen

- [FACT] [N I] 禁线在太阳光谱中太弱不可测。
- [FACT] 分析基于：**高激发 N I 线 + NH 振转线 + NH 纯转线 + CN 带**。
- [FACT] Non-LTE 效应较小：≈−0.05 dex（忽略 H 碰撞时，Caffau et al. 2009）。
- [FACT] 推荐值 log ε_N = **7.83 ± 0.05**（Sauval et al. 2009）。

### 3.4.1 与旧值对比

| 来源 | log ε_N |
|---|---|
| AG89 | 7.89 |
| GS98 | 7.92 |
| AGS05 | 7.83 |
| **AGSS09** | **7.83 ± 0.05** |

- [FACT] 比 GS98 **低 0.09 dex**，比 AG89 **低 0.22 dex**。

### 3.4.2 Caffau et al. (2009) vs Sauval et al. (2009)

- [FACT] Caffau et al. 用 co5bold 3D 模型对 N I 线的分析得到**高 0.05 dex** 的值，主要是**谱线选择不同**：
  - Sauval 剔除混杂线 → σ = 0.04 dex
  - Caffau 保留更多线 → σ = **0.12 dex**（明显偏高）
- [CRITIQUE] Caffau 未分析分子线，因此无法检验其 3D 模型在原子/分子一致性上的表现。

## 3.5 §3.4 Oxygen — 最重要的单个元素

### 3.5.1 历史下修轨迹

| 来源 | log ε_O |
|---|---|
| AG89 | 8.93 ± 0.04 |
| GS98 | 8.83 ± 0.06 |
| AGS05 | 8.66 |
| **AGSS09** | **8.69 ± 0.05** |

- [FACT] O 丰度 20 年间从 8.93 下修到 8.69，**降幅 ~0.24 dex**。

### 3.5.2 指示符与推荐值

- **[O I] 630.0 nm**：
  - Allende Prieto, Lambert & Asplund (2001) 用 3D + 辨识 Ni I 混杂 → 大幅下降
  - Ayres (2008) 用单帧 3D + 可变 Ni gf → **高 0.12 dex**（但用了过时 gf）
  - Caffau et al. (2008a) 用 co5bold 3D + 固定 Ni → 确认低值
  - Scott et al. (2009a) 先测 Ni 丰度再预测 Ni I 贡献 → 更自洽
  - Asplund et al. (2009c) 更新后 630 nm 给出 **8.66**
- **[O I] 636.3 nm**：被 Ca I 自电离线和 CN 混杂；Asplund et al. (2009c) 给出略高值（与 630 一致）
- **[O I] 557.7 nm**：下能级微激发 → 对模型依赖小；被 C₂ 严重混杂
- **[O I] 三线平均**：log ε_O = **8.70 ± 0.05**
- **O I 777 nm 三重线**（许可，高激发）：
  - **Non-LTE 效应显著**，依赖 **S_H**（H 碰撞 Drawin 缩放因子）
  - Pereira, Asplund & Kiselman (2009) 通过中心-边缘变化确定 **S_H = 1 略优于 S_H = 0**，LTE 可被高置信排除（Fig 5）
  - Asplund et al. (2009c) 用 3D non-LTE + S_H = 1 + 新 Barklem (2007a) 电子碰撞截面 → log ε_O = **8.69 ± 0.05**
  - Caffau et al. (2008a) 用 3D + 1D non-LTE + S_H = 1/3 → 8.73 ± 0.06；S_H = 1 时应为 8.75（差 0.06）
- **OH 分子线**（Grevesse, Sauval & van Dishoeck 1984 引入）：
  - 振转线：8.69 ± 0.03（无趋势）
  - 纯转线：8.69 ± 0.03（趋势存在但减弱且方向反转）

### 3.5.3 最终推荐

- [FACT] log ε_O = **8.69 ± 0.05**，是 [O I]、O I、OH 振转、OH 纯转的平均。
- [FACT] 各指示符在 3D 模型下**非常自洽**（Table 2），而 HM 1D 模型下不一致。

### 3.5.4 太阳黑子方法

- [FACT] Centeno & Socas-Navarro (2008) 用 [O I] 630 nm 的**谱偏振**（太阳黑子）分离 Ni I 贡献 → log ε_O = **8.86**（偏高）。
- [CRITIQUE] Scott et al. (2009a) 指出：他们用了**过时的 [O I] gf**；用更新 Ni 丰度和替代 CO 处理得到 **8.71**；用替代黑子模型后更低。

### 3.5.5 同位素

- [FACT] Scott et al. (2006) 用 CO 线得 **¹⁶O/¹⁸O = 479 ± 29**（接近地球值 498.7，但误差大）。
- [CRITIQUE] Ayres, Plymate & Keller (2006) 得明显低值 ¹⁶O/¹⁸O = 440 ± 20，可能因 1D 模型未正确处理不同同位素异构体的温度敏感性。

## 3.6 小结与判断

- [FACT] C, N, O 丰度在 3D + non-LTE 框架下都**显著低于**旧值。
- [FACT] 内洽性极好：各种原子+分子指示符一致性高，是下修"真实"的最有力证据。
- [CRITIQUE] 主要残余不确定性：
  - C I 的 3D non-LTE 仍缺
  - O 的 S_H 不确定（虽 S_H=1 略优）
  - B, Li 的 UV 区 missing opacity