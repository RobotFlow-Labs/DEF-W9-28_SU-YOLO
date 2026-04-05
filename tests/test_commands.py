from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from anima_su_yolo.commands import (
    build_eval_command,
    build_infer_command,
    build_train_command,
)
from anima_su_yolo.config import load_config


class TestCommands(unittest.TestCase):
    def setUp(self) -> None:
        self.cfg = load_config(ROOT / "configs/paper.toml")

    def test_train_command_contains_paper_defaults(self) -> None:
        cmd = build_train_command(self.cfg)
        text = " ".join(cmd)
        self.assertIn("--time-step 4", text)
        self.assertIn("--epochs 300", text)
        self.assertIn("--img 320", text)

    def test_eval_command_contains_weights(self) -> None:
        cmd = build_eval_command(self.cfg)
        text = " ".join(cmd)
        self.assertIn("--weights", text)

    def test_infer_command_contains_conf(self) -> None:
        cmd = build_infer_command(self.cfg)
        text = " ".join(cmd)
        self.assertIn("--conf-thres 0.25", text)


if __name__ == "__main__":
    unittest.main()
