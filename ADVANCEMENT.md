# 文献管理进阶实施方案（v2 定稿）

> 版本：v2.1（2026-08-13，v2 基础上按二次审查修正字段清单/图谱逻辑/路径主次，断言 b/e 已验证）
> 历史版本：`backup/ADVANCEMENT-v1.0-20260813.md`
> 起草：WorkBuddy（审查/咨询）｜执行：Hermes agent（用户确认后实施）
> 前置：papers 文档库（21 篇精读 + background 知识库 + webapp 4.06MB 单文件）已收尾稳定

---

## 0. 库现状（摸底确认，2026-08-13）

| 项 | 状态 |
|---|---|
| 论文 | 21 篇 / 3 个分类目录 |
| `00_overview.md` | 21/21 ✅（**表格格式，0 frontmatter**） |
| `98_vocabulary.md` / `99_final_summary.md` | 21/21 ✅ |
| `05_glossary.md` | **全库 1 份**（`background/05_glossary.md`，691 行表格，多对多三列：术语/出现论文/释义合并） |
| `registry.json` / `build_registry.py` | 不存在（本方案将创建） |
| `04_critique_index.md` / `00_key_values.md` | ✅ 已存在（阶段六依赖） |

## 1. 架构总览（决策基线，全部写死）

```
Obsidian(papers vault, 读写) ──status/lastread/checkbox/[[链接]]──→ md（唯一事实源）
       │  frontmatter 元数据 / body 内容 / task list                 │
       ↓（只读镜像，不改动）                                           │ build_registry.py
ObsFile/ReferenceRead(统一 vault 查看/图谱)                    registry.json ──→ webapp（形态B运行时 / 形态A快照）
```

**不可改动的决策**：
- D1 **md 是唯一事实源**（frontmatter 管元数据、body 管内容）；`registry.json` 是只读派生产物；`INDEX.md` 降级为人类浏览索引（不再承担机器数据源）
- D2 **进度写入方只有 Obsidian（papers vault）**——webapp 是静态产物写不了 md，localStorage 仅作"阅读中快速标记"补充、不作事实源
- D3 **frontmatter 必须写回**（O2 图谱 citations 与 Dataview 查询依赖）；表格（人类视图）与 frontmatter（机器源）并存，由阶段三断言兜底一致
- D4 进度显示：**形态 B（服务层，主路径）**；形态 A（rebuild 快照）仅作无服务层时的过渡
- D5 双 vault：`HermesLocal/papers` 可读写（源）；`ObsFile/ReferenceRead` 只读镜像（统一 vault 查看/图谱）
- D6 **两条 md→webapp 路径主次分明**：`registry → webapp` 为**元数据主路径**（构建期，PAPERS/标签/审计）；形态 B 服务层 `md → webapp` 为**进度/运行时辅路径**（checkbox/lastread 实时读取）。**进度数据不经过 registry**，两者职责互不重叠。

## 2. 阶段一（P0）：frontmatter + registry（O0 + O1 合并）

**流程**：`00_overview` 表格提取 → 写回 frontmatter → 派生 `registry.json`

1. **提取**（脚本 `webapp/build_fm.py`，复用 H4 解析经验）：从 21 篇 `00_overview.md` 表格解析**自动字段**（Title/Authors/Year/Journal/DOI/arXiv/Keywords/Abstract；注意部分篇含 V1/V2 双版本表格，**取 V1 主体**，字段名差异做容错映射）+ 6 个背景文档；**category 从目录名自动映射**（`01_cosmic-ray-propagation` → 宇宙线传播）
2. **半自动推断**（表格缺失字段，脚本生成骨架，减少人工）：
   - `read_date` ← 00_overview 的 git 首次提交日期（`git log --diff-filter=A --format=%ad`）或文件 mtime
   - `status` ← 默认 `completed`（21 篇已精读完毕，个别人工调整）
   - `tags` ← 从表格 Keywords 字段拆分，人工抽查补领域标签
   - `lastread` ← 初始 = read_date
   - `citations` ← 从各篇 `04_references.md`/正文引用**预填**，人工校准（21 篇批量，固定人工点）
3. **写回**：27 个入口文档（21×`00_overview.md` + 6×background/*.md）写入 YAML frontmatter：
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
   citations: ["0002_trimble-1975"]
   lastread: 2026-08-12
   ---
   ```
   （分章文件不补——Dataview 查论文级信息够用）
4. **派生**（`build_registry.py`）：读 frontmatter → 生成 `registry.json`（数组，结构=frontmatter 字段 + `quality` 从文件数统计 + `key_values` 从 00_key_values 回流）→ webapp PAPERS 改从 registry 生成
5. **校验三方**：frontmatter ↔ 表格 ↔ registry 一致

**验收**：27 文件 frontmatter 齐全；`python3 -m json.tool` 通过；Dataview `TABLE year, doi FROM "01_cosmic-ray-propagation"` 可查；表格未被破坏；read_date/status/tags 抽查 5 篇无异常。
**工作量**：脚本 1–1.5 单元 + 人工抽查（tags/citations 校准，约 0.5–1 小时，可借 Obsidian 属性面板）。

## 3. 阶段二（P0）：阅读追踪 + 复习提醒

- **写入**（唯一入口=Obsidian papers vault）：
  - **篇级**：frontmatter `status`（planned/reading/completed）+ `lastread`（YYYY-MM-DD）+ `read_date`（首次阅读日期）——属性面板维护
  - **章级**：~~各分章正文 `- [x]` task list~~ → **取消**（摸底发现 21 篇 md 源几乎无 task list 数据基础，强行章级会造数据）
- **webapp 显示**（**论文级 completed/reading**，dropdown checkbox + localStorage 持久化）：
  - **形态 B（主路径，批 2 实施）**：薄服务层 `python3 server.py`（Python stdlib）——`/api/progress?slug=` 运行时读源 md 的 `status/lastread`（免 rebuild）；`/api/rebuild` 一键重建；`/` 静态服务 webapp
  - 形态 A（过渡）：构建时读 md 写入产物快照，勾完需 rebuild
  - 复习提醒：`status=completed` 且 `now - lastread > 30 天` → 首页「建议复习：B²FH 1957（45 天未读）」
- **进度粒度变更**（附 13）：从"章级 task list"降为"论文级 completed/reading"——md 源无 task list 数据基础，论文级粒度已能覆盖"读完未读完"语义，复习提醒仍按阈值触发

## 4. 阶段三（P0）：构建期知识审计断言

在附 4 既有断言（id 唯一/label 合法/stats 一致）基础上增加：
- a) 每篇含 `00_overview.md`、`98_vocabulary.md`、`99_final_summary.md`（已确认 21/21 齐全，可直接启用）
- b) 每篇 TOC ≥3 条（**已验证：21/21 满足**，webapp TOCS 按 parent 分组统计）
- c) **frontmatter ↔ 00_overview 表格字段一致**（R1 双源兜底）；registry 存在时 label 与 registry 一致
- d) 全库 `background/05_glossary.md` 存在且术语表格行 ≥600（实测 691 ✓）
- e) 目录 `0[0-9]_*/NNNN_*/` ↔ `INDEX.md` 一一对应（**已验证：21↔21 无缺失无多余**）

任一失败非零退出。**工作量**：0.5 单元。

## 5. 阶段四（P1）：arXiv 元数据半自动

`webapp/fetch_arxiv.py`（stdlib urllib，无第三方依赖）：输入 arXiv ID/关键词 → `export.arxiv.org/api/query` 抓元数据+PDF → 生成 `NNNN_作者-年份/` 目录 + frontmatter 模板 md + 下载 PDF + 追加 registry 条目。
**验收**：真实论文跑通，产物符合 README 命名规范。**工作量**：1 单元。

## 6. 阶段五（P1）：术语 hover + 图谱

- **术语 hover**：解析 `background/05_glossary.md` 三列多对多结构（术语/出现论文/释义合并，术语列含 `·` 分隔多篇）→ `{术语: {释义, 出现论文[]}}` 注入 webapp `GLOSS` → 正文命中术语 hover 显示释义+出处
- **图谱**（问题 2 修正，两层配合）：
  - **论文级**：`00_overview.md` frontmatter 的 `citations` 字段驱动图谱（Obsidian Graph view 论文节点间连线）
  - **分章级**：分章 .md **不补 frontmatter**，但正文（各章 references/导航）加 `[[stem]]` 链接——Obsidian 内可见篇内/篇间关联
  - webapp SVG 图谱降级为可选
- **工作量**：1–1.5 单元

## 7. 阶段六（P2）：认知层

- 综述/讲义：background + registry 按主题生成（人工/AI 混合审校）
- 争议点演化：`04_critique_index.md` 结构化（争议主题→各文献立场→时间线）
- **工作量**：2+ 按需

## 8. 生态（P1）：PWA + 双机分工

- PWA：`manifest.json` + apple-touch-icon，Safari 添加到主屏幕
- Mac mini：PDF 批量解析、registry 检索等重任务；MacBook 精读/审查

## 9. 执行顺序

```
起步（0 前置，可直接跑）：阶段三 (a)(b)(e) + 阶段四 arXiv
批1：阶段一（frontmatter 写回 + registry）+ 阶段二（Obsidian 勾选，形态 A 过渡）
批2：阶段三 (c)(d) 断言 + 形态 B 服务层（进度闭环成立）
批3：阶段五（术语 hover + 图谱）
批4：阶段六 + PWA
```

## 10. 验收总则

- 每阶段：`build_webapp.py --include-papers` 跑通 + 附 4 断言全绿 + headless Chrome 运行时验证（懒加载 1 section、0 console error）+ 桌面 1280/移动 375 截图
- 数据一致性三方对照：`frontmatter ↔ registry.json ↔ webapp 产物`
- 新增文献走 `papers/ENHANCEMENTS.md` 顶部 SOP，registry/审计自动兜底

## 11. 工作量总览

| 阶段 | 内容 | 预估 |
|---|---|---|
| 一 | frontmatter 写回 + build_fm.py + build_registry.py | 1.5–2 |
| 二 | Obsidian 勾选 + 形态 A（0.5–1）+ 形态 B 服务层（1+） | 1.5–2 |
| 三 | 审计断言（a–e） | 0.5 |
| 四 | arXiv 脚本 | 1 |
| 五 | 术语 hover（多对多）+ 图谱 | 1–1.5 |
| 六 | 综述/争议演化 | 2+（按需） |
| 生态 | PWA | 0.5 |
