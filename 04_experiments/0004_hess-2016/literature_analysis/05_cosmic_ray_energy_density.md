---
title: "§5 Cosmic-Ray Energy Density"
paper: "hess-2016"
section: 5
nav_prev: "04_pevatron_evidence.md"
nav_next: "06_sagittarius_a_star_as_pevatron.md"
---
上一章：`04_pevatron_evidence.md` — §4
下一章：`06_sagittarius_a_star_as_pevatron.md` — Cosmic-Ray Energy Density

# §5 Cosmic-Ray Energy Density — 宇宙线能量密度

## [FACT] 5.1 w_CR(r) 径向分布

HESS 测量了 CMZ 内宇宙线能量密度 w_CR 随银心距 r 的分布（Fig. 2，原文 p.38）：

$$w_{CR}(r) \propto \frac{1}{r} \quad (10 \lesssim r \lesssim 200 \text{ pc})$$

这一轮廓有重要的物理含义：

1. **排除单次暴冲**：暴冲预期 ~1/r$^{2}$（随膨胀快速稀释）
2. **排除常数轮廓**：常数需要持续的点源注入
3. **支持连续注入**：中心源（如 Sgr A*）连续注入粒子

[FACT] w_CR(r) ~ 1/r 轮廓支持中心 PeVatron 连续注入宇宙线（原文 p.38，Fig. 2）。

## [FACT] 5.2 扩散模型拟合

扩散方程（原文 p.38，Methods）：

$$w_{CR}(r) = Q(E) \cdot \frac{\pi r^2}{4 D(E) t} \cdot \text{erfc}(r/r_{\text{diff}})$$

其中 $r_{\text{diff}} = \sqrt{4 D(E) t}$ 是扩散半径。

最佳拟合参数：
- 扩散系数：D(E) ~ E^0.5（与 CRM 下半对流尺度一致）
- 注入时间：Δt ≥ 10$^{4}$ yr

[FACT] 扩散模型拟合给出扩散系数 D(E) ~ E^0.5（原文 p.38，Methods），与银河系传播模型一致。

## [FACT] 5.3 与银河系盘的比较

CMZ w_CR 约是银河系盘均值的 **10 倍**（原文 p.38）：
- 银河系盘：$w_{\text{CR}} \approx 1 \text{ eV cm}^{-3}$
- CMZ：$w_{\text{CR}} \approx 10 \text{ eV cm}^{-3}$（原文 p.38）

[FACT] CMZ 宇宙线能量密度比银河系盘高约 10 倍（原文 p.38），说明该区域存在强 PeVatron 注入。