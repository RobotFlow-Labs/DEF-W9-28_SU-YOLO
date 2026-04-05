from __future__ import annotations

from pathlib import Path
from typing import Sequence

from .config import ModuleConfig


def _script(cfg: ModuleConfig, script_name: str) -> str:
    return str((cfg.repo_path / script_name).resolve())


def build_train_command(cfg: ModuleConfig) -> list[str]:
    c = cfg.train
    return [
        c.python,
        _script(cfg, c.script),
        "--workers",
        str(c.workers),
        "--device",
        c.device,
        "--batch",
        str(c.batch_size),
        "--data",
        str(cfg.repo_path / c.data),
        "--img",
        str(c.img_size),
        "--cfg",
        str(cfg.repo_path / c.cfg),
        "--name",
        c.run_name,
        "--epochs",
        str(c.epochs),
        "--time-step",
        str(c.time_step),
        "--hyp",
        str(cfg.repo_path / c.hyp),
    ]


def build_eval_command(cfg: ModuleConfig) -> list[str]:
    c = cfg.evaluate
    return [
        c.python,
        _script(cfg, c.script),
        "--device",
        c.device,
        "--batch",
        str(c.batch_size),
        "--data",
        str(cfg.repo_path / c.data),
        "--img",
        str(c.img_size),
        "--weights",
        c.weights,
    ]


def build_infer_command(cfg: ModuleConfig) -> list[str]:
    c = cfg.infer
    cmd = [
        c.python,
        _script(cfg, c.script),
        "--weights",
        c.weights,
        "--img",
        str(c.img_size),
        "--conf-thres",
        str(c.conf_thres),
        "--device",
        c.device,
    ]
    if c.source:
        cmd += ["--source", c.source]
    return cmd


def build_export_command(cfg: ModuleConfig) -> list[str]:
    c = cfg.export
    return [
        c.python,
        _script(cfg, c.script),
        "--weights",
        c.weights,
        "--imgsz",
        str(c.img_size),
        "--device",
        c.device,
        "--include",
        c.include,
    ]


def as_shell(cmd: Sequence[str]) -> str:
    return " ".join(str(x) for x in cmd)
