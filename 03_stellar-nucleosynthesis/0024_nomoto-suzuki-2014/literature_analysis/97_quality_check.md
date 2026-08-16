---
title: "97 Quality Check"
paper: "nomoto-suzuki-2014"
---

上一章：`10_conclusion.md`
下一章：`98_vocabulary.md`

# 97. Quality Check — 精读质量检查

## A. 元数据核查

| 检查项 | 结果 | 备注 |
|---|---|---|
| 作者 (PDF p.1) | ✅ 已验证 | K. Nomoto & T. Suzuki（双作者） |
| 目录名 | ✅ 一致 | `0024_nomoto-suzuki-2014` = PDF 作者 |
| 年份 | ✅ 一致 | PDF 版权 2014 (IAU Symp. 298, 会议 2013) |
| 页码 | ⚠️ 任务上下文偏移 +1 | 任务给 155–167，PDF 实际 **154–166**（已在 `00_overview.md` 勘误） |
| DOI | ✅ 一致 | 10.1017/S1743921313006327 |
| 会议编号 | ✅ 已验证 | IAU Symposium **No. 298** (Setting the scene for Gaia and LAMOST) |

## B. 章节覆盖

| 章节 | 覆盖 | 对应文件 |
|---|---|---|
| §1 Introduction | ✅ | `01_introduction.md` |
| §2 Progenitor's Mass and Explosion Energy | ✅ | `02_progenitor_energy.md` |
| §3 8–10 M☉ EC-SNe | ✅ | `03_8_10msun_ecsn.md` |
| §4 10–13 M☉ Faint SNe | ✅ | `04_10_13msun_faint.md` |
| §5 13–25 M☉ Normal SNe | ✅ | `05_13_25msun_normal.md` |
| §6 25–140 M☉ HN & Faint | ✅ | `06_25_140msun_hn_faint.md` |
| §7 Very Massive Stars (PISN+IMBH) | ✅ | `07_very_massive_stars.md` |
| §8 EMP Profiling (5 子节) | ✅ | `08_emp_profiling.md` |
| §9 Yield Tables | ✅ | `09_yield_tables.md` |
| §10 Concluding Remarks | ✅ | `10_conclusion.md` |
| References | ✅ | 56 条参考文献在 `10_conclusion.md` 汇总 |

## C. 图表覆盖

| 图表 | 覆盖 |
|---|---|
| Fig. 1 (left) Pop III 吸积演化 | ✅ `02_progenitor_energy.md` |
| Fig. 1 (right) E–M 双分支图 | ✅ `02_progenitor_energy.md`、`06_25_140msun_hn_faint.md` |
| Fig. 2 (a) 25 M☉ E₅₁=1 正常 SN | ✅ `06_25_140msun_hn_faint.md`、`08_emp_profiling.md` |
| Fig. 2 (b) 25 M☉ E₅₁=10 HN | ✅ 同上 |
| Fig. 3 四类 SN 产额对比 | ✅ `07_very_massive_stars.md`、`00_overview.md` |
| Fig. 4 (left) VMP vs. SN+HN 积分 & PISN | ✅ `08_emp_profiling.md` |
| Fig. 4 (right) EMP vs. SN vs. HN | ✅ `08_emp_profiling.md` |
| Fig. 5 (a–d) EMP/CEMP/UMP/HMP 与模型对比 | ✅ `08_emp_profiling.md` |
| Nomoto 2013 在线产额表 | ✅ `09_yield_tables.md` 详述规格 |

## D. 关键数值核查（与 PDF 比对）

| 数值 | 声明 | 来源 PDF 行 |
|---|---|---|
| E₅₁ > 10 定义为超新星 | ✅ §1.3 | PDF L71 |
| GRB-SNe E₅₁ = 30–50、⁵⁶Ni = 0.3–0.5 M☉ | ✅ §2.2 | PDF L118 |
| EC-SN E ≈ 10⁵⁰ erg (E₅₁ ≈ 0.1) | ✅ §3.2 | PDF L151 |
| EC-SN ⁵⁶Ni = 0.002–0.004 M☉ | ✅ §3.3 | PDF L160 |
| 64Zn 事件占所有 CC-SNe ≤ 20% | ✅ §3.3 | PDF L157 |
| 90–140 M☉ ⁵⁶Ni 上限 ≈ 10 M☉ | ✅ §6.4 | PDF L289 |
| PISN ⁵⁶Ni 上限 ≈ 40 M☉ | ✅ §7.1 | PDF L315 |
| Fig. 5 五颗 SN 模型的 (E₅₁, M(⁵⁶Ni)) | ✅ §8.3–8.5 | PDF L470–473 |
| Nomoto 2013 表 Z=0 质量网格 (11,13,15,18,20,25,30,40,100) | ✅ §9.3 | PDF L548 |
| HN 表 (M, E₅₁) 网格 | ✅ §9.3 | PDF L554–556 |

## E. 引用完整性

| 引用 | 在文中出现 | 已记录 |
|---|---|---|
| Umeda & Nomoto 2002 | ✅ | ✅ |
| Tominaga et al. 2007a/b, 2013a/b | ✅ | ✅ |
| Iwamoto et al. 2005 | ✅ | ✅ |
| Heger & Woosley 2002, 2010 | ✅ | ✅ |
| Ohkubo et al. 2006, 2009 | ✅ | ✅ |
| Beers & Christlieb 2005 | ✅ | ✅ |
| Nomoto et al. 2013 (ARAA) | ✅ | ✅ (本库 `0020_nomoto-2013`) |
| B²FH 1957 | ⚠️ 未在本篇正文中被引用（但父库关系存在） | ✅ 已在 `00_overview.md` citations 保留 |

## F. 交叉导航

- 每章均有 `上一章` / `下一章` 链接 ✅
- `00_overview.md` 含完整章节树与图表索引 ✅

## G. 已知局限

1. **篇幅限制**：本文是 IAU 短综述（13 页），不含公式推导；详细理论请见母综述 `0020_nomoto-2013`
2. **表格缺失**：文中**无正式表格**——Nomoto 2013 在线产额表以**外部 URL**形式给出，本文中仅给出 (M, Z) 规格；详细数值表**未含在 PDF 中**
3. **任务上下文勘误**：pages 由 155–167 更正为 154–166
