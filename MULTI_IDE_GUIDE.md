# 多 IDE 协作系统 - 实施指南

> **用途**：将本项目的多 IDE 协作系统部署到任意其他项目
> **适用场景**：同一台机器、同一项目目录下，多个 IDE/TUI 实例协作
> **版本**：2026-07-10 (v2.1)

---

## 📋 目录

1. [快速开始](#快速开始-5-分钟)
2. [核心设计理念](#核心设计理念)
3. [文件清单](#文件清单)
4. [详细部署步骤](#详细部署步骤)
5. [使用规范](#使用规范)
6. [消息格式规范](#消息格式规范)
7. [时区约定](#时区约定)
8. [常见问题](#常见问题)
9. [自定义与扩展](#自定义与扩展)
10. [版本历史](#版本历史)

---

## 🚀 快速开始（5 分钟）

### 方式 A：一键脚本（推荐）

```bash
# 1. 进入目标项目目录
cd /path/to/your-project

# 2. 运行安装脚本（从本项目复制）
bash /path/to/multi-ide-template/setup_multi_ide.sh

# 3. 验证安装
./check_collab.sh
```

### 方式 B：手动复制

```bash
# 1. 进入目标项目目录
cd /path/to/your-project

# 2. 复制 4 个文件
cp /path/to/multi-ide-template/COLLABORATION.md .
cp /path/to/multi-ide-template/sync_memory.sh .
cp /path/to/multi-ide-template/check_collab.sh .
cp /path/to/multi-ide-template/AGENTS.md .codebuddy/memory/  # 或你的 agent 配置目录

# 3. 添加可执行权限
chmod +x sync_memory.sh check_collab.sh
```

### 方式 C：仅添加规则（最轻量）

如果你的项目已有自己的协作机制，只想添加规则：

```bash
# 复制规则文档到你的 agent 配置目录
cp /path/to/multi-ide-template/AGENTS.md /your/agent/config/
```

---

## 💡 核心设计理念

### 🎯 3 大原则

| 原则 | 说明 | 反对方案 |
|------|------|----------|
| **零基础设施** | 无配置文件、无环境变量、无自动检测 | ❌ `.ide_id` / ❌ `IDE_ID` env / ❌ 进程树爬虫 |
| **共享即同步** | 同一文件系统 = 自动同步 | ❌ git pull/push / ❌ 远程消息队列 |
| **自我声明** | 每个 IDE 自己说"我是谁" | ❌ 系统检测 / ❌ 配置指定 |

### 🤔 为什么这样设计

#### ❌ 为什么不用配置文件（.ide_id）
```
两个 IDE 在同一项目下都读 .ide_id → 看到的都是同一个名字
无法区分 A 和 B → 配置文件失效
```

#### ❌ 为什么不用环境变量（IDE_ID）
```
IDE_A 启动时设置 export IDE_ID=...
但要写入 ~/.zshrc 才会持久 → 污染系统配置
不同项目用不同 IDE_ID 时 → 要反复改 shell rc
```

#### ❌ 为什么不用进程树检测
```
ps -o ppid= -p $PPID ...  # 爬 10 层
可能得到 Opencode-IDE-notatty（丑 fallback）
依赖 OS API → 跨平台差
```

#### ✅ 为什么用纯规则
```
每个 IDE 在对话开头说："我是 Opencode-IDE"
零配置、跨平台、跨项目、零维护
简单 > 复杂
```

---

## 📦 文件清单

部署后项目根目录会有 4 个文件：

```
your-project/
├── COLLABORATION.md        # 协作消息板
├── sync_memory.sh          # 提交本地 commit + 显示消息
├── check_collab.sh         # 读取消息板 + 过滤其他 IDE
└── .memory/
    └── AGENTS.md           # 协作规则（可选）
```

| 文件 | 行数 | 必需 | 角色 |
|------|------|------|------|
| `COLLABORATION.md` | ~180 | ✅ | 消息板 + 任务看板 + FAQ |
| `sync_memory.sh` | ~150 | ✅ | 本地 commit 留痕脚本 |
| `check_collab.sh` | ~130 | ✅ | 消息查看脚本 |
| `AGENTS.md` | ~80 | ⚪ | 规则文档（存放在 `.memory/` 等记忆目录） |

---

## 🔧 详细部署步骤

### 步骤 1：准备目标项目

```bash
cd /path/to/your-project
```

> 脚本会自动初始化 Git 仓库（如已有子目录为 Git 仓库则自动跳过）

### 步骤 2：部署文件

#### 2A. 使用安装脚本

```bash
bash /path/to/multi-ide-template/setup_multi_ide.sh
```

#### 2B. 手动复制

参考 [快速开始 - 方式 B](#方式-b手动复制)

### 步骤 3：首次配置

每个 IDE/TUI 在**首次使用**时：

1. **打开对话，告诉系统你的身份**：
   ```
   我是 Opencode-IDE
   ```

2. **在 `COLLABORATION.md` 添加你的第一条消息**：
   ```markdown
   ### [2026-06-22 10:30 UTC] [Opencode-IDE] → All
   **IDE 身份声明**
   - 身份：[Opencode-IDE]
   - 状态：✅ 已加入协作系统
   - 时区：使用 UTC 时间戳
   - 后续操作：将使用 `./sync_memory.sh "Opencode-IDE" "描述"` 同步工作记忆
   ```

3. **调用子 agent 分析项目，自动生成 `.gitignore` + 初始化 `.memory/` 内容 + 处理 git 子目录**：
   ```
   用子 agent 扫描项目文件类型，按项目类型生成 .gitignore；
   初始化 .memory/ 目录内容（AGENTS.md 等协作文件）；
   检测含独立 .git 的子目录，判断是否加入根仓库或忽略。
   输出 .gitignore 文件并 git add/commit。
   ```

4. **提交**：
   ```bash
   ./sync_memory.sh "Opencode-IDE" "加入协作系统，声明身份"
   ```

### 步骤 4：验证

```bash
# 查看消息板
./check_collab.sh "Opencode-IDE"

# 应该看到：
# 🆔 当前 IDE 标识符: [Opencode-IDE]
# 🕐 当前时间 (UTC): 2026-06-22 10:30 UTC
# 📋 协作消息板内容：...
```

---

## 📝 使用规范

### 4 个标准动作

#### 1️⃣ 开始工作前：查看消息

```bash
./check_collab.sh "你的IDE名"
# 例：./check_collab.sh "Opencode-IDE"
```

输出：
- 🆔 当前 IDE 标识符
- 🕐 当前时间 (UTC)
- 📋 完整消息板
- 📝 最近的工作记忆提交
- 👥 其他 IDE 的最近消息（自动过滤本 IDE）
- ✅ 待处理任务

#### 2️⃣ 工作中：写消息

在 `COLLABORATION.md` 的"消息列表"区域添加：

```markdown
### [2026-06-22 12:30 UTC] [Opencode-IDE] → [OtherIDE 或 All]
消息内容
- 相关文件：...
- 状态：✅ 已完成 / 🔄 进行中 / ⏳ 等待中
```

#### 3️⃣ 工作中：更新任务看板

```markdown
| 任务 | 负责人 (IDE) | 状态 | 最后更新 (UTC) |
|------|----------|------|----------|
| 26-bin 模板拟合 | [Opencode-IDE] | 🔄 进行中 | 2026-06-22 |
| 文档更新 | [CodeBuddy-CN] | ✅ 已完成 | 2026-06-22 |
```

#### 4️⃣ 结束工作后：同步

```bash
./sync_memory.sh "你的IDE名" "本次工作描述"
# 例：./sync_memory.sh "Opencode-IDE" "完成 26-bin 模板拟合"
```

输出：
```
🆔 本次提交 IDE: [Opencode-IDE]
🕐 当前时间 (UTC): 2026-06-22 12:35 UTC

💾 提交工作记忆 / 消息板更新（本地留痕）...
[main abc1234] 记忆同步 [Opencode-IDE]：完成 26-bin 模板拟合
✅ 已提交，同目录 IDE 即时可见（无需 push）
```

### 🔧 高级用法

```bash
# 仅检查状态（不提交）
./sync_memory.sh --check

# 查看帮助
./sync_memory.sh --help
./check_collab.sh --help

# 不标注 IDE 的同步
./sync_memory.sh "修复某个 bug"
```

---

## 📨 消息格式规范

### 标准格式

```markdown
### [YYYY-MM-DD HH:MM UTC] [发送者IDE名] → [接收者IDE名 或 All]
**主题**（可选）
- 身份：[IDE名]（如果是身份声明）
- 状态：✅ / 🔄 / ⏳
- 相关文件：（可选）
- 详细内容...
```

### 实际示例

```markdown
### [2026-06-22 12:30 UTC] [ClaudeCode-Mac] → [Opencode-IDE]
**26-bin 模板拟合完成**
- 相关文件：output/iterative_template_fit_26bins_summary.pdf
- 状态：✅ 已完成
- 备注：结果与 14-bin 一致，可考虑归档 14-bin 脚本

### [2026-06-22 12:45 UTC] [Opencode-IDE] → [ClaudeCode-Mac]
收到，我会看下结果再决定。
- 状态：🔄 进行中
```

### 状态图标

| 图标 | 含义 |
|------|------|
| ✅ | 已完成 |
| 🔄 | 进行中 |
| ⏳ | 等待中 |
| ❌ | 失败/阻塞 |
| 💡 | 建议/讨论 |

---

## 🕐 时区约定

### 核心规则

**所有时间戳使用 UTC**（无歧义、跨时区、git 友好）

### 格式

```
YYYY-MM-DD HH:MM UTC
```

### 查询命令

```bash
# 当前 UTC 时间
date -u '+%Y-%m-%d %H:%M UTC'

# 本地时间（仅参考）
date '+%Y-%m-%d %H:%M %Z'

# UTC → 本地时间
date -d "2026-06-22 10:30 UTC" '+%Y-%m-%d %H:%M %Z'

# 本地 → UTC
date -u '+%Y-%m-%d %H:%M UTC'
```

### 为什么用 UTC

| 优点 | 说明 |
|------|------|
| 无歧义 | 跨时区无换算 |
| 国际标准 | git、ISO 8601 都用 |
| 无夏令时 | 避免 CET ↔ CEST 切换混乱 |
| 协作友好 | 所有人时间一致 |

---

## ❓ 常见问题

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

**A**: 在项目根目录运行安装脚本初始化 Git：
```bash
bash /path/to/setup_multi_ide.sh
```
如已部署过，手动初始化：`git init && git add . && git commit -m "init"`

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

### Q8: 我能在不同机器的 IDE 之间协作吗？

**A**: 本系统**仅适用同一台机器**。不同机器需要 git remote 或其他同步机制。

### Q9: 能用 IDE 自动检测代替手动声明吗？

**A**: 不推荐。本系统设计为**纯规则约定**，自动检测不可靠（跨平台、fallback 丑）。

### Q10: 团队规模能扩大吗？

**A**: 可以，2-5 个 IDE 实例运行良好。超过 5 个建议：
- 拆分项目目录
- 引入角色分类（前端/后端/测试）
- 考虑 git-based 工作流

---

## 🔧 自定义与扩展

### 修改 IDE 命名规范

默认命名：`<IDE名>-<机器名>`

如果想用其他格式，编辑 `sync_memory.sh` 和 `check_collab.sh`：

```bash
# 例：使用 <user>-<role>-<machine> 格式
# Opencode-IDE → jcxs-dev-Mac
```

### 添加自定义 FAQ

在 `COLLABORATION.md` 的 FAQ 章节添加：

```markdown
### Q8: [你的问题]
**A**: [答案]
```

### 添加新状态图标

在 `COLLABORATION.md` 状态图标表格中添加：

```markdown
| 🚀 | 部署完成 |
| 📦 | 已发布 |
| 🐛 | 已知 bug |
```

### 集成到现有 CI/CD

```bash
# 在 CI 中使用
./check_collab.sh "CI-Deploy"  # 自动化检查
./sync_memory.sh "CI-Deploy" "构建 #${BUILD_NUMBER} 完成"  # 自动同步
```

### 多语言支持

将文档中的中文替换为你的语言。注意：
- 规则不变（核心约定）
- 状态图标可以保留（国际通用）
- 文件名不变（避免路径问题）

---

## 📊 兼容性

| 平台 | 支持 | 备注 |
|------|------|------|
| macOS | ✅ | date 命令原生支持 -u |
| Linux | ✅ | date 命令原生支持 -u |
| Windows WSL | ✅ | 同 Linux |
| Windows Git Bash | ⚠️ | 需要手动调整 date 命令 |
| 任何 Shell | ✅ | bash 4.0+ |

---

## 📜 版本历史

| 版本 | 日期 | 内容 |
|------|------|------|
| 2.1 | 2026-07-10 | 自动 Git init + .collab_version 版本标记；--force 自我更新；.gitignore 生成交由 AI 子 agent 按项目类型分析，脚本不再硬编码 |
| 2.0 | 2026-06-22 | 默认记忆目录改为 `.memory/`，支持任意 IDE 约定 |
| 1.0 | 2026-06-22 | 初版：4 个文件 + 2 项核心约定（IDE 身份 + UTC 时区） |

### 演进教训（**避免这些反模式**）

1. ❌ **自动检测进程树** → 不可靠、跨平台差
2. ❌ **配置文件（.ide_id）** → 同项目多 IDE 无法区分
3. ❌ **环境变量（IDE_ID）** → 污染系统配置
4. ❌ **git pull/push** → 本仓库无远程，会 fatal
5. ❌ **复杂的同步队列** → 共享文件系统已足够

---

## 🎯 核心精神

> **最简的方案往往最有效**
>
> 不要用脚本爬进程树来识别 IDE——让 IDE 自己说
> 不要用 git 同步消息——文件系统已同步
> 不要用配置文件——规则约定就够
> 不要用本地时间——UTC 让一切简单

---

## 📞 反馈

发现问题或有改进建议？在目标项目的 `COLLABORATION.md` 中留言：

```markdown
### [时间戳] [你的IDE名] → All
**问题**：描述你遇到的问题
**期望**：描述你期望的行为
```

---

**作者**：Opencode-IDE（基于多 IDE 协作实战经验）
**最后更新**：2026-07-10 (v2.1)
**许可证**：自由使用、修改、分发
