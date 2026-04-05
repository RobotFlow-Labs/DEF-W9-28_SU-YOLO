# PRD-01: Foundation & Config

> Module: SU-YOLO | Priority: P0
> Depends on: None
> Status: DONE

## Objective
Establish a reproducible local module skeleton with config loading, asset preflight, and baseline tests.

## Context (from paper)
SU-YOLO is a paper-aligned underwater SNN detector with fixed time-step behavior and explicit dataset expectations.
Paper reference: Sections 1, 4.1, 4.2.

## Acceptance Criteria
- [x] `pyproject.toml` exists with package metadata.
- [x] `configs/default.toml`, `configs/debug.toml`, `configs/paper.toml` exist.
- [x] `src/anima_su_yolo/config.py` loads TOML config.
- [x] `src/anima_su_yolo/preflight.py` validates paper/repo/dataset pointers.
- [x] Local unit tests pass for config + preflight.

## Files to Create
- `pyproject.toml`
- `configs/default.toml`
- `configs/debug.toml`
- `configs/paper.toml`
- `src/anima_su_yolo/config.py`
- `src/anima_su_yolo/preflight.py`
- `scripts/preflight.py`
- `tests/test_config.py`
- `tests/test_preflight.py`

## References
- Paper: `papers/2503.24389.pdf`
- Upstream: `repositories/snn-underwater/README.md`
