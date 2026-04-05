# 28_SU-YOLO — Module Context

This module operationalizes **SU-YOLO** from:
- Paper: `papers/2503.24389.pdf`
- Upstream reference: `repositories/snn-underwater/`

## Mission
Build an ANIMA-ready, paper-aligned implementation path for SU-YOLO with:
- reproducible config and preflight checks,
- local command wrappers for train/eval/infer,
- serving and deployment scaffolding,
- testable local baseline before CUDA-server optimization.

## Current Working Baseline
- Paper text extracted to `papers/2503.24389.txt`.
- Upstream code available in `repositories/snn-underwater`.

## Key Paper Targets
- URPC2019 mAP@0.5: **0.788**
- UDD mAP@0.5: **0.582**
- Params: **6.97M**
- Energy: **2.98 mJ**
- Recommended time steps: **T=4**

## Local Commands
- Preflight: `python3 scripts/preflight.py --config configs/paper.toml`
- Show train cmd: `python3 scripts/train.py --config configs/paper.toml --dry-run`
- Show eval cmd: `python3 scripts/evaluate.py --config configs/paper.toml --dry-run`
- Show infer cmd: `python3 scripts/infer.py --config configs/paper.toml --dry-run`
- Run tests: `python3 -m unittest discover -s tests -p 'test_*.py'`
