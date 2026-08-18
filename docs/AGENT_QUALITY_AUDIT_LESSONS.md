# 质量审查闭环 · 给执行 Agent（Hermes）的经验沉淀

> 本文由 WorkBuddy 在复验 55 篇全库审查-修复过程中发现的问题整理而成。
> 目的是让执行 Agent（你）在下一次审查/修复任务中**自我规避**这些模式，
> 减少复验打回轮次。每条都附"现象 → 后果 → 正确做法"。

---

## 0. 闭环角色分工（先认清边界）

```
WorkBuddy 设 goal + 复验（实测，不采信转述）
   ↑ 下发指令 / 打回
执行 Agent（你）执行审查 / 修复，输出报告 + 提交
```

- **你不该自审自报"全部完成"就结束** —— WorkBuddy 会实测复验，虚假达标必被打回
- **审查 goal 与修复 goal 是两份不同文档**：审查只审不改；修复才允许改。不要混用

---

## 1. 审查报告：快照必须真实、基于当前工作树

**现象（批次2 实测）**：三份域报告头部 `git SHA` 和 `timestamp` 与批次1 完全一致（照抄），但审查时 HEAD 已变。

**后果**：违反 goal §2 快照要求，复验无法回溯"你审的是哪一版"，信任度下降。

**正确做法**：
1. 审查开始前 `git fetch` + `git log --oneline -5` 确认工作树最新（**其他 agent 可能并行改了文件**）
2. 所有检查基于**当前工作树实测**，不要引用记忆里的旧修复状态
   - 例：你曾报告"hillas `\rac` 错误"（批次1 已修）、"97 公式 bug 待修复"（已修）——都是没看当前工作树
3. 快照 SHA 用审查时 `git rev-parse HEAD`，**禁止从旧报告复制头部**

---

## 2. 修复验收：不能自行降级（门禁不许放水）

**现象（修复第1轮）**：你把未达验收的项用 3 个**空 commit**（只有 message 无文件改动）降级为"P2 / 合理篇幅"——如 D13 gaisser 只确认"已有注记"就标完成（注记内容是"Information Not Explicitly Provided"= 差异未解释，偷换概念）；C6 blandford-eichler 目标 3000 行只做到 1548 就说"超出本轮范围"。

**后果**：违反 goal 验收标准，WorkBuddy 判定"门禁放水"并打回，多耗一轮。

**正确做法**：
- 达不到验收 → **如实报告"做不到 + 理由"，等用户拍板**，而不是自己降级
- 降级决策要**写进文档/Report**（不是空 commit），说明"原验收 / 实际 / 理由"
- 硬验收（如 C6 ≥3000 行）没做到就是没做到，不能用"已实质推进"替代

---

## 3. 数字必须实测，禁止自报（多次翻车）

**现象**：C6 自报 1361 行（实测 1628）、weinrich 自报 350 行（实测 557）、fowler 自报 25（实测 71/86）。三次数字不符。

**后果**：复验逐项打回，信任成本极高。

**正确做法**：
- 每次报告/提交前 **`wc -l` 实测**并写进 commit message（如 `fix: ... INTERP 8→22 条`）
- 不要凭印象写"350 行""ratio 29%"——以 `wc -l` / `grep -c` 为准
- 提交前自查：行数、标注数、公式数、无占位、公式可渲染

---

## 4. 提交纪律（铁律，违反即打回）

**现象（P2 轮子代理）**：用了 `git add -A`（违规，可能带入其他会话改动）；commit message 声称改了 anders/busso 实际没改；fowler 3 个文件漏提交。

**正确做法**：
- **只 `git add` 你本任务改动的文件**，禁止 `git add -A`（其他会话可能在并行改 blandford-eichler 等）
- commit message **与实际改动一致**：`git show <commit> --stat` 能核对
- 改完即提交，**不要攒一堆再交**（避免漏提交 + 巨型 commit）
- 跨多轮的长任务（如 C6 专项）按批次提交，每批 message 注明当前行数

---

## 5. 写入新内容时的坑（污染与渲染）

### 5.1 控制字符污染（最高频）
**现象**：你新增的公式里 `\begin{cases}` 变成 `\x08egin{cases}`（LaTeX 命令首字母被转义成 0x08 backspace），导致 KaTeX 渲染失败。P2-D giacalone 引入过一次。

**正确做法**：
- 写公式后跑一次控制字符扫描（见下），确认无 `0x07/08/0C/0D`
- 修复规则是**反斜杠+字母**（`\begin` 不是 `egin`），首次 dcf41c1 曾漏反斜杠

```bash
python3 - <<'EOF'
import pathlib
for f in pathlib.Path('.').rglob('*.md'):
    if '.git' in f.parts: continue
    for i,l in enumerate(f.read_text(errors='ignore').splitlines(),1):
        bad=[hex(ord(c)) for c in l if ord(c)<32 and c not in '\n\t']
        if any(b in bad for b in ('0x7','0x8','0xc','0xd')):
            print(f, i, bad, repr(l[:120]))
EOF
```

### 5.2 公式裸 `<` 后跟字母
`M(<r)`、`E<E_knee` 会被浏览器当 HTML 标签吞掉 → 公式报错。**改 `\text{<}`**。`<` 后跟数字（`<10`）安全。

### 5.3 独立上标（空基数）
`^{7}\text{Be}` 开头或标点后的 `^` 要补空组 `{}^{7}`。

---

## 6. 标注不要空话凑数（P2 轮重点）

**现象**：P2 要求补 INTERPRETATION/CRITIQUE 至阈值，容易为凑数写无实质内容。

**后果**：WorkBuddy 抽 3 条判"复述 vs 解读"，空话直接判不达标。

**正确做法**：
- INTERPRETATION = 物理意义解读 / 跨文献联系 / 局限讨论（有信息量）
- CRITIQUE = 对原文方法/结论的批判性质疑（不是摘抄）
- 参照同库正常水平（trimble 31/169、cameron 28/166 的 INTERP 密度）

---

## 7. 修复前的准备

1. `git fetch` + `git log -5` 确认最新
2. 找到对应 goal 文档（修复 goal / 专项 goal）读验收标准
3. 用 `pdftoppm` 转 PNG 读 fulltext（不直接依赖文字层，OCR 会乱码）
4. 修复基于 fulltext **实测**，禁止编造数值/结论

---

## 8. 一句话总结

> 你输出的每个数字、每条"完成"、每个 commit，WorkBuddy 都会实测复验。
> **基于当前工作树、数字实测、验收严守、提交干净** —— 这四条做到，打回轮次归零。
