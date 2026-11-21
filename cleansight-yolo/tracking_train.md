# CleanSight YOLO · 训练轨(train/val)

**生成**: 2026-11-07 12:30:09
**清单**: train.yaml
**项目**: yolo-train
**导出**: project-10-at-2026-11-07-04-13-a01302be.json

## 在册 task

| LS Task | 视频 | Split | 本次构建 | 动作段 | 检测类 | 落盘帧 |
|---------|------|-------|---------|--------|--------|--------|
| 50 | 218f9117-clip_1781583985044_1781584 | train | 否(增量跳过) | long_brush_insert | 4 | — |
| 51 | b004acff-clip_1781584008145_1781584 | train | 否(增量跳过) | long_brush_withdraw | 4 | — |
| 52 | 05ba4406-clip_1781584018103_1781584 | train | 否(增量跳过) | long_brush_insert | 5 | — |
| 53 | 9f93cf16-clip_1781584034867_1781584 | train | 否(增量跳过) | long_brush_withdraw | 4 | — |
| 54 | af0e7803-clip_1781584048438_1781584 | train | 否(增量跳过) | long_brush_insert | 6 | — |
| 55 | 7e8f5b4f-clip_1781584064111_1781584 | train | 否(增量跳过) | long_brush_withdraw | 4 | — |
| 58 | ed1f1353-clip_1781659288372_1781659 | train | 否(增量跳过) | short_brush_cleaning | 4 | — |
| 59 | 4807dbbe-clip_1781659328328_1781659 | train | 否(增量跳过) | air_injection, long_brush_insert, long_brush_withdraw | 4 | — |
| 60 | a2ade960-clip_1781660307856_1781660 | train | 否(增量跳过) | long_brush_insert, long_brush_withdraw, short_brush_cleaning | 6 | — |
| 61 | 65d70028-clip_1781661552468_1781661 | val | 否(增量跳过) | flush, long_brush_insert, long_brush_withdraw | 6 | — |
| 62 | 3614fb62-clip_1782091187000_1782091 | train | 否(增量跳过) | air_injection, flush, long_brush_insert, long_brush_withdraw | 7 | — |
| 68 | 63a848d5-clip_1782695363948_1782695 | train | 否(增量跳过) | flush, long_brush_insert, long_brush_withdraw | 6 | — |
| 69 | 2c635ddc-clip_1782695261284_1782695 | train | 否(增量跳过) | short_brush_cleaning | 6 | — |
| 71 | 37c53d37-clip_1782286495080_1782286 | val | 否(增量跳过) | long_brush_insert, long_brush_withdraw, short_brush_cleaning | 5 | — |
| 73 | f4b10ad8-clip_1782264442808_1782264 | val | 否(增量跳过) | air_injection | 6 | — |
| 77 | fedf6ff9-clip_1783393131145_1783393 | train | 否(增量跳过) | flush, short_brush_cleaning | 6 | — |
| 78 | b1b042a9-clip_1783395777441_1783395 | train | 否(增量跳过) | long_brush_insert, long_brush_withdraw | 3 | — |
| 80 | 6b722939-clip_1782802545949_1782802 | val | 否(增量跳过) | air_injection, flush, short_brush_cleaning | 7 | — |
| 82 | 3d3ec766-clip_1782869840929_1782869 | val | 否(增量跳过) | air_injection | 6 | — |
| 83 | 1301ed4c-clip_1782871306647_1782871 | train | 否(增量跳过) | air_injection, long_brush_insert, long_brush_withdraw | 6 | — |
| 84 | f0d28b80-clip_1783302144895_1783302 | train | 否(增量跳过) | air_injection, short_brush_cleaning | 4 | — |
| 85 | 1fcfcdea-clip_1783302201419_1783302 | train | 否(增量跳过) | long_brush_insert, long_brush_withdraw | 5 | — |
| 86 | 78f3593a-clip_1783301769259_1783301 | train | 否(增量跳过) | short_brush_cleaning | 4 | — |
| 87 | b3778449-clip_1783301814930_1783301 | train | 否(增量跳过) | long_brush_insert, long_brush_withdraw | 5 | — |
| 657 | eff1d4e7-clip_1793063733424_1793063 | train | 是 | — | 5 | 728 |
| 658 | 059a6dfe-clip_1793063824135_1793063 | train | 是 | — | 5 | 184 |
| 662 | 48476d19-clip_1793065916916_1793065 | train | 是 | — | 4 | 510 |
| 663 | a6f454bd-clip_1793065981250_1793065 | train | 是 | — | 4 | 153 |
| 664 | 020e2330-clip_1793065993366_1793066 | train | 是 | — | 4 | 141 |
| 665 | 0280eae2-clip_1793066087022_1793066 | train | 是 | — | 4 | 253 |
| 666 | a8152433-clip_1793077593843_1793077 | train | 是 | — | 5 | 360 |
| 667 | 199e3650-clip_1793081018213_1793081 | train | 是 | — | 5 | 241 |
| 668 | b50091d8-clip_1793081035881_1793081 | train | 是 | — | 4 | 52 |
| 669 | d213eef1-clip_1793086977392_1793086 | train | 是 | — | 4 | 87 |

## 各组产出

| 组 | Split | 图片 | 框 |
|----|-------|------|-----|
| group1_large | train | 13078 | 44399 |
| group1_large | val | 3925 | 13305 |
| group2_small | train | 8470 | 11493 |
| group2_small | val | 3624 | 5393 |

## Split 分配

| Split | Task |
|-------|------|
| train | 50, 51, 52, 53, 54, 55, 58, 59, 60, 62, 68, 69, 77, 78, 83, 84, 85, 86, 87, 657, 658, 662, 663, 664, 665, 666, 667, 668, 669 |
| val | 61, 71, 73, 80, 82 |

> 一个 task 的所有帧只进它的 split,杜绝时间相邻泄漏。
> 帧名 `t{task_id}_{frame:06d}` —— 身份键是 LS task id,不随视频重传而变。
> 旋转框自动转 AABB。
