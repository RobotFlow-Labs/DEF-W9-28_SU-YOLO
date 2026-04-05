# PRD-03: Inference & Command Orchestration

> Module: SU-YOLO | Priority: P0
> Depends on: PRD-02
> Status: DONE

## Objective
Provide executable wrappers for train/eval/infer that are safe to run locally in dry-run mode and server-ready for real execution.

## Context (from paper)
Inference and evaluation rely on the same model/time-step settings used in experiments; reproducibility requires deterministic CLI construction.
Paper reference: Sections 4.1–4.3.

## Acceptance Criteria
- [x] `python -m anima_su_yolo.train --dry-run` prints upstream command.
- [x] `python -m anima_su_yolo.evaluate --dry-run` prints upstream command.
- [x] `python -m anima_su_yolo.infer --dry-run` prints upstream command.
- [x] `scripts/smoke_local.py` validates orchestration without GPU execution.

## Files to Create
- `src/anima_su_yolo/train.py`
- `src/anima_su_yolo/evaluate.py`
- `src/anima_su_yolo/infer.py`
- `scripts/smoke_local.py`

## References
- `repositories/snn-underwater/train.py`
- `repositories/snn-underwater/val.py`
- `repositories/snn-underwater/detect.py`
