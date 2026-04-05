from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import re

from .config import ModuleConfig


@dataclass
class CheckResult:
    ok: bool
    detail: str


def _parse_dataset_yaml(dataset_yaml: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not dataset_yaml.exists():
        return out
    for line in dataset_yaml.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(train|val|test)\s*:\s*(.+)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def run_preflight(cfg: ModuleConfig) -> dict:
    repo = cfg.repo_path
    train_cfg = cfg.train
    dataset_yaml = repo / train_cfg.data
    dataset_paths = _parse_dataset_yaml(dataset_yaml)

    checks: dict[str, CheckResult] = {
        "paper_pdf": CheckResult(cfg.paper_pdf_path.exists(), str(cfg.paper_pdf_path)),
        "paper_txt": CheckResult(cfg.paper_txt_path.exists(), str(cfg.paper_txt_path)),
        "repo_root": CheckResult(repo.exists(), str(repo)),
        "train_script": CheckResult((repo / "train.py").exists(), str(repo / "train.py")),
        "val_script": CheckResult((repo / "val.py").exists(), str(repo / "val.py")),
        "detect_script": CheckResult((repo / "detect.py").exists(), str(repo / "detect.py")),
        "model_cfg": CheckResult((repo / train_cfg.cfg).exists(), str(repo / train_cfg.cfg)),
        "hyp_cfg": CheckResult((repo / train_cfg.hyp).exists(), str(repo / train_cfg.hyp)),
        "data_yaml": CheckResult(dataset_yaml.exists(), str(dataset_yaml)),
    }

    dataset_checks: dict[str, CheckResult] = {}
    for split, rel in dataset_paths.items():
        resolved = (repo / rel).resolve()
        dataset_checks[split] = CheckResult(resolved.exists(), str(resolved))

    all_ok = all(v.ok for v in checks.values()) and all(v.ok for v in dataset_checks.values())

    return {
        "module": cfg.module.name,
        "all_ok": all_ok,
        "checks": {k: {"ok": v.ok, "detail": v.detail} for k, v in checks.items()},
        "dataset_checks": {k: {"ok": v.ok, "detail": v.detail} for k, v in dataset_checks.items()},
        "targets": {
            "urpc_map50": cfg.targets.urpc_map50,
            "urpc_map5095": cfg.targets.urpc_map5095,
            "udd_map50": cfg.targets.udd_map50,
            "udd_map5095": cfg.targets.udd_map5095,
            "params_m": cfg.targets.params_m,
            "energy_mj": cfg.targets.energy_mj,
        },
    }


def report_json(report: dict) -> str:
    return json.dumps(report, indent=2, sort_keys=True)
