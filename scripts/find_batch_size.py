#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math


def estimate_batch_size(gpu_mem_gb: float, target_util: float) -> int:
    # Paper recipe: batch 16 on 23GB L4 at img=320, T=4.
    baseline_mem = 23.0
    baseline_batch = 16
    scaled = baseline_batch * (gpu_mem_gb / baseline_mem) * (target_util / 0.75)
    return max(1, int(math.floor(scaled)))


def main() -> int:
    parser = argparse.ArgumentParser(description="Approximate SU-YOLO batch size")
    parser.add_argument("--gpu-mem-gb", type=float, default=23.0)
    parser.add_argument("--target", type=float, default=0.75)
    args = parser.parse_args()

    bs = estimate_batch_size(args.gpu_mem_gb, args.target)
    print(bs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
