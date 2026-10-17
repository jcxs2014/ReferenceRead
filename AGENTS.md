# 多 IDE 协作规则 (2026-06-22)

> 适用场景：两个 IDE 在**同一台机器、同一目录**，共享同一份文件系统。
> 写入文件即同步，**同目录多 IDE 无需 git pull/push**。本仓库已配置 GitHub 远程（`origin` → `https://github.com/jcxs2014/ReferenceRead.git`，2026-08-28 启用）；本地工作通过 `git push origin main` 同步到 GitHub，**禁止 `git pull`**（会造成分叉/覆盖），推送前确保本地领先且快进。

## 📁 记忆目录约定
- **新项目**：使用 `.memory/`（通用、跨 IDE、隐藏目录）
- **兼容旧项目**：`.codebuddy/memory/` / `.opencode/` / `.claude/` / `.cursor/` 等
- **检测优先级**：
  1. `$MEMORY_DIR` 环境变量
  2. 项目内已存在的目录（按 `.memory/` > `memory/` > `.codebuddy/memory/` > `.opencode/` > `.claude/` > `.cursor/` 顺序）
  3. 默认 `.memory/`
- **自定义**：`bash setup_multi_ide.sh --memory-dir <dir>` 或 `export MEMORY_DIR=<dir>`

## 🆔 IDE 身份约定（规则，无配置文件）
- **不写入任何配置文件**——纯规则约定，每个 IDE/TUI **自己声明身份**
- **首次工作**：在对话开头告知身份，例如：
  > "我是 Opencode-IDE"
  > "我是 ClaudeCode-Mac"
- **每次写消息/提交**：前缀标注身份，例如 `### [时间戳] [Opencode-IDE] → All`
- **命名格式**：`<IDE名>-<机器名>`，统一格式，禁止混用旧写法
  - ✅ 正确：`Opencode-IDE`、`CodeBuddy-Mac`、`ZCode-Mac`
  - ❌ 错误：`CodeBuddy` / `CodeBuddy-CN` / `Opencode`（缺少机器名或格式不一）
- **不污染系统配置**（不写 `~/.zshrc`、不创建 `.ide_id` 文件）

## 🕐 时区约定（重要）
- **所有时间戳使用 UTC**（无歧义、跨时区、git 友好）
- **格式**：`YYYY-MM-DD HH:MM UTC`（ISO 8601 风格 + 明确后缀）
- **查询命令**：`date -u '+%Y-%m-%d %H:%M UTC'`
- 各 IDE 自行换算本地时间（`TZ=Asia/Shanghai date` 等）

## 工作流程

1. **工作记忆**：每次工作后用 `./collab/sync_memory.sh "IDE名" "描述"` 做**本地 commit 留痕**
2. **协作消息板**：在 `COLLABORATION.md` 中直接留言——同目录 IDE 写入后即时可见
3. **查看/同步脚本**：
   - `./collab/sync_memory.sh "IDE名" "描述"` - 本地提交记忆与消息板
   - `./collab/sync_memory.sh "描述"` - 不标注 IDE
   - `./collab/sync_memory.sh --memory-dir` - 显示当前记忆目录
   - `./collab/check_collab.sh [本IDE名]` - 读取消息板 + 过滤"其他 IDE 消息"
   - `./collab/check_collab.sh --registry` - 显示已登记的 IDE 身份列表
   - `./collab/check_collab.sh --all` - 显示完整消息板（默认仅最近 20 条）
4. **首次使用**：在对话中声明身份（如"我是 Opencode-IDE"）
5. **任务看板**：在 `COLLABORATION.md` 的"任务看板"区域更新任务状态
6. **时间戳**：消息、任务看板、commit message **全部使用 UTC**

## ❌ 不要做
- 不要写 .ide_id 文件
- 不要设置 IDE_ID 环境变量
- 不要执行 `git pull`（已启用 GitHub 远程，pull 会造成分叉/覆盖）；同步用 `git push origin main`（确保快进）
- 不要用本地时间（统一 UTC）
