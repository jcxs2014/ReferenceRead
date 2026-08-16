## [FACT] 2.1 事件选择核心策略

**在探测器内部首次看到光（in-fiducial-volume first light）**——这是本分析排除大气 μ 背景的关键几何判据。

事件入选条件（原文 p.1242856-4–5）：
1. **first light 位于 fiducial volume 内**（Fig.1），而非在边界/ veto 层
2. **总收集 PMT 电荷 Q_tot ≥ 6000 photoelectron**（Fig.6）
3. **veto 层内首个 250 photoelectron 中，触发 ≤ 3 个 PMT**（即未检测到进入径迹）

原文（p.5）关键数值：
- 该选择在 >6000 photoelectron 时 **veto 掉 99.999% 的 μ 背景**
- 同时对 fiducial 体积内数百 TeV 以上相互作用的中微子 **nearly full efficiency**

## [FACT] 2.2 背景模型组成

**总预期背景 10.6<sup>+5.0</sup><sub>−3.6</sub> 起**（原文 p.1242856-2，"10.6<sup>+5.0</sup><sub>−3.6</sub>"）

| 背景分量 | 预期事件数 | 原文 p.1242856-1/2 |
|--------|---------|-----|
| 大气 μ（veto 穿透） | **6.0 ± 3.4** | p.2 |
| 大气 ν p/K（次级 π/K 衰变） | **6.1**（含南天抑制修正） | p.2 |
| 大气 ν charm（prompt 快成） | **+1.5**（benchmark Enberg et al. 2008, ref 6） | p.2 |
| **合计** | **10.6<sup>+5.0</sup><sub>−3.6</sub>** | p.2 |

## [FACT] 2.3 大气 μ 背景测量方法（data-driven）

**双 veto 层 + in-data 控制样本**（原文 p.1242856-5）：

1. 外层 IceCube 标记"进入事件"（tagged），rate 3 kHz（原文 p.4）
2. 统计标记事件中穿透下一层 veto 的概率 per-layer
3. 几何修正因子 ~2（分析 fiducial 体积比深层 fiducial 大 ~2×）
4. 在 Q_tot > 6000 photoelectron 区，**观测到 3 起穿透事件**
5. 由此外推：两年数据中 **预测 6.0 ± 3.4 起 veto-penetrating μ 事件**

原文（p.5）关键句："In our signal region above 6000 photoelectrons, we observed three tagged events passing the inner veto and so predict 6.0 ± 3.4 veto-penetrating muon events in the 2-year dataset."

## [FACT] 2.4 大气 ν 背景建模

**大气 ν p/K 组分**（原文 p.1242856-5）：
- 基于 Honda et al. 2007（ref 5）atmospheric ν flux 参数化
- 与 IceCube 北部天 μ ν 的低能测量一致（ref 8）
- 引入 **南天抑制修正**：CORSIKA（ref 26）模拟，高能同气簇中伴随 μ 可触发 μ veto，导致向下 ν 被抑制
- 系统不确定性：宇宙线能谱 +30% / −20%（ref 27，Gaisser 2012）
- 电磁能量刻度不确定度 5%（ref 8）
- 探测器线性贡献 T15%

** charm 组分**（原文 p.5）：
- 目前未被观测到，90% CL 上限 **3.4 起**（IceCube, ref 8）
- Benchmark 模型（Enberg et al. 2008, ref 6）贡献 +1.5 起
- Charm 贡献在 benchmark 与 3.8× benchmark（90% CL 上限）之间变化

## [FACT] 2.5 南天偏置（Northern vs Southern Hemisphere asymmetry）

原文（p.2）指出：大气 ν 主要来自同气簇伴随的 μ 触发 veto 后的**北方天事件**（因为向下 ν 往往伴随向下 μ 被 veto 掉）。而本分析中 **大部分事件来自南方天**——这对纯大气起源是强烈约束。

原文（p.3）："Most of our events, however, arrive from the south. This places a strong model-independent constraint on any atmospheric neutrino production mechanism as an explanation for our data."

## [FACT] 2.6 盲分析设计

为**防止确认偏倚（confirmation bias）**：
- 选择标准在 **10% 子样本**上设计完成
- 全部数据拆为**两个独立样本**：
  - 早前报告：2 起最高能量 PeV 事件（Science 111, 021103，2013）
  - 本次报告：**26 起新增事件**

## [INTERPRETATION] 背景建模评价

该背景建模体现了粒子天体物理实验的成熟范式：
1. **数据驱动（data-driven）** 的 μ 背景：不依赖 MC 模拟，直接用控制样本
2. **理论 + 实验约束** 的 ν 背景：Honda 参数化 + 90% CL 上限
3. **盲分析流程**：先定标准，再看数据

但 charm ν 分量的不确定性（±3.8×）是主要系统误差来源——这也是 IceCube 此后多年专门针对 charm ν 进行的观测工作（"view of prompt atmospheric neutrinos"）的背景。

## [FACT] 2.7 灵敏度能量域

原文（p.2）："We obtained nearly full efficiency for interacting neutrinos above several hundred TeV, with some sensitivity extending to neutrino energies as low as 30 TeV."

- 能量阈值：**30 TeV**（约等于 EM 沉积能量）
- 全效率域：**> 数百 TeV**
- 该阈值由 Q_tot ≥ 6000 photoelectron 决定

## 精读来源

- 原文 "Materials and Methods" § Event Selection, § Atmospheric Muon Background, § Atmospheric Neutrinos（p.1242856-4–5）
- Table 1 事件列表
- Fig.6 PMT 电荷分布