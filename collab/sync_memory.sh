#!/bin/bash
# 提交工作记忆与协作消息板（纯本地）
#
# 两个 IDE 在同一台机器同一目录，共享同一份文件系统，
# 写入 COLLABORATION.md / 记忆目录 后对方即时可见，
# 无需 git pull/push。git commit 仅用于本地留痕与可追溯。
#
# 使用方式：
#   ./sync_memory.sh "IDE名" "描述本次工作"
#   ./sync_memory.sh "描述本次工作"
#   IDE_NAME=MyIDE ./sync_memory.sh "描述"
#   MEMORY_DIR=memory ./sync_memory.sh "描述"
#
# 选项：
#   -h, --help     显示帮助信息
#   --check        仅检查状态，不提交
#   --memory-dir   显示当前使用的记忆目录

set -e

# ============ 记忆目录检测 ============
detect_memory_dir() {
    local dir

    # 1. 环境变量
    if [ -n "$MEMORY_DIR" ]; then
        echo "$MEMORY_DIR"
        return
    fi

    # 2. 项目内已有的记忆目录（按优先级）
    for dir in .memory memory .codebuddy/memory .opencode .claude .cursor; do
        if [ -d "$dir" ]; then
            echo "$dir"
            return
        fi
    done

    # 3. 默认
    echo ".memory"
}

MEMORY_DIR=$(detect_memory_dir)

# 显示帮助
show_help() {
    echo "=========================================="
    echo "  工作记忆同步脚本使用帮助"
    echo "=========================================="
    echo ""
    echo "用途：提交工作记忆与协作消息板（本地留痕）"
    echo ""
    echo "使用方式："
    echo "  ./sync_memory.sh \"IDE名\" \"描述\"   # 推荐：标注 IDE"
    echo "  ./sync_memory.sh \"描述\"              # 不标注 IDE"
    echo "  IDE_NAME=MyIDE ./sync_memory.sh \"描述\"  # 通过环境变量"
    echo ""
    echo "选项："
    echo "  -h, --help     显示此帮助信息"
    echo "  --check        仅检查状态，不提交"
    echo "  --memory-dir   显示当前使用的记忆目录"
    echo ""
    echo "当前记忆目录: $MEMORY_DIR"
    echo "可通过环境变量自定义: MEMORY_DIR=.memory ./sync_memory.sh"
    echo ""
    echo "示例："
    echo "  ./sync_memory.sh \"Opencode-IDE\" \"完成 26-bin 模板拟合\""
    echo "  ./sync_memory.sh \"修复 bug\""
    echo "  ./sync_memory.sh --check"
    echo ""
    echo "注意："
    echo "  - 两个 IDE 在同一目录，写入即同步，无需 git push"
    echo "  - git commit 仅用于本地留痕与可追溯"
    echo "  - 请确保当前目录是 Git 仓库"
    echo ""
    exit 0
}

# 检查是否是帮助请求
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    show_help
fi

# 显示记忆目录
if [[ "$1" == "--memory-dir" ]]; then
    echo "当前使用的记忆目录: $MEMORY_DIR"
    exit 0
fi

cd "$(dirname "$0")/.."

# 仅检查模式
if [[ "$1" == "--check" ]]; then
    echo "🔍 检查工作记忆与消息板状态..."
    echo ""
    echo "📂 当前目录: $(pwd)"
    echo "📁 记忆目录: $MEMORY_DIR"
    echo ""
    echo "📝 工作记忆状态："
    git status --short "$MEMORY_DIR/" 2>/dev/null || echo "  (Git 仓库检查失败)"
    echo ""
    echo "📋 协作消息板状态："
    git status --short COLLABORATION.md 2>/dev/null || echo "  (COLLABORATION.md 无变更)"
    echo ""
    echo "📊 最近提交："
    git log --oneline -5 -- "$MEMORY_DIR/" COLLABORATION.md 2>/dev/null || echo "  (无提交记录)"
    exit 0
fi

# ============ 主流程 ============

# 0. 检查 Git 仓库
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ 错误：当前目录不是 Git 仓库"
    echo "   当前目录: $(pwd)"
    echo "   请确保在项目根目录运行此脚本"
    echo ""
    echo "提示：使用 ./sync_memory.sh --help 查看帮助"
    exit 1
fi

# 1. 解析参数
if [ $# -ge 2 ]; then
    IDE_NAME="$1"
    DESCRIPTION="$2"
elif [ $# -eq 1 ]; then
    DESCRIPTION="$1"
    IDE_NAME="${IDE_NAME:-}"
else
    DESCRIPTION="$(date -u '+%Y-%m-%d %H:%M UTC')"
    IDE_NAME="${IDE_NAME:-}"
fi

if [ -n "$IDE_NAME" ]; then
    echo "🆔 本次提交 IDE: [$IDE_NAME]"
    COMMIT_PREFIX="[$IDE_NAME]"
else
    echo "🆔 本次提交未标注 IDE"
    COMMIT_PREFIX=""
fi
echo "🕐 当前时间 (UTC): $(date -u '+%Y-%m-%d %H:%M UTC')"
echo "📁 记忆目录: $MEMORY_DIR"
echo ""

# 2. 提交本地记忆更新与消息板
STAGED=""
if [ -n "$(git status --short "$MEMORY_DIR/")" ]; then
    git add "$MEMORY_DIR/"
    STAGED="yes"
fi
if [ -n "$(git status --short COLLABORATION.md)" ]; then
    git add COLLABORATION.md
    STAGED="yes"
fi

if [ -n "$STAGED" ]; then
    echo "💾 提交工作记忆 / 消息板更新（本地留痕）..."
    if [ -n "$COMMIT_PREFIX" ]; then
        git commit -m "记忆同步 $COMMIT_PREFIX：$DESCRIPTION"
    else
        git commit -m "记忆同步：$DESCRIPTION"
    fi
    echo "✅ 已提交，同目录 IDE 即时可见（无需 push）"
else
    echo "✅ 工作记忆与消息板无更新"
fi

# 3. 显示协作消息板最近消息
if [ -f "COLLABORATION.md" ]; then
    echo ""
    echo "📋 协作消息板最近消息："
    echo "=========================================="
    grep -E '^### \[[0-9]{4}-' COLLABORATION.md | head -20 || echo "（无消息）"
    echo "=========================================="
    echo ""
fi

# 4. 显示成功提示
echo "✅ 同步完成！"
echo "   - 如有更新已提交（本地留痕）"
echo "   - 同目录 IDE 即时可见（无需 pull/push）"
echo ""
echo "📌 下一步："
echo "   - 查看消息板：./check_collab.sh"
echo "   - 检查状态：./sync_memory.sh --check"
echo "   - 查看其他 IDE 消息：./check_collab.sh [本IDE名]"
echo ""
