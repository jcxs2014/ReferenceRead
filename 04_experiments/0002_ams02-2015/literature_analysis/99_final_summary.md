# 99. Final Summary — AMS-02 质子谱精确测量

## 15.1 一句话总结

AMS-02 在 ISS 上基于 300 M 质子事例精确测量 1 GV–1.8 TV 宇宙线质子流强，首次以模型无关方式发现谱指数在 >100 GV 以上逐步变硬，99.9% C.L. 排除单幂律假设。

## 15.2 科学问题

质子谱的刚性依赖 $\Phi(R)$ 与谱指数 $\gamma(R)$ 如何？这关系到宇宙线的**起源**（源谱 $\gamma_{\text{inj}}$）、**加速**（SNR DSA 截断形态）、**传播**（扩散系数 $K \propto R^\delta$ 的谱）。

## 15.3 核心方法

- **探测器**：ISS 平台 AMS-02 磁谱仪（1.4 kG 永磁 + 9 层硅径迹 + 4 层 TOF + ACC + RICH + TRD + ECAL）
- **选例**：$Z=+1$ + 向下 + 穿透 L1+L9 + $\chi^2$/d.o.f. < 10 + 刚性 > 1.2 × 几何磁截止 + 质量 > 0.5 GeV/$c^2$
- **流强重建**：$\Phi_i = N_i / (A_i \varepsilon_i T_i \Delta R_i)$（Eq.1），含 MC 计算的接受度与数据测得的触发效率
- **拟合**：双幂律 Eq.(3) 拟合 45 GV–1.8 TV，得 $\chi^2$/d.o.f. = 25/26
- **谱指数**：$\gamma = d\ln\Phi / d\ln R$（Eq.4），变量宽度 bin

## 15.4 最重要结果

1. **质子流强 $\Phi(R)$**：72 bin 覆盖 1 GV – 1.8 TV，系统误差 <5%（中刚性端）
2. **双幂律拟合参数**：$\gamma = -2.849$，$\Delta\gamma = 0.133$，$R_0 = 336$ GV，$s = 0.024$
3. **谱指数变硬**：$\gamma(R)$ 在 $R \gtrsim 100$ GV 以上从 $-2.85$ 变硬至 $\sim -2.70$
4. **单幂律排除**：99.9% C.L.（$R > 45$ GV）
5. **前代实验一致性**：与 ATIC-2/BESS-Polar II/CREAM/PAMELA 在重叠能量段一致

## 15.5 核心创新

- **统计规模**：300 M 质子事例，宇宙线质子谱史上最大
- **$\gamma(R)$ 首次测量**：模型无关的逐刚性谱指数
- **系统误差深度研究**：Fig.2 四 panel 独立校验 + 两种独立 unfolding + 多研究小组盲复现
- **精度量级**：中刚性端系统误差 <3%，历史最优

## 15.6 主要局限

- **观测时间**：30 个月（2011–2013），后续 AMS-02 数据已扩展至 500 M+
- **双幂律唯象**：Eq.(3) 是数据驱动的唯象拟合，非理论推导（脚注 [29]）
- **太阳调制**：force-field 近似 + 外部太阳势 $\phi = 0.50$–0.62 GV，非自洽
- **拟合范围**：$R < 45$ GV 排除在外（太阳调制主导）
- **未直接拟合传播模型**：所有传播/起源约束为定性讨论

## 15.7 我应该记住什么

1. AMS-02 是 ISS 磁谱仪，刚性分辨 10 μm / 3 m 力臂 / 1.4 kG 场
2. 300 M 质子事例（$3.0\times10^{8}$），72 bin，1 GV–1.8 TV
3. 双幂律 $\chi^2$/d.o.f. = 25/26，单幂律 99.9% C.L. 排除
4. 谱指数在 >100 GV 变硬：$-2.85 \to -2.70$
5. 拟合参数：$R_0 = 336$ GV，$\Delta\gamma = 0.133$，$\gamma = -2.849$
6. 系统误差 4 分项 quadrature 合并（触发/接受度+截止+背景/unfolding/标度）
7. Fig.2 四 panel 是独立校验的标志性做法
8. 与 ATIC-2/CREAM/PAMELA/BESS-Polar II 一致，但精度量级超越
9. 隐含传播指数 $\delta \approx 0.7$，与 $^{10}$Be 时钟 $\delta \approx 0.3$ 张力
10. 后续精读文献：genolini-2021（传播参数拟合）、weinrich-2020（时钟方法）
11. 库内同主题实验：hess-2016（PeV 质子）、lhaaso-2021（膝区）、icecube-2013（中微子）

## 15.8 与相关工作的关系

| 库内文献 | 关系 |
|---|---|
| weinrich-2020 | 时钟方法测传播；AMS 数据为其输入 |
| genolini-2021 | 用最新数据（含 AMS 质子）拟合传播参数 |
| mewaldt-2001-clocks | $^{10}$Be 时钟给出 $\delta \approx 0.3$；与 AMS 隐含 $\delta \approx 0.7$ 张力 |
| hess-2016 | VHE γ 射线观测，推断 PeV 质子加速——与 AMS 构成直接-间接互补 |
| drury-1983 | SNR DSA 理论框架，预测源谱 $\gamma_{\text{inj}} \approx -2.1$；与 AMS 数据联合约束 $\delta$ |

---

## 25. Completeness Check

- [x] Abstract（PACS、DOI 核对）
- [x] Introduction（宇宙线起源/加速/传播的动机）
- [x] All main sections（8 段路径 B 覆盖）
- [x] Detector / Method（AMS-02 硬件、选例、触发）
- [x] Data（300 M 事件、72 bin、$7.96\times10^{7}$ s）
- [x] Background（氘核/$\pi$/$e^\pm$ 污染）
- [x] Signal（质子选例链）
- [x] Statistics（$\chi^2$/d.o.f. = 25/26、单幂律排除 99.9%）
- [x] Systematics（4 分项、Fig.2 四 panel 校验）
- [x] Results（双幂律参数、$\gamma(R)$）
- [x] Discussion（与库内文献关系）
- [x] Conclusion（原文结论段逐句引用）
- [x] Appendix（Supplemental Material 已引用）
- [x] Figures（Fig.1–4 全部分析）
- [x] Tables（本文无表格；Supplemental Material 已注明）
- [x] Important equations（Eq.1 流强、Eq.2 单幂律、Eq.3 双幂律、Eq.4 谱指数、误差合并）
- [x] Important numerical values（$R_0 = 336$ GV、$\Delta\gamma = 0.133$、$\gamma = -2.849$、$C = 0.4544$、$3.0\times10^{8}$ 事件、1 GV–1.8 TV、1.4 kG）
- [x] Important references（Ref.[1] Blasi 综述、[7] 模型综述、[27] Lafferty-Wyatt $\tilde{R}$、[29] 双幂律、[30] 太阳势）
