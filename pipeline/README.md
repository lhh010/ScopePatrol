# ScopePatrol · 训练/评测流水线

对 `../cleansight-yolo/` 数据集(从 [ModelScope: cleansight-yolo](https://www.modelscope.cn/datasets/lhh010/cleansight-yolo) 下载)做 YOLO 训练与验收。

数据集构建(Label Studio 拉取、标注转换、视频级切分)由曦源侧流水线完成,不在本仓库范围内。

## 结构

```
pipeline/
  03_train.py       # 各组训练 → runs/<组>/weights/best.pt
  04_validate.py    # 验证集指标 + 验收 PASS/FAIL → runs/<组>/acceptance_report.md
  config.yaml       # 唯一配置入口:分组 / 超参 / 验收阈值
  requirements.txt
  utils/            # common.py(路径与配置)、stats.py(标签分布统计)
  runs/             # 训练产物(git ignore)
```

## 用法

```bash
cd pipeline
pip install -r requirements.txt
python 03_train.py                 # 或只训某组:python 03_train.py group2_small
python 04_validate.py              # 指标 + 验收报告
python -c "from utils import stats; stats.main()"   # 数据分布统计
```

设备自动选 CUDA / MPS / CPU。无本地 GPU 时建议在 Colab / AutoDL 上运行。
