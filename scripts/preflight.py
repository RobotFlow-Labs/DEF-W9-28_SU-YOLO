#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from anima_su_yolo.config import load_config
from anima_su_yolo.preflight import report_json, run_preflight


def main() -> int:
    parser = argparse.ArgumentParser(description="SU-YOLO preflight")
    parser.add_argument("--config", default="configs/paper.toml")
    args = parser.parse_args()

    cfg = load_config(args.config)
    report = run_preflight(cfg)
    print(report_json(report))
    return 0 if report.get("all_ok", False) else 2


if __name__ == "__main__":
    raise SystemExit(main())
