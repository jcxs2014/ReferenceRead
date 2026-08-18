# P2 优化轮 goal —— 03 域综述解读补强 + strong §III + 公式密度 + giacalone

> 生成：2026-08-18 10:48（WorkBuddy）
> 依据：QUALITY_AUDIT 批次1/2 审查报告 P2 项（已剔除被 B/C 组修复覆盖的 blasi/biermann 批判章节、blandford-eichler/kotera 薄覆盖）
> 基线：WorkBuddy 2026-08-18 10:48 实测（见各项目标，以 wc -l/grep 实测为准）
> 定位：**允许修改文献**；P2 为优化建议——验收标准是"实质提升 + 可量化"而非硬门禁，但同样要求基于 fulltext 实测、禁编造、分项提交

---

## /goal 触发指令（直接粘贴给 Hermes）

```
/goal P2 优化轮：03 域综述解读补强 + strong-2007 §III + grevesse-sauval 公式密度 + giacalone 细节（允许修改文献，分项提交）

【任务定位】
按下方清单对 P2 项做优化。P2 是审查报告的优化建议，验收标准 = 标注密度
达到参照水平 + 内容基于 fulltext 实测。允许修改目标篇 literature_analysis/
下文件；禁止动其他文献文件；禁止删除文件。

【执行前】git fetch + git log --oneline -3 确认工作树最新；
每项修复前 wc -l / grep -c 实测基线（不要引用旧数字）；完成后自查。

【P2-A：03 域综述 INTERPRETATION 补强（11 篇）】
目标篇与当前 INTERP/FACT 基线（实测）：
  fowler-1984（8/317）、anders-grevesse（9/154）、kewley-2001（8/104）、
  dieterich-2014（7/82）、b2fh-1957（15/250）、busso-1999（12/129）、
  trimble-1975（31/169）、gies-lambert-1992（24/161）、cameron-1968（28/166）、
  grevesse-sauval-1998（10/40）、nomoto-suzuki-2014（P2 未列但可顺带）
要求：
  1. INTERP 偏低的 6 篇（fowler/anders-grevesse/kewley/dieterich/b2fh/busso）
     补 [INTERPRETATION] 至 ≥20 条（参照 trimble 31/169、cameron 28/166 水平）
  2. 各篇 CRITIQUE 补至 ≥10 条（fowler 30/busso 10 已达标篇除外）
  3. INTERPRETATION 内容须有实质（物理意义解读/跨文献联系/局限讨论），
     禁止为凑数写空话——抽查 3 条判定
验收：目标篇 INTERP ≥20 或 ≥现状+10；CRITIQUE ≥10；抽查无空话

【P2-B：strong-2007 特殊专题 + 标注补强（01 域）】
基线：2194 行 / FACT 229 / INTERP 2 / CRIT 2 ——标注几乎为零（最严重）
要求：
  1. 基于 fulltext §III（Special Topics）补独立章节：
     电子传播与同步辐射、宇宙线各向异性（如原文有对应小节）
  2. 03_figures.md 从纯 figure 列表展开为"图 + 内容解读"
  3. 全篇补 [INTERPRETATION] ≥20 条、[CRITIQUE] ≥15 条（分布各章）
验收：§III 新章节存在且 ≥150 行；03_figures 有内容解读；标注达标

【P2-C：grevesse-sauval-1998 公式密度（03 域）】
基线：78 公式 / 961 行（密度 6.3/千行，域内偏低）
要求：补关键公式展开（丰度标度/质量分数/对数丰度定义等，基于 fulltext）
验收：公式数 ≥150（含 block+inline）

【P2-D：giacalone-2017 细节（02 域）】
基线：856 行 / INTERP 9 / CRIT 5
要求：补 INTERPRETATION ≥15 条、CRITIQUE ≥10 条 + 关键细节展开
验收：标注达标 + 行数 ≥1000

【提交】分项提交（P2-A 按篇分组、P2-B/C/D 各一 commit），
只 add 本项文件（不 git add -A）；commit message 注明实测数字
（如 fix: P2 fowler-1984 解读补强 INTERP 8→22 条）

【红线】
- 只动清单涉及文件；基于 fulltext 实测（PDF 用 pdftoppm 转图）
- 禁止编造数值/结论；禁止空话凑数（抽查不通过打回）
- 每项完成即自查（标注数/公式渲染/无占位）并如实报告
- P2 不设硬行数门槛（行数只作参考），核心是标注密度与内容实质
```

---

## 复验口径（WorkBuddy）

- P2-A：目标 6 篇 INTERP ≥20 或 +10、CRITIQUE ≥10，抽查 3 条 INTERP 无空话
- P2-B：§III 章节存在 ≥150 行、03_figures 有解读、INTERP ≥20/CRIT ≥15
- P2-C：grevesse-sauval 公式 ≥150
- P2-D：giacalone INTERP ≥15/CRIT ≥10、行数 ≥1000
- 若再次出现自报数字与实测不符 / 空话凑数，打回
