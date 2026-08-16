## [FACT] 5.1 点源搜索方法

**最大似然点源分析（maximum likelihood point source analysis）**（原文 p.1242856-4）：

- 对全天每个天球坐标点，检验点源假设
- 使用每个事件的全天重建不确定度图（uncertainty maps）
- 得到 TS（Test Statistic）天空图：**TS = 2 log(L/L<sub>0</sub>)**，其中 L 为最大似然，L<sub>0</sub> 为 null hypothesis 似然（原文 p.4）
- 试遍效应的显著性评估：将事件赤经（RA）随机化，重复分析，用随机化图 TS 分布估计显著性（原文 p.4）

## [FACT] 5.2 全天 TS 图结果

**未达显著性**（原文 Fig.5 caption, p.1242856-4）：

| 项目 | 数值 | 原文 |
|------|------|-----|
| 最强聚类 TS 位置 | RA = 281°，Decl = −23° | p.4 |
| 对应银道坐标 | l = +12°，b = −9° | p.4 |
| 参与事件 | **5 起**（全部 shower，含第 2 高能量事件） | p.4 |
| **最终显著性** | **8%**（= 1.4σ，不显著） | p.4 |
| 银河系中心位置 TS 显著性 | **5.4%** | p.4 |

原文（Fig.5 caption）："The most significant cluster consists of five events — all showers and including the second highest energy event in the sample — with a final significance of 8%. This is not sufficient to identify any neutrino sources from the clustering study."

## [FACT] 5.3 银道面相关分析

**银道面匹配分析**（原文 p.1242856-4）：

- 对每起事件的全方向重建不确定度，定义与银道面的重叠度
- 银道面宽度 **T2.5°**（基于 TeV γ 射线观测，ref 15）
- 使用 sum of log-likelihood 值的多聚类搜索
- 未达显著性

## [FACT] 5.4 时间聚类搜索

**两次时间聚类测试**（原文 p.1242856-4）：

- 测试方法：将观测事件到达时间与均匀分布的随机时间比较
- 全部事件：**无显著时间聚类**
- 对每个含 >1 事件的聚类单独做时间聚类检验（8 个区域测试）
- 最显著一对（含最高能量 shower）：**与随机涨落一致**
- 最密集聚类的 5 起 shower 事件：**无显著时间聚类**

## [FACT] 5.5 银河系中心候选评估

**银河中心（Galactic Center）方向**（原文 p.4）：
- 最强聚类的 TS 位置（RA=281°, Dec=−23°）与银心方向（~l=0°, b=0°）接近
- 但银心位置的 TS 显著性仅 **5.4%**
- **角分辨率不足以识别**：6 起 shower 事件的角分辨率 10°–15°，无法精确定位

原文（p.4）："The final significance, estimated as the fraction of randomized maps with a similar or higher TS anywhere in the sky, is 8%. This degree of clustering may be compatible with a source or sources in the galactic center region, but the poor angular resolution for showers and the wide distribution of the events do not allow the identification of any sources at this time."

## [FACT] 5.6 事件分布与天球

**事件空间分布**（原文 Fig.5, Table 1）：
- 28 起事件在全天较分散分布
- 5 起最强聚类位于南天 RA≈281°，Dec≈−23° 区域
- 含次高能量事件（event 20, 1433 TeV, Dec=−67.2°）
- 无事件集中到银道面以外的特定区域

## [FACT] 5.7 时间分布

**28 起事件的时间跨度**（Table 1 modified Julian date）：
- 最早：event 1，MJD 55351（~2010-05-20）
- 最晚：event 28，MJD 56049（~2012-05-20）
- 时间跨度：**~698 天**（涵盖 2010 年 5 月到 2012 年 5 月）

## [INTERPRETATION] 空间相关性分析的意义

**IceCube 2013 未能识别具体中微子源**——这是该分析的诚实边界。但这一"未能识别"本身也携带信息：

1. **角分辨率瓶颈**：shower 事件的 10°–15° 角分辨率是当时无法识别源的主因（track 事件仅 7 起，能量偏低）
2. **8% 的银心方向 TS**：虽不显著，但暗示银河中心方向可能包含中微子源（后续 IceCube-170922A 于 2017 年确认为 TXS 0506+056 blazar 源）
3. **无时间聚类**：暗示事件来源不是瞬时爆发型源（如 GRB），而是长期稳定的加速器
4. **与 HESS 2016 的衔接**：银河系中心方向的弥散 TeV γ 辐射（HESS 2016）与 IceCube 2013 的银心方向弱 TS 是同一物理过程的两个观测切面

## [FACT] 5.8 与后续 IceCube 结果的对比

**后续 IceCube 进展**（原文未包含，库内交叉参考）：
- **IceCube-170922A**（2017）：首个识别的中微子源——blazar **TXS 0506+056**（MAGIC、Fermi LAT 联合确认）
- **NGC 1068**（2022–2023）：邻近 Seyfert 星系被识别为高能 ν 源
- **IceCube-190720A**（2019）：指向 blazar **4C 30.20**

IceCube 2013 的"无法识别源"在 4 年后被 IceCube-170922A 打破。

## 精读来源

- 原文 p.1242856-4 Search for Neutrino Sources 节
- Fig.5 Sky map of TS
- Table 1 事件方向