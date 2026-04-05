# SU-YOLO — Asset Manifest

## Paper
- Title: SU-YOLO: Spiking Neural Network for Efficient Underwater Object Detection
- ArXiv: 2503.24389
- Authors: Chenyang Li, Wenxuan Liu, Guoqiang Gong, Xiaobo Ding, Xian Zhong
- Code: https://github.com/lwxfight/snn-underwater

## Status
- READY (paper + upstream code present locally)
- DATA BLOCKED (local machine missing required training datasets/weights)

## Pretrained Weights
| Model | Size | Source | Path on Server | Status |
|---|---:|---|---|---|
| SU-YOLO checkpoint (paper) | N/A | Google Drive (upstream README) | /mnt/forge-data/models/su-yolo/checkpoint.pt | MISSING_LOCAL |
| YOLOv9 baseline weights (optional init) | N/A | upstream tooling | /mnt/forge-data/models/yolov9/ | UNKNOWN |

## Datasets
| Dataset | Size | Split | Source | Path | Status |
|---|---:|---|---|---|---|
| URPC2019 | N/A | train/val/test | https://universe.roboflow.com/underwater-fish-f6cri/urpc2019-nrbk1 | /mnt/forge-data/datasets/urpc | MISSING_LOCAL |
| UDD | N/A | train/val/test | https://universe.roboflow.com/yuyutsu/udd-j8cpd | /mnt/forge-data/datasets/udd | MISSING_LOCAL |
| Pascal VOC 2012 (for SeBN comparison) | N/A | train/val | VOC official | /mnt/forge-data/datasets/voc2012 | OPTIONAL |

## Hyperparameters (Paper + Upstream)
| Param | Value | Source |
|---|---|---|
| time_step | 4 | Paper Table 7 + abstract; `train.py --time-step` |
| epochs | 300 | Upstream training recipe |
| batch_size | 16 | Upstream training recipe |
| image_size | 320 | Upstream training recipe |
| optimizer | SGD | `train.py` default |
| lr0 | 0.01 | `data/hyps/hyp.scratch-high.yaml` |
| lrf | 0.01 | `data/hyps/hyp.scratch-high.yaml` |
| momentum | 0.937 | `data/hyps/hyp.scratch-high.yaml` |
| weight_decay | 0.0005 | `data/hyps/hyp.scratch-high.yaml` |
| warmup_epochs | 3.0 | `data/hyps/hyp.scratch-high.yaml` |

## Expected Metrics (Paper)
| Benchmark | Metric | Paper Value | Target |
|---|---|---:|---:|
| URPC2019 | mAP@0.5 | 0.788 | >= 0.78 |
| URPC2019 | mAP@0.5:0.95 | 0.429 | >= 0.42 |
| UDD | mAP@0.5 | 0.582 | >= 0.57 |
| UDD | mAP@0.5:0.95 | 0.266 | >= 0.26 |
| Model size | Params | 6.97M | <= 7.2M |
| Efficiency | Energy | 2.98 mJ | reproduce estimate |

## Local References
- Paper PDF: `papers/2503.24389.pdf`
- Paper text: `papers/2503.24389.txt`
- Upstream repo clone: `repositories/snn-underwater/`
