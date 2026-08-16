---
title: '§5 Massive stars: the SNII production of the p-nuclides'
paper: 03_stellar-nucleosynthesis/0018_arnould-goriely-2003/literature_analysis/00_overview.md
chapter: 5
status: completed
read_date: '2026-08-16'
---

# §5 大质量恒星：II 型超新星中的 p 核素生成（★核心位点）

> §5 是本文**最重要的章节**——把 §3 的反应网络应用于 §4 的天体物理位点，得到可比较太阳系统观测的 p 核素产量。

## 5.1 主要 p 过程反应流（§5.1）

- **激波加热场景**：铁核坍缩产生的激波向外传播，在 O/Ne 壳层（位于 ~2000 km，质量坐标 1.5–3.0 M☉）将物质加热至 T≈2–3 GK，持续 ~秒量级。
- **反应流主线**：O/Ne 壳中的 ²⁰Ne、²²Ne、²⁴Mg、¹⁶O 等大 A 缺中子侧核素 → 光致分解生成中等 A 核 → 与 s 过程种子核耦合，最终通过 (γ,n) 链爬升到 p 稳定线。
- **电子俘获与 β⁺ 衰变**：在冷却阶段帮助反应流"回到"稳定谷。

## 5.2 质量依赖性与 IMF 平均产量（§5.2）

- **恒星质量扫描**：作者计算 10, 12, 15, 18, 20, 25 M☉ 的 SNII 模型。
- **IMF 平均产量**：将各质量点产量按 Salpeter IMF 加权积分 → **IMF-averaged p 核素产量**。
- **与太阳系统对比**：IMF 平均产量在多数 p 核素上能给出**合理一致性**（2× 以内），但对 138La、180Ta(m)、轻 Mo/Ru 系统低估（见 §6）。

## 5.3 12C(α,γ)16O 率与爆炸能量的影响（§5.3）

- **12C(α,γ)16O 率**：决定燃烧后 O/Ne 比，进而影响 p 过程的种子丰度。
- 作者展示：将该率提高/降低 10×，p 核素丰度变化 **2×–5×**，是**最敏感的天体物理参数**之一。
- **爆炸能量**：从 0.5× 到 2× 标准值（1.5×10⁵¹ erg），p 核素产量相应变化 **~3×**。

## 5.4 金属度的影响（§5.4）

- 以 SN1987A（Z ≈ 1/3 Z☉）为低金属度基准计算，显示低金属度下 p 核素产量**下降**（s 过程种子少）。
- 对银河系化学演化模型有重要意义：IMF 平均产量需按红移/金属度历史演化加权。

## 5.5 反应率变化的影响（§5.5）★

> **核心结论**：核物理不确定性 > 天体物理不确定性。

- 作者对 §3.5 中的 ~50 个关键反应率，分别取上下不确定性因子重跑网络。
- **单一反应扰动**：多数 p 核素产量变化 ≤3×。
- **多反应联合扰动**：p 核素整体产量不确定性 ~5×–10×，**远超**爆炸能量或金属度的影响。
- **特别敏感的反应**：12C(γ,α)、12C(γ,n)、⁹²Mo(γ,α)、⁹⁴Mo(γ,n)、¹³⁸Ba(γ,n) 等。

## 5.6 与其他作者预测的比较（§5.6）

- 与 Rauscher, Thielemann, Kraft (2002) 等同时代工作对比：整体趋势一致，但**138La、180Ta(m)**的差距可达 **2–3 个数量级**，显示对这些疑难核素的建模方法学尚未收敛。

---

## 分章索引
- 上：04_pre_sn_production.md
- 下：06_puzzling_cases.md


---

## 5.7 关键公式补充（FACT+LaTeX，原文页码已注）

> **FACT 补充**：§5 将反应网络应用于 SNII 位点，得到 p 核素产量表达式与敏感性分析（原文 p.39–51）。

### 5.7.1 激波加热温-时曲线（原文 p.39–40，§5.1）
- 峰值温度随质量坐标：$T_{9}^{\mathrm{peak}}(m)\approx 2\text{–}3\,K$（原文 p.39）
- 时间演化：$T_9(t)\approx T_{9}^{\mathrm{peak}}\,\exp\!\left(-\dfrac{t}{\tau_{\mathrm{cool}}}\right)$，$\tau_{\mathrm{cool}}\sim 1\text{–}2\,\mathrm{s}$（原文 p.40）
- 积分加热参数：$\theta=\int_0^{\infty}\rho\,T^{10}\,dt$（原文 p.40–41）

### 5.7.2 反应网络质量守恒（原文 p.41，§5.1）
- 质量守恒：$\sum_i A_i\,Y_i(t)=\sum_i A_i\,Y_i(0)$（原文 p.41）
- 种子质量分数：$X_{\mathrm{seed}}(m,t)=\dfrac{\sum_{A\ge 56}A\,Y_A(m,t)}{\rho(m,t)}$（原文 p.41）

### 5.7.3 IMF 平均产量（原文 p.44–46，§5.2）
- IMF 加权：$\langle Y_p(Z)\rangle_{\mathrm{IMF}}=\dfrac{\int_{M_{\mathrm{min}}}^{M_{\mathrm{max}}}Y_p(Z,M)\,\xi(M)\,dM}{\int_{M_{\mathrm{min}}}^{M_{\mathrm{max}}}\xi(M)\,dM}$（原文 p.44）
- Salpeter IMF：$\xi(M)\propto M^{-2.35}$（原文 p.44）

### 5.7.4 反应率敏感性（原文 p.48–51，§5.5）
- 相对扰动：$\dfrac{\Delta Y_p}{Y_p}\approx\sum_r S_r\,\dfrac{\Delta\lambda_r}{\lambda_r}$，$S_r=\partial\ln Y_p/\partial\ln\lambda_r$（原文 p.48–49）
- 多反应联合扰动：$\Delta_{\mathrm{tot}}=\sqrt{\sum_r S_r^{2}\,\Delta_r^{2}}$（原文 p.51）
- 特别敏感反应：${}^{12}\mathrm{C}(\gamma,\alpha)$、${}^{12}\mathrm{C}(\gamma,n)$、${}^{92}\mathrm{Mo}(\gamma,\alpha)$、${}^{94}\mathrm{Mo}(\gamma,n)$、${}^{138}\mathrm{Ba}(\gamma,n)$（原文 p.51）


### 5.7.5 关键 FACT 汇总（原文 p.39–51）
- **[FACT]** 冷却时标 $\tau_{\mathrm{cool}}\sim 1\text{–}2\,\mathrm{s}$ 是 SNII O/Ne 层 p 过程"时窗"的直接定量量（原文 p.40）。
- **[FACT]** Salpeter IMF 指数 $-2.35$ 是 IMF 平均产量的核心假设（原文 p.44）。
- **[FACT]** 敏感性系数 $S_r=\partial\ln Y_p/\partial\ln\lambda_r$ 使作者能对 50 个反应率进行系统扰动分析（原文 p.48–49）。
