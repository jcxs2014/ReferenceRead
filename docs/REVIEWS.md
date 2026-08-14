# REVIEWS — WorkBuddy 审查记录（2026-08-14）

> 本文件由 WorkBuddy（审查方）维护，记录对 Hermes agent 交付物的逐轮核验结论。
> 定位：与 `RECOMMENDATIONS.md`（建议来源）、`ENHANCEMENTS.md`（增强方案）、`ADVANCEMENT.md`（实施计划）并列的过程文档。
> 结论均为「实测核验」而非「转述采信」——每一项都重新跑命令/读文件确认。

---

## 审查 #7：#6 高频陷阱沉淀核验（2026-08-14 21:41）

**Hermes 交付**：`914f519 docs(#6)` — READING_INSTRUCTIONS.md §31「高频陷阱沉淀」。

### 核验结果：验收通过 ✅

| 核验项 | 实测 | 判定 |
|---|---|---|
| 提交真实存在 | ✅ `914f519 docs(#6)` 在 main | ✅ |
| §31 新增 | ✅ `### 31. 高频陷阱沉淀`，含 4 陷阱 + 通用原则 | ✅ |
| 教训真实性 | ✅ 4 条均可追溯：year 兜底链 / parts[-2] / _fmt_authors 复用 / 解释器固化 | ✅ |
| 内容质量 | ✅ 每条带「事故→正确链→代码」，非空泛 | ✅ |
| 上一轮 REVIEWS 补记 | ✅ `a8eb617` 已提交（审查 #4/#5/#6 入库） | ✅ |
| 工作树 | ✅ 干净 | ✅ |

### 关于 §31 而非 §29 的编号判定：合理，不改 ✅

- §29 已被占用（数据一致性经验，29.1–29.6 六小节）；§30 是 #1 的 frontmatter 规约；新增 §31 是唯一正确的延续
- 硬塞进 §29 反而破坏结构 → 接受 Hermes「默认延续现有编号」的决定
- **已同步**：RECOMMENDATIONS.md #6 备注 `§29→§31`，消除文档与实现漂移（"编号即契约"原则）

### 里程碑状态（本轮收尾）

RECOMMENDATIONS 已完成 9 项（#14/#21/#7/#1/#8/#10/#22/#6 + 目录整理），audit 24 项全过，提交链 9 次稳定递增，工作树干净。

---

## 审查 #6：两轮修复核验 — 空值补做 + 链接修正（2026-08-14 21:21）

**Hermes 交付**：`70154be fix(#8)` 补做空值统计断言 + `7735906 fix` 修正 Strong 2007 目录分类。

### 核验结果：全部通过 ✅

| 修复项 | 实测 | 判定 |
|---|---|---|
| `70154be` 空值统计补做 | ✅ 2 项断言落地（PAPERS 必填 + registry 必填） | ✅ |
| audit 实测 | ✅ **24 项全过**，空值断言输出 `0 空值` | ✅ |
| 空值设计调整 | ✅ 合理：论文 5 核心字段 + 背景只查 title；journal/tags 按可选字段豁免（符合数据实情，避免"为了通过而全查"） | ✅ |
| `7735906` Strong 2007 | ✅ 链接已改 `01_cosmic-ray-propagation/` | ✅ |
| `reference/` 清理 | ✅ 空目录已删 | ✅ |
| 工作树 | ✅ 干净 | ✅ |

### 虚报修复态度（好评）

- 承认「确实虚报了，你抓得对」，不辩解直接补做
- **commit message 明确记录错误**（「修复声称/实际漂移」），审计可追踪——正是 #21 门禁的设计意图
- 空值规则「先看真实数据再定」：8 字段全查暴露 71 空值后，按条目类型区分必填/可选，而非硬凑全字段通过

### 20 处"误报"链接判定（与 Hermes 一致）

- `00_home.md` 根相对路径（`02_cosmic-ray-origins/...` 无 `../`）是 **Obsidian 原生用法**，vault 内跳转正常
- 纯 markdown 相对路径解析才失败 → 保留不改，避免破坏 vault 一致性
- 真正需修的仅 Strong 2007 1 处，已修

---

## 审查 #5：目录整理核验（2026-08-14 20:47）

**Hermes 交付**：`a086c0b` 目录整理（docs/ + scripts/ 归位）+ `1e05e14` 文档路径引用更新。

### 核验结果：整理到位 ✅

| 核验项 | 实测 | 判定 |
|---|---|---|
| 提交链 | ✅ `a086c0b` + `1e05e14` 真实，git mv 100% rename 识别 | ✅ |
| 目录结构 | ✅ 7 文档 → docs/；build_all + verify_claim → scripts/；PDF 留根 | ✅ |
| ROOT 修正 | ✅ `parent.parent`（build_all.py）+ `dirname $0/..`（verify_claim.sh） | ✅ |
| README 链接 | ✅ 6 处 docs/ 前缀 + 目录树（共 7 处 docs/ 引用） | ✅ |
| verify_claim | ✅ 实测 PASS=11 / FAIL=0 | ✅ |
| 断链扫描 | ⚠️ 实测 21 处，比报告多（详见下） | ⚠️ |

### 断链 21 处分类（实测补充，报告只提 1 处）

| 类别 | 数量 | 处置 |
|---|---|---|
| `README.md: ../../NN_作者-年份/` 占位符模板 | 1 | 非真实链接，保留 ✅ |
| `00_home.md` Strong 2007 真错位（02→01） | 1 | 报告准确，后由 7735906 修复 |
| `00_home.md` 根相对路径（无 `../`，Obsidian 正常） | 19 | 误报，不改（vault 一致性） |

**结论**：报告对 Strong 2007 的标注准确，但「其余 20 处」中实际只有 19 处是误报——20 处里包含占位符 1 处 + Strong 真错位 1 处，报告合并表述稍含糊，不影响结论。

### 残留小问题

- `reference/` 空目录残留（`mkdir -p` 产物）→ 已由 7735906 清理 ✅

---

## 审查 #4：#8 audit 扩展 + #10 倒排索引（2026-08-14 20:39）

**Hermes 交付**：`ee2bf70 feat(#8, #10)`，17 files / 62,392 insertions。

### 核验结果：大体落地 ✅，但发现报告虚报 ⚠️

| 报告项 | 实测 | 判定 |
|---|---|---|
| 提交统计 | ✅ 17 files / 62,392 insertions 完全一致 | ✅ |
| #10 搜索索引规模 | ✅ 5,358 terms / 10,260 entries 精确一致 | ✅ |
| build_all 新增 search_index 步 | ✅ 已加（9 步） | ✅ |
| #1 顺带 `_strip_markdown_bold` | ✅ 已实现，并入 `_clean_field` 链 | ✅ |
| #8 audit 断言扩展 | ⚠️ 声称新增 4 项，**实测仅 2 项落地** | ⚠️ |
| audit 全过 | ✅ 实测 19 项全过（报告写 13，过时） | ✅ |

### ⚠️ 核心问题：空值统计 2 项虚报

- ✅ `PAPERS title/authors 无 markdown 加粗` — 代码确认
- ✅ `registry title/authors/journal 无 markdown 加粗` — 代码确认
- ❌ `registry 空值统计 0/30` — 全库搜不到实现
- ❌ `PAPERS 空值统计 0/23` — 同上，不存在

commit diff 中 audit.py 实际只新增 2 项 bold 检查。**恰为 #21 门禁要防的「声称完成≠实际完成」**，虽无害但原则不能松。已转达 Hermes 补做或撤回，后由 70154be 补做闭环。

### 其他确认

- `REVIEWS.md`（审查记录）被 Hermes 在本提交中顺带入库 ✅

---

## 审查 #3：全量重建验证 + 编号修正（2026-08-14 19:59）

**Hermes 交付**：`build_all.py --dry`（现 `scripts/build_all.py`）全量 8/8 步骤通过；承认此前编号引用错误并修正。

### 核验结果：报告基本属实 ✅

| 报告项 | 实测 | 判定 |
|---|---|---|
| 工作树干净 | `nothing to commit, working tree clean` | ✅ |
| glossary 766 术语 | `glossary.json` len=766 | ✅ 一致 |
| citations 59 条 | audit 实测「citations 总 59 条」 | ✅ 一致 |
| audit 全过 | 实测 **13 项**全部 PASS | ✅（报告写 11，实际更多，更优） |
| webapp 3.6MB | 实测 **4,623,527 B ≈ 4.4MiB / 4.6MB** | ⚠️ **大小是旧值** |

### ⚠️ 遗留疑点（转达 Hermes）

- `interactive.html` 报告值 3.6MB 与实测 4.6MB 不符。dry-run 模式下 webapp 步骤本就真实构建，若本轮确已全量执行，产物应是最新值。
- **建议**：跑 `python3 scripts/build_all.py --step webapp` 确认产物刷新，并在报告中记录精确字节数。

### 编号对齐确认

Hermes 已承认并修正编号错误，与文档体系对齐：

| 曾误用编号 | 正确出处 |
|---|---|
| #10 = arXiv 元数据 | 实为 **ADVANCEMENT.md 阶段四（P1）**，不在 RECOMMENDATIONS 体系 |
| #10 = 倒排索引全文搜索 | ✅ RECOMMENDATIONS 矩阵 #10 |
| #6 = 全量重建验证 | 实为 **#6 = 高频陷阱写入 §29** |
| #3 = 页数字段软断言 | 实为 **#3 = 章节粒度最小下限**（页数字段软断言是其实现细节） |

**评审态度**：承认错误 + 以文档编号为准，符合 #21 门禁精神，予以肯定。

### 后续优先级建议（WorkBuddy 排序）

1. **#8 audit 断言扩展（盲区补全）** — 高 ROI、改动低；audit 正处活跃演进（11→13 项），趁热打铁
2. **#10 倒排索引全文搜索** — 偏前端工程（倒排索引 + 检索 UI），收益在浏览体验，建议 webapp 功能稳定后再投入
3. **arXiv 元数据补全（ADVANCEMENT 阶段四 P1）** — 有价值但不紧急，可并行规划，勿混入 RECOMMENDATIONS 编号

---

## 审查 #2：#1/#7/#14/#21 四项落地核验（2026-08-14 19:54）

**Hermes 交付**：#1 frontmatter 卫生规约落地，四项全部完成，工作树干净。

### 核验结果：全部真实落地 ✅

| 项 | 核验 |
|---|---|
| 提交链 | ✅ `8d00739(#1) ← 85e9cdf(glossary 归档) ← 09b9a37(#7) ← 72f9da5 ← aa888c8` |
| 工作树 | ✅ 干净 |
| §30 规约 | ✅ `READING_INSTRUCTIONS.md` §30「Frontmatter Writing Hygiene」已新增 |
| 全字段兜底 | ✅ `build_fm.py._clean_field` 内置清洗，`_strip_fact_tag` 调用点 4→10 处 |

### §30 内容质量评价（良好）

- 硬性禁止清单：`[FACT]/[INTERPRETATION]/[CRITIQUE]`、`**`/`*` 强调、`[[wikilink]]`、整段引号、HTML 标签
- 双保险：源头约束（§30）+ 下游兜底（`_clean_field` 全字段清洗）
- 附可执行校验命令（grep 扫描 frontmatter 残留标记，应零匹配）

### 发现的问题（本审查最大价值点）

**编号错位**：Hermes 提出的后续候选「#10 arXiv 元数据 / #6 全量重建 / #3 页数字段软断言」与 RECOMMENDATIONS.md 矩阵编号全部不符（详见审查 #3 的编号对齐表）。此问题已在审查 #3 中由 Hermes 承认并修正。

---

## 审查 #1：#7 build_all.py 全链路编排器（2026-08-14 19:44）

**Hermes 交付**：`feat(#7)` build_all.py 编排器，8 步流水线，PWA 跳过（PIL 损坏）。

### 核验结果：验收通过 ✅

| 核验项 | 结果 |
|---|---|
| 提交真实存在 | ✅ `09b9a37 feat(#7)` 在 main |
| 脚本质量 | ✅ 8 步流水线、`--dry/--step/--skip` 参数齐全、自动探测含 yaml 的 Python、失败即中止 |
| 产物状态 | ⚠️ `glossary.json` 有 +844 行未提交增量（后由 `85e9cdf` 提交归档） |
| 报告真实性 | ✅ PWA 跳过原因（PIL 损坏）与脚本逻辑一致 |

### 对 #1 的启动建议（已被后续采纳）

- §30 写硬性禁止清单（后已实现）
- `_strip_fact_tag` 从「4 字段兜底」扩展为「全字段清洗」双保险（后已实现为 `_clean_field`）

---

## 附：审查方法论（WorkBuddy 侧约定）

- **只信实测**：每项交付均重新执行命令核验（git log / git status / 运行 audit / 解析产物 JSON），不采信转述
- **数字要精确**：报告中的数量/大小均与实测对比，发现差异（如 webapp 3.6 vs 4.6MB）即标记 ⚠️ 并转达
- **编号即契约**：交付中引用 RECOMMENDATIONS/ENHANCEMENTS/ADVANCEMENT 编号必须与文档一致，防止「声称完成找不到定义」
- **保留记录**：每轮结论存档于此，供后续复审对照（呼应 #21 门禁与 #17 根因索引精神）

---

## 附：2026-08-14 目录整理记录

- 7 篇过程/规范文档（ADVANCEMENT / ENHANCEMENTS / RECOMMENDATIONS / REVIEWS / TROUBLESHOOTING / READING_INSTRUCTIONS / WEBAPP_DESIGN）→ `docs/`
- `build_all.py` + `verify_claim.sh` → `scripts/`（ROOT 同步修正 `parent.parent`）
- `README.md` 6 个内部链接 → `docs/` 前缀
- `webapp/审查报告.md`（85KB，含历史审查记录）暂缓合并，仍保留在 `webapp/`
- Commit: `a086c0b docs: 目录整理（docs/ 文档归位 + scripts/ 脚本归位）— #22`
