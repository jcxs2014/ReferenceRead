---
title: "2. The Orthodoxy — 标准范式的三大支柱"
paper: "Gabici et al. 2019, The origin of Galactic cosmic rays"
outline_ref: "§2 The Orthodoxy (§2.1–§2.5)"
original_sections: ["§2.1 Energy source; §2.2 Diffusive confinement; §2.3 DSA at SNR shocks; §2.4 VHE γ-rays; §2.5 Pion bump"]
---

> 上一章：[[02_cosmic-ray-origins/0012_gabici-2019/literature_analysis/01_introduction.md|01_introduction]]
> 下一章：[[02_cosmic-ray-origins/0012_gabici-2019/literature_analysis/03_observations_confront.md|03_observations_confront]]

## 2.1 [FACT] 支柱一：超新星爆炸提供 CR 能量

**局部 CR 能量密度**：$w_{\rm CR} \approx 1$ eV/cm$^3$，与 ISM 其他成分（磁场、软光子背景、热气体、湍流运动）能量密度相当。

**CR 能谱**：单幂律 $n_{\rm CR}(R) \propto R^{-\alpha}$，$\alpha \approx 2.7$，从多 GeV 延伸到数 PeV（PAMELA/AMS02 之前）。

**能量密度**主要被 GeV 质子和氦核携带——其 Larmor 半径 $r_L \sim 10^{12}$ cm，远小于任何银河系典型尺度（磁场相干长度、盘半径等），暗示 CR 在银河系内产生并被有效约束。

**γ 射线证据**（银河系起源的直接验证）：
- 银河系气体盘在 GeV 域发出弥散 γ 射线 → $\pi^{0}$ 衰变 → CR 与气体相互作用
- EGRET 对 SMC 的 γ 射线上限排除了"宇宙普遍 CR"假设（若 CR 全宇宙均匀，从 SMC 应能看到类似银河系的弥散 γ 射线）
- Fermi-LAT 对 LMC、SMC、M31 的观测确认 CR 强度因银河系而异

**银河系 CR 总能量**：$W_{\rm CR} \approx w_{\rm CR} \times V_d \approx 10^{55}$ erg

**所需注入功率**：$P_{\rm CR} \approx W_{\rm CR}/\tau_{\rm esc} \approx 10^{41}$ erg/s

**驻留时间** $\tau_{\rm esc}$ 的提取：通过 B/C 次级/初级比值，结合 spallation 截面，推出 grammage $\Lambda \approx 10$ g/cm$^{2}$ → $\tau_{\rm esc} \approx$ few Myr

**超新星能量匹配**：
- 银河系 SN 率 $\sim 3$/世纪
- 每次 SN 释放动能 $\sim 10^{51}$ erg
- 总注入率 $\sim 10^{42}$ erg/s
- **需 $\sim 10\%$ 效率**将 SN 动能转换为 CR 能量才能匹配 $P_{\rm CR} \approx 10^{41}$ erg/s

**替代方案**（银心爆发、恒星风）——近年被 γ 射线观测重新复兴。

## 2.2 [FACT] 支柱二：扩展磁化银河晕中的扩散约束

**驻留时间与路径长度矛盾**：$\tau_{\rm esc} \approx 10^7$ yr，路径 $c\tau_{\rm esc} \approx 1$ Mpc >> 盘半径+厚度。

**解决**：扩散运动（非直线传播）+ 扩展磁化晕（体积远大于盘）。

**$^{10}{\rm Be}$ 放射性同位素验证**：
- $^{10}{\rm Be}$ 半衰期 $\tau(^{10}{\rm Be}) \approx 1.4$ Myr
- 观测到的 $^{10}{\rm Be}$/Be 比值相对产生比值抑制 $\sim \tau(^{10}{\rm Be})/\tau_{\rm esc}$
- $\tau_{\rm esc} \approx 10$–$20$ Myr >> 盘内驻留时间 $\tau_{\rm esc,disk}$

**扩散系数估计**：
$$D_0 \approx 3 \times 10^{28} \left(\frac{H}{5 \; {\rm kpc}}\right)^2 \left(\frac{\Lambda}{10 \; {\rm g/cm^2}}\right)^{-1} \; {\rm cm^2/s}$$

**能量依赖**：$D(R) = D_0 (R/R_0)^\delta$，最佳拟合 $\delta = 0.3$–$0.6$，$D_0 \approx 10^{28}$–$10^{29}$ cm$^{2}$/s

**各向异性预言**：偶极各向异性 $\alpha \approx 10^{-4} (D_0/10^{28}) (L/3 \; {\rm kpc})^{-1}$

## 2.3 [FACT] 支柱三：SNR 激波上的 DSA 加速

**注入谱**：$q_{\rm CR}(E) \propto E^{-\alpha + \delta} \propto E^{-2.1}$–$-2.4$（需略陡于 $E^{-2}$）

**DSA 测试粒子极限**：强激波预言 $E^{-2}$，与观测略有张力。

**CR 反馈效应**（使谱变陡的机制）：
- 磁场放大 → Alfvén 速度增加 → Alfvén drift → 谱陡于 $E^{-2}$
- 中性粒子存在 → 谱变陡
- 完全自洽的"加速+逃逸"图像仍缺失

**化学组成**：
- 与太阳成分接近（LiBeB 和 sub-Fe 元素丰度比太阳高许多量级——spallation）
- Z > 2 相对于 H/He 略过量（未解释）
- **难挥发元素优于挥发元素**——与尘埃颗粒加速/碎裂有关

## 2.4 [FACT] SNR 的 VHE γ 射线：范式的经典测试

**预测**：若 SNR 将 $\sim 10\%$ 动能转为加速粒子（$E^{-2}$ 谱），则可几乎模型无关地预测 SNR 的 γ 射线光度（仅依赖 $n_{\rm ISM} \approx 0.1$–$1$ cm$^{-3}$）。

**观测**：
- 多个 SNR 在 GeV 和 TeV 域被探测到
- H.E.S.S. 银盘巡天（$35° < l < 65°$, $|b| < 3°$，至 1.5% Crab 灵敏度）：**8 个确定 SNR**——与 SNR 范式一致
- 但 >50% 源未确定或复合 SNR

**局限性**：
- 一致是**必要而非充分**条件
- $\pi^{0}$ 衰变 vs IC 散射的相对贡献不确定
- 经典例子：RX J1713.7-3946 可用轻子或强子模型解释

## 2.5 [FACT] "π 介子峰"（pion bump）的辨析

**§2.5 是论文的一个重要辨析段落**：

> "pion bump"（$\pi^{0}$ 衰变谱在 $E_\gamma = m_{\pi^0}/2 = 67.5$ MeV 处的峰）常被错误引用为 SNR 中强子 CR 的"证据"。

**论文的关键澄清**：
1. 实际峰在 67.5 MeV，低于 Fermi-LAT 当前分析极限 $\sim 100$ MeV
2. 在 $E^2$ 乘图下看到的 $\sim 1$ GeV 处的峰**不是**π 峰——而是来自质子谱在 GeV 区的断点
3. **正确做法**：对强子和轻子辐射做显式模型比较（模型依赖）
4. 例子：RCW 86 的 γ 射线+同步辐射数据**支持主要是轻子模型**
5. 真正的"smoking gun" π 峰需等 Fermi-LAT Pass 8 低能扩展或未来低 MeV 实验（COSI, eAstrogam）