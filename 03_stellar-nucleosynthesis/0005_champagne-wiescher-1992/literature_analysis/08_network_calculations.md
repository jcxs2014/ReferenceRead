> 本章属于：[[03_stellar-nucleosynthesis/0005_champagne-wiescher-1992/literature_analysis/00_overview.md|[Champagne & Wiescher 1992, *Explosive Hydrogen Burning*]]]
>
> 上一章：[[03_stellar-nucleosynthesis/0005_champagne-wiescher-1992/literature_analysis/07_rp_process_impedance.md|07_rp_process_impedance.md]]
>
> 下一章：[[03_stellar-nucleosynthesis/0005_champagne-wiescher-1992/literature_analysis/09_figures_and_tables.md|09_figures_and_tables.md]]

---

# 8. Network Calculations (p. 66–73) & Concluding Remarks (p. 73–74)

## 8.1 本节核心内容

把前述反应率整合进**大规模反应网络**，对**三种典型天体物理条件**计算产物演化，得到 rp-process 的**端点核素**随 ($T_{9}$, $\rho$, t) 的变化。

## 8.2 网络计算框架

### 8.2.1 净反应流定义（式 8）

**[FACT]** 两核素 i 与 j 之间的**净反应流**：

$$F_{ij} = \int \left[\dot{Y}(i \rightarrow j) - \dot{Y}(j \rightarrow i)\right] dt \tag{8}$$

其中 $\dot{Y}(i \rightarrow j)$ 是所有将核素 i 转化为 j 的反应引起的**同位素丰度 Y_i 随时间变化率**（Y = X/A，质量分数除以原子数）。

### 8.2.2 同位素丰度演化（式 9）

**[FACT]** 全部耗尽与产生反应率 $\lambda_{\rm i}$ 给出的**总时间演化**：

$$\dot{Y}_i = \sum_j \lambda_{ji}^{1} + \sum_{j,k} \lambda_{jk \rightarrow i}^{2} Y_k \tag{9}$$

- 第一项：所有核素 j → i 的 **$\beta^\pm$ 衰变 + 光裂**
- 第二项：核素 j 与 k 间的**两粒子反应**产生 i

### 8.2.3 网络规模

**[FACT]** Wallace & Woosley (18) 用于 A ≤ 40 的网络被**更新与扩展**。

**[FACT]** 新网络包含：

- **216 个稳定和不稳定核素**
- **946 个核相互作用**——包括 **$\beta^\pm$/电子俘获弱相互作用**，以及 **(p,$\gamma$)、(p,$\alpha$)、($\alpha$,$\gamma$)、($\alpha$,p)** 反应及其逆反应

### 8.2.4 计算的三种条件

**[FACT]** 三种温度、密度、时标：

| 编号 | $T_{9}$ | $\rho$ (g/cm$^{3}$) | 时标 t | 对应天体物理事件 |
|------|-----|-----------|--------|-----------------|
| (i)  | 0.3 | $10^{3}$       | 10 s   | 超新星激波 |
| (ii) | 0.4 | $10^{4}$       | 1000 s | 新星热失控 |
| (iii)| 1.5 | $10^{6}$       | 10 s   | X 射线暴热失控 |

**[FACT]** 全部计算在**恒定 T 和 $\rho$**下进行。

**[FACT]** 初始元素丰度分布采用**太阳同位素丰度** (121)。

## 8.3 章节 5.1: Low Temperatures and Densities ($T_{9}$ = 0.3, $\rho$ = $10^{3}$, t = 10 s)

### 8.3.1 反应流图 (Figure 4)

**[FACT]** A = 20–60 反应流：

- **HCNO 循环**清晰标注，导致 **$^{14}{\rm O}$、$^{15}{\rm O}$、$^{18}{\rm Ne}$ 等待点核**的丰度因 $^{12}{\rm C}$、$^{13}{\rm C}$、$^{16}{\rm O}$ 的两次质子俘获而**增强**。
- **HCNO 与 NeNa 区之间无连接** → rp-process **仅在已有 A ≳ 20 物质时才发生**。

### 8.3.2 NeNa 循环（高温版）

**[FACT]** NeNa 区反应流指示**热 NeNa 循环**：

$$^{20}\text{Ne}(p,\gamma)^{21}\text{Na}(p,\gamma)^{22}\text{Mg}(\beta^+\nu)^{22}\text{Na}(p,\gamma)^{23}\text{Mg}(\beta^+\nu)^{23}\text{Na}(p,\alpha)^{20}\text{Ne} \tag{11}$$

### 8.3.3 通向重质量的瓶颈

**[FACT]** 通过两个**瓶颈反应**：$^{23}{\rm Mg}$(p,$\gamma$)$^{24}{\rm Al}$ 与 $^{24}{\rm Mg}$(p,$\gamma$)$^{25}{\rm Al}$。

**[FACT]** 因**从 NeNa 循环逃逸的时间常数大**，大部分物质**在整个计算时标内被局限在 NeNa 区**。

### 8.3.4 SiP 循环

**[FACT]** 连续反应序列通向 Si,P,S 区：

$$^{24}\text{Al}(p,\gamma)^{25}\text{Si}(\beta^+\nu)^{25}\text{Al}(p,\gamma)^{26}\text{Si}(\beta^+\nu)^{26}\text{Al}(p,\gamma)^{27}\text{Si}(p,\gamma)^{28}\text{P}(\beta^+\nu)^{28}\text{Si} \tag{\text{11 (续)}}$$

**[FACT]** 热 SiP 循环：

$$^{28}\text{Si}(p,\gamma)^{29}\text{P}(p,\gamma)^{30}\text{S}(\beta^+\nu)^{30}\text{P}(p,\gamma)^{31}\text{S}(\beta^+\nu)^{31}\text{P}(p,\alpha)^{28}\text{Si} \tag{12}$$

### 8.3.5 端点核素（低 T 情形）

**[FACT]** 显著比例的 SiP 物质通过 **$^{31}{\rm P}$(p,$\gamma$)$^{32}{\rm S}$(p,$\gamma$)$^{33}{\rm Cl}$** 加工至更重质量。

**[FACT]** 到 $^{40}{\rm Ca}$ 的反应流**弱**。

**[FACT]** **Figure 5**（时间演化）：

- 初始 $^{20}{\rm Ne}$ 主要加工为 **$^{22}{\rm Mg}$**，因长半衰期（$T_{1}$/$_{2}$ = **3.86 s**）**被禁闭**。
- 已有 $^{24}{\rm Mg}$ 和 $^{28}{\rm Si}$ 加工为 **$^{26}{\rm Si}$ ($T_{1}$/$_{2}$ = 2.23 s)** 和 **$^{30}{\rm S}$ ($T_{1}$/$_{2}$ = 1.18 s)**。
- 这些衰变导致 **$^{31}{\rm S}$ ($T_{1}$/$_{2}$ = 2.57 s) 富集**。
- $^{31}{\rm S}$ 主要衰变至 **$^{31}{\rm P}$**，被 (p,$\alpha$) 反应再循环回 **$^{28}{\rm Si}$**——**在 SiP 区分布**。

**[FACT]** SiP 循环时间常数 = $\tau_{\rm SiP}$ = $\tau_{^{31}{\rm S}}$ · (p,$\gamma$)/(p,$\alpha$)。

**[FACT]** $^{32}{\rm S}$ 通过 $^{31}{\rm P}$(p,$\gamma$) 的产率比 $^{32}{\rm S}$(p,$\gamma$)$^{33}{\rm Cl}$ 消耗率**大三个量级** → 每循环一次 $^{31}{\rm P}$(p,$\gamma$)$^{32}{\rm S}$ 分支导致 **$^{32}{\rm S}$ 最终增强**。

**[FACT]** **对 A = 20–32 初始物质，燃烧 10 s 后 $^{32}{\rm S}$ 是核合成端点**；**更长燃烧期端点为 $^{40}{\rm Ca}$**。

**[FACT]** **此结果不同于**基于 Wallace & Woosley (18) 旧 $^{32}{\rm S}$(p,$\gamma$)$^{33}{\rm Cl}$ 率的网络计算——**旧率比 Iliadis 等人 (104) 新测量率高两个量级**。

## 8.4 章节 5.2: Intermediate Temperatures and Densities ($T_{9}$ = 0.4, $\rho$ = $10^{4}$, t = 1000 s)

### 8.4.1 反应流图 (Figure 6)

**[FACT]** 典型 nova 峰值 $T_{9}$ ~ 0.2 → 主 HCNO 主导。

**[FACT]** **能量 nova ($T_{9}$ = 0.4)** → rp-process 也重要。

**[FACT]** Figure 6（燃烧时标 100 s）显示**从 CNO 区到 A ~ 20 区的显著流**，路径：

$$^{14}\text{O}(\alpha,p)^{17}\text{F}(p,\gamma)^{18}\text{Ne}(\beta^+\nu)^{18}\text{F}(p,\gamma)^{19}\text{Ne}(p,\gamma)^{20}\text{Na}(p,\gamma)^{21}\text{Mg} \tag{13}$$

### 8.4.2 $^{22}{\rm Mg}$ 处的分叉

**[FACT]** 在 $^{22}{\rm Mg}$ 等待点，流分两支**绕过 NeNa 和 MgAl 循环**：

**第一支**（从 $^{22}{\rm Mg}$(p,$\gamma$)$^{23}{\rm Al}$ 启动）：

$$^{22}\text{Mg}(p,\gamma)^{23}\text{Al}(p,\gamma)^{24}\text{Si}(\beta^+\nu)^{24}\text{Al}(p,\gamma)^{25}\text{Si}(\beta^+\nu)^{25}\text{Al}(p,\gamma)^{26}\text{Si}(\beta^+\nu)^{26}\text{Al}(p,\gamma)^{27}\text{Si} \tag{14}$$

**第二支**（跟随 $^{22}{\rm Mg}$ $\beta$ 衰变）：

$$(^{22}\text{Mg} \xrightarrow{\beta^+} ^{22}\text{Na} \rightarrow \ldots) \tag{15}$$

### 8.4.3 更高 A 的流

**[FACT]** 沿质子滴线的一系列反应：$^{27}{\rm Si}$(p,$\gamma$)$^{28}{\rm P}$(p,$\gamma$)$^{29}{\rm S}$($\beta^\pm$$\nu$)$^{29}{\rm P}$(p,$\gamma$)$^{30}{\rm S}$。

**[FACT]** A ~ 40 区由**三个反应循环**特征化：**SiP、SCl、ArK**，通过瓶颈反应 **$^{31}{\rm S}$(p,$\gamma$)$^{32}{\rm Cl}$、$^{35}{\rm Ar}$(p,$\gamma$)$^{36}{\rm K}$** 分支互连。

**[FACT]** 向 A > 40 的推进通过两个**弱质子俘获**反应：**$^{39}{\rm Ca}$(p,$\gamma$)$^{40}{\rm Sc}$** 与 **$^{40}{\rm Ca}$(p,$\gamma$)$^{41}{\rm Sc}$** (122)，进入 **CaSc 循环**。

**[FACT]** 燃烧 ~20 s 后达到此阶段。

**[FACT]** A = 50 区，流通过 **$^{43}{\rm Ti}$(p,$\gamma$)$^{44}{\rm Y}$($\beta^\pm$$\nu$)$^{44}{\rm Ti}$(p,$\gamma$)$^{45}{\rm Y}$** 与 **$^{43}{\rm Sc}$(p,$\gamma$)$^{44}{\rm Ti}$(p,$\gamma$)$^{45}{\rm Y}$** 从 CaSc 循环泄漏。

**[FACT]** 进一步反应达到端点 **$^{52}{\rm Fe}$**。

### 8.4.4 时间演化 (Figure 7)

**[FACT]**

- **$^{20}{\rm Ne}$** 在过程第 1 秒内耗尽 → 转换为 **$^{22}{\rm Mg}$**（$T_{1}$/$_{2}$ = 3.86 s）。
- 因 $^{22}{\rm Mg}$ 可被 (p,$\gamma$) 破坏，**有效半衰期更短，$T_{1}$/$_{2}$,eff = 2.4 s**。
- 物质在等待点核 **$^{34}{\rm Ar}$ 和 $^{40}{\rm Ca}$** 中转换；丰度在 **~10 s 后达到生产-衰变平衡**。
- 后续因生产流停止，净丰度下降。
- **$^{40}{\rm Ca}$ 显著增强**（因弱衰变反应 $^{40}{\rm Ca}$(p,$\gamma$)$^{41}{\rm Sc}$）。
- 进一步加工完全转换 $^{40}{\rm Ca}$ 为 **$^{52}{\rm Fe}$**。
- 因 **$^{52}{\rm Fe}$ 长 $\beta$ 衰变半衰期 ($T_{1}$/$_{2}$ = 8.28 h)** 与弱 $^{52}{\rm Fe}$(p,$\gamma$)$^{53}{\rm Co}$ 衰变率 → **$^{52}{\rm Fe}$ 是该条件下 rp-process 的端点**。

## 8.5 章节 5.3: High Temperatures and Densities ($T_{9}$ = 1.5, $\rho$ = $10^{6}$, t = 10 s)

### 8.5.1 反应流图 (Figure 8)

**[FACT]** X 射线暴条件，预期持续 ≤10 s (11)。

**[FACT]** 反应流**从 $^{4}{\rm He}$ 连续流至 $^{73}{\rm Kr}$**——反应网络的端点。

**[FACT]** 爆发初期，**$^{12}{\rm C}$ 由三聚反应（triple reaction）产生，随后快速转换为 $^{14}{\rm O}$**。

**[FACT]** 轻等待点核 **$^{14}{\rm O}$, $^{18}{\rm Ne}$, $^{22}{\rm Mg}$, $^{28}{\rm Si}$, $^{30}{\rm S}$, $^{34}{\rm Ar}$** 通过 **(n,p) 反应序列**（称为 **np-process** (73)）**跨越**。

**[FACT]** **A > 38** 后，rp-process 路径由**质子滴线附近的质子俘获 + $\beta$ 衰变**特征化，**直至 Ni 区**。

**[FACT]** 因库仑势垒增大，(n,p) 反应**太慢无法与 $\beta$ 衰变竞争**。

**[FACT]** **$^{54}{\rm Ni}$ 被预言为粒子未束缚** (123) → 反应流沿：

$$^{53}\text{Co}(\beta^+)^{53}\text{Fe}(p,\gamma)^{54}\text{Co}(p,\gamma)^{55}\text{Ni}(p,\gamma)^{56}\text{Cu}(\beta^+)^{56}\text{Ni}(p,\gamma)^{57}\text{Cu} \tag{16}$$

**[FACT]** $^{55}$,$^{56}{\rm Ni}$ 上的 (p,$\gamma$) 反应 Q 值低（Q = **0.459 和 0.767 MeV**）→ **被光裂抑制** (120)。

**[FACT]** 反应继续至 **$^{64}{\rm Ge}$ ($T_{1}$/$_{2}$ = 63.7 s)**——在爆发期间**本质稳定**。

**[FACT]** 若 **$^{65}{\rm As}$ 质子未束缚** → **$^{64}{\rm Ge}$ 在 X 射线暴期间终止 rp-process**。

**[FACT]** 若 $^{65}{\rm As}$ 稳定 → 反应路径继续：

$$^{65}\text{As}(p,\gamma)^{66}\text{Se}(\beta^+)^{66}\text{As}(p,\gamma)^{67}\text{Se}(\beta^+)^{67}\text{As}(p,\gamma)^{68}\text{Se} \tag{17}$$

和

$$^{68}\text{Se}(p,\gamma)^{69}\text{Br}(p,\gamma)^{70}\text{Kr}(\beta^+)^{70}\text{Br}(p,\gamma)^{71}\text{Kr}(\beta^+)^{71}\text{Br}(p,\gamma)^{72}\text{Kr} \tag{18}$$

（前提 **$^{69}{\rm Br}$ 亦粒子稳定**）。

**[FACT]** 近期测量表明 **$^{73}{\rm Rb}$ 粒子未束缚** (110) → **rp-process 终止于 $^{72}{\rm Kr}$ ($T_{1}$/$_{2}$ = 17.2 s)**。

### 8.5.2 时间演化 (Figure 9)

**[FACT]**

- **0.5 s 后**，已有 CNO 与 NeNa 物质转换为 **$^{34}{\rm Ar}$**。
- **1 s 后**，($\alpha$,p) 过程产生 **$^{38}{\rm Ca}$**。
- **$^{55}$,$^{56}{\rm Ni}$ 丰度在 1.5 s 达峰值**。
- **5 s 后**，大部分原始物质达到 **$^{64}{\rm Ge}$**。
- **$^{64}{\rm Ge}$ 丰度缓慢下降**——因破坏过程 $^{64}{\rm Ge}$(p,$\gamma$)$^{65}{\rm As}$ 与 $^{64}{\rm Ge}$($\beta^\pm$)$^{64}{\rm Ga}$ 均弱。
- **$^{64}{\rm Ge}$ 最终转换为 $^{72}{\rm Kr}$**，20 s 后达到丰度峰值。

## 8.6 三情形端点核素对比

| 情形 | $T_{9}$ | $\rho$ (g/cm$^{3}$) | t (s) | 端点核 | 主要过程 |
|------|-----|-----------|--------|-------|---------|
| (i) | 0.3 | $10^{3}$ | 10 (或 100) | **$^{32}{\rm S}$** (或 $^{40}{\rm Ca}$) | 弱 rp-process |
| (ii) | 0.4 | $10^{4}$ | 1000 | **$^{52}{\rm Fe}$** | rp-process 完整段 |
| (iii) | 1.5 | $10^{6}$ | 10 | **$^{72}{\rm Kr}$** | rp-process + np-process 全开 |

**[INTERPRETATION]** 端点核随 ($T_{9}$, $\rho$, t) **单调向更重质量移动**——这直观反映了**温度与密度对质子俘获速率的指数增强** + **np-process 在高温下跨越 $\beta$ 等待点**的双重作用。

## 8.7 Concluding Remarks (p. 73–74)

**[FACT]** 作者的核心结语：

> "Although an impressive amount of effort has been devoted to understanding nucleosynthesis during explosive hydrogen burning, a great deal of work remains to be done. The reactions described in this review are only a few of the reactions of interest. All are uncertain to some degree."

**[FACT]** 网络计算虽已进行，但"based on our knowledge of reaction rates, it is fair to ask if we have not built a house of cards."——**经典的"沙上建塔"比喻**。

**[FACT]** "There is no substitute for measured rates"——**反应率测量不可替代**。

**[FACT]** 这既需要**放射性束的持续发展**，也需要**传统核光谱学**（质量、寿命等核输入的必备来源）。

**[FACT]** 将测量推至质子滴线**需要放射性束**。

## 8.8 关键公式（第 5 章汇总）

| 公式编号 | 表达 | 用途 |
|---------|------|------|
| (8) | F_ij = ∫[Ẏ(i→j) − Ẏ(j→i)] dt | 净反应流 |
| (9) | Ẏ_i = $\Sigma$ $\lambda$_{ji}$^{1}$ + $\Sigma$ $\lambda$_{jk→i}$^{2}$ Y_k | 同位素丰度演化 |

## 8.9 潜在问题与值得注意之处

1. **[FACT]** **np-process**（§5.3）是 Woosley (73) 提出但**本文首次在 $T_{9}$=1.5 网络中显式包含**的过程——它是**rp-process 在 X 射线暴条件下能跨越 $\beta$ 等待点**的关键机制。
2. **[CRITIQUE]** 所有网络计算在**恒定 T 和 $\rho$**下进行——这显著**简化**了真实 nova/X 射线暴的热力学演化（温度/密度随时间变化）。这是**反应网络计算的常见近似**，但会使丰度峰值时间被人为提前或推后。
3. **[FACT]** 初始丰度采用**太阳同位素丰度**——对 nova 而言，这**忽略了白矮星表面的化学富集**（例如 CNO 处理过的物质）。真实 nova 计算需更精细的初始丰度（如 CNO 平衡后的 C、N、O 比例）。
4. **[CRITIQUE]** 端点 $^{72}{\rm Kr}$ 的预言**依赖** $^{73}{\rm Rb}$ 的质子未束缚状态 (110)——这是**1991 年的实验结果**（Mohar et al. PRL 66:1571–74）。如果后续测量修正此结论，端点需重新评估。

## 8.10 参考文献（本章）

- (18) Wallace & Woosley ApJ Suppl. 45:389–420 (1981)
- (19) Wiescher et al. A&A 160:56–72 (1986)
- (31) Cowan, Thielmann & Truran Phys. Rep. 208:267–394 (1991)
- (73) Woosley (1985)
- (104) Iliadis et al. NP A539:97–111 (1992)
- (110) Mohar et al. PRL 66:1571–74 (1991)
- (114) Van Wormer (1991)
- (120) Wiescher et al. (Proc. RIB)
- (121) Anders & Ebihara Geochim. Cosmochim. Acta 46:2363 (1982)
- (122) Wiescher & Görres ApJ 346:1041–44 (1989)
- (123) Masson & Janecke At. Data Nucl. Data Tables 39:273–80 (1988)