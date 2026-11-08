"""Behavior checks using Python's standard-library unittest runner."""

from pathlib import Path
import subprocess
import sys
import unittest

from garden_advice import get_advice

APP = Path(__file__).with_name("garden_advice.py")


class GardenAdviceTests(unittest.TestCase):
    def test_all_season_and_plant_combinations(self):
        seasonal_phrases = {
            "spring": "Prepare the soil",
            "summer": "Water your plants",
            "autumn": "Add mulch",
            "winter": "Protect your plants from frost",
        }
        plant_phrases = {"flower": "encourage blooms", "vegetable": "pests!"}
        for season, season_phrase in seasonal_phrases.items():
            for plant, plant_phrase in plant_phrases.items():
                with self.subTest(season=season, plant=plant):
                    lines = get_advice(season, plant).splitlines()
                    self.assertEqual(len(lines), 2)
                    self.assertIn(season_phrase, lines[0])
                    self.assertIn(plant_phrase, lines[1])

    def test_choices_are_case_insensitive_and_trimmed(self):
        self.assertEqual(get_advice(" SUMMER ", " Flower "),
                         get_advice("summer", "flower"))

    def test_unsupported_choices_are_rejected(self):
        for season, plant in [("monsoon", "flower"), ("summer", "tree"),
                              ("", "flower"), ("winter", "")]:
            with self.subTest(season=season, plant=plant):
                with self.assertRaises(ValueError):
                    get_advice(season, plant)

    def test_cli_retries_invalid_choices(self):
        result = subprocess.run(
            [sys.executable, str(APP)], input="invalid\n WINTER \ntree\n VEGETABLE \n",
            capture_output=True, text=True, check=True,
        )
        self.assertEqual(result.stdout.count("Please choose one of:"), 2)
        self.assertIn("Protect your plants from frost", result.stdout)
        self.assertIn("Keep an eye out for pests!", result.stdout)

    def test_import_has_no_interactive_side_effects(self):
        result = subprocess.run(
            [sys.executable, "-c", "import garden_advice"], cwd=APP.parent,
            input="", capture_output=True, text=True, check=True,
        )
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")

    def test_cli_handles_end_of_input(self):
        result = subprocess.run(
            [sys.executable, str(APP)], input="summer\n",
            capture_output=True, text=True, check=True,
        )
        self.assertIn("Gardening advice cancelled.", result.stdout)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
