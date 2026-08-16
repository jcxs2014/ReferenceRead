# 故障排除与修复记录（Troubleshooting Log）

> **用途**：记录工作流中真实遇到的故障、根因、修复方案、防护措施。
> **三类内容**：(1) 文献阅读工作流故障；(2) 网页设计/构建工作流故障；(3) 跨流程数据一致性故障。
> **与已有文档的关系**：
> - 精读规范 → `READING_INSTRUCTIONS.md`（28 节精读规范 + 第 29 节数据一致性经验）
> - 网页设计 → `WEBAPP_DESIGN.md`（架构与实现）
> - 进阶方案 → `ADVANCEMENT.md`（路线图）
> - 增强项检查表 → `ENHANCEMENTS.md`（待办 P0/P1/P2）
> - **本文件**：补完"踩坑"维度——告诉后来者**坏在那里、怎么排、修完后怎么拦**。
> 维护原则：每次故障修复后**当批**追加到本文件；每年归并一次旧条目（保留教训性，去除时效性）。

---

## A. 文献阅读工作流故障

### A1. 子智能体把 `[FACT]` 信息分级标记误写进 frontmatter 元数据

**发生时间**：2026-08-14，corpus 扩展批次（Cameron 1968 / Kraft 1994 入库）

**症状**：
- webapp 论文图谱节点显示 `A. G. W. Cameron [fact] (1968)`（label 残留 `[fact]` 小写）
- frontmatter 多个字段值结尾带 `[FACT]`：`title: A New Table of Abundances of the Elements in the Solar System [FACT]`、`authors: A. G. W. Cameron [FACT]`、`journal: ... [FACT]`、`doi: 未提供 [FACT]`
- 共 4 篇被污染：0014_cameron-1968（4 字段）、0006_grenier-2015（abstract 内 1 处）

**根因**：
- 精读流水线（子智能体）从 98_vocabulary.md 等分析文件抽取字段时，**把正文里的 `[FACT]` 标记当作值的一部分拷进 frontmatter**
- build_fm.py 把这些值透传给 registry
- build_webapp.py 用 `_title_case` 把 `[FACT]` 转成小写 `[fact]`（首字母大写规则）

**修复**：
1. 手工清洗：正则 `\s*\[(FACT|INTERPRETATION|CRITIQUE)\]\s*` → 替换为空，扫 23 篇 frontmatter 闭区间（`---` 之间）所有字段值
2. 防御写入：`webapp/build_fm.py` 新增 `_strip_fact_tag(val)` 助手，fm 构造处对 title/authors/journal/doi/keywords/abstract 全部应用
3. 检测漏网：`webapp/audit.py` 新增断言 `附4: label 不含 [FACT/INTERPRETATION/CRITIQUE] 残留`

**防护**：
- build 入口：build_fm.py 写入时清洗 → 不会再污染
- 检测出口：audit 18 条断言，新条会拒绝通过
- 验收门禁：headless DOM 验证 + audit + git push 三重门禁

**复盘教训**：
精读流水线写 frontmatter 时**只应取干净字段值**，不能把分析文档的语义标记（[FACT] 等）误混进元数据。同类问题在 READING_INSTRUCTIONS 第 29 节"数据一致性经验"中已作为"派生文档只引用不重写"规则延伸。

---

### A2. frontmatter 首尾 `---` 分隔符误删回归链（pages 补齐事件）

**发生时间**：2026-08-15，pages 补齐批次

**症状**：Obsidian 属性面板不渲染（37/38 篇 00_overview YAML 不闭合）；`c746689` 声称修复后仍有 27/37 篇只补了开头。

**根因**（两次同源 bug）：
- `1ad9840`：执行侧插 pages 时误删 frontmatter 首尾 `---`（37/38 篇）
- `c746689`：修复脚本**先插开头 `---`，再查"正文前已有 `---`"时把刚插的开头当结尾证据** → 跳过补结尾
- WorkBuddy 首修尝试也有同类 bug（`is_fm_line` 把 `---` 当正文行 → 双 `---`），已 git checkout 回滚，改出指令

**修复**：`22ec1f1`（27 篇补结尾，纯 `+---`、diff 纯净、幂等）

**防护/复验判定（最终版）**：frontmatter 完整性 = `head -1 == "---"` **且** 正文第一行前 `---` 数 ≥ 2。**勿用**"正文前含 `---`"（把开头当结尾→假阳性 38/38）、**勿用**"正文前一行==`---`"（结尾后隔空行→bell 误判）。

**复盘教训**：
- `---` 必须被行分类器**跳过**（返回 True），当正文会双补
- 写回用 `split('\n')` + `'\n'.join()` 保行尾/末尾换行原样，diff 才纯净
- 修复脚本必须做**副本幂等验证**（修一次即稳定、重跑不叠加）再放行

---

### A3. `citations: []` + 顶格列表 YAML 非法——三次出现仍未根治

**发生时间**：2026-08-15（5c03446 修复后，d3bf2d1 又改回去，8329b6d 再修）

**症状**：`citations: []` 后接顶格 `- '[[...]]'` 列表 → PyYAML `expected <block end>, but found '-'`，Obsidian 属性面板整体不渲染。

**根因**：YAML 语义——`key: []`（已有值）+ 后续顶格列表 = 非法；正确写法是 `key:`（无值）+ 顶格列表。老库 23 篇原罪，修复后又被"fix 37 空 citations"批量脚本改回非法形态。

**防护**：
- 合法模式记忆：`key:`（无值）+ 顶格列表合法；`key: []` + 后续顶格列表非法
- 全库 frontmatter 复验用 **PyYAML 权威解析**（`/Users/jcxs2014/.workbuddy/binaries/python/envs/default/bin/python`，已装），不再靠正则推断
- frontmatter 判定须"`---` 块内含 `^[A-Za-z_]\w*\s*:` key 行"，否则视为无 frontmatter（防 98/99 文件——`---` 后直接正文标题——被误当损坏）

---

### A4. 路径 A 改造/补回内容引入 Unicode 公式回归（~243 处）

**发生时间**：2026-08-15，批 1/批 2 子节镜像 + b2fh 补回

**症状**：改造与补回的内容用 Unicode 上下标（`10²⁸`、`T¹⁵`、`e⁺`、`¹²C`），违反全库"公式 LaTeX 化"规范（四域规范化后残留应 ≈0）。b2fh 03 最重 220 处。

**防护**：
- 路径 A 改造/补内容**必须把"公式 LaTeX 化"作为固定收尾步骤**（复用 `scripts/convert_supsub.py`，幂等）
- **Unicode 检测须双通道**：LaTeX 正则（`10^{28}`）会漏 Unicode 上标（`10²⁸`）→ 需 canon（Unicode 上标归一 ASCII）后匹配
- 转换后**对照原文 PDF 抽查数值**（补回内容本就手写，转换后必须核数值不变）

---

### A5. FACT 零丢失判定——字面量/反斜杠/前 N 字三坑（批 1/批 2 复验方法论）

**发生时间**：2026-08-15，批 1 复验（误报 blasi/grenier 丢失）与批 2 复验（b2fh 真丢）

**症状**：FACT 计数减少被误判为"内容丢失"；反之真实丢失（b2fh 10 个数字特征）曾两轮误判为改写。

**判定三坑**：
1. **字面量匹配**被 LaTeX 写法误报（`$10^{17}$ eV` vs `17 eV`）
2. `\rm` **单/双反斜杠变体**漏匹配（`\rm` vs `\\rm`）
3. **前 N 字特征**被句子改写/加粗标签（`**[FACT]**`）误报

**正解（双通道）**：
- **数字特征通道**（最可靠，数字不会因改写而变）：`10^{x}`/`10ˣ`（Unicode）/`\d+(\.\d+)?\s*(eV|cm|MeV|K|pc|%|barn)` 等 token 做 canon（去 LaTeX 命令含双反斜杠 + Unicode 上标归一）后匹配
- **关键词语义通道**：段落级失配时用 2-3 个领域关键词 grep 确认语义保留
- 篇级守恒检查：`git ls-tree 旧 commit` vs 工作树全篇计数，定位到篇级净减才细查

---

### A6. 执行侧范围覆盖声明必须复算 + 先 `ls` 核实再执行

**发生时间**：2026-08-15，Unicode 转换批次

**症状**：Hermes 报"212 处 0 残留"，复验抓到 grenier 05/09、blasi 02 共 50 处遗漏（指令 9 文件清单只执行了 6 个）；执行侧归因"指令文件名写错"经核实不成立（指令文件名正确）。

**根因**：执行侧按清单逐项执行时**跳过找不到的文件**，未 `ls` 核实实际文件名；且范围覆盖声明（"全部执行"）未与指令清单逐项核对。

**防护（写进所有执行指令）**：
- 执行前**先 `ls` 核实目标文件存在**——不信任指令/手册/任何来源的文件名，找不到先列目录确认，而不是跳过
- 完成报告必须**逐项对照指令清单**声明覆盖（哪些执行/哪些跳过/为什么），复验时按清单逐项复算，不采信"0 残留"等汇总断言

---

## B. 网页设计/构建工作流故障

### B1. abstract 反斜杠雪球（乱码 10KB）

**发生时间**：2026-08-13，批 1（frontmatter 写回）

**症状**：Strong 2007 的 `00_overview.md` frontmatter 出现 10211 字符乱码（`\\\\\n` 大量堆叠），Grenier 2015 类似污染。abstract 字段值吞噬了整章正文段落。

**根因（双重）**：
1. `_extract_abstract` 正则 lookahead 只认下一个 `## 0.x` 二级标题——但 Abstract 内容用 `### 原文/### 自然中文/### 关键词` 三级标题组织 → 正则只截到 `### 原文` 前的空行；或反向吞到全文
2. **雪球效应**：每次 `build_fm.py` 重跑，从已含前一次乱码的全文提取，yaml.safe_dump 再次转义反斜杠 → 指数级增长

**修复**：
1. 边界修正：`^##\s+0?\.?\d*\s*[Aa]bstract[^\n]*\n(.*?)(?=^##\s|^---\n)`（`###` 是内容不是边界）
2. 剥离 frontmatter 后再提取：`body = parts[2] if text.startswith("---")`（防重跑雪球）
3. 2000 字符硬上限
4. 从 git `e892248` 恢复 2 篇污染文件为干净版

**防护**：build_fm.py 注释 + READING_INSTRUCTIONS 第 29 节 29.1 经验"防错误级联"

---

### B2. registry key 提取 bug（Strong 2007 失踪 + 20/21 字段退化）

**发生时间**：2026-08-14，批 2 重建

**症状**：
- registry 26 条（应 27），Strong 2007 消失
- 论文 frontmatter fields 退化（read_date/tags/citations 全部为空）
- webapp PAPERS 字段为空，audit 一度全绿（盲区）

**根因（三个独立 bug 同时）**：
1. `_paper_reg(stem)` key 不匹配——`_registry[stem] = e` 用了 `parts[-2]`（被截为 `literature_analysis`），应 `parts[-1]`（实际目录名）
2. `build_registry.py:parse_frontmatter` 扫描窗口 `min(len(lines), 80)`——Strong frontmatter 因 `\n` 转义在 324 行才闭合，扫描窗口不够
3. 误改 `parts[-2]` → `parts[-3]` 加剧（变成分类目录名 `01_cosmic-ray-propagation`）

**修复**：
1. 改用 `e["path"].replace("/00_overview.md","").split("/")` 取 `parts[-1]` 拿真实目录名
2. 扫描窗口 80 → 1000（或无 cap）
3. 凡路径分片疑惑，先 print 出 `parts[-1]/[-2]/[-3]` 实测再改

**防护**：
- audit.py 加 `附: registry 21 篇`/`PAPERS 21 篇` 数量断言（已动态化为 fs 目录数）
- 任何"fix"在 webapp 跑过 headless DOM 验证之前不算"修了"

**复盘教训**（附 22）：
- **静态断言抓不到运行时回归**——audit 14 条全绿时图谱实际 0 边
- **headless DOM 验证是验收门禁而非可选**——任何数据驱动 JS 渲染的特性都要有 headless 计数
- 修代码前先 `print 实际值/期望值`，不要凭直觉改索引

---

### B3. citations 库外 vs 库内 语义混淆

**发生时间**：2026-08-14，O2 图谱批次

**症状**：
- build_fm.py 内置 `build_citations()` 从 `*references*.md` 提取库外作者名（`[[cesarsky]]`、`[[berezinskii-et-al.]]`）
- 这与 `build_citations.py` 唯一生成器职责冲突
- 批 4 跑 build_fm 时把 frontmatter 库内 citations 覆盖回库外旧值
- 图谱 50 边 → 0 边，audit 仍全绿

**根因（双重）**：
1. 两个脚本写同一字段，**没有单一生成器约定**
2. audit 17 条断言**没有 citations 非空检查**——盲区

**修复**：
1. 职责单一化：build_fm.py 删 `build_citations()` 改 `_read_existing_citations()`（透传已写）
2. build_citations.py 定为**唯一生成器**（从「篇间导航」小节 `[\`stem\`](相对路径)` 提取）
3. audit.py 加 3 条 P0-6 防护：
   - `附: citations 非空 21/21`（动态化后 23/23）
   - `附: citations 无悬空(全库内指向)`（抓 `[[cesarsky]]` 型退化）
   - `附: 图谱数据 ≥30 条引用`（数据侧保证）

**防护**：单一生成器 + 三层断言 + 数据/渲染分离

---

### B4. P0-6 二次污染（apply_wikilinks 幂等失败 → 双重包裹）

**发生时间**：2026-08-14，V2.2 wikilink 批次

**症状**：21 篇 frontmatter citations 全部被双重包裹为
`[[01_cosmic-ray-propagation/02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/00_overview/literature_analysis/00_overview|...]]`

**根因**：
- `build_citations.py` 写 `- '[[...]]'`（带引号格式）
- `apply_wikilinks.py` 幂等判断 `ln.strip().startswith("- [[")`（无引号）→ 误判为未 wikilink → 重写
- 重写时取 `val` 已是完整路径，再拼一次 → 双重路径

**修复**：幂等判断先剥引号，再检查 `val.startswith("[[") and val.endswith("]]")` → 若已是 wikilink 整行保留

**复盘教训**：幂等检查**不能只看行首/行尾**，要看值本身是否已是目标格式。

---

### B5. Obsidian wikilink 指向目录名（悬空）

**发生时间**：2026-08-14，V2.2

**症状**：Obsidian Graph 里 50 条引用连线变 0 边（`byStem[c]` 匹配不到 `[[0004_blasi-2013]]` 目录）

**根因**：Obsidian wikilink 只认**文件**不认目录；目录名 `0004_blasi-2013` 没对应 `.md` 文件

**修复**：citations 指向目标篇 overview 文件（带分类前缀 + 别名）：
```
[[02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/00_overview|0004_blasi-2013]]
```

**复盘教训**（附 19/22）：wikilink 链接必须**能点击直达真实存在的文件**。

---

### B6. wikilink 路径缺分类目录前缀（312 → 0 全部悬空）

**发生时间**：2026-08-14，V2.2 首次跑

**症状**：apply_wikilinks 一次跑完后，312 条导航 wikilink 全部悬空（实际找不到目标）

**根因**：vault 根 = `papers/`，实际路径形如 `01_cosmic-ray-propagation/0001_.../literature_analysis/00_overview.md`。脚本初始版本拼成了 `0001_.../literature_analysis/00_overview.md`（漏分类前缀）

**修复**：`nav_link_target(paper_dir, fname, cat_dir)` 加 `{cat_dir}/` 前缀

**验证全量**（每次跑必须）：397 条导航 wikilink + 50 citations 目标 100% 存在

---

### B7. cross-category citation 前缀错（13/50 悬空）

**发生时间**：2026-08-14，V2.2 二次修复

**症状**：Strong（01_cosmic-ray-propagation）引用的 blasi-2013（实际 02_cosmic-ray-origins）被写成 `01_/0004_blasi-2013/...` 路径，13 条悬空

**根因**：citations 转换沿用 citing 篇的 cat_dir 当前缀，而跨分类引用应按**目标 stem 真实所在分类**生成路径

**修复**：新增 `stem_to_cat(stem)` 查目标 stem 所在分类目录（按 `ROOT/<cat>/<stem>.is_dir()` 探测）

---

### B8. 陈旧引用名 vs 当前文件名（25 处悬空）

**发生时间**：2026-08-14，V2.2 三次修复

**症状**：Champagne-Wiescher 等篇导航头引用 `02_nuclear_reactions.md`，但实际文件已重命名为 `02_reaction_rates.md`（+ Wallerstein 1 处）。18 条悬空。

**根因**：目录重命名（如 `chore: rename directories to match actual authors`）遗留了导航头里的旧文件名未同步更新

**修复**：`apply_wikilinks.py` 加编号对齐修复阶段：扫描 `literature_analysis/` 实际文件，构建 `actual_by_num`（按编号前缀索引），正则 `\`(\d{2})_...\.md\`` → 替换为真实文件名

**修复结果**：25 处陈旧引用全部对齐

---

### B9. 97/98 附录文件孤立（42 个 Graph 悬空节点）

**发生时间**：2026-08-14，V2.2 验证阶段

**症状**：97_quality_check.md / 98_vocabulary.md 各 21 篇（共 42 个）**无任何入链**——`> 上一文件：\`04_references.md\``（反引号格式）不匹配 apply_wikilinks 转换的"上一章/下一章"模式

**修复**：`patch_appendix_nav.py` 给 97/98/99 补标准导航头：
- 97: 上一章=本篇最后正文文件，下一章=98_vocabulary
- 98: 上一章=97，下一章=99
- 99: 已有则跳过，缺则补 上一章=98

**结果**：97/98 导航覆盖从 0/21 提升到 21/21

---

### B10. git checkout 误建无分类前缀目录（commit 污染）

**发生时间**：2026-08-14，V2.2 提交阶段

**症状**：提交里多了一个 `0005_champagne-wiescher-1992/literature_analysis/02_nuclear_reactions.md` 0 字节空文件（无 `03_` 前缀）

**根因**：`git checkout -- "01_cosmic-ray-propagation/" "02_cosmic-ray-origins/" "03_stellar-nucleosynthesis/"` 中第二条路径写错产生了无前缀目录，里面有个空文件被 `git add -A` 收编

**修复**：
1. `rm -rf 0005_champagne-wiescher-1992` + `git rm --cached` + commit --amend
2. `.gitignore` 加 `*.pdf` 防止根目录 PDF 被误提交

**复盘教训**：`git show <commit> --name-status --format=""` 看完整路径（`--stat` 路径长会截断显示 `.../`），无前缀路径 = 异常。

---

### B11. 教科书被误提交（占 17MB）

**发生时间**：2026-08-14，corpus 批次提交时

**症状**：用户已说"教科书跳过"但 git 提交里出现了 `Cosmic Ray Astrophysics ...pdf` 17MB

**根因**：`git add -A` 把根目录教科书 PDF 一并加进来，corpus 提交未排除

**修复**：`git rm --cached` + `.gitignore` 加 `*.pdf`（顶层不跟踪；库内目录的 PDF 通过 `git add -f` 单独处理）

---

### B12. audit 硬编码 21 → 库扩到 23 时失败

**发生时间**：2026-08-14，corpus 扩展后

**症状**：23 篇入库后 audit 报"PAPERS 21 篇"失败（硬编码值）

**修复**：新增 `_fs_paper_count()` 函数动态扫分类目录计数；断言改为 `与目录数一致`

**复盘教训**：阈值断言**不写死数**，写相对条件（"fs=N && papers=N"）才不因库扩容触发假报警

---

### B13. audit 文案残留 "21/21" 字样

**发生时间**：2026-08-14，同 B12

**症状**：PAPERS 数量已动态，但 "read_date 非空 21/21" 等文案残留固定数字

**修复**：所有数字文案动态化（`f"{len(papers)-len(rd_empty)}/{len(papers)} 缺 {len(rd_empty)}"`）

---

### B14. frontmatter 字段值残留 `[FACT]`（参见 A1）

build_fm 防护 + audit 断言

### B15. 移动端 overlay 遮罩作用域泄漏到桌面端（M11）

**发生时间**：2026-08（早期 webapp 迭代）  
**Commit**：`8a7004d fix: webapp — M11 overlay mobile-only + H6D1-D4 dropdown fixes`

**症状**：桌面端（>900px）点击 ☰ 侧边栏按钮后，整个内容区变暗，鼠标滚轮失效——`.main` 区域被遮罩拦截无法滚动。

**根因**：
- 修移动端遮罩时，`.app.sidebar-open #overlay { display:block }` **没放进 `@media (max-width:900px)`** 媒体查询内
- 注释写的是 "Overlay for mobile" 但**注释不等于规则作用域**——CSS 规则对所有视口生效
- 桌面端侧边栏打开时，`#overlay` 变 `display:block`，配合 `position:fixed; inset:0; z-index:98` 整页覆盖
- 覆盖在 `.main` 上方 + 拦截滚轮事件 → 滚动失效

**修复**：
```css
@media (max-width:900px) {
  .app.sidebar-open #overlay { display:block; }
}
```

**复盘教训**（"规则作用域"原则）：
- 新增 UI 功能必须**显式限定作用域**（媒体查询 / 选择器前缀 / `:where()`）
- 注释说"for mobile"不等于规则只在 mobile 生效——CSS 没有隐式作用域
- 测试覆盖：必须测**未被设计目标包含的视口**（桌面验证移动端修复时尤其容易漏）

**参考**：附 27 / H5 (sidebar + TOC) 同类修复历史

---

### B16. `overflow-x:auto` 强制裁剪绝对定位下拉（H6D1）

**发生时间**：2026-08（早期 webapp 迭代）  
**Commit**：`8a7004d fix: webapp — M11 overlay mobile-only + H6D1-D4 dropdown fixes`

**症状**：toolbar 分组下拉菜单（`.tab-dropdown`）被 toolbar 容器裁剪，只能看到一小片；容器内出现异常滚动条；某些点击路径下拉完全不可见。

**根因**：
- CSS Overflow 规范细节：`overflow-x` 非 `visible` 时，浏览器**强制把 `overflow-y` 设为 `auto`**（即使你只写了 `overflow-x:auto`）
- `.tab-groups { overflow-x:auto }`（原本为响应式换行）→ 垂直方向被强制 `auto` 裁剪
- `.tab-dropdown { position:absolute; top:calc(100%+4px) }` 的下拉定位在容器高度**之外** → 被父级 clip 掉
- `position:sticky` 不保护（sticky 只管 sticky 行为，不改变 overflow clip）

**修复**：
```css
.tab-groups { display:flex; gap:6px; align-items:center; flex:1; overflow:visible; flex-shrink:1; }
.toolbar   { ...; overflow:visible; }  /* 删 overflow-x:auto */
```
绝对定位弹层改 `position:fixed` + `getBoundingClientRect()` 定位（更彻底，但本仓库选择移除祖先 overflow）。

**复盘教训**（"绝对定位祖先链"原则）：
- 任何 `position:absolute` 子元素所在祖先链上**不能有 `overflow` 非 visible**
- 排查"元素在 DOM 存在但视觉上被裁剪"时，**先 trace 每一级祖先的 overflow**，再追 z-index/stacking context
- CSS overflow clip 是 painting-stage 约束，z-index 救不了
- 需要滚动条时，**让弹层用 fixed**而不是依赖父级 overflow

**参考**：附 27 / P10 H6D1 案例完整分析

---

### B17. KaTeX 延迟加载 + DOM 状态时序错位

**发生时间**：2026-08（早期 webapp 迭代）  
**Commit**：`15ec455 fix(shell): guard KaTeX applyMath — check readyState immediately + DOMContentLoaded`

**症状**：部分页面刷新后数学公式不被渲染（保留为 `$...$` 源码），但刷新一次后又能渲染——典型的时序竞态。

**根因**：
- shell.html 用 `<script defer src="katex.min.js">` 加载 KaTeX（defer = DOM 解析完成后才执行）
- 但 shell 主体 `<script>`（含 `applyMath()`）同步执行，可能在 KaTeX 之前完成
- `if (window.katex) applyMath()` 一次检查 → KaTeX 还没加载就跳过
- `DOMContentLoaded` 监听也可能错过（如果 `document.readyState === "loading"` 才触发，否则已 fire）

**修复**：
```js
// 关键：双触发点 + 立即检查 readyState
function tryApplyMath() {
  if (window.katex) { applyMath(); return true; }
  return false;
}
// 1) 立即检查（DOM 已 ready 且 KaTeX 已就绪的场景）
if (document.readyState !== "loading" && tryApplyMath()) { /* done */ }
// 2) DOMContentLoaded 兜底（DOM 还在 loading 时）
document.addEventListener("DOMContentLoaded", () => { tryApplyMath(); });
// 3) 一些版本的 KaTeX 还有内部 ready，可考虑 window.load
```

**复盘教训**（"延迟依赖时序"原则）：
- 任何依赖外部脚本（A/B/C 异步或 defer）的初始化函数，**至少有 2 个触发点**（立即检查 + 事件兜底）
- 单点检查（`if (X) init()`）在快网络/慢网络/缓存命中/重新加载等不同路径下表现不一致
- `document.readyState` 是同步属性，**比 DOMContentLoaded 事件早可用**——优先用

---

### B18. 搜索高亮 lastIndex 状态残留（H5）

**发生时间**：2026-08（早期 webapp 迭代）  
**Commit**：`f7d0648 fix: webapp — P0 audit fixes (H1/H2/H3/H4/H5/M1-M5/M7/M10 + H6 tab groups)`

**症状**：全文搜索后第二次搜索**第一次匹配位置不对**——例如输入"宇宙"第二次高亮位置比预期偏前一位。

**根因**：
- RegExp 的 `.exec()` 和 `String.match()`（带 `/g` flag）共用全局 `lastIndex` 状态
- 上一次搜索未重置 `lastIndex` 到 0，下一次调用从上次停止的位置开始
- 典型 hack：每次 `re.lastIndex = 0` 在循环前

**修复**（在搜索高亮函数顶部重置）：
```js
function highlightMatches(text, pattern) {
  pattern = new RegExp(escapeRegex(pattern), "gi");
  pattern.lastIndex = 0;  // 关键：显式重置
  // ...或直接用 .replaceAll(text, ...) 避开 lastIndex
  return text.replace(pattern, m => `<mark>${m}</mark>`);
}
```

**复盘教训**（"全局可变状态"原则）：
- 任何带 `g` 或 `y` flag 的 RegExp，跨调用共用 `lastIndex`
- 防御性做法：用 `.replace()` + global flag（每次返回新字符串，不依赖 lastIndex）
- 或在函数入口显式 `re.lastIndex = 0`

---

## C. 跨流程数据一致性故障

### C1. abstract 反斜杠雪球（参见 B1）

`[FACT]` 误写与 abstract 雪球是同型问题（重跑未剥离前产物），共享防护：build_fm 入口清洗 + 长度上限 + 字符硬截断。

---

### C2. 同一字段多个生成器竞争（参见 B3 + B4）

**规则**（现在全库适用）：`citations` = `build_citations.py` 唯一写；`abstract`/`year`/`read_date`/`category` = `build_fm.py` 唯一写；`registry.json` = `build_registry.py` 唯一派生读透传；`registry` 不允许手工改。

**违反**会立即报 P0-6 类别问题（看 audit 断言）。

---

## D. 工具与工程故障

### D1. browser_exec 需要用户点 Allow 弹窗

**现象**：`browser_exec` 在桌面端启动 Chrome remote debugging 必弹"Allow remote debugging?"——用户必须手动点击

**解决**：
- 静默验证优先用 `Chrome headless --dump-dom` + 字符串解析
- browser_exec 只在需要交互时用（用户批准弹窗后重试）
- 在记忆/SOP 中明示此约束

---

### D2. PyYAML 缺失导致 /api/rebuild 500

**发生时间**：2026-08-14，批 2 验收

**症状**：`POST /api/rebuild` 返回 500，registry_rc=1（`ModuleNotFoundError: No module named 'yaml'`），但 webapp_rc=0 用旧 registry 重建成功——**静默半成功**

**修复（三层）**：
1. `build_registry.py` 改为读 frontmatter 时不依赖 yaml（用纯字符串解析——已用 PyYAML 因为环境有；后续可改）
2. `server.py` 加顺序依赖：registry 失败 → 跳过 webapp → 500 + `registry_failed:true` + 修复 hint
3. `server.py` 启动自检：缺 yaml 立即 FATAL（exit 2）+ 修复指引

---

### D3. PIL 在 hermes venv 损坏

**现象**：`from PIL import Image` 在所有 Python 解释器下都失败（_imaging 导入错误）——PYTHONPATH 全局污染

**解决**：`env -u PYTHONPATH python3 webapp/build_pwa.py`（隔离 PATH，干净 homebrew PIL 12.x 工作）

---

## E. 排障 SOP（顺序）

新故障出现时按以下顺序排查（与 READMING_INSTRUCTIONS 第 29 节"数据一致性经验"互补）：

1. **复现**：用最小化命令复现（如 `python3 webapp/audit.py 2>&1`）
2. **静态断言 vs 运行时验证分离**：先看 audit 报什么，再看 headless 实际渲染什么——两边对不上就是渲染层 bug
3. **追溯构建链**：用 `git log --stat` 找到最后引入 bug 的提交，对比前/后产物
4. **避免"凭直觉改索引"**：任何 `parts[-1]/[-2]/[-3]` 疑惑，先 `print 实际值`
5. **修复 + 防护**：
   - 修复（手工清洗或代码改动）
   - 防御（写入端清洗：build_fm `_strip_fact_tag` 类）
   - 检测（audit 断言：防回归）
   - 验收（headless 端到端）
6. **本文件追加**：当批追加到对应章节，下次复盘时合并陈旧条目

---

## F. 待解决与已知局限

| 项 | 状态 | 备注 |
|---|---|---|
| `webapp/server.py` 自动从 `build_registry.py` 读 frontmatter 强依赖 PyYAML | 待优化 | 当前系统 Python 有 PyYAML 6.0.3 实测可用；改纯 stdlib 风险/收益待评估 |
| print 验收：`<md5>` 根目录 PDF 与库内副本比对 | 待做 | 当前只对比了一轮，可自动化 |
| 实时 lint（提交前自动跑 audit） | 缺失 | git pre-commit hook 候选 |

---

*本文件由 2026-08 多批次工作流的踩坑沉淀而来；维护原则 = 修复必追加 + 每年合并陈旧。*

### A8. check_density 阈值调成橡皮图章（门禁失效）

**发生时间**：2026-08-16，多轮调参后

**症状**：check_density 报 51/51 全通过，但 arnould（0公式）、busso（0公式）、karakas（15公式）全部通过。

**根因**：阈值设定逻辑是"先跑一遍看到最差篇是X，再把阈值设为X+0.4让它通过"。arnould 最低2.4，就把门槛定为2.0——等于用最差篇的密度给门禁划线。

**实录教训**：
| 篇 | agent报告 | check_density实测 |
|---|---|---|
| arnould | 58公式 | **169公式** |
| grevesse | 51公式 | **85公式** |
| nomoto-suzuki | 85公式 | **134公式** |

差距1.5-3倍。agent summary 永远不等于最终值，必须 subprocess 重跑。

**防护**：
- 阈值按**质量标杆**定（nomoto 12.7 / drury 7.2 / giacalone 4.4 的下沿 = 4.0）
- 禁止先看现状再调阈值让最差篇通过
- busso-1999（AGB理论综述）不得入 OBSERVATIONAL 豁免——分类错误会豁免掉真实问题
- 交付前必须 `python3 scripts/check_density.py` 用 subprocess 重跑，以脚本输出为准

### A7. build_fm.py 白名单重建丢字段（38 篇 frontmatter 回归）

**发生时间**：2026-08-15 深夜，并行会话跑 webapp 脚本链

**症状**：38 篇 00_overview frontmatter 被重写后**字段大面积丢失**（Bell 的 title/journal/doi/arxiv/pages + 刚补的 5 个 sections 全丢），Obsidian 属性面板字段缺失；audit 报 title 空/registry 不一致；15 篇 citations 被清空。

**根因**：`build_fm.py` 按**内部字段白名单**重建 frontmatter（title/authors/year/category/status/read_date/lastread/tags/citations/path），**丢弃白名单外字段**（journal/doi/arxiv/pages/sections/keywords/abstract…）。存量库已含增强字段（pages 补齐 1ad9840、sections 补齐、YAML 修复），白名单重建必然丢字段。

**防护**：
- **存量库（含增强字段）禁止裸跑 build_fm 全量写回**；必须：① 先 `--dry-run` 对比字段差异 ② 或改用增量脚本（只补 citations 等单字段）
- **属性面板完整性检查**：frontmatter 关键字段守恒 = title/pages/sections/citations 逐项非空（脚本链复验必查）
- 并行会话跑"全链脚本"时，**audit 失败是数据破坏预警**，不是"重跑就好"——先 diff 定位再动
- 回滚手段：`git checkout -- 0*/`（git 是最后防线，脚本跑前确保工作树干净可回滚）
