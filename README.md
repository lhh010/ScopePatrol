# ScopePatrol

**Multi-scale object detection for endoscope reprocessing: detecting hands, scope parts and tiny instruments in wash-inspection videos.**

ScopePatrol is a computer-vision module for AI-assisted inspection of endoscope reprocessing (cleaning & disinfection). It detects **hands**, **scope body parts** (control body, mid-section, distal end), and **small cleaning instruments** (syringe, short brush) in basin-side video, returning bounding boxes and confidences for downstream compliance auditing.

The core challenge is an extreme **scale gap within a single scene** — from hands covering ~2.4% of the frame down to a scope distal end at ~0.3%, a 40x disparity that defeats vanilla detectors. ScopePatrol systematically compares four strategies (dual-model grouping, a P2 detection head, high-resolution training, and tiled inference), adds hierarchy-aware post-processing for part-whole classes, and evaluates temporal consistency via lightweight tracking.

## Repository layout

| Path | Contents |
|---|---|
| `docs/` | Difficulty analysis & experiment design ([proposal-difficulties-and-design.md](docs/proposal-difficulties-and-design.md)) |
| `cleansight-yolo/` | Dataset metadata: class definitions, splits policy, tagging criteria. **Images/labels are not stored here** — download from [ModelScope: cleansight-yolo](https://www.modelscope.cn/datasets/lhh010/cleansight-yolo) |
| `pipeline/` | Training & validation pipeline (train → validate), adapted from the Xiyuan `cleansight-yolo-pipeline` |

## Classes

| Group | Class | id | Median box area |
|---|---|---|---|
| large | `hand` | 0 | 2.44% |
| large | `scope_control_body` | 1 | 3.65% |
| large | `scope_mid_section` | 2 | 3.18% |
| small | `syringe` | 0 | 1.22% |
| small | `short_brush` | 3 | 0.51% |
| small | `scope_distal_end` | 2 | **0.30%** |

## Pipeline usage

```bash
cd pipeline
pip install -r requirements.txt
python 03_train.py            # trains each group; weights land in runs/<group>/weights/best.pt
python 04_validate.py         # metrics + acceptance report
```

## Status

- [x] Dataset built & split (video-level, leak-free)
- [x] Difficulty analysis with full-label statistics
- [ ] Baseline: single 6-class model @640
- [ ] Dual-model grouping baseline
- [ ] P2 head + high-resolution
- [ ] Tiled inference (SAHI-style)
- [ ] Hierarchy-aware post-processing
- [ ] Temporal consistency evaluation
