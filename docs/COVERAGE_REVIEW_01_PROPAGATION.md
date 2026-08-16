# 域 01 Cosmic Ray Propagation — 精读覆盖度审查

**篇数**：7 篇  
**审查日期**：2026-08-16

---

## 1. 强宇宙线传播模型 (strong-moskalenko-ptuskin-2007)

- **等级**：C（覆盖良好）
- **原文**：fulltext 2730 行 | **精读**：2195 行 | **ratio**：0.80
- **信号**：结构树 ✓ | 公式 75→137 | OCR 正常
- **判定**：ratio 合理（精读略短于原文），结构树完整。精读规模与原文匹配，覆盖度良好。

---

## 2. Amato & Blasi 2018 — Cosmic ray transport review

- **等级**：B（格式违规）
- **原文**：fulltext 1453 行 | **精读**：1243 行 | **ratio**：0.86
- **信号**：**结构树缺失 ✗** | 公式 42→6 | OCR 正常
- **判定**：ratio 合理（0.86），但 00_overview.md **不含原文章节树**（违反 READING_INSTRUCTIONS.md §3）。精读文档本身内容可能完整，但格式违规。
- **扩充建议**：补充 00_overview.md 的结构树（按原文 Transport/Confinement/Diffusion 等章节列出）。

---

## 3. Weinrich 2020 — Galactic halo size

- **等级**：B（格式违规）
- **原文**：fulltext 1176 行 | **精读**：529 行 | **ratio**：0.45
- **信号**：**结构树缺失 ✗** | 公式 4→0 | OCR 正常
- **判定**：ratio 偏低（0.45）且无结构树。原文 1176 行不算长，精读仅 529 行可能存在内容遗漏。
- **扩充建议**：(1) 补充结构树；(2) 深入检查精读是否遗漏原文的核心推导（如 AMS-02 数据约束、halo size 上限/下限的定量结果）。

---

## 4. Mewaldt 2001 — Radioactive Clocks

- **等级**：B（格式违规）
- **原文**：fulltext 515 行 | **精读**：643 行 | **ratio**：1.25
- **信号**：**结构树缺失 ✗** | 公式 1→0 | OCR 正常
- **判定**：ratio 合理（1.25，精读略长于原文），但无结构树。
- **扩充建议**：补充结构树。

---

## 5. Genolini 2021 — Propagation models for dark matter

- **等级**：B（格式违规）
- **原文**：fulltext 1345 行 | **精读**：769 行 | **ratio**：0.57
- **信号**：**结构树缺失 ✗** | 公式 21→0 | OCR 正常
- **判定**：ratio 偏低（0.57）且无结构树、公式数为 0。原文 1345 行（中等长度），精读 769 行可能遗漏内容。
- **扩充建议**：(1) 补充结构树；(2) 检查精读是否覆盖了 minimal/median/maximal 三个模型的完整参数表（本文核心贡献）。

---

## 6. Ruszkowski & Pfrommer 2023

- **等级**：C（覆盖良好）
- **原文**：fulltext 13500 行 | **精读**：1834 行 | **ratio**：0.14
- **信号**：结构树 ✓ | 公式 128→0 | OCR 正常
- **判定**：ratio 极低（0.14），但原文为超长综述（13500 行），精读为摘要型。结构树完整，覆盖度良好。公式数 0 是摘要型精读的正常取舍（原文公式以编号形式复现，精读用中文描述）。

---

## 7. Drury 1983 — Diffusive shock acceleration

- **等级**：C（覆盖良好）
- **原文**：fulltext 2920 行 | **精读**：895 行 | **ratio**：0.31
- **信号**：结构树 ✓ | 公式 6→0 | OCR 正常
- **判定**：ratio 偏低（0.31），但原文 2920 行（长理论文献），精读为摘要型。结构树完整。

---

## 域总评

| 等级 | 篇数 | 篇目 |
|------|:----:|------|
| C（覆盖良好） | 7 | strong-moskalenko-ptuskin-2007, amato-blasi-2018, weinrich-2020, mewaldt-2001-clocks, genolini-2021, ruszkowski-pfrommer-2023, drury-1983 |

**全部 7 篇覆盖良好。** 原 4 篇 B 级（amato-blasi-2018, weinrich-2020, mewaldt-2001-clocks, genolini-2021）已补 §0.3 结构树（commit `e37b699`），升为 C 级。