#!/usr/bin/env python3
"""协作消息板归档工具（方案 A 通用版）——把 COLLABORATION.md 控制到可整读的体量。

============================================================================
1. 为什么需要
============================================================================
COLLABORATION.md 是「同机多 IDE 共享、写入即同步」的消息板，新消息**追加在顶部**，
因此会无限增长。一旦超过 **71,680 字符**（工具单次读取上限），agent 就无法一次
读完整块协作板（read_file 报 "... exceeds maximum allowed characters ..."），只能
grep / 分段读 —— 协作板最核心的用途随即失效。

本工具即为此设计：**主板只保留近期消息，历史移入归档目录**，并保证结构完整、可追溯。


============================================================================
2. 它做什么 / 不做什么
============================================================================
做：
  * 按「消息块」切分（不切断单条消息，也不破坏 Markdown 结构）；
  * 主板保留： 头部(标题/用途/🆔 约定/排序规则) + 归档索引行 + 近期消息 + 尾部结构区；
  * 归档文件写入 4 行头部（标题 / 来源 / 返回路径+git / 源 MD5+消息块范围+条数）；
  * 归档文件自动命名 ``<较新日期>_to_<较旧日期>.md``（与该文件内部「新→旧」顺序一致）；
  * 刷新主板内的「归档索引行」（幂等，重复运行不会重复插入）；
  * 打印计划并做校验，**校验不通过绝不写入任何文件**。

不做：
  * 不修改 check_collab.sh / sync_memory.sh 等外部脚本；
  * 不删除任何消息（只搬移，归档内容 = 原文逐字节切片）；
  * 不自动 commit（写入后请自行 git add / git commit）。


============================================================================
3. 结构假设（决定它能否用于你的协作板）
============================================================================
主板按下述三段构成：

    头部        第一条 ``### [YYYY-MM-DD`` 之前的所有行
    消息块      每条 ``### [YYYY-MM-DD ...`` 到下一个 ``### [ ...``
    尾部结构区  最后一条消息之后出现的第一个 ``^## `` 章节行 → 文件末
                （如 任务看板 / 协作日志 / 消息清理规则 / FAQ / 联系）

若你的协作板不是这个结构，只需改 parse_structure()，其余逻辑通用。


============================================================================
4. 参数
============================================================================
  --src          主板路径                        （默认 COLLABORATION.md）
  --arch-dir     归档目录                        （默认 Documents/COLLABORATION_ARCHIVE）
  --keep-since   保留该日期及更新（YYYY-MM-DD）    ← 推荐，语义直观
  --max-bytes    主板保留上限（字节，默认 60000，须 <71680）
                 （与 --keep-since 同时给出时，先按日期截断）
  --apply        真正写入；**不加则只打印计划（默认即 dry-run）**
  --dry-run      显式 dry-run（与默认等价，仅为可读性）
  -h, --help     帮助

阈值建议：主板保留「最近约 1 个月」，或让主板字节数稳定在 40–60 KB。


============================================================================
5. 退出码
============================================================================
  0   成功（dry-run 或 apply）
  2   参数错误（argparse）
  1   校验失败 / 主板仍超限 / 结构不符 —— **此时不会写入任何文件**


============================================================================
6. 安全机制（为什么可以放心运行）
============================================================================
  * **基线冻结**：读入后立即计算 MD5 与消息条数，并写入归档头部，可事后核对；
  * **恒等式校验**：主板保留块数 + 归档块数 == 原有消息总数，否则中止；
  * **上限保护**：新主板仍 >= 71680 字节则中止；
  * **原子替换**：新主板先写 .tmp 再 ``os.replace``，避免并发写下的半成品；
  * **只搬不删**：归档 = 原文切片，逐字节一致。


============================================================================
7. 典型工作流
============================================================================
  ① （可选）请另一个 IDE 先暂停写入 —— 协作板是共享文件，虽已用原子替换，仍建议避开并发窗口
  ② python3 archive_split.py                      # 看计划 + 校验（不写盘）
  ③ python3 archive_split.py --apply              # 执行
  ④ 校验条数：grep -c '^### \\[2026-' COLLABORATION.md Documents/COLLABORATION_ARCHIVE/*.md
  ⑤ git add COLLABORATION.md Documents/COLLABORATION_ARCHIVE/ && git commit
  ⑥ 在主板顶部广播一条「已归档」消息，告知其它 IDE

触发时机建议：主板接近 60 KB，或消息积压超过 ~1 个月。


============================================================================
8. 给「协作板模板项目」的采用建议
============================================================================
协作板相关文件应作为**一套**维护：

    COLLABORATION.md    主模板（含 头部 / 排序规则 / 尾部结构区）
    check_collab.sh     查看脚本
    sync_memory.sh      提交脚本
    archive_split.py    本文件（归档工具）

采用要点：
  * 主模板请保留与本文件一致的**三段结构**与
    ``### [YYYY-MM-DD HH:MM UTC] [IDE名] → All`` 消息格式；
  * 在模板的「消息清理规则」章节写明： **容量红线 71,680**、归档目录、
    命名 ``<较新日期>_to_<较旧日期>.md``（与主板「新→旧」顺序一致）、以及本工具用法；
  * 建议把「主板 < 71680」作为一条硬性检查项（例如放进 check 脚本）。

注意：本文件按当前项目决定**不纳入 git**（本地工具）。若要随模板分发，
请自行复制到模板项目。
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
from datetime import date

MSG_RE = re.compile(rb"^### \[(\d{4}-\d{2}-\d{2})")
SEC_RE = re.compile(rb"^## ")
IDX_RE = re.compile(re.escape("> **归档**".encode("utf-8")))   # 主板归档索引行
IDX_CONT_RE = re.compile(re.escape("> （".encode("utf-8")))     # 索引续行

HARD_LIMIT = 71680   # 工具单次读取上限


def bsize(lines) -> int:
    return sum(len(l) + 1 for l in lines)


def count_msgs(lines) -> int:
    return sum(1 for l in lines if MSG_RE.match(l))


def parse_structure(lines):
    """返回 (header, blocks, footer)。"""
    starts = [i for i, l in enumerate(lines) if MSG_RE.match(l)]
    if not starts:
        raise SystemExit("!! 未找到任何 '### [YYYY-MM-DD' 消息行")
    last = starts[-1]
    footer_start = next((i for i in range(last + 1, len(lines)) if SEC_RE.match(lines[i])), len(lines))
    header = lines[: starts[0]]
    blocks = [lines[st: (starts[k + 1] if k + 1 < len(starts) else footer_start)]
              for k, st in enumerate(starts)]
    return header, blocks, lines[footer_start:]


def strip_old_index(header):
    """移除上次运行写入的索引行（幂等）。"""
    out = [l for l in header if not (IDX_RE.match(l) or IDX_CONT_RE.match(l))]
    dedup = []
    for l in out:
        if l == b"" and dedup and dedup[-1] == b"":
            continue
        dedup.append(l)
    return dedup


def block_dates(blk):
    ds = [MSG_RE.match(l).group(1).decode() for l in blk if MSG_RE.match(l)]
    return ds[0], ds[-1]          # (newest, oldest)


def make_chunks(blocks, max_bytes):
    chunks, cur, sz = [], [], 0
    for blk in blocks:
        bs = bsize(blk)
        if cur and sz + bs > max_bytes:
            chunks.append(cur)
            cur, sz = [], 0
        cur.append(blk)
        sz += bs
    if cur:
        chunks.append(cur)
    return chunks


def arch_header(title, blk_range, cnt, base_md5):
    return [
        f"# 协作消息归档：{title}".encode(),
        "> 从 `COLLABORATION.md` 归档；保留原始顺序（新→旧）与原格式。".encode(),
        f"> 归档日期：{date.today().isoformat()}；返回主板：`../../COLLABORATION.md`；完整历史：`git log -- COLLABORATION.md`".encode(),
        f"> 归档时主板 MD5：{base_md5}（源：消息块 {blk_range}，{cnt} 条）".encode(),
        b"",
    ]


def main():
    ap = argparse.ArgumentParser(description="协作消息板归档工具")
    ap.add_argument("--src", default="COLLABORATION.md")
    ap.add_argument("--arch-dir", default=os.path.join("Documents", "COLLABORATION_ARCHIVE"))
    ap.add_argument("--max-bytes", type=int, default=60000,
                    help="主板保留上限（字节，须 <71680）")
    ap.add_argument("--keep-since", default=None, help="保留该日期及更新（YYYY-MM-DD）")
    ap.add_argument("--apply", action="store_true", help="实际写入（不加则只打印计划，即 dry-run）")
    ap.add_argument("--dry-run", action="store_true", help="显式 dry-run（与默认行为等价）")
    args = ap.parse_args()

    data = open(args.src, "rb").read()
    md5 = hashlib.md5(data).hexdigest()
    lines = data.split(b"\n")
    header, blocks, footer = parse_structure(lines)
    total = count_msgs(lines)

    # ---- 保留边界 ----
    keep_n, acc = 0, 0
    for blk in blocks:
        newest, oldest = block_dates(blk)
        if args.keep_since and oldest < args.keep_since:
            break
        bs = bsize(blk)
        if args.keep_since is None and keep_n > 0 and acc + bs > args.max_bytes:
            break
        acc += bs
        keep_n += 1
    keep_n = max(1, keep_n)
    keep_blocks, arch_blocks = blocks[:keep_n], blocks[keep_n:]

    print(f"源          : {args.src}")
    print(f"MD5         : {md5}")
    print(f"消息总数    : {total}")
    print(f"保留        : {len(keep_blocks)} 块  ({block_dates(keep_blocks[-1])[1]} .. {block_dates(keep_blocks[0])[0]})")
    print(f"归档        : {len(arch_blocks)} 块")

    if not arch_blocks:
        print("\n无需归档（主板未超限）。")
        return

    chunks = make_chunks(arch_blocks, args.max_bytes)
    outs = []
    bi = keep_n
    for ch in chunks:
        n = sum(count_msgs(b) for b in ch)
        newest = max(block_dates(b)[0] for b in ch)
        oldest = min(block_dates(b)[1] for b in ch)
        rng = f"#{bi + 1}–#{bi + len(ch)}"
        bi += len(ch)
        outs.append((f"{newest}_to_{oldest}.md", ch, n, rng))

    idx = [
        "> **归档**：较早的消息已移至 `%s/`" % args.arch_dir,
        "（" + "、".join(f"`{nm}` {n} 条" for nm, _c, n, _r in outs)
        + "）；完整历史见 `git log -- COLLABORATION.md`。",
        "",
    ]
    main_out = b"\n".join(
        strip_old_index(header) + [l.encode() for l in idx]
        + [l for blk in keep_blocks for l in blk] + footer
    )

    # ---- 校验 ----
    kept = sum(count_msgs(b) for b in keep_blocks)
    arched = sum(n for _nm, _c, n, _r in outs)
    print(f"\n主板保留 {kept} 条 = {len(main_out)} B ({'OK <71680' if len(main_out) < HARD_LIMIT else '!! 超限'})")
    for nm, ch, n, rng in outs:
        print(f"归档 {nm}: {n} 条 = {bsize([l for b in ch for l in b])} B")
    print(f"恒等式: {kept} + {arched} = {kept + arched}  (原 {total}) -> {'OK' if kept + arched == total else '!! 不符'}")

    if kept + arched != total:
        raise SystemExit("!! 消息条数恒等式校验失败，未写入")
    if len(main_out) >= HARD_LIMIT:
        raise SystemExit("!! 主板仍超 71680，请调小 --max-bytes 或调早 --keep-since")

    if not args.apply:
        print("\n[dry-run] 未写入（加 --apply 执行）。")
        return

    os.makedirs(args.arch_dir, exist_ok=True)
    for nm, ch, n, rng in outs:
        seg = [l for b in ch for l in b]
        title = nm[:-3].replace("_to_", " ~ ")
        open(os.path.join(args.arch_dir, nm), "wb").write(
            b"\n".join(arch_header(title, rng, n, md5) + seg) + b"\n")
    tmp = args.src + ".tmp"
    open(tmp, "wb").write(main_out)
    os.replace(tmp, args.src)
    print("\n[applied] 已写入 %d 个归档 + 新主板" % len(outs))


if __name__ == "__main__":
    main()
