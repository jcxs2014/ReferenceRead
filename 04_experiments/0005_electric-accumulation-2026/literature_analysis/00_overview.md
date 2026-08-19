---
title: "Electric Accumulation of Millicharged Particles"
authors: "Asher Berlin, Zachary Bogorad, Peter W. Graham, Harikrishnan Ramani"
year: 2026
journal: "Physical Review D"
volume: 114
issue: 1
pages: 015016
doi: "10.1103/physrevd.114.015016"
arxiv: "arXiv:2510.25825"  # companion paper; PRD version arXiv pending
path: 04_experiments/0005_electric-accumulation-2026
read_date: '2026-08-19'
lastread: '2026-08-19'
status: completed
citations:
  - "0006_cavendish-millicharge-2026"
  - "0002_ams02-2015"
  - "0003_icecube-2013"
---

# 0. 文献基本信息

## 0.1 论文核心摘要

**[FACT]** 本文提出一种概念简单但威力巨大的实验方案：利用带固定电压的导体壳（例如 Van de Graaff 发电机）在室温环境里高效"捕获"已热化到环境温度（~300 K）的 milli-charged particles (mCPs)，将局部密度提升高达约 $$10^{12} \times (t/\text{yr})$$ 倍，即 12 个数量级。壳层内部的感应电场几乎为零，因此可内嵌精密探测器（如离子阱、Cavendish 型实验）以测量 mCP 的超额密度。

**[FACT]** mCPs 的有效电荷量级 $$q_\chi \lesssim 10^{-1}$$，可由暗光子与 SM 光子的 kinetic mixing $$\mathcal{L} \supset \frac{\epsilon}{2} F'_{\mu\nu}F^{\mu\nu}$$ 自然生成，此时 $$eq_\chi \simeq \epsilon e'$$。GeV 质量尺度下，仍有 $$q_\chi \sim 10^{-1}$$ 的参数空间未被排除。

**[FACT]** mCPs 在地球上可通过两类渠道产生：(1) DM subcomponent，即作为暗物质的小比例成分被宇宙学演化遗留到现今；(2) 不可约 (irreducible) 的宇宙线大气级联产生，与宇宙学无关，探测即等于"加速器等效"的模型测试。

**[FACT]** 地球大气电场 $$E_\oplus \sim 1\,\text{V/cm}$$ 在电离层与地壳之间维持约 $$\phi_\oplus \sim 0.3\,\text{MV}$$ 的电势差，对 $$q_\chi \gtrsim 10^{-7}$$ 的正 mCPs 形成天然的"电气陷阱"。

**[FACT]** 本文在 companion paper [21] (PR Lett. 137, 021804, 2026) 中将此方案具体化为 Cavendish 型库仑定律检验实验，声称可达到超越未来加速器对 sub-GeV mCPs 的灵敏度。

## 0.2 全文结构树

```
Electric accumulation of millicharged particles
├── I. INTRODUCTION (L26-L118)
│     [背景] SM 不完备；mCP 扩展简单但未被约束
│     [主张] 带电壳层可将局部 mCP 密度提升 12 个量级
│     [结构预告]
├── II. MODEL OVERVIEW (L119-L183)
│     [动能混合] L ⊃ ε/2 F'F − j'A'
│     [直接耦合 vs 暗光子介导]
├── III. TERRESTRIAL POPULATION (L184-L654)
│     [总述] 地球上的 mCP 热化与密度
│     ├── A. Dark matter subcomponent (L350-L429)
│     └── B. Irreducible cosmic-ray population (L430-L654)
├── IV. ACCUMULATION IN THE LAB (L655-L1156)
│     [核心公式] n_trap ≃ 3 ε n_χ V_E t / R₀
│     ├── A. Indoors vs outdoors (L793-L987)
│     └── B. Electrical trapping (L988-L1156)
├── V. RESULTS (L1157-L1511)
├── VI. CONCLUSION (L1512-L1550)
├── Appendix A: Accumulation (L1581-L1809)
└── Appendix B: Diffusion and Drift (L1810-L1876)
```

## 0.3 关键术语速查

| 缩写 | 全称 |
|------|------|
| mCP | millicharged particle |
| DM | dark matter |
| SM | Standard Model |
| A' | dark photon |
| q_χ | effective charge of χ in units of e |
| ε | kinetic mixing parameter |
| e' | dark gauge coupling |
| n_χ | terrestrial mCP number density |
| n_trap | mCP density inside accumulator |
| V_E | electric accumulation velocity |
| Γ_p | momentum-exchange rate |
| Γ_E | energy-exchange rate |
| φ₀ | shell voltage (negative) |
| R₀ | shell radius |
| E_⊕ | atmospheric electric field |
| ϕ_⊕ | atmospheric voltage difference |
| f_DM | DM subcomponent fraction |
| t_⊕ | age of the Earth ≈ 4.5 × 10⁹ yr |

## 0.4 分析文件清单

| 文件 | 覆盖章节 | 八段模板 |
|------|----------|----------|
| 00_overview.md | 本文档 | frontmatter + 结构 |
| 01_model_and_introduction.md | §I + §II | 8 段 |
| 02_terrestrial_population.md | §III + A/B | 8 段 |
| 03_accumulation_in_the_lab.md | §IV + A/B | 8 段 |
| 04_results.md | §V | 8 段 |
| 05_conclusion.md | §VI | 8 段 |
| 06_appendix_a.md | Appendix A | 8 段 |
| 07_appendix_b.md | Appendix B | 8 段 |
| 08_references.md | 参考文献 | 分类索引 |
| 97_quality_check.md | 质量自查 | checklist |
| 98_vocabulary.md | 词汇/术语 | 学术词表 |
| 99_final_summary.md | 总结 | 综合评估 |

---
*生成时间：2026-08-19；数据来源：fulltext.txt (2076 lines, 86549 chars)*
