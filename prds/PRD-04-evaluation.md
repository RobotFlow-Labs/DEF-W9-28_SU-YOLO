# PRD-04: Evaluation & Benchmark Harness

> Module: SU-YOLO | Priority: P1
> Depends on: PRD-03
> Status: DONE

## Objective
Define benchmark targets and a local report path to compare runtime outputs against paper metrics.

## Context (from paper)
The paper reports URPC/UDD results, with ablations for SpikeDenoiser/SeBN and time-step sensitivity.
Paper reference: Section 4.3, Tables 1–7.

## Acceptance Criteria
- [x] Bench targets are codified in config/docs.
- [x] Local utility can emit expected-vs-observed placeholders.
- [x] Preflight warns when required datasets are missing.

## Files to Create
- `ASSETS.md`
- `src/anima_su_yolo/preflight.py`
- `scripts/preflight.py`

## References
- `papers/2503.24389.txt` (tables and metrics)
