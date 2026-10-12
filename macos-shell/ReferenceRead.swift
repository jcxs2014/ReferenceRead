// ReferenceRead 极简桌面壳
// 单文件 Swift + WKWebView，无 Xcode 工程、无第三方依赖、无 package manager。
//
// 设计要点：
//   1. 用自定义 scheme `refread://app/...` 加载页面。
//      ⚠️ 实测更正（2026-10-12，WKWebView / macOS）——file:// 并非不可用：
//        · location.origin 是 "file://"，不是 null；
//        · localStorage 可写可读，且跨进程持久化
//          （落盘于 ~/Library/WebKit/<bundleid>/.../LocalStorage/localstorage.sqlite3）；
//        · loadFileURL(_:allowingReadAccessTo:) 下相对子资源（CSS/字体）正常加载。
//      所以自定义 scheme 是「可选优化」而非「必需」。保留它的理由：origin 有名且稳定、
//      由 handler 统一控制 MIME/编码、便于将来改为非文件后端或补 HTTP 语义。
//      若追求最小实现，改用 loadFileURL 可整个删掉 WebAppSchemeHandler。
//   2. 默认直接读仓库里的 webapp/，不复制 14MB 载荷；只有打包分发时才拷进 Resources/webapp。
//   3. 构建一条 swiftc 命令，秒级完成。
//
// 版本：初始壳 DSH-Mac（2026-10-12）；加固 Hermes-Mac（同日）；
//       注释实测更正 DSH-Mac（2026-10-12）——代码逻辑未变，仅修正两处错误论断。

import Cocoa
import WebKit

// MARK: - 自定义 scheme 处理器

final class WebAppSchemeHandler: NSObject, WKURLSchemeHandler {
    /// 磁盘根目录（已标准化 + 解析符号链接）
    let root: URL

    init(root: URL) {
        self.root = root.standardizedFileURL.resolvingSymlinksInPath()
    }

    /// 把 URL 路径映射到 root 下的真实文件；越界（目录穿越）返回 nil。
    ///
    /// 不能用字符串前缀比较：`…/webapp-evil/probe.html` 会通过 `hasPrefix("…/webapp")`。
    /// 实测确认（2026-10-12，WKWebView 会把请求原样交给 handler）：
    ///   refread://app/..%2fwebapp-evil%2fprobe.html
    ///     → handler 收到 path `/../webapp-evil/probe.html`
    ///     → 旧版 standardizedFileURL 折叠成 `…/ReferenceRead/webapp-evil/probe.html`
    ///     → hasPrefix("…/webapp") 成立 → ⚠️ 越界放行
    ///       （仓库当前无 webapp-* 兄弟目录，故为潜在而非已可利用）
    /// 注意：`refread://app/..%2fX`、`%2e%2e%2fX` 这类**纯逃逸**旧版本来就拒绝
    /// （标准化后逃出前缀，hasPrefix 失败），真正的缺口是上面的「兄弟目录前缀」。
    /// 另：字面量 `../` 会被 WebKit 在交给 handler 前归一化掉，编码斜杠 `%2f` 不会。
    /// 故此处按 pathComponents 逐段比较，且标准化后仍含 ".." 一律拒绝。
    static func resolve(_ path: String, under root: URL) -> URL? {
        var rel = path
        while rel.hasPrefix("/") { rel.removeFirst() }
        guard !rel.isEmpty else { return nil }

        let base = root.standardizedFileURL.resolvingSymlinksInPath()
        let candidate = base.appendingPathComponent(rel)
            .standardizedFileURL
            .resolvingSymlinksInPath()

        guard !candidate.pathComponents.contains("..") else { return nil }
        let bc = base.pathComponents, cc = candidate.pathComponents
        guard cc.count > bc.count, Array(cc.prefix(bc.count)) == bc else { return nil }
        return candidate
    }

    func webView(_ webView: WKWebView, start task: WKURLSchemeTask) {
        guard let url = task.request.url else { return }
        var path = url.path
        if path.isEmpty || path == "/" { path = "/interactive.html" }

        // .mappedIfSafe：mmap 而非整份读进内存（14MB 载荷），减少主线程阻塞。
        // 注意 handler 回调在主线程，仍应避免在此做重活。
        guard let file = Self.resolve(path, under: root),
              let data = try? Data(contentsOf: file, options: [.mappedIfSafe]) else {
            task.didFailWithError(NSError(domain: "ReferenceRead", code: 404,
                                          userInfo: [NSLocalizedDescriptionKey: "not found: \(path)"]))
            return
        }
        let ext = file.pathExtension
        task.didReceive(URLResponse(url: url,
                                    mimeType: Self.mime(for: ext),
                                    expectedContentLength: data.count,
                                    textEncodingName: Self.isText(ext) ? "utf-8" : nil))
        task.didReceive(data)
        task.didFinish()
    }

    func webView(_ webView: WKWebView, stop task: WKURLSchemeTask) {}

    static func mime(for ext: String) -> String {
        switch ext.lowercased() {
        case "html", "htm": return "text/html"
        case "js", "mjs":   return "application/javascript"
        case "css":         return "text/css"
        case "json", "map": return "application/json"
        case "txt", "md":   return "text/plain"
        case "svg":         return "image/svg+xml"
        case "png":         return "image/png"
        case "woff2":       return "font/woff2"
        case "woff":        return "font/woff"
        case "ttf":         return "font/ttf"
        default:            return "application/octet-stream"
        }
    }

    /// 只有文本类型才声明 utf-8；png / woff2 这类二进制声明编码是错的。
    static func isText(_ ext: String) -> Bool {
        switch ext.lowercased() {
        case "html", "htm", "js", "mjs", "css", "json", "map", "txt", "md", "svg": return true
        default: return false
        }
    }
}

// MARK: - 应用

final class AppDelegate: NSObject, NSApplicationDelegate {
    var window: NSWindow!

    /// 依次尝试：打包进 .app 的 Resources/webapp → 仓库根的 webapp/ → 当前工作目录的 webapp/
    static func webRootCandidates() -> [URL] {
        var candidates: [URL] = []
        if let res = Bundle.main.resourceURL {
            candidates.append(res.appendingPathComponent("webapp"))
        }
        let exeDir = URL(fileURLWithPath: CommandLine.arguments[0])
            .resolvingSymlinksInPath().deletingLastPathComponent()
        // Contents/MacOS/ → Contents/ → .app/ → 仓库根
        candidates.append(exeDir.appendingPathComponent("../../../webapp"))
        candidates.append(URL(fileURLWithPath: FileManager.default.currentDirectoryPath)
            .appendingPathComponent("webapp"))
        return candidates
    }

    static func locateWebRoot() -> URL? {
        webRootCandidates().first {
            FileManager.default.fileExists(atPath: $0.appendingPathComponent("interactive.html").path)
        }
    }

    /// 载荷找不到时给出可见报错，而不是静默白屏。
    static func reportMissingWebRoot() {
        let tried = webRootCandidates()
            .map { "  • \($0.standardizedFileURL.path)" }
            .joined(separator: "\n")
        let alert = NSAlert()
        alert.alertStyle = .critical
        alert.messageText = "找不到 webapp 载荷"
        alert.informativeText = "已尝试以下路径：\n\(tried)\n\n"
            + "请把 ReferenceRead.app 放回仓库根目录，或用 ./macos-shell/build.sh --bundle 构建内嵌版。"
        alert.addButton(withTitle: "退出")
        alert.runModal()
    }

    func applicationDidFinishLaunching(_ note: Notification) {
        guard let webRoot = Self.locateWebRoot() else {
            Self.reportMissingWebRoot()
            NSApp.terminate(nil)
            return
        }

        let config = WKWebViewConfiguration()
        config.setURLSchemeHandler(WebAppSchemeHandler(root: webRoot), forURLScheme: "refread")
        // 私有 KVC 键：本地开发用（可开 Web Inspector 调试），上架 App Store 会被拒。
        config.preferences.setValue(true, forKey: "developerExtrasEnabled")

        let webView = WKWebView(frame: .zero, configuration: config)
        webView.autoresizingMask = [.width, .height]

        window = NSWindow(contentRect: NSRect(x: 0, y: 0, width: 1280, height: 860),
                          styleMask: [.titled, .closable, .miniaturizable, .resizable],
                          backing: .buffered, defer: false)
        window.title = "papers 知识库"
        window.contentView = webView
        window.center()
        window.makeKeyAndOrderFront(nil)

        webView.load(URLRequest(url: URL(string: "refread://app/interactive.html")!))
        NSLog("ReferenceRead: web root = %@", webRoot.path)
    }

    func applicationShouldTerminateAfterLastWindowClosed(_ app: NSApplication) -> Bool { true }
}

let app = NSApplication.shared
let delegate = AppDelegate()
app.delegate = delegate
app.setActivationPolicy(.regular)
app.run()
