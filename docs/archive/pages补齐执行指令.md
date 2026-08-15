# pages 全库补齐执行指令（整篇粒度）

> 生成：2026-08-15（WorkBuddy 主会话）｜执行：指定会话（本文件自包含）
> 目的：38 篇文献的 `00_overview.md` frontmatter 补齐 `pages:` 字段（**整篇粒度、期刊正式页码**）
> 背景：超长判定（综述 ≥40 页 / 原始论文 ≥20 页）依赖 pages 全量补齐——精读深度扩充备忘 §3.5/§5 的第一批前置任务
> **用户拍板（2026-08-15）**：pages 统一整篇粒度、只放 00_overview；分章文件已有 pages 不动
> **状态：✅ 已完成（2026-08-15）**——提交链 `1ad9840` 补齐 → `22ec1f1` 分隔符二次修复 → `5c03446` citations YAML 修复 → `11722f2` 备忘追踪。回归与修复记录见文末 §7（含修正后算法与复验口径）

---

## 0. 现状（2026-08-15 实测）

| 类别 | 数量 | 说明 |
|---|---|---|
| 已有整篇 `pages:`（00_overview） | **1 篇** | bell-1978 `pages: '147-156'`（与 Crossref 验证一致，跳过/保留） |
| 分章粒度 `pages:`（分章文件内） | 2 篇 | ruszkowski-pfrommer（5 章，`"11–60"` en-dash）、alvesbatista（4 章，`'2-7'`）——**保留不动** |
| 待补齐 | **37 篇** | 00_overview 无整篇 pages |

**字段覆盖（决定提取途径）**：
- `doi:` 字段：**32/38**
- `arxiv:` 字段：**29/38**
- 两源皆无（需标题搜索/PDF 兜底）：**5 篇**——`02_cosmic-ray-origins/0002_al-dargazelli-1996`、`03_stellar-nucleosynthesis/0006_anders-grevesse`、`0007_grevesse-sauval-1998`、`0011_kewley-2001-starburst`、`0012_dieterich-2014-h-burning-limit`

**环境**：Crossref API 已实测可用（bell DOI `10.1093/mnras/182.2.147` → `page: 147-156`，与库内一致）；本机有 `curl`。

## ⚠️ 铁律（用户要求）

1. **只加不动**：只在 `00_overview.md` frontmatter 增加整篇 `pages:`；**不得**改动分章文件的 pages、不得改动其他任何字段/正文。
2. **不编造**：页码范围必须来自可靠来源（Crossref / arXiv journal-ref / PDF 首页页眉）；查不到的篇目**列入"待人工"清单并说明原因**，宁缺毋滥，绝不允许凭 PDF 页数或记忆推断页码。
3. **语义**：`pages` = 期刊正式出版页码（如 RMP 79, 2451 → `'2451-2489'`）；**文章号型期刊**（PRD 等）crossref 返回单号（如 `083005`）时照写单号，**不强行造结束页**。
4. **格式统一**：`pages: '147-156'`——单引号、ASCII 连字符 `-`、无空格、无 en-dash（`–`）。

## 1. 提取途径（按优先级逐篇执行）

### 步骤 1：Crossref DOI 查询（32 篇，主途径）

```bash
# 逐篇查询（替换 DOI；URL 中的 / 直接保留）
curl -s "https://api.crossref.org/works/10.1103/RevModPhys.79.2451" | python3 -c "
import json,sys
m = json.load(sys.stdin)['message']
print('page:', m.get('page'), '| volume:', m.get('volume'))"
```

- 取 `message.page`（可能为 `"2451-2489"`、`"083005"` 或缺失）
- **无 `page` 字段**（部分老文献 Crossref 无页码）→ 转步骤 2/3

### 步骤 2：Crossref 标题查询（无 DOI 或 DOI 无 page 的篇）

```bash
curl -s "https://api.crossref.org/works?query.bibliographic=<论文标题>&rows=3" | python3 -c "
import json,sys
for it in json.load(sys.stdin)['message']['items']:
    print(it.get('title',['?'])[0][:50], '|', it.get('page'), '|', it.get('DOI'))"
```

- 取标题最匹配且含 `page` 的条目；**人工核对标题/期刊/年份一致**才采用

### 步骤 3：arXiv journal-ref（有 arxiv 字段的篇）

```bash
curl -s "https://arxiv.org/abs/2103.04108" | grep -oE 'journal_ref[^<]*|citation_journal_title[^>]*>[^<]*' | head -3
```

- 页面元数据含 journal-ref（如 `Phys. Rev. D 104, 083005 (2021)`）→ 提取页码

### 步骤 4：PDF 首页页眉 + pdfinfo（兜底，限老扫描文献）

```bash
pdfinfo <pdf路径> | grep Pages              # 页数（辅助）
pdftotext -f 1 -l 2 -layout <pdf路径> -      # 首页页眉常含期刊页码（如 147、152）
```

- 页眉页码 + pdfinfo 页数 → 推算页码范围（如首页页眉 147、共 10 页 → 147-156）
- **仅当**该篇确认无 Crossref/arXiv 记录时使用，且结果须在交付物中标注"PDF 推断"

### 步骤 5：待人工清单

- 以上均无法获得可靠页码 → 记录到交付物表格，**不写 pages、不编造**

## 2. 写入规范

- 文件：每篇 `literature_analysis/00_overview.md`
- 插入位置：frontmatter 中 **`journal:` 字段之后、`doi:` 之前**（无 `doi:` 则紧跟 `journal:` 之后）

```yaml
journal: Reviews of Modern Physics（根据格式推断，arXiv 上标注为 RMP 投稿，2008 年 2 月为草稿日期）
pages: '2451-2489'
doi: 10.1103/RevModPhys.79.2451
```

- 保留原有注释/格式；只插入一行

## 3. 验证（对照原文铁律）

1. **覆盖**：38/38 篇 00_overview 有 `pages:`（含 bell 原有）
2. **格式**：全部匹配 `^pages: '[0-9]+(-[0-9]+)?'$`（单引号 + ASCII 连字符；无 en-dash）
3. **合法性**：`start ≤ end`；`end-start+1 ≤ 300`（防异常值）
4. **交叉核对**：随机抽查 ≥10 篇，`pages` 与 Crossref 返回值逐字符一致；bell 与库内既有值一致
5. **待人工清单**：逐条列原因（如"Crossref 无 page 且无 arXiv"），清单允许非空但必须有解释

```bash
# 复验命令（执行侧自查）
grep -c "pages:" $(find . -name 00_overview.md)   # 应为 38
grep -rh "^pages:" --include="00_overview.md" . | grep -vE "^pages: '[0-9]+(-[0-9]+)?'$"  # 应为空
```

## 4. 提交约定

- **单笔提交**：`git add` 仅 38 个 `00_overview.md`（`git add 01_cosmic-ray-propagation/*/literature_analysis/00_overview.md ...`，或逐个路径），**不得 `git add -A`、不得动其他文件**
- commit message：`chore(papers): 补齐 38 篇 00_overview pages 字段（整篇粒度，Crossref/arXiv/PDF 多源）`
- 交付物表格（来源标注）放提交说明 body 或单独记录在 REVIEWS 条目

## 5. 交付物

- 38 篇 `00_overview.md` 的 `pages:` 字段（37 新增 + 1 保留）
- 来源明细表：每篇一行 `篇目 | pages | 来源(crossref-doi/crossref-title/arxiv/pdf/待人工) | 备注`

## 6. 完成标准（WorkBuddy 复验口径）

1. `grep -c "pages:"` 38/38 ✓
2. 格式/合法性正则全过、en-dash 残留 0 ✓
3. ≥10 篇抽查与 Crossref 一致 ✓
4. 待人工清单已列原因，数量 ≤5 且无"编造值" ✓
5. 工作树除 38 个 00_overview.md 外无其他改动 ✓

---

## 7. 回归与修复记录（1ad9840 误删 frontmatter 分隔符 → 已闭环）

> 本段为 2026-08-15 执行后的回归事件记录 + 最终复验口径，替代原独立《pages 补齐回归修复执行指令》（已合并删除）。

### 7.1 回归事件链

| 提交 | 事件 | 结果 |
|---|---|---|
| `1ad9840` | Hermes 补齐 pages 38/38（数值全部正确：Crossref 明细核对、A74/L29 为 ApJ 文章编号型合法页码） | ❌ **误删 37/38 篇 frontmatter 首尾 `---`**（仅 bell 未触碰）→ YAML 不闭合，Obsidian 属性面板不渲染 |
| `c746689` | Hermes 修复 | ❌ **只补了开头 `---`**，27/37 篇结尾仍缺（脚本把刚插的开头当结尾证据） |
| `22ec1f1` | WorkBuddy 二次修复 | ✅ 27 篇补结尾（+27 行纯 `---`，diff 纯净、幂等） |
| `5c03446` | WorkBuddy 深挖属性面板 | ✅ **修复老库 23 篇 `citations: []` + 顶格列表 YAML 非法**（`citations: []`→`citations:`，每篇 1 行）——这才是属性面板不渲染的直接根因 |

### 7.2 修正后修复算法（防再犯，已验证幂等）

```python
def is_fm_line(s):
    """True=frontmatter 内容行或结构行(可跳过)；False=正文行"""
    if s.strip() in ('', '---'): return True     # 空行与 --- 结构行都跳过
    if s.startswith(' '): return True            # 缩进续行
    if s.startswith('- '): return True           # 列表项（含顶格 `- '[[...]]'`）
    if re.match(r'^[A-Za-z_][A-Za-z0-9_]*\s*:', s): return True  # key:
    return False
```

- 补开头：首行非 `---` 则插入；补结尾：**正文第一行**（第一个 `is_fm_line` False 的行）前若无 `---` 则插入
- **坑 1**：`---` 必须被跳过（返回 True）——若当正文会双补
- **坑 2**：先插开头再查"已有 ---"会把刚插的开头当结尾证据 → 跳过补结尾（Hermes 的 bug）
- 写回用 `split('\n')` + `'\n'.join()` 保行尾/末尾换行原样，diff 才纯净

### 7.3 复验判定（最终版，勿用旧口径）

- **frontmatter 完整性**：`head -1 == "---"` **且** 正文第一行前 `---` 数 ≥ 2（开头+结尾）。勿用"正文前含 ---"（把开头当结尾→假阳性 38/38）、勿用"正文前一行==---"（结尾后隔空行→bell 误判）
- **YAML 可解析性（权威）**：用 PyYAML（`/Users/jcxs2014/.workbuddy/binaries/python/envs/default/bin/python`，已装）`yaml.safe_load(frontmatter)`，38/38 全过
- **全库 frontmatter 健康**：386 md / 99 真 frontmatter（38 个 00_overview + 61 其他）全部可解析；98_vocabulary/99_final_summary 无 frontmatter（`---` 后直接正文标题）非损坏
- **frontmatter 判定**：`---` 与 `---` 之间须含 `^[A-Za-z_]\w*\s*:` key 行，否则视为无 frontmatter（防把 98/99 误当损坏）
