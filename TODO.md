# TODO · ScopePatrol

> 进度标记:`[ ]` 未开始 / `[~]` 进行中 / `[x]` 完成。长期路线见 [docs/proposal-difficulties-and-design.md](docs/proposal-difficulties-and-design.md)。

## 0. 环境与数据准备

- [ ] 租用 GPU(Colab T4 / AutoDL,本机无 NVIDIA 卡),跑通 ultralytics 环境
- [ ] 确认 `cleansight-yolo` 数据集完整性(group1 35,090 帧 / group2 24,354 帧)
- [ ] 编写合并脚本:两组合并为统一 6 类数据集(类别重映射 + 统一 data.yaml),供单模型实验用
- [ ] `utils/stats.py` 跑一遍全量标签统计,把数字固化进报告(现有统计是采样的)

## 1. Baseline(必做,报告的对照基线)

- [ ] **B0**:单模型 6 类,yolo11s @640(统一数据集)
- [ ] **B1**:双模型分组(曦源现状:group1 + group2 各一套 yolo11s @640)
- [ ] 汇总两组 baseline 的逐类 AP / AP_small / mAP@0.5 / mAP@0.5:0.95 / FPS / 参数量

## 2. 对比实验(核心:同图 ~40× 尺度悬殊怎么解)

- [ ] **E1**:单模型 + **P2 检测头**(4× 下采样)— 自定义 yolo11-p2 结构
- [ ] **E2**:单模型 + **高分辨率训练**(960 / 1280)
- [ ] **E3**:单模型 + **切片推理**(SAHI 式 tile + 合并;训练 @640,推理切块)
- [ ] E1+E2 组合(P2 + 960)是否最优
- [ ] 统一评测协议:val 选型、test 报告;**AP_small(area<32²)单独汇报**,证明提升来自小目标
- [ ] 结论:双模型分组(B1)是工程妥协还是真有优势 → 写进报告讨论

## 3. 创新点一:类不平衡处理

- [ ] 小类(short_brush 2.1k 框 vs hand 28.8k,差 14×)copy-paste 增强
- [ ] 类别加权采样,对比无增强 baseline 的逐类 AP 变化

## 4. 创新点二:层级化后处理(部分-整体结构)

- [ ] 利用标注结构:brush_tip ⊂ short_brush 的包含关系,实现 hierarchical NMS / 一致性约束
- [ ] control_body 与 mid_section 的"同镜体"连接先验,减少相邻类混淆
- [ ] 消融:开/关后处理的逐类 precision/recall 对比

## 5. 创新点三:时序一致性评测

- [ ] 接入 ByteTrack 做帧间平滑,减少类别跳变
- [ ] 定义并实现时序一致性指标(相邻帧类别跳变率、ID switch、轨迹级 AP)
- [ ] 对比:纯帧级检测 vs +跟踪平滑,静态 mAP 与时序指标双维度报告

## 6. 报告与交付

- [ ] 实验记录模板(每次 run 记录配置/指标,自动汇总成表)
- [ ] 可视化:困难样例(小目标、遮挡、反光)的检测结果对比图
- [ ] 撰写最终报告:难点 → 设计 → 实验 → 结论
- [ ] 整理 repo(README 更新进度、清理 runs)
