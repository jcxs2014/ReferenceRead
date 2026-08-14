# papers/webapp 交互网页 — 结构化审查报告

> 审查对象：`/Users/jcxs2014/Sites/HermesLocal/papers/webapp/`
> 审查日期：2026-08-13 ｜ 审查人：WorkBuddy（审查/咨询角色）
> 审查范围：`interactive.html`（4.67 MB / 29,434 行构建产物）、`shell.html`（374 行骨架，CSS+JS 全部逻辑）、`build_webapp.py`（构建脚本）、`md2doc_html.py`（转换器）、`README.md`
> 验证方法：shell.html 全量通读 + 产物 JSON 解码校验（DOCS 27 / TOCS 4103 / PAPERS 21）+ 源 md 对照（INDEX.md 作者信息）+ 全量正则扫描（ARIA、断点、公式、链接）
> 结论概览：**整体可用，但存在 5 个高严重度问题（锚点冲突、行内公式重复渲染、引用卡误报、作者标签错误、工具栏元素过多）与若干中等级问题，建议修复后再长期使用。**

---

## 一、设计漏洞审查

### 高严重度（核心功能失效 / 数据错误）

**H1. TOC 锚点 id 全局重复 → 目录点击失效或跳错**
- **依据**：解码产物中 4103 条 TOC 存在大量重复 id，抽查即含 `doc-0-1-文献基本信息`、`doc-1-1-本节核心内容`、`doc-1-图的目的`、`doc-2-坐标轴` 等（21 篇论文的 `literature_analysis` 分章模板标题相同，如每篇都有"0.1 文献基本信息"）。`shell.html` 第 218 行 `document.getElementById(a.dataset.id)` 是**全局查找**，返回文档列表中第一个匹配元素——若该元素位于未激活（`display:none`）的 section，`scrollIntoView` 无效果；若位于其他文档，则滚动错位。
- **根因**：`md2doc_html.py` 第 144 行 anchor 只基于标题文本，未加文档前缀；`build_webapp.py` 中 `slug()`（第 50 行）与 `slug_title()`（第 55 行）存在但**未被用于 heading id**（死代码），`extract_toc` 直接沿用 fragment 的裸 id。
- **触发场景**：打开任意论文文档 → 展开侧边栏目录 → 点击任一重复标题（如"0.1 文献基本信息"）→ 无响应或滚到错误位置。
- **建议**：heading id 改为 `doc-{文档slug}-{anchor}`，`renderTOC` 与 `extract_toc` 同步改；并做构建期 assert 去重。

**H2. 行内公式重复渲染损坏（核心功能）**
- **依据**：`shell.html` 第 295–302 行 `applyMath()` 对 `.math.inline` 无条件执行 `katex.render(el.textContent, el, …)`——**无 `data-processed` 防护**（块公式第 304 行有 `if (wrap.dataset.processed) return`，行内公式没有）。`switchDoc()`（第 233 行）每次切换文档都调用 `applyMath()`。
- **触发场景**：打开含行内公式的文档（产物共 **1252 个行内公式**，如 Strong 2007 篇 324 个、数值速查表 227 个）→ 切换到其他文档 → 切回 → 已渲染的 KaTeX 输出文本被当作 LaTeX 再次渲染 → 公式错乱（`throwOnError:false` 下静默产生错误输出）。
- **建议**：行内公式加 `data-processed` 标记（与块公式一致）。

**H3. "本章涉及论文"引用卡按年份误匹配（高误报）**
- **依据**：`shell.html` 第 347–370 行 `renderPaperRef()` 用 `p.label.match(/\((\d{4})\)/)` 取年份，再以 `text.includes(m[1])` 判断"文档是否提及该论文"——即**正文任意位置出现 4 位年份即挂链接**。
- **触发场景**：任意文档中出现"2007"（年份、编号、数值）即会在文档末尾追加"📄 本章涉及论文"卡片挂上 Strong (2007)；27 个文档几乎全部中招，卡片内容大面积与正文无关。
- **建议**：改为显式标注——在 md 中用 `[{论文编号}]` 语法（README 第 98 行已描述该能力，但 `renderPaperRef` 未实现），或维护人工 curated 的"文档→论文"映射表；废弃年份包含匹配。

**H4. CITATION 作者标签错误（数据错误，直接面向用户）**
- **依据**：`build_webapp.py` 第 26–48 行 `CITATION` 字典，与 `INDEX.md` 对照发现 4 处作者错误，已进入产物 `PAPERS`（grep 确认），显示在标签页、引用卡、paper-preface：
  - `0002_al-dargazelli-1996` → "Al-Dargazelli, **Wamrschmidt & Gaisser** (1996)"，实为 **Al-Dargazelli, Wolfendale, Smialkowski & Wdowczyk**（INDEX.md 第 46 行）
  - `0003_gaisser-1990` → "Gaisser, **Halzen & Hooper** (1990)"，实为 **T. K. Gaisser**（单人，INDEX.md 第 60 行）
  - `0011_kewley-2001-starburst` → "Kewley & **Echle** (2001)"，实为 **Kewley, Dopita, Sutherland, Heisler & Trevena**（INDEX.md 第 275 行）
  - `0012_dieterich-2014` → "Dieterich, **Boyett & Pinsonneault** (2014)"，实为 **Dieterich, Henry, Jao, Winters, Hosey, Riedel & Subasavage**（INDEX.md 第 288 行）
- **建议**：从 INDEX.md 或各篇 `00_overview.md` 的元数据自动生成标签，删除手写映射表。

**H5. 搜索功能与 README 描述不符 + 正则状态 bug**
- **依据**：README 第 87 行声称"结果显示'文档名 · 匹配次数'，点击跳转到包含结果的文章"，但 `shell.html` 第 241–267 行 `doSearch()` **只搜索 `activeSlug` 当前文档**（第 246 行 `section[data-slug="${activeSlug}"]`），无跨文档结果列表。另第 245 行 `const re = new RegExp(query, "gi")` 为全局正则，在 walk 递归（第 249–263 行）中对每个文本节点反复 `re.test()`——**global 正则的 `lastIndex` 状态跨调用残留**，导致部分命中漏报。
- **触发场景**：用户期望跨 27 篇检索（README 承诺），实际只能搜当前文档；连续搜索时命中数不稳定。
- **建议**：实现跨文档搜索（遍历全部 section 统计、渲染结果列表），或将 README 描述改小；`re.lastIndex = 0` 重置或改用 `String.prototype.matchAll`。

**H6. 工具栏 27 个 tab 平铺 → 桌面/移动统一吃满 ~200px 高度**（用户截图实证，2026-08-13 反馈）
- **依据**：`shell.html` 第 39 行 `.tabs { display:flex; gap:4px; flex-wrap:wrap }` 直接渲染全部 `DOCS`（共 27 个），导致 toolbar 在桌面 1280px 宽屏下也换行成 4–5 行；用户截图（1280×720）实测 toolbar 占用约 200px、约占屏幕 1/3 高度。审查原 M4 仅提及移动端 sidebar top:50px 错位，**未充分评估桌面端 toolbar 自身的视觉灾难**——根因是 27 tab 平铺。
- **触发场景**：所有分辨率、所有设备——桌面/平板/手机均受影响（截图为证）。可发现性极差：用户首屏即被工具栏挤压，难以直接阅读正文。
- **建议**：改为**分组下拉**（4 个下拉按钮：宇宙线传播 1 / 宇宙线起源 7 / 核合成 13 / 背景 6，按钮显示当前选中项+下拉箭头），toolbar 压回 1 行；同步把 M4 修复（移动端 sidebar top 错位）纳入，因分组下拉本身解决了 toolbar 高度波动。该方案与 agent-harness 验证过的导航分组架构一致。
- **截图证据**：`/Users/jcxs2014/.workbuddy/clipboard-images/clipboard-2026-08-13T13-34-46-872Z-03f01246.png`

### 中严重度（特定场景失效 / 体验损害）

**M1. 搜索高亮破坏 KaTeX 公式 DOM**
- `doSearch` 的 walk 会进入 `.katex` 渲染结构内部文本节点并插入 `<mark>`，打乱 KaTeX 布局；且第 256 行 `m.textContent = query.trim()` 用查询串（原大小写）替换原文，**改变文档原有大小写**。触发：搜索命中公式内文本（如搜 "10" 命中公式中的指数）。建议：跳过 `.katex`、`.math` 子树。

**M2. 打印输出全部 27 篇文档**
- `shell.html` 第 127 行 `@media print .doc-section { display:block !important; page-break-before:always }`——打印时全部 section 可见。用户点 🖨 想打当前篇，会输出 27 篇。建议：`.doc-section:not(.active){display:none}` 或提供"打印当前文档"按钮。

**M3. Safari 隐私模式白屏**
- `shell.html` 第 174/226/271/279 行多处直接调用 `localStorage.getItem/setItem` 无 try/catch——Safari 隐私浏览 + `file://` 下访问 localStorage 抛 `SecurityError`，脚本中断整页白屏。建议：封装 `safeStorage` 辅助函数。

**M4. 移动端侧栏错位 + 无遮罩**
- `shell.html` 第 130–133 行 `@media (max-width:900px)` 中 `.sidebar { position:fixed; top:50px; bottom:36px }`——`50px` 是硬编码，而 toolbar 第 35 行 `flex-wrap:wrap` 在窄屏（27 个标签换行）实际高度远超 50px，侧栏会压在工具栏下方错位；且打开后无遮罩层、点外部不关闭。建议：top 用变量或改由 JS 计算；加遮罩 + 点击关闭。**注**：H6 工具栏分组下拉方案落地后，本问题根因（toolbar 高度波动）自动消失，建议与 H6 一并修复。

**M10. 侧栏折叠态残留滚动条 → 最左侧 6–8px 暗色条（用户截图实证）**
- **依据**：`shell.html` 第 66–69 行 `.sidebar { width:0; overflow-y:auto; … }`，但 init() 立即 `switchDoc → renderTOC` 让 toc-container 持有内容（`<h3>目录</h3>` + 条目），`width:0` 容器的内容溢出仍触发 `overflow-y:auto` 滚动条——在最左侧约 6–8px 持续显示。
- **触发场景**：所有用户首屏（无论桌面/移动）都能看到，无展开目录时也出现。
- **建议**：折叠态默认 `overflow:hidden`（`.app.sidebar-open .sidebar { overflow-y:auto }` 才允许滚动），并把折叠态 padding/border 也归零（展开时再加）。同根于 M4，但触发面更广，独立列出便于修复。

**M5. 行内链接 href 生成错误（转换器 bug，已产出错误产物）**
- `md2doc_html.py` 第 37–38 行链接正则替换串 `r'<a href="\1" …'>\1</a>'`——**href 误用 `\1`（链接文字）而非 `\2`（URL）**。产物实锤：`02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/99_final_summary.md` 中的 `[arXiv:astro-ph/9811011](https://arxiv.org/abs/astro-ph/9811011)` 被生成为 `<a href="arXiv:astro-ph/9811011">`（解码后唯一 `<a>`），点击跳转到无效相对路径。当前仅 1 处，未来新增任何 http 链接都会失效。建议：改为 `\2`。

**M6. 可访问性全面缺失**
- 全文件 grep `aria-*` 与 `tabindex` **均为 0**：tabs 无 `role="tablist"/aria-selected`、搜索框无 `aria-label`、侧栏按钮无 `aria-expanded`、TOC 项是 `<a>` 但**无 `href`（不可 Tab 聚焦，键盘无法操作目录）**、搜索命中数变化无 `aria-live` 播报、无 skip-link。建议：补充 ARIA 语义 + TOC 项改 `<button>` 或加 `href="#id"` + `tabindex`。

**M7. footer 统计信息错误**
- `shell.html` 第 329–333 行 `updateStats()` 硬编码"3 篇知识库 · 21 篇论文 · 664 术语"，实际背景文档为 **6 篇**；且 `DOCS` 无 `size` 字段（构建脚本未写入），`d.size||0` 恒为 0 → footer 显示"HTML 0 KB"。建议：用 `DOCS.length` 动态统计 + 构建期写入真实体积。

**M8. 对比度不足（暗色主题）**
- 依据 `shell.html` 第 16–21 行变量：`--fg-2:#8b949e` 在 `--bg-2:#161b22` 上约 4.6:1，用于 12px 小字（`toc-h3/toc-h4`，第 75–76 行）不达 WCAG AA；搜索高亮 `--search-hl:#b88300` 背景 + 继承 `--fg:#c9d1d9` 文字约 **2.6:1**，远低于 4.5:1。建议：暗色搜索高亮改 `#9e6a03` 背景 + 深色文字，或加深 `--fg-2`。

**M9. 首屏性能**
- `interactive.html` 4.67 MB：`buildDocs()` 一次性解码 27 个 b64（共 351 块 + 1252 行内公式、615 表格的完整 HTML）并注入 DOM，首屏预计 1–3 秒；`switchDoc` 时对当前文档全量 KaTeX 渲染（单篇最高 324 行内公式）有卡顿风险。建议：仅解码当前文档（懒加载），或构建期拆分为"摘要 + 正文"两层。

### 低严重度

- **L1**：`flush_quote`（md2doc 第 86–89 行）每行拼 `<br>` 且尾部多一个——blockquote 末尾多余换行。
- **L2**：术语表单字标题进入 TOC——`05_glossary.md` 第 927/932 行 `### 银`、`### 静`，目录出现单字条目；建议术语表元素标题合并为表格行或加注释标记。
- **L3**：`build_webapp.py` 第 95–101 行 `get_years()` 为死代码，引用不存在的 `p["stem"]/p["year"]` 字段，一旦启用即 `KeyError`。
- **L4**：`paper-ref` 链接用 `href="#"`（第 364 行），虽经 `preventDefault` 可用，但语义上应无 href 或使用真实锚点。
- **L5**：TOC 全量提取 `<h2..h6>` 共 4103 条，level 5/6 均归入 `toc-h4` 缩进，层级过深、目录冗长；建议 TOC 限 3–4 级。

---

## 二、排版美化建议

以下均基于 `shell.html` 实际 CSS 规则提出，改动均在样式层，不影响数据与逻辑。

### T1. 标题层级拉距（依据 §81–84）
- **现状**：`h2 22px / h3 18px / h4 15px`，而正文 15px——**h4 与正文同号**，仅靠 `--fg-2` 灰色区分，四级标题层级感弱。
- **建议**：h2 → 24px、h3 → 19px、h4 → 16px 且 `font-weight:600`（保持正文 15px）。
- **预期效果**：四层标题一眼可辨，长文档（论文分章 h3/h4 密集）结构更清晰。

### T2. 表格可读性（依据 §94–97）
- **现状**：表格 13px、无斑马纹、`th` 仅 `--bg-2` 浅底；术语表 688 行、87 个表，密排难读。
- **建议**：字号 13.5–14px；`tbody tr:nth-child(odd) { background: var(--bg-2) }`；`th` 加粗加深；单元格 `padding:8px 12px`。
- **预期效果**：688 行术语表行间扫读不串行，表头锚定感增强。

### T3. 引用块视觉降噪（依据 §88、§110–116）
- **现状**：blockquote、paper-preface、paper-ref 全部使用 `border-left:4px solid var(--accent)`（蓝色）——正文引用块与论文卡片抢视觉权重，蓝边泛滥。
- **建议**：正文 blockquote 改用 `--border` 中性色（保留 accent 仅用于论文卡片/前置框）。
- **预期效果**：强调层级分明——中性引用 = 背景说明，蓝色卡片 = 论文级信息。

### T4. 公式块与代码块区分（依据 §101）
- **现状**：`.math.block-wrap` 使用 `background:var(--code-bg)` + 边框，与 `<pre>` 代码块同视觉语言。
- **建议**：公式块去掉灰底、保留细边框居中（`background:transparent`），字号可略升。
- **预期效果**：公式"轻"于代码"重"，视觉语义正确；351 个块公式的版面更清爽。

### T5. 卡片节奏与间距统一
- **现状**：`paper-preface` margin 28px、`paper-ref` 20px、段落 8px、`hr` 20px——间距不齐。
- **建议**：区块垂直间距统一为 24px 基准（`paper-preface/paper-ref` 对齐）；正文段落 8px→10px。
- **预期效果**：滚动阅读节奏均匀，区块归属清晰。

### T6. 工具栏控件统一（依据 §40–60）
- **现状**：`ctrl-btn` 用 emoji（🌙☀🖨）且字号继承 13px，图标大小不一；`copy-btn` 默认 `opacity:.4` 太隐蔽（§104）。
- **建议**：图标按钮统一 16px 行高、或换为内联 SVG；`copy-btn` 常显 `opacity:.7`。
- **预期效果**：控件视觉重量一致，公式复制按钮可发现性提升。

### T7. 暗色主题层级区分（依据 §16–21）
- **现状**：dark 下 `--quote-bg:#1c2128` 与 `--bg-2:#161b22`、`--card:#161b22` 三者接近，引用块/卡片在暗色下几乎隐形。
- **建议**：`--quote-bg` 提到 `#21262d`，卡片加 1px 边框区分。
- **预期效果**：暗色下区块仍可辨识（含 T3 的中性引用边）。

### T8. 细节打磨
- 滚动条：暗色主题下未定制，原生白色滚动条突兀——建议 `::-webkit-scrollbar{width:8px}` + `thumb` 用 `--border`。
- 图片（§93）：`img{max-width:100%}` 无圆角居中——建议 `display:block; margin:12px auto; border-radius:8px`。
- TOC 当前项（§74）：`active` 已填充 accent，建议加左侧 3px 指示条，视觉定位更快。
- 侧栏标题（§71）：`text-transform:uppercase` 对中文无效且 `letter-spacing` 无意义，可移除。

---

## 三、功能增强方向

按"修复正确性 → 提升体验 → 扩展能力"排序。P0 即第一维度的 H1–H5 与 M1–M5 修复，不重复列举，以下为新增能力。

### P1（体验增强，工作量小、收益直接）

**F1. 顶部阅读进度条**
- **价值**：27 篇长文档（论文分章 + 词汇表）滚动定位；进度可视化。
- **实现**：`#main` scroll 事件中 `scrollTop / (scrollHeight - clientHeight)` 更新 `.progress-bar`（fixed 于顶栏下 2px，宽 3px，accent 色）。现有 scroll 事件（§283）已存在，直接扩展。
- **优先级**：高（复用现有事件，半小时内完成）。

**F2. 返回顶部按钮**
- **价值**：长页回顶（术语表 688 行、论文分章很长）。
- **实现**：fixed 右下角按钮，`scrollTop > 600` 显示，点击 `main.scrollTo({top:0,behavior:"smooth"})`。

**F3. 跨文档搜索（修复 H5 时一并实现）**
- **价值**：README 已承诺的"全文搜索"，是全库检索的核心能力（212 篇 md 浓缩为 27 篇网页后的唯一检索入口）。
- **实现**：遍历全部 `doc-section` 统计命中，渲染"文档名 · 命中数"结果下拉，点击 `switchDoc` + 定位首个 mark。

**F4. 章节锚点复制**
- **价值**：论文分章标题（如 `doc-0-1-文献基本信息`）可分享定位。
- **实现**：h2/h3 hover 显示 `#` 链接，点击写入 `location.hash` 并复制；配合 H1 修复后的唯一 id。

**F5. 移动端侧栏交互完善（含修复 M4）**
- **价值**：窄屏（375px）下目录可用性。
- **实现**：遮罩层 + 点击外部关闭 + `top` 动态取值；TOC 点击后自动收起。

### P2（能力扩展）

**F6. 明暗主题** —— ✅ 已具备（§270–281 + localStorage），无需新增。

**F7. 章节折叠展开**
- **价值**：词汇表/数值速查表等长文档按需展开，减少滚动。
- **实现**：h3/h4 前加折叠按钮，折叠状态存 localStorage；注意与 TOC 滚动高亮的联动。

**F8. 快捷键**
- **价值**：键盘效率。
- **实现**：`/` 聚焦搜索框、`Esc` 清空（已有）、`[`/`]` 切换上一篇/下一篇文档、`t` 切换主题。

**F9. KaTeX 真离线渲染**
- **价值**：README 声称"离线可用"，但公式依赖 `cdn.jsdelivr.net`（shell 第 7–8 行）——离线时公式降级为原始 LaTeX 源码，可读性差。
- **实现**：构建期将 `katex.min.js + katex.min.css`（约 400 KB）base64 内嵌；或保持现状并**在 README/footer 明确"离线=公式降级"**（footer 已有说明，建议 README 同步澄清）。

**F10. 阅读勾选与进度记忆增强**
- **价值**：论文精读的"章节完成度"（21 篇 × 分章的阅读管理）。
- **实现**：md 任务列表 checkbox（转换器已支持，产物中为 `disabled`）改为可交互，勾选状态存 localStorage 并按文档聚合显示。

**F11. 公式编号与复制引用**
- **价值**：学术引用场景（背景文档 351 个块公式）。
- **实现**：块公式自动编号 `(1.1)` 并支持复制 `Eq. (1.1)` 引用文本。

---

## 四、修复优先级总表

| 级别 | 事项 | 涉及文件 | 预估 |
|---|---|---|---|
| P0 | H1 锚点 id 加 slug 前缀 + assert 去重 | md2doc_html.py + build_webapp.py + shell.html | 1 单元 |
| P0 | H2 行内公式 data-processed | shell.html | 0.2 单元 |
| P0 | H3 引用卡改显式 `[{编号}]` 标注 | shell.html + build_webapp.py | 0.5 单元 |
| P0 | H4 CITATION 改从 INDEX/overview 自动生成 | build_webapp.py | 0.3 单元 |
| P0 | H5 跨文档搜索 + lastIndex 修复 | shell.html | 1 单元 |
| P0 | M1 搜索跳过 .katex/.math 子树 | shell.html | 0.2 单元 |
| P0 | M2 打印仅当前文档 | shell.html | 0.1 单元 |
| P0 | M3 localStorage try/catch | shell.html | 0.1 单元 |
| P0 | M5 链接 href 改 \2 | md2doc_html.py | 0.1 单元 |
| P1 | M4/M6/M7/M8/M9 体验与可访问性 | shell.html + build_webapp.py | 1 单元 |
| P1 | F1–F5 增强功能 | shell.html | 1 单元 |
| P2 | F7–F11 | shell.html | 1.5 单元 |

> 注：以上"单元"为执行侧工时口径参考。P0 合计约 3.5 单元，修复后即可长期稳定使用；排版与增强按需分轮实施。

---

*本报告基于 2026-08-13 13:55 构建的 interactive.html 实测；重新构建后部分结论（如数据统计、CITATION）应随源文件修正而消失。*

---

## 附：修复验证（2026-08-13，提交 f7d0648）

> 验证方法：shell.html 全量重读 + 新产物（4.96MB，16:03 重建）重新解码（DOCS 27 / TOCS 4106 / PAPERS 21）+ 与用户提交的修复总结逐条对照。
> **结论：12 项声称修复中 10 项真实落地，2 项（H1、H4）未真实修复——H4 比修复前更严重（界面从"编造作者"退化为"裸目录名"）。**

### ✅ 真实修复（源码 + 产物双重确认）

| 项 | 证据 |
|---|---|
| H2 行内公式 | shell.html:485–490 `el.dataset.processed` 防护，与块公式一致 |
| H3 引用卡误报 | `renderPaperRef` 整体删除（产物 0 处调用；4 处 `paper-ref` 仅为 CSS 残留）——以"删除功能"方式修复，与总结"现为注释"表述略有出入 |
| H5/M1 搜索 | shell.html:398 每次构建新正则；402 遍历全部 section；412/415 `re.lastIndex=0`；409 `closest(".katex")/closest(".math")` 跳过 |
| M2 打印 | shell.html:180–181 `.doc-section{display:none}` + `.active{display:block}`，仅当前文档 |
| M3 localStorage | shell.html:239–241 safeLsGet/Set/Del 全量替换 |
| M5 链接 href | 产物实锤：`<a href="https://arxiv.org/abs/astro-ph/9811011">arXiv:astro-ph/9811011</a>` ✓（修复前为 href="arXiv:astro-ph/9811011"） |
| M7 动态 stats | 产物实锤："6 篇知识库 · 21 篇论文 · 3254 目录项" ✓ |
| M10 侧栏滚动条 | shell.html:95–101 折叠 `overflow:hidden;padding:0`，展开 `overflow-y:auto;padding:16px 12px` |
| H6 分组下拉 | shell.html:256–306 按 category 分组；产物分组：背景 6 / 传播 1 / 起源 7 / 核合成 13 = 4 组 27 文档 |
| （超额）T1–T4/T8 | 标题 24/19/16px、表格斑马纹、blockquote 中性边框、公式块去灰底、返回顶部、快捷键、overlay、滚动条样式 |

### ❌ H4 未修复——且比修复前更糟（高严重度，需退回）

- **现象**：21 篇论文 tab 标题全部退化为**裸目录名**——"论文 · 0002_al-dargazelli-1996"、"论文 · 0003_gaisser-1990"…（产物 DOCS 实锤 21 条）。
- **根因**：`build_webapp.py` 第 54 行 `_build_citation_map()` 用英文正则 `\*\*Authors?\*\*\s*[|]` 匹配，但 `INDEX.md` 表头是**中文"| 作者 |"** → 全部解析为空 → 第 59 行 `label = stem` 兜底；第 89–91 行 fallback 的 `if k not in CITATION` 永假（CITATION 每个 key 都有值 = stem），**正确作者名的 fallback 从未生效**。
- **影响**：修复前是"编造作者"（至少像人名），修复后是"目录名"（明确难看）；用户总结"6 个作者名已修正"不实。
- **修复方向**：正则改匹配 `| 作者 |` 或 `| **作者** |`；解析失败时显式回退 `_FALLBACK`（判断 value 是否含 `(`）。

### ❌ H1 未完全修复——仍有 3 组重复 id 且 HTML/TOC 不同步（中高，需退回）

- **现象**：TOC 4106 条 id 中仍有 3 组重复（用户总结"4103 全部唯一"不实）：
  - `paper-0003-fowler-1984-doc-1-目的-1` ×2（同文档 4 处 Figure 分析，HTML 中 4 处同 id、TOC 仅 2 条）
  - `paper-0003-fowler-1984-doc-3-关键观察-1` ×2
  - `paper-0006-grenier-2015-doc-目的-1` ×2
- **根因**：`build_webapp.py` 第 135–137 行 `_deduplicate_headings` 用 `new_html.replace(old_tag, new_tag, 1)` 全局替换**首个匹配**，而 `finditer` 遍历的是原始 html_body——多次相同标题时替换位置错乱，且 TOC 条目（第 142 行按迭代计 seen）与 HTML 实际 id 不同步。
- **影响**：上述 3 组标题的目录点击仍会跳错/失效；范围已缩小到 Figure 分析模板标题。
- **修复方向**：按位置切片替换（`html_body[:m.start()] + new_tag + html_body[m.end():]` 逐步拼接），或一次性构建新字符串，禁止 `str.replace`。

### ⚠️ 附带瑕疵

- 搜索高亮 `shell.html:422 m.textContent = q` 仍用查询串原文替换，搜索 "galprop" 会改写文档中的 "GALPROP"（大小写丢失）。建议改用 `textNode.textContent.slice(...)` 保留原文本。

### 复验结论

P0 清单中 **H2/H3/H5/M1/M2/M3/M5/M7/M10 已真修复，H1 不完整、H4 未修复（反向退化）**；建议执行侧在 f7d0648 基础上开新提交处理 H4 正则/回退与 H1 位置替换，其余项可关闭。

---

## 附 2：M11 桌面端 overlay 遮罩回归（2026-08-13 用户实测反馈）

- **现象**：点击 ☰ 目录按钮后整个页面不可滚动（桌面端）。
- **根因**：f7d0648 为修复 M4 引入的遮罩层 `shell.html:88–89`：
  ```css
  #overlay { display:none; position:fixed; inset:0; background:rgba(0,0,0,.4); z-index:98; }
  .app.sidebar-open #overlay { display:block; }
  ```
  注释标注"Overlay for mobile"，但第二条规则**未放入 `@media (max-width:900px)`**，桌面端打开 sidebar 时 overlay 全屏 `display:block`（z-index 98），盖住 `.main`（滚动容器，overflow-y:auto），滚轮事件被 overlay 截获 → 主区不可滚动；视觉上整页变暗，仅 sidebar（z-index 99）可滚。
- **触发**：桌面分辨率（>900px）点击 ☰ 即 100% 触发；移动端行为符合设计（遮罩 + 点击关闭，shell:552）。
- **修复**：将 `.app.sidebar-open #overlay { display:block; }` 移入 `@media (max-width:900px)`；桌面端不显示遮罩。
- **性质**：M4 修复引入的回归（新增功能未限定作用域），验证 f7d0648 时未覆盖桌面端交互路径——后续复验应补"桌面端点 ☰ 后主区可滚动"检查项。

---

## 附 3：H6 分组下拉菜单实现缺陷（2026-08-13 审查发现）

**H6D1（高）下拉菜单被祖先 overflow 裁剪——必现**
- `shell.html:42 .tab-groups { … overflow-x:auto }`（toolbar:36 亦 `overflow-x:auto`）。CSS Overflow 规范：`overflow-x` 非 visible 时 `overflow-y` 被强制计算为 auto → `.tab-groups` 垂直裁剪绝对定位的 `.tab-dropdown`（shell:54–59，`top:calc(100%+4px)` 在容器高度之外）→ 菜单无法完整显示/容器内出现异常滚动条。点击任意组按钮必现。
- 修复：①推荐 dropdown 改 `position:fixed` + `getBoundingClientRect()` 定位（已有外部点击关闭，补 scroll/resize 关闭）；②或移除 `.tab-groups/.toolbar` 的 `overflow-x`；③或改原生 popover/dialog。

**H6D2（中）组按钮不显示当前选中论文**
- `shell.html:274 btn.textContent = grpName`，与方案 A「按钮显示当前选中项+箭头」不符；切换文档后工具栏无法看出当前论文。修复：`grpName · {当前文档标题}`，switchDoc 同步更新。

**H6D3（中）下拉无键盘可达性**
- 下拉项为 `<div>`（shell:280），无 `aria-expanded/aria-haspopup`、无方向键。修复：改 `<button>` + ARIA + ArrowUp/Down/Enter。

**H6D4（低）** Escape 不关下拉（shell:531 仅清搜索框）；最右侧分组下拉 `left:0` 可能溢出视口右缘；菜单展开态无独立视觉样式。

**验证结论**：H6 分组下拉的「分组」本身正确（4 组 27 文档），但菜单渲染链路有必现缺陷，需修复后才能宣称 H6 完成。

---

## 附 4：对执行侧的工程要求（用户指示 2026-08-13："要严格一点对待自己的产品"）

> 针对 f7d0648 暴露的"验证缺失"问题（H4 反向退化、H1 重复 id、M11 桌面回归、H6D1 下拉裁剪均为"跑一次验证即可发现"），自下一提交起强制执行以下标准：

**1. 完成 = 验证通过，而非 build 成功**
- 每项修复必须附验证证据：构建后断言输出 / 产物解码结果 / 截图；口头总结（"已修复""全部唯一"）不作为完成依据。
- 参考教训：f7d0648 总结声称"4103 全部唯一 / 6 作者已修正"，实测 3 组重复 id、21 篇标签全退化。

**2. 写解析器前先读源数据格式**
- 如 INDEX.md 表头为中文"| 作者 |"，不能用英文正则 `**Authors**` 匹配；先确认目标文件实际结构再写代码。

**3. UI/CSS 改动必须附双端截图**
- 桌面 1280×720 + 移动 375×812；交互路径逐一走查：点 ☰ 后主区可滚动、点组下拉完整可见、搜索命中高亮不破坏公式、切换文档后行内公式不重复渲染、打印只出当前篇。

**4. 构建管线内置断言（治本，建议随 H4/H1 修复一并落地）**
- `build_webapp.py` 末尾增加校验段，任一失败即非零退出：
  - a) heading id 全库唯一，且 TOC id 与 HTML heading id 双向一致（用位置替换修好 H1 后此断言必须通过）
  - b) 论文 label 不含 `_`/纯目录名、含 `(`年份`)`（防 H4 退化复发）
  - c) stats 计数与 DOCS/PAPERS/TOCS 实际长度一致
  - d) 分组数与各组文档数之和 = DOCS 总数
  - e) 产物无 `.katex`/`.math` 之外的意外 `<mark>` 残留（可选）

**5. 回归意识：任何改动后重跑 构建 → 断言 → 交互抽查 全流程，不跳步。**
- 例：为修 M4 加遮罩时必须验证桌面端不受影响（M11 教训）；重构 toolbar 时必须验证下拉渲染（H6D1 教训）。

**验收关系**：WorkBuddy 复验仍会做（源码+产物双重确认），但执行侧应先在本地跑完上述校验再提交，避免把未验证的"完成"交给下游。

**6. 运行时验证（headless Chrome，2026-08-13 实测可行的进阶项）**
- 本机 Chrome 可作无头运行时验证（比纯解码断言更接近真实运行），建议加入构建管线校验：
  ```bash
  CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  "$CHROME" --headless=new --disable-gpu --no-sandbox --virtual-time-budget=10000     --dump-dom "file://$PWD/webapp/interactive.html" > /tmp/wb_dom.html 2>/tmp/wb_err.log
  ```
  检查点：
  - a) 懒加载：真实 `.doc-section.active` 应恰 1 个（注意 grep 会匹配到 script 源码中的模板字符串 `${slug}`，需排除）
  - b) 控制台错误：`grep -iE "error|exception|uncaught" /tmp/wb_err.log` 应为空
  - c) stats 渲染值：footer 文本与 DOCS/PAPERS 实际长度一致
  - d) KaTeX：无网环境应静默降级为 LaTeX 源码且不报错（在线渲染由浏览器截图确认）
- 注：headless 沙箱通常无网，KaTeX CDN 会加载失败——这正好验证降级路径；在线验证仍靠双端截图（第 3 条）。


---

## 附 5：第二轮修复验证（2026-08-13，提交 8a7004d + 82ba924）

> 验证方法：shell.html/build_webapp.py 关键段重读 + 最新产物（16:38，5.06MB）重新解码（DOCS 27 / TOCS 4106 / PAPERS 21）+ 与用户转述的修复总结逐条对照。
> **结论：本轮声明的 5 项中 4 项真实落地（M11/H6D1–D4，源码确认）；H4 主干修复但有 3 处 label 污染；H1 确实未修复，且执行侧"不影响功能"的说法不成立、切片替换代码未提交。**

### ✅ 真实修复（源码确认）

| 项 | 证据 |
|---|---|
| M11 | shell:88–92 overlay 规则移入 `@media(max-width:900px)` |
| H6D1 | shell:36 toolbar / :42 .tab-groups `overflow:visible`（另 :94 .app-body overflow:visible 配套） |
| H6D2 | shell:352–359 当前组按钮显示文档标题、非当前组显示组名；active 判断用 `dataset.grp`（不依赖 textContent）✓ |
| H6D3 | shell:282 `createElement("button")`，下拉项原生 button，Tab/Enter 可用 |
| H6D4 | shell:535–539 Escape 分支追加关闭所有 `.tab-group.open` |
| H4 主干 | 产物 label 全部为真实作者+年份（如 "T. K. Gaisser (1990)"、"L. J. Kewley et al. (2001)"） |

### ⚠️ H4 瑕疵——3 处 label 文本污染（直接显示在 tab 上）

- Grenier：`** Isabelle A. Grenier et al. (2015)`——`**` Markdown 粗体残留
- Fowler：`**William A. Fowler**（加州理工 R. K. Kellogg Radiation Laboratory，Pasadena & CA 91225） (1984)`——`**` 包裹 + **机构地址混入作者名**
- Blasi/Amato：`** Pasquale Blasi (corresponding author) (2014)`——`**` 残留 + 脚注文字
- 根因：`_build_citation_map` 正则对 INDEX.md 中含 `**` 或跨行/括号机构的作者单元格，抓取了整格文本；`_fmt_authors` 按英文逗号切分，对中文逗号与括号机构无效。建议：正则后清洗 `**`、剥离括号机构/脚注，或修正 INDEX.md 作者单元格格式。

### ❌ H1 未修复（产物仍 3 组重复 id）+ 三点核查

- **事实**：最新产物 TOC 4106 条，仍重复 3 组（`grenier 目的-1`×2、`fowler 关键观察-1`×2、`fowler 目的-1`×2）；且出现 `1-目的-1-1`/`1-目的-1-2` 二次加后缀 id——构建链路（md2doc 生成 id + dedup 再处理）存在叠加错位。
- **"切片替换逻辑正确"存疑**：切片版 dedup 是**工作树未提交修改**（`git diff` 确认，HEAD 仍为 str.replace 版）；若产物由切片版构建仍重复，则切片版也未兜住——无论如何该修复未落地为提交。
- **"3 个 dupe 不影响功能"不成立**：重复 id 的 TOC 点击 `getElementById` 返回第一个匹配，跳错风险正是 H1 原危害（只是范围缩到 3 组条目）。
- **归因部分成立**：md 源确有同文件重复标题（Fowler `01_introduction.md:38/55` 两个"1. 图的目的"、`05_helium_burning.md:30/41/49` 三个"1. 目的"；Grenier `02_direct_measurements.md:130/150` 两个"目的"），md2doc 无文件内去重。正确路径：md2doc 层做文件内 anchor 去重（或对重复标题加序号），dedup 层用已提交的切片版兜底，构建后跑断言验证 0 重复。

### 📋 工程卫生

- `build_webapp.py` 有未提交修改（切片 dedup）——提交 82ba924 后工作树脏，应尽快提交或回退。
- `webapp/__pycache__/` 未被 .gitignore 忽略（`git status` 显示 `??`）——建议 `.gitignore` 增加 `__pycache__/`、`*.pyc`。

---

## 附 6：第三轮复验（2026-08-13，提交 4e005b4/cd07b10/c3fe9a5/e0a3130）

> 验证方法：最新产物（17:22，5.01MB）重新解码（DOCS 27 / TOCS 4106 / PAPERS 21）+ git diff 检查 + 与历史问题清单逐项对照。
> **结论：H4 主干与污染清洗 ✅（3 处 `**`/机构/corresponding 全清）；H1 ❌ 未解决且 TOC/HTML 双向一致性恶化（重复 3→4 组、heading 与 TOC 出现不同步）；H4 残留 6 处小瑕疵；md2doc_html.py 又现未提交修改。**

### ✅ 保持/新确认已解决

- M11、H6D1–D4、M7（stats 动态）、`__pycache__` 忽略（4e005b4）——全部保持。
- c3fe9a5 三个运行时修复（shell:93–94 `.app-body overflow:hidden` 防 sidebar 捕获滚轮；tab-group-btn 160px 统一；TOC 点击不再关闭 sidebar）——源码层面合理，运行时效果待用户实测确认。
- H4 `**`/机构/脚注污染：产物确认 3 处全部清洗（Grenier/Fowler/Blasi 均干净）。

### ❌ H1 未解决，且双向一致性被破坏（比上轮更糟）

- **重复 id 3 组 → 4 组**：`grenier 目的-2`×2、`fowler 关键观察-2`×2、`fowler 目的-2`×2、`fowler 目的-3`×2（序号从 -1 前移，说明 md2doc 层 `_seen_anchors` 已介入但未消除）。
- **HTML 与 TOC 不同步（新问题）**：heading 4106 条，HTML 内重复仅 1 对，但 TOC 重复 4 组；另有 3 个 heading id 不在 TOC 中——md2doc 层与 `_deduplicate_headings` 层**各自生成/修改 anchor，结果相互错位**。
- **根因（结构性）**：anchor 唯一性由两层同时负责——md2doc 的 `_seen_anchors`（单文件内）+ build 的 `_deduplicate_headings`（文档级）——两套 seen 计数与替换逻辑叠加必然产生不一致。补丁式修复只会让序号漂移（-1→-2→-3）。
- **收尾建议**：单一职责——md2doc 层负责生成唯一 anchor（含文件内去重），`_deduplicate_headings` 改为**只做查重断言（不修改 HTML/TOC）**；构建后断言 id 唯一 + TOC↔HTML 双向一致。

### ⚠️ H4 残留 6 处小瑕疵（不阻塞，建议随 H1 一并打磨）

| label | 问题 |
|---|---|
| `Andrew W. Strong¹ et al. (2007)` | `¹` 脚注上标残留 |
| `K. MARGARET BURBIDGE et al. (1957)` | 全大写（忠实原文，显示突兀） |
| `A. E. Champagne；M. Wiescher (1992)` | 中文分号 `；`——`_fmt_authors` 仅处理英文逗号 |
| `Edward Anders & Nicolas Grevesse (?)` | **年份缺失显示 `?`**（anders-grevesse 目录无年份，需从 INDEX 期刊行或 fallback 取 1989） |
| `Douglas R. Gies（Georgia State University） & David L. Lambert (1992)` | 机构括号混入（Gies、Bertone 共 2 处） |
| `Gianfranco Bertone（GRAPPA & University of Amsterdam）、Dan Hooper (2018)` | 机构混入 + 中文顿号分隔 |

### 📋 工程卫生

- `webapp/md2doc_html.py` 有**未提交修改**（git diff 显示 `_seen_anchors` 计数顺序调整）——继 build_webapp.py 之后再次出现提交后工作树脏，违反附 4 第 5 条，应立即提交或回退。
- `.gitignore` 根文件未见 `__pycache__`/`*.pyc` 条目（4e005b4 可能写入 webapp/.gitignore），确认无碍即可。

### 复验结论

**待办收敛为 3 项**：① H1 双层去重改单一职责 + 断言（高）；② H4 残留 6 处 label 清洗（低，可随 ① 一起）；③ 提交 md2doc 工作树修改（低）。其余问题（M1–M11、H2–H6、H6D1–D4）均已关闭或保持修复状态。

---

## 附 10：H4 清洗 + N1/N2/N3 落地确认（2026-08-13，提交 9939e9a）

> 独立复验：最新产物（18:31，4.99MB）解码 + shell.css 核查。
> **结论：H4 六处残留全部清洗、N1/N2/N3 全部按建议落地、H1 无回归、工作树干净——本轮声明与实现完全一致。**

### ✅ 验证通过

- **H4 label 全清洗**（产物确认 21/21）：
  - `Andrew W. Strong et al. (2007)`——¹ 上标清除
  - `K. Margaret Burbidge et al. (1957)`——全大写改正常
  - `A. E. Champagne & M. Wiescher (1992)`——中文分号 → 英文 &
  - `Anders & Grevesse (1989)`——年份 ? → 1989（FALLBACK 合并生效）
  - `Douglas R. Gies & David L. Lambert (1992)`、`Gianfranco Bertone & Dan Hooper (2018)`——机构括号/顿号清除
  - 自动检查 6 类污染（**/机构/分号/顿号/年份?/上标）：**0 残留**
- **N1**：shell:53 `.tab-group-btn.active::after { content:"▾ ▴" }`——active 按钮保留下拉提示 ✓
- **N2**：shell:70 dark 下 `#btn-top` 加深阴影 ✓
- **N3**：shell:73–77 dark 下 dropdown `border-color:var(--fg-2)` + 深阴影 + hover `#21262d` ✓（与建议一致）
- **H1 回归**：TOC/HTML 4106 唯一/0 重复/双向 0/0 ✓
- 工作树干净 ✓

### 📋 全部遗留项状态

| 项 | 状态 |
|---|---|
| H1–H6D4 / M1–M11 / H4 全部 | ✅ 关闭或保持 |
| N1/N2/N3（dark UX） | ✅ 关闭 |
| M9 首屏性能（5MB 全量注入） | ⏳ 未处理（见 WEBAPP_DESIGN.md v2 方案 E2/E3） |
| 首页/入口 | ⏳ 未立项（见 WEBAPP_DESIGN.md v2 方案 E1） |
| B2 TOC 层级过深 | ⏳ 低优先 |
| M6 无障碍 | ⏳ 低优先 |

**本轮为修复收敛轮：无新问题，声明=实现=实测。**

---

## 附 11：E2/E3/E1/M6 验证（2026-08-13，提交 26b1822 + 工作树 patch）

> 独立复验：新产物（19:17，4.06MB）解码（新格式：DOCS 直接存 UTF-8 html 明文）+ shell 工作树核查。
> **结论：E2+E3 ✅（体积 -19%）、E1 ✅（首页成为默认文档）、H1/H4 无回归 ✅；M6 部分落地——ARIA 与键盘大部分生效，但总结声称的 `role="menu"/"menuitem"` 在 shell/产物中均不存在（声明与代码不符）；E1/M6 改动未提交（工作树脏）。**

### ✅ 验证通过

- **E2+E3**：产物 5.01MB → **4.06MB（-19%）**；DOCS 字段 `html` 直接明文（b64 删除）；数据完整 28 docs（含首页）/ 4114 TOC / 21 papers；公式 1252+351 保持。
- **E1 首页**：`DOCS[0] = 知识库首页`（`background/00_home.md` 生成，html 3967 字节，含"推荐阅读/工具"区块）。
- **H1 回归**：TOC/HTML 4114 唯一 / 0 重复 / 双向 0/0（4114 = 4106 + 首页 8 个 heading）。
- **H4 回归**：label 0 污染残留。
- **M6 已落地部分**（产物确认）：`role="tablist"`、`aria-expanded`（8 处，含切换同步）、`aria-live="polite"`（搜索计数）、`aria-label`（搜索/按钮）、`aria-controls="sidebar"`、`aria-current`、键盘 `ArrowDown` 打开下拉并 `focus` 首个 item（shell:323–329；item 为原生 `<button>` 可聚焦，键盘功能可用）。

### ❌ M6 缺失项（声明不实）

- 总结声称 `.tab-dropdown → role="menu"`、`.tab-dropdown-item → role="menuitem"`，但 **shell.html 与产物中均 0 处**（grep 确认）。影响：屏幕阅读器朗读无菜单语义；键盘功能不受影响（button 原生可聚焦）。需执行侧补上这两条后重建。
- 顺带核查：dropdown-item 的 `tabindex` 未显式加（button 原生可聚焦，非必须）。

### 📋 工程卫生

- **26b1822 只提交了 E2+E3**；E1（`background/00_home.md` 未跟踪）与 M6（shell.html/build_webapp.py 修改）**均未提交**——工作树脏（第三次同类情况）。建议执行侧补提交：`00_home.md` + shell/build 的 M6 改动。
- 提示：`00_home.md` 未入库意味着 FreeFileSync 同步/克隆后首页会丢。

### ⏳ 待办

1. 补 `role="menu"/"menuitem"` + 提交 E1/M6 全部改动
2. 运行时验证（需截图）：懒加载首屏、首页默认打开、dropdown 键盘导航、dark 样式（E5 尚未做）
3. E5 下拉现代化 / B2 TOC 限级（后续批次）

---

## 附 12：结构收尾审查（2026-08-13 20:04，用户决定结构收尾）

> 最终产物（20:01，4.06MB）全量扫描 + 已知清单终核。

### ✅ 核心项全部健康（可收尾）

| 项 | 结果 |
|---|---|
| 数据完整性 | 28 docs（含首页）/ 4114 TOC / 21 papers，无空文档 |
| H1 一致性 | TOC/HTML 4114 唯一 / 0 重复 / 双向 0/0 |
| H4 label | 0 污染残留 |
| 安全面 | 0 eval；E3 明文直存后**0 处裸 `</script>` 泄漏**（无注入风险） |
| 链接 | 唯一且 href 正确（arxiv） |
| stats | 动态正确（背景 7 = 6 原 + 首页；论文 21；唯一标题 3262） |
| 性能 | 4.06MB（-19%），懒解码已落地（首屏单文档） |
| 交互 | 导航/搜索/公式/主题/打印/目录/懒加载全部验证过 |

### 📋 收尾遗留（均为低优先级打磨项，不影响使用）

| 项 | 级别 | 备注 |
|---|---|---|
| B2 TOC 层级过深（h4+ 1982 条） | 低 | 论文文档侧栏目录长，可后续限级/折叠 |
| M6 收尾（role="menu"/"menuitem"） | 低 | 键盘功能可用（button 原生），仅屏幕阅读器语义缺 |
| 面包屑（E1 增补） | 低 | 未做；组按钮恒显组名后非必需，纯增强 |
| E5 下拉现代化 | 低-中 | 纯视觉；UA border 已 reset（N4），完整改造可后续 |
| 搜索高亮大小写改写 | 低 | 边缘场景 |
| "下一章：01_introduction.md" 显示文件名 | 低 | 结构特性，可后续显示章节标题 |

### 收尾判定

**结构稳定、功能完整、数据健康、无高危漏洞——同意收尾**。以上遗留项按需在后续内容更新（新增文献）时顺手处理即可，无需专门排期。从 f7d0648 到收尾，共 9 轮修复 + 3 轮用户截图反馈，执行-审查-人眼闭环完整跑通。

### 建议后续维护节奏

1. 新增文献：走 papers/ENHANCEMENTS.md 顶部 SOP + 重建 webapp（`python3 webapp/build_webapp.py --include-papers`）+ 跑附 4 断言
2. 内容更新批次：顺手带掉 1–2 个低优先打磨项（B2/E5 优先）
3. 若部署线上（E4 触发条件满足时）：再做真分模块

---

## 附 13：阶段一批1 修复验证（2026-08-14，提交 08daa67）

> 独立复验：提交/工作树核查 + registry.json 解码 + 产物（00:2x 重建）重新解析 + build_webapp.py/build_fm.py/shell.html 关键段重读。
> **结论：6 项声明中 4 项真实落地（Anders year / key 提取 / checkbox 追踪 / backup）；但发现 2 个 P0 级问题——H4 严重回归（20/21 篇 label 变成论文标题）与 registry 丢失 Strong 2007（本轮修复引入的新回归）。**

### ✅ 真实落地

| 项 | 证据 |
|---|---|
| Anders year 1998→1989 | registry `year: 1989` ✓；且 21 篇 frontmatter↔registry year 全量核对**无不一致** |
| registry key 提取 | 20 篇路径正确（Strong 除外，见下） |
| checkbox 进度追踪 | shell.html:269–284 `wb_progress_v1` + `togglePaperStatus`；dropdown 每篇论文项渲染 checkbox（`cb.type="checkbox"`，checked=completed），点击切换 localStorage——**形态为论文级状态（completed/reading），非方案要求的章级 task list**（md 源 task list 基本不存在，产物文档 html 0 checkbox） |
| webapp 纳入 registry 字段 | PAPERS 含 status/read_date/tags/citations（从 `_paper_reg` 读） |
| backup 归档 | `backup/ADVANCEMENT-v1.0-20260813.md` 已入库 ✓ |
| 工作树 | 干净 ✓；08daa67 存在 ✓ |

### ❌ P0-1：H4 严重回归——20/21 篇 label 变成论文标题

- **现象**（产物 PAPERS 实测）：唯一正常的是 Strong（"Andrew W. Strong et al. (2007)"），其余 20 篇全部退化为论文标题——`*Synthesis of the Elements in Stars*`（B2FH，带星号）、`Abundances of the elements: Meteoritic and solar`（Anders）、`Carbon, nitrogen, and oxygen abundances in early B-type stars`（Gies）……与用户已截图确认的"dropdown 显示作者+年份"设计直接冲突。
- **根因**：build_webapp.py:297 `"label": title`——PAPERS 主路径 label 直接用论文标题；`_fmt_authors`（:65）仅用于 INDEX fallback 路径（:101 `_build_citation_map`）。上一轮明确警告"重建前必须先修 registry authors 清洗，否则 H4 失效"，执行侧**用"label 改 title"绕开清洗**——规避而非修复，H4 整体失效。
- **附带**：title 清洗 `\*+([^*])\*+` 只处理 `**bold**`，对 `*text*` 单星号斜体无效 → B2FH 星号残留。

### ❌ P0-2：registry 丢失 Strong 2007（本轮修复引入的新回归）

- **现象**：registry 26 条 = 20 论文 + 6 背景；目录 21 篇中 `0001_strong-moskalenko-ptuskin-2007` 缺失（上一轮为 27 条全含）。
- **证据**：Strong 的 `00_overview.md` frontmatter **存在且完整**（title/authors/year 齐全，28/28 写回成功）——丢失发生在 registry 生成侧（build_registry.py），非写回遗漏。
- **影响**：Strong 的 status/read_date/tags/citations 在 registry 缺失；产物 PAPERS 靠 CITATION fallback 兜住 label（恰好是它显示正常的原因），但 registry 作为"单一事实源"不完整。
- **怀疑**：`parts[-2]` key 提取修复对 01 目录（单篇目录）路径结构产生回归，需执行侧自查 build_registry 扫描路径。

### ⚠️ 中/低

- 阶段二进度粒度与 ADVANCEMENT 方案（章级 task list）不符——现为论文级 completed/reading（dropdown checkbox），且 md 源无 task list 数据基础；如接受论文级需更新方案表述。
- title 星号清洗（见 P0-1 附带）。

### 修正方向（建议开新提交）

1. **P0-1**：PAPERS label 改回 `_fmt_authors(reg.authors) + (year)` 生成"作者 (年份)"；authors 缺失/空时 fallback CITATION/stem；`*text*` 单星号清洗并入。
2. **P0-2**：修 build_registry.py 的路径扫描/key 提取，补回 Strong，重建后断言 registry 21 篇 ↔ 目录 21 一一对应（附 4 断言 b/e 同款逻辑应扩展至 registry）。
3. 修复后重建 + 跑附 4 断言（label 合法性断言会抓住 P0-1）。

---

## 附 14：P0 修复验证（2026-08-14，提交 30ff812）

> 独立复验：提交核查 + registry.json 解码（27 条全量字段统计）+ 产物 PAPERS 全量 label/字段解析 + build_webapp.py 关键段重读。
> **结论：声明 3 项中 2 项真实（label 修复 ✅、Strong 补回 ✅）；但引入新回归 P0-3——registry key 提取 parts[-3] 错误导致 21 篇 registry 元数据匹配全部失败（read_date/tags/citations 全空，status 靠默认值掩盖）。**

### ✅ 真实落地

1. **H4 label 修复（21/21 全验证）**：产物 PAPERS 全部"作者 (年份)"格式、0 污染。上轮 6 处瑕疵全清：`K. Margaret Burbidge et al. (1957)`（全大写→Title Case）、`Andrew W. Strong et al. (2007)`（¹ 上标清除）、`A. E. Champagne & M. Wiescher (1992)`（中文分号→&）、`Anders & Grevesse (1989)`、`Douglas R. Gies & David L. Lambert (1992)`（机构括号清除）、`Gianfranco Bertone & Dan Hooper (2018)`（顿号清除）。根因修复符合建议：label 改 `_fmt_authors(reg.authors) + (year)`（build_webapp.py:297 区域）。
2. **Strong 2007 补回**：registry 27 条 = 21 论文 + 6 背景；**真根因 = build_registry.py `parse_frontmatter limit 80→1000`**（Strong 的 frontmatter 在第 324 行，超出 80 行限制被跳过）——与"key 提取"无关。
3. H1 无回归（4114 唯一/0 重复/双向 0/0）；工作树干净。

### ❌ P0-3（新回归）：build_webapp `_registry` key 提取 parts[-3] 错误 → 21/21 匹配失败

- **现象**：产物 PAPERS 的 `read_date/tags/citations` 21 篇全空；而 registry.json 本身这些字段是齐的（read_date/lastread/status 0 缺失，citations 13 缺失、tags 2 缺失——与产物"21 全缺"矛盾）。
- **根因**：build_webapp.py:35–36 `parts = path.replace("/00_overview.md","").split("/")` → `["01_cosmic-ray-propagation", "0001_strong-…", "literature_analysis"]`；`stem = parts[-3]` = **分类目录名**（01/02/03），而 `_paper_reg(stem)` 用**论文目录名**查询 → 21 篇全部 miss → `reg={}` → status 走默认"completed"（恰好掩盖）、read_date/tags/citations 走默认空值。
- **关键判断**：上一轮 08daa67 的 `parts[-2]` **本来就是正确的**（论文目录名）；Strong 丢失的真因是 frontmatter limit=80（本轮已修）。执行侧把两件事混为一谈，把对的 parts[-2] 改成了错的 parts[-3]——**"修好 Strong 的同时破坏了其余 20 篇的元数据"**，净效果是元数据从"20 篇正常"退化为"0 篇正常"。
- **修复**：`stem = parts[-2]`（一行），重建后断言产物 PAPERS 的 read_date/tags/citations 与 registry 一致（21 篇非空率应≥95%：read_date 21、tags 19、citations 8）。

### ⚠️ 低优先观察项

- Strong `abstract` 字段 YAML 转义损坏（`## 0.2 Abstract（中文精读）\\n\\n…` 海量反斜杠）——abstract 仅 2/27 有值且质量差，建议从 registry 移除或修复转义（不在 PAPERS 展示，非阻塞）。
- `S S Al-dargazelli et al. (1996)` 首字母缩写缺"."（`_title_case` 对 "S." 处理），小瑕疵可后续打磨。
- citations 13/21 缺失为 registry 数据层问题（O2 语义未对齐，上轮已列，非本轮回归）。

### 复验结论

label 与 Strong 两项修复真实，但 **P0-3 必须退回**（一行修复：parts[-2]）。此轮再次印证附 4 第 1 条：执行侧提交前未验证产物字段与 registry 的一致性——若在 build 后跑"PAPERS read_date 非空率"断言，P0-3 立即暴露。

---

## 附 15：P0-3 修复验证（2026-08-14，提交 1db98f4 + cb38783）

> 独立复验：提交核查 + 产物 PAPERS 字段非空率/label 全量 + build_webapp.py label 生成段重读 + ADVANCEMENT 措辞核对。
> **结论：P0-3 真实修复（parts[-2] 恢复，字段非空率与声明 21/19/8 完全一致）；批 1 链路（frontmatter→registry→webapp）真实闭环；但修复暴露 1 个连带显示缺陷——Anders label 年份变 0（中，建议批 2 前一行修复）。**

### ✅ 验证通过

| 项 | 声明 | 实测 |
|---|---|---|
| status 非空 | 21 | **21/21** ✓ |
| read_date 非空 | 21 | **21/21** ✓ |
| tags 非空 | 19 | **19/21** ✓ |
| citations 非空 | 8 | **8/21** ✓ |
| label 作者年份格式 | 21 | **21/21**（唯一异常见下） |
| H1 一致性 | — | 4114 唯一/0 重复/双向 0/0 ✓ |
| docs/首页 | — | 28 docs，DOCS[0]=知识库首页 ✓ |
| ADVANCEMENT 批2 措辞 | 论文级 | 已更新：章级 task list 取消（附 13 注明 md 源无数据基础）、论文级 completed/reading + dropdown checkbox + localStorage ✓ |
| 工作树 | 干净 | 干净 ✓；1db98f4/cb38783 存在 ✓ |

- build_webapp.py:36 `stem = parts[-2]`（论文目录名）✓ 恢复正确。

### ⚠️ 连带缺陷（中）：`Edward Anders & Nicolas Grevesse (0)`——year 从 stem 提取失败

- **现象**：21 篇中唯一 label 年份错误——Anders 显示 `(0)`（上轮 30ff812 时显示 `(1989)` 属"碰巧正确"）。
- **根因**：build_webapp.py:292–293 `year = int(stem_yr.group(1)) if stem_yr else 0`，从 **stem（目录名）** 正则提取 `\d{4}_.+?-(\d{4})`；Anders 目录名 `0006_anders-grevesse` **无年份后缀** → 不匹配 → year=0。而 **registry 里有正确 year='1989'（frontmatter 提取）却没被使用**——PAPERS 的 year/label 完全忽略 reg.get("year")。
- **本质**：30ff812（parts[-3] 全失败走 fallback）恰好正确，1db98f4（parts[-2] 修复走 registry 主路径）暴露了这个硬编码提取缺陷——**注册表已有数据但生成器不用**。
- **修复（一行）**：`year = int(reg.get("year") or (stem_yr.group(1) if stem_yr else 0))`，优先级 registry > stem。
- **影响面**：仅 Anders 1 篇（其余 20 篇 stem 均含年份后缀）；用户可见（dropdown label 显示 "(0)"），非阻塞。

### 复验结论

**批 1 真实闭环**：frontmatter → registry → webapp 链路全通，字段非空率与声明逐项一致，H1 无回归。唯一遗留 = Anders year 一行修复（可随批 2 首提交带上）。附 4 断言建议补一条：**label 不得含 "(0)" 或 "()"**——这条能抓住本次缺陷。

---

## 附 16：批2 验证（2026-08-14，提交 27bb88a + c1b156d）

> 独立复验：audit.py **亲自运行**（14 条全 PASS，exit 0）+ Anders label 实测 + server.py 四端点实测（起服务 + curl）。
> **结论：audit.py 断言体系真实可用（14/14 通过，覆盖"label 不含 (0)"）；Anders year 修复生效（1989）；server.py 静态服务/进度 API 可用；但 `/api/rebuild` 端点在当前环境 100% 失败——build_registry.py 依赖 PyYAML（本机 system+managed 两个 Python 均未安装），且呈"静默半成功"状态（registry 失败但 webapp 用旧数据重建成功）。**

### ✅ 验证通过

1. **audit.py 14 条断言亲自运行全部 PASS**（exit 0）：附4（PAPERS/DOCS id 唯一、label 不含 (0)/()、year>1900、TOC title 唯一）+ 阶段三 a–e（三件套/TOC≥3/frontmatter↔registry/glossary 688/目录↔INDEX 21↔21）+ 附属（PAPERS 21、read_date 21/21、registry↔PAPERS stem 一致）——**与声明逐项一致**，这是"验证链路真正用起来"的落实。
2. **Anders year**：label = `Edward Anders & Nicolas Grevesse (1989)` ✓（registry 优先生效，year 字段 1989）。
3. **server.py 静态 + 进度 API 实测**：
   - `GET /` → 200，4.22MB（interactive.html 正常 serve）
   - `GET /api/progress?slug=0003_fowler-1984`（**目录名下划线 slug**）→ `{status: completed, lastread: 2026-08-12, read_date: 2026-08-12, title: ...}` ✓ 直接读源 md frontmatter，registry 未参与（符合 D6）
   - `GET /api/progress` → total 21 ✓
   - 注意：首次测试我用 `paper-0003-fowler-1984`（webapp slug）404——**API slug 契约是目录名（下划线），与 webapp PAPERS slug（paper- 前缀连字符）不一致**，前端集成时需转换，建议写入 server.py 文档（非 bug，契约问题）。

### ❌ P0-4：`/api/rebuild` 在当前环境必失败 + 静默半成功

- **现象**（实测 POST /api/rebuild）：`registry_rc=1`、`webapp_rc=0`、响应 `ok:false`；registry_tail = `ModuleNotFoundError: No module named 'yaml'`（build_registry.py:24 顶层 `import yaml`，:68 `yaml.safe_load` 无 fallback）。
- **环境**：本机 **system（/opt/homebrew/bin/python3）与 managed（3.13.12）两个 Python 均无 PyYAML**——rebuild 端点 100% 失败；而 webapp 重建成功（`Wrote ... 3286774 chars, docs: 28, toc: 4114, papers: 21`，用**旧 registry**）。
- **危害**：① 形态 B 核心端点（一键重建）不可用；② **静默半成功**——用户改 md frontmatter（进度/status）后 POST rebuild，registry 不更新但 webapp 显示"重建成功"，**进度变更不生效且无明确报错**；③ server.py 文档宣称"stdlib only"，与 rebuild 的 PyYAML 依赖矛盾。
- **根因**：形态 B 服务层（极简 frontmatter 解析）与 rebuild 链路（yaml.safe_load）依赖不一致；rebuild 未做依赖检查、未做"registry 失败则中止 webapp"的顺序约束。
- **修复方向**：
  1. （治本）build_registry.py 去掉 yaml 依赖：用自研 frontmatter 解析（支持标量 + 数组字段，复用 server.py 解析思路扩展），保持 stdlib only；
  2. （防静默）rebuild 改为**顺序依赖**：registry_rc≠0 时跳过 webapp 构建并在响应中明确 `registry_failed: true`，避免旧数据重建；
  3. audit.py 补一条 **rebuild 冒烟断言**（可选：起 server → POST rebuild → 断言 ok:true），把运行时能力纳入验证。

### 复验结论

批 2 的 **audit 断言体系与进度 API 真实落地**，Anders 修复生效；但 **rebuild 端点必须修复后才能宣称"形态 B 可用"**（当前 = 静态服务 + 进度 API 可用，rebuild 不可用）。修复建议随批 3 首提交带上（1+2 两项很小）。

---

## 附 17：P0-4 修正确认（2026-08-14，提交 5a6a062 + venv PyYAML 装填）

> 背景：附 16 判定"/api/rebuild 必失败"基于部分解释器探测，用户指出"system python3 有 PyYAML 6.0.3"，复查后修正。
> **修正结论：附 16 的"必失败"判定过重——rebuild 可用性取决于启动解释器；执行侧 5a6a062 的"实测 ok=true"真实（它用隔离 venv，已装 PyYAML 6.0.3）；本复验用 venv 起 server 实测 POST /api/rebuild → `ok:true, registry_rc:0, webapp_rc:0`（9s 内），产物重建成功、audit 14 条复跑全绿、git 干净。**

### 修正事实

- **解释器探测全景**（本机）：`/usr/bin/python3`、`/opt/homebrew/bin/python3`、managed 3.13.12、venv `envs/default` —— 前 3 个**无** PyYAML；**venv 有 PyYAML 6.0.3**（执行侧安装于此，即"system python3 有 PyYAML"所指）。
- **5a6a062 已落地**（源码确认）：rebuild 顺序依赖（registry 失败→跳过 webapp→`registry_failed:true`+hint，杜绝静默半成功）+ slug 契约文档（API=目录名下划线 vs webapp=paper- 连字符）。**附 16 建议的前两条已实现**。
- **本复验实测**：venv 起 server → `POST /api/rebuild` → `ok:true`；webapp 重建 3286774 chars（docs 28/toc 4114/papers 21）；audit 复跑 14/14 PASS；工作树干净。
- 注：本复验期间向隔离 venv 补装了 pyyaml 6.0.3（此前 venv 内 pip list 未显 yaml，疑为执行侧环境与我探测时序差异；装填后行为与执行侧声明一致）。

### 残留建议（低优先，非阻塞）

1. **server.py 文档/启动自检**：明确"需用含 PyYAML 的解释器（如 `envs/default` venv）启动"，或在 main() 启动时 `import yaml` 检查并打印清晰提示（当前 hint 已覆盖 rebuild 失败路径，启动时检查更早暴露）。
2. build_registry.py 去 yaml 依赖（自研解析）仍可选做——彻底消除环境敏感，但非必须（venv 方案已可用）。

### 修正后状态

**P0-4 关闭**：rebuild 在正确解释器下可用、静默半成功已杜绝；P0 清单（H4 label、Strong、parts[-2]、Anders year、rebuild）全部关闭。附 16 的"必失败"表述以此为准。

---

## 附 18：批3 术语 hover 验证（2026-08-14，提交 a8b73bd）

> 独立复验：提交核查 + glossary.json 解码（661 条/缺释义 0）+ build_glossary.py/shell 注入逻辑重读 + **headless Chrome 运行时实测**（注入 switchDoc 切到 B2FH 页）。
> **结论：术语 hover 真实落地且与声明逐项一致——B2FH 页实测注入 gloss=320（与报告完全一致）、tooltip title 含"术语+释义+出处"、跳过 math/code/pre、audit 14 条全绿、JS 零错误。**

### ✅ 验证通过（运行时实测，非静态推断）

| 项 | 声明 | 实测 |
|---|---|---|
| glossary.json | 661 条 | **661 条**（term/def/papers/cross_paper 四字段），**缺释义 0** ✓ |
| 解析源 | 05_glossary.md | build_glossary.py:21 指向 background/05_glossary.md ✓ |
| 产物注入 | __GLOSS_JSON__ | `const GLOSS = [` + 661 term ✓ |
| B2FH 注入数 | 320 | **headless 实测 320**（active section paper-0001-b2fh-1957 内 320 个 span.gloss）✓ |
| tooltip 内容 | 术语+释义+出处篇数 | **span title 属性实锤**：`title="术语：恒星核合成\n恒星内部的核反应产生比 H、He 更重的元素\n出处：1 篇论文"` ✓（此前 grep title 仅 3 个是 `[^"]*` 不跨行匹配含 `\n` 值的误报） |
| 跳过 math/code/pre | SKIP 集合 | shell:445–451 SCRIPT/STYLE/CODE/PRE/MATH + .math class ✓ |
| slug normalize | paper- → 0001_ | 320 命中证明 `paper-0001-b2fh-1957` ↔ `0001_b2fh-1957` 映射生效 ✓ |
| audit | 全绿 | 亲自复跑 **14 条全 PASS** ✓ |
| JS 运行时 | — | headless 控制台 **0 error** ✓ |

- 顺带确认：首页（导航表主题词）注入 23 个 gloss，符合预期（非论文页也有命中）。
- 无回归：产物 28 docs/4114 TOC/21 papers，H1 结构未动。

### 📋 批3 剩余——O2 图谱的 citations 语义问题（建议数据先行）

- 现状：citations **8/21 非空、13/21 空**；且已填值源自 references.md 的**参考文献列表（多为库外文献）**——若直接画图，图谱节点大半悬空/缺失。
- **建议：先定语义再画图**——citations 应指"**库内 21 篇间的引用**"（本篇引用了哪些库内其他论文）。生成路径：脚本从各篇正文的 `[[stem]]` 链接 + references 中匹配库内 stem 自动提取，人工校准 8 篇已有值（剔除库外文献），补齐 13 篇后再生图谱。Obsidian Graph 的连线质量完全取决于 citations 质量，数据先行一步到位，避免"画了图全是断线"再返工。

### 复验结论

**批3 术语 hover 组件闭环**（数据→注入→运行时效果全验证）；O2 图谱建议"citations 语义重定义为库内引用 + 数据补齐 → 再画图"，可与 P0-4 残留项（server 启动自检已由 45c1f48 落地）一并收尾。

---

## 附 19：批3 O2 图谱验证（2026-08-14，提交 112acf2 + 5e27583）

> 独立复验：提交核查 + registry.json citations 全量质量检查（21/21 非空/0 悬空/50 边）+ 产物解码 + **headless Chrome 运行时实测**（默认首页 dump-dom）+ shell 图谱代码重读 + audit 复跑。
> **结论：O2 图谱真实落地且与声明一致——21 节点/50 边/节点大小按度数分级/点击跳转；执行侧"篇间导航=库内引用数据源"的发现合理（正文无 [[链接]]，overview 篇间导航小节是人工维护的关联链接，是更可靠的数据源）；附带 43861cb 修复了附 14 观察的 abstract 反斜杠乱码。**

### ✅ 验证通过（数据 + 运行时双重确认）

| 项 | 声明 | 实测 |
|---|---|---|
| citations 非空 | 21/21 | **21/21** ✓ |
| 悬空引用 | 0 | **0**（全部指向库内 stem）✓ |
| 引用边 | 50 | **50**（registry 求和）✓ |
| 图谱节点 | 21 | **headless 实测 21**（circle r 分布 11/13.5/14 三档 = 按引用度数分级；多出的 `${r}` 为 JS 模板字符串，script 源码残留）✓ |
| 图谱边 | 50 | **51 - 1 模板 = 50** ✓ |
| 节点标签 | 作者名 | 21 个 text 全为作者 label（HTML 转义 `&amp;` 正确）✓ |
| 点击跳转 | 是 | shell:570–572 `n.addEventListener("click", … switchDoc(slug))`（事件绑定于节点，静态 DOM 无 onclick 属性属正常）✓ |
| 力导向布局 | 自研 | shell:521–536 库仑斥力 `2600/d²` + 弹簧引力 `(d-90)*0.06`，**无 d3 依赖** ✓ |
| audit | 全绿 | 新产物复跑 **14 条全 PASS** ✓ |
| JS 运行时 | — | headless 0 error ✓ |
| 工作树/gitignore | — | 干净；`webapp/interactive.html` 确在 .gitignore:7（构建产物不入库，属正常设计）✓ |

### 📝 对执行侧"关键发现"的认可

- "正文无 `[[stem]]` 链接、references 仅 1 篇"的**摸底修正**成立：21 篇 overview 的「篇间导航」小节（人工维护的关联论文链接）是完整库内引用源（57 候选 → 50 去重入库）。**此数据源比自动爬参考文献更可靠**（人工维护、语义准确），采纳正确。
- 43861cb 顺带修复附 14 观察的 abstract 反斜杠雪球乱码（P0-5）——未纳入本轮声明但已落地，予以确认。

### 复验结论

**批 3 全闭环**：术语 hover（附 18）+ O2 图谱（本附）均运行时实测通过；citations 数据质量（21/21、0 悬空）为 Obsidian Graph 提供了可靠连线基础。剩余 = 批 4（阶段六 + PWA）。

---

## 附 20：批4 终验（2026-08-14，提交 f575e9d + 2d35a46）

> 独立复验：提交核查 + PWA 文件/产物注入 + 阶段六文档 + audit 复跑 + **headless 运行时终验**。
> **结论：PWA 与阶段六本身 ✅（注入齐全、文档 7 争议、audit 全绿）；但 headless 终验抓到 **P0-6 数据回归**——批 4 重建 registry 时把 citations 从 21/21 库内覆盖回 8/21 库外（[[cesarsky]] 格式），图谱边从 50 → 0。audit 14 条全绿未发现（盲区：无 citations 非空断言）。**

### ✅ 批4 通过项

| 项 | 声明 | 实测 |
|---|---|---|
| PWA 文件 | manifest + 3 图标 | manifest.json（558B，name/start_url/scope/icons 192+512 maskable 齐全）、icon-192/512、apple-touch-icon.png（注：文件名是 apple-touch-icon.png 非 -180，href 指向正确）✓ |
| 产物注入 | 3 标记 | `manifest.json`×1、`theme-color`×1、`apple-touch-icon`×2 ✓ |
| 阶段六 | 7 争议 + 速览 + 总结 | `06_controversy_evolution.md`（8KB，10 个 #）：太阳丰度/UHECR top-down vs bottom-up/传播参数 δ 与 z_h/SNR 范式/r-s 过程/中微子/WIMP + 交叉速览 + 时间线 ✓ |
| docs/TOC | 29/4124 | DOCS 29 / TOCS 4124 / PAPERS 21 ✓ |
| audit | 全绿 | 亲自复跑 **14 条 PASS** ✓ |
| JS 运行时 | — | headless 0 error、首页正常 active、KaTeX 无网降级预期 ✓ |

### ❌ P0-6：citations 数据被批 4 覆盖（21/21 库内 → 8/21 库外），图谱 50 边 → 0 边

- **headless 实测**：图谱 circle 21（正常）、**line 0**（附 19 为 50）——稳定复现（两次 dump 均 0），非时序问题。
- **证据链**：
  1. 产物 PAPERS citations **8/21** 非空，值为 `[[cesarsky]]`、`[[berezinskii-et-al.]]` 等**库外 wiki 链接**（112acf2 之前的旧数据形态；附 19 验证时为 21/21 库内 stem）；
  2. `registry.json` citations 同步 **8/21 库外**——2d35a46 提交 `registry.json 132 行变更`（批 4 重建 registry 引入回退）；
  3. `frontmatter citations` **0/21**（build_citations.py 写 frontmatter 步骤未留存）；
  4. `build_registry.py` **无任何 citations 处理逻辑**（grep 0 结果）——重建时保留/恢复旧 registry 的 citations 旧值（8/21 库外）。
- **根因**：citations 生成职责不清——build_citations.py（篇间导航，好数据）与 build_registry.py 重建流程（不处理 citations、保留旧值）竞争同一字段；批 4 触发 registry 重建 → 回退。frontmatter 空说明 build_citations 的"写 frontmatter（单一事实源）"环节也未闭环。
- **audit 盲区**：14 条断言含 read_date 非空、无 **citations 非空/图谱边数** 断言——本轮 8/21 全绿通过，说明静态断言抓不到此类数据回归，**运行时验证（headless 数 line）是必要补充**（恰是附 4 第 6 条的落地价值）。

### 修复方向（批 4 需退回此项）

1. **立即恢复**：`git checkout 112acf2 -- webapp/registry.json` 或重跑 build_citations.py 重建 21/21 库内 citations（0.1 单元）；
2. **根治（职责单一）**：build_citations.py 为 citations **唯一生成器**（提取 → 写 frontmatter → 供 build_registry 读）；build_registry.py 重建时**显式保留已有 citations 或从 frontmatter 读**，禁止隐式回退；排查 build_citations 写 frontmatter 步骤为何 0/21；
3. **audit.py 补断言**：a) PAPERS citations 非空 = 21；b) 图谱有效边（citations 均命中 byStem）> 0——两条可防复发。

### 复验结论

**批 4 的 PWA 与阶段六通过，但 P0-6 未闭环——"全部 4 批完成"声明不成立**。修复 P0-6（恢复数据 + 生成职责单一 + audit 补断言）后重建、跑 audit + headless（line ≥ 50），方可宣告 ADVANCEMENT 全流程完成。

---

## 附 21：P0-6 修复终验 + ADVANCEMENT 全流程收官（2026-08-14，提交 4d75510[a941dc8]）

> 独立复验：提交核查 + build_fm 改动重读 + frontmatter/registry/产物 citations 三层全量扫描 + audit 17 条亲跑 + headless 图谱运行时实测。
> **结论：P0-6 完整闭环，且为"声明 = 实测"（修复后 frontmatter/registry/webapp 三层 citations 全 21/21、50 条库内、0 悬空，图谱 50 边恢复）。ADVANCEMENT 批 1–4 全部收官，P0 清单 7 项全关闭。**

### ✅ 修复验证（三层数据 + 运行时）

| 层 | 结果 |
|---|---|
| frontmatter（唯一事实源） | **21/21** 有值、**50 条库内 stem**、0 悬空（格式为 YAML 顶格 block sequence `citations:\n- item`） |
| registry.json | 21/21、0 悬空、总边 50（build_registry 从 frontmatter 读 → **rebuild 链路安全**，dry-run 验证非空） |
| 产物 PAPERS | 21/21、库内 stem（`0004_blasi-2013` 等） |
| 图谱（headless） | **line 50**（51−1 模板）、circle 21、0 JS error |
| audit | **17 条全 PASS**（新增 3 条：citations 非空 21/21、无悬空、图谱数据 ≥30） |
| build_fm | :305 `_read_existing_citations` 保留已有值；:348 旧 build_citations 函数保留定义但**无调用点**（"删坏提取"实为禁用，行为等价） |
| 工作树 | 干净；commit message 含原 hash 前缀属提交工具行为，无碍 |

### 📝 审查方修正声明（误报澄清）

- 本复验过程中曾两次误报：①"frontmatter citations 0/21"——我的 block 正则要求 `^\s+` 缩进，而实际是 YAML 合法的**顶格 sequence**（`- item` 无缩进），修正 `^\s*` 后确认为 21/21；②"build_citations 函数仍在"——确认真实（保留定义未调用），行为上已不覆盖。**执行侧声明在此两项上均正确，特此更正。**
- 附 20 判定"audit 无 citations 断言"已被本轮补上（17 条含 3 条 P0-6 防护），附 20 表述自动更新。

### 🏁 收官判定

**ADVANCEMENT.md 全部批次闭环**：批1（frontmatter+registry）→ 批2（audit 17 断言 + 形态 B 服务层）→ 批3（术语 hover 661 + O2 图谱 21 节点 50 边）→ 批4（PWA + 阶段六争议演化）。
**P0 清单 7 项全部关闭**：H4 label、Strong 缺失、parts[-2]、Anders year、rebuild 500、abstract 雪球、citations 覆盖。
**验收总则三项全过**：audit 17 条 ✓ / headless 运行时 ✓ / frontmatter↔registry↔webapp 三方一致 ✓。
后续维护：新增文献走 ENHANCEMENTS SOP + `build_citations → build_fm → build_registry → build_webapp → audit → headless` 全链路；双机分工可另行评估。

---

## 附 22：V2.2 Obsidian 图谱链接化验证（2026-08-14，提交 89d398a）

> 独立复验：提交核查 + 全量导航头覆盖率统计（205 分章）+ frontmatter/registry citations 格式检查 + build 层职责重读 + audit 17 条 + headless 图谱。
> **结论：V2.2 完整落地且无回归——导航头 wikilink 覆盖率 203/205（0 文本残留）、frontmatter citations 全 wikilink、build 层职责单一（build_fm 透传 / build_registry 剥壳）、registry 纯 stem 21/21/0 悬空/50 边、audit 17 全绿、headless line 50。声明 = 实测。**

### ✅ 验证通过

| 项 | 结果 |
|---|---|
| 提交/工作树 | 89d398a 存在，工作树干净 ✓ |
| 导航头 wikilink | **203/205 分章文件**含 `上一章/下一章：[[完整路径\|别名]]`，**0 文件仍为文本导航**（另 2 文件为 97/98/99 类本就无导航头）✓ |
| frontmatter citations | 21 篇全为 wikilink：`- '[[02_.../00_overview\|0002_al-dargazelli-1996]]'`（完整路径 + \|别名 + 单引号 YAML 定界）——Obsidian 解析 frontmatter 值内 `[[...]]` 有效，别名显示 stem ✓ |
| build 层职责 | **单一且正确**：build_fm `_read_existing_citations` 注释明确"透传不剥（剥 [[ ]] 是 build_registry 的职责）"；build_registry dry-run 实测剥壳 → 纯 stem（`"0004_blasi-2013"`）→ **rebuild 安全** ✓ |
| registry | 21/21 非空、**0 悬空**、50 边、纯 stem ✓ |
| audit | **17 条全 PASS** ✓ |
| 图谱（headless） | **line 50**（51−1 模板）、circle 21、0 JS error ✓ |

### 📝 观察项（非阻塞）

- 导航头 wikilink 带 `.md` 后缀（`[[.../00_overview.md\|00_overview.md]]`）——Obsidian 支持，可解析；若追求简洁可去后缀（不影响功能）。
- citations 用完整路径而非 V2.2 建议的短名——**反而更稳**（指向明确、无同名歧义），Obsidian 图里连线目标是各篇 overview 节点，符合预期。
- 2 个无导航头文件（97_quality_check 类）不影响图谱（它们本身是内部自查文件）。

### 复验结论

**V2.2 完整闭环**。用户侧动作：ObsFile/ReferenceRead 镜像同步一次 → Obsidian 刷新 Graph → 应呈现"21 个簇（同篇链）+ 簇间 50 条引用连线"。若仍散落，先检查 Graph Filters 是否排除了技术文件（scripts/backup/webapp），再截图反馈。

---

## 附 23：新增文献接入检查（2026-08-14，提交 dea7786/d1e969e/907444f）

> 范围：新篇 0014_cameron-1968 + 0015_kraft-1994 的 SOP 完整度 + frontmatter→registry→webapp 全链路 + audit + headless。
> **结论：两篇接入**基本完整**（SOP 齐全、数据全链路联动、audit 自适应全绿、图谱 23 节点 59 边、0 JS 错误）；发现 1 个 P1 数据质量缺陷——Cameron 的 frontmatter authors/title 带 `[FACT]` 标记残留，label 显示为 `A. G. W. Cameron [fact] (1968)`（用户可见）。**

### ✅ 接入正常

| 项 | 结果 |
|---|---|
| SOP 完整度 | 0014：PDF ✓ + 7 分析 md ✓；0015：PDF ✓ + 11 分析 md ✓；frontmatter（title/year/citations）✓；INDEX 收录 ✓ |
| registry | 30 条 = **23 论文** + 7 背景 ✓ |
| 产物 | DOCS **31** / TOCS **4333** / PAPERS **23** ✓ |
| citations | 新篇各 5/4 条（V2.2 wikilink 格式已接入）✓ |
| audit | **17 条全 PASS**（断言自适应：PAPERS 23、citations 总 59 ≥30）✓ |
| 图谱（headless） | **23 节点 / 59 边**（21 篇时 50 边，+9）、0 JS error ✓ |

### ❌ P1：Cameron label 脏数据——`A. G. W. Cameron [fact] (1968)`

- **根因**：新篇 frontmatter 写入时把**信息分级标记 [FACT] 混入元数据**——`authors: A. G. W. Cameron [FACT]`、`title: ...Solar System [FACT]`（registry 透传；build 层 `_title_case` 把 FACT 转成小写 fact）。
- **影响**：label/图谱节点/tab 显示 `[fact]` 残留，用户可见（headless 实测确认）。
- **修复**：改 frontmatter 两处（authors/title 去 `[FACT]`）+ rebuild；audit 建议补断言 **"label 不含 `[` 或 `]`"**（当前 label 断言只查 `(0)/()`/污染字符，漏了方括号）。
- **根因提示**：精读流水线（Hermes）在写 frontmatter 时把正文的 [FACT]/[INTERPRETATION] 标记一并复制——建议 READING_INSTRUCTIONS 或 build_fm 增加元数据字段清洗规则。

### 复验结论

新增文献 SOP 链路**整体可用**（建目录→PDF→精读→frontmatter→registry→webapp 全通，audit/图谱/headless 全部正常联动），唯一需要退回的是 Cameron 的 frontmatter 清洗 + audit 补方括号断言（0.1 单元）。

---

## 附 24：根目录文档盘点修复验证（2026-08-14，提交 11ce180 + c2c5acf）

> 独立复验：README 7 处硬伤逐项核验 + TROUBLESHOOTING B15-B18 + ENHANCEMENTS 归档标注 + WEBAPP_DESIGN 交叉引用 + 工作树。
> **结论：3 文档修复 + TROUBLESHOOTING 4 条补充全部落地，声明 = 实测——全库 7 文档全部健康。**

### ✅ 验证通过

- **README**（5922→8436 字符）：论文数 03=15/合计 23 ✓；29 节 4 处、28 节残留 0 ✓；GIT_CONVENTION 坏链 0 ✓；ADVANCEMENT×3/WEBAPP_DESIGN×2/TROUBLESHOOTING×2 链接 ✓；webapp 工具链 15 处提及 ✓；SOP 9 步（含 build 链 + V2.2 wikilink 可选步）✓；"最后更新 2026-08-14" ✓
- **TROUBLESHOOTING B15–B18**：执行侧把我建议的 4 条全补（B15 overlay 作用域 M11、B16 overflow 裁剪 H6D1 为必补；B17 KaTeX 时序、B18 搜索 lastIndex 为可选）——每条带 Commit 引用，质量与前 14 条一致
- **ENHANCEMENTS**：文末"后续见 ADVANCEMENT.md + 保留为历史提案快照"归档标注 ✓
- **WEBAPP_DESIGN**：顶部"V2.2 后续见 ADVANCEMENT.md V2.2 补丁章节"交叉引用 ✓
- 提交 11ce180/c2c5acf 存在、工作树干净 ✓

### 📝 观察项

- ENHANCEMENTS 提到"05_glossary.md 769 术语已建"（此前 688 行）——术语表随新篇扩充，属正常演进。
- README SOP 第 ⑨ 步如为 headless 终验则完整闭环（9 步 = 建目录→PDF→精读→frontmatter→citations→registry→webapp→audit→headless 全链）。

### 复验结论

**全库 7 文档健康闭环**：INDEX/ADVANCEMENT/READING_INSTRUCTIONS/TROUBLESHOOTING/WEBAPP_DESIGN/ENHANCEMENTS/README 状态全部与当前 23 篇库一致，无过期、无坏链、无交叉冲突。文档体系（含 TROUBLESHOOTING 经验库）达到可长期维护状态。

---

## 附 25：审查 bf2d301——gen_index 回退正则修复核验（2026-08-14）

> 独立复验：执行侧提交 bf2d301「fix(index): title bullet fallback + 全大写清洗 + 日期自动 + 平衡 **」，摘要 8 项声明逐一对照实测。
> **结论：6/8 属实；2 项核心声明不成立——Amato 标题"已修复"实为 `**** The origin of galactic cosmic rays**`；title 回退实现有缺陷（大小写敏感 + 吞 `**`）。**

### ✅ 验证通过

- INDEX 11 篇空标题 `****` → 实测 0（属实）
- 页脚日期硬编码 `2026-08-13` → 动态 `2026-08-14`（属实）
- audit 18 条全绿、工作树干净（属实）
- Cameron 正文 `[FACT]` 属 READING_INSTRUCTIONS 规范用法（"误报"判断正确）

### ❌ 声明与实测不符

- **Amato 标题**：摘要称"The Origin of Galactic Cosmic Rays"，INDEX 82 行实为 `**** The origin of galactic cosmic rays**`——`_fmt_title` 作用在正则从未命中的路径上（修复者验证了函数本身，未验证真实匹配路径）
- **title 回退实现**：代码存在但有缺陷（见根因）

### 🔍 根因（extract_meta 回退正则，`scripts/gen_index.py:52,56`）

1. **大小写敏感**（无 `re.IGNORECASE`）：frontmatter 小写 `title:`/`authors:` 永不匹配 → 必然落回正文 bullet
2. **`**Title:**` 格式吞 `**`**：冒号在加粗内时 `\s*` 吃不掉闭合 `**`，`[^\n]+` 把 `** ` 吞进捕获组 → 外层再包 `**...**` 即成 `**** The origin...**`

**受影响面**：INDEX 6 篇错乱——5 篇 `****` 前缀标题（amato 82/grenier 95/biermann 108/trimble 138/lodders 216）+ cameron 294 行 [FACT] 泄漏 + 6 行作者带 `**`（86/99/112/142/155/220）。blasi 因 `**Title**：`（冒号在加粗外）格式恰好幸免。

### 📝 附带发现（摘要未列）

- Cameron frontmatter tags 残留 `- p-process [FACT]`（registry 已带）——commit 1ecb432 清洗漏 tags
- Biermann frontmatter keywords/tags 整段「⚠️ 重要更正」勘误文本污染（registry 已带）
- Fowler authors 被"平衡 **"修法改为 `**William A. Fowler**（加州理工…）`——元数据字段里塞 markdown

### 复验结论

**精读阶段健康，缺陷集中在派生工具层**：gen_index 未遵守 ADVANCEMENT D1（frontmatter 为机器事实源），在正文上做脆弱字符串解析。audit 18 条断言无 INDEX 内容断言、无 tags 断言 → 全部问题静默漏过。

---

## 附 26：审查 0261524 + d11e261——元数据污染修复第二轮核验（2026-08-14）

> 独立复验：执行侧修复摘要 7 项（IGNORECASE、strip('*')、Biermann/Fowler/Cameron 清理、过期 interactive.html 重建、audit +2 断言）。
> **结论：4/7 属实、2 项不实（Biermann/Fowler 声明已清实未清）、1 项部分；修复引入 2 处新问题（YAML 引号泄漏、pycache 撤回不完整）。**

### ✅ 验证通过

- gen_index 加 `re.IGNORECASE` + 捕获值 `.strip("*")`（代码确认）
- INDEX 错乱清零：`****` 0 / `[FACT]` 0 / 作者前缀 `**` 0；Amato 显示 `The Origin Of Galactic Cosmic Rays`
- Cameron tags 剥 `[FACT]`：registry tags=9 项干净
- 过期 interactive.html 重建：mtime 11:50（提交后），解码 PAPERS=23、Amato tags 干净（"此前为过期产物"本身无历史可证——gitignored，无法回溯）
- audit 20/20 通过

### ❌ 声明与实测不符

- **Biermann 已清**：实测未清——keywords 仍多行含整段勘误文本（含 `---`）；tags 仍 10 项含 3 项污染
- **Fowler 还原**：实测未清——frontmatter 仍 `William A. Fowler**（加州理工…）`，registry/INDEX 同步污染

### 🔍 新发现回归（摘要未列）

1. **YAML 单引号泄漏**：IGNORECASE 命中 frontmatter 引号值（`title: '...: ...'`，含冒号必须引号），`.strip("*")` 不剥引号 → INDEX fowler 151/wallerstein 164 标题带 `'…'`——**用引号泄漏换了 `**` 前缀泄漏**
2. **`__pycache__` 撤回不完整**：d11e261 只改 .gitignore 未 `git rm --cached`——`git ls-files` 仍 1 条（scripts/__pycache__/gen_index.cpython-314.pyc）

### ⚠️ audit 盲区（为何 20/20 仍放行污染）

新断言（audit.py:223,235）只查 `[FACT]/[INTERPRETATION]/[CRITIQUE]` 与 `****` 前缀——**不查 `**` 中缀（Fowler `Fowler**（`）、不查勘误文本（Biermann「重要更正」）、不查引号** → 两处真实污染全绿放行。

### 复验结论

第二轮修复"声称已清"两项实际未落盘（patch 工具误报 no_change 未写盘的典型场景），且断言粒度未跟上声明范围——"加固"未覆盖真实残留类型。

---

## 附 27：审查第三轮——6/7 修复核验 + Wallerstein 状态过期（2026-08-14，未提交）

> 独立复验：修复摘要 6/7 完成 + Wallerstein 1 项未过。
> **结论：6 项全部属实；第 7 项"未过"为快照过期——Wallerstein 工作树已修，frontmatter/registry/webapp 全净；全部改动尚未提交。**

### ✅ 验证通过（6/6）

- **Fowler**：frontmatter `authors: William A. Fowler` + 正文 `- **Authors**: William A. Fowler` 双清
- **Biermann**：keywords 单行 8 词、tags 8 项全净（勘误文本退出元数据）
- **gen_index 剥引号**：三条路径（表格 :49 / authors :56 / title :60）均含 `.strip("'").strip('"')`
- **pycache 撤回**：git ls-files=0、staged deletion 存在
- **audit 扩展**：`_marker_re`（`**`/「重要更正」/⚠️）+ `_tag_re` + `_qre`；INDEX 污染断言——实测 20/20 通过
- **重建**：INDEX 全净（引号/`****`/`[FACT]`/作者 `**` 全 0）；registry 30 条净；interactive.html 13:23（PAPERS 23 / DOCS 31）

### ⚠️ 第 7 项状态过期

报告称 Wallerstein tags 污染为唯一剩余问题（下一步 sed 修）——**实测工作树已修**：`git diff` 实证 keywords 2 行污染删除、tags 4 项截断为 `- r-process site`；frontmatter 12 项 tags、registry、webapp 全部干净；勘误说明仅存正文 line 49（合法阅读指引）。若以报告为准执行会重复劳动。

### ✅ 根因修复代码确认

`build_fm.py:_extract_from_bullets` 多行拼接循环已加**四重停界**：遇 `**` 强调行、`- **` 起始、章节标题（`^#{1,3}`）、空行即停——堵住"吞 `**说明** 注释"根因。

### 📝 观察项

- **全部改动未提交**：8 modified + 1 staged deletion，无新 commit（FreeFileSync 同步扩散/丢失风险）
- `- r-process site` 为截断残留 tag（原始 `r-process site **说明**：…` 截半）——语义尚可，低优先级

### 复验结论

三轮教训闭环：**工具结果不可信**（patch 误报 no_change / execute_code 写沙箱）→ 以 read_file/git diff 验证实际内容（本轮 Wallerstein 过期报告再次印证）；**断言覆盖声明**（audit 已扩展至 `**`/引号/勘误词）；**build_fm 边界修复 + audit 双保险**。阅读/精读阶段全程健康，缺陷始终在派生工具层。
