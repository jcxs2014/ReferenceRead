#!/usr/bin/env python3
"""Convert background/*.md → HTML fragments for the interactive webapp.
Handles: headings, bold/italic, code (inline & fenced), links, tables, lists, blockquotes, hr.
Preserves $...$ inline math and $$...$$ block math as raw LaTeX for KaTeX runtime rendering.
"""
import re, html, sys
from pathlib import Path

SRC = sys.argv[1] if len(sys.argv) > 1 else ""
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/fragment.html"

def inline_markdown(t_raw):
    """Markdown inline formatting, splitting on $...$ to preserve math unescaped."""
    parts = re.split(r'(\$\$[^$]+\$\$|\$[^$]+\$)', t_raw)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # Math segment
            kind = "block" if part.startswith("$$") and part.endswith("$$") else "inline"
            inner = part[2:-2] if kind == "block" else part[1:-1]
            cls = f'math {"block" if kind=="block" else "inline"}'
            result.append(f'<span class="{cls}">{inner}</span>')
        else:
            s = html.escape(part, quote=False)
            # bold
            s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
            s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", s)
            # code
            s = re.sub(r"`([^`]+?)`", r"<code>\1</code>", s)
            # link
            s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
                       r'<a href="\1" target="_blank" rel="noopener">\1</a>', s)
            result.append(s)
    return "".join(result)

def escape_for_code(text):
    return html.escape(text, quote=False)

def convert(md_text):
    # Strip frontmatter
    md_text = re.sub(r"^---.*?---\n", "", md_text, count=1, flags=re.S)

    lines = md_text.split("\n")
    out = []
    i = 0
    n = len(lines)

    def flush_para(p):
        if p:
            t = " ".join(p).strip()
            if t:
                out.append(f"<p>{inline_markdown(t)}</p>")
        return []

    def flush_table(tbl):
        if not tbl:
            return []
        head = tbl[0]
        body = tbl[1:]
        rows_html = []
        rows_html.append("<thead><tr>" + "".join(f"<th>{inline_markdown(c.strip())}</th>" for c in head) + "</tr></thead>")
        if body:
            rows_html.append("<tbody>")
            for r in body:
                rows_html.append("<tr>" + "".join(f"<td>{inline_markdown(c.strip())}</td>" for c in r) + "</tr>")
            rows_html.append("</tbody>")
        out.append('<div class="doc-table"><table>' + "\n".join(rows_html) + "</table></div>")
        return []

    def flush_list(lst, typ):
        if not lst:
            return [], None
        tag = "ol" if typ == "ol" else "ul"
        out.append(f"<{tag}>")
        for item in lst:
            out.append(f"<li>{inline_markdown(item.strip())}</li>")
        out.append(f"</{tag}>")
        return [], None

    def flush_quote(q):
        if q:
            out.append("<blockquote>" + "".join(inline_markdown(l) + "<br>" for l in q) + "</blockquote>")
        return []

    para_buf = []
    list_buf = []
    list_type = None
    table_buf = []
    quote_buf = []
    in_code = False
    code_buf = []
    code_lang = ""

    while i < n:
        line = lines[i]

        # code fence
        m_fence = re.match(r"^\s*```(.*)", line)
        if m_fence:
            if not in_code:
                flush_para(para_buf); para_buf = []
                flush_list(list_buf, list_type); list_buf, list_type = [], None
                flush_table(table_buf); table_buf = []
                flush_quote(quote_buf); quote_buf = []
                in_code = True
                code_buf = []
                code_lang = m_fence.group(1).strip()
            else:
                lang_class = f' class="lang-{escape_for_code(code_lang)}"' if code_lang else ""
                out.append(f"<pre class='doc-code'{lang_class}><code>{escape_for_code(chr(10).join(code_buf))}</code></pre>")
                in_code = False
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue

        if not line.strip():
            flush_para(para_buf); para_buf = []
            flush_list(list_buf, list_type); list_buf, list_type = [], None
            flush_table(table_buf); table_buf = []
            flush_quote(quote_buf); quote_buf = []
            i += 1
            continue

        # heading
        m_h = re.match(r"^(#{1,6})\s+(.*)", line)
        if m_h:
            level = len(m_h.group(1))
            tag = f"h{min(level+1, 6)}"  # h1→h2 (main page title is h1)
            flush_para(para_buf); para_buf = []
            flush_list(list_buf, list_type); list_buf, list_type = [], None
            flush_table(table_buf); table_buf = []
            flush_quote(quote_buf); quote_buf = []
            txt = m_h.group(2).strip()
            # Remove trailing link target for anchor id
            anchor = re.sub(r"[^\w\u4e00-\u9fff0-9-]+", "-", txt).strip("-").lower()
            out.append(f'<{tag} id="doc-{anchor}">{inline_markdown(txt)}</{tag}>')
            i += 1
            continue

        # hr
        if re.match(r"^\s*-{3,}\s*$", line) or re.match(r"^\s*\*{3,}\s*$", line):
            flush_para(para_buf); para_buf = []
            flush_list(list_buf, list_type); list_buf, list_type = [], None
            flush_table(table_buf); table_buf = []
            flush_quote(quote_buf); quote_buf = []
            out.append("<hr class='doc-hr'>")
            i += 1
            continue

        # table row
        if line.strip().startswith("|") and line.strip().endswith("|"):
            cells = [c for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r"\s*:?-{2,}:?\s*", c) for c in cells):
                i += 1
                continue
            flush_para(para_buf); para_buf = []
            flush_list(list_buf, list_type); list_buf, list_type = [], None
            flush_quote(quote_buf); quote_buf = []
            table_buf.append(cells)
            i += 1
            continue

        # list (ordered)
        m_ol = re.match(r"^\s*(\d+)\.\s+(.*)", line)
        if m_ol:
            flush_para(para_buf); para_buf = []
            flush_table(table_buf); table_buf = []
            flush_quote(quote_buf); quote_buf = []
            if list_type != "ol":
                flush_list(list_buf, list_type); list_buf, list_type = [], None
                list_type = "ol"
            list_buf.append(m_ol.group(2))
            i += 1
            continue

        # list (unordered)
        m_ul = re.match(r"^\s*[-*]\s+(.*)", line)
        if m_ul:
            flush_para(para_buf); para_buf = []
            flush_table(table_buf); table_buf = []
            flush_quote(quote_buf); quote_buf = []
            if list_type != "ul":
                flush_list(list_buf, list_type); list_buf, list_type = [], None
                list_type = "ul"
            list_buf.append(m_ul.group(1))
            i += 1
            continue

        # task list item (checkbox)
        m_task = re.match(r"^\s*[-*]\s+\[([ xX])\]\s+(.*)", line)
        if m_task:
            flush_para(para_buf); para_buf = []
            flush_table(table_buf); table_buf = []
            flush_quote(quote_buf); quote_buf = []
            if list_type != "ul":
                flush_list(list_buf, list_type); list_buf, list_type = [], None
                list_type = "ul"
            checked = m_task.group(1).lower() == "x"
            item = m_task.group(2)
            list_buf.append(f'<input type="checkbox" disabled {"checked" if checked else ""}> {inline_markdown(item)}')
            i += 1
            continue

        # quote
        m_q = re.match(r"^\s*>\s?(.*)", line)
        if m_q:
            flush_para(para_buf); para_buf = []
            flush_list(list_buf, list_type); list_buf, list_type = [], None
            flush_table(table_buf); table_buf = []
            quote_buf.append(m_q.group(1))
            i += 1
            continue

        # normal para
        flush_list(list_buf, list_type); list_buf, list_type = [], None
        flush_table(table_buf); table_buf = []
        flush_quote(quote_buf); quote_buf = []
        para_buf.append(line.strip())
        i += 1

    flush_para(para_buf)
    flush_list(list_buf, list_type)
    flush_table(table_buf)
    flush_quote(quote_buf)
    if in_code and code_buf:
        out.append(f"<pre class='doc-code'><code>{escape_for_code(chr(10).join(code_buf))}</code></pre>")
    return "\n".join(out)

if __name__ == "__main__":
    if not SRC:
        print("Usage: md2doc_html.py <src.md> <out.html>")
        sys.exit(1)
    md = Path(SRC).read_text(encoding="utf-8")
    body = convert(md)
    Path(OUT).parent.mkdir(parents=True, exist_ok=True)
    Path(OUT).write_text(body, encoding="utf-8")
    print(f"Wrote {OUT} ({len(body)} chars)")
