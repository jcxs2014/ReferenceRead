# 子节镜像示例（路径 A）— Ruszkowski & Pfrommer 2023, §2.1

> 性质：**精读深度扩充备忘 §4.3「小样本验证」产物**（2026-08-15，用户拍板"先小样本验证再定稿"）
> 用途：展示 READING_INSTRUCTIONS §4 改写后的"路径 A（原文子节镜像）"分章形态，作为规范模板；验证通过后并入 §4
> 对照对象：现有 `01_cosmic-ray-propagation/0006_ruszkowski-pfrommer-2023/literature_analysis/02_physics.md`（路径 B：八段模板 + 内部编号三级标题）
> 素材：现有 02_physics 已核验内容重组（信息零新增），子节标题**逐字沿用原文**（fulltext 目录页）

---

## 形态对照（先看差异）

| | 现状（路径 B，存量风格） | 路径 A（本示例） |
|---|---|---|
| 二级标题 | `## 2.1 本节核心内容`（八段要素） | `## 2.1 Cosmic ray interactions with electromagnetic waves`（原文标题） |
| 子节 | `### 2.2.1 §2.1 ...`（模板内部编号，**无法寻址原文 2.1.1**） | `### 2.1.1 Estimates of cosmic ray number densities`（**原文子节号+标题，可 TOC/wikilink 寻址**） |
| 要素 | 八段固定（核心内容/原文/公式/参数/图表/逻辑/理解/问题） | 子节内按实际覆盖"核心内容/公式/参数/图表/逻辑"，不强制八段 |

---

# 2. Physics

## 2.1 Cosmic ray interactions with electromagnetic waves

> 原文 pp. 12–21。本节建立"CR 与磁化等离子体如何耦合"的物理基础：共振条件 → 波模分类 → 散射扩散 → 不稳定性。

**核心逻辑**：CR 通过与 MHD 波的 gyro-resonant 相互作用被散射，散射强度由磁场扰动决定；CR 自身又能驱动等离子体不稳定性放大扰动——形成自洽的"散射–反馈"闭环（§2.1.2 → §2.1.3 的衔接）。

### 2.1.1 Estimates of cosmic ray number densities

> **宇宙线数密度估计**

**核心内容**：给出银河盘与星系团 ICM 中 CR 数密度的量级估计，确立"CR 在粒子层面是微量组分"的基准。

**关键参数**：
- 银河盘（equipartition，Boulares & Cox 1990；Naab & Ostriker 2017）：CR 与磁场/湍动/热能能量密度近似均分；主导粒子能量 $\sim 10^{10}$ eV；ISM warm 相 $n \sim 1$ cm$^{-3}$ 时 CR 离子数密度 $\sim 10^{-9}$ cm$^{-3}$（每 $\sim 10^9$ 个 ISM 粒子约 1 个 CR 质子）
- ICM：$k_B T \sim 1$–$10$ keV、$n \sim 10^{-3}$ cm$^{-3}$；γ 射线给出 CR-to-thermal pressure ratio 上限 $\sim 10^{-2}$ → CR 数密度 $\sim 10^{-10}$ cm$^{-3}$（CR:background $\sim 10^{-7}$）

**逻辑**：粒子层面微量 ≠ 能量层面次要（equipartition）——为后文"CR 虽稀薄却能驱动反馈"埋下伏笔。

### 2.1.2 Cosmic ray-wave scattering and diffusion

> **宇宙线-波散射与扩散**

**核心内容**：CR 与 MHD 波的相互作用类型（gyro-resonant；集体波–粒散射显著降低有效 mean free path，Wentzel 1974），以及由此得到的扩散系数。

**关键公式**：
- 共振条件（论文 Eq. 1）：$$k_{\parallel}\,v_{\parallel} - \omega = \pm n\,\Omega_{\text{cr}}$$
  - $k_{\parallel}$/$v_{\parallel}$：沿磁场方向波数/CR 速度分量；$\Omega_{\text{cr}} = qB/(\gamma m c)$ 相对论回旋频率；$n=1$ 平行模式、$n>1$ 斜传播
- 扩散系数：$$D_{\text{cr}} \sim \tfrac{1}{3}\,\lambda_{\text{mfp}}\,c$$，$\lambda_{\text{mfp}}$ 由 Alfvén 波磁扰动 $B'/B_0$ 决定

**三种 MHD 波模**（系统分类）：Alfvén（$\omega = k_{\parallel} v_A$，$v_A = B/\sqrt{4\pi\rho}$）/ Fast magnetosonic（磁压+气压恢复力）/ Slow magnetosonic（气压为主）。

**关键参数**：散射各向异性——$\lambda_{\parallel} \gg \lambda_{\perp}$（平行磁场方向散射强、垂直弱）。

### 2.1.3 Cosmic ray driven plasma instabilities

> **宇宙线驱动的等离子体不稳定性**

**核心内容**：CR 驱动的四种等离子体不稳定性——CR 反馈的核心机制，说明 CR 如何自激散射所需的磁场扰动。

**关键公式与物理**：
1. **Streaming instability**（Parker 1965；Kulsrud & Pearce 1969）：CR 漂移速度超 Alfvén 速度时激发 Alfvén 波，gyro-resonant 增长率（Eq. 7，Shalaby et al. 2021）：
   $$\gamma_{\text{gyro}} \approx \Omega_{i,0}\,C\,\frac{n_{\text{cr}}(>p_{\min})}{n_i}\,\frac{v_d - v_A}{v_A}$$
   （$\Omega_{i,0} = qB/(m_i c)$；$C = (s-3)/(s-2)\sim\mathcal{O}(1)$；仅 super-Alfvénic CR 能驱动）
2. **Bell instability**（Bell 2004）：非共振电流驱动，放大 $B'$
3. **Whistler instability**（注 11）：电子 CR 驱动的 electron-scale 不稳定性
4. **Ion-cyclotron instability**（注 12）：离子回旋波不稳定激发

**补充**：注 10——相对磁场 oblique 传播的模式通常 subdominant。

---

## 验证要点（供 §4 定稿时评估）——✅ 用户已确认（2026-08-15）

1. **可寻址性** ✅：`### 2.1.1/2.1.2/2.1.3` 与原文子节一一对应，Obsidian TOC / wikilink 可直接定位原文 §2.1.2 的精读内容
2. **信息密度** ✅：与现有 02_physics 的 §2.1 部分（约 40 行八段混合）相比，本示例子节归位后**要素集中、章节寻址明确**；信息零丢失（素材全部来自已核验内容）
3. **工作量** ✅：对已有八段内容做"重组 + 补原文子节标题"，非重写——成本可控；若从零精读则直接在子节下写，不增额外步骤
4. **格式代价** ✅（用户拍板）：标题沿用原文英文，**标题下加中文翻译段**（`> **翻译内容**` 引用块，翻译直接加粗）——中英混排可读性解决

**用户决定（2026-08-15）**：路径 A 风格认可，**可分批应用到文献库**（存量分章分批改造）——分批方案见精读深度扩充备忘。
