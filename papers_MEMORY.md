# Papers 项目专属记忆库

> 本文件为 papers 项目专属记忆，git 可跟踪，无长度限制。
> 由 Hermes Agent 维护，每次更新需同步修改日期。

## 项目状态（2026-08-19 更新）

- **PAPERS**: 57 篇（域 01=7 / 02=20 / 03=24 / 04=6）
- **commit d0b58aa**（2026-08-18）：cavendish-millicharge-2026 入库，56篇基准
- **commit dfb771d/116afb9/7733f67/4cf1f44**（2026-08-19）：electric-accumulation-2026 入库 + 重建 + DS_Store 清理 + PDF 归档
- **check_density**: 57/57
- **verify_claim**: PASS=12/FAIL=0
- **audit**: 全部 29 项通过 ✅（2026-08-19）

---

## 篇数自动化（commit d0b58aa 确立）

```
正确流程：
  gen_index.py → update_counts.py --write → build_webapp.py --include-papers → audit.py

scripts/_meta.py：PAPER_COUNT / FILE_COUNT / TOPIC_COUNTS 全局计数源（勿手动改）
scripts/gen_index.py：自动写 INDEX.md + _meta.py
scripts/update_counts.py --write：读取 _meta.py → 更新 background/ 所有静态文案
```

**入库不再手动搜替计数——只需跑上述流程即可。**

---

## 收尾 Checklist（每次入库后必跑）

1. `git status --short`
2. `check_density N/N`（N=当前篇数）
3. `audit.py` → 0 FAIL
4. `verify_claim.sh` → FAIL=0
5. webapp rebuild 核数字
6. 根目录散文件 `ls *.pdf *.md`
7. 确认 `_meta.py` PAPER_COUNT 已刷新

---

## Commit 纪律教训（2026-08-19 总结）

1. **commit 前 `git ls-files <dir> | wc -l` 实际数文件数**，message 写"N文件"必须与实测吻合（本会话：报11实12，已纠正）
2. **`git add -f` 只加目标文件**，禁止加隐藏文件（.DS_Store），避免绕过 .gitignore（2026-08-19 实测：.DS_Store 进 commit 是因为用 `-f` 绕过了 ignore）
3. **总结列出所有 commit hash**，漏报即不完整（2026-08-19 漏了 `4cf1f44` 归档 PDF）

---

## DS_Store 陷阱（2026-08-19 更新）

- 每次 `git add` 后立即 `git rm --cached <path>` 移除误加的 .DS_Store，再 amend
- 多次 patch 导航块会累积重复 → 需 strip-all 再重建
- 子 agent 表格 frontmatter → 直接重写而非 patch

---

## 占位符门禁（实证 cf64bea/7d76a35）

- `{one_sentence}` / `{scientific_question}` / （按需填入）/ 仅模板 A/B/C 标题 → quality_matrix 不检 98/99 内容是否真有文字
- **冰山模式**：H1/导航/frontmatter 合规后即报"完成"，但 99/98 仍是空模板
- **规避方法**：99/98 完成后 `grep "按需填入|\{.*\}|^## 15\.[0-9]+ *$"` 必为 0（仅命中子标题不算占位）；commit 前 grep 占位符清单

---

## 表格列数检测 SOP（关键）

- 检测必须先 `line.replace(r'\|', 'X')` 把转义占位再算 `|` 数——否则误报率 100%
- 实证：1297 个表格，初版误报 92 处 → 转义处理后真问题仅 4 处
- 甄别：`|b|` 合法转义（绝对值）、`{xxx}` 占位符

---

## 审查与修复并行铁律

- **报告快照滞后**：审查与修复并行时报告落盘即可能过时，核验必须实测当前工作树（`git log` / file size / 实际内容）
- **任何报告/审查输出必带 git SHA + 时间戳**，让审阅者知道状态
- **不采信转述**：用户对脚本检测结果必复核（实证：92 处误报→用户指出→5 处真问题）

---

## Hermes vs WorkBuddy 双归属

- 并行会话可能做同一工作，报告时用 `git log -1 -- <file>` 区分归属
- "本会话提交了"必须附 commit hash，不能把别人 commit 算成自己的

---

## Papers 三教训（2026-08-16 实测）

1. **审查报告快照滞后**——核验必须实测当前工作树，不可信报告历史数字
2. **OCR 成功 ≠ 干净**——重 OCR 后必须 `grep` 论文标题确认正文起始行，删除错页前缀（eichler-1989 教训）
3. **命名不一致让自动审查误报**——统一命名是合规的一部分

---

## 前序教训（已整合入上方）

- **sections**：非路径A专属，豁免用 fulltext.txt 验证；分章文件名不能冒充 sections
- **综述补深度 SOP**：公式 `$$...$$` LaTeX，禁 Unicode 上下标；每薄弱章新增 §X.5 关键定量公式节；每篇 1 commit 每章独立 patch
- **工作区根 ≠ papers 根**：Hermes workspace=~/Sites/HermesLocal/；papers git 根=~/Sites/HermesLocal/papers/
- **清理带证据**：`git status --short` + `ls` 验证，不接受口头声称
- **用户复核纪律**：先看后报，先复核后分类

---

## 待办

- [ ] 01/02/03 跨篇综述融入 17 篇新文献（按主题插入小节非简单追加，1篇1commit），完成后重建+audit
- [ ] 背景知识库补全：已完成 ①②③；④key_values/glossary；⑤critique 补 13 篇

---

*最后更新：2026-08-19*
