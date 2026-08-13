#!/usr/bin/env python3
"""build_fm.py — 从 00_overview.md 提取 frontmatter 并写入。

遍历 3 个分类目录下所有 NNNN_*/literature_analysis/00_overview.md，
解析元信息表格/列表，合并 git 首次提交日期、citations 等字段，
在文件顶部写入 YAML frontmatter。同时为 6 个 background/*.md 写入 frontmatter。

仅用 Python 3.11 stdlib + PyYAML。
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATEGORY_MAP = {
    "01_cosmic-ray-propagation": "宇宙线传播",
    "02_cosmic-ray-origins": "宇宙线起源",
    "03_stellar-nucleosynthesis": "恒星核合成",
}

# 8 个自动字段
AUTO_FIELDS = ("Title", "Authors", "Year", "Journal", "DOI", "arXiv", "Keywords", "Abstract")

# overview 表格内字段 → frontmatter 字段映射
FIELD_MAP_TABLE = {
    "title": "title",
    "authors": "authors",
    "author": "authors",
    "year": "year",
    "journal": "journal",
    "doi": "doi",
    "arxiv": "arxiv",
    "keywords": "keywords",
    "abstract": "abstract",
    "journal / conference": "journal",
    "journal (published)": "journal",
    "research field": "field",
    "publication date": "year",
}

# bullets 字段名别名
BULLET_ALIASES = {
    "title": "title",
    "authors": "authors",
    "author": "authors",
    "journal": "journal",
    "doi": "doi",
    "arxiv": "arxiv",
    "keywords": "keywords",
    "abstract": "abstract",
}


# ---------------------------------------------------------------------------
# 字段提取
# ---------------------------------------------------------------------------

def _normalize_key(s: str) -> str:
    s = re.sub(r"[*`]", "", s).strip().lower()
    # 中英混用 "字段" header — 不是 field 名称本身，但兜底处理
    return s


def _split_table_row(row: str):
    """拆分 markdown 表格行，返回两列列表。"""
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    if len(cells) < 2:
        return None
    key_raw, val = cells[0], cells[1]
    key = _normalize_key(key_raw)
    if key == "字段" or key == "field":
        return None
    return key, val


def _extract_year(text: str) -> str | None:
    if not text:
        return None
    # 匹配 4 位年份，取第一个
    m = re.search(r"\b(19\d{2}|20\d{2})\b", text)
    return m.group(1) if m else None


def _most_likely_year(text: str) -> str | None:
    """从全文中提取最合理的论文年份（排除 2026）。

    优先策略：
    1. 匹配 "Author & Author (YYYY)" 格式（第一行摘要附近）——代表本文年份
    2. 否则取最早出现的有意义年份
    """
    import re as _re
    # 策略1：找 "Name & Name (YYYY)" 或 "Name (YYYY)" 出现在摘要/导言区域的年份
    # 截取前 2000 字符（通常是摘要区）
    search_area = text[:2000]
    # 匹配 "Anders & Grevesse (1989)", "Burbidge; Burbidge; Fowler; Hoyle (1957)" 等
    m = _re.search(r"\([(\s]*(19[5-9]\d|20[0-2]\d)[)\s]*[,\]]", search_area)
    if m:
        return m.group(1)
    # 策略2：取最早出现的有意义年份
    matches = _re.findall(r"\b(19[5-9]\d|20[0-2]\d)\b", text)
    filtered = [y for y in matches if y != "2026"]
    return filtered[0] if filtered else None


def _extract_abstract(text: str) -> str:
    """从 overview 全文中提取 ## 0.x Abstract / 摘要 段落。"""
    # 常见小节标题
    m = re.search(
        r"##\s+0\.\d+\s*[Aa]bstract.*?(?=\n##\s+0\.\d+\s|\n##\s+\d|---\n)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m:
        return m.group(0).strip()
    m = re.search(r"##\s*[Aa]bstract.*?(?=\n##\s+|\n---\n)", text, re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(0).strip()
    return ""


def _strip_html(s: str) -> str:
    s = re.sub(r"<br\s*/?>", "; ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return s.strip()


def _clean_field(s: str) -> str:
    s = _strip_html(s)
    s = re.sub(r"\s+", " ", s).strip()
    # 去掉末尾多余标点空格
    return s.rstrip("。.;，, ")


def _extract_from_table(text: str) -> dict[str, str]:
    """从 markdown 表格提取元信息。V1/V2 双表时取第一个。"""
    lines = text.splitlines()
    # 找表格起始行：含 `| **Field**` 或 `| **字段**` 的表头
    start = None
    for i, ln in enumerate(lines):
        # 表头：第一列是 "字段"/"项目"/"Field"
        if re.search(r"\|\s*\*{0,2}(Field|字段|项目)\*{0,2}\s*\|\s*(内容|Content)", ln, re.IGNORECASE):
            start = i
            break
    if start is None:
        return {}

    fields: dict[str, str] = {}
    for ln in lines[start + 1 :]:
        if re.search(r"\|\s*\*{0,2}(Field|字段|项目)\*{0,2}\s*\|\s*(内容|Content)", ln, re.IGNORECASE):
            break
        # 跳过纯分隔行
        if re.match(r"^\s*\|[\s:|:-]*\|\s*$", ln):
            continue
        row = _split_table_row(ln)
        if row is None:
            continue
        key, val = row
        key = _normalize_key(key)
        fm_key = FIELD_MAP_TABLE.get(key)
        if fm_key is None:
            first = key.split()[0] if key.split() else ""
            fm_key = FIELD_MAP_TABLE.get(first)
        if fm_key is None:
            continue
        val = _clean_field(val)
        fields[fm_key] = val

    # 若 year 来自日期字段，尝试抽取
    if "year" in fields:
        y = _extract_year(fields["year"])
        if y:
            fields["year"] = y
    if "year" not in fields:
        src = (fields.get("doi", "") + " " + fields.get("journal", ""))
        y = _extract_year(src)
        if y:
            fields["year"] = y
    return fields


def _extract_from_bullets(text: str) -> dict[str, str]:
    """从 bullets `- **Field:** value` 提取元信息。"""
    fields: dict[str, str] = {}
    # 支持单行 `**Key:** value` 和 冒号后到下一行 `**` 之前的多行
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^\s*[-*]\s*\*\*([^*:]+?)\*{0,2}\s*[:：]\s*\*{0,2}\s*(.*)", line)
        if not m:
            i += 1
            continue
        raw_key = _normalize_key(m.group(1))
        fm_key = BULLET_ALIASES.get(raw_key) or BULLET_ALIASES.get(raw_key.split()[0])
        if fm_key is None:
            i += 1
            continue
        val = m.group(2).strip()
        # 若值很短且下一行也是连续内容，多行拼接
        if val and not val.endswith("。") and not val.endswith("."):
            j = i + 1
            while j < len(lines) and not lines[j].lstrip().startswith("- **") and not re.match(r"^#{1,3}\s", lines[j]):
                val += " " + lines[j].strip()
                j += 1
        val = _clean_field(val)
        if fm_key == "year":
            val = _extract_year(val) or val
        fields[fm_key] = val
        i += 1
    # 兜底 year
    if "year" not in fields:
        for k in ("doi", "journal", "arxiv"):
            y = _extract_year(fields.get(k, ""))
            if y:
                fields["year"] = y
                break
    return fields


def extract_fields(text: str) -> dict[str, str]:
    fm = _extract_from_table(text)
    if not fm:
        fm = _extract_from_bullets(text)
    # 提取 abstract（从全文）
    if not fm.get("abstract"):
        fm["abstract"] = _extract_abstract(text)
    return fm


# ---------------------------------------------------------------------------
# Git / 引用辅助
# ---------------------------------------------------------------------------

def git_first_commit_date(path: Path) -> str | None:
    try:
        r = subprocess.run(
            ["git", "log", "--all", "--diff-filter=A", "--format=%aI", "--", str(path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=15,
        )
        lines = [l.strip() for l in r.stdout.splitlines() if l.strip()]
        if lines:
            iso = lines[0][:10]
            return iso
    except Exception:
        return None
    return None


def git_any_commit_date(path: Path) -> str | None:
    try:
        r = subprocess.run(
            ["git", "log", "--format=%aI", "--", str(path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=15,
        )
        lines = [l.strip() for l in r.stdout.splitlines() if l.strip()]
        if lines:
            return lines[0][:10]
    except Exception:
        return None
    return None


def _split_tags(kw: str) -> list[str]:
    if not kw:
        return []
    kw = kw.replace("；", ";").replace("、", ";").replace("，", ";")
    kw = kw.replace(",", ";").replace("；", ";")
    parts = [p.strip().strip("`*").strip() for p in re.split(r"\s*[;·]\s*", kw)]
    tags: list[str] = []
    for p in parts:
        if not p or p == "未提供":
            continue
        p = p.replace("Keywords", "").strip()
        if p:
            tags.append(p)
    return tags


def build_citations(overview_path: Path) -> list[str]:
    """在 literature_analysis/ 目录中寻找 *references*.md，把每个 ref 编号/作者名作为 [[stem]] 链接。"""
    la_dir = overview_path.parent
    refs_files = sorted(la_dir.glob("*references*.md"))
    if not refs_files:
        return []
    # 取第一个 references 文件
    text = refs_files[0].read_text(encoding="utf-8", errors="ignore")
    stems: list[str] = []
    # 尝试从表格行 `(N) Author (Year)` 或 `[N] Author` 提取
    for m in re.finditer(r"\(\s*(\d{1,3})\s*\)\s+([A-Z][^)\n(]{1,60})", text):
        author_part = m.group(2).strip()
        # 简化为作者首字母 + 年份（从原文档或文件名）
        stem = author_part.split(",")[0].split(";")[0].strip().lower().replace(" ", "-")
        # 截到 40 字符
        stem = stem[:40]
        if stem and stem not in stems:
            stems.append(stem)
        if len(stems) >= 20:
            break
    # 若表格抓不到，取整段文字中的首行作者
    if not stems:
        for m in re.finditer(r"^\|\s*\(\s*\d+\s*\)\s*\|\s*\*{0,2}([A-Z][^\n|]{3,50})", text, re.MULTILINE):
            stem = m.group(1).strip().lower().replace(" ", "-")[:40]
            if stem and stem not in stems:
                stems.append(stem)
    if not stems:
        # 再退一步：从 references 文件的标题行抓作者
        mm = re.search(r"(?:属于|by)\s*[:：]\s*([A-Z][^\n.]{3,80})", text)
        if mm:
            stem = mm.group(1).split(",")[0].lower().replace(" ", "-")[:40]
            stems.append(stem)
    # 转为 [[stem]] 链接
    citations = [f"[[{s}]]" for s in stems if s]
    return citations


# ---------------------------------------------------------------------------
# Frontmatter 处理
# ---------------------------------------------------------------------------

def write_fm_to_file(fm: dict, dry_run: bool) -> None:
    """把 fm 写入文件顶部。若文件已有 frontmatter 则替换；否则在顶部插入。"""
    pass


def build_fm(overview_path: Path) -> dict | None:
    """解析 overview，返回完整 fm 字典，失败返回 None。"""
    try:
        text = overview_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[ERR] {overview_path} — read failed: {e}", file=sys.stderr)
        return None

    fields = extract_fields(text)
    # 正文（不含 frontmatter）用于 _most_likely_year
    parts = text.split("---", 2)
    body  = parts[2].lstrip("\n") if len(parts) >= 3 else text
    if not fields.get("title") and not fields.get("authors"):
        print(f"[WARN] {overview_path} — 未能提取元信息字段", file=sys.stderr)
        return None

    # category 映射
    rel = overview_path.relative_to(ROOT)
    category = ""
    for prefix, cn in CATEGORY_MAP.items():
        if str(rel).startswith(prefix):
            category = cn
            break

    # read_date
    rd = git_first_commit_date(overview_path) or git_any_commit_date(overview_path)
    if not rd:
        mtime = overview_path.stat().st_mtime
        rd = dt.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")

    tags = _split_tags(fields.get("keywords", ""))
    citations = build_citations(overview_path)

    fm = {
        "title": fields.get("title", ""),
        "authors": fields.get("authors", ""),
        # 最终 year 兜底：正文优先（正文是最终事实源）
        # frontmatter → parent.parent.stem → 文件名 → 正文
        "year": fields.get("year", "") or _extract_year(overview_path.parent.parent.stem) or _extract_year(overview_path.stem) or _most_likely_year(body) or "",
        "journal": fields.get("journal", ""),
        "doi": fields.get("doi", ""),
        "arxiv": fields.get("arxiv", ""),
        "keywords": fields.get("keywords", ""),
        "abstract": fields.get("abstract", ""),
        "category": category,
        "status": "completed",
        "read_date": rd,
        "lastread": rd,
        "tags": tags,
        "citations": citations,
        "path": str(rel),
    }
    # 移除空字符串，保留空列表
    fm = {k: v for k, v in fm.items() if (v != "" and v is not None) or isinstance(v, list)}
    return fm


def compose_fm_str(overview_path: Path, fm: dict, content: str) -> str:
    """在文件顶部组装 frontmatter；已有则替换。"""
    fm_text = yaml.safe_dump(
        fm, allow_unicode=True, sort_keys=False, default_flow_style=False, width=120
    ).strip()

    lines = content.splitlines()
    # 已有 frontmatter？
    if lines and lines[0].strip() == "---":
        # 找第二个 ---
        end = None
        for i in range(1, min(len(lines), 100)):
            if lines[i].strip() == "---":
                end = i
                break
        if end is not None:
            rest = "\n".join(lines[end + 1 :]).lstrip("\n")
            return f"---\n{fm_text}\n---\n{rest}\n"

    # 没有则顶部插入
    # 但保留开头的引用块（> ...）和 --- 分割线
    if content.startswith(">") or content.startswith("---"):
        # 把 frontmatter 插在最前，然后保留原内容
        return f"---\n{fm_text}\n---\n\n{content}\n"
    return f"---\n{fm_text}\n---\n\n{content}\n"


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def process_overview(overview_path: Path, dry_run: bool) -> bool:
    text = overview_path.read_text(encoding="utf-8")
    fm = build_fm(overview_path)
    if fm is None:
        return False
    new_text = compose_fm_str(overview_path, fm, text)
    if dry_run:
        print(f"[DRY] {overview_path.relative_to(ROOT)}")
        print(f"    title: {fm.get('title','')[:60]}")
        print(f"    category: {fm.get('category','')}")
        print(f"    year: {fm.get('year','')}  read_date: {fm.get('read_date','')}  tags: {len(fm.get('tags',[]))}  citations: {len(fm.get('citations',[]))}")
    else:
        overview_path.write_text(new_text, encoding="utf-8")
        print(f"[OK]  {overview_path.relative_to(ROOT)}")
    return True


def make_background_fm(path: Path) -> dict:
    title = path.stem
    cat = "背景知识"
    rd = git_first_commit_date(path) or git_any_commit_date(path)
    if not rd:
        mtime = path.stat().st_mtime
        rd = dt.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    tags = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", ";", title).split(";")
    tags = [t.strip() for t in tags if t.strip()]
    return {
        "title": title,
        "category": cat,
        "status": "completed",
        "read_date": rd,
        "lastread": rd,
        "tags": tags,
        "citations": [],
        "path": str(path.relative_to(ROOT)),
    }


def process_background(path: Path, dry_run: bool) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[ERR] {path} — {e}", file=sys.stderr)
        return False
    fm = make_background_fm(path)
    new_text = compose_fm_str(path, fm, text)
    if dry_run:
        print(f"[DRY] {path.relative_to(ROOT)}  (bg)")
        print(f"    title: {fm['title']}  read_date: {fm['read_date']}  tags: {fm['tags']}")
    else:
        path.write_text(new_text, encoding="utf-8")
        print(f"[OK]  {path.relative_to(ROOT)}")
    return True


def main() -> None:
    ap = argparse.ArgumentParser(description="Build YAML frontmatter for overview & background files.")
    ap.add_argument("--dry-run", action="store_true", help="只打印，不写入")
    args = ap.parse_args()

    overview_files: list[Path] = []
    for prefix in CATEGORY_MAP:
        d = ROOT / prefix
        if not d.exists():
            print(f"[WARN] category dir not found: {d}", file=sys.stderr)
            continue
        overview_files.extend(sorted(d.rglob("00_overview.md")))
    overview_files = sorted(set(overview_files))

    bg_dir = ROOT / "background"
    bg_files = sorted(bg_dir.glob("*.md")) if bg_dir.exists() else []

    ok, fail = 0, 0
    for p in overview_files:
        try:
            if process_overview(p, args.dry_run):
                ok += 1
            else:
                fail += 1
        except Exception as e:
            print(f"[ERR] {p} — {e}", file=sys.stderr)
            fail += 1

    for p in bg_files:
        try:
            if process_background(p, args.dry_run):
                ok += 1
            else:
                fail += 1
        except Exception as e:
            print(f"[ERR] {p} — {e}", file=sys.stderr)
            fail += 1

    print(f"\n--- 统计 ---")
    print(f"处理了 {ok} 个文件，失败 {fail} 个")


if __name__ == "__main__":
    main()
