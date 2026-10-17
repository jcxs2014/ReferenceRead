#!/bin/bash
# 查看协作消息板（纯本地读取）
#
# 两个 IDE 在同一台机器同一目录，共享同一份文件系统，
# 无需 git pull——对方写入后此文件即时可见。
#
# 使用方式：./check_collab.sh [本IDE名称]
#   - 参数：可选，用于过滤"其他 IDE"的消息
#   - 也可通过环境变量 IDE_NAME 指定
#
# 选项：
#   -h, --help     显示帮助信息
#   --memory-dir   显示当前使用的记忆目录

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# ============ 记忆目录检测 ============
detect_memory_dir() {
    local dir

    if [ -n "$MEMORY_DIR" ]; then
        echo "$MEMORY_DIR"
        return
    fi

    for dir in .memory memory .codebuddy/memory .opencode .claude .cursor; do
        if [ -d "$dir" ]; then
            echo "$dir"
            return
        fi
    done

    echo ".memory"
}

MEMORY_DIR=$(detect_memory_dir)

# 显示帮助
show_help() {
    echo "=========================================="
    echo "  协作消息板查看工具使用帮助"
    echo "=========================================="
    echo ""
    echo "用途：查看协作消息板、工作记忆、待处理任务"
    echo ""
    echo "使用方式："
    echo "  ./check_collab.sh [本IDE名称]"
    echo "  IDE_NAME=MyIDE ./check_collab.sh"
    echo ""
    echo "选项："
    echo "  -h, --help     显示此帮助信息"
    echo "  --memory-dir   显示当前使用的记忆目录"
    echo "  --registry     显示已登记的 IDE 身份列表"
    echo ""
    echo "当前记忆目录: $MEMORY_DIR"
    echo ""
    echo "示例："
    echo "  ./check_collab.sh Opencode-IDE"
    echo "  ./check_collab.sh \"\"   # 不标注 IDE"
    echo "  IDE_NAME=ClaudeCode ./check_collab.sh"
    echo ""
    echo "输出内容："
    echo "  1. 协作消息板完整内容"
    echo "  2. 最近的工作记忆提交"
    echo "  3. 其他 IDE 的最近消息（如指定了本 IDE 名）"
    echo "  4. 待处理任务列表"
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

# 显示已登记的 IDE 身份列表
if [[ "$1" == "--registry" ]]; then
    echo "=========================================="
    echo "  已登记的 IDE 身份列表"
    echo "=========================================="
    echo ""
    REGISTRY="collab/collab_identities.json"
    if [ ! -f "$REGISTRY" ]; then
        echo -e "${YELLOW}⚠️  $REGISTRY 不存在${NC}"
        echo "   身份登记表尚未创建"
        exit 0
    fi
    # 解析 JSON 并显示 canonical + aliases
    python3 -c "
import json, sys
try:
    d = json.load(open('$REGISTRY'))
    identities = d.get('identities', [])
    if not identities:
        print('  (暂无登记身份)')
    for i, ident in enumerate(identities, 1):
        canonical = ident.get('canonical', '?')
        confirmed = ident.get('confirmed', False)
        aliases = ident.get('aliases', [])
        status = '✅' if confirmed else '⚠️ '
        print(f'  {i}. {status} {canonical}')
        if aliases:
            print('     aliases: ' + ', '.join(aliases))
        note = ident.get('_note', '')
        if note:
            print(f'     note: {note[:80]}...' if len(note) > 80 else f'     note: {note}')
    print()
    print(f'机器后缀约定: {d.get(\"_机器后缀约定\", \"未设置\")}')
except Exception as e:
    print(f'  解析失败: {e}', file=sys.stderr)
    exit(1)
"
    exit 0
fi

cd "$(dirname "$0")/.."

# 0. 检查 Git 仓库
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${RED}❌ 错误：当前目录不是 Git 仓库${NC}"
    echo "   当前目录: $(pwd)"
    echo "   请确保在项目根目录运行此脚本"
    echo ""
    echo "提示：使用 ./check_collab.sh --help 查看帮助"
    exit 1
fi

# 1. 可选地确定本 IDE 标识符（仅用于过滤显示，不写入任何文件）
MY_IDE="${1:-${IDE_NAME:-}}"
echo "=========================================="
if [ -n "$MY_IDE" ]; then
    echo -e "${BLUE}🆔 当前 IDE 标识符: [$MY_IDE]${NC}"
else
    echo -e "${YELLOW}🆔 当前 IDE 标识符: (未声明)${NC}"
fi
echo -e "${BLUE}🕐 当前时间 (UTC): $(date -u '+%Y-%m-%d %H:%M UTC')${NC}"
echo -e "${BLUE}📁 记忆目录: $MEMORY_DIR${NC}"
echo "=========================================="
echo ""

# 2. 显示消息板内容（直接读本地文件）
echo -e "${GREEN}🔍 查看协作消息板...${NC}"
echo ""
if [ -f "COLLABORATION.md" ]; then
    echo -e "${BLUE}📋 协作消息板内容：${NC}"
    echo "=========================================="
    # C1: 默认限长，--all 才全文
    if [ "${2:-}" = "--all" ]; then
        cat COLLABORATION.md
    else
        echo "（默认仅显示最近 20 条；全文请加 --all）"
        grep -n '^### \[[0-9]\{4\}-' COLLABORATION.md | head -20
    fi
    echo "=========================================="
    echo ""
else
    echo -e "${YELLOW}⚠️  协作消息板文件不存在：${NC}"
    echo "   创建空文件：touch COLLABORATION.md"
    echo ""
fi

# 2.5 容量红线检查
if [ -f "COLLABORATION.md" ]; then
    SZ=$(wc -c < COLLABORATION.md)
    if [ "$SZ" -ge 71680 ]; then
        echo -e "${RED}⚠️  COLLABORATION.md = ${SZ} B，已超单次读取上限 71680，请归档：${NC}"
        echo "      python3 archive_split.py            # 先看计划"
        echo "      python3 archive_split.py --apply    # 执行"
        echo ""
    fi
fi

# 3. 显示最近的工作记忆提交记录
echo -e "${GREEN}📝 最近的工作记忆提交：${NC}"
git log --oneline -10 -- "$MEMORY_DIR/" 2>/dev/null || echo "（无提交记录）"
echo ""

# 4. 识别消息板中其他 IDE 的消息
if [ -f "COLLABORATION.md" ] && [ -n "$MY_IDE" ]; then
    echo -e "${GREEN}👥 其他 IDE 的最近消息（不含 [$MY_IDE]）：${NC}"
    OTHER_MSGS=$(grep -E '^### \[[0-9]{4}-' COLLABORATION.md 2>/dev/null | grep -v "\[$MY_IDE\]" | head -5 || true)
    if [ -n "$OTHER_MSGS" ]; then
        echo "$OTHER_MSGS"
    else
        echo -e "${YELLOW}（无其他 IDE 消息）${NC}"
    fi
    echo ""
fi

# 5. 显示待处理的任务
if [ -f "COLLABORATION.md" ]; then
    echo -e "${GREEN}✅ 待处理任务：${NC}"
    grep -E -B1 "⏳|等待中|TODO" COLLABORATION.md 2>/dev/null || echo -e "${YELLOW}（无待处理任务）${NC}"
    echo ""
fi

# 6. 显示完成提示
echo "=========================================="
echo -e "${GREEN}✅ 检查完成！${NC}"
echo ""
echo "📌 下一步："
echo "   - 同步更新：./sync_memory.sh [IDE名] \"描述\""
echo "   - 查看帮助：./check_collab.sh --help"
echo "   - 编辑消息板：nano COLLABORATION.md"
echo "=========================================="
