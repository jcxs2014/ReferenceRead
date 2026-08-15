---
title: "3. Acceleration Mechanisms — 统计加速与直接加速"
paper: "Hillas 1984, The Origin of Ultra-High-Energy Cosmic Rays"
outline_ref: "§3 ACCELERATION MECHANISMS"
original_sections: ["§3.1 Statistical (Fermi/Shock) (L414–572)", "§3.2 Direct (Pulsar/AGN) (L575–683)", "§3.3 Final Comments (L686–692)"]
---

> 上一章：`02_observational_data.md`
> 下一章：`04_propagation.md`

## 3.1 两类加速机制的对比

Hillas 将加速机制分为两类：

| | 统计加速（Fermi/激波） | 直接加速（电磁感生） |
|---|---|---|
| 代表 | Fermi 二阶加速、激波 DSA | 旋转中子星/黑洞的 unipolar inductor |
| 优点 | 谱指数自然得出 $\sim E^{-2}$ | 快速，单步到高能 |
| 缺点 | 慢，高能时能量损失超过增益 | 环境能量密度极高，易被辐射损失击败 |
| 谱型 | 幂律（自然） | 幂律需要特殊机制 |

## 3.2 [FACT] Fermi 统计加速与能量损失

**Fermi 加速基本公式**（Cavallo 22; Greisen 47）：

统计加速特征时间 $t_A$（$dE/dt = E/t_A$）与逃逸时间 $t_E$ 竞争，粒子出射谱：

$$J(E) \propto E^{-\gamma}, \quad \gamma = 1 + \frac{t_A}{t_E}$$

需 $t_A \lesssim t_E$ 才能得到硬谱（$\gamma$ 小）。

**Fermi 二阶加速时间**（散射中心随机运动速度 $\beta c$，平均自由程 $\lambda = \eta r_L$）：

$$t_A = \frac{2c}{\beta^2} \frac{\lambda}{c} \approx \frac{2\eta r_L}{\beta^2}$$

对 Alfvén 波散射：$\lambda \sim (4\text{–}25) r_L$，取 $\eta \sim 10$。

**同步辐射损失时间**（质子，$B$ 单位 Gauss）：

$$t_s = \frac{1.4}{E_{20}^2 B^2} \; \rm yr$$

其中 $E_{20}$ 以 $10^{20}$ eV 为单位。重核（质量数 $A$、电荷 $Z$）的损失时间放大 $(A/Z)^4$。

**光核反应损失时间**（质子 + $2.7$ K CMB）：

$$t_p \approx 7 \times 10^8 \; \rm yr \text{ at } E = 10^{20} \text{ eV}, \quad t_p \approx 5 \times 10^9 \; \rm yr \text{ at } E = 10^{19} \text{ eV}$$

$t_p$ 随 $E$ 上升而快速下降（因光核反应阈以上截面增大），且在明亮天体附近因局部辐射场增强而大幅减小。

## 3.3 [FACT] Figure 6：Fermi 加速的允许区域

Figure 6 在 $\log B$ vs $\log \beta$ 平面上标出**能加速到 $10^{20}$ 或 $10^{19}$ eV 的组合**（分质子和铁核两图）：

- **上部阴影（同步辐射）**：$B$ 太大 → $t_s < t_A$ → 被同步辐射击败
- **下部阴影（光核反应）**：$\beta$ 太小 → $t_A$ 太长 → 被光核反应击败
- **对角线下方**：$BL < E/(Ze\beta)$ → 不满足 Hillas 判据 → 扩散逃逸太快
- **允许的三角形区域**：$B \sim 10^{-6}$–$10^{-4}$ G，$\beta \sim 10^{-3}$–$10^{-1}$

**候选天体位置**：

| 天体 | $B$ (G) | $\beta$ | 结论 |
|------|---------|---------|------|
| 星系团（Virgo/Coma） | $\sim 2 \times 10^{-6}$ | $\sim 3 \times 10^{-3}$ ($v_A \sim 1000$ km/s) | 边缘，需 $R \sim 0.5$ Mpc |
| 大射电星系瓣 | 同上 | 同上 | 同上 |
| 射电星系热点（Cyg A） | $\sim 10^{-4}$ | $\sim 10^{-2}$–$10^{-1}$ | 勉强可行 |
| 大尺度结构（IGM） | $\sim 3 \times 10^{-8}$ | $\sim 10^{-3}$ | 不可行：$t_A \gg t_{\rm Hubble}$ |
| AGN 吸积盘 | $\sim 1$–$10^4$ G | $\sim 1$ | 不可行：同步辐射 $t_s$ 太短 |

**对 $E = 10^{20}$ eV 质子**：任何散射体速度 $\beta < c$ 时，磁场 $B < 1$ G；$E = 10^{19}$ eV 时 $B < 50$ G。

## 3.4 [FACT] 激波 DSA 的详细分析

Hillas 对激波 DSA 的评价：

- 平行激波（$B \parallel$ 气体流动）是最受关注的构型
- 每次穿越激波平均增益 $\Delta E / E = 4\beta_2 / 3$（$eta_2$ 为下游速度）
- 粒子在激波前平均穿越次数 $\sim 1/[4(\beta_1 - \beta_2)]$
- 强激波统计给出 $E^{-2}$ 谱（与观测膝以下谱一致）

**关键限制**（Lagage & Cesarsky 67）：

- SNR 激波的有限尺寸和有限寿命（$\sim 10^4$–$10^5$ yr）限制最大能量
- 已知散射机制给出的 $E_{\max} \sim$ few $	imes 10^{13}$ eV（质子）——**比膝低两个量级**
- 集合效应（ensemble of shocks）不能显著改善
- 有效加速率 $t_A^{-1} \sim c\beta_2^2/(\lambda_1 + 4\lambda_2)$，与 Fermi 加速形式相同，仅 $\beta$ 需放大

**结论**：激波 DSA 在 SNR 尺度上无法突破 $10^{15}$ eV，更不用说 $10^{19}$ eV。

## 3.5 [FACT] 直接加速：脉冲星与 AGN

### 脉冲星

**旋转中子星参数**（以 Crab 为例）：

- 表面磁场 $B_s \sim 10^{12}$ G
- 半径 $r \sim 10$ km
- 旋转频率 $\omega/2\pi \sim 30$ s$^{-1}$

极-赤道 emf（cgs）：

$$\mathcal{E} \approx \frac{\omega B r^2}{c} \sim 10^{18} \; \rm V$$

但 magnetosphere 中充满电浆后，$E \cdot B = 0$ 约束使有效 emf 缩减因子 $r \omega / c$（即 light cylinder 因子）。

**Berezinsky (10) 模型**：主要电位降发生在远离脉冲星处（可能 near light cylinder）：

$$V = \frac{B \omega^2 r^3}{4 c^2}$$

Crab 脉冲星可加速**铁核到 $10^{18}$ eV，质子仅到 $5 \times 10^{16}$ eV**——重核因 $Z$ 大而占优，但辐射损失 $-dE/dx = 2\gamma^4 Z^2 e^2/(3 R_c)$ 也随之增大。

### AGN / 黑洞

**Lovelace (75) 模型**：$10^8 M_\odot$ 黑洞吸积盘，$B \sim 10^4$ G，可产生 $\sim 10^{19}$ V emf，沿轴射出质子束（需 $B \cdot \Omega < 0$）。

**Blandford-Znajek (14) / Rees et al. (81)**：自旋黑洞的电动力学能量提取，最大可提取旋转能 $0.29 Mc^2$。电场 emf：

$$V = 10^{19} \left(\frac{B}{10^4 \;\rm G}\right) \left(\frac{M}{10^8 M_\odot}\right)^2 \; \rm V$$

**关键问题**（Hillas 明确指出）：虽然提取功率高效，但**热伽马光子产生的正负电子等离子体会屏蔽电场**，且与高能质子相互作用。Colgate (26) 估计在 Cen A 等明亮核区，能量损失时标 $< 1$ yr——加速必须发生在远离核区的地方才能避免损失。

## 3.6 [FACT] 流体激波（Colgate-Johnson）

Colgate & Johnson (27) 提出超新星内爆激波在恒星大气密度梯度中加速到相对论速度，直接加速粒子。Hillas 评价：

- $E_{\max}$ 似乎太小
- Colgate 需要解释激波如何从 $E \sim 3 \times 10^{14}$ eV/核子处继续传播
- 证据表明超新星中的相对论粒子主要是在**爆发之后**获得能量的

## 3.7 [FACT] §3.3 最终评论

Hillas 总结：上述任何方案都**没有真正利用一阶 Fermi 加速**（一阶 Fermi 比二阶快得多，因为能量增益 $\propto \beta$ 而非 $\beta^2$）。激波 DSA 在前沿本身涉及一阶加速，但大部分散射只是产生扩散。理想情况下希望找到"高反射系数的前进镜"。

## 3.8 [INTERPRETATION] 我的理解

Hillas 1984 最重要的洞察：

1. **统计加速（Fermi/DSA）无法突破 $10^{18}$ eV**：同步辐射和光核反应双重限制把允许的 $B$-$eta$ 参数空间压缩到极小三角形
2. **直接加速（脉冲星/AGN）在能量上可行，但被辐射场环境击败**：emf 足够大，但加速区附近的辐射场使得 $t_{\rm loss} < t_{\rm acc}$
3. **Hillas 隐含的期待**：一阶 Fermi 加速 + 足够大的空间 + 足够快的散射体 → 目前尚无私想方案

## 3.9 [CRITIQUE] 潜在问题

1. Hillas 引用的 Lagage & Cesarsky $E_{\max}$ 值基于 1983 年散射机制的估计，后续（Katz 1994; Bell 1994）表明 SNR 内自激发不稳定性可使 $\lambda \to r_L$，$E_{\max}$ 可达 PeV
2. Blandford-Znajek 机制在 1984 年处于理论早期，现代 GRMHD 模拟表明该机制在 AGN 喷流中可能比 Hillas 设想的更稳健
3. 未考虑相对论激波（GRB 内）的一阶 Fermi 加速——1997 年 GRB 被提出后才得到系统研究
