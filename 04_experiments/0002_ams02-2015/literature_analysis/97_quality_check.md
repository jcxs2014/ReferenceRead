# 97. Quality Check — 完成度自查

> 文献：`0002_ams02-2015`（Aguilar et al. PRL 114, 171103, 2015）
> 自动生成：统计 `literature_analysis/` 下所有 Markdown 文件。

## 文件清单

| 组件 | 状态 |
|---|---|
| 00_overview.md | ✅ |
| 99_final_summary.md | ✅ |
| 98_vocabulary.md | ✅ |
| 正文章节文件 | 8 个（01–08，✅） |
| **合计** | **11 个分析文件** |

## 覆盖统计

| 项目 | 数量 | 说明 |
|---|---|---|
| 正文章节 | 8 | 01–08 路径 B 八段模板 |
| Figure 引用 | 4 | Fig.1 / Fig.2 / Fig.3 / Fig.4，逐图分析 |
| Table 引用 | 0 | 本文无表格；数据表在 Supplemental Material |
| 公式 | 6+ | 流强 (1)、单幂律 (2)、双幂律 (3)、谱指数 (4)、拟合公式、误差合并公式 |
| [FACT] | 26 | 事实陈述 |
| [INTERPRETATION] | 4 | 解读 |
| [CRITIQUE] | 12 | 批判 |

## 密度指标

| 指标 | 值 |
|---|---|
| 总词数（英文 + 中文分词） | ~1500 |
| [FACT] 数 | 26 |
| FACT 密度（/千字） | ~17.3 |
| 门槛（OBSERVATIONAL 豁免公式数） | 公式门槛已豁免 |

**注**：本文属 OBSERVATIONAL 名单（AMS-02 磁谱仪质子谱测量），公式门槛豁免，FACT 密度远高于 4.0 门槛。

## 数值核对（对照原文 PDF）

| 核对项 | 本文数值 | 原文 PDF | 结果 |
|---|---|---|---|
| 观测刚性范围 | 1 GV – 1.8 TV | 标题、Abstract、p.2 明确 "from 1 GV to 1.8 TV" | ✅ 一致 |
| 谱指数变硬 | $\gamma$ 在 $R \gtrsim 100$ GV 以上变硬 | 原文 p.7 "progressively hardens with rigidity above ~100 GV"（fulltext.txt 行 532–535） | ✅ 一致 |
| 双幂律拟合 | $\chi^2$/d.o.f. = 25/26 | 原文 p.6 "yields a $\chi^2$/d.o.f. = 25/26" | ✅ 一致 |
| 拟合参数 $R_0$ | $336^{+86}_{-76}$ GV (sys) | 原文 p.6 "$R_0 = 336^{+68}_{-64}$(fit) $^{+86}_{-76}$(sys)" | ✅ 一致 |
| 事件数 | $3.0\times10^{8}$ | 原文 p.3 "sample of $3.0\times10^{8}$ primary cosmic rays with $Z=+1$" | ✅ 一致 |

## 完成度评分

| 维度 | 得分 | 满分 |
|---|---|---|
| 元数据 (00_overview) | 1 | 1 |
| 总结 (99_final_summary) | 1 | 1 |
| 词汇表 (98_vocabulary) | 1 | 1 |
| 正文覆盖 | 2 | 2 |
| 图表完整性 | 2 | 2 |
| 批判性分析 | 2 | 2 |
| 数值核对 | 1 | 1 |
| **合计** | **10** | **10** |
