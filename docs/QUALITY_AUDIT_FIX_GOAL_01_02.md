# 精读质量修复 goal —— 批次1+2 真实 P0/P1 清单（允许修改文献）

> 生成：2026-08-18 09:05（WorkBuddy）
> 依据：QUALITY_AUDIT_01（7 篇）+ QUALITY_AUDIT_02/03/04（48 篇）审查报告，经 WorkBuddy 复验剔除误报
> 定位：**本 goal 允许修改文献精读文件**（与审查 goal"只审不改"相反）；按清单逐项修复、分项提交
> 样板参照：bell-1978 的 `05_critical_assessment` 批判章节 + 综述精读深度标准

---

## /goal 触发指令（直接粘贴给 Hermes）

```
/goal 精读质量修复：批次1+2 真实 P0/P1 清单逐项修复（允许修改文献，分项提交）

【任务定位】
按下方清单逐项修复文献精读文档。本任务允许修改 literature_analysis/ 下的
精读文件；禁止修改与清单无关的文件；禁止删除文件；禁止 cleanup。

【执行前】git fetch + git log --oneline -5 确认工作树最新；
每项修复前 git status 确认工作区干净；修复后自查：
- 行数/结构达标（见每项验收）
- 公式可渲染（无 .katex-error；PDF 提取用 pdftoppm 转图）
- 无"需人工确认"占位
提交：按"项"分组提交，只 add 本项涉及文件（不 git add -A），
message 如 fix: 补充 amato-2014 批判章节（P1）

【A 组 · 阻塞项（先做）】
1. bell-1978-ii（02域）fulltext 重抽 + 补内容
   - fulltext.txt 仅 39 行（PDF 下载头部，无正文）→ 从 arXiv 1408.3338 或 ADS
     重抽全文（pdftoppm 转 PNG 逐页读，防混入邻页/OCR 错漏）
   - 补 §98_vocabulary（现 21 行）与 §99_final_summary（现 16 行）
   - 补 §0.3 论文结构树节
   - 验收：fulltext ≥ 500 行有效正文；§98/§99 各 ≥ 80 行；结构树节存在；
     忠实性可重新验证（对照新 fulltext 抽 3 条 [FACT]）

【B 组 · 补批判章节（参照 bell-1978 的 05_critical_assessment 模式）】
2. amato-2014（02域）：CRITIQUE 仅 12 条（Blasi 2013 有 37 条），多节仅 1 条
   → 各正文章节补 [CRITIQUE]，新增或强化批判性分析段
3. blasi-2013（02域）：无统一批判章节 → 补 05_critical_assessment 类章节
4. biermann-1996（02域）：无批判章节 → 同上
5. al-dargazelli-1996（02域）：§2.2 与 §8 表述张力（EG质子 vs 重核主导）
   无批判收束 → 补批判章节收束；统计显著性量化（补 σ 值）
   → 验收：各篇新增批判内容 ≥ 10 条 [CRITIQUE] 或 1 个批判章节

【C 组 · 补深（覆盖/展开不足）】
6. blandford-eichler-1987（02域）：75 页综述仅 1524 行（ratio 37%），
   正文 [FACT]/[INTERP]/[CRITIQUE] 各仅 3 条 → 补正文分章（目标 ≥ 3000 行，
   综述标准）并分散标注
7. blandford-ostriker-1978（02域）：正文 [FACT]/[INTERP]/[CRITIQUE] 各仅 3 条
   （995 行）→ 补标注与展开；公式 347 条集中在末尾 → 分散到对应章节
8. kotera-olinto-2011（02域）：§00 仅 43 行（缺关键词/结构树/基础信息表）、
   §98 仅 47 行、§07 合并双章 → 补 §00/§98，拆分 §07
9. telescope-array-2023（02域）：§05 结论仅 66 行 → 补深
10. caprioli-2014（02域）：§05/§07/§09 各仅 35/34/28 行 → 补深
11. weinrich-2020（01域）：ratio 46%（534 vs 1162 行），results 展开不足 → 补深
12. genolini-2021（01域）：03_statistical_method 仅 74 行 → 补深
    → 验收：各篇目标行数达成（综述 ≥800 / 研究型 ≥500）；补的章节内容
     来自 fulltext 实测（非模板填充）

【D 组 · 澄清/修正】
13. gaisser-1990（02域）：Eq.(1) 数值与超新星供给功率数量级差异未澄清；
    air-shower 模型依赖未给定量误差 → 补澄清说明（对照 fulltext 实测）
    → 验收：差异有解释（数值核对 + 说明），非含糊带过

【提交顺序】A → B → C → D 依次执行，每组完成后提交；全部完成后汇总说明。

【红线】
- 只动清单涉及文件；PDF 提取 pdftoppm；fulltext 重抽后检查邻页混入
- 修复内容必须基于 fulltext 实测，禁止编造数值/结论
- 每项完成即自查（行数/公式渲染/无占位）并在 commit message 注明验收结果
```

---

## 清单来源与剔除说明（给 WorkBuddy 复验用）

- 批次2 报告 P1 16 条 → 剔除 2 条误报：hillas `\rac`（dcf41c1 已修）、
  bhattacharjee longair（文档自注非误记）→ 剩 14 条
- 批次1 P1 3 条 → 剔除 97 公式 bug（f87d9a2 已修）→ 剩 2 条
- 合计真实 P1：14 + 2 = 16 条（含 bell-1978-ii 的 §98/§99/结构树并入 A 组第 1 项）
- P0：1 项（bell-1978-ii fulltext）并入 A 组
- P2 未列入本 goal（03 域 11 篇深度类 + strong §III 等，作为后续优化轮）
