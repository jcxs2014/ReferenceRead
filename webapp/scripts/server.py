#!/usr/bin/env python3
"""形态 B 薄服务层：静态服务 webapp + 进度 API。

用法:
    python3 webapp/server.py [--port 8747] [--host 127.0.0.1]

端点:
    /                      → webapp/interactive.html（静态）
    /api/progress?slug=X   → GET 读 X/literature_analysis/00_overview.md frontmatter
                            的 status/lastread/read_date（JSON）
    /api/progress          → GET 全部 21 篇进度（JSON）
    /api/rebuild           → POST/SET 跑 build_registry.py + build_webapp.py（一键重建）

slug 契约:
    API 的 slug = 论文**目录名**，下划线分隔：`0003_fowler-1984`（stem 格式）。
    注意与 webapp 产物内 id 不同（`paper-0003-fowler-1984`，连字符）——
    前端集成时需转换：`slug.replace("_", "-")` → `paper-${that}`。

rebuild 顺序依赖:
    registry (build_registry.py) 失败 → 跳过 webapp 构建，返回 500 + registry_failed:true，
    杜绝"webapp 用旧 registry 重建成功"的静默半成功。

进度数据在**源 md frontmatter**（唯一事实源），registry 是派生物、不参与进度读取。
"""
import json
import re
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
WEBAPP = ROOT / "webapp"
INTERACTIVE = WEBAPP / "interactive.html"
CAT_DIRS = ["01_cosmic-ray-propagation", "02_cosmic-ray-origins", "03_stellar-nucleosynthesis"]

_PORT = 8747
_HOST = "127.0.0.1"


def parse_frontmatter_text(text: str) -> dict:
    """极简 frontmatter 解析（无第三方依赖，够读 status/lastread/read_date）。"""
    result = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return result
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip().strip("'\"")
            result[key] = val
    return result


def progress_all() -> list[dict]:
    entries = []
    for cat in CAT_DIRS:
        cat_path = ROOT / cat
        if not cat_path.exists():
            continue
        for d in sorted(cat_path.iterdir()):
            if not d.is_dir():
                continue
            p = d / "literature_analysis" / "00_overview.md"
            if not p.exists():
                continue
            fm = parse_frontmatter_text(p.read_text(encoding="utf-8"))
            entries.append({
                "stem": d.name,
                "status": fm.get("status", "planned"),
                "lastread": fm.get("lastread", ""),
                "read_date": fm.get("read_date", ""),
                "title": fm.get("title", ""),
            })
    return entries


class Handler(BaseHTTPRequestHandler):
    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _text(self, body: bytes, ctype: str, code=200):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?")[0]
        query = self.path.split("?", 1)[1] if "?" in self.path else ""
        params = dict(kv.split("=", 1) for kv in query.split("&") if "=" in kv)

        if path == "/" or path == "/index.html":
            if not INTERACTIVE.exists():
                self._text(b"interactive.html not built", "text/plain; charset=utf-8", 500)
                return
            self._text(INTERACTIVE.read_bytes(), "text/html; charset=utf-8")
            return

        if path == "/api/progress":
            slug = params.get("slug")
            all_progress = progress_all()
            if slug:
                hit = [e for e in all_progress if e["stem"] == slug]
                if not hit:
                    self._json({"error": "not found", "slug": slug}, 404)
                    return
                self._json(hit[0])
                return
            self._json({"papers": all_progress, "total": len(all_progress)})
            return

        if path == "/api/rebuild":
            self._json({"error": "use POST /api/rebuild"}, 405)
            return

        # 其余静态资源（前缀 /assets 等）
        self._text(b"not found", "text/plain; charset=utf-8", 404)

    def do_POST(self):
        path = self.path.split("?")[0]
        if path == "/api/rebuild":
            try:
                r1 = subprocess.run(
                    [sys.executable, str(WEBAPP / "build_registry.py")],
                    cwd=ROOT, capture_output=True, text=True, timeout=120)
                # 顺序依赖：registry 失败 → 跳过 webapp 构建（防静默半成功）
                if r1.returncode != 0:
                    self._json({
                        "ok": False,
                        "registry_failed": True,
                        "webapp_skipped": True,
                        "registry_rc": r1.returncode,
                        "registry_tail": (r1.stderr or r1.stdout).strip()[-500:],
                        "hint": "build_registry 失败（常见：当前 Python 无 PyYAML）。"
                                "修复环境后重试：python3 -m pip install pyyaml 或改用含 yaml 的解释器",
                    }, 500)
                    return
                r2 = subprocess.run(
                    [sys.executable, str(WEBAPP / "build_webapp.py"), "--include-papers"],
                    cwd=ROOT, capture_output=True, text=True, timeout=300)
                ok = r2.returncode == 0
                self._json({
                    "ok": ok,
                    "registry_failed": False,
                    "registry_rc": r1.returncode,
                    "webapp_rc": r2.returncode,
                    "registry_tail": (r1.stderr or r1.stdout).strip()[-300:],
                    "webapp_tail": (r2.stderr or r2.stdout).strip()[-300:],
                }, 200 if ok else 500)
            except subprocess.TimeoutExpired:
                self._json({"ok": False, "error": "timeout"}, 500)
            return
        self._json({"error": "not found"}, 404)

    def log_message(self, format, *args):
        sys.stderr.write("[server] " + (format % args) + "\n")


def main():
    global _PORT, _HOST
    # 启动自检：rebuild 依赖的 yaml 若缺失，立即暴露（而非 rebuild 时才炸）
    try:
        import yaml  # noqa: F401
    except ImportError:
        print("[FATAL] 当前解释器缺少 PyYAML，/api/rebuild 将无法工作。", file=sys.stderr)
        print("        请用含 yaml 的 Python 启动，例如：", file=sys.stderr)
        print("          python3 -m pip install pyyaml    # 或", file=sys.stderr)
        print("          ~/.hermes/hermes-agent/venv/bin/python3 webapp/server.py", file=sys.stderr)
        sys.exit(2)
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--port" and i + 1 < len(args):
            _PORT = int(args[i + 1])
        if a == "--host" and i + 1 < len(args):
            _HOST = args[i + 1]
    server = ThreadingHTTPServer((_HOST, _PORT), Handler)
    print(f"形态 B 服务层: http://{_HOST}:{_PORT}/  (进度 API: /api/progress?slug=<stem>)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main()