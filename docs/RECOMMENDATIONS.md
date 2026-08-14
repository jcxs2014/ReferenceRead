# 改进建议路线图（2026-08-14）

> **来源**：本会话三轮审查（见 `webapp/审查报告.md` 附 25–27）沉淀的 22 条可执行建议
> **范围**：文献阅读工作流 + 网页构建工作流 + 性能与可维护性 + 项目战略
> **状态**：⬜ 待实施（按价值 / 改动量矩阵取舍）
> **标记**：`[价值: 高 / 中 / 低]` `[改动: 极低 / 低 / 中 / 高]`
> **关联约定**：所有 "附 N" 均指 `webapp/审查报告.md` 附录；"A1 / B2" 等指 `TROUBLESHOOTING.md` 条目
>
> **与 `ENHANCEMENTS.md` 的关系**：`ENHANCEMENTS.md` 是历史快照（9 条全部 ✅ 完成，2026-08-14 归档），本文件是其**后续续集**——记录本会话新发现的 22 条改进建议。两者长期并存：本文件定位为"现行建议"，`ENHANCEMENTS.md` 定位为"已完成建议"，避免清单冲突。

---

## 总览矩阵

| # | 标题 | 类别 | 价值 | 改动 |
|---|---|---|---|---|
| 1 | 子智能体 frontmatter 卫生规约 | 文献工作流 | 高 | 低 |
| 2 | `READING_INSTRUCTIONS` 机器可读自检 | 文献工作流 | 高 | 中 |
| 3 | 章节粒度最小下限（按论文类型） | 文献工作流 | 中 | 低 |
| 4 | 术语跨篇一致性自动检查 | 文献工作流 | 高 | 中 |
| 5 | `build_citations` 差异对账 | 文献工作流 | 中 | 低 |
| 6 | 高频陷阱写入 §29（实落 §31） | 文献工作流 | 高 | 低 |
| 7 | `build_all.py` 顶层编排器 | 网页构建 | 高 | 低 |
| 8 | audit 断言扩展（盲区补全） | 网页构建 | 高 | 低 |
| 9 | 增量重建缓存 | 网页构建 / 性能 | 高 | 中高 |
| 10 | 倒排索引全文搜索 | 网页构建 / 性能 | 高 | 中 |
| 11 | KaTeX 自托管离线模式 | 网页构建 | 中 | 低 |
| 12 | 基础无障碍审计 | 网页构建 | 中 | 低 |
| 13 | `server.py` 加重建锁 | 网页构建 | 低 | 极低 |
| 14 | 零测试补齐 | 可维护性 | 极高 | 中 |
| 15 | 性能基线与回归检测 | 可维护性 | 中 | 低 |
| 16 | 仓库卫生巡检脚本 | 可维护性 | 中 | 低 |
| 17 | `TROUBLESHOOTING.md` 加根因索引 | 可维护性 | 高 | 极低 |
| 18 | Obsidian 镜像一致性检查 | 可维护性 | 低 | 低 |
| 19 | 语料增长路线图 | 项目战略 | 高 | 极低 |
| 20 | background/ 争议演化扩列 | 项目战略 | 中 | 中 |
| 21 | 「声称完成」自动化门禁 | 项目战略 | 高 | 中 |
| 22 | 过程文档合并 | 项目战略 | 低 | 低 |

---

## 一、文献阅读工作流（`READING_INSTRUCTIONS.md` / 子智能体提取）

### 1. 子智能体 frontmatter 卫生规约 [价值高 / 改动低]

**现状**：本会话三轮反复出现同一类 bug——子智能体把正文的 `[FACT] / [INTERPRETATION] / [CRITIQUE]` 标记混入 frontmatter 元数据（TROUBLESHOOTING A1、附 25）。`build_fm.py._strip_fact_tag` 是事后兜底，覆盖不全（漏 tags，见附 25 / 27）。

**建议**：
- 在 `READING_INSTRUCTIONS.md` 增 §30「**Frontmatter Writing Hygiene**」硬性规则——"frontmatter 任何字段值不得包含 `[FACT]` 等标记 / 任何 `**` 加粗 / 单引号包裹的整段说明"，违规即拒写
- 子智能体源头约束；下游清洗作为冗余防御

**关联**：附 25、TROUBLESHOOTING A1

### 2. `READING_INSTRUCTIONS` 机器可读自检 [价值高 / 改动中]

**现状**：`READING_INSTRUCTIONS.md` 是 29 节纯文本；每篇 `97_quality_check.md` 是手工产物，**全库 23 篇无统一"29 节覆盖率"仪表盘**。

**建议**：
- 写 `scripts/quality_matrix.py`——扫描 23 篇分章文件 vs 29 节 checklist，输出覆盖率矩阵
- 展示于 INDEX 或新增的 `background/07_quality_dashboard.md`
- 让"精读深度"可度量、可比对

### 3. 章节粒度最小下限（按论文类型）[价值中 / 改动低]

**现状**：23 篇精读文件数从 5（proceedings 短文）到 14+（大综述）不等；90 页大综述与 9 页短讲稿用同一精读模板不现实——前者章节粒度明显不足。

**实施缺口（审查发现）**：soft 断言需要页数来源——当前 frontmatter 没有 `pages` 字段，PDF 页数需解析；不能直接"章节数 ≥ floor(页数/10)"。

**建议**：
- **第一步**：在 23 篇 frontmatter 加 `pages: <整数>` 字段（人工或半自动：从 PDF 元数据 `fitz.open(...).page_count` 提取）
- **第二步**：在 `READING_INSTRUCTIONS.md` §2 / §3 按"页数 × 论文类型"规定最低章节数：
  - 综述：≥10 章
  - 长文（30–80 页）：≥8 章
  - 短文（5–15 页）：≥5 章
- **第三步**：`webapp/audit.py` 加软断言："章节数 ≥ floor(页数 / 10)"，对无 pages 字段的篇目仅 warning 不 fail

### 4. 术语跨篇一致性自动检查 [价值高 / 改动中]

**现状**：`background/05_glossary.md` 已聚合 795 行术语（附 27 报告）；但**同术语不同译法未自动发现**——人工查重工作量大（ENHANCEMENTS #9 已完成聚合，缺一致性检查）。

**建议**：
- 写 `scripts/term_consistency_check.py`——对 23 篇 `98_vocabulary.md` 的 B 部分做术语聚类
- 对每个聚类展示所有译法 + 出处 + 上下文
- 输出 `background/08_term_consistency.md`
- 让"同物异名"显式化

### 5. `build_citations` 差异对账 [价值中 / 改动低]

**现状**：citations 是 frontmatter 的关键字段（驱动图谱、Obsidian wikilink），但 frontmatter citations ↔ 各篇 `04_references.md` ↔ 正文引用**没有对账**。错位会被 audit 漏过。

**建议**：
- 写 `scripts/citations_diff.py`——对每篇，比对 frontmatter citations vs `04_references.md` vs 正文 `(\d{4})` 引用模式
- 输出不一致清单到 `background/09_citations_diff.md`

### 6. 高频陷阱写入 §29 → 实落 §31 [价值高 / 改动低] ✅ 已完成（2026-08-14，`914f519`）

**现状**：本会话已确认 3 类反复出现的子智能体 bug——正文 `**` 加粗吞并、引号泄漏、勘误文本溢出元数据。

**建议**：
- 把这 3 条加入 `READING_INSTRUCTIONS.md` §29「数据一致性经验」作为"高频陷阱"
- 配 `build_fm.py` 防御映射（哪条对应哪个清洗函数）
- 让后续写新篇时**先看这 3 条**，避免重新踩坑

---

## 二、网页构建工作流（`webapp/` 11+ 脚本）

### 7. `build_all.py` 顶层编排器 [价值高 / 改动低]

**现状**：README 列了 7+ 脚本链式调用，人工 bash 拼接；本会话附 25 / 26 根因之一即"build_webapp 用了过期 interactive.html"——执行侧跳过了其中一步。

**建议**：
- 写 `scripts/build_all.py`——按依赖顺序调用：`build_citations → build_fm → build_registry → build_glossary → build_webapp → audit`
- 每步失败立即终止并打印"哪一步 / 哪行错"
- 一次调用、失败可定位——杜绝"跳步导致过期产物"

### 8. audit 断言扩展（盲区补全）[价值高 / 改动低]

**现状**：audit 已从 18 → 20 条（附 26 / 27），覆盖了 `[FACT]` / `****` / 引号 / 勘误词，但仍缺：
- 分章文件存在性 vs 00_overview 章节清单一致性
- 章节顺序连续性（无跳号）
- `[[wikilink]]` 解析可达性（Obsidian 图谱实际连通数）
- 内 / 外部链接可达性（HTTP 200 + vault 内可达）
- 大小 / 体积异常（webapp > 10MB 警告、frontmatter 字段值 > 2KB）

**建议**：分批加 5 条左右，覆盖"结构完整性"维度。

### 9. 增量重建缓存 [价值高 / 改动中高]

**现状**：`build_webapp.py --include-papers` 每次都全量重建 4.6MB interactive.html（23 篇约数秒）；随语料增长线性增长 O(n)。

**复杂度（审查修正）**：原方案"只重建 hash 变化篇"低估了依赖关系——
- `build_registry.py` 是全 frontmatter 扫描（虽然只变化篇的 entry 会变，但 build 本身 O(n)）
- citations 是跨篇 stem 引用；audit 检查悬空引用需全集
- 跨篇的 TOC / 图谱 / 章节编号也要重算

**建议（分两层实现，registry 层接受全量重建）**：
- **Layer A（先做，复杂度低）**：维护 `.webapp_cache/html_fragments/`（gitignored）——按 (paper_stem, source_md_hash) 存预生成 HTML fragment；`build_webapp` 只对 hash 变化篇重生成 fragment，最后注入 shell。**对日常"改 frontmatter 一篇"的修复循环价值最大**（附 25 / 26 / 27 那种）
- **Layer B（暂缓，价值/复杂度比下降）**：registry 增量构建需要把 build_registry 改为"读 frontmatter → 按 stem diff 局部更新 JSON"，复杂度高且 citations 校验仍需全集。**接受 registry 全量重建**（当前耗时 < 1 秒）

预期收益：日常单篇 frontmatter 修复的 build 耗时从 ~5 秒降到 < 1 秒（Layer A），registry 保持全量无回归。

### 10. 倒排索引全文搜索 [价值高 / 改动中]

**现状**：`shell.html` 搜索用 `text.includes()` 全文扫描，23 篇 / 4.6MB 单文件下勉强可用；50+ 篇后明显变慢。

**建议**：
- 构建期生成 `const IDX = {term: [{doc, offset, length}, ...]}`（倒排索引）
- 浏览器端二分查找；支持高亮多个命中、按相关度排序
- O(n) → O(log n + m) 的飞跃

### 11. KaTeX 自托管离线模式 [价值中 / 改动低]

**现状**：KaTeX 经 CDN 加载；README 提"离线降级为等宽字体显示原始 LaTeX"——**有网才正常**。

**建议**：
- `build_pwa.py` 增加 `--offline` 模式
- 把 KaTeX CSS + JS 内联进 interactive.html（增加约 300KB），换来真离线可用
- 与 PWA 哲学一致

### 12. 基础无障碍审计 [价值中 / 改动低]

**现状**：未做 a11y 审查（ARIA、键盘导航、对比度）。

**建议**：
- 快速可加项——TOC 加 `role="tree"` + `aria-expanded`、正文加"跳到内容"链接、`:focus-visible` 样式、表格 `caption` 与 `scope`
- `webapp/a11y_check.py` 跑 axe-core CLI

### 13. `server.py` 加重建锁 [价值低 / 改动极低]

**现状**：`/api/rebuild` 无并发保护；同时两次调用会撞车。

**建议**：加 `threading.Lock` 或文件锁 + 状态字段（`building / ready / error`），前端按钮显示状态。

---

## 三、性能与可维护性（横切）

### 14. 零测试补齐 [价值极高 / 改动中]

**现状**：整个项目**没有 `tests/` 目录**，audit 是结构检查不是单元测试。本会话三轮的 bug（gen_index 正则、build_fm 多行拼接、引号泄漏）都是同一类 bug 的反复出现——没有测试网拦截。

**建议**：新建 `tests/`，从高价值处入手：
- `test_extract_meta.py`：bullet / table / quoted / missing-fields 四 case
- `test_strip_fact_tag.py`：tags 字段也被覆盖（附 25 已暴露漏洞）
- `test_extract_from_bullets.py`：multiline 遇 `**` / 空行 / 标题即停（附 27 修复）
- `test_build_citations.py`：路径分片类（附 1 修过的同类）
- `test_audit.py`：每条断言给一正一反例
- 配合 `pytest`（或 stdlib 替代），接入 `build_all.py` 的门禁

**关联**：附 25 / 26 / 27 反复出现的"同一类 bug 多副本"现象的根本防御

### 15. 性能基线与回归检测 [价值中 / 改动低]

**建议**：
- 写 `scripts/build_bench.py`——跑完整 build 链，记录耗时、registry 大小、interactive.html 大小、TOC 总条数、citations 总边数
- append 到 `metrics.csv`（gitignored）
- 每次审计输出"与上次对比 ±X%"——捕捉性能 / 体积回归

### 16. 仓库卫生巡检脚本 [价值中 / 改动低]

**现状**：附 25 / 26 / 27 两次踩 "tracked-but-ignored" 坑（pycache、.gitignore 漏写）。

**建议**：写 `scripts/repo_hygiene.py`：
- 检测 tracked 文件在 .gitignore 中（建议 `git rm --cached`）
- 检测 gitignore 模式覆盖范围（如 `fulltext.txt` vs `full_text.txt` 大小写陷阱）
- 检测大文件 / PDF 是否被 .gitignore 忽略但又被 `-f` 提交
- 输出报告，建议每月跑一次

### 17. `TROUBLESHOOTING.md` 加根因索引 [价值高 / 改动极低]

**现状**：TROUBLESHOOTING 是按时间序 A / B / C…排列（18+ 条），但**根因高度重复**：
- regex 锚定 bug 出现 ≥3 次（附 1、附 25、附 26）
- frontmatter 解析 bug 出现 ≥3 次（A1、附 25、附 26）

**建议**：
- 在文件开头加一段"**Top 5 recurring root causes**"
- 每条链向具体条目
- 让新读者**按根因查**而不是按时间查

### 18. Obsidian 镜像一致性检查 [价值低 / 改动低]

**现状**：D5 规定 `ObsFile/ReferenceRead` 是只读镜像，靠 FreeFileSync 同步；**无机器验证同步是否真的成功**。

**建议**：写 `scripts/check_obsidian_mirror.py`——对比 `HermesLocal/papers` 与 `ObsFile/ReferenceRead` 的 mtime / hash，输出 drift 报告（缺失、新增、修改）。

---

## 四、项目层 / 战略建议

### 19. 语料增长路线图 [价值高 / 改动极低]

**现状**：23 篇以"经典 / 综述"为主（1957–2018），无明确的"下一批加什么"标准。

**建议**：新建 `CORPUS_ROADMAP.md`——记录 5–10 篇候选 + 选择标准：
- **主题域平衡**：03 已 15 篇，01 仅 1 篇，**优先补 01 领域**
- **时间跨度**：加 2020+ 近期成果（LHAASO 2021、Auger 2020、IceCube Gen2 等）
- **体裁平衡**：proceedings / letter / review 比例

这正是 ENHANCEMENTS 顶层"扩展性优先"原则的具象化。

### 20. background/ 争议演化扩列 [价值中 / 改动中]

**现状**：`background/06_controversy_evolution.md` 已有 **7 个详细争议**（§1–§7：太阳金属丰度 / UHECR top-down vs bottom-up / CR 传播参数 δ 与 z_h / SNR 范式 / r-s 过程位点 / 太阳中微子 / WIMP 暗物质）+ §8 速览表（7 项未展开）+ §9 时间线总结——比我最初印象中"只有 1 个"丰富得多。我提议的"太阳丰度"已是争议 1、"暗物质 WIMP"已是争议 7。

**建议**：聚焦**真正缺失**的 1 条独立争议时间线：
- **SN Ia 起源** 单简并 vs 双简并（数十年争议，2010s 后未彻底解决）

可选深化（优先级低）：§8 速览表 7 项里挑 1–2 项（如"再加速重要性"或"正电子超出"）升格为 §10 完整争议时间线。

每个争议给"时间线 + 各文献立场 + 当前共识"。

### 21. 「声称完成」自动化门禁 [价值高 / 改动中]

**现状**：本会话三轮反复证明"Hermes 报告完成 ≠ 实际完成"——patch no_change 误报、execute_code 沙箱、stale build 产物。**唯一防御就是 review 循环**。

**建议**：写 `scripts/verify_claim.sh`：
- 跑 `webapp/audit.py`
- 跑 `scripts/gen_index.py --check`
- 跑 `webapp/build_webapp` + 解码 PAPERS 数量对比 registry
- exit 0 才允许 commit message 含 "✅" 标记

不强制 commit hook（避免摩擦），但让"声称完成"有客观锚点。

**关联**：附 25 / 26 / 27 三轮的根因——本会话最大教训

### 22. 过程文档合并 [价值低 / 改动低]

**现状**：`TROUBLESHOOTING.md` 在根、`webapp/审查报告.md` 在 webapp/——都是"事后复盘"性质，归属不清。

**建议**：考虑移到一个统一 `process/` 子目录（或保留现状但加交叉索引），让"内容（background/）" vs "过程（TROUBLESHOOTING + 审查报告）"分层更清晰。

---

## 高 ROI 组合推荐

若只能先做 4 项，按 ROI 排序：

| 序 | 项 | 价值 | 改动 | 对应根因 |
|---|---|---|---|---|
| 1 | **#14 零测试补齐** | 极高 | 中 | 三轮反复出现的"同一类 bug 多副本" |
| 2 | **#21 「声称完成」自动化门禁** | 高 | 中 | 报告与实测不符 / patch no_change 误报 |
| 3 | **#7 `build_all.py` 顶层编排器** | 高 | 低 | "build_webapp 用了过期 interactive.html" |
| 4 | **#1 子智能体 frontmatter 卫生规约** | 高 | 低 | `[FACT]` 标记混入元数据 |

完成后，下一轮审查会轻松很多。

---

> **最后更新**：2026-08-14（基于本会话三轮审查沉淀）
> **下次复审建议**：实施 4–6 项后，跑一轮完整 build + audit + headless，确认无回归再勾选对应项。
