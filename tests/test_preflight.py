from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from anima_su_yolo.config import load_config
from anima_su_yolo.preflight import run_preflight


class TestPreflight(unittest.TestCase):
    def test_preflight_report_schema(self) -> None:
        cfg = load_config(ROOT / "configs/paper.toml")
        report = run_preflight(cfg)
        self.assertIn("all_ok", report)
        self.assertIn("checks", report)
        self.assertIn("dataset_checks", report)
        self.assertIn("targets", report)
        self.assertIn("paper_pdf", report["checks"])


if __name__ == "__main__":
    unittest.main()
