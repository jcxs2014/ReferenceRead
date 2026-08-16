# 2. Evolution and Nucleosynthesis prior to the AGB（AGB 前的演化与核合成）

**上一章**: [01_introduction.md](01_introduction.md) · **下一章**: [03_agb_tp_hbb.md](03_agb_tp_hbb.md) §3

## 2.1 示意例子（Illustrative Examples）

[FACT] 本文使用 2M⊙, Z=0.02 的详细 MESA 模型作为贯穿 §2–§3 的示意例子（图 2、图 5、表 1）。

[FACT] 主序之后：核心收缩，恒星穿过赫罗间隙；H 壳燃烧开始；外层因冷不透明度增大而变对流（Hayashi 极限），形成红巨星支。

[FACT] 1M⊙ 模型的对流包络随 RGB 上升而持续加深，最深时触及部分 H 燃烧产物区域 → **第一 dredge-up（FDU）**（图 3）。

## 2.2 First Dredge-Up（FDU, 一 dredge-up）

[FACT] FDU 是恒星演化中最早、最重要的混合事件：对流包络加深至 H 燃烧产物区，把 ¹³C、¹⁴N、¹⁷O、⁴He 带到表面，同时稀释 ¹²C、⁷Li、¹⁶O、¹⁸O。

[FACT] **FDU 后 ¹²C/¹³C 由太阳初始 ~89 降到 18–26**（表 1；Charbonnel 1994；Boothroyd & Sackmann 1999）。
- 2M⊙, Z=0.02: FDU 后 ¹²C/¹³C = 20.16（SDU 后 20.49）。
- 1M⊙, Z=0.02: FDU 后 12C/13C = 28.26。

[FACT] FDU 有三个关键光度点（图 3）：
1. 表面丰度开始变化的光度；
2. FDU 最深处的光度；
3. RGB 光度函数 "bump" 光度。

[FACT] **Bump** 是 RGB 光度函数中的光度尖峰，源于对流包络最深时吞噬 He 燃烧产物层（"He 燃烧残骸"）所致的额外混合。Renzini (1991) 指出此现象。

## 2.3 RGB 上的非对流混合过程

### 2.3.1 额外混合的观测标志
[FACT] RGB 上观测到低光度巨星仍有 H 燃烧产物增丰——"额外混合（extra-mixing）"机制的存在。

### 2.3.2 自转混合
[FACT] 自转导致的子午环流与剪切混合可延长巨星包络混合深度。

### 2.3.3 参数化模型
[FACT] 传统做法：用指数衰减混合长度 `d lnτ_v / d lnτ = -α` 与时间尺度 τ₁ 参数化额外混合（Barrè et al. 1980; Meynet et al. 1997）。

### 2.3.4 热盐水混合（Thermohaline mixing）
[FACT] **⁴He/³He 不稳定**（del Sordo 1991；Thielemann 1993；Kato 2000）— CNO 平衡产生 ³He，导致 ³He 富集层密度小于下方 → Ledoux 不稳定 → 分子扩散式混合。

[FACT] 本文 2M⊙ 模型（图 8）：热盐水混合成功再现观测到的 RGB ¹²C/¹³C 下降、表面 Li 破坏和低光度巨星的 N 增丰。

### 2.3.5 磁场与其他机制
[FACT] 磁流体混合与对流超射（overshoot）也被讨论，但本文主用热盐水模型。

## 2.4 锂（Lithium）

[FACT] 主序端 RGB 顶巨星表面 Li 显著低于初始值；⁷Li 破坏温度阈值 ~2.5×10⁶ K。

[FACT] 低光度巨星仍有 Li 消耗（"Li 消耗问题"），需要额外混合来解释。

## 2.5 Second Dredge-Up（SDU, 二 dredge-up）

[FACT] SDU 在 He 核心耗尽后、第二次上升巨分支（AGB 早期）时发生，主要影响 **M ≳ 4M⊙** 恒星。

[FACT] 与 FDU 相比，SDU 影响较轻：表 1 显示 SDU 后 Y(He) 显著增加（2M⊙: 0.304→0.304；5M⊙: 0.291→0.309；8M⊙: 0.296→0.362），¹²C/¹³C 变化较小，但 ¹⁴N、²³Na 略增。

[FACT] SDU 最深处的金属度依赖性对 M ≳ 3.5M⊙ 恒星较弱；低金属度中质量恒星甚至跳过 RGB 直接核心 He 点燃。

## 2.6 低金属度下的变化

### 2.6.2 Core Helium Flash
[FACT] 最大 He 闪质量 ~2.1M⊙（Z=0.02，无超射）；含超射模型降到 ~1.6M⊙（Bertelli et al. 1986a）。

### 2.6.3 Proton Ingestion Episodes（PIEs）
[FACT] 简并 He 闪期间，局部 H 层可能被卷入极高温 He 燃烧区 → 部分 H 质子被 CNO 燃烧（"PIEs"）。

[FACT] PIEs 在低金属度、低质量（M ≈ 1.0M⊙）模型中增强；可产生 ²⁶Al、¹³N，但一般不显著改变最终 WD 产额。

## 关键数值表（表 1 摘要，Z=0.02）

| Mass (M⊙) | Event | Y | ¹²C/¹³C | ¹⁴N/¹⁵N | ¹⁶O/¹⁸O | X(²³Na) |
|-----------|-------|------|---------|---------|---------|---------|
| 1.00 | FDU | 0.304 | 28.26 | 884 | 556 | 3.9e-5 |
| 2.00 | SDU | 0.292 | 20.16 | 2224 | 743 | 4.84e-5 |
| 5.00 | SDU | 0.309 | 18.74 | 3289 | 751 | 5.96e-5 |
| 8.00 | SDU | 0.362 | 18.21 | 4675 | 637 | 7.21e-5 |
