---
title: '07. ASTROPHYSICAL WEAK-INTERACTION RATES (Fowler §VII)'
authors: William A. Fowler
year: '1984'
journal: Reviews of Modern Physics 56, 149 (1984) — Nobel Lecture
doi: '未提供（诺贝尔特刊，版权属 THE NOBEL FOUNDATION 1984）'
category: 恒星核合成
chapter: §VII
sections:
  - 'VII. ASTROPHYSICAL WEAK-INTERACTION RATES'
status: completed
read_date: '2026-08-15'
lastread: '2026-08-15'
path: 03_stellar-nucleosynthesis/0003_fowler-1984/literature_analysis/07_weak_rates.md
---
# 7. ASTROPHYSICAL WEAK-INTERACTION RATES (Sec. VII)

> 本章属于：**William A. Fowler (1984), *Experimental and theoretical nuclear astrophysics: the quest for the origin of the elements*, Rev. Mod. Phys. 56, 149–172**
>
> 上一章：[[03_stellar-nucleosynthesis/0003_fowler-1984/literature_analysis/06_advanced_burning.md|06_advanced_burning.md]]
>
> 下一章：[[03_stellar-nucleosynthesis/0003_fowler-1984/literature_analysis/08_abundances_explosive.md|08_abundances_explosive.md]]

## 7.1 本节核心内容

[FACT] 弱核相互作用在恒星演化、坍缩与爆炸中与强相互作用**协同作用**——**只有弱相互作用能改变核物质的总质子数和总中子数**。

[FACT] 中子星的形成**要求**普通恒星物质中的质子通过**电子俘获**转化。

[FACT] Type-II 超新星核心引力坍缩**只要电子还在向外提供压力就被延迟**。

## 7.2 Fuller-Fowler-Newman (FFN) 数据库

[FACT] 数十年理论+实验工作 culminating 于 Fuller, Fowler, Newman (1980, 1982a, 1982b) 的**系统计算与制表**：

- **电子与正电子发射速率**
- **连续电子与正电子俘获速率**
- **关联的中微子能量损失率**

覆盖：
- **自由核子**
- **226 个原子核**，质量数 **A = 21–60**
- 向更高/更低的 Z 值扩展正在进行

## 7.3 实验基础：Gamow-Teller 矩阵元

[FACT] FFN 的计算**严重依赖** Kellogg Lab 的 Wilson, Kavanagh, Mann (1980) 对**中质量核中 87 个离散跃迁的 Gamow-Teller 元**的实验测定。

[FACT] **大部分 Fermi 与 Gamow-Teller 离散跃迁的实验矩阵元以及核能级数据**取自 Lederer & Shirley (1978) 的全面汇编。

[FACT] 对未测量的允许跃迁矩阵元，分配**平均值**（Fuller, Fowler, Newman 1982a）：
```
⟨|M_F|$^{2}$⟩ ≈ 0.062
⟨|M_GT|$^{2}$⟩ ≈ 0.039
对应 log ft = 5，其中 f 为相空间因子，t 为半衰期
```

## 7.4 Tz 核与 GT 求和规则

[FACT] 通过简单壳模型论证估计**Gamow-Teller 求和规则与集体态共振激发能**——这些对 **Tz 核** 和 **T+ 核** 是合理近似（由 Goodman et al. 1980 与 Ajzenberg-Selove et al. 1984 的 p,n 与 T,$^{3}{\rm He}$ 反应高分辨测量验证）。

[FACT] 文中定义 T 为同位旋，例如 $^{54}{\rm Fe}$ 中 T=2（对 $^{54}{\rm Fe}$(e,$\nu$)$^{54}{\rm Mn}$ 或 $^{54}{\rm Fe}$(n,p)$^{54}{\rm Mn}$），$^{55}{\rm Mn}$ 中 T=3。

[FACT] Bloom & Fuller (1984) 使用 LLNL 的 vector shell model 代码对 $^{54}{\rm Fe}$, $^{56}{\rm Fe}$, $^{58}{\rm Fe}$ 的基态与第一激发态做了**动量方法（moment method）的 GT 强度函数计算**——确认 FFN 近似的总体趋势。

## 7.5 温度密度依赖

### 离散态贡献（准静态阶段）

[FACT] 离散态贡献**由 Fermi 跃迁的实验信息主导**，决定**超新星前准静态演化阶段的弱核速率**。

[FACT] 温度依赖主要来自母核激发态的热布居（除最低温度与最高密度外）。密度依赖最小，但电子发射在高密度低温下可能有显著的 Pauli 阻塞。

### 连续态俘获（坍缩阶段）

[FACT] 在超新星坍缩阶段（更高 T、$\rho$），电子俘获**由 Gamow-Teller 集体共振贡献主导**。

[FACT] 连续俘获的 T,$\rho$ 依赖**严重**——标准网格的插值困难，需高阶插值。对阈值不为零的电子俘获尤为严重。

[FACT] FFN 的创新：**定义简单的连续俘获相空间积分**（基于母基态 → 子基态跃迁 Q 值），然后除以 FFN 表中速率得到**有效 ft 值**——这些对 T、$\rho$ **依赖弱得多**。这种用**标准 Fermi 积分**的表述在 $\mu$ → 0 时具有连续值与连续导数。

## 7.6 中子壳阻塞与坍缩物理

[FACT] 当前核状态方程观点：铁核坍缩早期，**核变得极度富中子**，以至于**允许电子俘获（$\Delta$l=0）被阻塞**——当中子填满与质子同 l 的子壳时。

[FACT] Fuller (1982) 用简单壳模型研究了**中子壳阻塞现象与若干高温高密下的解锁机制**（包括**禁戒电子俘获**）。

[FACT] 解锁机制对状态方程细节敏感——典型情况导致**重核上电子俘获率大幅减小**，转而依赖**少量自由质子的电子俘获**，整体中子化率下降。

[FACT] Fuller (1982) 的单区坍缩计算表明：中子壳阻塞效应导致**中微子捕获时核内轻子分数更大**（每重子轻子数）。

[FACT] 由 Chandrasekhar 关系**核质量 ∝ 轻子分数$^{2}$**，较大最终核质量 → **更强的 bounce 后激波**。但 pre-collapse Si 燃烧中新电子俘获速率减小轻子分数 → 较小初始核质量 → 较少激波可耗散的物质 → 激波耗散减小（Weaver, Woosley, Fuller 1983）。

## 7.7 Bethe 1982 Caltech 访学

[FACT] Hans Bethe 于 1982 年初作为 Caltech Fairchild Scholar 访问 Kellogg Lab，与 Yahil、Brown、Cooperstein、Wilson 合作完成两篇开创性论文：
- Bethe, Yahil, Brown (1982)
- Bethe, Brown, Cooperstein, Wilson (1983)

这两篇为 Type-II 超新星爆炸与坍缩的核、原子、等离子体、流体力学综合问题奠定了基础。

## 7.8 逆反应与中微子阻塞

[FACT] FFN 近期找到了**e$^{-}$/e$^{+}$ 俘获的逆反应**（即 $\nu$/$\nu$̄ 俘获）的表达式，以及 $\nu$/$\nu$̄ 对直接反应的**阻塞效应**——这两者在超新星核心坍缩中 $\nu$/$\nu$̄ 最终被捕获（neutrino trapping）时**变得重要**，导致**双向俘获间达成平衡**。

[FACT] 已导出一般解析表达式并以计算机可用的近似方程形式化。所有新结果将发表於 Fuller, Fowler, Newman (1984)（当时在准备中），并制作包含 $\nu$/$\nu$̄ 俘获的新磁带供研究者请求使用。

## 7.9 作者的逻辑链

弱相互作用在核合成中的不可替代性 → FFN 数据库构建（实验 GT 元 + 理论）→ 温度密度依赖的处理策略（有效 ft 值）→ 中子壳阻塞与坍缩 → 逆反应与 $\nu$ 阻塞 → 新磁带供研究社区使用。

## 7.10 潜在问题与关注点

[CRITIQUE] **现代视角**：FFN (1980–1984) 的弱相互作用速率表至今仍被许多恒星演化与超新星模拟使用，但 1990 年代后有更多改进（Fuller 1998；Otsuki et al. 2014；Wan et al. 2017）。核心坍缩的中微子运输如今用完整 Boltzmann 方程，FFN 表仍是其基础输入。

[CRITIQUE] 文中提到 "neutrino trapping" 的概念，是 Type-II 超新星物理的标志性进展——1984 年 Bethe 等人的工作为 2017 年 GW170817 中子星并合的多信使天文学提供了理论背景。