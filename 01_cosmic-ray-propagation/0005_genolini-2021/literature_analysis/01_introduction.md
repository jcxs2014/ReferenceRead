> 本章属于：New minimal, median, and maximal propagation models for dark matter searches with Galactic cosmic rays（Génolini et al. 2021）
>
> 下一章：`02_generalities.md`
>
> 总览：`00_overview.md`

# 1. Introduction — 引言

## 1.1 本节核心内容

Génolini et al. (2021) 更新了暗物质间接探测所需的**银河系宇宙线传播 min/med/max 基准模型**。新模型基于 AMS-02 最新二级/一级比率数据，覆盖扩散系数的低刚度和高刚度断裂，同时约束了传播晕大小 $L$。

## 1.2 核心问题

暗物质间接探测（通过高能反物质宇宙线搜寻暗物质湮灭/衰变信号）对银河系 CR 传播模型高度敏感。旧版 min/med/max（Cirelli et al. 2008）已过时——需要新数据更新。

## 1.3 主要改进

| 方面 | 旧版 (2008) | 新版 (2021) |
|---|---|---|
| 数据 | PAMELA 等 | AMS-02 最新数据 |
| 扩散系数 | 简单幂律 | 低+高刚度断裂 |
| 晕大小 $L$ | 未约束 | 放射性同位素约束 |
| 传播方案 | 单一 | BIG/SLIM/QUAINT 三种 |
| 不确定性量化 | 粗略 | 系统统计方法 |

## 1.4 关键数据

| 数据集 | 来源 |
|---|---|
| AMS-02 B/C | Aguilar et al. 2017 |
| AMS-02 Li/C, Be/C | Aguilar et al. 2017 |
| AMS-02 positrons | Aguilar et al. 2017 |
| AMS-02 antiprotons | Aguilar et al. 2018 |
| Voyager | Webber et al. |

## 1.5 关键公式

| 编号 | 公式 | 出处 | 物理意义 |
|---|---|---|---|
| 1 | CR 能量空间传输方程 | §1 | 扩散 + 平流 + 能量损失 + 注入 |
| 2 | DM 源项 $Q(E,x) = \langle\sigma v\rangle \rho^2/(2m^2) \cdot dN/dE$ | §1 | 暗物质湮灭源 |
| 4 | 晕大小标度 $\sim \rho(R_\odot)$ | §1 | $L \ll R$ 时通量正比于本地 DM 密度 |
| 5 | Green 函数 $G_p(E,x,x_s) \propto 1/K(E)$ | §1 | 反质子传播的 Green 函数 |
| 7 | 通量标度 $dp/dE \propto L^2/K(E)$ | §1 | 反质子通量的晕大小依赖 |
| 8 | DM 通量的 $L/R$ 级数展开 | §1 | $L/R$ 小量展开 |

## 1.6 作者的逻辑

```
DM 间接探测需要传播模型
→ 旧版 min/med/max 过时（数据更新、晕约束、断裂）
→ 本文提供新版 min/med/max
→ 三种传播方案（BIG/SLIM/QUAINT）
→ 系统统计方法定义 min/max
→ 提供拟合公式供 DM 搜寻使用
```

## 1.7 潜在问题与值得关注的地方

1. **min/med/max 的主观性**：虽然用统计方法定义，但参数空间的切割仍有主观成分
2. **SLIM vs BIG vs QUAINT**：三种方案对扩散系数的参数化不同——SLIM 是简化版，BIG 含更多自由度
3. **晕大小约束**：来自放射性同位素（¹⁰Be 等）的 $L \sim 3-10$ kpc 约束