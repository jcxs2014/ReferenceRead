# papers/webapp/ — 交互知识库网页（构建与维护引导）

> 将 `papers/background/` 知识库 + 38 篇论文精读，构建为**单文件离线交互网页**（`interactive.html`）。
> 本 README 是 webapp 的统一引导：目录结构 → 脚本分类 → 构建链执行步骤 → 注意事项。

## 目录结构

```
webapp/
├── README.md              ← 本文档（统一引导）
├── shell.html             ← 骨架模板（CSS + JS + 3 个 JSON 占位符，构建注入数据）
├── docs/                  ← webapp 文档（审查报告）
├── scripts/               ← 构建/服务脚本（分类见下）
│   └── archive/           ← 已完成使命/一次性脚本（勿全库重跑）
├── tests/                 ← 单元测试（unittest，verify_claim 门禁会跑）
├── third-party/katex/     ← KaTeX 自托管资源（http:// 协议本地字体）
├── interactive.html       ← 构建产物（~7 MB，不入库）
├── registry.json          ← 构建产物（45 条，不入库）
├── glossary.json          ← 构建产物（766 术语，不入库）
├── search_index.json      ← 构建产物（全文索引，不入库）
├── manifest.json / icon-*.png / apple-touch-icon.png  ← PWA 产物（不入库）
```

**构建产物全部不入库**（顶层 `.gitignore` 统一管理），由构建链再生成。

## 脚本分类（12 → 9 保留 + 3 归档）

| 类别 | 脚本 | 用途 | 执行时机 |
|---|---|---|---|
| **构建链必需**（每次构建跑） | `build_registry.py` `build_glossary.py` `build_search_index.py` `build_webapp.py` `audit.py` `md2doc_html.py` | 生成 registry/glossary/索引 → 构建 interactive.html → 审计 | 每次构建 |
| **按需** | `server.py` | 形态 B 本地服务（/api/progress, /api/rebuild） | 需要本地服务时 |
| **危险·仅新库**（⚠️） | `build_fm.py` `build_citations.py` | 写 frontmatter / 生成 citations | **仅新文献入库**；存量库禁止全库重跑（见注意事项 1） |
| **已归档**（archive/） | `apply_wikilinks.py` `patch_appendix_nav.py` `build_pwa.py` | 图谱 wikilink 化 / 97/98/99 补导航 / PWA 资源 | 已完成使命；重生成按需（见注意事项 3） |

## 构建链执行步骤（详细）

```bash
cd papers

# ── 一键全链路（推荐，scripts/build_all.py，9 步骤）──
python3 scripts/build_all.py                # citations→fm→registry→glossary→index→search_index→webapp→audit→quality

# ── 手动分步（从 papers 根目录）──
PY=/Users/jcxs2014/.workbuddy/binaries/python/envs/default/bin/python

# 1. registry（frontmatter → registry.json）
$PY webapp/scripts/build_registry.py
# 2. glossary（98_vocabulary → glossary.json）
$PY webapp/scripts/build_glossary.py
# 3. 全文索引（md → search_index.json）
$PY webapp/scripts/build_search_index.py
# 4. 主构建（background + 论文 → interactive.html）
$PY webapp/scripts/build_webapp.py --include-papers    # 含 38 篇论文；仅背景用不带参数
# 5. 审计（18 条断言 + 附检查，失败非零退出）
$PY webapp/scripts/audit.py

# ── 声称完成门禁（非破坏性检查）──
bash scripts/verify_claim.sh               # 或 --full-rebuild 真重建
```

构建后打开 `webapp/interactive.html`（双击即可，无需服务器）。本地服务：`python3 webapp/scripts/server.py`。

## ⚠️ 注意事项（重要）

### 1. build_fm / build_citations 存量库禁止全库重跑（P0 教训，见 docs/TROUBLESHOOTING A7）

- **build_fm.py 是"白名单重建"**——重写 frontmatter 只保留 `title/authors/year/category/status/read_date/lastread/tags/citations/path`，**会丢弃 journal/doi/arxiv/pages/sections/keywords 等增强字段**（2026-08-15 曾致 38 篇属性面板字段丢失，已回滚）
- **build_citations.py 会重写 38 篇 frontmatter 的 citations**——存量库重跑会清空/改写
- **适用场景**：仅新文献入库时的单篇/新库初始化；跑前必须 `--dry-run` 对比字段差异
- 全库构建链（build_all）默认以 `--dry-run` 跑这两步——**不要去掉 dry-run**

### 2. 产物不入库

registry.json / glossary.json / search_index.json / manifest.json / icon-*.png / apple-touch-icon.png / interactive.html 全部 `.gitignore`，由构建链再生成。**不要 git add 这些产物**。

### 3. 归档脚本（webapp/scripts/archive/）重生成方法

| 脚本 | 何时重跑 | 命令 |
|---|---|---|
| `apply_wikilinks.py` | 新文献入库后需图谱 wikilink 化 | `python3 webapp/scripts/archive/apply_wikilinks.py`（幂等，但存量库重跑会产生换行噪音，确认 diff 后再提交） |
| `patch_appendix_nav.py` | 新篇 97/98/99 缺导航头 | `python3 webapp/scripts/archive/patch_appendix_nav.py` |
| `build_pwa.py` | 需重生成 PWA 图标/manifest | `python3 webapp/scripts/archive/build_pwa.py`（需 venv 有 Pillow） |

### 4. 环境

- 需要 PyYAML 的脚本（build_registry 等）用 **managed venv**：`/Users/jcxs2014/.workbuddy/binaries/python/envs/default/bin/python`（系统 python3 无 yaml）
- build_pwa 需要 Pillow（venv 已装 12.3.0）
- KaTeX 协议自适应：`file://` 走 CDN、`http://` 走 third-party 本地字体（shell.html 自动切换）

## 故障指引

- webapp 构建/渲染故障：`docs/TROUBLESHOOTING.md` B 区（B1–B18）
- frontmatter/YAML/脚本回归：`docs/TROUBLESHOOTING.md` A 区（A2–A7）
- 构建链验证：`bash scripts/verify_claim.sh`（PASS=11 门禁）
