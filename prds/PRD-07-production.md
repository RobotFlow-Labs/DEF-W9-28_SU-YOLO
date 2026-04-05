# PRD-07: Production Hardening & Export

> Module: SU-YOLO | Priority: P2
> Depends on: PRD-04
> Status: DONE

## Objective
Provide essential export/checkpoint tooling stubs and checklist for CUDA-server execution.

## Context
Paper-level reproduction and deployment require export flow (weights to inference artifacts) and strict preflight before training.

## Acceptance Criteria
- [x] Export command wrapper implemented.
- [x] Batch-size helper script present.
- [x] `NEXT_STEPS.md` documents remaining server-only steps.

## Files to Create
- `src/anima_su_yolo/export.py`
- `scripts/find_batch_size.py`
- `NEXT_STEPS.md`
