# sections 字段补齐执行指令（15 篇路径 A）

> 生成：2026-08-15（WorkBuddy 主会话）｜执行：指定会话（本文件自包含）
> 背景：Hermes 自审报告发现 18 篇缺 `sections:` 字段；复验确认其中 **3 篇（Bell/BO/BE）为路径 B 八段模板，无 sections 属预期豁免**；**15 篇路径 A 缺 sections 为真实缺陷**，本指令补齐
> 关联：`docs/执行指令模板.md`（通用结构）｜`docs/README.md` 无直接引用

---

## 0. 任务概览

| 项 | 内容 |
|---|---|
| 任务 | 15 篇路径 A 文献的 `00_overview.md` frontmatter 补 `sections:` 字段 |
| 范围 | 见 §1 清单（15 篇，仅 00_overview.md） |
| 完成判定 | 15/15 有 sections、格式正确、标题与原文/分章对照、YAML 0 失败 |

---

## 1. 目标篇目（15 篇，实测缺 sections 且为路径 A）

```
01_cosmic-ray-propagation/0006_ruszkowski-pfrommer-2023
01_cosmic-ray-propagation/0003_weinrich-2020
01_cosmic-ray-propagation/0004_mewaldt-2001-clocks
01_cosmic-ray-propagation/0002_amato-blasi-2018
02_cosmic-ray-origins/0015_telescope-array-2023
02_cosmic-ray-origins/0006_grenier-2015
02_cosmic-ray-origins/0003_gaisser-1990
02_cosmic-ray-origins/0004_blasi-2013
02_cosmic-ray-origins/0013_giuffrida-2022
02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000
02_cosmic-ray-origins/0002_al-dargazelli-1996
03_stellar-nucleosynthesis/0006_anders-grevesse
03_stellar-nucleosynthesis/0015_kraft-1994
03_stellar-nucleosynthesis/0007_grevesse-sauval-1998
03_stellar-nucleosynthesis/0014_cameron-1968
```

**豁免（不动）**：`0008_bell-1978`、`0009_blandford-ostriker-1978`、`0010_blandford-eichler-1987`（路径 B 八段模板，无 sections 属预期）

---

## 2. 格式规范（沿用库内既有）

参照已合规篇（strong-moskalenko-2007 / cowan-2021）：

```yaml
sections:
  - '§I Theoretical Background'
  - '§II Confrontation with Data'
```

- `sections:` 后每个章节一行 `  - '标题'`（两个空格缩进 + 单引号）
- **标题逐字沿用原文**（含编号体系：§I/§II 罗马 或 1./2. 数字 或 §4.1，按该篇原文实际）
- 放在 `pages:` 之后、`status:`/`read_date:` 之前（frontmatter 内，位置与 strong 一致）

---

## 3. 提取来源（优先级）

1. **该篇 `00_overview.md` 的"论文结构树"**（若已有原文章节列表，直接采用）
2. **分章文件内的路径 A 二级标题**（`## N. 原文标题`，如 ruszkowski `## 2.1 Cosmic ray interactions...`）——按分章编号顺序汇总
3. **原文 PDF 目录**（`pdftotext -layout` 或视觉读图）——分章未覆盖时兜底

**铁律**：
- **不编造**章节标题——每项必须能在原文/结构树/分章标题中找到依据
- 不翻译（保留原文标题，如 `§II Observations`）
- 只补 `sections:` 字段，**不动 frontmatter 其他内容、不动正文分章**
- 完成前 `ls` 核实每篇 `00_overview.md` 存在（先核实再执行）

---

## 4. 执行步骤

1. 对每篇：读 `00_overview.md`（结构树）→ 若缺，扫分章 `## N.` 标题 → 汇总章节列表
2. 插入 `sections:` 块（格式见 §2）
3. PyYAML 验证（见 §5）

## 5. 验证

```bash
PY=/Users/jcxs2014/.workbuddy/binaries/python/envs/default/bin/python
# YAML 全过 + 15 篇均有 sections
$PY -c "
import glob, yaml
bad = []
for f in glob.glob('0*/**/00_overview.md', recursive=True):
    if 'backup' in f: continue
    d = yaml.safe_load(open(f, encoding='utf-8').read().split('---',2)[1])
    if d.get('path','').split('/')[1] in [p.split('/')[1] for p in '''<15篇清单>'''.strip().splitlines()] and not d.get('sections'):
        bad.append(f)
print('15 篇缺 sections:', bad if bad else '0')
" 
# 格式抽查：每项 - '...' 单引号
grep -A3 "^sections:" 01_cosmic-ray-propagation/0006_ruszkowski-pfrommer-2023/literature_analysis/00_overview.md
```

## 6. 提交

- 单笔 commit：`docs(papers): 15 篇路径 A 补 sections 字段（自审修复）`
- 精确 `git add` 15 个 00_overview.md，**禁 `git add -A`**
- 不碰 Bell/BO/BE 及工作树其他并发文件

## 7. 完成报告要求

1. 提交 hash + 15 篇每篇的 sections 条目数
2. 提取来源说明（每篇用了结构树/分章标题/PDF 中的哪种）
3. 自检结果（§5 命令输出）

## 8. 完成标准（WorkBuddy 复验口径）

| # | 检查项 | 口径 |
|---|---|---|
| 1 | 覆盖 | 15/15 有 `sections:` 且非空 |
| 2 | 格式 | 每项 `  - '...'` 单引号，编号体系与原文一致 |
| 3 | 对照 | ≥5 篇抽查章节标题与分章/原文目录一致（逐字） |
| 4 | YAML | PyYAML 全库 0 失败（无回归） |
| 5 | diff | 仅 15 个 00_overview.md，每篇仅加 sections 块 |
| 6 | 工作树 | 干净（仅允许声明的并发文件） |
