# papers — 文献阅读与分析工作区

> **38 篇文献**（38 篇精读全部闭环）、38 篇分析目录、7 篇跨篇主题背景知识库。
>
> 按主题域 → 单篇论文 → `literature_analysis/` 三层结构组织。每篇文献按 `docs/READING_INSTRUCTIONS.md` 的 30 节规范精读（§4 分章结构：综述/长文献走"路径 A 子节镜像"，短篇走"路径 B 八段"）。

## 目录结构

```
papers/
├── README.md                       ← 本文档：工作区总览与接入 SOP
├── docs/READING_INSTRUCTIONS.md         ← 精读操作手册（30 节规范 + 数据一致性经验）
├── INDEX.md                        ← 38 篇论文分析入口（gen_index.py 自动生成）
├── docs/ADVANCEMENT.md                  ← 进阶方案（v2.1 + V2.2 补丁，已全部落地）
├── docs/WEBAPP_DESIGN.md                ← Webapp 架构与实现
├── docs/ENHANCEMENTS.md                 ← 改进建议清单（9 条全部完成，归档参考）
├── docs/TROUBLESHOOTING.md              ← 故障排除与修复记录（A/B/C/D/E/F 六类 + 排障 SOP）
├── backup/                         ← 历史快照
│
├── 01_cosmic-ray-propagation/      ← 宇宙线传播主题
│   └── NNNN_作者-年份/
│       ├── *.pdf                   ← 原文（被 .gitignore 忽略，库内单独 git add -f）
│       └── literature_analysis/    ← 精读产出
│           ├── 00_overview.md            ← 文献元数据 + 结构树 + 篇间导航
│           ├── 01_…NN_*.md              ← 正文分章
│           ├── 97_quality_check.md      ← 完成度自查（gen_quality_check.py 自动生成）
│           ├── 98_vocabulary.md          ← 词汇表（A 逻辑词 + B 术语 + C 长难句）
│           └── 99_final_summary.md
│
├── 02_cosmic-ray-origins/          ← 宇宙线起源与 UHECR 主题
├── 03_stellar-nucleosynthesis/     ← 恒星核合成与元素丰度主题
│
├── background/                     ← 跨篇主题知识体系（库级）
│   ├── 00_key_values.md             ← 跨篇关键数值速查表
│   ├── 01_cosmic_rays.md           ← 宇宙线物理（传播、加速、UHECR、CR-ISM）
│   ├── 02_nucleosynthesis.md       ← 恒星核合成（八大过程、BBN、爆炸性燃烧）
│   ├── 03_astrophysics.md          ← 太阳丰度与天体物理（太阳组成、恒星、暗物质）
│   ├── 04_critique_index.md        ← 跨篇 CRITIQUE 观点索引
│   ├── 05_glossary.md              ← 全库术语表（gen_glossary.py 自动生成，769 术语）
│   └── 06_controversy_evolution.md ← 争议演化时间线
│
├── webapp/                         ← 单文件 HTML 知识库（详见 webapp/README.md 引导）
│   ├── README.md                   ← webapp 引导（目录/构建链/快速开始/故障）
│   ├── shell.html                  ← HTML 模板（CSS + JS + KaTeX 集成）
│   ├── docs/                       ← webapp 文档（审查报告等）
│   ├── scripts/                    ← 12 个构建/服务脚本（统一管理，见下）
│   │   ├── build_webapp.py         ← 主构建（背景必跑，加 --include-papers 收论文）
│   │   ├── build_fm.py             ← 写 frontmatter（剥离 _strip_fact_tag 等防护）
│   │   ├── build_citations.py      ← citations 唯一生成器（篇间导航 → 库内引用）
│   │   ├── build_registry.py       ← 读 45 frontmatter → webapp/registry.json
│   │   ├── build_glossary.py       ← 从 38 篇 98_vocabulary.md 抽 → 05_glossary.md
│   │   ├── build_pwa.py            ← PWA 资源（manifest + 图标 + apple-touch-icon）
│   │   ├── apply_wikilinks.py      ← V2.2: 导航/citations → Obsidian wikilink
│   │   ├── patch_appendix_nav.py   ← V2.2: 给 97/98 附录补链（防孤立）
│   │   ├── audit.py                ← 构建后审计（18 条断言，失败非零退出）
│   │   ├── server.py               ← 形态 B 服务层（/api/progress?slug=, /api/rebuild）
│   │   ├── md2doc_html.py          ← md → HTML 片段
│   │   └── build_search_index.py   ← 全文搜索索引
│   ├── interactive.html            ← 构建产物（~4 MB，被 .gitignore 忽略）
│   ├── registry.json               ← 派生产物（45 条，构建生成，不入库）
│   └── glossary.json               ← 派生产物（769 术语，构建生成，不入库）
│
├── scripts/                        ← 库级工具（生成 + 文献内容处理）
│   ├── gen_index.py                ← 扫描 → INDEX.md
│   ├── gen_quality_check.py        ← 扫描 → 97_quality_check.md
│   ├── gen_glossary.py             ← 扫描 → 05_glossary.md（已被 webapp/scripts/build_glossary.py 替代）
│   ├── build_all.py                ← 全链路编排（scripts + webapp 构建链）
│   ├── quality_matrix.py           ← 8 列质量矩阵 + 子节镜像统计
│   ├── verify_claim.sh             ← 声称完成门禁（PASS=11）
│   ├── convert_unicode_math.py     ← 公式 Unicode → LaTeX（round1/round2）
│   ├── convert_supsub.py           ← Unicode 上下标 → LaTeX（全库清零）
│   └── fix_math_fragmentation.py   ← 公式割裂修复（幂等）
└── setup_obsidian.sh               ← Obsidian 仓库初始化
```

## 主题域

| 编号 | 主题 | 论文数 |
|---|---|---|
| 01 | 宇宙线传播 | 6 |
| 02 | 宇宙线起源与 UHECR | 15 |
| 03 | 恒星核合成与元素丰度 | 17 |
| **合计** | | **38** |

新增主题域直接开 `NN_主题名/`（编号顺延），同时更新 `INDEX.md` 和本文档。

## 文献演化关系（学术谱系）

> 38 篇文献的内在演化脉络（奠基 → 继承 → 综述）。标号为文献库编号，**点击跳转对应 `00_overview.md`**；缩进表示谱系继承，`→` 表示思想/方法上的直接传承，`≍` 表示同一时期的平行/互补工作。

### 01 宇宙线传播（6 篇）

- **[0001_strong-2007](01_cosmic-ray-propagation/0001_strong-moskalenko-ptuskin-2007/literature_analysis/00_overview.md)** — 银河系 CR 传播与相互作用综述（**框架基石**）
  - 参数现代化：**[0005_genolini-2021](01_cosmic-ray-propagation/0005_genolini-2021/literature_analysis/00_overview.md)**（最小/中位/最大传播模型，DM 探测口径）
  - 放射性时钟方法线：**[0004_mewaldt-2001](01_cosmic-ray-propagation/0004_mewaldt-2001-clocks/literature_analysis/00_overview.md)**（Be-10/Al-26/Cl-36 时钟）→ **[0003_weinrich-2020](01_cosmic-ray-propagation/0003_weinrich-2020/literature_analysis/00_overview.md)**（AMS-02 数据约束晕大小）
  - 输运理论综述：**[0002_amato-blasi-2018](01_cosmic-ray-propagation/0002_amato-blasi-2018/literature_analysis/00_overview.md)** → 反馈动力学：**[0006_ruszkowski-2023](01_cosmic-ray-propagation/0006_ruszkowski-pfrommer-2023/literature_analysis/00_overview.md)**（星系/星系团 CR 反馈）

### 02 宇宙线起源与 UHECR（15 篇）

- DSA 奠基（1978 双璧）：
  - **[0008_bell-1978](02_cosmic-ray-origins/0008_bell-1978/literature_analysis/00_overview.md)**（平行激波加速）≍ **[0009_blandford-ostriker-1978](02_cosmic-ray-origins/0009_blandford-ostriker-1978/literature_analysis/00_overview.md)**（扩散激波加速）
    - 理论综述：**[0010_blandford-eichler-1987](02_cosmic-ray-origins/0010_blandford-eichler-1987/literature_analysis/00_overview.md)**
  - 现代综述与 SNR 应用：
    - **[0004_blasi-2013](02_cosmic-ray-origins/0004_blasi-2013/literature_analysis/00_overview.md)**（银河 CR 起源现代综述）→ **[0005_amato-2014](02_cosmic-ray-origins/0005_amato-2014/literature_analysis/00_overview.md)**（SNR 伽马射线）、**[0012_gabici-2019](02_cosmic-ray-origins/0012_gabici-2019/literature_analysis/00_overview.md)**（逃逸与宇宙线海）
      - 观测验证：**[0013_giuffrida-2022](02_cosmic-ray-origins/0013_giuffrida-2022/literature_analysis/00_overview.md)**（SN 1006 多波段）
- 能量/尺度判据与全景：
  - **[0011_hillas-1984](02_cosmic-ray-origins/0011_hillas-1984/literature_analysis/00_overview.md)**（Hillas 判据）→ 超 GZK 观测：**[0015_telescope-array-2023](02_cosmic-ray-origins/0015_telescope-array-2023/literature_analysis/00_overview.md)**
  - **[0006_grenier-2015](02_cosmic-ray-origins/0006_grenier-2015/literature_analysis/00_overview.md)**（银河系内 CR 九命全景综述）
  - **[0003_gaisser-1990](02_cosmic-ray-origins/0003_gaisser-1990/literature_analysis/00_overview.md)**（高能银河 CR 起源）
  - **[0007_biermann-1996](02_cosmic-ray-origins/0007_biermann-1996/literature_analysis/00_overview.md)**（星系尺度加速与元素丰度关联）
- UHECR 链：**[0001_bhattacharjee-sigl-2000](02_cosmic-ray-origins/0001_bhattacharjee-sigl-2000/literature_analysis/00_overview.md)**（极端能量 CR 综述）→ **[0014_alvesbatista-2019](02_cosmic-ray-origins/0014_alvesbatista-2019/literature_analysis/00_overview.md)**（开放问题）
  - 并行视角：**[0002_al-dargazelli-1996](02_cosmic-ray-origins/0002_al-dargazelli-1996/literature_analysis/00_overview.md)**（最高能 CR 起源）

### 03 恒星核合成与元素丰度（17 篇）

- **奠基**：**[0001_b2fh-1957](03_stellar-nucleosynthesis/0001_b2fh-1957/literature_analysis/00_overview.md)**（元素恒星合成）→ 综述：**[0002_trimble-1975](03_stellar-nucleosynthesis/0002_trimble-1975/literature_analysis/00_overview.md)** → **[0004_wallerstein-1997](03_stellar-nucleosynthesis/0004_wallerstein-1997/literature_analysis/00_overview.md)**（四十年进展）
- 太阳丰度表谱系：**[0014_cameron-1968](03_stellar-nucleosynthesis/0014_cameron-1968/literature_analysis/00_overview.md)** → **[0006_anders-grevesse](03_stellar-nucleosynthesis/0006_anders-grevesse/literature_analysis/00_overview.md)**（陨石+太阳）→ **[0007_grevesse-sauval-1998](03_stellar-nucleosynthesis/0007_grevesse-sauval-1998/literature_analysis/00_overview.md)**（标准太阳组成）→ **[0009_asplund-2009](03_stellar-nucleosynthesis/0009_asplund-2009-solar-composition/literature_analysis/00_overview.md)**（3D 模型）
  - 太阳系丰度与凝聚温度：**[0008_lodders-2003](03_stellar-nucleosynthesis/0008_lodders-2003/literature_analysis/00_overview.md)**
- 核反应与核天体物理：**[0005_champagne-wiescher-1992](03_stellar-nucleosynthesis/0005_champagne-wiescher-1992/literature_analysis/00_overview.md)**（爆炸氢燃烧）、**[0003_fowler-1984](03_stellar-nucleosynthesis/0003_fowler-1984/literature_analysis/00_overview.md)**（核天体物理）、**[0017_kaeppeler-2011](03_stellar-nucleosynthesis/0017_kaeppeler-2011/literature_analysis/00_overview.md)**（s 过程史）
- 恒星观测丰度：**[0010_gies-lambert-1992](03_stellar-nucleosynthesis/0010_gies-lambert-1992/literature_analysis/00_overview.md)**（B 型星 CNO）、**[0015_kraft-1994](03_stellar-nucleosynthesis/0015_kraft-1994/literature_analysis/00_overview.md)**（球状星团）、**[0011_kewley-2001](03_stellar-nucleosynthesis/0011_kewley-2001-starburst/literature_analysis/00_overview.md)**（星暴星系金属丰度）
- 恒星演化边界与宇宙学核合成：**[0012_dieterich-2014](03_stellar-nucleosynthesis/0012_dieterich-2014-h-burning-limit/literature_analysis/00_overview.md)**（氢燃烧极限）、**[0013_bertone-hooper-2018](03_stellar-nucleosynthesis/0013_bertone-hooper-2018/literature_analysis/00_overview.md)**（含 BBN 的暗物质史）
- 重元素现状：**[0016_cowan-2021](03_stellar-nucleosynthesis/0016_cowan-2021/literature_analysis/00_overview.md)**（r 过程现状）与 **[0017_kaeppeler-2011](03_stellar-nucleosynthesis/0017_kaeppeler-2011/literature_analysis/00_overview.md)**（s 过程）并列为重元素两条通道

## 产出流水线

每篇论文严格按以下顺序产出：

```
PDF 原文
  │
  ├──→ fulltext.txt（pdftotext/fitz 提取，38/38 已补齐含 OCR；.gitignore 忽略；跨设备靠 FreeFileSync 同步）
  │
  └──→ literature_analysis/
       00_overview.md            ← 文献元数据 + 结构树 + 篇间导航
       01_…NN_*.md                ← 分章精读（[FACT]/[INTERPRETATION]/[CRITIQUE] 三标签）
       97_quality_check.md      ← 完成度自查（gen_quality_check.py）
       98_vocabulary.md          ← A 学术逻辑词 + B 领域术语 + C 长难句
       99_final_summary.md       ← 一句话总结 + 核心结果 + 创新 + 局限 + 15 条记忆点
```

精读操作手册见 [`docs/READING_INSTRUCTIONS.md`](docs/READING_INSTRUCTIONS.md)。

## 新增文献接入 SOP（验证版）

按下面 9 步执行（Cameron 1968 / Kraft 1994 批次已走通完整流程）：

```bash
① 建目录   在合适主题域下新建 NNNN_作者-年份/（编号为主题域内下一个序号）
② 归档原文  PDF 放入目录；仓库内 PDF 用 `git add -f`（根目录 PDF 默认 .gitignore）
③ 提取文本  pdftotext <pdf> <篇>/fulltext.txt（文本型）；扫描型用 pdftoppm 转 PNG → OCR/视觉读取
④ 精读     按 READING_INSTRUCTIONS.md 30 节执行（§4：综述/长文献 → 路径 A 子节镜像；短篇 → 路径 B 八段）
            → literature_analysis/：00_overview → 分章 → 98_vocabulary → 99_final_summary
            → 篇间导航小节用 [``stem``](../../NN_作者-年份/literature_analysis/00_overview.md) 标准格式
⑤ 走 build 链（顺序关键，P0-6 防护）：
            python3 webapp/scripts/build_citations.py    # 篇间导航 → frontmatter citations
            python3 webapp/scripts/build_fm.py           # 写 frontmatter（自动清洗 [FACT] 等）
            python3 webapp/scripts/build_registry.py     # 生成 webapp/registry.json
⑥ 自动维护：
            python3 scripts/gen_index.py        # 38 篇 → INDEX.md
            python3 scripts/gen_quality_check.py # → 97_quality_check.md
            python3 scripts/gen_glossary.py      # → background/05_glossary.md
            （gen_glossary.py 已被 webapp/scripts/build_glossary.py 部分替代，后者直接生成 webapp/glossary.json）
⑦ webapp 重建：
            python3 webapp/scripts/build_webapp.py --include-papers    # papers 38（docs/TOC 以实际输出为准）
⑧ 审计：   python3 webapp/scripts/audit.py              # 18 条断言，失败非零退出
            headless 验证：/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --dump-dom ...
⑨ 提交     git add -f <新篇目录> + git commit
```

**V2.2 wikilink 化**（可选，让 Obsidian Graph 显示论文间连线）：
```bash
python3 webapp/patch_appendix_nav.py     # 97/98 补链（孤立节点）
python3 webapp/apply_wikilinks.py        # 导航头 + citations → [[wikilink]]（含编号对齐修复）
```

## 常用命令

```bash
# 进入工作区
cd /Users/jcxs2014/Sites/HermesLocal/papers

# 列出所有论文目录
ls 0?-*/  | grep "000[0-9]"

# 完整 build 链
python3 webapp/scripts/build_citations.py && \
python3 webapp/scripts/build_fm.py && \
python3 webapp/scripts/build_registry.py && \
python3 scripts/gen_index.py && \
python3 scripts/gen_quality_check.py && \
python3 webapp/scripts/build_webapp.py --include-papers && \
python3 webapp/scripts/audit.py

# 启动形态 B 服务层（端口 8747）
python3 webapp/scripts/server.py

# 检查 git 状态
git status
git log --oneline -10

# 提取 PDF 全文（fitz）
env -u PYTHONPATH python3 -c "import fitz; doc=fitz.open('XX.pdf'); print(doc[0].get_text())"
```

## webapp 工具链（12 脚本）

| 脚本 | 职责 | 调用顺序 |
|---|---|---|
| `build_citations.py` | **citations 唯一生成器**（篇间导航 → 库内引用） | 1 |
| `build_fm.py` | 写 frontmatter（剥 `[FACT]`/wikilink 透传/P0-6 防护） | 2 |
| `build_registry.py` | 读 45 frontmatter → `registry.json` | 3 |
| `build_glossary.py` | 769 术语解析 → `glossary.json` | 4 |
| `build_webapp.py` | 主构建（`--include-papers` 收论文） | 5 |
| `audit.py` | 18 条断言（label/年份/TOC/citations/图谱） | 6 |
| `build_pwa.py` | PWA 资源（manifest + 图标） | 7 |
| `apply_wikilinks.py` | V2.2 导航/citations → wikilink | 8 |
| `patch_appendix_nav.py` | V2.2 97/98 补链 | 8 前置 |
| `server.py` | 形态 B 进度 API | 独立 |
| `md2doc_html.py` | md → HTML 片段 | build_webapp 内部 |
| `build_search_index.py` | 全文搜索索引 | build_webapp 内部 |

**最小可重跑链**：`build_citations → build_fm → build_registry → build_webapp → audit`

**scripts/ 库级工具**（9 脚本）：`gen_index.py`（INDEX 生成）、`gen_quality_check.py`（97 生成）、`gen_glossary.py`（已被 build_glossary 替代）、`build_all.py`（全链路编排）、`quality_matrix.py`（质量矩阵 + 子节镜像统计）、`verify_claim.sh`（声称完成门禁）、`convert_unicode_math.py` / `convert_supsub.py` / `fix_math_fragmentation.py`（公式 Unicode → LaTeX / 上下标 → LaTeX / 割裂修复，文献内容处理）

## 元数据勘误记录（13 处）

原始 PDF 文件名含误导性作者名；以下论文目录名已修正为**实际第一作者-年份**（详见 `docs/ENHANCEMENTS.md` §A）：

| 原目录名 | 实际作者 | 年份 |
|---|---|---|
| `0001_sievers-2007` | Strong, Moskalenko & Ptuskin | 2007 |
| `0001_longair-ptuskin-1999` | Bhattacharjee & Sigl | 2000 |
| `0003_high-energy-galactic-1990` | Gaisser | 1990 |
| `0004_aharonian-2013` | Blasi | 2013 |
| `0005_padovani-protheroe-2013` | Blasi 2013 + Amato 2014 | 双论文 |
| `0006_thackeray-2016` | Grenier, Black & Strong | 2015 |
| `0007_moskalenko-1996` | Biermann | 1996 |
| `0002_burbidge-1975` | Trimble | 1975 |
| `0003_caughlan-fowler-1988` | Fowler | 1984（Nobel Lecture）|
| `0004_woosley-1997` | Wallerstein et al. | 1997 |
| `0005_explosive-h-burning-1992` | Champagne & Wiescher | 1992 |
| `0010_gomez-1992-cno-b-stars` | Gies & Lambert | 1992 |
| `0013_weinberg-2018-dark-matter` | Bertone & Hooper | 2018 |

## 关键文档索引

| 文档 | 用途 |
|---|---|
| [`docs/READING_INSTRUCTIONS.md`](docs/READING_INSTRUCTIONS.md) | 精读操作手册（30 节规范 + 数据一致性经验） |
| [`INDEX.md`](INDEX.md) | 38 篇论文分析入口（自动生成） |
| [`docs/REVIEWS.md`](docs/REVIEWS.md) | 审查记录（#1–#30：批次核验/回归修复/复验方法论） |
| [`docs/精读深度扩充设计备忘.md`](docs/精读深度扩充设计备忘.md) | 精读深度扩充设计决策源（路径 A/B/批次/97 块） |
| [`docs/RECOMMENDATIONS.md`](docs/RECOMMENDATIONS.md) | 改进建议路线图（22 条） |
| [`docs/ADVANCEMENT.md`](docs/ADVANCEMENT.md) | 进阶方案 v2.1 + V2.2 补丁（已全部落地） |
| [`docs/WEBAPP_DESIGN.md`](docs/WEBAPP_DESIGN.md) | Webapp 架构与实现细节 |
| [`docs/ENHANCEMENTS.md`](docs/ENHANCEMENTS.md) | 改进建议清单（9 条全部 ✅ 完成） |
| [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) | 故障排除与修复记录（A1–A6 + B1–B18 + C/D/E/F + SOP） |
| [`docs/合规审查报告.md`](docs/合规审查报告.md) | 全库合规审查 + WorkBuddy 批注（翻译段/路径 B/97 块判定修正） |
| [`docs/执行指令模板.md`](docs/执行指令模板.md) | 批量任务执行指令通用模板（铁律/复验口径/归档约定） |
| [`docs/子节镜像示例-ruszkowski-02.md`](docs/子节镜像示例-ruszkowski-02.md) | 路径 A 子节镜像规范模板示例 |
| [`docs/archive/`](docs/archive/) | 14 份闭环执行指令归档（含 audit/ 审计明细，索引见 `docs/archive/README.md`） |
| [`background/`](background/) | 7 篇跨篇主题知识库 |

## 已完成 / 进行中

- ✅ 批 1（frontmatter + registry）
- ✅ 批 2（audit + 形态 B 服务层）
- ✅ 批 3（术语 hover + O2 图谱，61 边）
- ✅ 批 4（PWA + 阶段六争议演化）
- ✅ V2.2 补丁（Obsidian 图谱链接化）
- ✅ 库扩至 38 篇（全部精读闭环，REVIEWS #23）
- ✅ fulltext.txt 全库补齐（38/38，含 2 篇扫描型 OCR）
- ✅ pages 字段全量补齐（38/38 整篇粒度）+ frontmatter YAML 修复
- ✅ 公式 Unicode/上下标 → LaTeX 规范化（全库四域）
- ✅ 精读深度扩充备忘定稿（路径 A/B 选择规则，见 READING_INSTRUCTIONS §4）
- ✅ 子节镜像批 1 + 批 2（4 篇长综述 30 分章 + 20 篇长文献，路径 A 改造，REVIEWS #25/#26）
- ✅ 议题 3（quality_matrix 子节镜像统计 + 97 子节级覆盖块，覆盖率 100%）
- ✅ docs 整理（一次性执行指令 13 份归档至 `docs/archive/`，通用模板见 `docs/执行指令模板.md`）

后续路线见 [`docs/ADVANCEMENT.md`](docs/ADVANCEMENT.md)。

---

> 最后更新: 2026-08-15
