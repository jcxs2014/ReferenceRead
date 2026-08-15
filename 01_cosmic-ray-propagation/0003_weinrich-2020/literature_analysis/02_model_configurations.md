> 本章属于：Galactic halo size in the light of recent AMS-02 data（Weinrich et al. 2020）
>
> 上一章：`01_introduction.md`
>
> 下一章：`03_halo_size_from_clocks.md`
>
> 总览：`00_overview.md`

# 2. Model and Configurations — 模型与传播配置

## 2.1 本节核心内容

§2 描述三种传播配置（BIG/SLIM/QUAINT）的参数化、几何假设、拟合方法（$\chi^2$ minos），以及使用的数据集。

## 2.2 几何与物理假设

**几何**：无限板模型，半高 $L$，银河盘无限薄（$h = 100$ pc $\ll L$）。CR 源和气体限制在盘内，碎裂/能量损失仅在盘中发生。

**物理项**：

| 项 | 公式 | 参数 |
|---|---|---|
| 空间扩散 | $K(E)$ | $K_0, \delta, R_l, \delta_l$ |
| 平流（银河风）| $V_c$ | 常数，垂直于盘 |
| 动量扩散（再加速）| $K_{pp}$ | $V_A$（Alfvén 速度）|
| 能量损失 | $\dot{E}$ | 同步辐射 + 逆康普顿 |

## 2.3 三种配置

| 配置 | 自由度 | 特点 |
|---|---|---|
| BIG | 7 参数（$K_0, \delta, R_l, \delta_l, V_c, V_A, L$）| 含对流 + 再加速 + 高低刚度断裂 |
| SLIM | 5 参数（$K_0, \delta, R_l, \delta_l, L$）| $V_c = V_A = 0$, $\delta_l = 1$（简化版）|
| QUAINT | 6 参数（$K_0, \delta, \delta_h, V_c, V_A, L$）| 含对流 + 再加速 + 高刚度断裂，无低刚度断裂 |

**扩散系数完整形式**：

$$K(E) = K_0 \, \beta \left(\frac{R}{4\text{ GV}}\right)^\delta \left[1 + \left(\frac{R_l}{R}\right)^{\delta_l}\right]^{-1} \left[1 + \left(\frac{R}{R_h}\right)^{\delta_h}\right]^{-1}$$

## 2.4 拟合方法

$\chi^2$ 最小化（IMinuit，James & Roos 1975），minos 算法给出非对称误差。包括：

- Solar modulation（force-field 近似，参数 $FF$）
- 交叉截面不确定性（通过 nuisance parameters 处理）
- 能量相关性（协方差矩阵）

**不确定性来源**（总不确定性）：
- 传输参数不确定性
- Solar modulation 不确定性
- 交叉截面不确定性

## 2.5 使用数据集

| 数据集 | 内容 | 备注 |
|---|---|---|
| AMS-02 Li/C, B/C, Be/B | Aguilar et al. 2018 | "Base" 数据 |
| ACE-CRIS $^{10}{\rm Be}$/$^{9}{\rm Be}$ | Lave et al. 2013 | 低能 $^{10}{\rm Be}$ 数据 |
| ISOMAX $^{10}{\rm Be}$/$^{9}{\rm Be}$ | | 低能 $^{10}{\rm Be}$ 数据 |
| ACE-CRIS $^{7}{\rm Be}$/$^{9}{\rm Be}$+$^{10}{\rm Be}$ | | Be 同位素数据 |
| Voyager 1&2 | | 太阳系外 CR |
| PAMELA $^{10}{\rm Be}$/$^{9}{\rm Be}$ | 初步分析 | |

## 2.6 关键参数表

| 参数 | 值/范围 | 备注 |
|---|---|---|
| $h$（盘半高）| 100 pc | 固定 |
| $\delta_l$（低刚度指数）| 1（SLIM）| 固定 |
| $R_h$（高刚度断裂刚度）| $\sim 10^4$ GV | 固定 |
| $FF$（Solar modulation）| 拟合 | 依赖数据时期 |