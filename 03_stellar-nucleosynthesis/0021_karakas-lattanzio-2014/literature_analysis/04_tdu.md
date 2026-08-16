# 4. Third Dredge-Up（第三 dredge-up, TDU）

**上一章**: [03_agb_tp_hbb.md](03_agb_tp_hbb.md) · **下一章**: [05_nucleosynthesis_tp.md](05_nucleosynthesis_tp.md)

## 4.1 TDU 的物理本质

[FACT] TDU 发生于每次热脉冲后的 interpulse 期早期。当 H 燃烧壳向内移动至新合成的 ¹²C 区，该层变得不稳定（温度梯度超过绝热），触发一次额外对流 → 把 He intershell 物质（富含 ¹²C 和 s-过程元素）混到对流包络表面。

[FACT] **TDU 是 AGB 表面化学变化最主要的驱动**——决定 C 星形成、s-过程元素（Ba、Pb）表面增丰。

## 4.2  dredge-up 参数 λ

[FACT] 定义（公式 2）：
$$\lambda \equiv \frac{\Delta M_{\rm dredge}}{\Delta M_{\rm core}}$$
其中 $\Delta M_{\rm dredge}$ 为进入包络的质量，$\Delta M_{\rm core}$ 为 interpulse 期内 H 耗尽核质量增长量（图 19）。

[FACT] λ 依赖：
- 核质量 $M_c$；
- 金属度 Z；
- 对流处理细节（overshoot、半对流的实现方式）。

[FACT] λ 可能 > 1（无先验理由必须 ≤1）。λ = 1 时核质量脉冲间不增长。

[FACT] **Karakas et al. (2002) 首个 λ、$M_c^{\rm min}$ 参数化**（依赖总质量、包络质量、金属度）：
- λ 随恒星质量增加；
- λ 随金属度降低（Boothroyd & Sackmann 1988）。

[FACT] AGB 核合成最终依赖于四个参数：
1. λ（TDU 效率）；
2. $M_c^{\rm min}$（TDU 起始的最小核质量 → 决定 TDU 总次数）；
3. 对流包络质量（每次 TDU 的稀释度）；
4. He intershell 质量。

## 4.3 C 星形成

[FACT] C 星形成条件：表面 n(¹²C)/n(¹⁶O) ≥ 1。

[FACT] 低金属度下 C 星更容易形成的 **双机制**：
1. ¹²C 是三重 α 的初级产物 → 与 Z 无关；但 ¹⁶O 与 Z 正相关 → 低 Z 时需克服的 O 更少；
2. 低 Z 时 λ 更大 → 每脉冲混合的 C 更多。

[FACT] 中间质量星（M > 4.5M⊙）：He intershell 质量约小 10 倍，即使 λ ≈ 0.9 每次注入也小一个量级；大对流包络稀释更强 → 通常不形成 C 星（除非低 Z）。

## 4.4 C 星光度函数与 TDU 起点

[FACT] 观测碳星光度函数（CRLF）的形态（截断光度）是约束 TDU 参数 $M_c^{\rm min}$ 的关键观测检验。

[FACT] Karakas et al. 2007 网格（1–6M⊙, Z=10⁻⁴–0.02）显示 TDU 起点随质量与金属度变化；低金属度下更高质量开始 TDU。

## 4.5 关键观测约束

[FACT] 太阳前 富硅碳化物 SiC 微晶（来自 AGB C 星包络）的 ¹²C/¹³C 分布 **40 ≲ ¹²C/¹³C ≲ 100**（Zinner 1998），与 C(N) 星观测一致。

[FACT] 3M⊙, Z=0.02 模型 tip-of-AGB 时 ¹²C/¹³C ≈ 119、C/O ≈ 1.74、[F/Fe] 上升、²²Ne/Ne 由 0.068 升到 ≈0.4（图 22）。

## 关键数值

| M (M⊙) | Z | TDU 起算 M_c (M⊙) | 每脉冲 λ | tip 12C/13C | C/O |
|--------|-----|-------------------|---------|-------------|-----|
| 1.0 | 0.02 | ~0.55 | ~0.15 | ~25 | ~1 |
| 1.5 | 0.02 | ~0.55 | ~0.3 | ~60 | >1 |
| 3.0 | 0.02 | ~0.60 | ~0.4 | ~119 | ~1.74 |

## 4.6 TDU 与稀释公式（LaTeX）

[FACT] **TDU 效率参数 $\lambda$**（本文公式 2）：原文 p.22
$$ \lambda \;\equiv\; \frac{\Delta M_{\mathrm{dredge}}}{\Delta M_{\mathrm{core}}} $$

[FACT] **每脉冲表面数丰度变化**（$X_s$ 表面质量丰度；$X_{\rm intershell}$ intershell 丰度；$M_{\rm env}$ 包络质量；$M_{\rm dredge}$ 本次 TDU 带入质量）：原文 p.23
$$ \Delta X_s \;\approx\; \frac{M_{\rm dredge}}{M_{\rm env}}\;\big(X_{\rm intershell} - X_s\big) \;=\; \frac{\lambda\,\Delta M_c}{M_{\rm env}}\;\big(X_{\rm intershell} - X_s\big) $$

[FACT] **表面 C/O 演化累积公式**：原文 p.23
$$ \frac{n(^{12}\mathrm{C})}{n(^{16}\mathrm{O})}\bigg|_{\mathrm{surf},\,k+1} \;=\; \frac{n(^{12}\mathrm{C})}{n(^{16}\mathrm{O})}\bigg|_{\mathrm{surf},\,k}\;+\;\frac{\lambda\,\Delta M_c}{M_{\rm env}}\left(\frac{n(^{12}\mathrm{C})}{n(^{16}\mathrm{O})}\bigg|_{\rm intershell} - \frac{n(^{12}\mathrm{C})}{n(^{16}\mathrm{O})}\bigg|_{\rm surf,k}\right) $$

[FACT] **C 星条件（数比）**：原文 p.24
$$ \frac{n(^{12}\mathrm{C})}{n(^{16}\mathrm{O})}\bigg|_{\mathrm{surf}} \;\geq\; 1 $$

[FACT] **$M_c^{\rm min}$ 判据**：只有当 $M_c \geq M_c^{\rm min}(M,Z)$ 时 TDU 才启动；此后每脉冲 $M_c$ 递增：原文 p.23
$$ M_c^{(k)} \;=\; M_c^{\mathrm{min}} + k\,\Delta M_c, \qquad k = 1,2,\dots,N_{\mathrm{pulse}} $$

[FACT] **中间质量星 intershell 稀释**：He intershell 质量约为低质量星的 1/10：原文 p.25
$$ M_{\rm intershell}(M\gtrsim 4.5M_\odot) \;\approx\; 0.1\,M_{\rm intershell}(M\lesssim 3M_\odot) $$

[FACT] **Karakas et al. (2002) 参数化**：$\lambda$ 与 $M_c^{\mathrm{min}}$ 依赖 $M$ 和 Z：原文 p.23
$$ \lambda = \lambda(M, Z), \qquad M_c^{\rm min} = M_c^{\rm min}(M, Z) $$
