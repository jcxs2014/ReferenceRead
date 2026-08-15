# 公式 LaTeX 化批量执行说明

> 生成：2026-08-15（WorkBuddy，供执行侧参考）
> 背景：全库 292 个 md、约 25,400 处 Unicode 数学字符（历史欠账：精读未约束公式格式）。试点已完成 `background/02_nucleosynthesis.md`（144 处，提交 `1a40647`），规范已写入 `READING_INSTRUCTIONS.md` §7.1（提交 `0336a59`）。
> **铁律（用户 2026-08-15 明确）：修改公式必须对照原文 PDF 确保正确性——格式转换不得改变任何数值/符号语义。**

---

## 0. 转换规则（方案 B，已定）

| 形态 | 示例 | 处理 |
|---|---|---|
| 科学记数法（纯数值） | `10⁷ yr` | `$10^{7}$ yr` ✅ 转 |
| 科学记数法（×10ⁿ） | `2×10⁶ yr` | `$2\times10^{6}$ yr` ✅ 转 |
| 参数下标 | `T₉`、`t₁/₂` | `$T_9$`、`$t_{1/2}$` ✅ 转 |
| 核素/同位素 | `¹²C`、`⁸Be`、`Zr⁹⁰`、`¹³N(p,γ)¹⁴O` | **保留 Unicode**（化学排版惯例） |
| 单位带指数 | `g cm⁻³`、`cm⁻² s⁻¹` | **保留 Unicode** |
| 衰变标记/不确定度 | `β⁺`、`±²/₋₄` | **保留 Unicode** |
| 已有 LaTeX | `$\tau_\gamma(...)$` | 保护不碰 |

## 1. 转换脚本（升级版，复用试点）

- 复用试点逻辑：frontmatter 状态机（开头 `---` 进入、遇 `---` 退出）、已有 `$..$` 占位保护。
- **新增 ① 复合下标**：`t₁/₂` 类（字母+下标/下标）一次转成 `$X_{1/2}$`，禁止先转一半再补（试点教训）。
- **新增 ② 审计清单输出**：每次转换记录 `文件\t行号\t原文\t转换后\t类别`，输出 `conversion_audit.tsv`——**这是对照原文验证的凭据，必须生成并随批提交**。
- **新增 ③ Unicode 残留自检**：转换后统计残留上标/下标，人工核对残留是否全部属于"保留类"（核素/单位/衰变标记）。

## 2. 对照原文验证流程（强制，核心环节）

> 目的：证明"该转的都转了、不该转的没转、数值一个没变"。格式层正确（渲染无残破）≠ 语义正确（对照原文）。

### 2.1 每篇转换完成后，从审计清单抽样对照原文 PDF

**抽样策略（按类别分级）**：

| 类别 | 抽查强度 | 方法 |
|---|---|---|
| 科学记数法数值（含小数/多位数，如 `8.2×10⁻¹⁷`） | **全覆盖**（每处必查） | 数值一致性核对 |
| 参数下标（`T₉`/`t₁/₂`/`T₈` 等） | 每篇 ≥5 处 | 符号核对 |
| ×10ⁿ 表达式 | 每篇 ≥5 处 | 数值+结构核对 |
| 保留类（核素/单位） | 抽查 3 处确认"确实保留了" | 确认未误转 |

**对照方法**：
- 文本型 PDF：`pdftotext <pdf> -` 提取全文 → 按关键词/数值搜索原文该段 → 核对转换后 md 的数值/符号与原文一致。
- 扫描型 PDF：`pdftoppm -png -r 150 <pdf> <out>` 转 PNG → 视觉读取对应段落。
- background 汇总文档：数值溯源到对应文献 PDF（如 `T₉` 源自某篇综述），对照该篇。

**完成判定**：抽查 100% 通过（数值零差异、语境正确、保留类无误转）→ 该篇转换合格；任一不符 → 退回修正该处（连带检查同类形态是否同样出错）。

### 2.2 渲染验证（每批）

- 重建产物（venv）：`python3 webapp/build_webapp.py --include-papers`
- headless 检查：新转文档 `math.inline` 注入数 > 0、**残破形态 0**（`$t_{1}$/₂` 类）、JS 0 错误：
  ```bash
  CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  "$CHROME" --headless=new --disable-gpu --no-sandbox --virtual-time-budget=15000 \
    --dump-dom "file://$PWD/webapp/interactive.html" > /tmp/wb.html 2>/tmp/wb.err
  grep -c 'class="math inline"' /tmp/wb.html   # 应 >0
  grep -icE 'uncaught|exception' /tmp/wb.err    # 应 0
  ```
- `audit.py` 全绿。

## 3. 批处理顺序

1. **论文文献优先**（用户实际阅读对象）：02 起源 → 03 核合成 → 01 传播，每篇独立提交（`feat(fm): <篇名> 公式 LaTeX 化`）。
2. **background 其余文档**：01_cosmic_rays / 03_astrophysics / 04_critique_index / 05_glossary / 00_home / 06_controversy_evolution（02_nucleosynthesis 已完成）。
3. **frontmatter 不动**（year/abstract 等元数据 Unicode 不转）。
4. 每批提交必须附：`conversion_audit.tsv` + 对照验证记录（抽查了哪几处、对照了哪篇 PDF、结论）。

## 4. 工作量与验收

- 脚本升级：0.5 单元；逐篇转换+对照：每篇约 0.1–0.2 单元（文献长文相应上浮）。
- **总验收**：全库残留 Unicode 仅剩"保留类"（核素/单位/衰变标记）；audit 全绿；headless 无残破；抽查记录齐全。
