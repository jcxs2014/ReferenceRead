# 文献管理进阶实施方案（v1）

> 起草：WorkBuddy（审查/咨询角色），2026-08-13
> 执行主体：本地 Hermes agent（用户确认后实施）
> 前置：`papers/` 文档库（21 篇精读 + background 知识库 + webapp 4.06MB 单文件）已收尾稳定
> 原则：数据层地基 → 交互层体验 → 工作流层防腐化 → 认知层复利；每阶段跑「附 4 断言 + headless 运行时验证 + 双端截图」

---

## 阶段一（P0，地基）：结构化元数据 registry

**目标**：生成 `papers/registry.json`——21 篇文献的机器可读元数据，作为后续所有自动化（webapp 数据源、审计、图谱、检索）的单一事实源。

**数据模型**（每篇一个对象）：

```json
{
  "stem": "0001_strong-moskalenko-ptuskin-2007",
  "title": "Cosmic-ray propagation and interactions in the Galaxy",
  "authors": ["A. W. Strong", "I. V. Moskalenko", "V. S. Ptuskin"],
  "year": 2007,
  "category": "01_cosmic-ray-propagation",
  "category_label": "宇宙线传播",
  "journal": "Rev. Mod. Phys. 79 (2007) 2451",
  "doi": "10.1103/RevModPhys.79.2451",
  "arxiv": "astro-ph/0701517",
  "read_date": "2026-08-12",
  "status": "completed",
  "quality": {"overview": true, "chapters": 6, "vocabulary": true, "summary": true},
  "key_values": [
    {"quantity": "D_xx @3 GV", "value": "(3-5)e28 cm2/s", "section": "§3.2"}
  ],
  "citations": ["0002_trimble-1975"],
  "tags": ["cosmic-ray", "propagation", "GALPROP"]
}
```

**生成方式**：
1. 脚本 `webapp/build_registry.py`：解析 `INDEX.md`（复用 `build_webapp.py::_build_citation_map` 的块解析思路，已有中文表头经验）+ 各篇 `00_overview.md` 的 frontmatter/表格（作者/期刊/DOI/arXiv/read_date 均有）
2. `quality.chapters` 从 `literature_analysis/` 文件数统计
3. 人工校验一遍（21 篇，重点核对 authors/doi/arxiv）
4. `citations` 首版可留空数组，后续人工/半自动填充

**验收**：21 篇全量；`python3 -m json.tool` 校验通过；authors/year/doi 与 INDEX 对照 0 差错；`key_values` 覆盖 ≥60% 篇目（数据从 `00_key_values.md` 回流）。

**工作量**：0.5–1 单元。

---

## 阶段二（P0，体验最实用）：阅读追踪 + 复习提醒

**目标**：webapp 内每篇可标记阅读进度、记录最后阅读时间、到期提醒复习。

**实现**（shell.html + md2doc_html.py 微调）：
1. **checkbox 可交互**：md2doc 已把 `- [x]` 转成 `<input type="checkbox" disabled>`——去掉 `disabled`，点击时写 `localStorage["kb_progress_" + slug] = JSON 数组`（按章节标题索引）；渲染时回填勾选态。
2. **最后阅读时间**：`switchDoc()` 写 `localStorage["kb_lastread_" + slug] = Date.now()`。
3. **完成度显示**：
   - dropdown item 右侧加进度点（`✓` 数/总章节数 或 百分比，≤3 字符）
   - 首页（`00_home.md`）加「未完成 0 篇 / 建议复习 X 篇」区块——由 JS 动态注入（首页 section 内的 `#kb-stats` 占位 div）
4. **复习提醒**：已完成且 `now - lastread > 30 天` 的篇目，首页顶部列出「建议复习：B²FH 1957（45 天未读）」，点击跳转该篇。

**验收**：勾选后刷新保持；切换文档更新 lastread；首页统计正确；复习阈值 30 天可配置。

**工作量**：0.5–1 单元。

---

## 阶段三（P0，防扩展腐化）：构建期知识审计断言

**目标**：`build_webapp.py` 在既有断言（附 4：id 唯一/label 合法/stats 一致）基础上，增加**知识完整性**断言，失败非零退出。

**新增断言**：
- a) 每篇论文 `literature_analysis/` 含 `00_overview.md`、`98_vocabulary.md`、`99_final_summary.md`
- b) 每篇 TOC 条目 ≥3
- c) 论文 label 与 `registry.json`（阶段一产出）的 authors/year 一致（无 registry 时跳过）
- d) `05_glossary.md` 术语表格行 ≥600（防术语表退化）
- e) 目录 `0[0-9]_*/NNNN_*/` 与 `INDEX.md` 条目一一对应（新增文献未更新 INDEX 即失败）

**验收**：对当前库跑通 0 失败；故意删一篇的 vocabulary 验证会失败。

**工作量**：0.5 单元。

---

## 阶段四（P1）：arXiv 元数据半自动获取

**目标**：新文献接入时，脚本自动抓元数据 + 下载 PDF，减少手填。

**实现**：`webapp/fetch_arxiv.py`（Python 标准库 urllib，无第三方依赖）：
- 输入：arXiv ID 或标题关键词
- 调 `http://export.arxiv.org/api/query`（ATOM 解析：标题/作者/摘要/DOI/PDF 链接）
- 输出：`NNNN_作者-年份/` 目录 + `frontmatter` 模板 md + 下载 PDF + 追加 registry 条目

**验收**：任选一篇真实 arXiv 论文跑通，产物符合 README 命名规范。

**工作量**：1 单元。

---

## 阶段五（P1，交互增强）：术语 hover + 引用图谱

**5.1 术语 hover**：
- `05_glossary.md`（688 行）→ 构建 `{术语: 释义}` 映射（脚本解析表格）→ 注入 webapp `GLOSS` JSON
- 正文中命中术语的文本 span 化（构建期 md2doc 处理，避免运行时重 DOM），hover 显示 tooltip（纯 CSS，`title` 属性或自绘）

**5.2 引用图谱**：
- 从 `registry.citations` 生成 21 节点引用图（SVG，复用 agent-harness 拓扑图经验）
- 首页或独立视图展示，节点可点击跳转论文

**验收**：术语 hover 在 3 篇抽样文档生效；图谱节点/连线正确。

**工作量**：1–1.5 单元。

---

## 阶段六（P2，认知层）：综述生成 + 争议点演化

- **综述/讲义**：基于 background 三篇 + registry，按主题参数化生成（人工/AI 混合审校后入 background 或独立 docs/）
- **争议点演化**：`04_critique_index.md` 结构化（争议主题 → 各文献立场 → 时间线），可并入图谱或独立页

**工作量**：2+ 单元（按需排期，不阻塞 P0/P1）。

---

## 生态（P1）：移动阅读 + 双机分工

- **PWA**：加 `manifest.json` + `<link rel="apple-touch-icon">`，Safari「添加到主屏幕」后全屏阅读（interactive.html 已响应式）
- **Mac mini**：PDF 批量解析、registry 大规模检索等重任务放常开 mini；MacBook 做精读/审查

---

## 执行顺序与依赖

```
阶段一 registry ──→ 阶段三 审计断言（依赖 registry 的 label 对照）
         │
阶段二 阅读追踪（独立，可与一并行）
阶段四 arXiv 获取（独立）
阶段五 术语/图谱（依赖 registry.citations）
阶段六 认知层（依赖 background 稳定）
```

**推荐批次**：批 1 = 阶段一 + 二（并行）；批 2 = 阶段三 + 四；批 3 = 阶段五；批 4 = 阶段六 + PWA。

## 总验收

- 每阶段：`python3 webapp/build_webapp.py --include-papers` 跑通 + 附 4 断言全绿 + headless Chrome 运行时验证（懒加载 1 section、0 console error）+ 桌面 1280 / 移动 375 截图
- 数据一致性三方对照：`registry.json` ↔ `INDEX.md` ↔ webapp 产物
- 新增文献走 `papers/ENHANCEMENTS.md` 顶部 SOP，registry/审计自动兜底

## 工作量总览

| 阶段 | 内容 | 预估 |
|---|---|---|
| 一 | registry.json + build_registry.py | 0.5–1 |
| 二 | 阅读追踪 + 复习提醒 | 0.5–1 |
| 三 | 知识审计断言 | 0.5 |
| 四 | arXiv 元数据脚本 | 1 |
| 五 | 术语 hover + 引用图谱 | 1–1.5 |
| 六 | 综述/争议演化 | 2+（按需） |

---

# V1.1 摸底修订（2026-08-13，执行侧摸底审查后）

> 摸底确认：21/21 篇 `00_overview.md` 为**表格格式、0 frontmatter**；`registry.json`/`build_registry.py` 不存在；`05_glossary.md` 为**全库一份**（background/，691 行表格，多对多结构）；`98/99` 文件 21/21 齐全。
> 下列修订覆盖原正文对应段落（保留原段作历史，执行以本节为准）。

### R1（P0）O0 重设计——工作量上调，frontmatter 必须写回

- **现状**：21 篇元数据是 `00_overview.md` 表格（Title/Authors/DOI/arXiv 等 9 字段），0 frontmatter。
- **流程定稿**：① 脚本从 21×9 表格字段提取（复用 H4 解析经验）→ ② **写回 frontmatter**（27 个入口文档，YAML 块）→ ③ 由 frontmatter 派生 `registry.json`。
- **为什么必须写回 frontmatter**（与摸底建议分歧点）：O2 图谱（`citations` 字段）与 Obsidian Dataview 查询依赖 frontmatter；不写回则 Obsidian 协同版失去一半价值。
- **双源兜底**：表格（人类视图）与 frontmatter（机器源）并存，由阶段三新增断言 `frontmatter ↔ 00_overview 表格字段一致` 保证，审计失败即构建中断。
- **工作量**：0.5–1 → **1.5–2 单元**（提取 + 写回 + 校验三方）。
- **验收补充**：写回后 27 文件 frontmatter 齐全；Dataview 可查；表格未被破坏。

### R2（P1）阶段三断言 (d) 措辞修正

- 原："`05_glossary.md` 术语表格行 ≥600" → 改为：**全库 `background/05_glossary.md` 存在且术语表格行 ≥600**（实测 691 ✓）。
- 断言 (a)：21/21 的 98/99 已齐全，可直接启用（无需补文件）。
- 断言 (c)：registry 存在时才运行；新增 frontmatter↔表格一致检查（见 R1）。

### R3（P1）阶段五术语 hover——数据源为全库多对多结构

- `05_glossary.md`（background/，691 行）表头为 `| 术语 | 出现论文 | 释义合并 |`，**多对多映射**（术语列含 `·` 分隔的多篇引用），不是 key-value 字典。
- 实现：解析三列结构 → 构建 `{术语: {释义, 出现论文[]}}` 注入 webapp `GLOSS`；hover 显示释义 + 出处论文。
- 工作量：1–1.5 不变（含多对多解析）。

### R4（P1）阶段二进度闭环——形态 A 降级为过渡，形态 B 为主路径

- 摸底评估：形态 A（rebuild 快照）作为日常流"不现实"——接受，**降级为无服务层时的过渡方案**。
- **主路径定稿**：Obsidian（papers vault）勾选/维护 → md → **形态 B 薄服务层**（`python3 server.py`，`/api/progress` 运行时读 md、`/api/rebuild` 一键重建，工作量 1+ 单元，随批 2 实施）。
- localStorage：仅"webapp 阅读中快速标记"补充，不作事实源（与方案甲一致）。
- 推荐批次调整：**批 2 必含形态 B 服务层**（进度闭环成立的前提），不再作为纯可选。

### R5 执行顺序微调（可直接启动项）

- **建议从阶段三断言 (a)(b)(e) 起步**（不依赖 registry，0 前置）：21 篇 98/99 齐全、TOC≥3、目录↔INDEX 一一对应——全部可直接验证。
- 阶段四（arXiv 脚本）独立可并行。
- 依赖链不变：O0(frontmatter) → O1(registry) → 断言 (c)/O2 图谱。


> 现状（2026-08-13 用户澄清双 vault）：`HermesLocal/papers` 为**独立 vault（可读写，直接指向源）**；另有一份**只读镜像**在统一 vault `ObsFile/ReferenceRead`（仅查看/图谱连通，改动不回传）。
> 定位：**Obsidian = 管理/图谱/进度写入层**（在 papers vault 读写）；webapp = 沉浸阅读/检索层；**md 为唯一事实源**（frontmatter 管元数据、body 管内容）。
> 数据源分工（冲突消解，2026-08-13）：`md(frontmatter+body)` 唯一事实源 → `registry.json` 为派生产物（只读，不手动维护）→ `INDEX.md` 降级为人类浏览索引（不再承担机器数据源，阶段三审计断言保证 frontmatter↔INDEX 一致）；webapp PAPERS 改从 registry 生成。

## O0（前置，P0）：27 个入口文档补 frontmatter

- **范围**：21 篇论文的 `literature_analysis/00_overview.md` + 6 个背景文档（background/*.md）——分章文件不补（Dataview 查论文级信息够用）。
- **字段**：README 模板 + 扩展：
  ```yaml
  ---
  title: Cosmic-ray propagation and interactions in the Galaxy
  authors: [A. W. Strong, I. V. Moskalenko, V. S. Ptuskin]
  year: 2007
  category: 宇宙线传播
  journal: Rev. Mod. Phys. 79 (2007) 2451
  doi: 10.1103/RevModPhys.79.2451
  arxiv: astro-ph/0701517
  read_date: 2026-08-12
  status: completed
  tags: [cosmic-ray, propagation]
  citations: ["0002_trimble-1975"]   # 论文间引用，驱动图谱
  ---
  ```
- **生成**：脚本从各篇 00_overview 表格 + INDEX.md 提取（执行侧已有 H4 解析经验）；**在源（HermesLocal/papers）生成**，再同步到 vault。
- **验收**：27 文件 frontmatter 齐全；Dataview `TABLE year, doi FROM "ReferenceRead/01_cosmic-ray-propagation"` 可查。

## O1：registry.json 由 frontmatter 派生（替代阶段一独立解析）

- `build_registry.py` 改为：读 27 个入口文档 frontmatter → 生成 `registry.json`（结构同 v1）→ webapp PAPERS 从 registry 生成。
- 单一事实源：**frontmatter → registry → webapp**，三处不再各维护。

## O2：图谱走 Obsidian Graph view

- `citations` 字段 + 各篇 `references` 文件加 `[[stem]]` 双向链接（脚本批量加）。
- Obsidian Graph view 零成本出图；webapp 内 SVG 图谱降级为可选（阶段五精简）。

## O3（定稿，2026-08-13 用户选方案甲）：进度进 md，Obsidian 主入口；webapp 显示形态二选一

- **粒度两级**：
  - **篇级**：frontmatter `status`（planned/reading/completed）+ `lastread`（YYYY-MM-DD）——Obsidian 属性面板维护，Dataview 可查
  - **章级**：各分章正文 `- [x]` task list——Obsidian 勾选，webapp 统计"已勾/总数"
- **写入方**：仅 Obsidian（papers vault，可读写）。webapp **不写 md**（静态产物，写不了）。
- **webapp 显示形态**（V1.1 摸底后：形态 A 降级为过渡，形态 B 为主路径）：
  - **形态 B（主路径，批 2 实施）**：薄本地服务层（`python3 server.py`，1+ 单元）——webapp 运行时经 `/api/progress?slug=` 直接读源 md，勾完刷新即见，**免 rebuild**；顺带提供 `/api/rebuild` 一键重建
  - **形态 A（过渡，无服务层时可用）**：rebuild 快照——构建时读 md 的 status/lastread/checkbox 写入产物；勾完进度需 `build_webapp.py` 重建才刷新（摸底评估：作为日常流不现实，故仅作过渡）
- **备选（明确不主用）**：webapp localStorage——仅作"阅读中快速标记"补充，不作为事实源，避免与 md 双轨分裂。
- **ObsFile 只读镜像**：不参与写入，仅统一 vault 内查看/图谱连通。

## 执行顺序（协同版定稿，V1.1 修订后）

```
起步（0 前置，可直接跑）: 阶段三断言 (a)(b)(e) + 阶段四 arXiv 脚本
批1: O0 frontmatter 写回（表格提取→YAML→校验三方）+ 阶段二（Obsidian 勾选，形态 A 过渡）
批2: O1 registry 派生 + 阶段三断言 (c)（含 frontmatter↔表格一致）+ 形态 B 服务层（进度闭环）
批3: O2 图谱（[[链接]]，依赖 O0 citations）+ 术语 hover（阶段五，多对多解析）
批4: 阶段六认知层 + PWA
```

## 数据流总览（双 vault 定稿）

```
Obsidian(papers vault, 读写) ──status/lastread/checkbox/[[链接]]──→ md（唯一事实源）
       │                                                          │ build_registry.py
       ↓（只读镜像）                                                ↓
ObsFile/ReferenceRead(查看/图谱)                          registry.json ──→ webapp(形态A快照 / 形态B运行时)
```



