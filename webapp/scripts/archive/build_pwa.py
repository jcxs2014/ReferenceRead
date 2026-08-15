#!/usr/bin/env python3
"""build_pwa.py — 生成 PWA 资源：manifest.json + apple-touch-icon.png。

产物（webapp/ 下）：
    manifest.json        — name/short_name/start_url/display/theme_color/icons
    icon-192.png         — Android Chrome
    icon-512.png         — PWA maskable
    apple-touch-icon.png — iOS Safari 180x180

同时在 shell.html <head> 注入：
    <link rel="manifest">
    <link rel="apple-touch-icon">
    <meta name="apple-mobile-web-app-capable">
    <meta name="theme-color">

仅用 stdlib + Pillow（PIL，用于画图标）。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
WEBAPP = ROOT / "webapp"
SHELL = WEBAPP / "shell.html"

NAME = "Papers 知识库"
SHORT_NAME = "Papers"
THEME = "#101418"
BG = "#101418"

ICON_192 = WEBAPP / "icon-192.png"
ICON_512 = WEBAPP / "icon-512.png"
APPLE = WEBAPP / "apple-touch-icon.png"
MANIFEST = WEBAPP / "manifest.json"


def draw_icon(size: int, path: Path) -> None:
    """深色圆角背景 + 白色『文』字。"""
    from PIL import Image, ImageDraw, ImageFont

    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # 圆角矩形背景（macOS 风格圆角 22%）
    radius = int(size * 0.22)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=(16, 20, 24, 255))
    # 『文』字形：五笔结构——点、横、撇、捺 + 十字
    s = size
    accent = (74, 108, 247, 255)     # 主色
    light = (235, 238, 244, 255)     # 文字
    lw = max(3, int(s * 0.075))      # 线宽
    # 横
    d.line([s*0.20, s*0.28, s*0.80, s*0.28], fill=light, width=lw)
    # 撇（左上→中下）
    d.line([s*0.50, s*0.28, s*0.30, s*0.78], fill=light, width=lw)
    # 捺（中→右下）
    d.line([s*0.50, s*0.28, s*0.72, s*0.78], fill=light, width=lw)
    # 点（顶部）
    d.ellipse([s*0.58, s*0.10, s*0.58 + s*0.09, s*0.10 + s*0.09], fill=light)
    # 十字（文的下部交叉：撇捺交叉处横一条）
    d.line([s*0.22, s*0.62, s*0.78, s*0.62], fill=accent, width=lw)
    img.save(path, "PNG")


def inject_head(shell_text: str) -> str:
    """在 </head> 前注入 PWA link/meta。幂等：已有标记则跳过。"""
    if '<link rel="manifest"' in shell_text:
        return shell_text
    block = (
        '    <link rel="manifest" href="manifest.json">\n'
        '    <link rel="apple-touch-icon" href="apple-touch-icon.png">\n'
        '    <link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">\n'
        '    <meta name="apple-mobile-web-app-capable" content="yes">\n'
        '    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n'
        '    <meta name="theme-color" content="' + THEME + '">\n'
    )
    if "</head>" in shell_text:
        return shell_text.replace("</head>", block + "</head>", 1)
    return shell_text


def main() -> int:
    # 1) 图标
    draw_icon(192, ICON_192)
    draw_icon(512, ICON_512)
    draw_icon(180, APPLE)

    # 2) manifest.json
    manifest = {
        "name": NAME,
        "short_name": SHORT_NAME,
        "description": "天体物理/核天体物理论文精读知识库（单文件离线 webapp）",
        "start_url": "interactive.html",
        "scope": ".",
        "display": "standalone",
        "orientation": "any",
        "background_color": BG,
        "theme_color": THEME,
        "icons": [
            {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "icon-512.png", "sizes": "512x512", "type": "image/png",
             "purpose": "any maskable"},
        ],
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # 3) inject shell.html
    shell = SHELL.read_text(encoding="utf-8")
    new_shell = inject_head(shell)
    if new_shell != shell:
        SHELL.write_text(new_shell, encoding="utf-8")
        print("[OK] shell.html 已注入 PWA link/meta")
    else:
        print("[OK] shell.html 已含 PWA 标记（跳过）")

    print(f"[OK] manifest.json ({len(manifest['icons'])} icons)")
    print(f"[OK] icon-192.png / icon-512.png / apple-touch-icon.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())