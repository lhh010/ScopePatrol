#!/usr/bin/env python3
"""
构建统一 6 类数据集:合并 group1_large + group2_small → cleansight-yolo/unified_6cls/

类别映射(统一 id,追加式,以后加类只能加在末尾):
  group1_large: hand=0, scope_control_body=1, scope_mid_section=2(不变)
  group2_small: syringe 0→3, scope_distal_end 2→4, short_brush 3→5
  丢弃: air_gun(1)、brush_tip_out(4)(见 pj 设定)

关键语义:
  - 同一帧在两组都有标注 → 两个文件的框合并进一个标签(这是"合并"的本意)
  - 仅图片硬链接(同盘不占空间),失败退化复制;标签重写(小文件)
  - 文件名冲突(两组各有、但图片字节不同,极少见)→ group2 侧加前缀 g2_

用法(在 pipeline/ 下执行,仅标准库):
    python 00_build_unified.py
"""
import os
import shutil
import stat
import sys
from pathlib import Path

from utils.common import DATASETS

SRC_GROUPS = {"group1_large": {0: 0, 1: 1, 2: 2},   # 原 id -> 统一 id
              "group2_small": {0: 3, 2: 4, 3: 5}}   # air_gun/brush_tip_out 不在表中=丢弃
NAMES = ["hand", "scope_control_body", "scope_mid_section",
         "syringe", "scope_distal_end", "short_brush"]
OUT = DATASETS / "unified_6cls"
SPLITS = ("train", "val", "test")


def _rmtree_retry(path: Path):
    """rmtree 容错:只读属性清掉后重试一次(Windows/杀软常见)。"""
    def onerr(func, p, exc_info):
        os.chmod(p, stat.S_IWRITE)
        func(p)
    shutil.rmtree(path, onerror=onerr)


def link_or_copy(src: Path, dst: Path):
    if dst.exists():
        return
    try:
        os.link(src, dst)             # 同盘硬链接,零拷贝(Python 3.9 可用)
    except OSError:
        shutil.copy2(src, dst)        # 跨盘等场景的最后手段


def remap_label(txt: Path) -> list[str]:
    out = []
    for line in txt.read_text(encoding="utf-8").splitlines():
        p = line.strip().split()
        if len(p) < 5:
            continue
        new = SRC_GROUPS_CURRENT.get(int(p[0]))
        if new is None:               # 被丢弃的类
            continue
        out.append(f"{new} " + " ".join(p[1:5]))
    return out


def main():
    global SRC_GROUPS_CURRENT
    if OUT.exists():
        _rmtree_retry(OUT)
    stats = {s: {"frames": 0, "boxes": 0, "dropped": 0} for s in SPLITS}

    for split in SPLITS:
        (OUT / "images" / split).mkdir(parents=True, exist_ok=True)
        (OUT / "labels" / split).mkdir(parents=True, exist_ok=True)

    for gname, mapping in SRC_GROUPS.items():
        SRC_GROUPS_CURRENT = mapping
        for split in SPLITS:
            img_dir = DATASETS / gname / "images" / split
            lbl_dir = DATASETS / gname / "labels" / split
            if not img_dir.exists():
                print(f"  [warn] 缺 {img_dir},跳过")
                continue
            for img in sorted(img_dir.iterdir()):
                stem, ext = img.stem, img.suffix
                lbl = lbl_dir / (stem + ".txt")
                lines = remap_label(lbl) if lbl.exists() else []
                stats[split]["dropped"] += (0 if not lbl.exists() else
                    sum(1 for l in lbl.read_text(encoding="utf-8").splitlines()
                        if l.strip() and int(l.split()[0]) not in mapping))

                out_lbl = OUT / "labels" / split / (stem + ".txt")
                out_img = OUT / "images" / split / (stem + ext)
                if out_img.exists():   # 同帧已在另一组出现过 → 合并标签
                    if lines:
                        old = out_lbl.read_text(encoding="utf-8").splitlines() if out_lbl.exists() else []
                        out_lbl.write_text("\n".join(old + lines) + "\n", encoding="utf-8")
                    continue

                # 目标名被另一组占用(同 stem 不同内容,极少)→ g2_ 前缀
                if any((OUT / "images" / s / (stem + ext)).exists() for s in SPLITS):
                    if gname == "group2_small":
                        stem = "g2_" + stem
                        out_lbl = OUT / "labels" / split / (stem + ".txt")
                        out_img = OUT / "images" / split / (stem + ext)
                    else:
                        continue

                link_or_copy(img, out_img)
                if lines:
                    out_lbl.write_text("\n".join(lines) + "\n", encoding="utf-8")
                stats[split]["frames"] += 1
                stats[split]["boxes"] += len(lines)

    names = "\n".join(f"  {i}: {n}" for i, n in enumerate(NAMES))
    (OUT / "data.yaml").write_text(
        f"path: {OUT.resolve()}\n"
        f"train: images/train\nval: images/val\ntest: images/test\n"
        f"nc: {len(NAMES)}\nnames:\n{names}\n", encoding="utf-8")

    print(f"\n=== 统一数据集已生成: {OUT} ===")
    for s in SPLITS:
        print(f"  {s:5s} frames={stats[s]['frames']:6d} boxes={stats[s]['boxes']:6d} dropped={stats[s]['dropped']}")


if __name__ == "__main__":
    main()