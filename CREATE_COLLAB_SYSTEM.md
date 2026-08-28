# 创建多 IDE 协作系统 - 指令模板

> **用途**：在任意项目中部署多 IDE 协作系统
> **适用对象**：AI Agent / 用户
> **位置**：`/Users/jcxs2014/Sites/OpenCodeFiles/multi-ide-template/`

---

## 📦 模板文件清单

```
/Users/jcxs2014/Sites/OpenCodeFiles/multi-ide-template/
├── CREATE_COLLAB_SYSTEM.md  # 本文件：给 AI Agent 的指令模板
├── MULTI_IDE_GUIDE.md       # 详细使用指南（必读）
├── setup_multi_ide.sh       # 安装脚本（项目部署后自动软链接至模板）
├── sync_memory.sh           # 同步脚本（项目部署后自动软链接至模板）
├── check_collab.sh          # 检查脚本（项目部署后自动软链接至模板）
├── COLLABORATION.md         # 协作消息板模板
└── AGENTS.md                # 协作规则模板
```

---

## 🚀 给 AI Agent 的指令（复制粘贴使用）

### 指令 A：完整部署（推荐）

```
请在当前项目目录下部署多 IDE 协作系统：

1. 运行安装脚本：
   bash /Users/jcxs2014/Sites/OpenCodeFiles/multi-ide-template/setup_multi_ide.sh

2. 验证安装成功：
   - ./check_collab.sh "你的IDE名"
   - 应显示 "🆔 当前 IDE 标识符: [你的IDE名]"

3. 在 COLLABORATION.md 添加第一条身份声明消息

4. 调用子 agent 分析项目结构，生成 .gitignore + 初始化 .memory/ 内容

5. 提交：
   ./sync_memory.sh "你的IDE名" "完成多 IDE 协作系统部署"
```

### 指令 B：自动化部署（无交互）

```bash
cd /path/to/your-project
bash /Users/jcxs2014/Sites/OpenCodeFiles/multi-ide-template/setup_multi_ide.sh
./check_collab.sh "$(echo $IDE_NAME)" || ./check_collab.sh "Opencode-IDE"
```

### 指令 C：自定义参数部署

```bash
# 指定 IDE 名
IDE_NAME="MyCustomIDE" bash /Users/jcxs2014/Sites/OpenCodeFiles/multi-ide-template/setup_multi_ide.sh

# 强制覆盖已有协作系统文件（重新部署）
bash /Users/jcxs2014/Sites/OpenCodeFiles/multi-ide-template/setup_multi_ide.sh --force

# 安装到指定目录
bash /Users/jcxs2014/Sites/OpenCodeFiles/multi-ide-template/setup_multi_ide.sh /path/to/project
```

> **注意**：部署后的脚本文件（`setup_multi_ide.sh` / `sync_memory.sh` / `check_collab.sh`）均为**软链接**指向模板目录。
> 模板更新后，所有已部署项目自动同步最新版本。

---

## 📋 部署后必做清单

### 步骤 1：声明身份

在对话中明确说：

> **"我是 [你的IDE名]，[可选：机器名/角色]"**

示例：
- `我是 Opencode-IDE`
- `我是 ClaudeCode-Mac`
- `我是 Cursor-Win`

### 步骤 2：写第一条消息

在 `COLLABORATION.md` 的"消息列表"区域添加：

```markdown
### [2026-06-22 12:30 UTC] [你的IDE名] → All
**IDE 身份声明 + 系统验证**
- 身份：[你的IDE名]
- 环境：[OS / IDE 版本]
- 状态：✅ 已加入协作系统
- 时区：使用 UTC 时间戳
- 验证：./check_collab.sh 输出正常
```

### 步骤 3（重要）：调用子 agent 分析项目结构 + 初始化协作目录

> **用途**：自动生成 `.gitignore`、初始化 `.memory/` 内容、处理含独立 `.git` 的子目录

```
调用子 agent 分析项目：
1. 扫描项目文件类型（.py/.cpp/.js/.root 等），按项目类型生成 `.gitignore`
2. 初始化 `.memory/` 目录内容（写入 AGENTS.md 等协作文件）
3. 检测含独立 `.git` 的子目录，判断是否加入根仓库或忽略
4. 生成 `.gitignore` 文件并 git add，如需则 git commit
```

### 步骤 4：提交记录

```bash
./sync_memory.sh "你的IDE名" "完成多 IDE 协作系统部署"
```

### 步骤 5：通知其他 IDE（如有）

在 `COLLABORATION.md` 任务看板更新：

```markdown
| 任务 | 负责人 (IDE) | 状态 | 最后更新 (UTC) |
|------|----------|------|----------|
| 多 IDE 协作部署 | [你的IDE名] | ✅ 已完成 | 2026-06-22 |
```

---

## 🎯 日常使用工作流

### 工作开始前

```bash
./check_collab.sh "你的IDE名"
# 查看：消息板 + 其他 IDE 消息 + 待处理任务
```

### 工作中

- 写消息：在 `COLLABORATION.md` 添加带 `[时间戳 UTC] [IDE名]` 的消息
- 更新任务：在"任务看板"区域修改状态
- 解决冲突：每个 IDE 标注自己身份

### 工作结束后

```bash
./sync_memory.sh "你的IDE名" "本次工作描述"
# 自动 commit 留痕，消息板同步给其他 IDE
```

---

## 🛠️ 高级用法

### 1. 批量部署到多个项目

```bash
for project in /path/to/proj1 /path/to/proj2 /path/to/proj3; do
    cd "$project"
    bash /Users/jcxs2014/Sites/OpenCodeFiles/multi-ide-template/setup_multi_ide.sh --force
done
```

### 2. 集成到 Git 钩子

在 `.git/hooks/post-commit` 添加：

```bash
#!/bin/bash
# 自动同步 COLLABORATION.md
if [ -f "./sync_memory.sh" ]; then
    ./sync_memory.sh "Hook-Auto" "自动 commit: $(git log -1 --pretty=%s)" || true
fi
```

### 3. CI/CD 集成

```yaml
# .github/workflows/notify-collab.yml
- name: Notify collaboration
  run: |
    ./sync_memory.sh "CI-Deploy" "Build #${BUILD_NUMBER} ${BUILD_STATUS}"
```

### 4. 自定义消息格式

编辑 `COLLABORATION.md` 的"消息列表"区域说明：

```markdown
### [YYYY-MM-DD HH:MM UTC] [发送者] → [接收者]
**主题**
- 优先级：🔴/🟡/🟢
- 截止：YYYY-MM-DD
- 内容：...
```

---

## ❓ 故障排查

### 问题 1：脚本无权限

```bash
chmod +x /Users/jcxs2014/Sites/OpenCodeFiles/multi-ide-template/setup_multi_ide.sh
chmod +x sync_memory.sh check_collab.sh  # 在目标项目
```

### 问题 2：非 Git 目录

无需处理，脚本会自动初始化 Git 仓库。如有子目录已含 `.git`，会自动跳过。

### 问题 3：文件已存在

脚本会自动检测版本，已最新则跳过。如需强制覆盖重新部署：
```bash
bash /Users/jcxs2014/Sites/OpenCodeFiles/multi-ide-template/setup_multi_ide.sh --force
```

### 问题 4：时区显示不对

```bash
# macOS/Linux 检查
date -u
# 应该返回 UTC 时间

# 如果不对，检查系统时区设置
ls -la /etc/localtime
```

---

## 📖 进阶阅读

| 文档 | 内容 |
|------|------|
| `MULTI_IDE_GUIDE.md` | 完整使用指南（FAQ、设计理念、自定义） |
| `COLLABORATION.md`（部署后） | 消息板和任务看板 |

---

## 🔗 相关资源

- **模板位置**：`/Users/jcxs2014/Sites/OpenCodeFiles/multi-ide-template/`
- **设计来源**：SubIron 项目（4 个 IDE 协作验证）
- **测试 IDE**：Opencode-IDE / CodeBuddy-CN / Qoder-CN / ZCode-Mac

---

## 💡 核心精神

> **最简的方案往往最有效**
>
> - 共享文件系统 = 自动同步
> - 每个 IDE 自己说"我是谁"
> - UTC 消除时区混乱
> - 规则约定 > 复杂脚本

---

**最后更新**：2026-07-10 (v2.1)
**维护者**：Opencode-IDE
**许可证**：自由使用、修改、分发
