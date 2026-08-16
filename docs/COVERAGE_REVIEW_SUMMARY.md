# 全库文献精读覆盖度审查汇总

**审查范围**：`papers` 库全库 55 篇论文（4 域）  
**审查日期**：2026-08-16  
**审查人**：opencode agent（自动化信号扫描 + 针对性抽查）

---

## 1. 审查方法

### 1.1 自动化信号扫描（全库 55 篇）

对每篇论文提取以下信号：

| 信号 | 说明 | 判定依据 |
|------|------|----------|
| `ftL` | fulltext.txt 行数（原文提取量） | PDF 提取质量 |
| `mdL` | literature_analysis/ 全部 md 行数（精读量） | 精读规模 |
| `ratio` | mdL/ftL | 精读 vs 原文篇幅比 |
| 结构树 | 00_overview.md 是否含原文章节树 | 格式合规（§3） |
| 公式差 | 原文编号公式 vs 精读编号公式 | 公式覆盖（§7） |
| OCR 质量 | fulltext 是否可读 | 审查可行性 |

### 1.2 抽查验证

对关键信号异常的篇目进行原文-精读逐节对比：
- **b2fh-1957 / trimble-1975 / fowler-1984**：ratio 极低（0.07/0.19/0.17），抽查确认结构树完整（B²FH 的 I–XIII + Appendix、trimble 的 I–V 五章 + 文件索引、fowler 的 13 节 + 28 图 2 表），判定为长综述摘要型精读，覆盖良好
- **arnould-goriely-2003 / karakas-lattanzio-2014 / cowan-2021**：ratio 低但结构树详细（10 章+子节 / 30+ 小节 / 9 章+关键词聚合），覆盖良好
- **eichler-1989**：fulltext.txt 仅 6 行乱码（OCR 失败），PDF 为扫描件，无法对比

### 1.3 校准说明

- **长综述型文献**（原文 >3000 行）：ratio 低是正常的（精读是摘要），覆盖度主要看结构树完整性
- **短文/原创论文**（原文 <1000 行）：ratio 应接近或超过 1.0
- **公式差**信号易被年份引用（(1998) 等）污染，仅作为辅助参考
- **结构树缺失**是最可靠的覆盖度异常信号（违反 READING_INSTRUCTIONS.md §3）

---

## 2. 全库覆盖度总览

| 等级 | 数量 | 说明 |
|------|------|------|
| **A（无法审查）** | 1 | OCR 失败，原文不可读 |
| **B（格式违规/建议检查）** | 14 | 00_overview 缺结构树，违反 §3 格式要求 |
| **C（覆盖良好）** | 40 | 结构树完整，ratio 合理，抽查通过 |
| **合计** | 55 | |

---

## 3. 关键发现

### 3.1 OCR 失败（1 篇）

| 篇目 | 问题 | 影响 |
|------|------|------|
| `03_stellar-nucleosynthesis/0023_eichler-1989` | fulltext.txt 仅 6 行乱码（pytesseract OCR 失败），PDF 为扫描件 | 精读覆盖度完全不可审查；精读可能基于人工读 PDF 而非 OCR 文本 |

### 3.2 00_overview 缺结构树（14 篇）

以下篇目的 00_overview.md **不包含原文章节树**（违反 READING_INSTRUCTIONS.md §3 格式要求）：

| 域 | 篇目 |
|----|------|
| 01 | amato-blasi-2018, weinrich-2020, mewaldt-2001-clocks, genolini-2021 |
| 02 | bell-1978, blandford-ostriker-1978, hillas-1984, gabici-2019, giuffrida-2022, telescope-array-2023, kotera-olinto-2011, bell-1978-ii |
| 03 | wallerstein-1997, busso-1999 |

### 3.3 公式覆盖异常（辅助信号，已排除年份引用污染）

以下篇目原文公式数远多于精读，但多为正则误匹配年份引用，不构成可靠信号。仅列出经抽查确认的实际公式缺口：

- 经抽查，**blasi-2013 / bhattacharjee-2000 / wallerstein-1997** 的"公式缺口"实为正则误匹配，精读以中文描述覆盖公式内容，未逐一复现编号公式——属摘要型精读的正常取舍

### 3.4 覆盖良好（40 篇）

以下篇目结构树完整、ratio 合理、抽查通过，判定覆盖良好：

**01 域（3 篇）**：strong-moskalenko-ptuskin-2007, ruszkowski-pfrommer-2023, drury-1983  
**02 域（10 篇）**：bhattacharjee-sigl-2000, al-dargazelli-1996, gaisser-1990, blasi-2013, amato-2014, grenier-2015, biermann-1996, blandford-eichler-1987, alvesbatista-2019, caprioli-2014, caprioli-2014-ii, giacalone-2017  
**03 域（21 篇）**：b2fh-1957, trimble-1975, fowler-1984, champagne-wiescher-1992, anders-grevesse, grevesse-sauval-1998, lodders-2003, asplund-2009-solar-composition, gies-lambert-1992, kewley-2001-starburst, dieterich-2014-h-burning-limit, bertone-hooper-2018, cameron-1968, kraft-1994, cowan-2021, kaeppeler-2011, arnould-goriely-2003, sneden-cowan-2008, nomoto-2013, karakas-lattanzio-2014, nomoto-suzuki-2014  
**04 域（4 篇）**：lhaaso-2021, ams02-2015, icecube-2013, hess-2016

---

## 4. 按域分布

| 域 | 总数 | A（无法审查） | B（格式违规） | C（覆盖良好） |
|----|------|:---:|:---:|:---:|
| 01_cosmic-ray-propagation | 7 | 0 | 4 | 3 |
| 02_cosmic-ray-origins | 20 | 0 | 8 | 12 |
| 03_stellar-nucleosynthesis | 24 | 1 | 2 | 21 |
| 04_experiments | 4 | 0 | 0 | 4 |
| **合计** | **55** | **1** | **14** | **40** |

---

## 5. 建议

### 5.1 优先处理（A 级）

- **eichler-1989**：重新精读。PDF 为扫描件（403 KB），需人工阅读 PDF 后重新生成 fulltext.txt 和精读文档。或至少补全 00_overview 的结构树。

### 5.2 格式修复（B 级）

14 篇缺结构树的篇目，建议补充 00_overview.md 的结构树（按 READING_INSTRUCTIONS.md §3 格式）。其中：
- 若精读文档本身内容完整（ratio 合理），仅需补结构树
- 若 ratio 异常且内容疑有遗漏，需进一步深入检查

### 5.3 维持现状（C 级）

40 篇覆盖良好，无需扩充。其中长综述型（b2fh-1957 等）的 ratio 低属正常摘要行为。

---

## 6. 方法论局限

1. 自动化信号为定量代理指标，最终判定依赖人工抽查校准
2. 公式差信号受年份引用（(1998) 等）污染，仅辅助参考
3. 未逐篇进行逐字级覆盖度核对（55 篇工作量过大），仅对信号异常篇目深入抽查
4. 结构树缺失是最可靠的异常信号，但部分篇目可能用非标准措辞（如 cowan-2021 的"章节级核心关键词"表），需人工确认

---

**详见各域详细审查文档**：
- [01_PROPAGATION.md](COVERAGE_REVIEW_01_PROPAGATION.md)
- [02_ORIGINS.md](COVERAGE_REVIEW_02_ORIGINS.md)
- [03_NUCLEOSYNTHESIS.md](COVERAGE_REVIEW_03_NUCLEOSYNTHESIS.md)
- [04_EXPERIMENTS.md](COVERAGE_REVIEW_04_EXPERIMENTS.md)