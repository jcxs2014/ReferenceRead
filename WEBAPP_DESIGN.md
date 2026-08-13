# background 知识库交互式网页 — 详细实施方案

> 关联条目：`ENHANCEMENTS.md` #7（P2 工具与体验层）
> 版本：v1（2026-08-13，由 WorkBuddy 审查时起草，供执行侧 Hermes agent 参考/确认后实施）
> 可复用资产：`/Users/jcxs2014/Sites/Workbuddy-Local/agent-harness/agent-harness-interactive.html`（220KB 单文件）与 `tools/md2doc_html.py`（无依赖 md→HTML 转换器）

---

## 1. 定位与目标

把 `background/` 三篇跨文献知识库从「静态 md」升级为「可检索、可跳转、可交互的单文件网页」，解决当前痛点：

| 痛点 | 现状 | 目标 |
|---|---|---|
| 检索 | 212 个 md 只能靠编辑器/ripgrep | 网页内全文搜索 + 结果定位高亮 |
| 公式 | LaTeX 源码不可读，GitHub 渲染不全 | 网页内可读的公式排版 |
| 导航 | 三篇文档 + 21 篇论文各自孤立 | 自动目录、滚动高亮、篇间交叉跳转 |
| 术语 | 21 篇词汇表各自独立 | 全库术语表可点击查询 |
| 体验 | 纯文本 | 浅/深主题、阅读进度记忆、可打印 |

**设计原则**（沿用 agent-harness 成功范式）：单文件、无外部依赖、离线可用、浏览器直接打开即用。

---

## 2. 内容与数据规模（实测，2026-08-13）

| 文档 | 行数 | 章节(#) | 公式块($$) | 行内公式 | 表格行 |
|---|---|---|---|---|---|
| `01_cosmic_rays.md`（宇宙线） | 673 | 31 | 64 | 387 | 137 |
| `02_nucleosynthesis.md`（核合成） | 910 | 68 | 40 | 97 | 266 |
| `03_astrophysics.md`（丰度/暗物质） | 643 | 63 | 18 | 28 | 167 |
| **合计** | **2226** | **162** | **122** | **512** | **570** |

**结论**：
- 公式总量大（122 块 + 512 行内）→ 公式渲染是首要技术决策（见 §4.2）。
- 表格 570 行 → 转换器必须正确处理表格（含 blockquote 内表格，已踩过坑）。
- 网页预计体积 300–450KB，离线单文件完全可行（agent-harness 为 220KB）。

---

## 3. 功能设计

### P0 — 核心（必须）
| # | 功能 | 说明 | 复用来源 |
|---|---|---|---|
| F1 | 三文档切换 | 顶部 tab 或下拉，切换三篇背景文档 | agent-harness 导航 |
| F2 | 自动目录 TOC + 滚动高亮 | 左侧目录，滚动时高亮当前章节 | agent-harness scrollSpy |
| F3 | 全文搜索 | 跨当前文档搜索，命中高亮 + 结果列表跳转 | agent-harness runDocSearch（含 escHtml/escapeReg） |
| F4 | 公式渲染（预渲染方案） | 见 §4.2 | 新增 |
| F5 | 浅/深主题切换 | localStorage 记忆 | agent-harness toggleTheme |
| F6 | 论文交叉跳转 | 每篇背景文档页脚列出「本章涉及论文」链接 → 跳转对应论文 `00_overview`（新开标签打开 md 或未来嵌入摘要） | 新增，数据来自 INDEX.md |
| F7 | 阅读进度记忆 | localStorage 记录每文档滚动位置 + 章节勾选 | 新增 |

### P1 — 增强（第二迭代）
| # | 功能 | 说明 |
|---|---|---|
| F8 | 全库术语表 | 聚合 21 篇 `98_vocabulary.md` 的 B 部分（领域术语），去重汇总，点击词条定位到出处文档/章节 |
| F9 | 数值速查表 | 与 ENHANCEMENTS #4 联动：background/README 的公式索引升级为「公式+关键数值」双索引页 |
| F10 | 主题知识图谱 | 三文档 × 21 篇的归属/引用关系，SVG 可点击（类似 agent-harness 5 拓扑图） |
| F11 | 打印友好 | @media print，可导出单篇文档为干净 PDF |

### P2 — 可选（体验打磨）
- 双语（zh/en）——三篇文档以中文为主、公式与英文术语密集，双语价值低，暂缓
- 移动端布局优化
- 每篇论文摘要内嵌（21 篇 overview 摘要直接嵌网页，点击展开）——若 F6 采用内嵌方案则并入 P0

---

## 4. 技术方案

### 4.1 总体架构：单文件 + 预渲染数据

```
background-interactive.html（单文件，无外部请求）
├── <style>        主题变量（浅/深）、布局、打印样式
├── <div id=nav>   三文档切换 + 全库术语表入口
├── <div id=toc>   自动目录（按当前文档生成）
├── <div id=doc>   三个 <section> 预渲染的文档 HTML（切换显隐，agent-harness 双容器模式）
├── <script>
│   ├── DATA:      三篇文档 HTML 片段（由 md2doc_html.py 预转换，内嵌字符串）
│   ├── DATA2:     21 篇论文元数据（编号/标题/作者/主题域/路径，来自 INDEX.md）
│   ├── DATA3:     术语表（21 篇 vocabulary B 部分聚合，P1）
│   ├── setLang/toggleTheme/localStorage      ← 复用 agent-harness
│   ├── buildTOC/scrollSpy/runDocSearch       ← 复用 agent-harness
│   └── renderMath（预渲染已内嵌，运行时无需处理）
```

### 4.2 关键技术决策：公式渲染（三选一）

| 方案 | 效果 | 离线 | 体积 | 维护 | 推荐度 |
|---|---|---|---|---|---|
| A. 运行时 KaTeX/MathJax（CDN） | ★★★ 真正排版 | ✗ 需网络 | 小 | 简单 | 中（仅需网络场景） |
| B. 构建期预渲染 HTML（CSS 排版） | ★★ 结构清晰、无真排版 | ✓ | 小 | 转换器逻辑 | **高（推荐）** |
| C. 预渲染 + 可选 CDN 增强 | ★★→★★★ | 部分 | 小 | 双路径 | 中 |

**推荐方案 B**，理由：
1. 与「离线单文件」原则一致（用户已验证 agent-harness 离线价值）；
2. 122 块公式绝大多数是可预渲染的结构（分数、指数、下标、希腊字母、和式）；
3. 转换器在 `md2doc_html.py` 中扩展 `latex_to_html()`，规则示例：
   - `\frac{a}{b}` → `<span class="frac"><span class="num">a</span><span class="den">b</span></span>`
   - `^ {…}` / `_{…}` → `<sup>` / `<sub>`
   - `\rm / \text{中文}` → 正体 span（background 已用 `\text{}` 包裹中文，2026-08-12 修复过）
   - 希腊字母表（α β γ δ λ σ …）→ 实体字符
   - `\cdot \times \nabla \partial \rightarrow` → 实体/符号
   - 无法识别的复杂结构 → 降级为 `<code>` 等宽展示（宁可显示源码，不可显示错误）
4. 若未来确实需要真排版，保留方案 A 作为可开关增强（`<script>` 动态加载），不影响 B 的默认路径。

### 4.3 数据管线（md 改动后如何重建）

```
background/*.md
   │  修改后
   ▼
tools/md2doc_html.py（参数化：SRC=md, OUT=片段）
   │  输出
   ▼
tools/build_webapp.py（三步）
   1. 对三篇 md 分别调用 md2doc_html.py → 三份 HTML 片段
   2. 从 INDEX.md / 各篇 00_overview 提取 21 篇元数据 → JS 数组
   3. 注入 HTML 模板（占位符替换，用 assert 防漏）→ background-interactive.html
```

- 转换器必须沿用 agent-harness 已验证的细节：`html.escape` 转义、表格处理、列表处理、blockquote 处理（**注意 background 存在 blockquote 内表格的变体，需专门测试**）。
- 脚本存放：`papers/background/tools/`（background/ 未被 .gitignore 忽略，可入库）。

### 4.4 目录与文件布局

```
papers/background/
├── README.md               ← 追加「交互网页」说明与重建命令
├── 01_cosmic_rays.md       （源文档，不改动）
├── 02_nucleosynthesis.md
├── 03_astrophysics.md
├── background-interactive.html   ← 交付物（单文件）
└── tools/
    ├── md2doc_html.py      （从 agent-harness 复制适配）
    └── build_webapp.py     （编排：三篇转换 + 元数据注入）
```

---

## 5. 页面结构（布局）

```
┌────────────────────────────────────────────────┐
│ 顶栏: [宇宙线] [核合成] [丰度/暗物质] │ 主题切换 │ 搜索框 │
├──────────┬─────────────────────────────────────┤
│ 目录 TOC │  文档正文（随顶部切换）              │
│ (滚动    │  公式渲染 / 表格 / 引用块            │
│  高亮)   │  ……                                │
│          │  ── 本章涉及论文 ──                  │
│          │  [Strong 2007] [Blasi 2013] …(F6)   │
├──────────┴─────────────────────────────────────┤
│ 底栏: 阅读进度(章节勾选 F7) · 打印(F11) · 21 篇索引入口 │
└────────────────────────────────────────────────┘
```

---

## 6. 关键实现细节与坑（来自 agent-harness 实战）

1. **全局 let/const 必须放 script 顶部**——曾因 `LANG` 放中部触发 TDZ，整段脚本失效（"EN 按钮不可点"事故）。
2. **搜索高亮必须 escHtml 转义**——搜 `&`/`<` 会破坏文档 DOM / 自注入；`escapeReg` 处理正则特殊字符。
3. **Python 批量替换要 assert 防漏**——占位符（如 `/*__DOC1__*/`）替换后 assert 不再含占位符；注意 `&gt;` 与未转义 `>` 变体并存。
4. **表格转换**：background 有 blockquote 内表格、多行表头等变体，转换器需覆盖；md2doc_html.py 已禁用 Pandoc 式 multiline 判定（那是 pandoc 流程的坑，此处为自研转换器）。
5. **公式中文**：`\text{中文}` 必须保持正体不斜体；2026-08-12 已在 background 修复过双反斜杠与 blockquote 内表格问题，转换器按修复后格式为准。
6. **大 HTML 维护**：不要手改生成的 HTML，只改 md 源 + 重跑管线；HTML 文件可加入 `.gitignore`（如背景文档稳定后可考虑），避免每次重建产生 diff 噪音——**决策点，由执行侧定**。

---

## 7. 里程碑与工作量

| 里程碑 | 内容 | 预估 |
|---|---|---|
| M1 数据管线 | md2doc_html.py 适配 background（公式 latex_to_html + 表格变体 + 引用块），产出三份片段 | 2–3 单元 |
| M2 骨架 | 单文件壳：导航/TOC/滚动高亮/主题切换/搜索，先跑通一篇文档 | 2 单元 |
| M3 集成 | 三篇全量嵌入 + 论文交叉跳转(F6) + 阅读进度(F7) | 1–2 单元 |
| M4 增强 | 术语表(F8) + 数值/公式索引(F9) + 打印(F11) | 2 单元 |
| M5 打磨 | 移动端、边界 case、浏览器兼容、验收 | 1 单元 |

（"单元"以执行侧 Hermes agent 的工时口径计，约等于一个连续工作段。）

## 8. 风险与对策

| 风险 | 对策 |
|---|---|
| 公式预渲染效果不佳（复杂公式如 3α 反应率、DSA 谱） | 降级规则兜底显示源码；保留 CDN 增强开关（方案 A） |
| HTML 体积过大（>500KB） | 三篇按需懒渲染（切到该文档才填充），或拆三份 HTML |
| md 与网页不同步 | 以 md 为唯一事实源，README 写明"改 md → 重跑 build_webapp.py" |
| 与 Hermes agent 维护流程冲突 | 方案待用户/执行侧确认后再动工；所有脚本放 `background/tools/` 不污染其他结构 |

## 9. 验收标准

- [ ] 浏览器直接打开 `background-interactive.html` 离线可用（断网可测）
- [ ] 三篇文档切换、目录滚动高亮、全文搜索定位正常
- [ ] 122 块公式 + 512 行内公式全部有输出（可读排版或显式降级，无渲染错误/无源码串行）
- [ ] 21 篇论文交叉跳转链接指向正确路径
- [ ] 主题切换、进度记忆刷新后保持
- [ ] 打印样式导出干净（M4 后）

---

# V2 增强方案（2026-08-13 用户询问后立项，审查报告附 10 后）

> 背景：webapp 已稳定可用（27 文档 / 5MB 单文件 / 全部修复收敛）。以下为三项增强的方向与具体改法，按性价比排序。执行侧确认后实施。

## E2（首推）懒解码 —— 首屏 DOM 构建 27→1 个文档

- **问题**：`buildDocs()` 一次性 decode 全部 27 个 b64 并注入 27 个 `<section>`（约 5MB 字符串），首屏卡顿（M9）。
- **改法**（shell.html）：
  ```js
  const docCache = {};   // slug -> decoded HTML
  function getDocHTML(slug) {
    if (!(slug in docCache)) {
      const d = DOCS.find(x => x.slug === slug);
      docCache[slug] = decodeBase64(d.b64 || d.body_b64);
    }
    return docCache[slug];
  }
  // buildDocs(): 只渲染当前文档 section
  // switchDoc(slug): 先确保该 section 存在（没有则 append），再切换 active
  ```
  要点：初始只构建 `activeSlug` 的 section；切换时按需 append + 缓存；TOC/搜索遍历全部 section 的逻辑需适配（搜索可改为"对已加载 section 搜索 + 未加载文档只查标题/摘要"或保持全量构建 TOC 但正文懒加载）。
- **收益**：首屏 DOM 构建从 ~5MB 降到 ~200KB（约 10–25 倍）；本地文件下载体积不变。
- **工作量**：约 0.5–1 单元。

## E3（顺手）b64 → UTF-8 直存 —— 文件 5.0MB → ~3.7MB

- **问题**：base64 编码有 33% 体积膨胀。
- **改法**（build_webapp.py）：`json.dumps` 直接放 HTML 字符串（`ensure_ascii=False` 已处理中文/引号），删掉 `decodeBase64()`，shell 中 `DOCS[i].html` 直接用。注意 JSON 字符串内不能有裸 `</script>`（HTML 内容含 `</script>` 会截断——b64 正是为此引入；改用 `</scr` + `ipt` 转义或确保 md 转换器不输出裸 script 标签，转换器不输出 script 所以安全）。
- **收益**：体积 -26%；解析少一层解码。
- **工作量**：约 0.3 单元。建议与 E2 一起做。

## E1 轻量首页 —— 默认文档（成本最低）

- **做法**：新增 `background/00_home.md`，`build_webapp.py` 的 `bg_files` 数组首位加入 `("00_home.md", "首页")`，使其成为 `DOCS[0]`（默认打开）。
- **内容建议**：库定位一句话；三个主题组（传播 1 / 起源 7 / 核合成 13）各一段介绍 + 入口；推荐阅读路径（背景 README 已有：入门 → 核合成 → 宇宙线）；速查表 / 术语表 / CRITIQUE 三个工具入口。
- **收益**：新用户进来有上下文、有路径；几乎零成本（1 个 md + 重建）。
- **工作量**：0.2 单元（写 md）。

## E4（远期）真分模块 —— 仅当"部署到服务器"时

- **约束**：`file://` 协议下 `fetch` 本地文件被 CORS 拦截，多文件按需加载会破坏"双击打开离线"卖点。
- **触发条件**：库持续增长至 >10MB，且接受部署静态服务器（或本地起 http server）。
- **做法**：`index.html`（壳）+ 每文档一个 `.json`（或 `docs/01.json`…），`fetch` 按需加载；服务端 gzip（HTML 文本可再压 5–6 倍）。
- **不触发时**：永远走 E2+E3（单文件 + 懒解码 + 紧凑编码）。

## 执行顺序建议

1. **E2 + E3**（首屏性能 + 体积，一起改，一次构建）
2. **E1**（首页，0.2 单元）
3. **N3 已关闭 / B2 TOC 限级 + M6 无障碍**（低优先，可与 E1 同批）
4. **E4**（远期，触发条件满足再做）

> 与本方案配套的验证：构建后跑附 4 断言（id 唯一双向 / label 合法 / stats 一致），UI 改动附双端截图。

---

## V2 补充（2026-08-13 用户反馈后追加）

### E1 增补：当前文档面包屑（方案 B，与首页同批）

- **问题**：组按钮显示文档标题（H6D2）破坏导航语义（用户确认"不太好"）；方案 A（组按钮恒显组名）为最小修正，面包屑为可选增强。
- **做法**：组按钮永远显示组名（删掉 switchDoc 中 `b.textContent = getDoc(slug).title`）；在主区顶部加静态面包屑 `组名 / 当前文档标题`（如 `背景知识 / 宇宙线（传播与起源）`），switchDoc 时更新。
- **归属**：与 E1 首页同批实施。

### E5 下拉菜单现代化（用户评价"上个世纪的作品"，独立视觉打磨）

- **问题**：无动画硬切、active 整块 accent 填充（按钮样式）、单层浅阴影无层次、13px 小字无分组分区。
- **改造**（CSS 级，不动 JS 逻辑）：
  ```css
  .tab-dropdown { border-radius:12px; padding:8px;
    box-shadow:0 4px 16px rgba(0,0,0,.12), 0 16px 48px rgba(0,0,0,.18); }
  .tab-group.open .tab-dropdown { animation:menuIn .12s ease-out; }
  @keyframes menuIn { from{opacity:0; transform:translateY(-4px)} to{opacity:1; transform:none} }
  .tab-dropdown-item { padding:8px 14px; border-radius:6px; border-left:3px solid transparent; }
  .tab-dropdown-item:hover { background:rgba(var(--accent-rgb),.08); }
  .tab-dropdown-item.active { background:rgba(var(--accent-rgb),.10); color:var(--accent);
    border-left-color:var(--accent); font-weight:600; }
  .tab-dropdown hr { margin:6px 8px; border-top:1px solid var(--border); }
  ```
  建议在 `:root`/dark 分别定义 `--accent-rgb`（light: 9,105,218 / dark: 88,166,255）；分组分隔线按需加。
- **优先级**：低-中（纯视觉），建议与 E1 批一起做。
