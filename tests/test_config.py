from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from anima_su_yolo.config import load_config


class TestConfig(unittest.TestCase):
    def test_load_paper_config(self) -> None:
        cfg = load_config(ROOT / "configs/paper.toml")
        self.assertEqual(cfg.module.name, "su_yolo")
        self.assertEqual(cfg.train.time_step, 4)
        self.assertEqual(cfg.train.epochs, 300)
        self.assertEqual(cfg.train.img_size, 320)


if __name__ == "__main__":
    unittest.main()
