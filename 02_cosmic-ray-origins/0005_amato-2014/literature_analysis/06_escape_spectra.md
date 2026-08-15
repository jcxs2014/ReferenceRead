# 6. CR 逃逸与谱（Escape & Spectra）

> 本章属于：The origin of galactic cosmic rays (Blasi 2013 §6.1–6.2 & Amato 2014 §3.2, §5)
>
> 上一章：[[02_cosmic-ray-origins/0005_amato-2014/literature_analysis/05_magnetic_field_amplification.md|05_magnetic_field_amplification.md]]
>
> 下一章：[[02_cosmic-ray-origins/0005_amato-2014/literature_analysis/07_gammaray_snr.md|07_gammaray_snr.md]]

## 6.1 逃逸的物理图像（Blasi §6.1）

**[FACT]** 理想平面无限激波中，上游 CR 的返回概率为 1 → 所有粒子被永远困住，直到激波消散；但：
- (1) Sedov-Taylor 相激波减速，R_sh ∝ t^{2/5}，扩散前沿 ∝ t^{1/2} → 粒子更易逃逸；
- (2) 激波可能破裂；
- (3) 自散射中心机制在远离激波处失效（粒子密度下降）。

**[FACT]** 主流建模：在 $z_{0}$ 处（~10% R_sh）设自由逃逸边界 f(p, $z_{0}$)=0。

**[FACT]** 该边界条件下分布函数（Blasi 式 (100)）：
$$f(z,p) = f_0(p)\, \frac{\exp(uz/D(p)) - \exp(uz_0/D(p))}{1 - \exp(uz_0/D(p))}$$

**[FACT]** 逃逸通量（Blasi 式 (101)）：
$$F(z_0,p) = -D(p)\frac{\partial f}{\partial z}\bigg|_{z=z_0} = -\frac{u_1 f_0(p)\, \exp(uz_0/D(p))}{1-\exp(uz_0/D(p))}$$

**[FACT]** 逃逸通量在动量空间是一个**尖锐峰值**，峰值位于 $D(p^*)/u_1 \simeq x_0$。

## 6.2 Sedov-Taylor 相的逃逸粒子谱（Blasi §6.1 尾）

**[FACT]** 假设 p_max(t) ∝ (t/T_s)^{-α}，能量守恒（Blasi 式 (102)）：
$$d\epsilon = 4\pi p^2 dp\, p c\, N_{esc}(p) = \xi_{esc}\,\frac{1}{2}\rho v_{sh}^3\, 4\pi R_{sh}^2\, dt$$

**[FACT]** 在 Sedov-Taylor 相（R_sh ∝ t^{2/5}，V_sh ∝ t^{-3/5}），导出（Blasi 式 (103)）：
$$\boxed{N_{esc}(p) \propto p^{-4}\, \xi_{esc}(t)}$$

**[INTERPRETATION]** 这个 p⁻⁴ 与 test-particle DSA 的 p⁻⁴ **无关**——它纯粹是 Sedov-Taylor 自相似演化 + 峰状逃逸的直接后果。若 ξ_esc 随时间下降，逃逸谱**比 p⁻⁴ 更硬**。

## 6.3 Amato §3.2：逃逸粒子的谱（同源推导）

**[FACT]** Amato 给出更一般的推导（Amato 式 (17)-(18)）：假设 R_S ∝ t^α, V_S ∝ t^{α-1}, p_max ∐ t^β，则：
$$N_{esc}(p) \propto f_{esc}\, p^{-4}\, t^{5\alpha - 2}$$

**[FACT]** 当 α = 2/5（Sedov-Taylor）：$N_{esc}(p) \propto f_{esc}\, p^{-4}$ → 与 Blasi 结果完全一致。

**[FACT]** Amato Fig.4：一个"典型"SNR 释放的 CR 谱：
- 逃逸粒子（虚线）比 p⁻⁴ 更硬；
- 后期释放（点划线，被对流到下游的）在最高能端贡献少；
- **总谱（实线）接近 p⁻⁴**；
- 但该"典型"SNR 的最高能量仍**达不到膝区**。

## 6.4 SNR 释放的完整谱：NLDSA 预测（Blasi §6.2）

**[FACT]** Blasi Fig.10（Caprioli et al. 2010a）：$n_{0}$ = 0.1 cm⁻³, $T_{0}$ = $10^{5}$ K, ξ_inj = 3.9, 逃逸边界 χ=0.15 R_sh。
- 虚线：逃逸粒子
- 点划线：激波消散后释放的粒子（能量损失导致高能端截断）
- 实线：总谱
- **最高能端出现"鼓包"**，因为逃逸通量主导

**[CRITIQUE]** Blasi 明确指出 NLDSA 预测的总谱在**两个层面**与观测不符：
1. **γ 射线观测**：SNR 的推断粒子谱比 E⁻² **更陡**（Caprioli 2011）；
2. **银河系各向异性**：若注入谱 ~E⁻²，需要 D(E) ∝ E^{0.7} → 各向异性**远**超观测值（Ptuskin 2006; Blasi & Amato 2012b）。

**[FACT]** Amato §5 进一步分析：
- 从 B/C 反推 δ 的不确定性 → 注入谱斜率 **2 < γ_inj < 2.4**；
- 用 GALPROP/DRAGON 无法解决"离散源"问题；
- 包含源空间-时间离散性的计算（Blasi & Amato 2012a,b 或类似）显示：
  - γ_inj = 2.34, δ = 1/3（Kolmogorov）→ 谱与各向异性**都**符合；
  - γ_inj = 2.07, δ = 0.6 → 谱符合但各向异性**过大**（Amato Fig.7-8）；
- **结论**：SNR 注入的 CR 谱比 E⁻² 更陡（γ_inj ~ 2.3–2.4），与 NLDSA 的"凹形硬谱"预测**严重矛盾**。

## 6.5 可能的理论修订（Blasi §6.2 尾 & Amato §6）

**[FACT]** 多种"软化"机制被提出：

1. **快速运动的散射中心**（Bell 1978a; Ptuskin 2010; Caprioli 2010a, 2012）：
   谱斜率由波速修正的压缩比决定（Blasi 式 (104)）：
   $$\alpha = \frac{\tilde{r}+2}{\tilde{r}-1},\quad \tilde{r} = \frac{u_1 \pm v_{W,1}}{u_2 \pm v_{W,2}}$$
   若 v_W 为放大磁场中的 Alfvén 速度，谱可显著变陡。

2. **主要垂直激波几何**（Schure & Bell 2013）：下游返回概率降低 → 更陡谱。

3. **局域密度涨落**（Berezhko 2013）：假设 SNR 中存在不均匀高密度团块，可把硬谱"伪装"成观测到的陡谱。

**[CRITIQUE]** Blasi 坦言这些机制"依赖理论细节"，很难判断哪个是真正的答案。