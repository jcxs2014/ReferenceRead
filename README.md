# papers — 文献阅读与分析工作区

> 21 篇文献（23 篇分析目录，含两篇双论文并列）、205 个分析文件、3 篇主题背景知识库。
>
> 按主题域 → 单篇论文 → `literature_analysis/` 三层结构组织。每篇文献按 `READING_INSTRUCTIONS.md` 的 28 节规范精读。
- `TROUBLESHOOTING.md` — 故障排除与修复记录（按工作流分类：精读/构建/数据一致性/工具）

## 目录结构

```
papers/
├── README.md                       ← 本文档：工作区总览与接入 SOP
├── READING_INSTRUCTIONS.md         ← 精读操作手册（28 节规范）
├── INDEX.md                        ← 21 篇论文分析入口（含目录、概览、总结）
├── ENHANCEMENTS.md                 ← 改进建议清单（P0/P1/P2）
├── GIT_CONVENTION.md               ← Git 提交规范（来自 HermesLocal 根）
│
├── 01_cosmic-ray-propagation/      ← 宇宙线传播主题
│   └── NNNN_作者-年份/
│       ├── *.pdf                   ← 原文（被 .gitignore 忽略）
│       └── literature_analysis/    ← 精读产出
│           ├── 00_overview.md
│           ├── 01_…NN_*.md          ← 正文分章
│           ├── 98_vocabulary.md    ← 词汇表（A 逻辑词 + B 术语 + C 长难句）
│           └── 99_final_summary.md
│
├── 02_cosmic-ray-origins/          ← 宇宙线起源主题
├── 03_stellar-nucleosynthesis/     ← 恒星核合成与元素丰度主题
│
├── background/                     ← 跨篇主题知识体系（库级）
│   ├── README.md
│   ├── 01_cosmic_rays.md           ← 宇宙线物理（传播、加速、UHECR、CR-ISM）
│   ├── 02_nucleosynthesis.md       ← 恒星核合成（八大过程、BBN、爆炸性燃烧）
│   └── 03_astrophysics.md          ← 太阳丰度与天体物理（太阳组成、恒星、暗物质）
│
└── scripts/                        ← 自动化脚本（详见 P2-8）
    └── gen_index.py                ← 从目录结构自动生成 INDEX.md
```

## 主题域

| 编号 | 主题 | 论文数 |
|---|---|---|
| 01 | 宇宙线传播 | 1 |
| 02 | 宇宙线起源 | 7 |
| 03 | 恒星核合成与元素丰度 | 13 |
| **合计** | | **21** |

新增主题域直接开 `NN_主题名/`（编号顺延），同时更新 `INDEX.md` 和本文档。

## 产出流水线

每篇论文严格按以下顺序产出：

```
PDF 原文
  │
  ├──→ fulltext.txt / extracted.json（fitz 提取；.gitignore 忽略；跨设备靠 FreeFileSync 同步）
  │
  └──→ literature_analysis/
       00_overview.md            ← 文献元数据 + 结构树 + 关键术语
       01_…NN_*.md                ← 分章精读（[FACT]/[INTERPRETATION]/[CRITIQUE] 三标签）
       98_vocabulary.md          ← A 学术逻辑词 + B 领域术语 + C 长难句
       99_final_summary.md       ← 一句话总结 + 核心结果 + 创新 + 局限 + 15 条记忆点
```

精读操作手册见 [`READING_INSTRUCTIONS.md`](READING_INSTRUCTIONS.md)。

## 新增文献接入 SOP

按下面 7 步执行；新增主题域需同步更新本文档与 `INDEX.md`。

```
① 建目录   在合适主题域下新建 NNNN_作者-年份/（编号为主题域内下一个序号）
② 放原文   论文 PDF 放入目录；命名沿用现有风格（作者-简短标题+编号.pdf）
③ 提取文本 用 fitz 脚本提取 → fulltext.txt / extracted/*.json（.gitignore 忽略，
            依赖 FreeFileSync 跨设备同步；扫描版 PDF 用 pdftoppm 转 PNG → vision_analyze）
④ 精读     按 READING_INSTRUCTIONS.md 28 节执行
            → literature_analysis/：00_overview → 分章 → 98_vocabulary → 99_final_summary
⑤ 挂接     在 00_overview.md 标注「前序阅读/关联论文」（见 P0-3 篇间导航）
            判断是否汇入 background/ 对应主题文档
⑥ 更新索引 跑 scripts/gen_index.py 自动生成 INDEX.md（或手动更新）
            若开新主题域，同步更新本文档与 INDEX.md
⑦ 提交同步 git commit + FreeFileSync 双向同步
```

## 常用命令

```bash
# 进入工作区
cd /Users/jcxs2014/Sites/HermesLocal/papers

# 列出所有论文目录
ls 0?-*/  | grep "000[0-9]"

# 生成 INDEX.md
python3 scripts/gen_index.py

# 查看主题背景知识
ls background/

# 检查 git 状态
git status
git log --oneline -10
```

## 元数据勘误记录（13 处）

原始 PDF 文件名含误导性作者名；以下论文目录名已修正为**实际第一作者-年份**，详见 `ENHANCEMENTS.md` §A 与各篇 `00_overview.md` 元数据：

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

- **精读操作手册**：[`READING_INSTRUCTIONS.md`](READING_INSTRUCTIONS.md)（28 节规范）
- **论文分析入口**：[`INDEX.md`](INDEX.md)（21 篇概览 + 总结）
- **改进建议清单**：[`ENHANCEMENTS.md`](ENHANCEMENTS.md)（P0/P1/P2 待办）
- **主题知识体系**：[`background/`](background/)（3 篇跨篇综述）

---

> 最后更新: 2026-08-13
