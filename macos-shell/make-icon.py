#!/usr/bin/env python3
"""make-icon.py — 为 ReferenceRead.app 生成 macOS 图标 AppIcon.icns。

用法:
    python3 macos-shell/make-icon.py [输出路径.icns]
默认输出: <repo>/macos-shell/AppIcon.icns

图标源（按优先级）:
  1. 调用 webapp/scripts/archive/build_pwa.py 的 draw_icon() 以 1024 重绘。
     该函数是仓库图标的参数化矢量绘制源，各尺寸都清晰；实测重绘结果与仓库现有
     webapp/icon-512.png 外观一致（差异仅重采样抗锯齿，平均每通道 <1/255）。
  2. 退化为把 webapp/icon-512.png 放大到 1024（归档脚本不可用时）。

为什么要留白:
  源图标是满幅 squircle（内容占画布 100%）。macOS 原生 app 图标的内容只占
  824/1024 = 80.5%，四周透明（实测 Calculator 79.3% / Maps 80.1%）。若直接转
  icns，图标在 Dock 里会比邻居大一圈。故须缩到 80.5% 再居中。

为什么要投影:
  macOS 原生图标（Big Sur 之后）自带一层柔和投影，向四周外扩约 4% 画布宽
  （实测 Calculator 512px：实体 406px、含投影 448px，外扩 +21px）。没有投影的
  图标放在系统图标旁会显得「贴平」。这里用图形 alpha 通道做高斯模糊（半径 18，
  即 1.76% 画布）并下移 12px、透明度 30%，实测得 512px 实体 410 / 含投影 450 /
  外扩 +20px，与原生一致。

依赖: Pillow。缺失时打印提示并以 0 退出（调用方据此跳过图标，不影响构建）。
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
WEBAPP = REPO / "webapp"
ARCHIVE = WEBAPP / "scripts" / "archive"

MASTER = 1024
CONTENT_RATIO = 824 / MASTER  # 0.8046875

# 投影参数（按 1024 画布；生成小尺寸时同比例缩放）
SHADOW_BLUR = 18
SHADOW_OFFSET_Y = 12
SHADOW_ALPHA = 0.30

# iconutil 要求的 iconset 文件与像素尺寸（1x + @2x）
ICONSET = [
    ("icon_16x16.png", 16),
    ("icon_16x16@2x.png", 32),
    ("icon_32x32.png", 32),
    ("icon_32x32@2x.png", 64),
    ("icon_128x128.png", 128),
    ("icon_128x128@2x.png", 256),
    ("icon_256x256.png", 256),
    ("icon_256x256@2x.png", 512),
    ("icon_512x512.png", 512),
    ("icon_512x512@2x.png", 1024),
]


def build_master():
    """返回 1024x1024 的 RGBA 主图（满幅，未留白）。"""
    from PIL import Image

    try:
        sys.path.insert(0, str(ARCHIVE))
        import build_pwa  # type: ignore

        tmp = Path(tempfile.mkdtemp()) / "master.png"
        try:
            build_pwa.draw_icon(MASTER, tmp)
            img = Image.open(tmp).convert("RGBA")
        finally:
            shutil.rmtree(tmp.parent, ignore_errors=True)
        print(f"[icon] 主图: 重绘 draw_icon({MASTER})")
        return img
    except Exception as exc:  # 归档脚本被移动 / 缺 Pillow 之外的意外
        src = WEBAPP / "icon-512.png"
        if not src.exists():
            raise SystemExit(f"错误: 无法重绘图标（{exc}），且缺少 {src}")
        print(f"[icon] 主图: 放大 {src.name}（重绘不可用: {exc}）")
        return Image.open(src).convert("RGBA").resize((MASTER, MASTER), Image.LANCZOS)


def compose(size: int, art):
    """把满幅主图缩到 macOS 规范比例，居中放到 size×size 画布，并加原生风格投影。"""
    from PIL import Image, ImageFilter

    content = max(1, round(size * CONTENT_RATIO))
    icon = art.resize((content, content), Image.LANCZOS)
    off = (size - content) // 2
    scale = size / MASTER

    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    # 投影：以图形 alpha 为源，模糊 + 下移 + 降透明度
    if size >= 32:  # 极小尺寸加投影只会糊成一团，原生的投影在此也已几乎不可见
        blur = max(1.0, SHADOW_BLUR * scale)
        alpha = Image.new("L", (size, size), 0)
        alpha.paste(icon.getchannel("A"), (off, off))
        shadow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        shadow.putalpha(alpha.filter(ImageFilter.GaussianBlur(blur)))
        dy = SHADOW_OFFSET_Y * scale
        shadow = shadow.transform(
            shadow.size, Image.AFFINE, (1, 0, 0, 0, 1, -dy), resample=Image.BICUBIC
        )
        shadow.putalpha(shadow.getchannel("A").point(lambda v: int(v * SHADOW_ALPHA)))
        canvas = Image.alpha_composite(canvas, shadow)

    canvas.paste(icon, (off, off), icon)
    return canvas


def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "AppIcon.icns"

    try:
        from PIL import Image
    except ImportError:
        print("[icon] 跳过: 未安装 Pillow（pip3 install Pillow）", file=sys.stderr)
        return 0

    master = build_master()
    iconset = Path(tempfile.mkdtemp(suffix=".iconset"))
    try:
        for name, px in ICONSET:
            compose(px, master).save(iconset / name, "PNG")

        out.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["iconutil", "-c", "icns", str(iconset), "-o", str(out)], check=True)
    finally:
        shutil.rmtree(iconset, ignore_errors=True)

    print(f"[icon] 已生成 {out}（{out.stat().st_size} 字节）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
