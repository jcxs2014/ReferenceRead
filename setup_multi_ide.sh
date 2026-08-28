#!/bin/bash
# setup_multi_ide.sh — 多 IDE 协作系统一键安装脚本 v2.1
#
# 用途：将多 IDE 协作系统部署到任意 Git 项目
# 使用方式：
#   bash setup_multi_ide.sh                          # 安装到当前目录（默认 .memory/）
#   bash setup_multi_ide.sh /path/to/project         # 安装到指定目录
#   bash setup_multi_ide.sh --memory-dir .opencode   # 自定义记忆目录
#   bash setup_multi_ide.sh --help                   # 显示帮助
#
# 部署内容：
#   - COLLABORATION.md (消息板 + 任务看板 + FAQ)
#   - sync_memory.sh (本地 commit 留痕脚本)
#   - check_collab.sh (消息查看脚本)
#   - <MEMORY_DIR>/AGENTS.md (规则文档)
#
# v2.1 变更：
#   - 记忆目录在检测时即创建（不再延迟到文件写入阶段）
#   - 检测自身 .git（而非父目录），修复误判父 git 仓库的问题
#   - 脚本文件全部改为软链接至模板目录，部署即同步更新
#   - 移除嵌入 heredoc，脚本体积大幅精简（889→281行）
#   - 移除 .collab_version 版本标记（软链接架构下始终最新，无需版本检测）
#   - .gitignore 和 AGENTS.md 生成交由 AI 子 agent 按项目类型自动分析
# v2.0 变更：
#   - 默认记忆目录从 .codebuddy/memory/ 改为 .memory/（通用、跨 IDE、隐藏）
#   - 支持任意 IDE 的记忆目录约定
#   - 自动检测优先级：$MEMORY_DIR > .memory/ > .codebuddy/memory/ > .opencode/ ...

set -e

# ============ 配置 ============
SCRIPT_VERSION="2.1"
TEMPLATE_DIR="$(cd "$(dirname "$0")" && pwd)"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 默认记忆目录（按优先级排序）
DEFAULT_MEMORY_DIRS=(".memory" "memory" ".codebuddy/memory" ".opencode" ".claude" ".cursor" ".aider")



# ============ 帮助信息 ============
show_help() {
    cat << EOF
========================================
  多 IDE 协作系统安装脚本 v${SCRIPT_VERSION}
========================================

用途：将多 IDE 协作系统部署到任意 Git 项目

使用方式：
  bash setup_multi_ide.sh                          # 安装到当前目录
  bash setup_multi_ide.sh /path/to/project         # 安装到指定目录
  bash setup_multi_ide.sh --memory-dir .memory     # 指定记忆目录
  bash setup_multi_ide.sh --help                   # 显示帮助

选项：
  --help, -h           显示此帮助信息
  --force              覆盖已存在的协作系统文件（默认仅检查版本，已最新则跳过）
  --skip-check         跳过 Git 仓库检查
  --memory-dir DIR     指定记忆目录（默认自动检测）

记忆目录检测顺序：
  1. \$MEMORY_DIR 环境变量
  2. --memory-dir 命令行参数
  3. 项目内已存在的目录（按优先级）：
     .memory/  >  memory/  >  .codebuddy/memory/  >  .opencode/  >  .claude/  >  .cursor/

默认行为：
  - 新项目：使用 .memory/（通用、跨 IDE、隐藏目录）
  - 已有 .codebuddy/memory/：继续使用（向后兼容）
  - 已有其他 IDE 目录：可指定或自动选择

示例：
  cd /path/to/your-project
  bash setup_multi_ide.sh                          # 新项目
  bash setup_multi_ide.sh --memory-dir .opencode   # Opencode IDE 项目
  bash setup_multi_ide.sh --force                  # 覆盖现有文件

部署内容：
  - COLLABORATION.md (消息板)
  - sync_memory.sh (提交脚本)
  - check_collab.sh (查看脚本)
  - <MEMORY_DIR>/AGENTS.md (规则)
EOF
    exit 0
}

# ============ 参数解析 ============
FORCE=false
SKIP_CHECK=false
TARGET_DIR=""
MEMORY_DIR_OVERRIDE=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --help|-h)
            show_help
            ;;
        --force)
            FORCE=true
            shift
            ;;
        --skip-check)
            SKIP_CHECK=true
            shift
            ;;
        --memory-dir)
            MEMORY_DIR_OVERRIDE="$2"
            shift 2
            ;;
        *)
            TARGET_DIR="$1"
            shift
            ;;
    esac
done

# 默认目标目录
if [ -z "$TARGET_DIR" ]; then
    TARGET_DIR="$(pwd)"
fi

# 转为绝对路径
TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

# ============ 检测记忆目录 ============
detect_memory_dir() {
    local dir

    # 1. 优先级最高：环境变量
    if [ -n "$MEMORY_DIR" ]; then
        echo "$MEMORY_DIR"
        return
    fi

    # 2. 命令行参数
    if [ -n "$MEMORY_DIR_OVERRIDE" ]; then
        echo "$MEMORY_DIR_OVERRIDE"
        return
    fi

    # 3. 项目内已有的记忆目录（按优先级）
    cd "$TARGET_DIR"
    for dir in "${DEFAULT_MEMORY_DIRS[@]}"; do
        if [ -d "$dir" ]; then
            echo "$dir"
            return
        fi
    done

    # 4. 默认使用通用 .memory/（隐藏目录）
    echo ".memory"
}

MEMORY_DIR=$(detect_memory_dir)
mkdir -p "$TARGET_DIR/$MEMORY_DIR"
echo -e "${GREEN}✅ 记忆目录已就绪: $MEMORY_DIR${NC}"

# ============ 环境检查 ============
echo "=========================================="
echo -e "${BLUE}🚀 多 IDE 协作系统安装脚本 v${SCRIPT_VERSION}${NC}"
echo "=========================================="
echo ""
echo "目标目录: $TARGET_DIR"
echo "记忆目录: $MEMORY_DIR"
echo ""

# 检查目标目录是否存在
if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${RED}❌ 错误：目标目录不存在${NC}"
    echo "   $TARGET_DIR"
    exit 1
fi

# 检查并初始化 Git 仓库
if [ "$SKIP_CHECK" = false ]; then
    cd "$TARGET_DIR"
    if [ -d ".git" ] || [ -f ".git" ]; then
        echo -e "${GREEN}✅ Git 仓库检查通过${NC}"
    else
        SUB_GIT_DIRS=$(find . -maxdepth 3 -name ".git" \( -type d -o -type f \) 2>/dev/null | while read p; do dirname "$p"; done | sort -u | grep -v "^\.$" || true)
        if [ -n "$SUB_GIT_DIRS" ]; then
            echo -e "${YELLOW}⚠️  目标目录不是 Git 仓库，但子目录中存在 Git 仓库${NC}"
            echo "   自动初始化 Git 仓库..."
            git init
            for item in * .[!.]*; do
                [ -e "$item" ] || continue
                skip=false
                for subdir in $SUB_GIT_DIRS; do
                    if [ "$item" = "$subdir" ] || [ "$item" = "$subdir/" ]; then
                        skip=true
                        break
                    fi
                done
                if [ "$skip" = false ]; then
                    git add "$item"
                fi
            done
            git commit -m "init: 多 IDE 协作系统初始化" 2>/dev/null || true
            echo -e "${GREEN}✅ 已初始化 Git 仓库（跳过已有 Git 的子目录）${NC}"
        else
            echo -e "${YELLOW}⚠️  目标目录不是 Git 仓库，自动初始化...${NC}"
            git init
            git add -A
            git commit -m "init: 多 IDE 协作系统初始化" 2>/dev/null || true
            echo -e "${GREEN}✅ 已初始化 Git 仓库${NC}"
        fi
    fi
fi

# ============ 部署文件 ============

# COLLABORATION.md（从模板拷贝，供 AI 子 agent 定制）
cp "$TEMPLATE_DIR/COLLABORATION.md" "$TARGET_DIR/COLLABORATION.md"
echo -e "${GREEN}✅ COLLABORATION.md${NC}"

# sync_memory.sh → 软链接
ln -sf "$TEMPLATE_DIR/sync_memory.sh" "$TARGET_DIR/sync_memory.sh"
echo -e "${GREEN}✅ sync_memory.sh (软链接)${NC}"

# check_collab.sh → 软链接
ln -sf "$TEMPLATE_DIR/check_collab.sh" "$TARGET_DIR/check_collab.sh"
echo -e "${GREEN}✅ check_collab.sh (软链接)${NC}"

# setup_multi_ide.sh → 软链接（仅当尚未是正确链接时）
if [ ! -L "$TARGET_DIR/setup_multi_ide.sh" ] || [ "$(readlink "$TARGET_DIR/setup_multi_ide.sh")" != "$TEMPLATE_DIR/setup_multi_ide.sh" ]; then
    ln -sf "$TEMPLATE_DIR/setup_multi_ide.sh" "$TARGET_DIR/setup_multi_ide.sh"
fi
echo -e "${GREEN}✅ setup_multi_ide.sh (软链接)${NC}"

# AGENTS.md 由 AI 子 agent 按项目分析后生成（脚本仅确保目录存在）
echo -e "${GREEN}✅ $MEMORY_DIR/ (内容待 AI 子 agent 初始化)${NC}"

# ============ 完成 ============
echo ""
echo "=========================================="
echo -e "${GREEN}🎉 多 IDE 协作系统部署完成！${NC}"
echo "=========================================="
echo ""
echo "已部署文件："
echo "  - $TARGET_DIR/COLLABORATION.md"
echo "  - $TARGET_DIR/sync_memory.sh (软链接)"
echo "  - $TARGET_DIR/check_collab.sh (软链接)"
echo "  - $TARGET_DIR/setup_multi_ide.sh (软链接)"
echo "  - $TARGET_DIR/$MEMORY_DIR/ (目录，内容待 AI 子 agent 初始化)"
echo ""
echo "📌 下一步："
echo ""
echo "  1. 首次声明身份（在对话中说）："
echo "     \"我是 <你的IDE名>\""
echo ""
echo "  2. 在 COLLABORATION.md 添加第一条消息"
echo ""
echo "  3. 调用子 agent 分析项目结构，生成 .gitignore + 初始化 .memory/ 内容"
echo ""
echo "  4. 验证安装："
echo "     cd $TARGET_DIR"
echo "     ./check_collab.sh \"<你的IDE名>\""
echo ""
echo "  5. 查看记忆目录："
echo "     ./sync_memory.sh --memory-dir"
echo ""
echo "  6. 工作流："
echo "     - 工作前：./check_collab.sh \"<你的IDE名>\""
echo "     - 工作后：./sync_memory.sh \"<你的IDE名>\" \"描述\""
echo ""
echo "📖 详细文档：MULTI_IDE_GUIDE.md"
echo ""
echo "🆔 已成功支持 4 个 IDE 协作："
echo "   - Opencode-IDE"
echo "   - CodeBuddy-CN"
echo "   - Qoder-CN"
echo "   - ZCode-Mac"
echo ""
echo -e "${BLUE}祝你协作愉快！${NC}"
