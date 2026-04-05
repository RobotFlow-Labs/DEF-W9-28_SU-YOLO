from __future__ import annotations

import argparse
import subprocess

from .commands import as_shell, build_infer_command
from .config import load_config


def main() -> int:
    parser = argparse.ArgumentParser(description="SU-YOLO inference wrapper")
    parser.add_argument("--config", default="configs/paper.toml")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cfg = load_config(args.config)
    cmd = build_infer_command(cfg)

    if args.dry_run:
        print(as_shell(cmd))
        return 0

    return subprocess.run(cmd, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
