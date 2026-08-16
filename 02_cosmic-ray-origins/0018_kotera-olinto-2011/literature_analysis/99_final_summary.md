> 本章属于：**The Astrophysics of Ultrahigh Energy Cosmic Rays** (Kotera & Olinto, 2011)
>
> 上一章：`97_quality_check.md`
>
> 下一章：无

# 99 Final Summary

## 15.1 一句话总结

Kotera & Olinto 2011 是 UHECR 天体物理的**权威综述**：系统梳理观测现状（GZK 已确认、hint 级各向异性、成分谜团）、传播物理（背景辐射 + 磁场二自由度）、加速机制、候选源（Hillas + 五重检验）、多信使（cosmogenic ν 是关键探针），并给出下一代观测路线图。

## 15.2 核心贡献

1. **观测总结的权威整合**：HiRes + Auger 2010 数据联合，成分谜团首次清晰呈现
2. **传播物理框架化**：将"谱"与"各向异性"分别归因到背景辐射与磁场 → 观测谜题不再矛盾
3. **候选源筛选标准**：Hillas 判据 + t_acc/t_esc/t_age/t_loss + L_B 下限 = 五重检验
4. **磁星模型的正名**：重核注入 + 瞬发特性 → 自然解释 Auger 40 EeV 重核 + 无瞬发对应
5. **Cosmogenic ν 作为模型判据**：Fig 12 明确量化 → 一个 EeV ν 即可划掉一半模型
6. **"Fake correlation" 效应**：EGMF 时间延迟让瞬发源伪造与前景物质相关 → 解释"无对应"

## 15.3 方法论

- 综述式写作：观测 → 理论 → 应用 → 未来路线
- 严格区分 [FACT]/[INTERPRETATION]/[CRITIQUE]
- 每张图单独分析，每个公式保留完整
- 数值参数保留单位与上下文

## 15.4 关键数值

| 物理量 | 数值 |
|--------|------|
| 膝点 | ~1 PeV |
| 踝点 | ~3 EeV |
| GZK 截断起始 | ~30 EeV |
| GZK 视界 | ~100 Mpc |
| 磁星表面磁场 | ~10¹⁵ G |
| Hillas E_max 参考 | 1 EeV · Z · (B/μG) · (R/kpc) |
| AGN 中心 E_max | ~10¹⁹ eV (辐射损失限制) |
| 磁星理论 E_max | ~3×10²¹ eV |
| IceCube cosmogenic ν 预期 | 0.06–0.2 /yr |
| Auger cosmogenic ν 预期 | 0.03–0.06 /yr |
| 银河 Fe E_max (SNR) | ~5 EeV (Ptuskin 2010) |

## 15.5 重要方程

- Hillas: **E_max ≈ ZeBRc ≈ 1 EeV · Z (B/μG) (R/kpc)**
- Cosmogenic 阈值: E_p,π ≈ 200 EeV (ε_CMB/ε)
- 磁延时: t_Δ ≈ 2.3×10² yr · Z² · (D/10 Mpc)² · (B/2×10⁻⁹ G)² · (l_B/0.1 Mpc)² · (10²⁰ eV/E)⁻²
- 能量学下限: L_B > 10⁴⁵ Z⁻² Ẇ₂₀² erg/s

## 15.6 与其他论文的关系

**上游（本文引用）**：
- bhattacharjee-sigl-2000 (02/0001) — 早期综述，本文扩展
- hillas-1984 (02/0011) — Hillas 判据原始，本文 §6.1 完整复现
- Greisen 1966; Zatsepin & Kuzmin 1966 — GZK 理论
- Allard et al. 2007; Kotera et al. 2010b — 谱拟合
- Kotera & Lemoine 2008b — "fake correlation" 方法

**下游（引用本文）**：
- **alvesbatista-2019 (02/0014)** — 本文的 2019 更新版：IceCube PeV 中微子首批结果、Auger 偶极各向异性、TA 结果、成分再讨论
- telescope-array-2023 (02/0015) — TA 观测综述，用本文框架分析 TA 数据

**路径 A 核心节点**：本文是 UHECR 起源研究的**关键中间综述**——上游 Hillas 判据 + GZK 理论，下游 alvesbatista-2019 与 telescope-array-2023。

## 15.7 开放问题（2011 状态，部分已解）

1. **成分**：Auger 重核 vs HiRes 轻核 → 2017 Auger 确认重核趋势，HiRes 数据量有限
2. **源类**：AGN/GRB/磁星/吸积激波哪个是主导？→ 仍无定论
3. **EGMF 强度**：10⁻¹⁶ – 10⁻⁹ G 跨度 → 2020 年约束到 ~10⁻¹⁴ G 量级（有限进展）
4. **Cosmogenic ν**：0.03–0.2 ν/年 → IceCube 2020 给出上限，Auger 2022 首次发现 ~100 PeV ν 事件，**验证了本文 Fig 12 灰区低端**
5. **LHC 校准强子模型** → 已进行，影响 Xmax 判读

## 15.8 阅读建议

- **必须配合**：alvesbatista-2019 (02/0014) 作为 2011 后更新；telescope-array-2023 (02/0015) 作为观测对照
- **上游基础**：hillas-1984 (02/0011) Hillas 判据原始
- **传播代码**：CRPropa 官方文档 (若需重算)
- **强子模型**：EPOS-LHC, QGSJETII-4, Sibyl 2.1（Auger 2017 以后采用）

---

## Completeness Check

- [x] Abstract, Introduction (§1), All main sections (§2–§7)
- [x] All 12 Figures (Fig 1–12) 逐一分析
- [x] 核心公式 (Hillas、传播阈值、t_Δ、L_B、磁星注入谱)
- [x] 关键数值表 (frontmatter + §2-§6)
- [x] 候选源四大类 (§6.1.1-§6.1.4)
- [x] 多信使 (§6.3) cosmogenic ν / γ / Waxman-Bahcall
- [x] 术语表 (98_vocabulary.md) 50+ 条目
- [x] Citations 明确 (outgoing + incoming)
- [x] 路径 A 关系 (alvesbatista-2019) 明确

**精读状态：完成。**
