> 本章属于：Solar System Abundances and Condensation Temperatures of the Elements (Lodders 2003)
>
> 上一章：[[03_stellar-nucleosynthesis/0008_lodders-2003/literature_analysis/00_overview.md|00_overview.md]]
>
> 下一章：[[03_stellar-nucleosynthesis/0008_lodders-2003/literature_analysis/02_abundance_selection.md|02_abundance_selection.md]]

# 1. Introduction（p. 1220–1221）

## 1.1 本节核心内容
作者阐述冷凝温度（T_C）在天文学、行星科学、陨石学中的诊断地位，指出既有冷凝温度表的混乱来源，以及 Allende Prieto et al. (2001, 2002) 对太阳 C、O 丰度的大幅下调如何触发本文的必要性。

## 1.2 原文内容与历史背景
[FACT] 冷凝温度（元素从太阳成分气相中首次凝固的温度）被广泛用于诊断化学分馏过程。文献脉络：
- Wildt (1933)、Russell (1934)：最早尝试太阳与冷恒星的热化学计算，含凝析项；
- Lord (1965)：恢复该主题；
- Larimer (1967, 1973)、Grossman (1972)、Grossman & Larimer (1974)、Boynton (1975)、Wai & Wasson (1977, 1979)、Sears (1978)、Fegley & Lewis (1980)、Saxena & Eriksson (1983)、Fegley & Palme (1985)、Kornacki & Fegley (1986)、Palme & Fegley (1990)：系统工作；
- Ebel & Grossman (2000)：在多种星云条件下重算主要岩石形成元素的冷凝。

[FACT] 作者指出既有冷凝温度表是"melange"（大杂烩）：
1. 数据来源跨越 1970s–1980s，来源混杂；
2. 混合"冷凝温度"与"50% 冷凝温度"两种不同定义，难以直接比较；
3. 对某些元素（Rb, Cs, F, Cl, Br, I, Bi, In, Hg, Pb, Sn, Tl）的冷凝温度未知或不可靠；
4. 各研究使用的太阳成分与热力学数据不同，随着二者更新，冷凝温度也应重算。

## 1.3 触发本文的直接原因：C、O 向下修订

[FACT] Allende Prieto, Lambert & Asplund (2001, 2002) 大幅下调太阳 C、O 丰度（相对 Anders & Grevesse 1989 约低 1.4–1.7 倍）：
- C、O 是控制大部分其他元素化学的两个最丰富的元素；
- 绝对 O 丰度降低 → 含 O 化合物的冷凝温度降低；
- C/O 比也影响冷凝温度（C/O 越接近 1，氧化物与硅酸盐冷凝温度越低，初始氧化物/硅酸盐冷凝物被含 C 化合物取代）。

[FACT] Allende Prieto et al. 给出的 C/O ≈ 0.50，比 Grevesse & Sauval (1998) 的 0.49 略高、比 Anders & Grevesse (1989) 的 0.42 明显更高。

[FACT] S、P 等其他元素丰度的变化也会同步改变它们的冷凝温度。

## 1.4 研究目标
[FACT] 本文提供：
1. 更新后的太阳大气元素丰度表（表 1）；
2. 原始太阳 = 太阳系丰度表（表 2），考虑 He 与重元素沉降；
3. 太阳系同位素丰度表（表 6）；
4. 与两套丰度自洽的冷凝温度表（表 7–11）。

## 1.5 研究动机（深层）

[FACT] **问题 1（历史）**：此前把"太阳大气丰度"当作"太阳系丰度"使用，忽略了太阳内部的分馏（He 与重元素沉降）。Lodders 2003 明确纠正了这一传统做法。

[FACT] **问题 2（技术）**：既有冷凝温度表混合两套不同定义，混合多个时代的太阳成分，缺乏自洽性。

[FACT] **问题 3（触发事件）**：C、O 新丰度使金属度 Z 显著下降（Z/X 从 0.0245 降到 0.0177），冷凝温度与冷凝产物分布必然随之改变。

## 1.6 作者的论证链

```
历史问题（混合冷凝温度表）
  → 触发事件（C、O 向下修订）
    → 研究目标（重算自洽丰度 + 冷凝温度）
      → 关键认识（大气丰度 ≠ 太阳系丰度；必须考虑沉降）
        → 方法（CONDOR 化学平衡代码 + 陨石 + 太阳光谱 + SSM）
          → 输出（两套自洽的丰度表与冷凝温度表）
```

## 1.7 我的理解

[INTERPRETATION] 引言虽然篇幅不长，但完成了三件关键事：
1. 把本文放在"50 年冷凝温度研究"的长脉络中，说明它不是孤立工作；
2. 明确"自洽"是本文的方法论核心（丰度 + 冷凝温度必须同源）；
3. 提出沉降问题，为§ 2.3.1.1 中利用 SSM 重算 Y₀/Z₀ 埋下伏笔。

[CRITIQUE] 引言未提及 Fegley 与 Lodders 自己 1993、1995、1997、2000 年已完成的 CONDOR 重算工作——但正文§ 3.1 与参考文献中充分引用。这是"综述性引言"常见倾向。