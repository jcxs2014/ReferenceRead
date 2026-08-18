# 专项补深 goal —— blandford-eichler-1987（75 页综述 → ≥3000 行）

> 生成：2026-08-18 10:39（WorkBuddy）
> 背景：C6 两轮均未达验收（第1轮 1548 行仅加标注；第2轮 1628 行补了核心物理推导但仍 <3000）
> 定位：**单篇专项长时补深 goal，允许修改文献**；无严格时限，按章节分批推进、分批提交
> 实测基线：当前 1628 行（WorkBuddy 2026-08-18 10:21 实测，非 Hermes 自报的 1361）

---

## /goal 触发指令（直接粘贴给 Hermes）

```
/goal 专项补深：blandford-eichler-1987 精读从 1628 行补到 ≥3000 行（75 页综述）

【任务定位】
对 02_cosmic-ray-origins/0010_blandford-eichler-1987 的精读文档做专项补深。
该篇是 Blandford & Eichler (1987) 75 页顶级综述（Physics Reports），
当前精读 1628 行（WorkBuddy 实测基线），目标 ≥3000 行（综述精读合理深度，
参照同库 ruszkowski-2023 50 页综述 1826 行的比例，75 页 ≈ 2700-3000 行）。
允许修改该篇 literature_analysis/ 下文件；禁止动其他文献文件。

【执行前】git fetch + git log --oneline -3 确认工作树最新；wc -l 实测
当前基线行数（应为 ~1628，以实测为准，不要引用旧数字）。

【方法与节奏（分批推进，每批提交）】
按精读章节分批补深，建议批次：
  批1：01_introduction + 02_observational_background（当前 107+205 行）
  批2：03_diffusion_approximation + 04_test_particle_approximation（242+207）
  批3：05_wave_spectrum + 06_nonlinear_theory（162+195）
  批4：07_summary 收尾 + 全篇自查
每批完成即 git 提交（只 add 该篇文件），message 如
fix: blandford-eichler 专项补深批1（01/02章 +N行）

【每章补深内容要求（参照 ruszkowski-2023 精读质量）】
- 物理机制展开：不仅列结论，给出推导链/物理图像/关键假设
- 历史与动机：为什么引入该概念（原文章节背景）
- 观测对比：理论预测 vs 观测证据
- 标注分散：[FACT]/[INTERPRETATION]/[CRITIQUE] 均匀分布各章
  （当前全篇 11 条 CRITIQUE 偏少，目标各章 ≥3 条 CRITIQUE）
- 公式分散：现有 347 条公式不得集中在少数文件，补深时公式随内容落位

【验收】
1. wc -l 实测 ≥3000 行（全部 md 文件合计）
2. 各正文章节 CRITIQUE ≥3 条、标注密度合理（对照 bell-1978）
3. 公式分布均匀（无"集中在末尾"现象）
4. 无"需人工确认"占位；公式可渲染（无 .katex-error）
5. 内容基于 fulltext 实测（PDF 用 pdftoppm 转 PNG 逐页读），禁止编造数值/结论

【红线】
- 只动 0010_blandford-eichler-1987/literature_analysis/ 下文件
- 数字如实：每次提交前 wc -l 实测并写在 commit message（禁止自报错误数字）
- 分批推进，禁止一次性全改后提交一个巨型 commit
- 本 goal 无时限，可跨多轮执行；每批完成后简短汇报进度（当前行数/剩余目标）
```

---

## 复验口径（WorkBuddy）

- 每批提交后核实行数增量与内容真实性（抽查新增段落是否来自 fulltext）
- 最终验收：wc -l ≥3000、CRITIQUE 分布、公式分布、无占位、公式渲染 0 错误
- 若再次出现"自报数字与实测不符"，直接打回并要求以 wc -l 为准
