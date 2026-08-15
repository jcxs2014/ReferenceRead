# Unicode 公式检查与转换执行指令（批 1/批 2 引入回归）

> 生成：2026-08-15（WorkBuddy 主会话）｜执行：指定会话（本文件自包含）
> 背景：批 1/批 2 子节镜像改造与 b2fh 补回时，**引入了 Unicode 上下标公式**（如 `10²⁸`、`T¹⁵`、`e⁺`、`¹²C`、`ε_CN ∝ T¹⁵`），违反全库"公式 LaTeX 化"规范（四域规范化已完成，残留应 ≈0）——WorkBuddy 扫描确认约 350 处
> 目标：最近更新文档中的 Unicode 公式 → LaTeX（复用 `webapp/convert_supsub.py` 幂等转换），恢复规范
> **铁律：对照原文 PDF 核对转换后数值/符号正确性**（转换是机械的，但补回内容本就来自人工书写，需抽查）

---

## 0. 扫描结果（WorkBuddy 实测，2026-08-15）

| 文件 | Unicode 处数 | 主要字符 |
|---|---|---|
| `03_stellar-nucleosynthesis/0001_b2fh-1957/.../03_hydrogen_helium_alpha_burning.md` | **220** | ²³¹⁰⁴⁵⁶⁷⁸⁹⁻⁺（补回内容） |
| `02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/.../06_magnetic_fields_constraints.md` | 18 | ²¹⁰⁹⁻ |
| `.../08_acceleration_sources.md` | 19 | ²¹⁰⁷⁸⁻₁ |
| `.../07_source_search_transport.md` | 13 | ²³¹⁻₀ |
| `.../09_topdown_basic_fragmentation.md` | 9 | ²³¹⁶⁻ |
| `02_cosmic-ray-origins/0006_grenier-2015/.../05_crism_interactions.md` | 25 | ⁺⁻₂₃ |
| `.../09_conclusion.md` | 13 | ¹⁰⁶⁺⁻₂₃ |
| `02_cosmic-ray-origins/0004_blasi-2013/.../02_sn_r_premises.md` | 12 | ³¹⁴⁻₁₅ |
| `03_stellar-nucleosynthesis/0005_champagne-wiescher-1992/.../07_rp_process_impedance.md` | 12 | ²⁵⁶⁷⁺₁₂₉ |

> 说明：部分 Unicode（如核素 `¹²C`、电荷 `e⁺`）是补回/重写时手写的；同位素在旧规范中最终形态为 `$^{12}{\rm C}$`——统一按 `convert_supsub.py` 规则转

## 1. 执行步骤

### 步骤 1：dry-run（先看改动面）

```bash
cd /Users/jcxs2014/Sites/HermesLocal/papers
# 用 convert_supsub 对上述 9 个文件 dry-run（脚本 --dry-run 或先复制到 /tmp 试跑）
/Users/jcxs2014/.workbuddy/binaries/python/envs/default/bin/python webapp/convert_supsub.py --dry-run <文件>   # 若支持；否则在副本上试
```

### 步骤 2：转换（每篇独立跑，避免跨文件干扰）

```bash
/Users/jcxs2014/.workbuddy/binaries/python/envs/default/bin/python webapp/convert_supsub.py \
  03_stellar-nucleosynthesis/0001_b2fh-1957/literature_analysis/03_hydrogen_helium_alpha_burning.md \
  # ...逐文件（或按脚本用法批量）
```

- **规则以 convert_supsub.py 为准**（同位素 `¹²C`→`$^{12}{\rm C}$`、单位指数 `cm⁻²`→`cm$^{-2}$`、电荷 `e⁺`→`e$^{+}$`、变量幂 `10²⁸`→`10$^{28}$` 等）
- **不动 frontmatter**；`±` 不确定度豁免（`±²/₋₄` 类保留）

### 步骤 3：对照原文抽查（铁律）

- **b2fh 03（220 处，补回内容）**：转换后抽查 ≥5 处数值与 PDF 原文一致（如 `10²⁸`→`10$^{28}$` 数值、`0.421 MeV`、S₀ 公式系数）
- 其余文件抽查 ≥2 处
- 重点核对：转换器对**手写 Unicode 组合**（如 `ε_CN ∝ T¹⁵ ~ 10²⁸ erg g⁻¹ s⁻¹`、`4p → ⁴He + 2e⁺ + 2ν_e`）的拆分是否语义正确（是否切成多个公式对象但数值不变）

## 2. 验证

```bash
# 1) 9 个文件 Unicode 上下标残留 = 0（复用 convert_supsub 字符集扫描）
# 2) 幂等：重跑 dry-run 0 改动
# 3) 数字守恒：转换前后数值 token 集合一致（Unicode 数字归一 ASCII 同值）
# 4) $ 配对偶数；无残留裸 Unicode 上下标（frontmatter 豁免除外）
# 5) 对照原文抽查通过（步骤 3）
```

## 3. 提交约定

- 每篇 1 commit（9 个）：`style(formulas): <篇> 分章 Unicode 公式→LaTeX（批1/批2回归修复）`
- 精确 add 对应分章文件，**不得 git add -A**
- b2fh 03 单独 1 commit（最大，220 处）

## 4. 完成标准（WorkBuddy 复验口径）

1. 9 个文件 Unicode 上下标残留 = 0（frontmatter/± 豁免除外）
2. b2fh 03 对照原文 ≥5 处数值一致；其余 ≥2 处
3. 幂等、数字守恒、$ 配对全过
4. 全库公式规范恢复（上下标残留回到规范化后的 ≈0 水平）
5. 工作树干净、提交规范
