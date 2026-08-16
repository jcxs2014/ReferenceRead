#!/usr/bin/env python3
"""check_density.py — 精读内容密度门禁

阈值（基于质量标杆：nomoto=12.7 / drury=7.2 / giacalone=4.4 的下沿）：
  FACT密度 ≥ 4.0 /千字（理论类）
  公式数   ≥ 50（理论类）；豁免：sneden-cowan-2008（观测综述）
  解读批判比 暂不设（误杀率高）

用法：
  python3 scripts/check_density.py [--json]
  python3 scripts/check_density.py --check   # build_all 模式：exit 1 则阻断
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 纯观测/数据类（公式豁免）——必须是观测综述，不含理论模型推导
OBSERVATIONAL = {
    "sneden-cowan-2008",    # 观测丰度综述，公式少
}

# 公式优先理论论文（FACT密度门槛豁免，公式数仍需 ≥50）
FORMULA_FIRST = {
    "amato-blasi-2018",       # 宇宙线加速理论，方程主导
    "weinrich-2020",          # 宇宙线传播模型，方程主导
    "genolini-2021",          # 宇宙线传播理论，方程主导
    "blandford-ostriker-1978", # 激波加速理论，方程密集
    "blandford-eichler-1987",  # 宇宙线加速，方程密集
    "bell-1978",               # 粒子注入理论，方程密集（221公式，26%解读批判）
    "hillas-1984",             # 宇宙线加速综述，方程密集（353公式，27%解读批判）
}

# 阈值（基于质量标杆，不是现状最差值）
THRESHOLDS = {
    "fact_density_min": 4.0,   # 标杆下沿（nomoto=12.7/drury=7.2/giacalone=4.4）
    "formula_min": 50,         # 理论综述类 ≥50 公式（0=系统性缺失）
}


def count_words(text: str) -> int:
    """中英混合分词，word = 连续字母/汉字序列"""
    return len(re.findall(r"[a-zA-Z]{2,}|[\u4e00-\u9fff]", text))


def analyze_lit(dirpath: Path):
    """分析单个 literature_analysis 目录"""
    files = sorted(dirpath.glob("*.md"))
    total_fact = 0
    total_interp = 0
    total_crit = 0
    total_formulas = 0
    total_words = 0

    for fp in files:
        if fp.name in ("00_overview.md",):
            continue
        text = fp.read_text(encoding="utf-8", errors="replace")
        words = count_words(text)
        total_words += words

        total_fact   += len(re.findall(r"\[FACT\]", text))
        total_interp += len(re.findall(r"\[INTERP\]", text))
        total_crit   += len(re.findall(r"\[CRITIQUE\]", text))
        total_formulas += len(re.findall(r"\$[^$]+\$", text))

    tagged = total_fact + total_interp + total_crit
    interp_ratio = (total_interp + total_crit) / tagged if tagged > 0 else 0.0
    fact_density = (total_fact / (total_words / 1000)) if total_words > 0 else 0.0

    return {
        "files": len(files),
        "words": total_words,
        "FACT": total_fact,
        "INTERP": total_interp,
        "CRIT": total_crit,
        "tagged": tagged,
        "formulas": total_formulas,
        "fact_density": fact_density,
        "interp_ratio": interp_ratio,
    }


def check_paper(dirpath: Path) -> dict:
    """返回 pass/fail 及失败原因"""
    d = analyze_lit(dirpath)
    failures = []
    name = dirpath.parent.name
    pure_name = re.sub(r"^\d+_", "", name)
    is_formula_first = pure_name in FORMULA_FIRST
    is_observational = pure_name in OBSERVATIONAL

    if not is_formula_first and d["fact_density"] < THRESHOLDS["fact_density_min"]:
        failures.append(f"FACT密度{d['fact_density']:.1f}<{THRESHOLDS['fact_density_min']}")

    if not is_observational and d["formulas"] < THRESHOLDS["formula_min"]:
        failures.append(f"公式数{d['formulas']}<{THRESHOLDS['formula_min']}")

    return {
        "path": str(dirpath),
        "is_observational": is_observational,
        "is_formula_first": is_formula_first,
        **d,
        "pass": len(failures) == 0,
        "failures": failures,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    ap.add_argument("--check", action="store_true", help="build_all 模式：exit 1 则阻断")
    args = ap.parse_args()

    results = []
    for domain in ["01_cosmic-ray-propagation", "02_cosmic-ray-origins", "03_stellar-nucleosynthesis"]:
        domain_root = ROOT / domain
        if not domain_root.exists():
            continue
        for paper_dir in sorted(domain_root.iterdir()):
            if not paper_dir.is_dir():
                continue
            lit_dir = paper_dir / "literature_analysis"
            if not lit_dir.exists():
                continue
            r = check_paper(lit_dir)
            r["name"] = paper_dir.name
            r["domain"] = domain
            results.append(r)

    fails = [r for r in results if not r["pass"]]

    if args.json:
        import json
        print(json.dumps({"papers": results, "fails": fails}, indent=2, ensure_ascii=False))
        return

    print(f"\n{'='*70}")
    print(f"{'精读密度审计':^60}  (阈值: FACT密度≥4.0/千字, 公式≥50, sneden观测豁免)")
    print(f"{'='*70}")
    print(f"{'论文':<40} {'FACT密度':>8} {'公式':>5} {'解读比':>8} {'判定':>6}")
    print("-"*70)

    for r in results:
        status = "✅" if r["pass"] else "❌"
        tag = ""
        if r.get("is_formula_first"):
            tag = " [公式优先]"
        elif r.get("is_observational"):
            tag = " [观测豁免]"
        print(f"{r['name']:<40} {r['fact_density']:>7.1f} {r['formulas']:>5} "
              f"{r['interp_ratio']:>7.0%} {status:>6}{tag}")
        if not r["pass"]:
            for f in r["failures"]:
                print(f"    ↳ {f}")

    print(f"\n{'='*70}")
    print(f"通过 {len(results)-len(fails)}/{len(results)}  |  失败 {len(fails)}")
    print(f"{'='*70}")

    if fails:
        print("\n失败篇目:")
        for r in fails:
            print(f"  [{r['domain']}] {r['name']}")
            for f in r["failures"]:
                print(f"      - {f}")

    if args.check and fails:
        sys.exit(1)


if __name__ == "__main__":
    main()
