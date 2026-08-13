# papers/webapp/ — 交互知识库网页构建工具

> 将 `papers/background/` 下的 Markdown 知识库 + 可选的 21 篇论文精读合辑，构建为**单文件离线交互网页**。

## 目录结构

```
webapp/
├── README.md              ← 本文档
├── shell.html             ← 骨架模板（CSS + JS + 3 个 JSON 占位符）
├── build_webapp.py        ← 构建脚本（md→html→b64→注入→输出）
├── md2doc_html.py         ← Markdown → HTML fragment 转换器
└── interactive.html       ← 构建产物（4.4 MB 单文件，离线可用）
```

## 三个文件各自做什么

### shell.html — 骨架模板

网页的**外壳**，包含：
- 全局 CSS（暗/亮主题、flex 布局、sidebar 展开/收起）
- 三个 JSON 占位符（`build_webapp.py` 会替换它们）
- 全部 JavaScript 逻辑（导航、搜索、公式渲染、复制按钮等）

不直接可打开——必须经过 `build_webapp.py` 注入数据后才能使用。

### build_webapp.py — 构建脚本

**流程**：
```
┌──────────────┐    ┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ background/*.md  │──→│ md2doc_html.py  │──→│  base64 编码    │──→│ shell.html      │
│ 文学/论文*.md     │    │ (markdown→html)  │    │  + TOC 提取    │    │ (注入 → 输出)   │
└──────────────┘    └─────────────────┘    └──────────────────┘    └─────────────────┘
```

1. 读取 `background/*.md`（跳过 `00_*`、`99_*` 等非内容文件）
2. 调用 `md2doc_html.py` 将每个 md 转为 HTML fragment
3. 从 fragment 的 `<h2..h6 id="doc-xxx">` 标签提取 TOC
4. 将 fragment 内容 base64 编码（避免 HTML 嵌套转义问题）
5. 将 `DOCS`（文档列表 + b64）、`TOCS`（目录 flat array）、`PAPERS`（论文元数据）注入 `shell.html`
6. 输出单文件 `interactive.html`

### md2doc_html.py — Markdown 转换器

将单个 Markdown 文件转为 HTML fragment。**关键设计**：
- 每个 heading 带 `id="doc-{anchor}"`（anchor 去空格/符号转 `-`、小写）→ 用于 TOC 锚点跳转
- 行内 `$...$` 和块 `$${...}$$` 公式**保留原始 LaTeX**（不渲染），由浏览器端 KaTeX 处理
- 块公式自动添加「📋 LaTeX」复制按钮
- 不输出 `<html>/<body>` 标签——只输出文档正文片段

## 构建流程

```
背景 Markdown ─┐                            ┌─→ shell.html (骨架)
               ├─→ md2doc_html.py ─→ HTML   ├─→ base64 编码 ─→ 注入 DOCS 占位符
论文 Markdown ─┘      fragment    │         ├─→ 提取 TOC   ─→ 注入 TOC 占位符
                                  │         └─→ 论文元数据  ─→ 注入 PAPERS 占位符
                                  │
                    webapp/interactive.html (4.4 MB 单文件)
```

```bash
cd papers

# 仅构建 background 知识库（6 个文档，约 1 MB）
python3 webapp/build_webapp.py

# 包含全部 21 篇论文精读（27 个文档，约 4.4 MB）
python3 webapp/build_webapp.py --include-papers

# 指定输出路径
python3 webapp/build_webapp.py --include-papers --out background/background-interactive.html
```

构建后打开 `webapp/interactive.html`（双击即可，无需服务器）。

## 交互功能

### 导航栏
顶部 27 个标签页（按主题分组：宇宙线传播 / 宇宙线起源 / 恒星核合成 / 论文 21 篇），点击切换文档。

### 侧边栏目录
点击 `☰` 按钮展开，显示当前文档的 TOC（最多 4 级标题，带缩进），**点击 TOC 条目平滑滚动**到对应章节。

### 搜索
顶部搜索框，全文匹配关键词，结果显示"文档名 · 匹配次数"，点击跳转到包含结果的文章。

### 公式
- 行内公式：自动 KaTeX 渲染
- 块公式：右侧带「📋 LaTeX」按钮，点击复制 LaTeX 源码
- 公式字体颜色跟随正文（不会全部红色）

### 主题切换
点击 `🌙`/`☀` 按钮切换暗/亮模式，自动保存到 `localStorage`。

### 跨论文引用卡
文档中 `[{论文编号}]` 语法自动渲染为引用卡片（显示论文年份、标题、主题）。

## 技术细节

### TOC 锚点格式

TOC 条目 id 与 heading id 严格一致，格式为 `doc-{anchor}`，anchor 规则：
```
re.sub(r"[^\w\u4e00-\u9fff0-9-]+", "-", title).strip("-").lower()
```
例如「0.1 文献基本信息」→ `doc-0-1-文献基本信息`。

### 离线降级

KaTeX 通过 CDN 加载（`cdn.jsdelivr.net/npm/katex@0.16.9`），如离线则自动降级为等宽字体显示原始 LaTeX 源码。

### 构建碎片清理

`md2doc_html.py` 生成 `.fragment.html` 临时文件，`build_webapp.py` 完成后自动删除，不残留。

## Git 忽略

`webapp/interactive.html`（4.4 MB 构建产物）已加入 `.gitignore`。
每次修改后重新构建即可。