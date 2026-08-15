# pages 补齐回归修复执行指令（frontmatter 分隔符）

> 生成：2026-08-15（WorkBuddy 主会话）｜执行：指定会话（本文件自包含）
> 背景：`1ad9840`（pages 补齐，38/38 覆盖）执行时**误删了 frontmatter 首尾 `---` 分隔符**——WorkBuddy 审查复验发现 P0 回归
> 影响：37/38 篇 00_overview 开头 `---` 缺失、部分篇结尾 `---` 也缺失 → YAML frontmatter 结构破坏（Obsidian 属性 / registry / webapp 构建全部失效）
> **pages 值本身全部正确**（Crossref 明细核对无误）——本次只补分隔符，**不动任何其他内容**

---

## 0. 现状（2026-08-15 实测）

| 类别 | 数量 | 说明 |
|---|---|---|
| 完好 | **1 篇** | `0008_bell-1978`（未被 1ad9840 触碰）——**不要动** |
| 缺开头 + 缺结尾 `---` | **37 篇** | 首行直接是 `title:` 等字段；frontmatter 结束处（正文标题前）也无 `---`（注意：正文里可能有 `---` 水平分隔线，**不是** frontmatter 结束符） |

**判定方法（每篇必须同时满足）**：
1. 第一行是 `---`
2. frontmatter 结束处（正文第一行之前）有一个 `---`

## ⚠️ 铁律

1. **只补分隔符**：每篇仅可能插入 2 行以内的 `---`；**不得**修改 pages 值、其他字段、正文。修完 `git diff` 应只含 `---` 行增删。
2. **绝不叠加**：补之前先检查目标位置是否已有 `---`；已有则跳过。**`---` 是结构行，不是正文，绝不能把补进去的 `---` 当成正文第一行再补一次**（上一轮修复脚本即因此产生双 `---`，已回滚）。
3. **不动 bell-1978**。
4. 每篇修完自查 3 项（见 §2 验证），全部通过才算该篇完成。

## 1. 修复算法（推荐直接跑下方脚本，勿手改）

**frontmatter 内容行定义**（判定"正文第一行"用）：
- `key: value` 行（如 `title: xxx`、`path: xxx`）
- 缩进续行（如 abstract 多行字符串、citations 列表项 ` - '[[...]]'`）
- 空行
- **`---` 行**（结构行，既不是 frontmatter 内容也不是正文）

**正文第一行** = 第一个不满足上述条件的行（特征：`# 00.`、`## 基本信息`、`> 状态：`、`| 字段 |` 等开头）。

修复动作：
1. 若第一行不是 `---` → 文件头部插入 `---\n`
2. 定位正文第一行位置；若它**前面没有任何 `---` 行** → 在正文第一行前插入 `---\n`
3. 若正文第一行前已有 `---` → 不动（防叠加）

**可执行脚本**（python3 运行，修改前会 dry-run 打印计划；脚本不做 git 操作）：

```python
#!/usr/bin/env python3
"""修复 1ad9840 误删的 frontmatter 分隔符（37 篇，bell 跳过）"""
import glob, re, sys

SKIP = {"0008_bell-1978"}

def is_fm_line(s):
    """True=frontmatter 内容行或结构行(可跳过)；False=正文行"""
    if s.strip() in ('', '---'): return True     # 空行与 --- 结构行都跳过
    if s.startswith(' '): return True            # 缩进续行
    if s.startswith('- '): return True           # 列表项（含顶格 `- '[[...]]'`）
    if re.match(r'^[A-Za-z_][A-Za-z0-9_]*\s*:', s): return True  # key:
    return False

def fix(f):
    lines = open(f, encoding='utf-8').read().splitlines()
    acts = []
    if not lines or lines[0].strip() != '---':
        lines.insert(0, '---'); acts.append('开头')
    # 正文第一行 = 第一个非 frontmatter 内容行（--- 算正文侧）
    body = next((i for i, l in enumerate(lines) if not is_fm_line(l)), len(lines))
    if not any(l.strip() == '---' for l in lines[:body]):
        lines.insert(body, '---'); acts.append(f'结尾@L{body+1}')
    open(f, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    return acts

if '--dry-run' in sys.argv:
    for f in sorted(glob.glob('0*/**/00_overview.md', recursive=True)):
        if 'backup' in f or '.git' in f or any(s in f for s in SKIP): continue
        lines = open(f, encoding='utf-8').read().splitlines()
        need = []
        if not lines or lines[0].strip() != '---': need.append('补开头')
        body = next((i for i, l in enumerate(lines) if not is_fm_line(l)), len(lines))
        if not any(l.strip() == '---' for l in lines[:body]): need.append('补结尾')
        if need: print(f"❌ {f}: {','.join(need)}")
    print('dry-run 完毕（未修改）')
else:
    for f in sorted(glob.glob('0*/**/00_overview.md', recursive=True)):
        if 'backup' in f or '.git' in f or any(s in f for s in SKIP): continue
        acts = fix(f)
        print(('✅' if not acts else '🔧'), f, acts or '未动')
```

注意：`glob('0*/**/00_overview.md')` 会命中 `backup/`，脚本已排除；跑之前先 `--dry-run` 确认清单为 37 篇。

## 2. 验证（对照原文铁律）

每篇修完自查：

```bash
# 1) 第一行是 ---
head -1 <篇>/literature_analysis/00_overview.md          # 必须输出 ---
# 2) frontmatter 结束 --- 在正文标题之前
awk 'NR<=60 && /^---$/{print NR": ---"}' <篇>/literature_analysis/00_overview.md | head -2
#    第二个 --- 必须出现在 '# 00.' 标题行号之前
# 3) pages 仍在
grep '^pages:' <篇>/literature_analysis/00_overview.md
```

全库复验（执行侧自查）：

```bash
# 缺开头的应为 0
for f in $(find . -name 00_overview.md -not -path './backup/*'); do head -1 "$f" | grep -q '^---$' || echo "缺开头: $f"; done
# frontmatter 结尾缺失的应为 0（正文标题行号前无 --- 即缺失）
```

**提交前 `git diff` 核对**：所有改动应只是 `---` 行的增删；`pages:` 值一行不差。

## 3. 提交约定

- **单笔提交**：`git add` 仅 37 个 `00_overview.md`（精确路径，可用 `git status --short | grep 00_overview` 核对清单），**不得 `git add -A`**
- commit message：`fix(papers): 修复 1ad9840 误删的 37 篇 00_overview frontmatter 首尾 --- 分隔符`
- 提交后工作树应只剩 `docs/精读深度扩充设计备忘.md`（untracked，勿动）

## 4. 完成标准（WorkBuddy 复验口径）

1. 38/38 篇 `head -1` == `---` ✓
2. 每篇正文第一行前有 `---`（frontmatter 闭合）✓
3. `pages:` 值全部不变（与 1ad9840 一致）✓
4. 提交 diff 仅含 `---` 行增删 ✓
5. 工作树干净（仅 untracked 备忘）✓
