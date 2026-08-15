#!/usr/bin/env python3
"""convert_unicode_math.py — Unicode 数学字符 → LaTeX 批量转换器

用法:
    python3 convert_unicode_math.py <file|dir> [<file2> ...] [--round 1|2] [--audit audit.tsv]

规则（READING_INSTRUCTIONS §7.1 + 公式LaTeX化执行指令.md）:
    第一轮（方案 B）：科学记数法 / 参数下标 → LaTeX；核素 / 单位 / 标记保留 Unicode
    第二轮（全转）：核素 / 单位 / β± / M☉ / 希腊字母 / 数学符号 → LaTeX
                  中文术语内的希腊字母保留（邻侧含 CJK 则不转）

保护机制:
    - frontmatter 状态机（--- 之间不转换）
    - 已有 $..$ 占位保护（不重复处理，保证幂等）
    - 数学符号（×÷≈≠≤≥ 等）默认不自动转（风险高、且多在科学记数法里已转），用 --aggressive 开启裸命令替换（不自动包 $，需人工包 $）
"""
from __future__ import annotations
import argparse, re, sys, pathlib

SUP_MAP = {'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9','⁻':'-','⁺':'+'}
SUB_MAP = {'₀':'0','₁':'1','₂':'2','₃':'3','₄':'4','₅':'5','₆':'6','₇':'7','₈':'8','₉':'9'}
SUP_CHARS = ''.join(SUP_MAP)
SUB_CHARS = ''.join(SUB_MAP)
# 118 个真实化学元素符号（核素识别白名单，避免 B²FH 等缩写误判）
ELEMENTS = {'H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar',
            'K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr',
            'Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe',
            'Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu',
            'Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn',
            'Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr',
            'Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og'}
MATH_MAP = {'×':'\\times','÷':'\\div','≈':'\\approx','≠':'\\neq','≤':'\\leq','≥':'\\geq',
            '±':'\\pm','∝':'\\propto','∞':'\\infty','→':'\\to','←':'\\leftarrow',
            '∂':'\\partial','∇':'\\nabla','∑':'\\sum','∫':'\\int'}
GREEK_MAP = {'α':'\\alpha','β':'\\beta','γ':'\\gamma','δ':'\\delta','ε':'\\epsilon','ζ':'\\zeta',
             'η':'\\eta','θ':'\\theta','ι':'\\iota','κ':'\\kappa','λ':'\\lambda','μ':'\\mu',
             'ν':'\\nu','ξ':'\\xi','ο':'\\omicron','π':'\\pi','ρ':'\\rho','σ':'\\sigma',
             'τ':'\\tau','υ':'\\upsilon','φ':'\\phi','χ':'\\chi','ψ':'\\psi','ω':'\\omega',
             'Α':'\\Alpha','Β':'\\Beta','Γ':'\\Gamma','Δ':'\\Delta','Ε':'\\Epsilon','Ζ':'\\Zeta',
             'Η':'\\Eta','Θ':'\\Theta','Ι':'\\Iota','Κ':'\\Kappa','Λ':'\\Lambda','Μ':'\\Mu',
             'Ν':'\\Nu','Ξ':'\\Xi','Ο':'\\Omicron','Π':'\\Pi','Ρ':'\\Rho','Σ':'\\Sigma',
             'Τ':'\\Tau','Υ':'\\Upsilon','Φ':'\\Phi','Χ':'\\Chi','Ψ':'\\Psi','Ω':'\\Omega'}
GREEK_RE = re.compile(r'([αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ])')
MATH_RE = re.compile(r'[×÷≈≠≤≥±∝∞→←∂∇∑∫]')
CJK = re.compile(r'[一-鿿]')

# 核素：上标质量数 + 元素符号，如 ¹²C ⁸Be ²³⁸U ¹³N
NUCLIDE_RE = re.compile(r'([' + SUP_CHARS + ']+)([A-Z][a-z]?)')
# 科学记数法：系数 × 10ⁿ
SCINOT_X10 = re.compile(r'(\d+(?:\.\d+)?)[×x]([' + SUP_CHARS + ']+)')
# 科学记数法：纯 10ⁿ
SCINOT_PURE = re.compile(r'(?<![A-Za-z$])(\d+(?:\.\d+)?)([' + SUP_CHARS + ']+)(?![A-Za-z])')
# 参数下标：T₉ t₁/₂ T₈（多字母函数名如 log₁₀ 整体识别）
PARAM_SUB = re.compile(r'([A-Za-z]+)([' + SUB_CHARS + r']+)(?:/(\d+))?')
# 数学函数名下标特例（log₁₀ → \log_{10}）
FUNC_MAP = {'log':'\\log','ln':'\\ln','sin':'\\sin','cos':'\\cos','tan':'\\tan',
            'exp':'\\exp','lim':'\\lim','min':'\\min','max':'\\max','det':'\\det','dim':'\\dim'}
def param_repl(m: re.Match) -> str:
    base = m.group(1)
    sub = sub_to_latex(m.group(2))
    suffix = f'/{m.group(3)}' if m.group(3) else ''
    tex = FUNC_MAP.get(base, base)
    return f'${tex}_{{{sub}{suffix}}}$'

def sup_to_latex(s: str) -> str:
    return ''.join(SUP_MAP.get(c, c) for c in s)

def sub_to_latex(s: str) -> str:
    return ''.join(SUB_MAP.get(c, c) for c in s)

def protect_math(text: str) -> tuple[str, list[str]]:
    """已有 $..$ 占位保护（幂等关键）"""
    placeholders: list[str] = []
    def repl(m):
        placeholders.append(m.group(0))
        return f"\x00P{len(placeholders)-1}\x00"
    return re.sub(r'\$[^$]+\$', repl, text), placeholders

def restore_math(text: str, placeholders: list[str]) -> str:
    for i, p in enumerate(placeholders):
        text = text.replace(f"\x00P{i}\x00", p)
    return text

def in_frontmatter(text: str) -> list[bool]:
    lines = text.split('\n')
    res = [False] * len(lines)
    # 仅当首行是 '---' 且其后（前 60 行内）存在闭合 '---' 时才视为 frontmatter。
    # 否则（如正文顶部的装饰性 '---' 无闭合）整体按正文处理，避免误跳过全部转换。
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

def convert_round1(text: str, audit: list[str]) -> str:
    """方案 B：科学记数法 / 参数下标 → LaTeX；核素 / 单位保留"""
    lines = text.split('\n')
    fm = in_frontmatter(text)
    out = []
    for i, line in enumerate(lines):
        if fm[i]:
            out.append(line)
            continue
        orig = line
        line, ph = protect_math(line)
        line = SCINOT_X10.sub(lambda m: f'${m.group(1)}\\times10^{{{sup_to_latex(m.group(2))}}}$', line)
        line = SCINOT_PURE.sub(lambda m: f'${m.group(1)}^{{{sup_to_latex(m.group(2))}}}$', line)
        line = PARAM_SUB.sub(param_repl, line)
        line = restore_math(line, ph)
        if line != orig:
            audit.append(f"{i+1}\t{orig.strip()}\t{line.strip()}\tR1 参数下标/科学记数法")
        out.append(line)
    return '\n'.join(out)

def convert_round2(text: str, audit: list[str], aggressive: bool = False) -> str:
    """全转：核素 / 单位 / β± / M☉ / 希腊字母 / 数学符号（幂等）"""
    lines = text.split('\n')
    fm = in_frontmatter(text)
    out = []
    for i, line in enumerate(lines):
        if fm[i]:
            out.append(line)
            continue
        orig = line
        # 缩写白名单（先替换，避免 ²F 被误当核素）
        line = line.replace('B²FH', 'B$^2$FH').replace('B²F²H', 'B$^2$F$^2$H')
        line, ph = protect_math(line)
        # 核素 ¹²C → $^{12}{\rm C}（仅当后跟真实元素符号）
        line = NUCLIDE_RE.sub(
            lambda m: f'$^{{{sup_to_latex(m.group(1))}}}{{\\rm {m.group(2)}}}$'
                      if m.group(2) in ELEMENTS else m.group(0), line)
        # M☉ → $M_\odot$
        line = line.replace('M☉', '$M_\\odot$')
        # β⁺ β⁻ → $\beta^{+}$ / $\beta^{-}$
        line = re.sub(r'β([⁺⁻])',
                      lambda m: f'$\\beta^{{"+" if m.group(1)=="⁺" else "-"}}$', line)
        # 兜底：参数下标 + 科学记数法（protect 后不重复，幂等安全）
        line = SCINOT_X10.sub(lambda m: f'${m.group(1)}\\times10^{{{sup_to_latex(m.group(2))}}}$', line)
        line = SCINOT_PURE.sub(lambda m: f'${m.group(1)}^{{{sup_to_latex(m.group(2))}}}$', line)
        line = PARAM_SUB.sub(param_repl, line)
        # 希腊字母（中文邻侧保留）
        def greek_repl(m: re.Match) -> str:
            g = m.group(1)
            idx = m.start()
            before = line[idx-1] if idx > 0 else ''
            after = line[idx+1] if idx+1 < len(line) else ''
            if CJK.match(before) or CJK.match(after):
                return g  # 中文术语内，保留 Unicode
            return f'${GREEK_MAP.get(g, g)}$'
        line = GREEK_RE.sub(greek_repl, line)
        # 数学符号（aggressive 仅做裸命令替换，不自动包 $，需人工补 $）
        if aggressive:
            line = MATH_RE.sub(lambda m: MATH_MAP.get(m.group(0), m.group(0)), line)
        line = restore_math(line, ph)
        if line != orig:
            audit.append(f"{i+1}\t{orig.strip()}\t{line.strip()}\tR2 核素/希腊字母/单位")
        out.append(line)
    return '\n'.join(out)

def collect_files(paths: list[str]) -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for p in paths:
        pp = pathlib.Path(p)
        if pp.is_dir():
            files.extend(sorted(pp.rglob('*.md')))
        else:
            files.append(pp)
    return files

def main():
    ap = argparse.ArgumentParser(description='Unicode 数学字符 → LaTeX 批量转换器')
    ap.add_argument('paths', nargs='+', help='文件或目录（目录递归 *.md）')
    ap.add_argument('--round', type=int, default=1, choices=[1, 2])
    ap.add_argument('--audit', default='conversion_audit.tsv')
    ap.add_argument('--aggressive', action='store_true', help='开启数学符号裸命令替换（需人工包 $）')
    args = ap.parse_args()
    files = collect_files(args.paths)
    total_rows: list[str] = []
    for fp in files:
        if '.git' in fp.parts or '.obsidian' in fp.parts:
            continue
        text = fp.read_text(encoding='utf-8')
        rows: list[str] = []
        new = convert_round2(text, rows, args.aggressive) if args.round == 2 else convert_round1(text, rows)
        if new != text:
            fp.write_text(new, encoding='utf-8')
            print(f"[OK] {fp}  ({len(rows)} 处)")
        else:
            print(f"[--] {fp}  (无改动)")
        total_rows.extend(rows)
    if total_rows:
        with open(args.audit, 'w', encoding='utf-8') as f:
            for r in total_rows:
                f.write(r + '\n')
        print(f"审计 {len(total_rows)} 条 → {args.audit}")
    else:
        print("无转换，未写审计。")

if __name__ == '__main__':
    main()
