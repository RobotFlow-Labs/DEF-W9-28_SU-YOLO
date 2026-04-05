#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from anima_su_yolo.commands import (
    as_shell,
    build_eval_command,
    build_infer_command,
    build_train_command,
)
from anima_su_yolo.config import load_config


def main() -> int:
    cfg = load_config(ROOT / "configs/paper.toml")
    print("TRAIN:", as_shell(build_train_command(cfg)))
    print("EVAL:", as_shell(build_eval_command(cfg)))
    print("INFER:", as_shell(build_infer_command(cfg)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
