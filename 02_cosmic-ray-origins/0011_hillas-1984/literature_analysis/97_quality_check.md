---
title: "97. Quality Check"
---

## Completeness Check

| 要求 | 状态 | 说明 |
|------|------|------|
| 所有章节覆盖 | ✅ | §1 Why Bother, §2 Observational Data (2.1/2.2), §3 Acceleration (3.1/3.2/3.3), §4 Propagation (4.1/4.2), §5 Conclusions |
| 所有图表覆盖 | ✅ | Figure 1 Hillas 图、Figure 2 轨迹尺度、Figure 3 能谱、Figure 4 各向异性、Figure 6 Fermi 允许区域 |
| 所有公式覆盖 | ✅ | $r_L$、Hillas 判据、$\gamma = 1 + t_A/t_E$、$t_A = 2c\lambda/\beta^2 c^2$、$t_s$、$t_p$、emf、$V_{\rm BZ}$ |
| 所有数值覆盖 | ✅ | Crab 参数、BZ emf 公式、$t_p$ 值、各向异性 $0.06\%$、密度梯度 $15\%$/kpc |
| 与 00_overview 无逐字重复 | ✅ | 00 仅保留元数据 + 一段总览 |

## 关键数值校验

- $r_L(E=10^{20}$ eV, $B=1 \;\mu$G$) = 1.08 \times 10^{15} / (1 \times 1) \;\rm pc$ = $1.08 \times 10^5$ kpc ✅
- Hillas 判据 $BL \gtrsim 2 E_{15}/(Z\beta)$（含 $eta$ 修正）✅
- $t_s = 1.4/(E_{20}^2 B^2)$ yr ✅
- $t_p(E=10^{20}$ eV$) \approx 7 \times 10^8$ yr ✅
- $t_p(E=10^{19}$ eV$) \approx 5 \times 10^9$ yr ✅
- Crab emf $\omega B r^2/c \sim 10^{18}$ V ✅
- BZ emf $V = 10^{19}(B/10^4)(M/10^8)^2$ V ✅
- $\gamma = 1 + t_A/t_E$（Fermi 谱指数）✅
- 各向异性 $A \approx \lambda_{\rm mfp}/r$，$\lambda_{\rm mfp} \sim 10$ Mpc（若 $A \sim 0.6$ 在 $6 \times 10^{19}$ eV）✅

## 分章独立内容确认

- §1：$r_L$ 公式推导、Figure 1/2 详细分析、10 个排除天体列表
- §2：四大实验对比、能谱三阶段定量、各向异性相位能量依赖表
- §3：五种直接加速模型（脉冲星、BZ、Lovelace、Colgate、Fischhoff）、Figure 6 三角形分析、$E_{\max}$ 限制定量
- §4：GZK 视界定量、扩散模型参数、$15\%$/kpc 密度梯度
- §5：三重问题框架、1984 vs 现代对比表
