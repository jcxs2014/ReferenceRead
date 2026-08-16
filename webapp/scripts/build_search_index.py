#!/usr/bin/env python3
"""Build a simple inverted-index for full-text search.

Reads all .md files under papers/, extracts text per doc section,
builds { term -> [slug, section-title, snippet... ] } map, writes
webapp/search_index.json (embedded into interactive.html).

Usage:
    python3 webapp/build_search_index.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
WEBAPP = ROOT / "webapp"
OUT = WEBAPP / "search_index.json"

# docs we index: all papers lit-analysis + background (skip meta like 98/99)
DOC_PATTERNS = [
    "literature_analysis/0[0-9]*_*.md",   # papers: 00-99 per section
    "background/*.md",
]


def _extract_sections(text: str) -> list[dict]:
    """Split markdown into h2/h3 sections with plain-text bodies."""
    lines = text.splitlines()
    sections: list[dict] = []
    current: dict | None = None

    for line in lines:
        h2 = re.match(r"^##\s+(.+)$", line)
        h3 = re.match(r"^###\s+(.+)$", line)
        if h2:
            if current:
                sections.append(current)
            current = {"title": h2.group(1).strip(), "lines": []}
        elif h3 and current:
            sections.append(current)
            current = {"title": h3.group(1).strip(), "lines": []}
        elif current:
            # skip code blocks, frontmatter, images
            if line.strip().startswith("```"):
                continue
            if line.strip().startswith("---"):
                continue
            current["lines"].append(line)

    if current:
        sections.append(current)
    return sections


def _plain(text: str) -> str:
    """Strip markdown formatting to plain text."""
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)      # images
    text = re.sub(r"\[([^\]]*)\]\([^\)]*\)", r"\1", text)  # links
    text = re.sub(r"`[^`]*`", "", text)               # inline code
    text = re.sub(r"\*\*|___|__|\*|\*", "", text)     # emphasis
    text = re.sub(r"<[^>]+>", "", text)               # HTML
    text = re.sub(r"[^\w\u4e00-\u9fff\s]", " ", text) # punctuation
    return text


def _tokenize(text: str) -> list[str]:
    """Tokenize: split on whitespace, keep >=2 char tokens, lowercase."""
    tokens: list[str] = []
    for w in text.split():
        w = w.lower()
        if len(w) >= 2 and not w.isdigit():
            tokens.append(w)
    return tokens


def _slugify(title: str) -> str:
    """标题 → HTML 锚点（与 md2doc_html.py 的 heading anchor 同规则）。"""
    raw = re.sub(r"[^\w\u4e00-\u9fff0-9-]+", "-", title).strip("-").lower()
    if not raw:
        bare = re.sub(r"[^\w\u4e00-\u9fff0-9]+", "-", title).strip("-")
        raw = f"h-{bare.lower()}" if bare else "h"
    return raw


def _snippet(plain: str, term: str, radius: int = 50) -> str:
    """匹配词前后的上下文片段（前后各 radius 字符，… 截断标记）。"""
    idx = plain.lower().find(term)
    if idx == -1:
        return ""
    start = max(0, idx - radius)
    end = min(len(plain), idx + len(term) + radius)
    pre = "…" if start > 0 else ""
    post = "…" if end < len(plain) else ""
    return pre + plain[start:end].strip() + post


def main() -> None:
    index: dict[str, list[dict]] = {}

    for pattern in DOC_PATTERNS:
        for path in sorted(ROOT.glob(pattern)):
            if not path.is_file():
                continue
            rel = str(path.relative_to(ROOT))
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            # Strip YAML frontmatter
            if text.startswith("---"):
                end = text.find("---", 4)
                if end != -1:
                    text = text[end + 4 :]

            sections = _extract_sections(text)
            if not sections:
                # Whole doc as one section
                sections = [{"title": path.stem, "lines": text.splitlines()}]

            for sec in sections:
                body = "\n".join(sec["lines"])
                plain = _plain(body)
                tokens = _tokenize(plain)
                # Deduplicate per section
                seen = set()
                for t in tokens:
                    if t in seen:
                        continue
                    seen.add(t)
                    # Derive slug from path
                    parts = rel.split("/")
                    if len(parts) >= 3:
                        slug = parts[-2] + "/" + parts[-1]
                    else:
                        slug = parts[-1]
                    entry = {
                        "slug": slug,
                        "section": sec["title"][:80],
                        "anchor": _slugify(sec["title"]),   # 标题锚点（前端 scrollIntoView 用）
                        "snippet": _snippet(plain, t),      # 匹配词上下文（前端展示用）
                        "path": rel,
                    }
                    index.setdefault(t, []).append(entry)

    # Limit: top 200 results per term to keep payload small
    for k in index:
        index[k] = index[k][:200]

    data = {
        "count": len(index),
        "total_entries": sum(len(v) for v in index.values()),
        "index": index,
    }

    OUT.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(f"[OK]  {OUT}")
    print(f"      terms: {data['count']}  entries: {data['total_entries']}")


if __name__ == "__main__":
    main()