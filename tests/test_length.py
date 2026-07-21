import unittest

from length import convert_length


class TestLengthConversion(unittest.TestCase):

    def test_meter_to_feet(self):
        result, unit = convert_length(
            1,
            "meters",
            "feet"
        )

        self.assertAlmostEqual(result, 3.28084)
        self.assertEqual(unit, "feet")

    def test_feet_to_meter(self):
        result, unit = convert_length(
            3.28084,
            "feet",
            "meters"
        )

        self.assertAlmostEqual(result, 1)
        self.assertEqual(unit, "meters")


if __name__ == "__main__":
    unittest.main()
