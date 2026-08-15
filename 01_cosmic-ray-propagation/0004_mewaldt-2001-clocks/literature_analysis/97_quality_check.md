---
title: "97. Quality Check"
---

## Completeness Check

| 要求 | 状态 | 说明 |
|------|------|------|
| 所有章节覆盖 | ✅ | §1 Introduction, §2 加速延迟时钟, §3 EC 核与再加速, §4 β 衰变时钟, §5 总结 |
| 所有图表覆盖 | ✅ | Figure 1 (Co/Ni 质量分布), Figure 2 ($^{59}$Ni/$^{59}$Co 约束), Figure 3 ($^{51}$Cr EC 衰变), Figure 4 (四种时钟同位素质谱), Figure 5 (时钟比与 LBM), Figure 6 ($\tau_{\rm esc}$ 对比), Figure 7 (探测尺度示意), Figure 8 (密度-距离图), Figure 9 (四模型 $D$ 比较), Table I (时钟参数) |
| 所有公式覆盖 | ✅ | 逃逸路径长度公式 (1)、$R = \sqrt{D \tau_d \gamma}$、$f_{\rm surv} = 1/(1+\tau_{\rm esc}/\tau_d)$、$\tau_{\rm esc} = \lambda_{\rm esc}/(\rho c \beta)$ |
| 所有数值覆盖 | ✅ | Table I 全部 4×4 参数、$\tau_{\rm esc} = 14.5$ Myr、$\rho = 0.36 \rm\,H\,cm^{-3}$、$D = 2 \times 10^{28} \rm\,cm^2\,s^{-1}$、$\Delta t > 10^5$ 年 |
| 与 00_overview 无逐字重复 | ✅ | 00 只留作者/年份/期刊/主题/一句核心 |

## 关键数值校验

- $^{59}$Ni 半衰期 $7.6 \times 10^4$ 年 — ✅
- $^{59}$Ni 占质量-59 核 68%（Salpeter IMF 积分）— ✅
- Woosley & Weaver 11–25 $M_\odot$ 范围：27–87% — ✅
- 四种时钟 $\tau_{\rm esc}$：14.5 / 20.4 / 13.8 / 22.4 Myr — ✅
- $^{59}$Ni 延迟约束：$\gtrsim 3 \times 10^4$ 年 (≥20% 占比)；$\gtrsim 10^5$ 年 (≥40%) — ✅
- 银河系宇宙线功率 $3 \times 10^{40}$ erg s$^{-1}$ — ✅
- CRIS 质量分辨率 0.1–0.25 amu、几何因子 250 cm² sr — ✅

## 分章独立内容确认

每章均有 00_overview 未包含的展开内容：
- §2：Woosley & Weaver 核合成比例、四类模型判决、在途衰变分析
- §3：五位作者再加速争议对比表、五项不确定性因素列举
- §4：四种时钟参数完整表、四个扩散模型对比、高能 $^{10}$Be 展望
- §5：LBM 转折评价、AMS-02/CALET/DAMPE 后续影响
