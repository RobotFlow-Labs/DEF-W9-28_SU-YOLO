# PRD-02: Core Model Alignment

> Module: SU-YOLO | Priority: P0
> Depends on: PRD-01
> Status: DONE

## Objective
Capture paper-aligned model/training defaults (SeBN, SpikeDenoiser, SU-Blocks, T=4) in strongly-typed module configuration.

## Context (from paper)
Key architectural elements are SU-Block1/2, SpikeDenoiser, SpikeSPP, SeBN, and IF-based spiking flow with best performance at 4 time steps.
Paper reference: Sections 3.1, 3.2, 3.3, 4.3.7.

## Acceptance Criteria
- [x] Module config includes time_step, model cfg, hyp path, dataset YAML path.
- [x] Default paper-aligned values match upstream command recipe.
- [x] Command-building logic can emit equivalent train command to upstream.
- [x] Unit test validates key command args (`--time-step 4`, `--epochs 300`, `--img 320`).

## Files to Create
- `src/anima_su_yolo/config.py`
- `src/anima_su_yolo/commands.py`
- `tests/test_commands.py`

## References
- Paper tables: Table 1, Table 7
- Upstream model cfg: `repositories/snn-underwater/models/detect/su-yolo.yaml`
- Upstream trainer: `repositories/snn-underwater/train.py`
