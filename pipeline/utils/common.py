"""脚本共用:定位路径、加载 config.yaml。"""
from pathlib import Path

import yaml

PKG_ROOT = Path(__file__).resolve().parent.parent   # pipeline/
REPO_ROOT = PKG_ROOT.parent                          # ScopePatrol/
DATASETS = REPO_ROOT / "cleansight-yolo"             # 数据集根(ModelScope 下载后放这里)
RUNS = PKG_ROOT / "runs"                             # 训练产物
CONFIG_PATH = PKG_ROOT / "config.yaml"


def load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
