#!/usr/bin/env python3
"""
fix_math_fragmentation.py — 公式格式割裂修复（形态①/②/③）

铁律：
  - 数字零变化（只把 ×/上下标 并入 $...$，数字/指数不变）
  - $ 配对完整（每行 $ 数为偶数）
  - 不动已规范公式（已是 $...\times10^{...}$ 等跳过）
  - 幂等（重复运行无新增改动）

用法：
  python3 fix_math_fragmentation.py [--audit FILE] [--dry-run] PATH [PATH ...]
  PATH 可为文件或目录（目录递归处理 *.md）。
"""
import re
import sys
import pathlib

# ---------- Unicode 上下标映射 ----------
SUP_MAP = {
    '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6',
    '⁷': '7', '⁸': '8', '⁹': '9', '⁺': '+', '⁻': '-', '⁽': '(', '⁾': ')',
    'ⁿ': 'n',
}
SUB_MAP = {
    '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6',
    '₇': '7', '₈': '8', '₉': '9', '₊': '+', '₋': '-', '₍': '(', '₎': ')',
    'ₐ': 'a', 'ₑ': 'e', 'ₕ': 'h', 'ᵢ': 'i', 'ⱼ': 'j', 'ₖ': 'k', 'ₗ': 'l',
    'ₘ': 'm', 'ₙ': 'n', 'ₒ': 'o', 'ₚ': 'p', 'ᵣ': 'r', 'ₛ': 's', 'ₜ': 't',
    'ᵤ': 'u', 'ᵥ': 'v', 'ₓ': 'x',
}
UNI_SUPSUB = set(SUP_MAP) | set(SUB_MAP)

# ---------- 形态① 正则 ----------
R1 = re.compile(r'([\d.~≈]+)\s*×\s*\$10\^\{([^{}]+)\}\$')
# ---------- 形态③ 步骤1：去掉 $\Phi$(eX) 外层 $ ----------
R3_PHI = re.compile(r"\$\\Phi\$\((e[⁺⁻])\)")
# ---------- 形态③ 步骤2：包裹未包 $ 的流比表达式 ----------
# 注意：R3_PHI 已将 ± 转为 ASCII [+-]，此处必须用 [+-] 而非 [⁺⁻]
R3_WRAP = re.compile(
    r"(?<!\$)(?P<e>\\Phi\(e\^\{[+-]\}\)/\(\\Phi\(e\^\{[+-]\}\)"
    r"\+\\Phi\(e\^\{[+-]\}\)\))(?!\$)"
)


# ---------- frontmatter 状态机（修复版：无闭合 --- 视为正文） ----------
def in_frontmatter(text):
    lines = text.split('\n')
    res = [False] * len(lines)
    if not lines or lines[0].strip() != '---':
        return res
    infm = True
    res[0] = True
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            infm = False
            res[i] = True
            continue
        res[i] = infm
    return res


# ---------- 形态② 辅助 ----------
def capture_text(s):
    """从 s 开头捕获 [ASCII字母数字 / Unicode上下标 / 数字间小数点] 连续段，转 ASCII。"""
    out = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch.isalnum() or ch in UNI_SUPSUB:
            out.append(SUP_MAP.get(ch, SUB_MAP.get(ch, ch)))
            i += 1
        elif ch == '.' and out and out[-1].isdigit() and i + 1 < len(s) and s[i + 1].isdigit():
            out.append('.')
            i += 1
        else:
            break
    return ''.join(out), i


def capture_unicode(s):
    """从 s 开头捕获连续 Unicode 上下标，转 ASCII。"""
    out = []
    i = 0
    while i < len(s) and s[i] in UNI_SUPSUB:
        out.append(SUP_MAP.get(s[i], SUB_MAP.get(s[i], s[i])))
        i += 1
    return ''.join(out), i


def merge_into(inner, kind, content, is_nested):
    """把上下标并入 inner（无外层 $），返回新 inner。content 已转 ASCII。"""
    if is_nested:
        # 嵌套公式内容（如 \mu），单 token 不加花括号
        if re.match(r'^(\\[a-zA-Z]+|[a-zA-Z])$', content):
            return f'{inner}{kind}{content}'
        return f'{inner}{kind}{{{content}}}'
    if re.fullmatch(r'[\d.]+', content):
        return f'{inner}{kind}{{{content}}}'          # 数字/小数直接进 braces，不加 \rm
    if len(content) == 1:
        if content.isdigit():
            return f'{inner}{kind}{content}'          # 单数字无花括号
        return f'{inner}{kind}{{\\rm {content}}}'  # 单字母 -> \rm
    if content.isdigit():
        return f'{inner}{kind}{{{content}}}'          # 多数字无 \rm
    return f'{inner}{kind}{{\\rm {content}}}'      # 多字母 -> \rm


def fix_form2_line(line):
    out = []
    i = 0
    n = len(line)
    changes = []
    while i < n:
        ch = line[i]
        if ch == '$':
            j = line.find('$', i + 1)
            if j == -1:
                out.append(line[i:])
                break
            formula = line[i:j + 1]
            inner = line[i + 1:j]
            tail = line[j + 1:]
            k = 0
            while k < len(tail) and tail[k].isspace():
                k += 1
            if k >= len(tail):
                out.append(formula)
                i = j + 1
                continue
            c = tail[k]
            if c not in '^_' and c not in UNI_SUPSUB:
                out.append(formula)
                i = j + 1
                continue
            # 迭代合并链式的 ^X _Y Unicode（一次 pass 内完成，保证幂等）
            cur_inner = inner
            pos = k
            merged_any = False
            while pos < len(tail):
                cc = tail[pos]
                if cc in '^_':
                    nxt = tail[pos + 1] if pos + 1 < len(tail) else ''
                    if nxt == '{':
                        break  # 合法 LaTeX 上下标，停止合并
                    rest = tail[pos + 1:]
                    if rest and rest[0] == '$':
                        # 嵌套公式：$\nu$_$\mu$ -> $\nu_\mu$
                        j2 = rest.find('$', 1)
                        if j2 != -1:
                            nested_inner = rest[1:j2]
                            cur_inner = merge_into(cur_inner, cc, nested_inner, True)
                            pos = (pos + 1) + (j2 + 1)
                            merged_any = True
                            continue
                    content, consumed = capture_text(rest)
                    if consumed == 0:
                        break
                    cur_inner = merge_into(cur_inner, cc, content, False)
                    pos = (pos + 1) + consumed
                    merged_any = True
                    continue
                elif cc in UNI_SUPSUB:
                    content, consumed = capture_unicode(tail[pos:])
                    if consumed == 0:
                        break
                    kind = '^' if cc in SUP_MAP else '_'
                    cur_inner = merge_into(cur_inner, kind, content, False)
                    pos = pos + consumed
                    merged_any = True
                    continue
                else:
                    break
            if merged_any:
                newf = f'${cur_inner}$'
                oldseg = line[i:j + 1 + pos]
                changes.append(('form2', oldseg, newf))
                out.append(newf)
                i = j + 1 + pos
                continue
            else:
                out.append(formula)
                i = j + 1
                continue
        else:
            out.append(ch)
            i += 1
    return ''.join(out), changes


# ---------- 形态① ----------
def fix_form1_line(line):
    changes = []

    def repl(m):
        before = line[:m.start()]
        if before.count('$') % 2 != 0:
            return m.group(0)   # 处于 math 模式内，不动
        new = f'${m.group(1)}\\times10^{{{m.group(2)}}}$'
        changes.append(('form1', m.group(0), new))
        return new

    return R1.sub(repl, line), changes


# ---------- 形态③ ----------
def fix_form3_line(line):
    changes = []

    def repl_phi(m):
        sign = '+' if m.group(1)[-1] == '⁺' else '-'
        return f"\\Phi(e^{{{sign}}})"

    line2 = R3_PHI.sub(repl_phi, line)
    if line2 != line:
        m = R3_WRAP.search(line2)
        if m:
            wrapped = '$' + m.group('e') + '$'
            changes.append(('form3', m.group('e'), wrapped))
            line2 = line2[:m.start()] + wrapped + line2[m.end():]
    return line2, changes


# ---------- 主转换 ----------
def convert(text):
    lines = text.split('\n')
    fm = in_frontmatter(text)
    audit = []
    out_lines = []
    for idx, line in enumerate(lines):
        if fm[idx]:
            out_lines.append(line)
            continue
        new1, c1 = fix_form1_line(line)
        new2, c2 = fix_form2_line(new1)
        new3, c3 = fix_form3_line(new2)
        for form, old, new in c1 + c2 + c3:
            audit.append((idx + 1, form, old, new))
        out_lines.append(new3)
    return '\n'.join(out_lines), audit


def collect_files(paths):
    files = []
    for p in paths:
        pp = pathlib.Path(p)
        if pp.is_dir():
            files.extend(sorted(pp.rglob('*.md')))
        else:
            files.append(pp)
    return files


def main():
    args = sys.argv[1:]
    audit_path = None
    dry = False
    paths = []
    i = 0
    while i < len(args):
        if args[i] == '--audit':
            audit_path = args[i + 1]
            i += 2
        elif args[i] == '--dry-run':
            dry = True
            i += 1
        else:
            paths.append(args[i])
            i += 1

    stats = {'form1': 0, 'form2': 0, 'form3': 0, 'files': 0}
    audit_rows = []
    for f in collect_files(paths):
        try:
            text = f.read_text(encoding='utf-8')
        except Exception:
            continue
        new_text, audit = convert(text)
        if new_text != text:
            stats['files'] += 1
            for ln, form, old, nw in audit:
                audit_rows.append((str(f), ln, form, old, nw))
                stats[form] += 1
            if not dry:
                f.write_text(new_text, encoding='utf-8')

    if audit_path:
        with open(audit_path, 'w', encoding='utf-8') as fh:
            fh.write('文件\t行号\t形态\t原片段\t修复后\n')
            for fp, ln, form, old, nw in audit_rows:
                fh.write(f'{fp}\t{ln}\t{form}\t{old}\t{nw}\n')
    print(f"改动文件数: {stats['files']}")
    print(f"形态①(×并入$): {stats['form1']}")
    print(f"形态②($外上下标并入): {stats['form2']}")
    print(f"形态③(Φ流比包$): {stats['form3']}")
    print(f"审计条目总数: {len(audit_rows)}")
    if dry:
        print("[dry-run] 未写入文件")


if __name__ == '__main__':
    main()
