# TODO · ScopePatrol

> 进度标记:`[ ]` 未开始 / `[~]` 进行中 / `[x]` 完成。长期路线见 [docs/proposal-difficulties-and-design.md](docs/proposal-difficulties-and-design.md)。

## 0. 环境与数据准备

- [x] ~~问助教预训练权重~~ → ✅ 已同意允许 COCO 预训练初始化,按原计划执行

- [ ] 租用 GPU(Colab T4 / AutoDL,本机无 NVIDIA 卡),跑通 ultralytics 环境
- [ ] 确认 `cleansight-yolo` 数据集完整性(group1 35,090 帧 / group2 24,354 帧)
- [ ] 编写合并脚本:两组合并为统一 6 类数据集(类别重映射 + 统一 data.yaml),供单模型实验用
- [ ] `utils/stats.py` 跑一遍全量标签统计,把数字固化进报告(现有统计是采样的)

## 1. Baseline(必做,报告的对照基线)

- [ ] **B0 主 baseline**:单模型 6 类,yolo11s @640,**ultralytics 全默认超参/默认增强**,不加任何自设计模块;训练预算(epochs/patience)与后续实验严格一致,保证公平
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
- [ ] **汇报可视化(最终答辩用)**:
  - [ ] 逐类检测效果画廊(每类挑好/坏各几张,对应论文定性分析)
  - [ ] 方法对比动图/拼图:B0 vs 各设计在同一帧上的检测差异
  - [ ] 混淆矩阵(大目标组内、小目标组内相邻类混淆)
  - [ ] 尺度-精度曲线:box 面积分桶 vs AP,直观展示"40× 尺度鸿沟"
  - [ ] demo 视频:连续洗消片段逐帧检测 + ByteTrack 轨迹叠加(现场演示用)
  - [ ] 训练过程曲线汇总(loss/mAP,ultralytics results.png 拼版)
- [ ] 撰写最终报告:难点 → 设计 → 实验 → 结论
- [ ] 整理 repo(README 更新进度;runs 按"论文表格编号"命名,不删训练日志)

## 7. 提交物(截止 2027-01-05,elearning)

- [ ] 代码 + checkpoint(权重传外部存储,README 放链接)
- [ ] 训练日志汇总(runs/*/results.csv + curves,对应论文实验编号)
- [ ] 课程论文:CVPR2027 双栏,正文 ≤ 8 页,第 14 周前出初稿框架
- [ ] 确认:test 结果只进最终报告,选型全部用 val(红线)
