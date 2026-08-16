---
title: README
category: 背景知识
status: completed
read_date: '2026-08-12'
lastread: '2026-08-12'
tags:
- README
citations: []
path: background/README.md
---
# Background — 背景知识体系

基于 55 篇文献精读的系统整理，按主题组织为背景知识文档体系（首页/速查/三综述/批判索引/术语表/争议演化/实验全景）。

## 文档索引

| 文档 | 内容 | 对应论文 | 页数 |
|---|---|---|---|
| [`00_home.md`](00_home.md) | 库首页：主题域分布与导航 | — | 81 行 |
| [`00_key_values.md`](00_key_values.md) | 关键数值速查（全库 55 篇） | 55 篇 | 468 行 |
| [`01_cosmic_rays.md`](01_cosmic_rays.md) | 宇宙线传播、加速、观测约束、UHECR、星系 CR | 14 篇（01×1 + 02×13） | 702 行 |
| [`02_nucleosynthesis.md`](02_nucleosynthesis.md) | 恒星核合成：核过程框架（H/He燃烧→s/r/p过程） | 13 篇（03×13） | 935 行 |
| [`03_astrophysics.md`](03_astrophysics.md) | 太阳丰度、恒星丰度观测、星暴星系、暗物质 | 11 篇（03×7 + 04×4） | 668 行 |
| [`04_critique_index.md`](04_critique_index.md) | 批判性观点索引（全库 35 篇 CRITIQUE） | 35 篇 | 440 行 |
| [`05_glossary.md`](05_glossary.md) | 术语表（全库 55 篇，含新增 14 篇核心术语） | 55 篇 | 1291 行 |
| [`06_controversy_evolution.md`](06_controversy_evolution.md) | 争议演化时间线（含 §10 现代实验裁决） | 55 篇 | 183 行 |
| [`07_experimental_panorama.md`](07_experimental_panorama.md) | 实验观测全景：LHAASO/AMS-02/IceCube/HESS 方法、测量、理论约束 | 4 篇（04×4） | 101 行 |

## 主题交叉关系

```
宇宙线物理 (01) ──宇宙线散裂产生 Li/Be/B──→ 核合成 (02 §2.8 x 过程)
                          │
                          ↓
               CR-ISM 相互作用影响星系化学演化
                          │
                          ↓
               星暴星系 (03 §6) 与 CR 驱动星系风 (01 §1.5.2)
               
太阳丰度 (03 §1-2) ──提供基准丰度──→ 核合成模型 (02 §2.10 化学演化)
                          │
                          ↓
               C/O 比影响 s 过程预言 (02 §2.5)
               AGSS09 金属丰度下调 30% 影响恒星演化模型 (03 §1.5)
               
暗物质 (03 §8) ──宇宙线正电子超额──→ 宇宙线传播 (01 §1.3.5 反质子与正电子)
```

## 关键公式索引

| 公式 | 所在文档 | 用途 |
|---|---|---|
| CR 传播方程 (1) | `01_cosmic_rays.md` §1.1.1 | 宇宙线传播理论核心 |
| DSA 谱指数 $\alpha$ = 3r/(r-1) | `01_cosmic_rays.md` §1.2.1 | 激波加速 |
| 丰度标度 A_el = log(N_el/N_H) + 12 | `03_astrophysics.md` §1.6 | 太阳丰度标度 |
| 3$\alpha$ 反应率 | `02_nucleosynthesis.md` §2.3.1 | 氦燃烧 |
| s 过程稳态流 $\sigma$N = const | `02_nucleosynthesis.md` §2.5.2 | 慢中子俘获 |
| 封闭箱模型 Z = y·ln(1/$\mu$) | `02_nucleosynthesis.md` §2.10.1 | 化学演化 |

## 文献阅读顺序建议

1. **入门**：从 `03_astrophysics.md` §1 太阳丰度开始 → 建立"丰度"概念
2. **核合成**：接 `02_nucleosynthesis.md` 理解元素从何而来
3. **宇宙线**：再读 `01_cosmic_rays.md` 理解宇宙线物理
4. **深入**：回到各篇论文的 `literature_analysis/` 精读原文

> 最后更新：2026-08-16
