---
section: "2.2"
title: "Shock kinematics and scatter-free acceleration"
pages: "982-987"
parent: "00_overview.md"
previous: "02_basic_theory.md"
next: "04_diffusive_acceleration.md"
---

# 2.2 Shock kinematics and scatter-free acceleration

原文§2.2，p.982-987（fulltext.txt 行 269-458）

## 2.1 激波运动学与分类

[FACT] 局部近似将激波面视为平面，上游/下游介质均匀，速度 $U_1, U_2$，磁场 $B_1, B_2$。

[FACT] 高电导率保证电场所零于等离子体静止系：$\mathbf{E} = -\mathbf{U}_{1,2}\times\mathbf{B}_{1,2}$。

[FACT] **超磁声/亚磁声**区分：磁场线与激波面的交点运动速度 $v_{\rm int} = U_1/\cos\theta_1$ 与光速 $c$ 的比较；只有亚磁声情形粒子才能从激波反射。

[FACT] 亚磁声情形：存在唯一框架，激波静止、电场为零、$\mathbf{U}_1\parallel\mathbf{B}_1$、$\mathbf{U}_2\parallel\mathbf{B}_2$（图 1a，p.979 行 303）。

[FACT] 超磁声情形：洛伦兹变换到"交点速度无穷大"框架，磁场垂直激波法线，激波不静止；再沿激波法线 boost 到激波静止系，此时 $B_1,B_2$ 都垂直法线，$B_2 = r B_1$（图 1b）。

## 2.2 关键运动学量

[FACT] 定义 $\theta_{1,2}$ 为 $B_{1,2}$ 与激波法线夹角；压缩比 $r = U_{1x}/U_{2x}$。

- $\theta_1 = \theta_2 = 0$：**平行激波（parallel）**
- 否则：**斜激波（oblique）**

[FACT] MHD Rankine–Hugoniot 条件（de Hoffmann & Teller 1950, Lust 1955a,b）：一般情况下 $\mathbf{U}_2,\mathbf{B}_2$ 在 $xy$ 平面内，将 $\theta_2, r$ 与上游动力学参数关联。

## 2.3 强激波情形（special case）

[FACT] 质量守恒 (2.15)：$\rho_1 U_{1x} = \rho_2 U_{2x} = A$

[FACT] 动量守恒 (2.16)：$U_{1y} = U_{2y}$；$A U_{1x} = A U_{2x} + P$（$P$ = 下游压力）

[FACT] 能量守恒 (2.17)：$\rho_1 U_{1x}(\frac{1}{2}U_1^2 + \frac{\gamma}{\gamma-1}\frac{P_1}{\rho_1}) = A U_{2x}(\frac{1}{2}U_2^2 + \frac{\gamma}{\gamma-1}\frac{P}{\rho_2})$

[FACT] 由此 $r = 1 + \frac{2}{(\gamma+1)}\frac{1}{M^2}$（强激波 $M\to\infty$）：

- 单原子非相对论气体 $\gamma=5/3$：$P = \frac{2}{3}\mathcal{E}$，**$r = 4$**
- 相对论气体 $\gamma=4/3$：$P = \frac{1}{3}\mathcal{E}$，**$r = 7$**

[FACT] 由 $U_{1x} = r U_{2x}$ 和 $U_{1y} = U_{2y}$：$r\tan\theta_1 = \tan\theta_2$——磁场"变垂"关系。

## 2.4 无散射加速（scatter-free, Liouville 定理）

[FACT] 超磁声情形：粒子在磁场中做螺旋运动叠加 $\mathbf{E}\times\mathbf{B}$ 漂移，穿越激波时下游回旋半径变小，产生沿 $\mathbf{E}$ 方向的漂移从而获得动量（p.981 行 374-382）。

[FACT] 在 $U \gg U_{1x}$ 极限下应用 Liouville 定理，得到 (2.22)-(2.23)：

$$p_{\perp 2}^2 = r\, p_{\perp 1}^2 + \text{const.}$$

常数由 $p_{\perp 1}=0 \Rightarrow p_{\perp 2}=0$ 确定，得 $p_{\perp 2} = \sqrt{r}\, p_{\perp 1}$。

[FACT] 物理解释：粒子近似守恒第一绝热不变量（first magnetic moment）——如同磁场变化绝热而非突变（但机制不同：靠 gyrophase 无关性）。

## 2.5 无散射加速的局限

[FACT] 对平行激波：单次穿越能量增益仅"moderate"，不能解释幂律尾部。

[FACT] 全过程是纯运动学且可逆的——"essentially the pre-acceleration spectrum shifted in energy"。

[INTERPRETATION] 无散射加速只是 DSA 的"第一阶"——真正的幂律需要**扩散返回**（repeated shock crossings via diffusion），这是 § 2.3 的核心。

[CRITIQUE] 无散射机制在相对论激波或磁重联区域可能有重要贡献（§ 3.1 讨论斜激波时再回到此问题）。

下一章：[[04_diffusive_acceleration.md]]
上一章：[[02_basic_theory.md]]
