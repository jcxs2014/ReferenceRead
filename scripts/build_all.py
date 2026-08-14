#!/usr/bin/env python3
"""build_all.py — 全链路编排器

顺序: citations → fm → registry → glossary → index → webapp → pwa → audit

用法:
    python3 build_all.py           # 全量构建
    python3 build_all.py --dry     # dry-run（只打印不写入）
    python3 build_all.py --step fm # 从指定步骤开始（跳过前面的）

依赖:
    python3 需含 PyYAML（用 envs/default venv 或 homebrew python）
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # scripts/ 内，parent.parent = 仓库根
WEBAPP = ROOT / "webapp"

# 检测含 yaml 的 python3
_PREFERRED_PY = shutil.which("python3") or sys.executable


def _detect_python() -> str:
    for py in [_PREFERRED_PY, "/opt/homebrew/bin/python3",
               "/Users/jcxs2014/.workbuddy/binaries/python/envs/default/bin/python3"]:
        if py and _have_yaml(py):
            return py
    return sys.executable


def _have_yaml(py: str) -> bool:
    try:
        r = subprocess.run([py, "-c", "import yaml"], capture_output=True, timeout=5)
        return r.returncode == 0
    except Exception:
        return False


PY = _detect_python()
print(f"[build_all] Using python: {PY}")


# ── Steps ────────────────────────────────────────────────────────────────────
STEPS: list[dict] = [
    {"id": "citations", "cmd": [PY, str(WEBAPP / "build_citations.py"), "--dry-run" if os.environ.get("DRY") else ""],
     "label": "citations"},
    {"id": "fm", "cmd": [PY, str(WEBAPP / "build_fm.py"), "--dry-run" if os.environ.get("DRY") else ""],
     "label": "frontmatter"},
    {"id": "registry", "cmd": [PY, str(WEBAPP / "build_registry.py"), "--dry-run" if os.environ.get("DRY") else ""],
     "label": "registry"},
    {"id": "glossary", "cmd": [PY, str(WEBAPP / "build_glossary.py"), "--dry-run" if os.environ.get("DRY") else ""],
     "label": "glossary"},
    {"id": "index", "cmd": [PY, str(ROOT / "scripts" / "gen_index.py"), "--check"],
     "label": "INDEX.md"},
    {"id": "search_index", "cmd": [PY, str(WEBAPP / "build_search_index.py")],
     "label": "search_index"},
    {"id": "webapp", "cmd": [PY, str(WEBAPP / "build_webapp.py"), "--include-papers"],
     "label": "webapp"},
    {"id": "pwa", "cmd": [PY, str(WEBAPP / "build_pwa.py")],
     "label": "PWA"},
    {"id": "audit", "cmd": [PY, str(WEBAPP / "audit.py")],
     "label": "audit"},
    {"id": "quality", "cmd": [PY, str(ROOT / "scripts" / "quality_matrix.py"), "--check"],
     "label": "quality_matrix"},
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true", help="dry-run 模式（fm/registry/citations 不写入）")
    ap.add_argument("--step", help="从指定步骤开始（跳过前面的），如 --step webapp")
    ap.add_argument("--skip", nargs="*", help="跳过指定步骤，如 --skip pwa audit")
    args = ap.parse_args()

    if args.dry:
        os.environ["DRY"] = "1"

    # 更新 cmd 里的 --dry-run 参数（已经根据 env 设置了）
    start_id = args.step
    skipping = set(args.skip or [])

    for step in STEPS:
        # 更新 cmd（根据 args.dry 重新构建）
        dry_flag = "--dry-run" if args.dry else ""
        if step["id"] == "citations":
            cmd = [PY, str(WEBAPP / "build_citations.py")] + ([dry_flag] if dry_flag else [])
        elif step["id"] == "fm":
            cmd = [PY, str(WEBAPP / "build_fm.py")] + ([dry_flag] if dry_flag else [])
        elif step["id"] == "registry":
            cmd = [PY, str(WEBAPP / "build_registry.py")] + ([dry_flag] if dry_flag else [])
        elif step["id"] == "glossary":
            cmd = [PY, str(WEBAPP / "build_glossary.py")] + ([dry_flag] if dry_flag else [])
        elif step["id"] == "index":
            cmd = [PY, str(ROOT / "scripts" / "gen_index.py"), "--check"]
        elif step["id"] == "search_index":
            cmd = [PY, str(WEBAPP / "build_search_index.py")]
        elif step["id"] == "webapp":
            cmd = [PY, str(WEBAPP / "build_webapp.py"), "--include-papers"]
        elif step["id"] == "pwa":
            cmd = [PY, str(WEBAPP / "build_pwa.py")]
        elif step["id"] == "audit":
            cmd = [PY, str(WEBAPP / "audit.py")]
        else:
            continue

        if start_id and start_id != step["id"]:
            continue
        if step["id"] in skipping:
            print(f"[SKIP]  {step['label']}")
            continue

        print(f"\n[=====] {step['label']}")
        r = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
        if r.stdout.strip():
            print(r.stdout.strip()[-500:])
        if r.stderr.strip():
            print(f"  [stderr] {r.stderr.strip()[-300:]}", file=sys.stderr)
        if r.returncode != 0:
            print(f"[FAIL]  {step['label']} (exit {r.returncode})")
            sys.exit(r.returncode)
        print(f"[PASS]  {step['label']}")

    print("\n[=====] 全部完成 ✅")


if __name__ == "__main__":
    main()