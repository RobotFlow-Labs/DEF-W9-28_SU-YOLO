# PRD-05: API & Docker Serving

> Module: SU-YOLO | Priority: P1
> Depends on: PRD-03
> Status: DONE

## Objective
Scaffold a serving interface with health/readiness endpoints and container files for later GPU deployment.

## Context
Autopilot production flow requires module service endpoints and compose/docker definitions before deployment hardening.

## Acceptance Criteria
- [x] `serve.py` exposes `/health`, `/ready`, `/predict` handlers.
- [x] `Dockerfile.serve` exists.
- [x] `docker-compose.serve.yml` exists.
- [x] Service can be imported locally without GPU.

## Files to Create
- `src/anima_su_yolo/serve.py`
- `Dockerfile.serve`
- `docker-compose.serve.yml`
