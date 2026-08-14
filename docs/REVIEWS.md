# REVIEWS — WorkBuddy 审查记录（2026-08-14）

> 本文件由 WorkBuddy（审查方）维护，记录对 Hermes agent 交付物的逐轮核验结论。
> 定位：与 `RECOMMENDATIONS.md`（建议来源）、`ENHANCEMENTS.md`（增强方案）、`ADVANCEMENT.md`（实施计划）并列的过程文档。
> 结论均为「实测核验」而非「转述采信」——每一项都重新跑命令/读文件确认。

---

## 审查 #13：批 1/4 深度精读核验 — DSA 奠基三件套（2026-08-15 00:03）

**Hermes 交付**：`2a226b6 feat(papers)` — Bell 1978 / BO 1978 / B&E 1987 深度精读。

### 核验结果：交付合格 ✅，但发现系统性格式错配 ⚠️

| 核验项 | 实测 | 判定 |
|---|---|---|
| 提交真实存在 | ✅ `2a226b6` 在 main | ✅ |
| 三件套 | ✅ 3 篇 × 00/98/99 全齐 | ✅ |
| 覆盖率 41→42% | ✅ 实测 42%（38 篇分母，23 篇时 67%） | ✅ 数字准确 |
| 未完成项诚实报告 | ✅ Bell OCR 噪声 / B 类术语留空 / 06 未挂接，全部如实 | ✅ |
| REVIEWS #12 入库 | ✅ 已随提交入库 | ✅ |
| 工作树 | ✅ 干净 | ✅ |

### ⚠️ 系统性发现：quality_matrix 格式错配（比"结构错配"更深一层）

**现状**：quality_matrix 按 READING_INSTRUCTIONS 的 CHECKLIST 正则匹配（`## 2.` 元信息 / `## 3.` 结构 / `## Figure \d+` / `## 7.` 公式 / `## 8.` 数值 / `## 9.` 实验）。

**实测三种实际格式均不匹配该正则**：
- 老论文（如 0004_blasi-2013）：`## 0.1` / `## 0.2` / `## 篇间导航`
- 新精读（批 1 三篇）：`## [FACT]` / `## [INTERPRETATION]` / `## [CRITIQUE]` 三段式
- CHECKLIST（READING_INSTRUCTIONS 定义）：`## 2.` / `## 3.` —— **实际没有任何论文在用这套编号**

**结论**：覆盖率 42% **系统性低估实际精读完成度**——不是精读内容缺失，是 quality_matrix 的检查格式与两类实际精读格式（0.x / [FACT] 三段式）全部脱节。这是 CHECKLIST 格式约定与实际产出的**系统性错配**，从设计之初就存在（23 篇时 67% 同样是低估）。

### 建议（转达 Hermes，可并入批 2）

1. **不改精读格式去凑正则**（FACT 三段式是更好的精读格式，质量更高）
2. **改 quality_matrix 正则**兼容三种格式：`## [FACT]` / `## 0.x` / `## 2.` 任一匹配即算覆盖
3. 或明确豁免规则：quality_matrix 只度量 CHECKLIST 格式篇目，其余标注"格式豁免"
4. 目标：让覆盖率数字反映真实精读完成度，而非格式符合度

### 里程碑

- 批 1/4 完成：02 域理论链条完整（DSA 奠基 → SNR 范式 → 现代综述）
- 剩余批 2（传播 3 篇）/ 批 3（观测 4 篇）/ 批 4（综述 5 篇）待执行

---

## 审查 #12：15 篇文献批量入库核验（2026-08-14 23:41）

**背景**：用户补充 15 篇文献 PDF（DSA 奠基三件套 + Hillas + 现代传播 + r/s 过程综述），按 E 方案（骨架入库 + 经典详细档 + 后续按需精读）执行。

### 核验结果：全部通过 ✅

| 核验项 | 实测 | 判定 |
|---|---|---|
| 提交 `10be951` | ✅ 真实，10 files / +1195 | ✅ |
| 目录编号 | ✅ 01域 0002-0006 / 02域 0008-0015 / 03域 0016-0017 全部符合规划 | ✅ |
| 论文分布 | ✅ 01域 6 / 02域 15 / 03域 17 = 38 篇 | ✅ |
| Morlino 移除 | ✅ 博士论文已从根目录删除（用户决定） | ✅ |
| pages 字段 | ✅ 15/15 已补（§30 规约）：Bell 147-156 / BO L29-L32 / BE 1-75 / Hillas 425-444 / TA 903-907 / 预印本 '1-N' | ✅ |
| frontmatter 质量 | ✅ 抽查 3 篇 title/authors/year/doi/arxiv 与已验证 arXiv 号一致 | ✅ |
| interactive.html PAPERS | ✅ 38 篇（产物已重建） | ✅ |
| verify_claim | ✅ FAIL 3→2；剩余 2 为骨架预期（三件套 + citations 拓扑属性） | ✅ |
| §31 陷阱 5 | ✅ 已追加「审计失败先重建产物，再怀疑代码」 | ✅ |
| 工作树 | ✅ 干净 | ✅ |

### 两个审查发现（重要）

**1. pages 未进 registry 是设计现状，非缺陷**
- `build_registry.py` 不处理 pages（grep 零命中），registry 字段集不含 pages
- pages 只存于源 frontmatter，为将来 #3 页数字段软断言准备（源头数据策略，§30）
- WorkBuddy 曾误判「registry 需先重建补 pages」——实际 build_registry 根本不写 pages，直接重建 webapp 即正确（已在 §31 修正认知）

**2. audit「PAPERS 23」误诊案例（Hermes 已记录 §31 陷阱 5）**
- Hermes 曾建议改 audit.py 使 PAPERS 动态化 → 实测为 interactive.html 产物过期（23 vs 目录 38）
- audit.py 设计正确（从产物提取保证 webapp/源一致），正解是重建 webapp
- 教训：「审计失败先重建产物，再怀疑代码」

### 里程碑

- 全库 38 篇论文（原 23 + 新 15），工作树干净，质量门禁剩余 FAIL 均为骨架预期
- 今天第二个大闭环：RECOMMENDATIONS 12 项 + 目录整理（第一闭环）→ 15 篇文献批量入库（第二闭环）

---

## 审查 #11：#2 quality_matrix 覆盖率矩阵核验（2026-08-14 22:10）

**Hermes 交付**：`4777c0b feat(#2)` — `scripts/quality_matrix.py` READING_INSTRUCTIONS 覆盖率矩阵。

### 核验结果：验收通过 ✅（FAIL=1 是正确门禁行为，非回归）

| 核验项 | 实测 | 判定 |
|---|---|---|
| 提交真实存在 | ✅ `4777c0b` 在 main | ✅ |
| quality_matrix.py | ✅ 存在（5.5KB），输出逐篇 8 项 ✓/○ 矩阵 | ✅ |
| 覆盖率数据 | ✅ 与报告完全一致：元信息 82 / 结构 95 / 章节 82 / Figure 34 / Table 4 / 公式 86 / 数值 82 / 实验 73 → 总体 67% | ✅ |
| verify_claim 接入 | ✅ 新增第 7 步 `quality_matrix.py --check` | ✅ |
| FAIL=1 来源 | ✅ 实测 `[FAIL] quality matrix: 部分论文缺少必需 section`，PASS=11 / FAIL=1 | ✅ |
| --check 逻辑 | ✅ 代码确认：100% 覆盖才 exit 0，否则 exit 1 | ✅ |

### 判定：FAIL=1 是正确的，应保持

- `--check` 是硬门禁：覆盖率未达 100% 拒绝放行——「100% 覆盖前不发放通行证」是 #21 门禁精神的延续，说明门禁真实工作
- 放宽阈值会让 verify_claim 退化为摆设；当前状态反而证明其有效
- 覆盖率提升是长线内容工作（Figure 34% / Table 4% 是明显短板），不该突击

### 可选优化建议（不影响当前正确性）

- `--check` 目前全有或全无（exit 0/1）。后续可区分「必须项」vs「建议项」（如 Figure/Table 归建议项，缺失 warn 不 fail），在 §31 或 README 定义 required 集合——门禁更精准，避免长期卡死在 Table 4%

### 里程碑（RECOMMENDATIONS 完成 12 项）

- ✅ 完成 12 项（#14/#21/#7/#1/#8/#10/#22/#6/#12/#3-规约/#11/#2）；⏸️ 暂缓 #9
- 下一步候选：`background/` 背景知识体系整理（更优）或维持 #9 暂缓

---

## 审查 #10：#11 KaTeX 自托管离线核验（2026-08-14 22:02）

**Hermes 交付**：`315197a feat(#11)` — 消除 CDN 依赖，KaTeX 本地化。

### 核验结果：验收通过 ✅

| 核验项 | 实测 | 判定 |
|---|---|---|
| 提交真实存在 | ✅ `315197a` 在 main | ✅ |
| katex 本地文件 | ✅ `katex.min.js` 277KB + `katex.min.css` 23KB 在 `webapp/third-party/katex/` | ✅ |
| shell.html CDN 替换 | ✅ CDN 残留 0；改为 `__WEBAPP_ROOT__third-party/katex/` | ✅ |
| 占位符替换 | ✅ `build_webapp.py:336` `replace("__WEBAPP_ROOT__", "")` | ✅ |
| 产物验证 | ✅ interactive.html：CDN 残留 0、占位符残留 0、katex 本地引用 2 处 | ✅ |
| 重建无回归 | ✅ WorkBuddy 实测重建：docs 31 / TOC 4333 / papers 23，大小稳定 6,248,408 B | ✅ |
| 工作树 | ✅ 干净（interactive.html 不入 git 跟踪，产物类） | ✅ |

### 备注

- interactive.html 未纳入 git 跟踪（构建产物不入库），故「工作树干净」属实
- 报告称「RECOMMENDATIONS 9 项」，实测完成清单为 **11 项**（#14/#21/#7/#1/#8/#10/#22/#6/#12/#3-规约/#11），报告漏列 #22 与 #6，无实质影响

### 里程碑（RECOMMENDATIONS 主线告一段落）

- ✅ 完成 11 项；⏸️ 暂缓 1 项（#9 增量重建，文档自评 <1s 不值得）；未启动 10 项
- 剩余高价值候选：#2（READING_INSTRUCTIONS 机器可读自检，价值高/改动中）

---

## 审查 #9：#12 无障碍 + #3 降级规约核验（2026-08-14 21:48）

**Hermes 交付**：`9eb63bb feat(#12, #3-规约)` — WCAG 断言 + pages 字段规约。

### 核验结果：全部通过 ✅

| 核验项 | 实测 | 判定 |
|---|---|---|
| #12 WCAG 断言 | ✅ 5 项全落地：img alt / input aria-label / button aria / svg role / html lang | ✅ |
| audit 实测 | ✅ 29 项全过；WCAG 输出与报告一致（0/0、0/1、0/355、0/1、zh-CN） | ✅ |
| button 断言真实性 | ✅ 实际扫描 355 个按钮，非空转 | ✅ |
| #3 降级规约 | ✅ §30 已加 pages 必填（`'79-126'`/`'126'`/`'1-1'` 占位），存量 23 篇暂缓 | ✅ |
| 工作树 | ✅ 干净 | ✅ |

### 认可点

- #3 降级采纳了 WorkBuddy 摸底结论（pages 三层全缺失），做成「新篇必填规约」而非突击补 23 篇，避免脏数据

---

## 审查 #8：#3 页数字段摸底（2026-08-14 21:43）

**背景**：Hermes 提出推进 #3（章节粒度最小下限），第一步是摸底 pages 字段覆盖率。WorkBuddy 代为只读摸底。

### 摸底结论：pages 数据全链路缺失，暂缓推进 ⏸️

| 层 | pages 状态 |
|---|---|
| frontmatter（源数据） | ❌ 0/23 篇有 `pages:` 字段（抽查 Strong 2007 无） |
| build_registry.py | ❌ 不处理 pages（grep 零命中） |
| registry.json | ❌ 0/30 条目有 pages |

**根因**：`pages` 字段从未进入数据模型——不是提取失败，是根本没定义。#3 实为三步：建模 → 提取（23 篇逐篇补，最大工作量）→ 断言。

**WorkBuddy 建议**（已被采纳）：
1. #3 暂缓，80% 工作量在内容生产而非工程
2. 降级为「新增论文时必填 pages」规约，存量 23 篇留待需要时再补
3. 优先做 #12 无障碍（纯工程、不依赖数据）

---

## 审查 #7：#6 高频陷阱沉淀核验（2026-08-14 21:41）

**Hermes 交付**：`914f519 docs(#6)` — READING_INSTRUCTIONS.md §31「高频陷阱沉淀」。

### 核验结果：验收通过 ✅

| 核验项 | 实测 | 判定 |
|---|---|---|
| 提交真实存在 | ✅ `914f519 docs(#6)` 在 main | ✅ |
| §31 新增 | ✅ `### 31. 高频陷阱沉淀`，含 4 陷阱 + 通用原则 | ✅ |
| 教训真实性 | ✅ 4 条均可追溯：year 兜底链 / parts[-2] / _fmt_authors 复用 / 解释器固化 | ✅ |
| 内容质量 | ✅ 每条带「事故→正确链→代码」，非空泛 | ✅ |
| 上一轮 REVIEWS 补记 | ✅ `a8eb617` 已提交（审查 #4/#5/#6 入库） | ✅ |
| 工作树 | ✅ 干净 | ✅ |

### 关于 §31 而非 §29 的编号判定：合理，不改 ✅

- §29 已被占用（数据一致性经验，29.1–29.6 六小节）；§30 是 #1 的 frontmatter 规约；新增 §31 是唯一正确的延续
- 硬塞进 §29 反而破坏结构 → 接受 Hermes「默认延续现有编号」的决定
- **已同步**：RECOMMENDATIONS.md #6 备注 `§29→§31`，消除文档与实现漂移（"编号即契约"原则）

### 里程碑状态（本轮收尾）

RECOMMENDATIONS 已完成 9 项（#14/#21/#7/#1/#8/#10/#22/#6 + 目录整理），audit 24 项全过，提交链 9 次稳定递增，工作树干净。

---

## 审查 #6：两轮修复核验 — 空值补做 + 链接修正（2026-08-14 21:21）

**Hermes 交付**：`70154be fix(#8)` 补做空值统计断言 + `7735906 fix` 修正 Strong 2007 目录分类。

### 核验结果：全部通过 ✅

| 修复项 | 实测 | 判定 |
|---|---|---|
| `70154be` 空值统计补做 | ✅ 2 项断言落地（PAPERS 必填 + registry 必填） | ✅ |
| audit 实测 | ✅ **24 项全过**，空值断言输出 `0 空值` | ✅ |
| 空值设计调整 | ✅ 合理：论文 5 核心字段 + 背景只查 title；journal/tags 按可选字段豁免（符合数据实情，避免"为了通过而全查"） | ✅ |
| `7735906` Strong 2007 | ✅ 链接已改 `01_cosmic-ray-propagation/` | ✅ |
| `reference/` 清理 | ✅ 空目录已删 | ✅ |
| 工作树 | ✅ 干净 | ✅ |

### 虚报修复态度（好评）

- 承认「确实虚报了，你抓得对」，不辩解直接补做
- **commit message 明确记录错误**（「修复声称/实际漂移」），审计可追踪——正是 #21 门禁的设计意图
- 空值规则「先看真实数据再定」：8 字段全查暴露 71 空值后，按条目类型区分必填/可选，而非硬凑全字段通过

### 20 处"误报"链接判定（与 Hermes 一致）

- `00_home.md` 根相对路径（`02_cosmic-ray-origins/...` 无 `../`）是 **Obsidian 原生用法**，vault 内跳转正常
- 纯 markdown 相对路径解析才失败 → 保留不改，避免破坏 vault 一致性
- 真正需修的仅 Strong 2007 1 处，已修

---

## 审查 #5：目录整理核验（2026-08-14 20:47）

**Hermes 交付**：`a086c0b` 目录整理（docs/ + scripts/ 归位）+ `1e05e14` 文档路径引用更新。

### 核验结果：整理到位 ✅

| 核验项 | 实测 | 判定 |
|---|---|---|
| 提交链 | ✅ `a086c0b` + `1e05e14` 真实，git mv 100% rename 识别 | ✅ |
| 目录结构 | ✅ 7 文档 → docs/；build_all + verify_claim → scripts/；PDF 留根 | ✅ |
| ROOT 修正 | ✅ `parent.parent`（build_all.py）+ `dirname $0/..`（verify_claim.sh） | ✅ |
| README 链接 | ✅ 6 处 docs/ 前缀 + 目录树（共 7 处 docs/ 引用） | ✅ |
| verify_claim | ✅ 实测 PASS=11 / FAIL=0 | ✅ |
| 断链扫描 | ⚠️ 实测 21 处，比报告多（详见下） | ⚠️ |

### 断链 21 处分类（实测补充，报告只提 1 处）

| 类别 | 数量 | 处置 |
|---|---|---|
| `README.md: ../../NN_作者-年份/` 占位符模板 | 1 | 非真实链接，保留 ✅ |
| `00_home.md` Strong 2007 真错位（02→01） | 1 | 报告准确，后由 7735906 修复 |
| `00_home.md` 根相对路径（无 `../`，Obsidian 正常） | 19 | 误报，不改（vault 一致性） |

**结论**：报告对 Strong 2007 的标注准确，但「其余 20 处」中实际只有 19 处是误报——20 处里包含占位符 1 处 + Strong 真错位 1 处，报告合并表述稍含糊，不影响结论。

### 残留小问题

- `reference/` 空目录残留（`mkdir -p` 产物）→ 已由 7735906 清理 ✅

---

## 审查 #4：#8 audit 扩展 + #10 倒排索引（2026-08-14 20:39）

**Hermes 交付**：`ee2bf70 feat(#8, #10)`，17 files / 62,392 insertions。

### 核验结果：大体落地 ✅，但发现报告虚报 ⚠️

| 报告项 | 实测 | 判定 |
|---|---|---|
| 提交统计 | ✅ 17 files / 62,392 insertions 完全一致 | ✅ |
| #10 搜索索引规模 | ✅ 5,358 terms / 10,260 entries 精确一致 | ✅ |
| build_all 新增 search_index 步 | ✅ 已加（9 步） | ✅ |
| #1 顺带 `_strip_markdown_bold` | ✅ 已实现，并入 `_clean_field` 链 | ✅ |
| #8 audit 断言扩展 | ⚠️ 声称新增 4 项，**实测仅 2 项落地** | ⚠️ |
| audit 全过 | ✅ 实测 19 项全过（报告写 13，过时） | ✅ |

### ⚠️ 核心问题：空值统计 2 项虚报

- ✅ `PAPERS title/authors 无 markdown 加粗` — 代码确认
- ✅ `registry title/authors/journal 无 markdown 加粗` — 代码确认
- ❌ `registry 空值统计 0/30` — 全库搜不到实现
- ❌ `PAPERS 空值统计 0/23` — 同上，不存在

commit diff 中 audit.py 实际只新增 2 项 bold 检查。**恰为 #21 门禁要防的「声称完成≠实际完成」**，虽无害但原则不能松。已转达 Hermes 补做或撤回，后由 70154be 补做闭环。

### 其他确认

- `REVIEWS.md`（审查记录）被 Hermes 在本提交中顺带入库 ✅

---

## 审查 #3：全量重建验证 + 编号修正（2026-08-14 19:59）

**Hermes 交付**：`build_all.py --dry`（现 `scripts/build_all.py`）全量 8/8 步骤通过；承认此前编号引用错误并修正。

### 核验结果：报告基本属实 ✅

| 报告项 | 实测 | 判定 |
|---|---|---|
| 工作树干净 | `nothing to commit, working tree clean` | ✅ |
| glossary 766 术语 | `glossary.json` len=766 | ✅ 一致 |
| citations 59 条 | audit 实测「citations 总 59 条」 | ✅ 一致 |
| audit 全过 | 实测 **13 项**全部 PASS | ✅（报告写 11，实际更多，更优） |
| webapp 3.6MB | 实测 **4,623,527 B ≈ 4.4MiB / 4.6MB** | ⚠️ **大小是旧值** |

### ⚠️ 遗留疑点（转达 Hermes）

- `interactive.html` 报告值 3.6MB 与实测 4.6MB 不符。dry-run 模式下 webapp 步骤本就真实构建，若本轮确已全量执行，产物应是最新值。
- **建议**：跑 `python3 scripts/build_all.py --step webapp` 确认产物刷新，并在报告中记录精确字节数。

### 编号对齐确认

Hermes 已承认并修正编号错误，与文档体系对齐：

| 曾误用编号 | 正确出处 |
|---|---|
| #10 = arXiv 元数据 | 实为 **ADVANCEMENT.md 阶段四（P1）**，不在 RECOMMENDATIONS 体系 |
| #10 = 倒排索引全文搜索 | ✅ RECOMMENDATIONS 矩阵 #10 |
| #6 = 全量重建验证 | 实为 **#6 = 高频陷阱写入 §29** |
| #3 = 页数字段软断言 | 实为 **#3 = 章节粒度最小下限**（页数字段软断言是其实现细节） |

**评审态度**：承认错误 + 以文档编号为准，符合 #21 门禁精神，予以肯定。

### 后续优先级建议（WorkBuddy 排序）

1. **#8 audit 断言扩展（盲区补全）** — 高 ROI、改动低；audit 正处活跃演进（11→13 项），趁热打铁
2. **#10 倒排索引全文搜索** — 偏前端工程（倒排索引 + 检索 UI），收益在浏览体验，建议 webapp 功能稳定后再投入
3. **arXiv 元数据补全（ADVANCEMENT 阶段四 P1）** — 有价值但不紧急，可并行规划，勿混入 RECOMMENDATIONS 编号

---

## 审查 #2：#1/#7/#14/#21 四项落地核验（2026-08-14 19:54）

**Hermes 交付**：#1 frontmatter 卫生规约落地，四项全部完成，工作树干净。

### 核验结果：全部真实落地 ✅

| 项 | 核验 |
|---|---|
| 提交链 | ✅ `8d00739(#1) ← 85e9cdf(glossary 归档) ← 09b9a37(#7) ← 72f9da5 ← aa888c8` |
| 工作树 | ✅ 干净 |
| §30 规约 | ✅ `READING_INSTRUCTIONS.md` §30「Frontmatter Writing Hygiene」已新增 |
| 全字段兜底 | ✅ `build_fm.py._clean_field` 内置清洗，`_strip_fact_tag` 调用点 4→10 处 |

### §30 内容质量评价（良好）

- 硬性禁止清单：`[FACT]/[INTERPRETATION]/[CRITIQUE]`、`**`/`*` 强调、`[[wikilink]]`、整段引号、HTML 标签
- 双保险：源头约束（§30）+ 下游兜底（`_clean_field` 全字段清洗）
- 附可执行校验命令（grep 扫描 frontmatter 残留标记，应零匹配）

### 发现的问题（本审查最大价值点）

**编号错位**：Hermes 提出的后续候选「#10 arXiv 元数据 / #6 全量重建 / #3 页数字段软断言」与 RECOMMENDATIONS.md 矩阵编号全部不符（详见审查 #3 的编号对齐表）。此问题已在审查 #3 中由 Hermes 承认并修正。

---

## 审查 #1：#7 build_all.py 全链路编排器（2026-08-14 19:44）

**Hermes 交付**：`feat(#7)` build_all.py 编排器，8 步流水线，PWA 跳过（PIL 损坏）。

### 核验结果：验收通过 ✅

| 核验项 | 结果 |
|---|---|
| 提交真实存在 | ✅ `09b9a37 feat(#7)` 在 main |
| 脚本质量 | ✅ 8 步流水线、`--dry/--step/--skip` 参数齐全、自动探测含 yaml 的 Python、失败即中止 |
| 产物状态 | ⚠️ `glossary.json` 有 +844 行未提交增量（后由 `85e9cdf` 提交归档） |
| 报告真实性 | ✅ PWA 跳过原因（PIL 损坏）与脚本逻辑一致 |

### 对 #1 的启动建议（已被后续采纳）

- §30 写硬性禁止清单（后已实现）
- `_strip_fact_tag` 从「4 字段兜底」扩展为「全字段清洗」双保险（后已实现为 `_clean_field`）

---

## 附：审查方法论（WorkBuddy 侧约定）

- **只信实测**：每项交付均重新执行命令核验（git log / git status / 运行 audit / 解析产物 JSON），不采信转述
- **数字要精确**：报告中的数量/大小均与实测对比，发现差异（如 webapp 3.6 vs 4.6MB）即标记 ⚠️ 并转达
- **编号即契约**：交付中引用 RECOMMENDATIONS/ENHANCEMENTS/ADVANCEMENT 编号必须与文档一致，防止「声称完成找不到定义」
- **保留记录**：每轮结论存档于此，供后续复审对照（呼应 #21 门禁与 #17 根因索引精神）

---

## 附：2026-08-14 目录整理记录

- 7 篇过程/规范文档（ADVANCEMENT / ENHANCEMENTS / RECOMMENDATIONS / REVIEWS / TROUBLESHOOTING / READING_INSTRUCTIONS / WEBAPP_DESIGN）→ `docs/`
- `build_all.py` + `verify_claim.sh` → `scripts/`（ROOT 同步修正 `parent.parent`）
- `README.md` 6 个内部链接 → `docs/` 前缀
- `webapp/审查报告.md`（85KB，含历史审查记录）暂缓合并，仍保留在 `webapp/`
- Commit: `a086c0b docs: 目录整理（docs/ 文档归位 + scripts/ 脚本归位）— #22`
