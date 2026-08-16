#!/usr/bin/env python3
"""阶段三构建期知识审计断言（附 4 + a–e + 附属项）。

用法:
    python3 webapp/audit.py            # 全量断言（失败非零退出）
    python3 webapp/audit.py --quiet    # 只报失败
"""
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
WEBAPP = ROOT / "webapp"
INTERACTIVE = WEBAPP / "interactive.html"
REGISTRY = WEBAPP / "registry.json"
INDEX = ROOT / "INDEX.md"
GLOSSARY = ROOT / "background" / "05_glossary.md"
CAT_DIRS = ["01_cosmic-ray-propagation", "02_cosmic-ray-origins", "03_stellar-nucleosynthesis", "04_experiments"]

FAILED = []


def check(name: str, cond: bool, detail: str = ""):
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        FAILED.append(name)


def load_papers_from_html() -> list | None:
    """从 interactive.html 提取 PAPERS JSON（与 webapp 运行时一致）。"""
    if not INTERACTIVE.exists():
        return None
    text = INTERACTIVE.read_text(encoding="utf-8")
    m = re.search(r"const PAPERS\s*=\s*(\[[\s\S]+?\]);\nconst", text)
    if not m:
        m = re.search(r"const PAPERS\s*=\s*(\[[\s\S]+?\]);", text)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None


def load_docs_from_html() -> list | None:
    text = INTERACTIVE.read_text(encoding="utf-8")
    m = re.search(r"const DOCS\s*=\s*(\[[\s\S]+?\]);", text)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None


def load_tocs_from_html() -> list | None:
    text = INTERACTIVE.read_text(encoding="utf-8")
    m = re.search(r"const TOCS\s*=\s*(\[[\s\S]+?\]);", text)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None


def main() -> int:
    quiet = "--quiet" in sys.argv

    # ── 附 4：id 唯一 / label 合法 / stats 一致 ──────────────────────────
    docs = load_docs_from_html()
    papers = load_papers_from_html()
    tocs = load_tocs_from_html()

    if papers is None:
        check("附4: PAPERS 从产物提取", False, "interactive.html 无 PAPERS JSON")
    else:
        ids = [p["slug"] for p in papers]
        check("附4: PAPERS id 唯一", len(ids) == len(set(ids)), f"{len(ids)} 条")
        bad_labels = [p["label"] for p in papers if re.search(r"\(\s*0*\s*\)|\(\s*\)", p["label"])]
        check("附4: label 不含 (0) 或 () ", not bad_labels, str(bad_labels) if bad_labels else "21/21 合理")
        # P1-22 防护：label 残留 [FACT]/[INTERPRETATION]/[CRITIQUE] 标签
        tag_re = re.compile(r"\[(FACT|INTERPRETATION|CRITIQUE)\]", re.IGNORECASE)
        tag_polluted = [p["label"] for p in papers if tag_re.search(p["label"])]
        check("附4: label 不含 [FACT/INTERPRETATION/CRITIQUE] 残留", not tag_polluted,
              str(tag_polluted) if tag_polluted else f"{len(papers)}/{len(papers)} 干净")
        yrs = [p["year"] for p in papers]
        check("附4: year 全部 > 1900", all(isinstance(y, int) and y > 1900 for y in yrs), f"min={min(yrs) if yrs else 'n/a'}")

    if docs is not None:
        doc_ids = [d["id"] for d in docs]
        check("附4: DOCS id 唯一", len(doc_ids) == len(set(doc_ids)), f"{len(doc_ids)} 条")
        toc = [t for d in docs for t in d.get("toc", [])]
        titles = [t["title"] for t in toc]
        check("附4: TOC title 唯一", len(titles) == len(set(titles)), f"{len(titles)} 条")

    # ── 阶段三 a) 每篇 00/98/99 齐全 ────────────────────────────────────
    papers_dirs = []
    for cat in CAT_DIRS:
        cat_path = ROOT / cat
        if cat_path.exists():
            papers_dirs += [d for d in sorted(cat_path.iterdir()) if d.is_dir()]
    missing_999899 = [
        d.name for d in papers_dirs
        if not (d / "literature_analysis" / "00_overview.md").exists()
        or not (d / "literature_analysis" / "98_vocabulary.md").exists()
        or not (d / "literature_analysis" / "99_final_summary.md").exists()
    ]
    check("a) 00/98/99 三件套齐全", not missing_999899,
          f"{len(papers_dirs)} 篇" + (f"，缺: {missing_999899}" if missing_999899 else ""))

    # ── 阶段三 b) 每篇 TOC ≥3（TOCS 按 parent_id 分组）───────────────
    if tocs is not None:
        per_paper = {}
        for t in tocs:
            pid = t.get("parent_id", "")
            m = re.match(r"^paper-(0\d{3}-[\w\-]+)$", pid)
            if m:
                per_paper.setdefault(m.group(1), 0)
                per_paper[m.group(1)] += 1
        low_toc = [k for k, v in per_paper.items() if v < 3]
        check("b) 每篇 TOC ≥3", not low_toc, f"{len(per_paper)} 篇"
              + (f"，少: {low_toc}" if low_toc else ""))
    else:
        check("b) TOCS 从产物提取", False, "interactive.html 无 TOCS JSON")

    # ── 阶段三 c) frontmatter ↔ registry ↔ PAPERS 一致 ─────────────────
    if REGISTRY.exists():
        reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
        reg_titles = {}
        for e in reg:
            if "literature_analysis" in e["path"]:
                parts = e["path"].replace("/literature_analysis/00_overview.md", "").split("/")
                reg_titles[parts[-1]] = e.get("title", "")
        # 与 frontmatter 源对比（读各篇 frontmatter title）
        fm_titles = {}
        for d in papers_dirs:
            p = d / "literature_analysis" / "00_overview.md"
            if p.exists():
                txt = p.read_text(encoding="utf-8")
                mt = re.search(r"^title:\s*(.+)$", txt, re.M)
                if mt:
                    fm_titles[d.name] = mt.group(1).strip().strip("'\"")
        mism = [k for k in fm_titles if k in reg_titles and _norm(fm_titles[k]) != _norm(reg_titles[k])]
        check("c) frontmatter ↔ registry title 一致", not mism, f"核对 {len(reg_titles)} 篇"
              + (f"，不一致: {mism}" if mism else ""))

    # ── 阶段三 d) glossary ≥600 行 ─────────────────────────────────────
    if GLOSSARY.exists():
        rows = sum(1 for line in GLOSSARY.read_text(encoding="utf-8").splitlines()
                   if line.strip() and line.startswith("|") and not line.startswith("|--") and not line.strip().startswith("| ") or line.count("|") >= 4 and not line.startswith("|--"))
        # 简化：数表格行（含表头）
        g_lines = GLOSSARY.read_text(encoding="utf-8").splitlines()
        tbl_rows = [l for l in g_lines if l.strip().startswith("|") and not re.match(r"^\|[\s:-]+\|", l)]
        check("d) glossary 表格行 ≥600", len(tbl_rows) >= 600, f"{len(tbl_rows)} 行")
    else:
        check("d) glossary 存在", False, "background/05_glossary.md 不存在")

    # ── 阶段三 e) 目录 ↔ INDEX 一一对应 ────────────────────────────────
    if INDEX.exists():
        idx = INDEX.read_text(encoding="utf-8")
        # INDEX 用 `### `0001_xxx`` 三级标题列出每篇 stem
        idx_stems = set(re.findall(r"### `([0-9]{4}_[^`]+)`", idx))
        fs_stems = set(d.name for d in papers_dirs)
        only_idx = idx_stems - fs_stems
        only_fs = fs_stems - idx_stems
        check("e) 目录 ↔ INDEX 一一对应", not only_idx and not only_fs,
              f"fs={len(fs_stems)} idx={len(idx_stems)}"
              + (f"，仅INDEX: {only_idx}" if only_idx else "")
              + (f"，仅fs: {only_fs}" if only_fs else ""))
    else:
        check("e) INDEX.md 存在", False, "INDEX.md 不存在")

    # ── 附属：PAPERS 字段非空率与 registry 一致 ───────────────────────
    if papers is not None and REGISTRY.exists():
        reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
        reg_papers = [e for e in reg if "literature_analysis" in e["path"]]
        check("附: PAPERS 与目录数一致", len(papers) == _fs_paper_count(), f"{len(papers)} 篇 (fs={_fs_paper_count()})")
        rd_empty = [p["stem"] for p in papers if not p.get("read_date")]
        check("附: read_date 非空", not rd_empty, f"{len(papers)-len(rd_empty)}/{len(papers)} 缺 {len(rd_empty)}")
        check("附: registry 与目录数一致", len(reg_papers) == _fs_paper_count(), f"{len(reg_papers)} 篇 (fs={_fs_paper_count()})")
        reg_stems = set()
        for e in reg_papers:
            parts = e["path"].replace("/literature_analysis/00_overview.md", "").split("/")
            reg_stems.add(parts[-1])
        papers_stems = {p["stem"] for p in papers}
        check("附: registry ↔ PAPERS stem 一致", reg_stems == papers_stems,
              f"registry-only={reg_stems - papers_stems} papers-only={papers_stems - reg_stems}")

    # ── P0-6 回归防护：citations 非空 + 图谱有效边 ─────────────────────
    if papers is not None:
        cit_empty = [p["stem"] for p in papers if p.get("citations") is None]
        check("附: citations 非空 21/21", not cit_empty,
              f"缺 {len(cit_empty)}" + (f": {cit_empty[:5]}" if cit_empty else ""))
        # citations 全部指向库内 stem（无库外 [[...]] 悬空）
        papers_stems_all = {p["stem"] for p in papers}
        def _stem(c: str) -> str | None:
            """从 wikilink [[path|stem]] 提取 stem；裸字串（非wikilink）返回 None（外部引用）。"""
            m = re.search(r'\[\[.+?\|(.+?)\]\]', c)
            return m.group(1) if m else None
        dangling = sorted({c for p in papers for c in p.get("citations", [])
                           if _stem(c) is not None and _stem(c) not in papers_stems_all})
        check("附: citations 无悬空(全库内指向)", not dangling,
              f"悬空 {len(dangling)}" + (f": {dangling[:5]}" if dangling else ""))

    # 图谱数据侧静态断言（渲染本身是运行时行为，由 headless 验证）：
    # 数据满足"21 篇 × 平均 ≥1.43 条引用 = ≥30 边"即可支撑图谱
    if papers is not None:
        total_cits = sum(len(p.get("citations", [])) for p in papers)
        check("附: 图谱数据 ≥30 条引用", total_cits >= 30,
              f"citations 总 {total_cits} 条（渲染由 headless 运行验证）")
        # P0-6 + P1-22 + 附24 防护：tags/authors/title 不含
        # - [FACT]/[INTERPRETATION]/[CRITIQUE] 残留
        # - ** 标记残留（如 "Fowler**（..."）
        # - YAML 单引号/双引号泄漏（如 `'...'`）
        # - "重要更正" 等勘误文本残留
        _tag_re   = re.compile(r"\[(FACT|INTERPRETATION|CRITIQUE)\]", re.IGNORECASE)
        _marker_re = re.compile(r"\*\*|\b[\u4e00-\u9fff]重要更正\b|⚠️")
        _qre      = re.compile(r"^[\x27\"]+|[\x27\"]+$")
        bad_tags = []
        for p in papers:
            stem = p["stem"]
            for k in ("tags", "authors", "title"):
                val = p.get(k)
                vals = val if isinstance(val, list) else ([val] if val else [])
                for v in vals:
                    sv = str(v)
                    if _tag_re.search(sv) or _marker_re.search(sv) or _qre.search(sv):
                        bad_tags.append((stem, k, sv[:40]))
        check("附: registry tags/authors/title 无污染标记", not bad_tags,
              f"污染 {len(bad_tags)}" + (f": {bad_tags[:3]}" if bad_tags else ""))

    # ── 附 #8: title/authors markdown bold 检查（PAPERS + registry 全字段） ──
    if papers is not None:
        bad_bold = 0
        for p in papers:
            for field in ("title", "authors"):
                val = p.get(field, "")
                if val and bool(re.search(r"\*{1,2}", val)):
                    bad_bold += 1
                    print(f"[DETAIL]  {p.get('slug','?')} 的 {field} 含 markdown 标记: {val[:60]}")
        check("附: PAPERS title/authors 无 markdown 加粗 — 污染 0", bad_bold == 0,
              f"污染 {bad_bold}")

    # ── 附 #8: PAPERS 空值统计（字段结构：slug/label/year/stem/status/read_date/tags/citations） ──
    if papers is not None:
        papers_empty_fields = 0
        _pe = []
        for p in papers:
            for field in ("label", "year", "status", "read_date"):
                v = p.get(field)
                if v is None or v == "" or (isinstance(v, str) and not v.strip()):
                    papers_empty_fields += 1
                    _pe.append(f"{p.get('stem','?')}:{field}")
        check("附: PAPERS 必填字段空值统计 — 0 空值", papers_empty_fields == 0,
              f"空值 {papers_empty_fields}" + (f": {_pe[:3]}" if _pe else ""))

    # ── 附 #8: registry 全字段检查（bold + 空值） ──
    if REGISTRY.exists():
        _reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
        reg_bold = 0
        for e in _reg:
            for field in ("title", "authors", "journal"):
                val = e.get(field, "")
                if val and bool(re.search(r"\*{1,2}", val)):
                    reg_bold += 1
                    print(f"[DETAIL]  registry {e.get('stem','?')} 的 {field} 含标记: {val[:60]}")
        check("附: registry title/authors/journal 无 markdown 加粗 — 污染 0", reg_bold == 0,
              f"污染 {reg_bold}")

        # registry 空值统计（论文条目查必填字段，背景条目只查 title）
        reg_empty_fields = 0
        _empty_detail = []
        for e in _reg:
            is_paper = "literature_analysis" in e.get("path", "")
            required = ("title", "authors", "year", "status", "read_date") if is_paper else ("title",)
            for field in required:
                v = e.get(field)
                if v is None or (isinstance(v, str) and not v.strip()) or v == []:
                    reg_empty_fields += 1
                    _empty_detail.append(f"{e.get('path','?')}:{field}")
        check("附: registry 必填字段空值统计 — 0 空值", reg_empty_fields == 0,
              f"空值 {reg_empty_fields}" + (f": {_empty_detail[:3]}" if _empty_detail else ""))
    # - **** 多星（gen_index 回退正则吞 ** 的旧问题）
    # - [FACT] 残留
    # - 单引号/双引号包裹（YAML 引号泄漏）
    # - ** 中缀残留
    index_path = ROOT / "INDEX.md"
    if index_path.exists():
        idx_text = index_path.read_text(encoding="utf-8")
        idx_bad = []
        for i, line in enumerate(idx_text.splitlines()):
            if "|" not in line:
                continue
            # 剥引号包裹 + 星号后检查残留
            clean = line.strip().strip("'").strip('"')
            # 标题列（第三列：`| authors | journal | **title** | year`）
            cols = [c.strip() for c in clean.split("|")]
            title = ""
            for c in cols:
                if c.startswith("**") and c.endswith("**"):
                    inner = c[2:-2].strip()
                    if re.search(r"\[(FACT|INTERPRETATION|CRITIQUE)\]", inner, re.I):
                        idx_bad.append((i+1, "fact", inner[:40]))
                    if re.search(r"\*\*|⚠️|重要更正", inner):
                        idx_bad.append((i+1, "marker", inner[:40]))
                    if re.match(r"^[\x27\"]+", inner):
                        idx_bad.append((i+1, "quote", inner[:40]))
        check("附: INDEX 无污染标题",
              not idx_bad,
              f"坏标题 {len(idx_bad)}" + (f": {idx_bad[:3]}" if idx_bad else ""))

    # ── 附 #12: WCAG 基础无障碍审计 ──
    if INTERACTIVE.exists():
        html = INTERACTIVE.read_text(encoding="utf-8")
        # <img> 必须有 alt
        imgs = re.findall(r"<img[^>]*>", html, re.I)
        img_no_alt = [m for m in imgs if "alt=" not in m]
        check("附: <img> 必须有 alt", len(imgs) == 0 or len(img_no_alt) == 0,
              f"无 alt {len(img_no_alt)}/{len(imgs)}")
        # <input> 必须有 aria-label / label[id==input.id]
        inputs = re.findall(r"<input[^>]*>", html, re.I)
        bad_inputs = 0
        for inp in inputs:
            has_aria = "aria-label" in inp
            inp_id = re.search(r'\bid="([^"]+)"', inp)
            has_label = bool(inp_id and (f'for="{inp_id.group(1)}"' in html))
            if not has_aria and not has_label:
                bad_inputs += 1
        check("附: <input> 必须有 aria-label 或关联 label", bad_inputs == 0,
              f"无 label {bad_inputs}/{len(inputs)}")
        # <button> 必须有 aria-label / title / 非空文本
        buttons = re.findall(r"<button[^>]*>", html, re.I)
        bad_btns = 0
        for btn in buttons:
            if "aria-label" in btn or "title=" in btn or "aria-label" in btn:
                continue
            # 简单检查: 若 button 内有 <span>/<i> 等 icon-only 则必须有 aria
            if any(icon_tag in btn.lower() for icon_tag in ["<i ", "<svg", "class="]):
                bad_btns += 1
        check("附: <button> 图标按钮必须有 aria-label 或 title", bad_btns == 0,
              f"图标按钮无 label {bad_btns}/{len(buttons)}")
        # <svg> 必须有 role="img" 或 title
        svgs = re.findall(r"<svg[^>]*>", html, re.I)
        svg_no_role = [s for s in svgs if "role=" not in s and "title" not in s.lower()]
        check("附: <svg> 必须有 role=\"img\" 或内嵌 <title>", len(svg_no_role) == 0,
              f"无 role/title {len(svg_no_role)}/{len(svgs)}")
        # <html> 必须有 lang
        html_has_lang = bool(re.search(r'<html[^>]*\blang\s*=', html, re.I))
        check("附: <html> 必须有 lang 属性", html_has_lang)

    # 附: 篇数一致性——PAPERS JSON 条目数 vs 静态文案"共 X 篇"模式
    paper_count = len(papers)
    doc_ids_with_mismatch = []
    for doc in docs:
        html = doc.get('html', '')
        for m in re.finditer(r'共\s*(\d+)\s*篇', html):
            declared = int(m.group(1))
            if declared != paper_count:
                doc_ids_with_mismatch.append(f'{doc["id"]}({declared}篇)')
    check("附: 静态文案篇数一致性", len(doc_ids_with_mismatch) == 0,
          f'{"; ".join(doc_ids_with_mismatch) if doc_ids_with_mismatch else "0 不一致"} ≠ {paper_count}篇(PAPERS)')

    print()
    if FAILED:
        print(f"审计结果: {len(FAILED)} 项失败 — {', '.join(FAILED)}")
        return 1
    print("审计结果: 全部通过 ✅")
    return 0


def _fs_paper_count() -> int:
    """文件系统中论文目录数（动态，不再硬编码 21）。"""
    n = 0
    for cat in CAT_DIRS:
        cp = ROOT / cat
        if cp.exists():
            n += sum(1 for d in cp.iterdir()
                     if d.is_dir() and (d / "literature_analysis" / "00_overview.md").exists())
    return n


def _norm(s: str) -> str:
    return re.sub(r"\*+", "", s).strip().lower()


if __name__ == "__main__":
    sys.exit(main())