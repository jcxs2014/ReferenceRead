# fulltext 全库补齐执行指令

> 生成：2026-08-15（WorkBuddy 主会话）｜执行：指定会话（本文件自包含）
> 目的：老库 22 篇缺失/命名不统一的提取文本，统一为 `fulltext.txt` 并补齐
> **用户明确要求：已有文本不重新提取，仅统一名称**

---

## 0. 现状（2026-08-15 实测）

| 类别 | 篇数 | 说明 |
|---|---|---|
| ✅ 已有 `fulltext.txt`（无下划线） | **18 篇** | 新批次 + strong-2007，**已 git 跟踪**，跳过 |
| ⚠️ 旧命名（已 tracked） | **2 篇** | `0001_b2fh-1957/extracted.txt`、`0003_fowler-1984/full_text.txt`——只改名，不重提 |
| ❌ 纯缺失（有 PDF） | **20 篇** | 19 篇 pdftotext 可提取（文本型）；**1 篇扫描型**（`0007_grevesse-sauval-1998`，pdftotext 仅 14 字符）——跳过并记录 |

- **环境**：`pdftotext` 可用（/opt/homebrew/bin/pdftotext）
- **git 约定**：`fulltext.txt`（无下划线）**被跟踪**（.gitignore 只忽略 `full_text.txt` 下划线版）——补齐后**入库**，与现有 18 个一致

## ⚠️ 铁律（用户要求）

1. **已有文本不重新提取**——凡是磁盘上已有 `fulltext.txt` / `full_text.txt` / `extracted.txt` 的篇目，**绝不重新跑 pdftotext**，只做名称统一
2. **提取内容正确性**：pdftotext 提取后抽查 2 篇对照 PDF 关键段落（数值/标题一致），防空提取/错页
3. **不改任何精读 md**——本任务只产生/重命名 `*.txt` 提取文件

## 1. 任务清单

### 步骤 1：旧命名改名（2 篇，不重提）

```bash
cd /Users/jcxs2014/Sites/HermesLocal/papers
git mv "03_stellar-nucleosynthesis/0001_b2fh-1957/extracted.txt"   "03_stellar-nucleosynthesis/0001_b2fh-1957/fulltext.txt"
git mv "03_stellar-nucleosynthesis/0003_fowler-1984/full_text.txt" "03_stellar-nucleosynthesis/0003_fowler-1984/fulltext.txt"
```

- 用 `git mv`（保留 rename 历史），不用 `mv`+`git add`
- 改名后验证内容没变：`git diff --stat 03_stellar-nucleosynthesis/0001_b2fh-1957/fulltext.txt` 应为 0（纯 rename）

### 步骤 2：缺失篇 pdftotext 提取（19 篇）

```bash
for d in <19 个篇目路径>; do
  pdf=$(ls "$d"/*.pdf | head -1)
  pdftotext "$pdf" "$d/fulltext.txt"
done
```

**19 篇清单**（02 起源域 7 + 03 核合成域 12）：
```
02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000
02_cosmic-ray-origins/0002_al-dargazelli-1996
02_cosmic-ray-origins/0003_gaisser-1990
02_cosmic-ray-origins/0004_blasi-2013
02_cosmic-ray-origins/0005_amato-2014
02_cosmic-ray-origins/0006_grenier-2015
02_cosmic-ray-origins/0007_biermann-1996
03_stellar-nucleosynthesis/0002_trimble-1975
03_stellar-nucleosynthesis/0004_wallerstein-1997
03_stellar-nucleosynthesis/0005_champagne-wiescher-1992
03_stellar-nucleosynthesis/0006_anders-grevesse
03_stellar-nucleosynthesis/0008_lodders-2003
03_stellar-nucleosynthesis/0009_asplund-2009-solar-composition
03_stellar-nucleosynthesis/0010_gies-lambert-1992
03_stellar-nucleosynthesis/0011_kewley-2001-starburst
03_stellar-nucleosynthesis/0012_dieterich-2014-h-burning-limit
03_stellar-nucleosynthesis/0013_bertone-hooper-2018
03_stellar-nucleosynthesis/0014_cameron-1968
03_stellar-nucleosynthesis/0015_kraft-1994
```

（实测各 PDF 可提取 30KB–613KB 文本，全为文本型）

### 步骤 3：扫描型跳过（1 篇）

- `03_stellar-nucleosynthesis/0007_grevesse-sauval-1998`——pdftotext 仅 14 字符（扫描版），**跳过**，在交付报告记录"需 OCR/视觉读取，暂缓"

## 2. 验证（对照原文铁律）

1. **每篇提取后字符数**：`wc -c <fulltext.txt>` 应 > 10,000（防空提取）；列出全部 19+2 篇的大小
2. **抽查 2 篇对照 PDF**：
   - `0004_blasi-2013`：`grep -c "diffusion\|acceleration\|10\^" fulltext.txt` 应 > 0，且与 PDF 标题/摘要首段一致
   - `0001_b2fh-1957`（改名篇）：`diff` 改名前后内容一致（git 层确认 0 变化）
3. **旧命名清理**：全库不再存在 `extracted.txt` / `full_text.txt`（除被忽略的临时文件）

## 3. 提交约定

```bash
git add 02_cosmic-ray-origins/*/fulltext.txt 03_stellar-nucleosynthesis/*/fulltext.txt 2>/dev/null
git add -A 03_stellar-nucleosynthesis/0001_b2fh-1957 03_stellar-nucleosynthesis/0003_fowler-1984  # git mv 的 rename
git commit -m "feat(papers): 全库 fulltext.txt 补齐（老库 19 篇 pdftotext 提取 + 2 篇改名统一）"
```

- **禁止** `git add -A` 全库（会带入无关改动）
- 提交信息可含 `[skip grep]` 不强制；`fulltext.txt` 是文本提取物，正常入库
- 若工作树有 Hermes 并发未提交改动，先 `git status` 确认，只 add 本任务的 txt 文件

## 4. 交付物

1. 19 篇新 `fulltext.txt`（各篇目录下）
2. 2 篇改名（extracted.txt/full_text.txt → fulltext.txt，git rename 保留）
3. 提取大小清单 + 抽查记录
4. 1 篇扫描型（grevesse-sauval-1998）标注"暂缓，需 OCR"

## 5. 完成标准（WorkBuddy 复验口径）

- 全库 38 篇中 **37 篇有 fulltext.txt**（grevesse-sauval 例外标注）
- 旧命名文件 0 残留
- 每篇提取 > 10KB；抽查 2 篇对照 PDF 一致
- git 提交干净，无无关文件混入
