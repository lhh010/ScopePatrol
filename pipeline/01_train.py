#!/usr/bin/env python3
"""
按组训练 YOLO 目标检测(ultralytics)。各组一套权重,落在 runs/<组>/weights/best.pt。
设备自动选 CUDA / MPS(Apple) / CPU。超参在 config.yaml 的 train: 段。

用法(在 pipeline/ 下执行):
    python 01_train.py                 # 全部组
    python 01_train.py group2_small    # 只训某组
"""
import sys

from utils.common import DATASETS, RUNS, load_config


def pick_device() -> str:
    import torch
    if torch.cuda.is_available():
        return "0"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def main():
    from ultralytics import YOLO

    tcfg = load_config().get("train", {})
    device = pick_device()

    requested = [a for a in sys.argv[1:] if not a.startswith("-")]
    groups = requested or [p.name for p in sorted(DATASETS.iterdir()) if p.is_dir()]
    if not groups:
        raise SystemExit(f"{DATASETS} 下没有数据集组,请先从 ModelScope 下载 cleansight-yolo")

    results = []
    for g in groups:
        data = DATASETS / g / "data.yaml"
        if not data.exists():
            print(f"  [skip] {g}: 缺 data.yaml")
            continue
        print(f"\n=== 训练 {g}  (device={device}, model={tcfg.get('model')}) ===")
        model = YOLO(tcfg.get("model", "yolo11n.pt"))
        model.train(
            data=str(data),
            epochs=tcfg.get("epochs", 100),
            imgsz=tcfg.get("imgsz", 640),
            batch=tcfg.get("batch", 16),
            patience=tcfg.get("patience", 20),
            device=device,
            project=str(RUNS),
            name=g,
            exist_ok=True,
        )
        best = RUNS / g / "weights" / "best.pt"
        print(f"  权重: {best}")
        results.append((g, best))

    print("\n=== 完成 ===")
    for g, best in results:
        print(f"{g}: {best}")
    print("下一步:02_validate.py 出验收报告")


if __name__ == "__main__":
    main()
