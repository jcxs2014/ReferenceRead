> 本章属于：Asplund et al. (2009) AGSS09
>
> 上一章：`01_introduction.md`
>
> 下一章：`03_light_elements.md`

# 2. Ingredients for Solar Abundance Analysis（§2 分析原料）

## 2.1 本节核心内容

§2 建立太阳丰度分析所需的四块基石：
1. 观测：太阳谱线（强度谱 / 流量谱）
2. 原子与分子数据：跃迁概率、加宽、超精细结构、电离、配分函数
3. 大气模型与线形成：1D vs 3D、LTE vs. non-LTE
4. 观测检验：3D 模型如何被中边缘（center-to-limb）变化、Hα/Hβ、金属线线型验证

## 2.2 §2.1 Observations（观测）

- [FACT] 分析基于**太阳光谱中的吸收线指纹**（吸光带、吸收轮廓）。
- [FACT] 关键太阳图集：
  - **光学宁静太阳盘心强度谱**：
    - Jungfraujoch / Liège 图集（Delbouille, Roland & Neven 1973）
    - **Kitt Peak 太阳图集**（Neckel & Labs 1984）——分辨率略高
  - Liège 图集因为台站海拔高，受大气吸收（telluric）影响小；Kitt Peak 分辨率更高。
  - **红外**：Kitt Peak（Delbouille et al. 1981）与 shuttle 上的 ATMOS 实验（Abrams et al. 1996；Farmer & Norton 1989）
  - **流量谱**：Kurucz (2006) 重新还原的 Kitt Peak 流量数据（Kurucz et al. 1984 为早期版本）
- [FACT] "All solar atlases agree very well with each other except for spectral regions afflicted by telluric features."
- [INTERPRETATION] 因此**观测质量不是太阳丰度误差的主要来源**，重点在于模型和原子数据。

## 2.3 §2.2 Atomic and Molecular Data（原子与分子数据）

### 2.3.1 需要的数据（逐一列出）

- [FACT] 除跃迁概率 `gf` 外，还需：
  1. **线加宽**（连续加宽 / van der Waals broadening）
  2. **超精细与同位素分裂**
  3. **解离能**（分子）
  4. **配分函数**
  5. **光致电离截面**（non-LTE 关键）
  6. **碰撞激发 / 电离截面**（最难）

### 2.3.2 关键进展

- [FACT] **self-broadening（van der Waals）**：Anstee & O'Mara 1995, Barklem & Asplund-Johansson 2005, Barklem et al. 2000a 使其可以精确计算，"使经典 Unsöld 加宽及其任意增强因子基本过时"（对中性物种）。
- [FACT] **Opacity and Iron Projects**（Badnell et al. 2005）显著改进光致电离数据。
- [FACT] **碰撞截面完全缺失**（除 Fe I、少量晚期型星相关的体系）：只能依赖 van Regemorter (1962)、Drawin (1968) 经典公式——作者警告"充其量是量级估计"。
- [CRITIQUE] 当通过调节 Drawin 缩放因子（`S_H`）拟合谱线时，"揭示的是模型缺陷而非真实碰撞截面"（Asplund 2005）。

## 2.4 §2.3 Solar Atmospheric and Line Formation Modelling

### 2.4.1 1D 模型两类

- **理论 1D**（Kurucz 1993；MARCS – Gustafsson et al. 2008）：
  - 恒总能流（辐射 + 对流）通过大气层
  - 对流用**混合长理论**（Böhm-Vitense 1958）
  - 辐射通常假设 LTE
  - 必须处理完整 line blanketing

- **半经验 1D**（Holweger & Müller 1974；VAL3C Vernazza et al. 1976；MISS Allende Prieto et al. 2001）：
  - 温度从连续谱中-边缘变化和不同形成高度的线中反演
  - 仍假设静水力学平衡，但不要求恒总能流，也不必估算对流输运

- [FACT] 太阳学界偏爱 **Holweger & Müller (1974)**（"部分出于习惯"），但其 1974 版本源自 1967 年 Holweger 模型的压力积分重算；温度结构在谱线形成区**高估约 50 K**（因当时太阳谱分辨率有限）。
- [FACT] 半经验模型（HM, MISS）的**温度梯度比 1D 理论模型更浅**（见 Fig 1）。

### 2.4.2 3D 时间依赖流体动力学模型

- [FACT] 求解**质量、动量、能量守恒方程 + 3D 辐射转移方程**，在代表太阳表面小体积内。
- [FACT] 辐射加热/冷却率驱动对流运动；为节省计算，opacity 用 **4–20 个典型 opacity bins** 表示（Nordlund 1982），与单色方案对比"令人惊讶地准确"。
- [FACT] 已有多个 3D 模型：Asplund et al. 2000b、Caffau et al. 2008a（co5bold）、Trampedach et al. 2009。
- [FACT] **不需要任何混合长参数**——对流能流是流体动力学的自然产物。
- [FACT] **本文主要使用 Trampedach et al. (2009) 3D 模型**（改进了辐射转移处理，opacity 更新，温度梯度更浅）。

### 2.4.3 线形成方法

- [FACT] 两条途径：
  1. 从观测测**等值宽度**（equivalent width）；
  2. 直接对**线轮廓**做理论拟合（line profile fitting）。
- [FACT] LTE：能级占据由 Boltzmann + Saha 分布给出。
- [FACT] Non-LTE（统计平衡）：同时求解所有相关能级/物种的速率方程和所有相关波长的辐射转移。

## 2.5 §2.4 Observational Constraints on Solar Modelling（观测检验）

- [FACT] **3D 模型**在以下诊断上全面优于 1D：
  1. **米粒组织拓扑**、特征尺度、对流速度、亮度对比；
  2. **连续谱中-边缘变化**（Fig 2）：Trampedach et al. (2009) 3D 模型甚至优于**半经验**的 Holweger & Müller 模型（后者就是为拟合该诊断而设计的）；
  3. **Hα、Hβ 线翼**（Fig 2 + §2.4）：Pereira et al. (2009) 发现 3D 模型在 LTE 下就能很好重现，且**不需要任何自由参数**；
  4. **金属线线型、不对称性和位移**（Fig 3）：无需 micro- 和 macroturbulence 自由参数，3D 模型的**对流多普勒效应**自然解释了加宽、位移和不对称。

- [CRITIQUE] Caffau 的 co5bold 模型整体线型好，但**线不对称性**尚未系统检验。

- [FACT] 本节结论句（关键）："**the 3D solar model employed here appears to be a very realistic representation of the solar photosphere**"

## 2.6 误差量化（跨§3 前置）

在§3.0（p.9）作者详细说明：

- [FACT] 三类系统误差：
  1. **Mean atmospheric stratification**：½ · |3D spatial average − Holweger & Müller|
  2. **Atmospheric inhomogeneities**：½ · |full 3D − 3D average|
  3. **Non-LTE**：½ · |non-LTE correction|；下限 0.03 dex
- [FACT] **总误差 = sqrt(σ_stat² + σ_syst²)**，其中 σ_stat = 加权标准误（权重来自谱线连续谱放置和已知混杂）
- [FACT] 作者**未尝试**量化 gf 值的系统误差——这部分依赖谱线离散度来间接吸收。

## 2.7 关键判断

- [FACT] 3D 模型 + 完整辐射转移 + 无自由加宽参数 = 目前**最真实的太阳光球模型**
- [FACT] 但 **atomic data（尤其碰撞截面、中性金属 gf）** 仍是最大短板
- [INTERPRETATION] 因此 AGSS09 的丰度不确定性主要来自**原子数据 + non-LTE 近似**，而非模型大气本身
