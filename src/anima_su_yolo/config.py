from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import tomllib


@dataclass
class ModuleSection:
    name: str
    repo_root: str
    paper_pdf: str
    paper_txt: str


@dataclass
class TrainSection:
    python: str
    script: str
    cfg: str
    data: str
    hyp: str
    weights: str
    project: str
    run_name: str
    time_step: int
    epochs: int
    batch_size: int
    img_size: int
    device: str
    workers: int


@dataclass
class EvalSection:
    python: str
    script: str
    data: str
    weights: str
    img_size: int
    batch_size: int
    device: str


@dataclass
class InferSection:
    python: str
    script: str
    source: str
    weights: str
    img_size: int
    conf_thres: float
    device: str


@dataclass
class ExportSection:
    python: str
    script: str
    weights: str
    img_size: int
    device: str
    include: str


@dataclass
class TargetsSection:
    urpc_map50: float
    urpc_map5095: float
    udd_map50: float
    udd_map5095: float
    params_m: float
    energy_mj: float


@dataclass
class ModuleConfig:
    root: Path
    module: ModuleSection
    train: TrainSection
    evaluate: EvalSection
    infer: InferSection
    export: ExportSection
    targets: TargetsSection

    @property
    def repo_path(self) -> Path:
        return (self.root / self.module.repo_root).resolve()

    @property
    def paper_pdf_path(self) -> Path:
        return (self.root / self.module.paper_pdf).resolve()

    @property
    def paper_txt_path(self) -> Path:
        return (self.root / self.module.paper_txt).resolve()


def _section(data: dict, key: str) -> dict:
    if key not in data:
        raise KeyError(f"Missing [{key}] section in TOML config")
    return data[key]


def load_config(config_path: str | Path) -> ModuleConfig:
    path = Path(config_path).resolve()
    raw = tomllib.loads(path.read_text(encoding="utf-8"))

    module = ModuleSection(**_section(raw, "module"))
    train = TrainSection(**_section(raw, "train"))
    evaluate = EvalSection(**_section(raw, "evaluate"))
    infer = InferSection(**_section(raw, "infer"))
    export = ExportSection(**_section(raw, "export"))
    targets = TargetsSection(**_section(raw, "targets"))

    return ModuleConfig(
        root=path.parent.parent,
        module=module,
        train=train,
        evaluate=evaluate,
        infer=infer,
        export=export,
        targets=targets,
    )
