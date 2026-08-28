# Papers 项目长期记忆

> 本目录是 papers 项目的**持久记忆系统**，用普通文件管理，替代内置 memory 工具。
> 会话启动约定：每次新会话先读本文件了解项目背景。

## 项目身份

- **项目路径**：`Documents/Works/ReferenceRead`（独立 git 仓库）
- **主题**：天体物理文献深度精读（宇宙线传播 / 起源于 / 恒星核合成 / 实验观测）
- **主题域**：`01_propagation` / `02_origin` / `03_nucleosynthesis` / `04_experiments`
- **当前规模**：**57 篇**（域 01=7 / 02=20 / 03=24 / 04=6）
- **三层结构**：主题域 → 单篇（`编号_作者-年份/`）→ `literature_analysis/`

## 精读流水线

```
00_overview → 分章（01-NN） → 98_vocabulary → 99_final_summary
```
- 顶层文档：`README.md` / `INDEX.md` / `READING_INSTRUCTIONS.md` + `background/` 知识库
- `docs/`：质量审查报告（QUALITY_AUDIT_*.md）、覆盖度审查（COVERAGE_REVIEW_*.md）
- `scripts/`：门禁脚本（check_density.py / gen_quality_check.py / verify_claim.sh）

## 双 agent 分工（铁律）

- **Hermes = 执行方**：精读、新增文献、索引维护、提交前自审
- **WorkBuddy / 审查方 = 审查/复验方**：独立实测核验，不执行文献改动
- **核心要求**：执行方必须 self-check 做在前面，不能依赖审查方兜底

## 质量门禁（接手后必过）

1. `check_density.py` — 55/55 通过（或其他更新）
2. `verify_claim.sh` — PASS=12 / FAIL=0
3. `grep "按需填入|\{.*\}|^## 15\.[0-9]+ *$"` — 占位符必为 0
4. `grep "10\^|10⁻|π⁰|e⁺e⁻"` — Unicode 数学符号必为 0

## 入库 / 计数自动化（勿手动 patch）

```
python3 scripts/gen_index.py                    # 重写 INDEX.md + 生成 _meta.py
python3 scripts/update_counts.py --write       # 更新 background/ 静态篇数文案
python3 webapp/scripts/build_webapp.py --include-papers
python3 webapp/scripts/audit.py
```
红线：不得手动搜索替换 `INDEX.md` / `background/` 计数。

## 提交纪律

- 禁 `git add -A` / `git add .`；精确 `git add <paths>`
- commit message 写"N files"必须与 `git ls-files` 实测吻合
- `.DS_Store` 等无关文件不得进入提交

## 关键教训（长期记忆）

### 并行审查铁律
- **报告快照滞后**：审查与修复并行时报告落盘即可能过时
- **任何报告必带 git SHA + 时间戳**
- **不采信转述**：实测当前工作树

### OCR 教训
- OCR 成功 ≠ 干净——重 OCR 后必须 `grep` 论文标题确认正文起始行
- 实证：eichler-1989 首 41 行为蛋白折叠论文错页混入

### 公式写作教训
- 双重反斜杠：`\\chi` → `\chi`；`\\\` → `\,`
- 空行 `\\ ` 是换行命令，非空格；应输 `\,`

### 占位符门禁
- 98/99 占位符：`{one_sentence}` / `{scientific_question}` / （按需填入）
- `grep "按需填入|\{.*\}|^## 15\.[0-9]+ *$"` 必为 0

### 表格列数检测
- 先 `line.replace(r'\|', 'X')` 转义再算 `|` 数，否则误报率 100%

## 记忆系统本身

- 长期约定 → 更新本文件，按节归类、保持精炼
- 当日事项 → append 到 `YYYY-MM-DD.md`（追加，不覆盖历史）
- 用 Write/Edit 工具维护，勿用内置 memory 工具写大量内容