# SU-YOLO Task Index

## Build Order

| Task | Title | Depends | Status |
|---|---|---|---|
| PRD-0101 | Initialize package + project metadata | None | DONE |
| PRD-0102 | Add config files and config loader | PRD-0101 | DONE |
| PRD-0103 | Implement preflight checks and tests | PRD-0102 | DONE |
| PRD-0201 | Encode paper defaults in typed config | PRD-0102 | DONE |
| PRD-0202 | Build upstream command constructors | PRD-0201 | DONE |
| PRD-0301 | Implement train wrapper CLI | PRD-0202 | DONE |
| PRD-0302 | Implement eval/infer wrapper CLIs | PRD-0301 | DONE |
| PRD-0401 | Add benchmark targets and comparison structure | PRD-0302 | DONE |
| PRD-0402 | Expose dataset/weights readiness diagnostics | PRD-0401 | DONE |
| PRD-0501 | Add serving handlers (`health`, `ready`, `predict`) | PRD-0302 | DONE |
| PRD-0502 | Add Docker + Compose serving scaffolding | PRD-0501 | DONE |
| PRD-0601 | Define `anima_module.yaml` runtime contract | PRD-0502 | DONE |
| PRD-0701 | Add export command wrapper | PRD-0402 | DONE |
| PRD-0702 | Add pre-train batch-size helper and smoke script | PRD-0701 | DONE |

## Notes
- Tasks are marked DONE for local essential scaffolding.
- CUDA-server data provisioning and full training reproduction remain pending.
