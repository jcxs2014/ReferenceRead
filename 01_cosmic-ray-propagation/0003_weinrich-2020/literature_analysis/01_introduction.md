> 本章属于：Galactic halo size in the light of recent AMS-02 data（Weinrich et al. 2020）
>
> 下一章：`02_model_configurations.md`
>
> 总览：`00_overview.md`

# 1. Introduction — 引言

## 1.1 本节核心内容

Weinrich et al. (2020) 用 AMS-02 最新数据约束银河系 CR 传播晕大小 $L$，主要利用放射性同位素时钟（¹⁰Be 等）打破 $K_0/L$ 简并。

## 1.2 科学问题

银河系 CR 传播晕半高 $L$（即 CR 扩散区域的垂直尺寸）一直是**高度不确定**的参数。传统模型取 $L = 4$ kpc（GALPROP），但 AMS-02 高精度数据要求更精确的约束。

## 1.3 关键挑战——$K_0/L$ 简并

B/C 比率对 $K_0/L$ 的比值敏感，但对 $K_0$ 和 $L$ 单独不敏感——这被称为 $K_0/L$ 简并。打破简并的方法：使用**放射性同位素时钟**（如 ¹⁰Be，半衰期 $t_{1/2} = 1.387$ Myr），其衰变率与传播时间 $L^2/K_0$ 直接相关。

## 1.4 主要方法

1. 联合拟合 AMS-02 Li/C、B/C、Be/B 数据 + 多个 ¹⁰Be 相关数据集
2. 三种传播配置（BIG/SLIM/QUAINT）
3. 最小化 $\chi^2$，minos 算法给出非对称误差
4. Solar modulation 用 force-field 近似

## 1.5 核心结果

| 数据组合 | L（SLIM）| 备注 |
|---|---|---|
| Base（Li/C + B/C）| 不约束 | B/C 对 L 不敏感 |
| Base + Be/B（AMS-02）| $5.04^{+3.07}_{-1.79}$ kpc | AMS-02 Be/B 精度足够 |
| Base + Be/B + ¹⁰Be/Be + ¹⁰Be/⁹Be | $4.66^{+1.35}_{-0.97}$ kpc | **最严格约束** |

## 1.6 作者的逻辑

```
CR 晕大小 L 是传播模型的关键参数
→ B/C 只约束 K₀/L（简并）
→ 放射性同位素时钟打破简并
→ AMS-02 Be/B 精度足够约束 L
→ 联合 ¹⁰Be 数据进一步收紧
→ 传统 L = 4 kpc 被排除（对 δ = 0.3 模型）
```

## 1.7 与 Génolini 2021 的关系

Weinrich 2020 是 **Génolini 2021 的前置工作**——后者的 min/med/max 模型正是基于本文的 L 约束建立的。