# ENHANCEMENTS — 文献工作区增强建议清单

> 生成日期：2026-08-13
> 背景：基于对 `papers/` 全库（21 篇、205+ 分析文件、43 commits）的整体扫描后提出的改进建议。
> 原则：**不破坏已固化的精读流水线**（`00_overview → 分章 → 98_vocabulary → 99_final_summary`），只补「库级能力」：连接、检索、可维护性。
> 状态图例：⬜ 待办 ｜ ✅ 已完成
> **执行主体**：本地 Hermes agent（本清单由 WorkBuddy 审查时生成，供执行侧参考；WorkBuddy 不承担执行）。
> **扩展约定（2026-08-13 用户确认）**：后续会持续新增文献，本清单所有建议以「保持文档系统可扩展性」为最高优先级。

---

## 扩展性设计 — 现状评估与接入 SOP

### A. 现有设计中天然支持扩展的部分（保持不变）

- **主题域 → 单篇论文 → literature_analysis/ 三层结构**：新增论文只需在对应主题域下新建一个独立目录，与其他论文零耦合。
- **编号系统 `NNNN_作者-年份`**：主题域内递增编号（0001, 0002, …），作者-年份后缀保证唯一；新增主题域直接开新目录（如 `04_xxx`）。
- **规则驱动**：`READING_INSTRUCTIONS.md` 的 28 节规范就是"精读操作手册"，新论文照章执行即可，无需新设计。
- **每篇独立产出流水线**：`00_overview → 分章 → 98_vocabulary → 99_final_summary`，新增一篇不影响已有 21 篇。

### B. 扩展时的摩擦点（对应下方 P0/P1/P2 建议）

1. `INDEX.md` 手工维护，新增论文必须手动改表格（→ 建议 #8 脚本生成）
2. `README.md` 未描述接入流程，新会话不知道"怎么加一篇"（→ 建议 #1）
3. 无篇间导航，新论文难以挂接进既有知识网络（→ 建议 #3）
4. 词汇表各自独立，新论文术语无法复用/对齐全库（→ 建议 #9）
5. 未提交变更会随 FreeFileSync 同步扩散（→ 建议 #2）

### C. 新增文献接入 SOP（标准流程）

```
① 建目录   XX_主题域/ 下新建 NNNN_作者-年份/（编号为主题域内下一个序号）
② 放原文   论文 PDF 入目录；命名沿用现有风格（作者-简短标题+编号.pdf）
③ 提取文本 用 fitz 脚本提取 → fulltext.txt / extracted/*.json（被 .gitignore 忽略，
            依赖 FreeFileSync 跨设备同步；扫描版 PDF 用 pdftoppm 转 PNG 视觉转录）
④ 精读     按 READING_INSTRUCTIONS.md 28 节执行
            → literature_analysis/：00_overview → 分章 → 98_vocabulary → 99_final_summary
            （若 #5 落地，追加 97_quality_check.md 自查）
⑤ 挂接     在 00_overview.md 标注「前序阅读/关联论文」（若 #3 落地）；
            判断是否汇入 background/ 对应主题文档
⑥ 更新索引 更新 INDEX.md（当前手工 → 未来 #8 脚本生成）；若开新主题域，同步更新 README
⑦ 提交同步 git commit + FreeFileSync 双向同步
```

### D. 开新主题域时的注意点

- 在 `papers/` 下新建 `NN_新主题名/`，主题域编号顺延（现有 01/02/03）。
- 同步更新：`INDEX.md` 增加新分类小节、`README.md` 目录结构、`background/README.md` 交叉关系图（如新主题与既有主题相关）。

---

## P0 — 结构层（低成本、立即见效）

### 1. ⬜ README 升级为工作区总览
- **问题**：`README.md` 只有命名规范 + frontmatter 模板，未描述项目实际产出体系（`literature_analysis/` 分章、`background/` 知识库、`READING_INSTRUCTIONS.md` 的作用），新会话/新设备无法 30 秒看懂全貌。
- **做法**：补充「目录结构图 + 产出流水线说明 + 各顶层文件职责 + 阅读顺序建议」。
- **涉及文件**：`README.md`

### 2. ⬜ 提交遗留 git 变更
- **问题**：工作区有未提交变更（8 个 `98_vocabulary.md` 从论文根目录移入 `literature_analysis/` 的删除记录 + `.sync.ffs_db` 修改）。
- **做法**：`git add -A && git commit`（建议 `.sync.ffs_db` 仍保持 ignore，仅提交词汇表移动）。
- **涉及文件**：仓库根 git 状态

### 3. ⬜ 篇间阅读导航
- **问题**：`00_overview.md` 只有文件内导航（上一章/下一章），无篇间导航；21 篇之间存在明确的传承/对照关系。
- **做法**：每篇 overview 增加「前序阅读 / 关联论文」字段。已知关系：
  - Blasi (2013) ↔ Amato (2014)：同主题双综述
  - B²FH (1957) → Wallerstein (1997)：核合成传承线
  - Anders & Grevesse (1989) → Grevesse & Sauval (1998) → Lodders (2003) → Asplund (2009)：太阳丰度标准演进线
  - 丰度标准 → 恒星演化/核合成模型（AGSS09 金属丰度下调 30%）
- **涉及文件**：各篇 `literature_analysis/00_overview.md`

---

## P1 — 内容层（提升精读档案的复用价值）

### 4. ⬜ 关键数值速查表标准化
- **问题**：`99_final_summary.md` §15.4「最重要结果」表格格式各篇不统一。
- **做法**：固定为「物理量 / 数值 / 不确定度 / 来源章节」四列模板；`background/README.md` 建「全库关键数值索引」（目前只有公式索引，缺数值索引）。
- **涉及文件**：各篇 `99_final_summary.md`、`background/README.md`

### 5. ⬜ 完成度自查清单落地
- **问题**：`READING_INSTRUCTIONS.md` §25 要求 Completeness Check，但每篇无自查文件，「精读完成度」不可核查。
- **做法**：新增 `97_quality_check.md`（覆盖章节数、图表数、公式数、[CRITIQUE] 条数），INDEX.md 展示完成度。
- **涉及文件**：各篇 `literature_analysis/`（新文件）、`INDEX.md`

### 6. ⬜ CRITIQUE 观点汇总
- **问题**：[CRITIQUE] 观点分散在各分章，二次审读时难聚焦。
- **做法**：每篇在总结前附「批判观点清单」；跨篇可汇总「领域争议点索引」（如扩散谱指数 0.3 vs 0.54、晕高度 4–6 kpc）。
- **涉及文件**：各篇 `99_final_summary.md` 或新增小节

---

## P2 — 工具与体验层

### 7. ⬜ background 知识库交互式网页
- **做法**：把 `background/` 三篇文档做成单文件交互网页（全文搜索、公式渲染、主题切换、术语表查询、21 篇论文交叉跳转），复用 `agent-harness` 已验证的单文件架构（i18n + 浅/深主题 + 全文搜索）。
- **涉及文件**：新建（如 `background/background-interactive.html`）

### 8. ⬜ 脚本自动生成 INDEX.md
- **做法**：写脚本从目录结构 + frontmatter 自动生成 `INDEX.md`（含篇数、分析文件数、链接、统计），新增论文时零手工维护。
- **涉及文件**：新建脚本 + `INDEX.md`

### 9. ⬜ 全库术语一致性检查
- **做法**：21 篇 `98_vocabulary.md` 各自独立，同一术语可能存在译法分歧；做一次跨篇查重并汇总为全库术语表。
- **涉及文件**：各篇 `98_vocabulary.md`、新建全库术语表

---

## 实施顺序建议（扩展性优先，已重排）

1. P0-2（提交遗留变更，纯卫生，5 分钟）
2. **P2-8（脚本自动生成 INDEX.md —— 扩展刚需，新增论文后索引零手工维护）**
3. P0-1（README 总览，含「新增文献接入 SOP」，作为扩展操作手册）
4. P0-3（篇间导航，需人工标注一次，建立知识网络挂接点）
5. P1-4/5/6（内容档案增强，可随新论文精读逐步补）
6. P2-7（交互网页，工作量最大，单独排期）
7. P2-9（术语查重，建议在新论文接入时同步维护）
