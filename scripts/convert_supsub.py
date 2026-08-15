#!/usr/bin/env python3
"""
convert_supsub.py — Unicode 上标/下标 → LaTeX（清零库内 Unicode 上下标）

范围（见 docs/公式上下标LaTeX化执行指令.md）：
  所有残留 Unicode 上标(⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁽⁾ⁿ) / 下标(₀₁₂₃₄₅₆₇₈₉₊₋₍₎ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ)
  → LaTeX ^{..} / _{..}。基底留数学模式外作文本；已处 $..$ 内只插 ^{..}。

铁律：
  - 数字零变化（Unicode 数字归一 ASCII，值不变）
  - $ 配对完整（每行 $ 偶数）
  - 幂等（重复运行零新增）
  - 无残留 Unicode 上下标
  - 不动 frontmatter；跳过 $$ 显示公式

用法：
  python3 convert_supsub.py [--audit FILE] [--dry-run] PATH [PATH ...]
  PATH 可为文件或目录（目录递归 *.md）。
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

# 跨 $ 边界的欧式小数点修复：前置转换曾把 10¹⁷·⁵ 拆成 $10^{17}$·$^{5}$。
# 仅当指数前为数字（即数字的指数）时才合并，避免误并乘式 a²·³ 之类。
DECIMAL_REPAIR = re.compile(r'(\d)\^\{(\d+)\}\$\s*·\$\^\{(\d+)\}\$')

# 希腊字母（仅作为上下标基底时一并转，如 β⁺ → $\beta^{+}$）
GREEK_MAP = {
    'α': '\\alpha', 'β': '\\beta', 'γ': '\\gamma', 'δ': '\\delta', 'ε': '\\epsilon',
    'ζ': '\\zeta', 'η': '\\eta', 'θ': '\\theta', 'ι': '\\iota', 'κ': '\\kappa',
    'λ': '\\lambda', 'μ': '\\mu', 'ν': '\\nu', 'ξ': '\\xi', 'ο': '\\omicron',
    'π': '\\pi', 'ρ': '\\rho', 'σ': '\\sigma', 'τ': '\\tau', 'υ': '\\upsilon',
    'φ': '\\phi', 'χ': '\\chi', 'ψ': '\\psi', 'ω': '\\omega',
    'Α': '\\Alpha', 'Β': '\\Beta', 'Γ': '\\Gamma', 'Δ': '\\Delta', 'Ε': '\\Epsilon',
    'Ζ': '\\Zeta', 'Η': '\\Eta', 'Θ': '\\Theta', 'Ι': '\\Iota', 'Κ': '\\Kappa',
    'Λ': '\\Lambda', 'Μ': '\\Mu', 'Ν': '\\Nu', 'Ξ': '\\Xi', 'Ο': '\\Omicron',
    'Π': '\\Pi', 'Ρ': '\\Rho', 'Σ': '\\Sigma', 'Τ': '\\Tau', 'Υ': '\\Upsilon',
    'Φ': '\\Phi', 'Χ': '\\Chi', 'Ψ': '\\Psi', 'Ω': '\\Omega',
}

# 同位素元素白名单（118 种真实元素符号，避免 B²FH 等缩写误判）
ELEMENTS = {
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si',
    'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
    'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb',
    'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
    'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho',
    'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
    'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np',
    'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg',
    'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og',
}


# ---------- frontmatter 状态机（无闭合 --- 视为正文） ----------
def in_frontmatter(text):
    lines = text.split('\n')
    res = [False] * len(lines)
    if not lines or lines[0].strip() != '---':
        return res
    close = None
    for j in range(1, min(len(lines), 60)):
        if lines[j].strip() == '---':
            close = j
            break
    if close is None:
        return res
    for i in range(close + 1):
        res[i] = True
    return res


def is_uncertainty(line, i, prev_src):
    """不确定度记法（±²/₋₄ 之类）跳过，不机械处理。"""
    if prev_src == '±':
        return True
    if prev_src == '/' and '±' in line[max(0, i - 8):i]:
        return True
    return False


def convert_line(line):
    """单行转换；返回 (new_line, changes)。changes: list of (form, old, new)。

    注意：`$` 逐个切换奇偶（不把相邻行内公式的 $$ 误判为显示公式）。
    显示公式（$$ 独占一行）的跳过由 convert() 的 in_display 状态机负责。
    """
    out = []
    i = 0
    n = len(line)
    parity = 0          # 单 $ 奇偶
    changes = []
    while i < n:
        if line[i] == '$':
            parity ^= 1
            out.append('$')
            i += 1
            continue
        if line[i] in UNI_SUPSUB:
            j = i
            while j < n and line[j] in UNI_SUPSUB:
                j += 1
            # 欧式小数点 ·（如 E⁻²·⁷ = E^{-2.7}）：仅当上标数字后紧跟 ·+上标数字时并入同一指数
            while (j + 1 < n and line[j] == '·' and line[j + 1] in SUP_MAP
                   and line[j + 1].isdigit() and line[i] in SUP_MAP):
                j += 1
                while j < n and line[j] in UNI_SUPSUB:
                    j += 1
            run = line[i:j]
            prev_src = line[i - 1] if i > 0 else ''
            if '·' in run:
                # 十进制指数：整体作上标，· 替换为 .
                norm = ''.join(SUP_MAP.get(c, SUB_MAP.get(c, ('.' if c == '·' else c))) for c in run)
                blocks = [('^', norm)]
            else:
                # 拆分同类连续段（处理 ₃⁺ 这类上下标相邻）
                blocks = []
                k = 0
                while k < len(run):
                    c0 = run[k]
                    sup0 = c0 in SUP_MAP
                    m = k
                    while m < len(run) and (run[m] in SUP_MAP) == sup0:
                        m += 1
                    seg = run[k:m]
                    norm = ''.join(SUP_MAP.get(x, SUB_MAP.get(x, x)) for x in seg)
                    blocks.append(('^' if sup0 else '_', norm))
                    k = m
            inner = ''.join(f'{kk}{{{nm}}}' for kk, nm in blocks)

            # 不确定度排除
            if is_uncertainty(line, i, prev_src):
                out.append(run)
                changes.append(('skip', prev_src + run if prev_src else run, run))
                i = j
                continue

            # 同位素：前置上标 + 元素符号（基底非字母数字，且其后为元素）
            if blocks[0][0] == '^' and (i == 0 or not prev_src.isalnum()):
                el = None
                for L in (2, 1):
                    cand = line[j:j + L]
                    if cand in ELEMENTS:
                        el = cand
                        break
                if el:
                    if parity % 2 == 1:
                        repl = f'^{{{blocks[0][1]}}}{{\\rm {el}}}'
                    else:
                        repl = f'$^{{{blocks[0][1]}}}{{\\rm {el}}}$'
                    oldseg = line[i:j + len(el)]
                    out.append(repl)
                    changes.append(('isotope', oldseg, repl))
                    i = j + len(el)
                    continue

            # 希腊字母基底（β⁺ → $\beta^{+}$）
            if prev_src in GREEK_MAP:
                gl = GREEK_MAP[prev_src]
                if parity % 2 == 1:
                    repl = gl + inner
                else:
                    repl = '$' + gl + inner + '$'
                if out and out[-1] == prev_src:
                    out.pop()
                out.append(repl)
                changes.append(('supsub-greek', prev_src + run, repl))
                i = j
                continue

            # 普通基底（基底留文本，上下标进数学模式）
            if parity % 2 == 1:
                repl = inner
            else:
                repl = '$' + inner + '$'
            out.append(repl)
            changes.append(('supsub', run, repl))
            i = j
            continue

        out.append(line[i])
        i += 1
    return ''.join(out), changes


def repair_decimal(line):
    """修复跨 $ 边界的欧式小数点：10^{17}$·$^{5}$ → 10^{17.5}$。

    仅匹配「数字指数}$·$^{数字」形态——这只能是前置转换把 10¹⁷·⁵ 拆错
    的残留，绝不会由新文本产生（新文本由 in-run 欧式修复在单 run 内合并），
    故安全。返回 (new_line, [(old, new), ...])。
    """
    repairs = []

    def _sub(m):
        d, a, b = m.group(1), m.group(2), m.group(3)
        old = m.group(0)
        new = '%s^{%s.%s}$' % (d, a, b)
        repairs.append((old, new))
        return new

    new_line = DECIMAL_REPAIR.sub(_sub, line)
    return new_line, repairs


def convert(text):
    lines = text.split('\n')
    fm = in_frontmatter(text)
    audit = []
    out_lines = []
    in_display = False    # 跨行显示公式状态机（仅整行 $$ 才是边界）
    for idx, line in enumerate(lines):
        if fm[idx]:
            out_lines.append(line)
            continue
        stripped = line.strip()
        if in_display:
            # 显示公式内部行：不转换（可能含合法前置上下标如 ^7Li）
            if stripped == '$$':
                in_display = False
            out_lines.append(line)
            continue
        if stripped == '$$':
            # 整行 $$：显示公式开口/闭口边界行，跳过
            in_display = True
            out_lines.append(line)
            continue
        new_line, c = convert_line(line)
        for form, old, new in c:
            audit.append((idx + 1, form, old, new))
        # 跨 $ 边界欧式小数点修复（10^{17}$·$^{5}$ → 10^{17.5}）
        new_line, dec_repairs = repair_decimal(new_line)
        for old, new in dec_repairs:
            audit.append((idx + 1, 'supsub-decimal', old, new))
        out_lines.append(new_line)
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

    stats = {'supsub': 0, 'isotope': 0, 'supsub-greek': 0, 'supsub-decimal': 0, 'skip': 0, 'files': 0}
    audit_rows = []
    for f in collect_files(paths):
        try:
            text = f.read_text(encoding='utf-8')
        except Exception:
            continue
        new_text, audit = convert(text)
        if new_text != text:
            stats['files'] += 1
            for ln, form, old, new in audit:
                audit_rows.append((str(f), ln, form, old, new))
                if form in stats:
                    stats[form] += 1
            if not dry:
                f.write_text(new_text, encoding='utf-8')

    if audit_path:
        with open(audit_path, 'w', encoding='utf-8') as fh:
            fh.write('文件\t行号\t形态\t原片段\t修复后\n')
            for fp, ln, form, old, new in audit_rows:
                fh.write(f'{fp}\t{ln}\t{form}\t{old}\t{new}\n')
    print(f"改动文件数: {stats['files']}")
    print(f"上下标(supsub): {stats['supsub']}")
    print(f"同位素(isotope): {stats['isotope']}")
    print(f"希腊基底(supsub-greek): {stats['supsub-greek']}")
    print(f"跨$小数点(supsub-decimal): {stats['supsub-decimal']}")
    print(f"跳过(uncertainty等): {stats['skip']}")
    print(f"审计条目总数: {len(audit_rows)}")
    if dry:
        print("[dry-run] 未写入文件")


if __name__ == '__main__':
    main()
