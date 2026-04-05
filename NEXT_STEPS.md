# NEXT_STEPS — 28_SU-YOLO

## Session Heartbeat
- [21:10] Gate 0 complete: fresh scaffold, no prior PRD progress.
- [21:12] Gate 1 complete: paper aligned to SU-YOLO (`2503.24389`).
- [21:13] Gate 2 partial: environment `MAC_LOCAL`; required datasets/weights not yet provisioned locally.
- [21:14] Gate 3 in progress: infra files scaffolded for ANIMA module lifecycle.
- [21:15] Gate 3.5 complete: PRD suite + task breakdown generated.
- [21:16] Phase 4 in progress: essential local code implementation + tests.

## Current State
- PRD suite generated (`prds/PRD-01..07`).
- Task suite generated (`tasks/INDEX.md` + per-PRD tasks).
- Essential local implementation scaffold is present in `src/anima_su_yolo/`.

## Blockers
- Full training and paper-metric reproduction blocked until datasets and weights are available on runtime host.

## Next Actions
1. Provision datasets/weights per `ASSETS.md` on CUDA server.
2. Run `scripts/preflight.py` on server.
3. Launch training with generated command from `configs/paper.toml`.
4. Run evaluation and export pipeline.
