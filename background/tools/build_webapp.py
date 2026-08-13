#!/usr/bin/env python3
"""Build the single-file interactive webapp from background/*.md sources.

Usage:
    python3 build_webapp.py

Output:
    ../background-interactive.html   (single-file, no external deps)
"""
import sys
import json
import re
import html as html_mod
import base64
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
PARENT = HERE.parent  # background/
PAPERS = PARENT.parent  # papers/

SCRIPT = HERE / "md2doc_html.py"

# The 3 background docs in display order
DOCS = [
    ("01_cosmic_rays.md", "宇宙线", "cosmic-rays"),
    ("02_nucleosynthesis.md", "核合成", "nucleosynthesis"),
    ("03_astrophysics.md", "太阳丰度与天体物理", "astrophysics"),
]

# 21 papers metadata (for cross-reference links in the webapp)
PAPERS_META = [
    # (topic_dir, dir_name, label)
    ("01_cosmic-ray-propagation", "0001_strong-moskalenko-ptuskin-2007", "Strong, Moskalenko & Ptuskin (2007)"),
    ("02_cosmic-ray-origins",     "0001_bhattacharjee-sigl-2000",       "Bhattacharjee & Sigl (2000)"),
    ("02_cosmic-ray-origins",     "0002_al-dargazelli-1996",            "Al-Dargazelli et al. (1996)"),
    ("02_cosmic-ray-origins",     "0003_gaisser-1990",                  "Gaisser (1990)"),
    ("02_cosmic-ray-origins",     "0004_blasi-2013",                    "Blasi (2013)"),
    ("02_cosmic-ray-origins",     "0005_amato-2014",                    "Amato (2014)"),
    ("02_cosmic-ray-origins",     "0006_grenier-2015",                  "Grenier, Black & Strong (2015)"),
    ("02_cosmic-ray-origins",     "0007_biermann-1996",                 "Biermann (1996)"),
    ("03_stellar-nucleosynthesis","0001_b2fh-1957",                     "B2FH (1957)"),
    ("03_stellar-nucleosynthesis","0002_trimble-1975",                  "Trimble (1975)"),
    ("03_stellar-nucleosynthesis","0003_fowler-1984",                   "Fowler (1984) Nobel Lecture"),
    ("03_stellar-nucleosynthesis","0004_wallerstein-1997",              "Wallerstein et al. (1997)"),
    ("03_stellar-nucleosynthesis","0005_champagne-wiescher-1992",       "Champagne & Wiescher (1992)"),
    ("03_stellar-nucleosynthesis","0006_anders-grevesse",               "Anders & Grevesse (1989)"),
    ("03_stellar-nucleosynthesis","0007_grevesse-sauval-1998",          "Grevesse & Sauval (1998)"),
    ("03_stellar-nucleosynthesis","0008_lodders-2003",                  "Lodders (2003)"),
    ("03_stellar-nucleosynthesis","0009_asplund-2009-solar-composition","Asplund et al. (2009) AGSS09"),
    ("03_stellar-nucleosynthesis","0010_gies-lambert-1992",             "Gies & Lambert (1992)"),
    ("03_stellar-nucleosynthesis","0011_kewley-2001-starburst",         "Kewley et al. (2001)"),
    ("03_stellar-nucleosynthesis","0012_dieterich-2014-h-burning-limit","Dieterich et al. (2014)"),
    ("03_stellar-nucleosynthesis","0013_bertone-hooper-2018",           "Bertone & Hooper (2018)"),
]

def convert_doc(path: Path):
    """Run md2doc_html.py on the md file, return the HTML body string."""
    tmp = path.with_suffix(".fragment.html")
    r = subprocess.run(
        [sys.executable, str(SCRIPT), str(path), str(tmp)],
        capture_output=True, text=True, cwd=str(HERE)
    )
    if r.returncode != 0:
        raise RuntimeError(f"md2doc_html failed on {path}:\n{r.stderr}")
    return tmp.read_text(encoding="utf-8")

def build():
    fragments = []
    for filename, label, slug in DOCS:
        src = PARENT / filename
        if not src.exists():
            print(f"ERROR: missing {src}")
            sys.exit(1)
        html_body = convert_doc(src)
        fragments.append({
            "label": label,
            "slug": slug,
            "filename": filename,
            "body": html_body,
            "size": len(html_body),
        })
        print(f"  ✓ {filename}: {len(html_body)} chars")

    # Base64 encode each fragment
    for f in fragments:
        f["body_b64"] = base64.b64encode(f["body"].encode()).decode()

    # 21 papers JSON
    papers_json = json.dumps([
        {"topic": t, "dir": d, "label": l}
        for (t, d, l) in PAPERS_META
    ], ensure_ascii=False, indent=2)

    # Build TOC per document (h2+h3 from HTML)
    toc_data = []
    for f in fragments:
        hs = re.findall(r'<h([2-4])\s+id="([^"]+)">(.*?)</h\1>', f["body"], re.S)
        items = []
        for level, aid, title in hs:
            title_clean = re.sub(r"<[^>]+>", "", title).strip()
            items.append({"level": int(level), "id": aid, "title": title_clean})
        toc_data.append({"slug": f["slug"], "items": items})

    toc_json = json.dumps(toc_data, ensure_ascii=False, indent=2)
    frags_json = json.dumps([{k: v for k, v in f.items() if k == "body_b64"} |
                              {"slug": f["slug"], "label": f["label"], "filename": f["filename"], "size": f["size"]}
                             for f in fragments],
                            ensure_ascii=False)

    # Load HTML shell and inject
    shell_src = HERE / "shell.html"
    shell = shell_src.read_text(encoding="utf-8")
    final = shell.replace("__DOCS_JSON__", frags_json) \
                 .replace("__TOC_JSON__", toc_json) \
                 .replace("__PAPERS_JSON__", papers_json)

    assert "__DOCS_JSON__" not in final
    assert "__TOC_JSON__" not in final
    assert "__PAPERS_JSON__" not in final

    out = PARENT / "background-interactive.html"
    out.write_text(final, encoding="utf-8")
    print(f"\nWrote {out} ({len(final)} chars)")

if __name__ == "__main__":
    build()
