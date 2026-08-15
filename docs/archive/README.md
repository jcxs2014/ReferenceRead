# docs/archive — 归档的执行指令

> **用途**：一次性/批次性执行指令的归档区。任务闭环（复验通过 + REVIEWS 记条）后从 `docs/` 根目录移入本目录，**git mv 保留提交历史**，根目录只保留常驻文档（指南/规范/备忘/模板）。
> **归档日期**：2026-08-15（13 份全部归档）

## 归档清单

| 文件 | 原任务 | 闭环状态 |
|---|---|---|
| `pages补齐执行指令.md` | 38 篇 frontmatter `pages` 补齐 | ✅ 38/38（含回归修复链，见 TROUBLESHOOTING A2） |
| `fulltext补齐执行指令.md` | 老库 fulltext.txt 统一补齐 | ✅ 38/38（含 2 篇 OCR） |
| `公式LaTeX化执行指令.md` | Unicode 数学字符 → LaTeX（两轮） | ✅ 全库四域完成 |
| `公式上下标LaTeX化执行指令.md` | Unicode 上下标 → LaTeX | ✅ 四域完成 |
| `公式割裂修复执行指令.md` | 公式格式割裂修复 | ✅ 460 处修复 |
| `公式LaTeX化批量执行说明.md` | 批量转换验证流程细则 | ✅（方法被 READING_INSTRUCTIONS §7.1 引用） |
| `子节镜像批1执行指令.md` | 4 篇长综述路径 A 示范 | ✅ REVIEWS #25（含补内容误报确认） |
| `子节镜像批2执行指令.md` | 20 篇长文献路径 A | ✅ REVIEWS #26（20/20） |
| `子节镜像批2进度与执行手册.md` | 批 2 执行进度跟踪 | ✅ 收官（原 untracked，随批 2 闭环归档） |
| `批1补内容执行指令.md` | blasi/grenier FACT 归位 | ✅ 复验确认误报（内容全在） |
| `批1修复执行指令.md` | grenier 层级/占位符 + bhattacharjee 子节号 | ✅ 覆盖率恢复 100% |
| `议题3实施指令.md` | quality_matrix 子节统计 + 97 块 | ✅ 1beb068/f0e139a |
| `Unicode公式检查转换执行指令.md` | 批改造引入的 Unicode 回归 | ✅ ~243 处，残留 0 |

## 通用知识去向

归档指令中的**通用方法论**已沉淀至常驻文档，不因归档丢失：

- 执行指令的**通用结构**（铁律/步骤/验证/提交/完成标准/复验口径）→ `docs/执行指令模板.md`
- **踩坑与修复**（frontmatter 分隔符、citations YAML、Unicode 回归、FACT 判定、范围声明复算）→ `docs/TROUBLESHOOTING.md` A2–A6
- **规范**（公式 LaTeX、路径 A 子节镜像、页数字段）→ `docs/READING_INSTRUCTIONS.md`
- **设计决策**（超长阈值、批次决策、97 块）→ `docs/精读深度扩充设计备忘.md`

## 恢复/复用

- 新任务需要相似步骤：参照 `docs/执行指令模板.md` 重建，不直接改归档副本
- 存量按需拓展某篇时：参照 `子节镜像批1执行指令.md` 的提取/改造/验证命令
- 若需回滚归档（恢复至根目录）：`git mv docs/archive/<file> docs/<file>`（需保持 git 追踪）

## audit/ 子目录（2026-08-15 追加归档）

- **`audit/`**（18 个 .tsv）：公式 LaTeX 化两轮（r1/r2）与割裂修复的**逐行转换审计清单**（audit_背景/核合成/起源/传播 各域 × r1/r2 + gap + fix_audit + supsub_audit）——任务已闭环（REVIEWS 有档、残留 0），tsv 仅作追溯明细，从 webapp/ 移入。
- 构建产物（registry.json / glossary.json / search_index.json / manifest.json / icon-*.png / apple-touch-icon.png / interactive.html）**不入库**（webapp/.gitignore），由构建链 `build_registry → build_glossary → build_search_index → build_pwa → build_webapp` 再生成。
