# QUALITY_AUDIT_BATCH2_SUMMARY_2026-08-17
> 批次2（三域）精读质量审查汇总报告
> git SHA: `67bf54a2e73646365aecaf26b1f203704a7640ec`
> timestamp: 2026-08-17T21:44:44Z
> 审查者: Hermes Agent
> 定位: 只审不改

---

## 三域概览

| 域 | 篇数 | 均分 | P0 | P1 | P2 |
|---|---|---|---|---|---|
| 01 传播（批次1） | 7 | 25.0 | 0 | 3 | 2 |
| **02 起源（批次2）** | **20** | **26.9** | **1** | **16** | **0** |
| **03 核合成（批次2）** | **24** | **26.6** | **0** | **0** | **11** |
| **04 实验（批次2）** | **4** | **27.0** | **0** | **0** | **0** |
| **批次2 合计** | **48** | **26.8** | **1** | **16** | **11** |
| **全库 55 篇** | **55** | **26.5** | **1** | **19** | **13** |

---

## 批次2分数分布

| 分数段 | 篇数 |
|---|---|
| 30/30（满分） | 3（giuffrida-2022, alvesbatista-2019, caprioli-2014-ii） |
| 29/30 | 3（bell-1978标杆, gabici-2019, giacalone-2017） |
| 28/30 | 4（grenier-2015, hillas-1984, telescope-array-2023, caprioli-2014） |
| 27/30 | 9（03域14篇 + 04域4篇 + blandford-eichler） |
| 26/30 | 4（02域3篇 + 03域11篇） |
| 25/30 | 4（02域3篇 + 03域若干） |
| 24/30 | 1（biermann-1996） |
| 23/30 | 2（amato-2014, blandford-eichler-1987, bell-1978-ii） |

---

## P0 问题（阻塞项）

| # | 论文 | 问题 | 建议 |
|---|---|---|---|
| **1** | **bell-1978-ii（02域）** | **fulltext.txt 仅39行PDF下载头部，无正文——无法核实忠实性** | **必须重抽 fulltext（arXiv 1408.3338 或 ADS 源），再补 §98/§99（当前各仅16-21行）** |

---

## P1 问题（高优先级）

| # | 论文 | 问题 | 级别 |
|---|---|---|---|
| 1 | bell-1978-ii | fulltext 无效（见P0） | P0→P1 |
| 2 | bell-1978-ii | §99/§98/§00 各仅16/21/38行（fulltext修复后补） | P1 |
| 3 | blandford-eichler-1987 | 75页综述仅1524行（ratio 37%），密度差5倍 | P1 |
| 4 | amato-2014 | CRITIQUE仅12条（Blasi 2013有37条） | P1 |
| 5 | bhattacharjee-sigl-2000 | 99中目录名误记"longair-ptuskin-1999" | P1 |
| 6 | hillas-1984 | §03 L60 LaTeX语法错误 `\rac`→`\frac` | P1 |
| 7 | caprioli-2014 | §05/§07/§09 各仅35/34/28行 | P1 |
| 8 | blasi-2013 | 无批判章节（参照bell-1978的05_critical_assessment） | P1 |
| 9 | biermann-1996 | 无批判章节 | P1 |
| 10 | al-dargazelli-1996 | §2.2与§8表述张力无整体批判收束 | P1 |
| 11 | gaisser-1990 | Eq.(1)数值与SN供给功率数量级差异未澄清 | P1 |
| 12 | blandford-ostriker-1978 | 正文[FACT]/[INTERP]/[CRITIQUE]各仅3条（997行） | P1 |
| 13 | kotera-olinto-2011 | §00仅43行缺元数据，§98仅47行，§07合并双章 | P1 |
| 14 | telescope-array-2023 | §05结论仅66行 | P1 |
| 15 | bell-1978-ii | 结构树节缺（fulltext修复后补） | P1 |
| 16 | blandford-ostriker-1978 | 公式347条集中在末尾，未分散到逐节 | P2升级P1 |

**P1 合计: 16 处（批次2）**

---

## P2 问题（优化建议）

| 域 | 问题类型 | 篇数 |
|---|---|---|
| 02 起源 | 批判章节缺失（blasi/biermann） | 2 |
| 02 起源 | 薄覆盖（blandford-eichler/kotera-olinto/giacalone细节） | 3 |
| 03 核合成 | 综述体以复述为主，INTERPRETATION不足（b2fh/fowler/trimble等） | 11 |
| 03 核合成 | formula密度偏低（grevesse-sauval 6.3） | 1 |

**P2 合计: 17 处（批次2）**

---

## 三域共性问题

### 1. 批判章节结构缺失（02域）
bell-1978 的 `05_critical_assessment` 是02域标杆结构，但 blasi-2013、biermann-1996 等多篇缺失整体批判收束章节。

### 2. 薄覆盖类（02/03域）
- blandford-eichler-1987: 75页综述仅1524行（37%）
- kotera-olinto-2011: §00仅43行，§98仅47行
- 03域综述体：精读以复述为主，INTERPRETATION 批判性分析不足

### 3. fulltext 无效（02域）
bell-1978-ii 的 fulltext.txt 是无效的 PDF 下载头部记录，需重抽。

### 4. LaTeX 语法错误（02域）
hillas-1984 §03 存在 `\rac` 而非 `\frac` 的语法错误，导致公式渲染失败。

---

## 全库55篇总览

| 指标 | 批次1 | 批次2 | 合计 |
|---|---|---|---|
| 均分 | 25.0 | 26.8 | **26.5** |
| P0 | 0 | 1 | **1** |
| P1 | 3 | 16 | **19** |
| P2 | 2 | 17 | **19** |
| 满分(30) | 0 | 3 | **3** |
| ≥28分 | 1 | 10 | **11** |

---

## 批次1遗留 P1（未修复）

| 问题 | 论文 | 状态 |
|---|---|---|
| 97 公式统计 bug | amato-blasi-2018（及其他全库） | **待修复**（97_quality_check.py bug） |
| ratio 46% 过薄 | weinrich-2020 | 待修复 |
| 统计方法展开薄 | genolini-2021 | 待修复 |

---

## 审查结论

批次2（48篇）整体质量良好，均分26.8/30。

**必须修复（批次2 P0/P1）**：
1. **bell-1978-ii fulltext 重抽**（阻塞项）
2. **amato-2014 补批判章节**（CRITIQUE 12条 vs Blasi 37条）
3. **blandford-eichler-1987 补深**（75页综述仅1524行）
4. **hillas-1984 修复 LaTeX 语法**（`\rac`→`\frac`）
5. **bell-1978-ii 补 §98/§99**（fulltext 修复后）

**优化方向（批次2 P2 + 批次1 P1/P2）**：
1. 02域综述补批判章节（bell-1978 05_critical_assessment 结构推广）
2. 03域综述增加 INTERPRETATION 批判性分析
3. 全库 check_density 97_quality_check.py 公式统计 bug 修复
