# 修复 goal —— 元数据缺口 + abstract 补全 + 词汇表 A 节补强（跨域）

> 生成：2026-08-18 15:55（WorkBuddy）
> 依据：2026-08-18 对「修正版审计报告」的实测复核（磁盘 + git 双核对）
> 基线：WorkBuddy 2026-08-18 实测（全部以 awk/grep 实测为准，见末尾复验口径）
> 定位：**允许修改文献**；仅处理双方（审查方 + 复核方）一致认定的真问题；**P0「26 篇失踪」已证伪，不在范围内**

---

## ⚠️ 前置结论（必须先读）

一份外部审查报告声称「P0：git index 55 / 磁盘 29 / 26 篇失踪，需从 git 恢复」。
**该结论已实测证伪，整套恢复动作禁止执行：**

- `git ls-files` 与磁盘 `find` 双核对：磁盘 **55 篇 = git HEAD 55 篇**，分布完全一致 `01:7 / 02:20 / 03:24 / 04:4`
- `git status` 干净（0 行）——「status 干净却 26 篇不在磁盘」在 git 语义上不可能并存
- 报告把 `01_cosmic-ray-propagation` 这类**域文件夹**误当成论文数，导致磁盘误数为 29

**本 goal 范围内只有下方 Tier A / Tier B 的真问题；任何「恢复 26 篇 / 磁盘 git 不同步」类动作一律不做。**

---

## /goal 触发指令（直接粘贴给 Hermes）

```
/goal 元数据缺口 + abstract 补全 + 词汇表 A 节补强（允许修改文献，分项提交，排除假 P0）

【任务定位】
仅处理下方经实测确认的真问题：①小元数据缺口（DOI/journal/sections）②abstract 补全
③词汇表 A 节逻辑词补强。允许修改目标篇 literature_analysis/ 下文件（00_overview.md
frontmatter、98_vocabulary.md）；禁止动其他文献文件；禁止删除文件；禁止做任何
"恢复 26 篇缺失论文"的动作（该 P0 已被复核证伪，磁盘 git 均为 55 篇、status 干净）。

【执行前】git fetch + git log --oneline -3 确认工作树最新；
每项修复前用下方复验口径的 awk/grep 实测基线（不要引用旧数字）；完成后自查。

【Tier A：小元数据缺口（10 个事实字段，从 PDF / crossref 补全）】
DOI 缺 6（填真实 DOI，优先 crossref 或 PDF 首页）：
  02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000
  02_cosmic-ray-origins/0002_al-dargazelli-1996
  03_stellar-nucleosynthesis/0006_anders-grevesse
  03_stellar-nucleosynthesis/0007_grevesse-sauval-1998
  03_stellar-nucleosynthesis/0011_kewley-2001-starburst
  03_stellar-nucleosynthesis/0012_dieterich-2014-h-burning-limit
journal 缺 1：
  03_stellar-nucleosynthesis/0009_asplund-2009-solar-composition
sections 缺 3（填该文真实章节标题列表，如 ['§I ...','§II ...']）：
  02_cosmic-ray-origins/0015_telescope-array-2023
  03_stellar-nucleosynthesis/0007_grevesse-sauval-1998
  03_stellar-nucleosynthesis/0014_cameron-1968

【Tier B1：abstract 补全（52 篇）】
现状：55 篇中仅 3 篇有 abstract（strong-moskalenko-ptuskin-2007 / grenier-2015 /
arnould-goriely-2003），其余 52 篇 frontmatter 缺 abstract: 字段。
要求：从 PDF 抽取原文摘要（verbatim），写入 00_overview.md frontmatter 的 abstract:
字段，格式对齐已有 3 篇（"### 原文 > ... ### 自然中文 ... ### 关键词与要点"等，
允许适度精简但须含原文摘要 + 中文翻译）。禁止编造摘要内容。
验收：55/55 篇 abstract: 字段存在且非空、内容为真实摘要。

【Tier B2：词汇表 A 节逻辑词补强（18 篇，补至 ≥15 条）】
现状（A 节表格行数，<15 即不达标）：
  01_cosmic-ray-propagation/0003_weinrich-2020(11) 0006_ruszkowski-pfrommer-2023(7)
  02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000(14) 0002_al-dargazelli-1996(9)
    0003_gaisser-1990(12) 0004_blasi-2013(12) 0005_amato-2014(10) 0006_grenier-2015(13)
    0007_biermann-1996(9) 0008_bell-1978(9) 0014_alvesbatista-2019(7)
    0018_kotera-olinto-2011(0) 0019_bell-1978-ii(0)
  03_stellar-nucleosynthesis/0016_cowan-2021(7) 0017_kaeppeler-2011(7)
    0018_arnould-goriely-2003(0) 0022_busso-1999(14) 0023_eichler-1989(0)
要求：按 READING_INSTRUCTIONS §10/§28 模板，在 98_vocabulary.md 的 A 节
（表格 | 单词 | 词性 | 逻辑功能 | 中文 | 原文例句 | 逻辑说明 |）补逻辑词至 ≥15 条，
词条须来自本篇分析文本中实际出现的学术逻辑词（因果/转折/递进/限定等），禁止凑数空话。
验收：55/55 篇 A 节逻辑词 ≥15 条。

【提交】分项提交（Tier A 按字段分组、Tier B1/B2 各按域或按批），
只 add 本项改动文件（严禁 git add -A）；commit message 注明实测数字
（如 fix: 补 6 篇 DOI + asplund journal + 3 篇 sections（frontmatter 元数据））。

【红线】
- 只动清单涉及文件；基于 fulltext 实测（PDF 用 pdftoppm 转图读取）
- 禁止编造 DOI / 摘要 / 逻辑词；禁止空话凑数（抽查不通过打回）
- 每项完成即自查（字段存在性 / 词条数）并如实报告实测数字
- 严禁执行任何"恢复 26 篇缺失论文 / 重建索引"类动作（P0 已证伪）
- abstract 与 vocab 为批量任务，可分多批提交，但每批 commit 只含本批文件
```

---

## 复验口径（WorkBuddy）

以下命令为各项验收的实测基准，Hermes 自评与 WorkBuddy 复验共用：

```bash
cd /Users/jcxs2014/Sites/HermesLocal/papers
files=$(find . -name '00_overview.md' -path '*/literature_analysis/*' | sort)
# frontmatter 字段存在性（在 --- 块内）
has_field(){ awk -v F="$1" 'BEGIN{fm=0} /^---[[:space:]]*$/{fm++; if(fm==2) exit; next} fm==1 && $0 ~ "^"F":"{print 1; exit}' "$2"; }

# Tier A 验收：下列字段缺失数应为 0
echo "DOI missing:    $(for f in $files; do [ -z "$(has_field doi $f)" ] && echo x; done | wc -l | tr -d ' ')"
echo "journal missing:$(for f in $files; do [ -z "$(has_field journal $f)" ] && echo x; done | wc -l | tr -d ' ')"
echo "sections missing:$(for f in $files; do [ -z "$(has_field sections $f)" ] && echo x; done | wc -l | tr -d ' ')"
echo "abstract missing:$(for f in $files; do [ -z "$(has_field abstract $f)" ] && echo x; done | wc -l | tr -d ' ')"

# Tier B2 验收：A 节逻辑词 <15 的篇数应为 0
echo "vocab A <15: $(for vf in $(find . -name '98_vocabulary*.md' -path '*/literature_analysis/*'); do
  r=$(awk '/^## A/{f=1;next} /^## /{if(f)exit} f&&/^\|/{if($0~/单词/)next; if($0~/^\|[\s:|-]+\|/)next; n++} END{print n+0}' "$vf");
  [ "$r" -lt 15 ] && echo x; done | wc -l | tr -d ' ')"
```

目标验收值：**DOI 0 / journal 0 / sections 0 / abstract 0（即 55/55）/ vocab A <15 = 0**。

若 Hermes 自报数字与实测不符、或 abstract/vocab 出现编造/空话凑数，打回。
