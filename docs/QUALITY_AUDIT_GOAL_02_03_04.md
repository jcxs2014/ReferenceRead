# 文献精读质量审查批次 2 —— 02/03/04 域一次性指令（分域提交）

> 生成：2026-08-18 00:00（WorkBuddy）
> 前置：QUALITY_AUDIT_GOAL.md（完整流程，v1.0）+ QUALITY_AUDIT_01 批试跑成功（01 域 7 篇，均分 25/30）
> 状态：本指令为一次性交付，Hermes 依次执行三域、分域提交，全程无需外部等待；WorkBuddy 事后统一复验

---

## /goal 触发指令（直接粘贴给 Hermes）

```
/goal 文献精读质量审查批次2：02/03/04 域逐篇审查（只审不改，分域提交）

【任务定位】
对 02 起源域、03 核合成域、04 实验域全部文献精读文档做质量审查并输出报告。
本任务只审查、不修改任何文献文件；禁止运行写文档脚本；禁止 cleanup/切分类操作。

【整体流程】依次执行三个域（顺序执行，不要并行）：
  02 起源域（20 篇）→ 03 核合成域（24 篇）→ 04 实验域（4 篇）
每完成一个域：
  1. 写该域报告：docs/QUALITY_AUDIT_02_ORIGINS_<YYYY-MM-DD>.md /
     docs/QUALITY_AUDIT_03_NUCLEOSYNTHESIS_<YYYY-MM-DD>.md /
     docs/QUALITY_AUDIT_04_EXPERIMENTS_<YYYY-MM-DD>.md
  2. git 提交：只 add 该报告文件（不 git add -A），message 如
     docs: QUALITY_AUDIT_02_ORIGINS 批次报告
  3. 直接进入下一域，无需等待外部确认
全部三域完成后，写一份 docs/QUALITY_AUDIT_BATCH2_SUMMARY.md 汇总（三域均分、
P0/P1/P2 统计、共性问题），提交。

【每篇 6 步】
1. 忠实性：抽 5–10 条 [FACT] 声明，逐条对照 fulltext 原文，标
   grounded/partial/hallucinated，后两者必须给原文页码 + 精读摘录作证据
2. 覆盖度：原文各章 vs 精读覆盖，输出 recall ≈ 覆盖章/总章 + 遗漏/浅覆盖清单
3. 密度：check_density.py + wc -l 实测行数（综述≥800/研究型≥500，不采信自报）；
   分章与 00_overview 相似度<10%（防搬运）
4. 解读抽查：随机抽 ≥3 段判"复述 vs 解读批判"；3 段全复述 → 深度不足
5. 格式：§0.3 统一「论文结构树」；97 无"需人工确认"占位；表格列数一致；
   公式可渲染（查 .katex-error/空基数上标/裸<后跟字母）
6. 评分：六维（忠实/覆盖/深度/密度/结构/规范）各 1–5，先列依据再给分；
   禁止因文档长/格式好看/语气自信给高分

【每域报告要求】
- 头部带 git rev-parse HEAD + 时间戳快照
- 每篇一节：六维分数表（附 rationale）+ P0/P1/P2 问题清单
  （P0=事实错误/整段遗漏；P1=深度/格式违规；P2=优化建议）+ 忠实性明细 + 覆盖度 recall
- 末尾：该域统计（分数、P0/P1/P2 数量、共性问题）

【红线与已知更新】
- 只审不改；禁 cleanup；禁"需人工确认"占位；拿不准的如实标注不要猜
- 97 公式统计 bug 已修复（commit f87d9a2）——97_quality_check.md 的"公式"字段
  现在是真实值，审查时可直接引用
- 标杆校准：02 域内的 0008_bell-1978 即标杆篇（01 批已用它校准过），02 域
  批次继续以它为"5 分基准"；03/04 域沿用同一标准
- 00_overview 相似度检查用 n-gram 重叠率（去空白）；PDF 提取用 pdftoppm 转图读取

【各域清单】
02 起源域 20 篇：
0001_bhattacharjee-sigl-2000、0002_al-dargazelli-1996、0003_gaisser-1990、
0004_blasi-2013、0005_amato-2014、0006_grenier-2015、0007_biermann-1996、
0008_bell-1978、0009_blandford-ostriker-1978、0010_blandford-eichler-1987、
0011_hillas-1984、0012_gabici-2019、0013_giuffrida-2022、0014_alvesbatista-2019、
0015_telescope-array-2023、0016_caprioli-2014、0017_caprioli-2014-ii、
0018_kotera-olinto-2011、0019_bell-1978-ii、0020_giacalone-2017

03 核合成域 24 篇：
0001_b2fh-1957、0002_trimble-1975、0003_fowler-1984、0004_wallerstein-1997、
0005_champagne-wiescher-1992、0006_anders-grevesse、0007_grevesse-sauval-1998、
0008_lodders-2003、0009_asplund-2009-solar-composition、0010_gies-lambert-1992、
0011_kewley-2001-starburst、0012_dieterich-2014-h-burning-limit、
0013_bertone-hooper-2018、0014_cameron-1968、0015_kraft-1994、0016_cowan-2021、
0017_kaeppeler-2011、0018_arnould-goriely-2003、0019_sneden-cowan-2008、
0020_nomoto-2013、0021_karakas-lattanzio-2014、0022_busso-1999、
0023_eichler-1989、0024_nomoto-suzuki-2014

04 实验域 4 篇：
0001_lhaaso-2021、0002_ams02-2015、0003_icecube-2013、0004_hess-2016

【交付后】三域全部完成并提交 SUMMARY 后，任务结束。等待 WorkBuddy 复验。
```

---

## 备注（给 WorkBuddy 复验用）

- 复验口径与 01 批一致：行数 7 篇抽验 vs 实测、忠实性声明抽 1–2 条对照 fulltext、P 问题抽查
- 重点复核对象：02 域 0010_blandford-eichler-1987、03 域 0009_asplund-2009 等大型综述篇的行数；03 域 0004_wallerstein（今天修过公式）的忠实性
- 三域报告应各自独立提交，SUMMARY 最后提交；检查 git log 确认提交粒度
