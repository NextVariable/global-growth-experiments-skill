"""Check calculation against fixed examples and boundary cases, not prose."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "skills/global-growth-experiments/scripts/conversion_summary.py"
SPEC = importlib.util.spec_from_file_location("conversion_summary", SCRIPT)
CALC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CALC)


class ConversionTests(unittest.TestCase):
    def test_wilson_reference(self):
        # 50/100: standard Wilson 95% interval around one half.
        result = CALC.group_summary(50, 100)
        self.assertAlmostEqual(result["wilson_95"][0], 0.4038315303659956)
        self.assertAlmostEqual(result["wilson_95"][1], 0.5961684696340044)

    def test_absolute_and_relative_are_distinct(self):
        result = CALC.summarize(20, 100, 30, 100)
        self.assertAlmostEqual(result["difference_percentage_points"], 10)
        self.assertAlmostEqual(result["relative_change_percent"], 50)

    def test_zero_baseline_is_undefined_relative(self):
        result = CALC.summarize(0, 10, 1, 10)
        self.assertIsNone(result["relative_change_percent"])
        self.assertAlmostEqual(result["control"]["wilson_95"][0], 0)
        self.assertAlmostEqual(result["control"]["wilson_95"][1], 0.2775327998628892)

    def test_full_conversion_has_uncertainty(self):
        interval = CALC.group_summary(10, 10)["wilson_95"]
        self.assertAlmostEqual(interval[0], 0.7224672001371107)
        self.assertAlmostEqual(interval[1], 1)

    def test_invalid_counts_rejected(self):
        for pair in ((0, 0), (-1, 20), (21, 20), (1.5, 20), (True, 20), (1, -20), (1, 10**13)):
            with self.subTest(pair=pair), self.assertRaises(ValueError):
                CALC.group_summary(*pair)

    def test_cli_rejects_invalid_without_json(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "--control", "2", "1", "--variant", "1", "5"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

    def test_cli_outputs_finite_json(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "--control", "0", "5", "--variant", "0", "7"], capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        self.assertIsNone(data["relative_change_percent"])
        self.assertEqual(data["difference_percentage_points"], 0)


if __name__ == "__main__":
    unittest.main()
