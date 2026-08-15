# papers/webapp/ — 交互知识库网页（构建与维护引导）

> 将 `papers/background/` 知识库 + 38 篇论文精读，构建为**单文件离线交互网页**（`interactive.html`）。
> 本 README 是 webapp 的统一引导：目录结构 → 构建链 → 快速开始 → 故障指引。

## 目录结构

```
webapp/
├── README.md              ← 本文档（统一引导）
├── shell.html             ← 骨架模板（CSS + JS + 3 个 JSON 占位符，构建注入数据）
├── scripts/               ← 12 个构建/服务脚本（统一管理，见「构建链」）
├── docs/                  ← webapp 文档（审查报告：webapp/docs/审查报告.md）
├── tests/                 ← 单元测试（unittest，verify_claim 门禁会跑）
├── third-party/katex/     ← KaTeX 自托管资源（http:// 协议本地字体，315197a 引入）
├── interactive.html       ← 构建产物（~7 MB 单文件，不入库）
├── registry.json          ← 构建产物（45 条，不入库）
├── glossary.json          ← 构建产物（769 术语，不入库）
├── search_index.json      ← 构建产物（全文索引，不入库）
├── manifest.json / icon-*.png / apple-touch-icon.png  ← PWA 产物（不入库）
```

**构建产物全部不入库**（顶层 `.gitignore` 统一管理），由构建链再生成。

## 构建链（webapp/scripts/ 12 脚本）

| 脚本 | 职责 | 顺序 |
|---|---|---|
| `build_citations.py` | citations 唯一生成器（篇间导航 → 库内引用） | 1 |
| `build_fm.py` | 写 frontmatter（剥 `[FACT]`/wikilink 透传/P0-6 防护） | 2 |
| `build_registry.py` | 读 frontmatter → `registry.json` | 3 |
| `build_glossary.py` | 98_vocabulary → `glossary.json` | 4 |
| `build_webapp.py` | 主构建（`--include-papers` 收论文） | 5 |
| `audit.py` | 构建后审计（18 条断言，失败非零退出） | 6 |
| `build_pwa.py` | PWA 资源（manifest + 图标 + shell 注入） | 7 |
| `apply_wikilinks.py` | V2.2 导航/citations → Obsidian wikilink | 8 |
| `patch_appendix_nav.py` | V2.2 97/98 附录补链 | 8 前置 |
| `server.py` | 形态 B 服务层（/api/progress?slug=, /api/rebuild） | 独立 |
| `md2doc_html.py` | md → HTML 片段（build_webapp 内部调用） | 内部 |
| `build_search_index.py` | 全文搜索索引 | build_webapp 内部 |

**最小可重跑链**：`build_citations → build_fm → build_registry → build_webapp → audit`

## 快速开始

```bash
cd papers

# 一键全链路（scripts/build_all.py，含 citations/fm/registry/glossary/index/webapp/pwa/audit）
python3 scripts/build_all.py --full

# 或手动最小链（从 papers 根目录）
python3 webapp/scripts/build_citations.py
python3 webapp/scripts/build_fm.py
python3 webapp/scripts/build_registry.py
python3 webapp/scripts/build_webapp.py --include-papers
python3 webapp/scripts/audit.py            # 18 条断言

# 声称完成门禁（非破坏性检查）
bash scripts/verify_claim.sh               # 或 --full-rebuild 真重建

# 本地服务（形态 B）
python3 webapp/scripts/server.py
```

构建后打开 `webapp/interactive.html`（双击即可，无需服务器）。

## 协议自适应（KaTeX 字体）

- `file://` 打开：KaTeX 走 CDN（`cdn.jsdelivr.net/npm/katex@0.16.9`），离线自动降级为等宽源码
- `http://` 服务：走 `third-party/katex/` 本地字体（自托管，`shell.html` 按协议自动切换）

## 故障指引

- webapp 构建/渲染故障：见 `docs/TROUBLESHOOTING.md` B 区（B1–B18，KaTeX 时序/overlay/搜索高亮等）
- frontmatter/YAML/审计问题：见 `docs/TROUBLESHOOTING.md` A 区（A2–A6）
- 公式转换工具（Unicode → LaTeX / 割裂修复）：`scripts/convert_supsub.py` 等（库级工具，非本目录）
