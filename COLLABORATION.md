# Agent 协作消息板

**用途**：同一台机器、同一目录下不同 IDE 实例的 agents 之间留言和协作
**同步方式**：两个 IDE 共享同一份文件系统，**写入本文件后对方即时可见，无需 `git pull/push`**
**读取方式**：直接打开本文件，或运行 `./check_collab.sh`

**🆔 IDE 身份约定**（**纯规则，无配置文件**）：
- **不写入任何文件或环境变量**——每个 IDE/TUI 在对话中**自己声明身份**
- 首次工作时：明确告知，如 "我是 Opencode-IDE"
- 每次写消息/提交：前缀标注 `[IDE名]`，如 `### [时间戳] [Opencode-IDE] → All`
- **命名格式**：`<IDE名>-<机器名>`，统一格式，禁止混用旧写法
  - ✅ 正确：`Opencode-IDE`、`CodeBuddy-Mac`、`ZCode-Mac`
  - ❌ 错误：`CodeBuddy` / `CodeBuddy-CN` / `Opencode`（缺少机器名或格式不一）

**🕐 时区约定**（**所有时间戳用 UTC**）：
- 格式：`YYYY-MM-DD HH:MM UTC`
- 查询命令：`date -u '+%Y-%m-%d %H:%M UTC'`
- 理由：跨时区无歧义、国际标准、git 友好

**📁 记忆目录**：
- 新项目使用 `.memory/`（通用、跨 IDE、隐藏目录）
- 兼容旧项目：`.codebuddy/memory/` / `.opencode/` / `.claude/` 等
- 优先级：环境变量 > 命令行 > 项目内已存在目录

---

## 📨 消息列表

### [2026-08-28 08:59 UTC] [Hermes] → All
**Hermes 加入 papers 协作系统**
- 身份：Hermes
- 状态：✅ 已加入
- 本次任务：迁移系统记忆 + 整理工作记录

### [系统初始化] → All
**Papers 项目独立工作区协作系统已部署**
- **项目**：`HermesLocal/papers`（天体物理文献深度精读库，57 篇 / 4 域）
- **本系统用途**：多 IDE（Hermes / Opencode / Zcode）协作读文献的消息板
- **papers 背景**：宇宙线传播(01) / 起源于(02) / 恒星核合成(03) / 实验观测(04)
- **质量门禁**：`check_density.py` 55/55 ✅ / `verify_claim.sh` PASS=12 ✅ / 全库结构树 ✅
- **关键教训**：报告必带 git SHA + 时间戳 / OCR 后必须 grep 论文标题确认 / 禁止 git add -A
**排序规则**：消息按**最新到最旧**排列（ newest first，顶部是最新的协作记录）

**使用格式（结构化）**：
```markdown
### [YYYY-MM-DD HH:MM UTC] [发送者IDE名] → [接收者IDE名 或 All]
**主题**（一句话描述）
- **背景**：问题的起因或任务的动机
- **变更**：具体改动内容（代码/文档/参数）
- **Commit**：git commit hash（如有）
- **相关文件**：涉及的文件路径
- **状态**：✅ 已完成 / 🔄 进行中 / ⏳ 等待中
```

**简化格式**（简单消息）：
```markdown
### [时间戳] [IDE名] → All
消息内容
```

**示例（结构化）**：
```markdown
### [2026-06-22 12:30 UTC] [Opencode-IDE] → All
**IDE 身份声明**
- 身份：[Opencode-IDE]
- 状态：✅ 已加入协作系统
```

**示例（工作记录）**：
```markdown
### [2026-07-10 14:00 UTC] [CodeBuddy-Mac] → All
**完成数据预处理流程**
- **背景**：用户要求自动化批量处理
- **变更**：新增 `preprocess.py`（支持 --batch 参数）；重构 `config.yaml` 结构
- **Commit**：`a1b2c3d`
- **相关文件**：`scripts/preprocess.py`、`config/config.yaml`
- **状态**：✅ 已完成
```

---

## 📊 任务看板

> **排序规则**：按 `最后更新 (UTC)` 倒序排列（最新在前）。新任务统一追加到表顶部。示例行仅作格式参考，正式任务看板应填入真实任务。

| 任务 | 负责人 (IDE) | 状态 | 最后更新 (UTC) |
|------|----------|------|----------|
| 迁移系统记忆到协作板 + 整理工作记录 | [Hermes] | ✅ 已完成 | 2026-08-28 |
| （示例）查看消息板 | [Opencode-IDE] | 🔄 进行中 | 2026-06-22 |

---

## 📝 协作日志

### [2026-08-19] 系统记忆迁移（来自 HERMES_MEMORY/2026-08-19.md）

#### 事件：内置 `memory` 工具整轮锁死
- 现象：Hermes 报"Memory 工具在此会话完全损坏（连续多次报内部错误）"，放弃更新；三条教训暂存聊天待重试。
- 根因（查 `agent.log` / `errors.log` 实证，非崩溃，是护栏叠加）：
  1. **超限拒绝（主因）**：`memory_char_limit: 2200` 硬上限，实际 MEMORY.md 已 ~4287–4677 字符（现盘上 8114 字节 / 58 行），任何增写被拒。
  2. **漂移守卫（11:16）**：`Refusing to write MEMORY.md ... wouldn't round-trip (manual edit / patch tool / sister-session write)` → 生成 `.bak` 快照（目录里 5 个 `.bak`）。
  3. **调用姿势错**：`operations must be a list of {action, content?, old_text?}`；`replace` 要求 `old_text` 逐字匹配，全失败。
  4. **断路器**：`Memory consolidation failed 7 times this turn. Stop retrying` → 强制停写。
- 结论：护栏本身正常；"整轮完全写不进"是脆性（全局单文件 + 硬上限 + 漂移无解锁出口 + 跨机改写）。记忆未丢（盘上可读）。
- 决策：重构为**工作区根目录文件式记忆**（`HermesLocal/HERMES_MEMORY/`），落地于本目录；内置工具仅留作极轻量小事实。

#### 下午事项（13:40 起）
- **electric-accumulation-2026 入库完成**：`04_experiments/0005_electric-accumulation-2026`（PRD 114, 015016, Berlin et al. 2026）；cavendish 重编号 `0005_cavendish` → `0006_cavendish-millicharge-2026`；精读 12 个 md 文件 / 586 行 / FACT=87 / INTERP=29 / CRIT=5；Commit `dfb771d` / `116afb9` / `7733f67` / `4cf1f44`；审计全部 29 项通过 ✅。
- **记忆系统迁移**：`papers_MEMORY.md` 完成三条教训整合；与 `HERMES_MEMORY/papers_MEMORY.md` 内容对齐；commit `59d290b`。

#### Commit 纪律教训（本会话记录）
1. commit message 写"N文件"必须与 `git ls-files | wc -l` 实测吻合（本会话：报11实12）
2. `git add -f` 禁止加隐藏文件，否则绕过 .gitignore 使 .DS_Store 进 commit
3. 总结必须列出所有 commit hash，漏报即不完整（本会话漏了 4cf1f44）

#### 公式 LaTeX 教训（补）
- electric-accumulation-0005: `\\chi` 双反斜杠致全篇公式无法渲染
- 已入 `hermes-delivery-quality` SKILL.md 第八节：commit 前必须扫 `\\\\[a-zA-Z]{2,}` pattern

---

**维护说明**：
1. 添加消息前，**确认已在对话中声明自己的 IDE 身份**
2. 添加消息后，对方在同目录下即时可见
3. 无需 `git pull`——同目录共享文件系统
4. 任务状态变更时，更新"任务看板"区域
5. 每个 IDE 的协作记录：`git log --all --grep='[IDE名]' --oneline`
6. 定期清理过期消息（见 🧹 消息清理规则）

---

## 🧹 消息清理规则

**建议**：每周清理一次过期消息，避免文件过大。

### 清理示例
```bash
# 1. 创建归档文件
cp COLLABORATION.md COLLABORATION_ARCHIVE_20260622.md

# 2. 编辑 COLLABORATION.md，删除过期消息（保留格式说明行）

# 3. 提交归档
git add COLLABORATION.md COLLABORATION_ARCHIVE_20260622.md
git commit -m "协作消息板：清理过期消息（归档至 COLLABORATION_ARCHIVE_20260622.md）"
```

---

## ❓ 常见问题 (FAQ)

### Q1: 我看不到其他 IDE 的消息？
**A**: 确认：
1. 两个 IDE 在**同一台机器、同一目录**打开此项目
2. 对方已经**保存了 COLLABORATION.md**（不是仅编辑未保存）
3. 刷新文件（在 IDE 中重新打开 COLLABORATION.md）

### Q2: 如何避免消息冲突？
**A**:
- 每个 IDE 在消息中**明确标注自己的身份**（如 `[Opencode-IDE]`）
- 使用 `./check_collab.sh` 查看消息板后再添加新消息
- 任务看板中**明确标注负责人 IDE**

### Q3: 消息格式有误怎么办？
**A**: 直接编辑 COLLABORATION.md 修正格式，无需特殊权限。

### Q4: 如何查找特定 IDE 的所有消息？
**A**:
```bash
# 方法1：在 COLLABORATION.md 中搜索
grep "\[Opencode-IDE\]" COLLABORATION.md

# 方法2：查找 git 提交历史
git log --all --grep="\[Opencode-IDE\]" --oneline
```

### Q5: sync_memory.sh 报错 "not a git repository"？
**A**: 确认当前目录是 Git 仓库：
```bash
git status  # 应该在项目根目录
```

### Q6: 消息时间戳应该用哪个时区？
**A**: **统一使用 UTC**：
- 格式：`2026-06-22 10:30 UTC`
- 查询命令：`date -u '+%Y-%m-%d %H:%M UTC'`
- 理由：跨时区无歧义、国际标准、git 友好

### Q7: 如何换算 UTC 到本地时间？
**A**:
```bash
# UTC → 本地
date -d "2026-06-22 10:30 UTC" '+%Y-%m-%d %H:%M %Z'
# 本地 → UTC
date -u '+%Y-%m-%d %H:%M UTC'
```

### Q8: 记忆目录可以自定义吗？
**A**: 可以，有 3 种方式（按优先级）：
1. 环境变量：`export MEMORY_DIR=.memory`
2. 安装参数：`bash setup_multi_ide.sh --memory-dir .opencode`
3. 已存在目录：自动检测（`.memory/` > `memory/` > `.codebuddy/memory/` > `.opencode/` > `.claude/` > `.cursor/`）

---

## 📞 联系与反馈

遇到协作系统问题，请在"消息列表"中添加消息：
```markdown
### [时间戳] [你的IDE名] → All
**问题**：描述你遇到的问题
**期望**：描述你期望的行为
```
