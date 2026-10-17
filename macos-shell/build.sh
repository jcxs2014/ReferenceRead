#!/usr/bin/env bash
# 构建 ReferenceRead.app（极简壳）
# 用法: ./build.sh            仅编译出 .app（不内嵌 webapp，运行时读仓库里的 ../webapp）
#       ./build.sh --bundle   额外把 webapp 拷进 .app，得到可独立分发的包
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(dirname "$HERE")"
APP="$REPO/ReferenceRead.app"
MC="$HERE/.module-cache"
SRC="$REPO/webapp"

BUNDLE_WEBAPP=0
[ "${1:-}" = "--bundle" ] && BUNDLE_WEBAPP=1

[ -f "$SRC/interactive.html" ] || { echo "错误: 找不到载荷 $SRC/interactive.html" >&2; exit 1; }

echo "==> 编译 Swift"
mkdir -p "$MC"
swiftc -O -module-cache-path "$MC" \
  -framework Cocoa -framework WebKit \
  -o "$HERE/ReferenceRead" "$HERE/ReferenceRead.swift"

echo "==> 组装 $APP"
rm -rf "$APP"
mkdir -p "$APP/Contents/MacOS" "$APP/Contents/Resources"
cp "$HERE/ReferenceRead" "$APP/Contents/MacOS/ReferenceRead"

echo "==> 生成图标"
# make-icon.py 每次重绘（幂等，约 0.3s）；Pillow 缺失时它自行跳过并返回 0。
ICNS="$HERE/AppIcon.icns"
if ! python3 "$HERE/make-icon.py" "$ICNS"; then
  echo "    警告: 图标生成失败，$APP 将使用系统默认图标" >&2
fi
if [ -f "$ICNS" ]; then
  cp "$ICNS" "$APP/Contents/Resources/AppIcon.icns"
fi

cat > "$APP/Contents/Info.plist" <<'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>CFBundleName</key><string>ReferenceRead</string>
  <key>CFBundleDisplayName</key><string>papers 知识库</string>
  <key>CFBundleIdentifier</key><string>com.jcxs2014.referenceread</string>
  <key>CFBundleExecutable</key><string>ReferenceRead</string>
  <key>CFBundlePackageType</key><string>APPL</string>
  <key>CFBundleVersion</key><string>0.1.0</string>
  <key>CFBundleShortVersionString</key><string>0.1.0</string>
  <key>NSHighResolutionCapable</key><true/>
  <key>LSMinimumSystemVersion</key><string>13.0</string>
  <key>NSPrincipalClass</key><string>NSApplication</string>
</dict></plist>
PLIST

# 仅在图标确实存在时才声明 CFBundleIconFile，避免指向不存在的资源
if [ -f "$ICNS" ]; then
  plutil -insert CFBundleIconFile -string AppIcon "$APP/Contents/Info.plist"
fi

if [ "$BUNDLE_WEBAPP" = "1" ]; then
  echo "==> 内嵌 webapp（整目录拷贝，再剪掉开发用目录）"
  # 不手工列文件清单：清单会随 webapp 构建漂移，页面新引用的资源会静默 404。
  cp -R "$SRC" "$APP/Contents/Resources/webapp"
  rm -rf "$APP/Contents/Resources/webapp/scripts" \
         "$APP/Contents/Resources/webapp/tests" \
         "$APP/Contents/Resources/webapp/docs" \
         "$APP/Contents/Resources/webapp/.DS_Store"
  # 载荷自检：页面实际引用的资源必须都在包里
  for f in interactive.html manifest.json apple-touch-icon.png icon-192.png third-party; do
    [ -e "$APP/Contents/Resources/webapp/$f" ] || { echo "错误: 内嵌包缺少 $f" >&2; exit 1; }
  done
  echo "    载荷: $(du -sh "$APP/Contents/Resources/webapp" | cut -f1) / $(find "$APP/Contents/Resources/webapp" -type f | wc -l | tr -d ' ') 个文件"
fi

plutil -lint "$APP/Contents/Info.plist" >/dev/null
echo "==> 完成: $APP  ($(du -sh "$APP" | cut -f1))"
echo "    运行: open '$APP'"
