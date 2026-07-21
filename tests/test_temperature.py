import unittest

from temperature import convert_temperature


class TestTemperatureConversion(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        result, unit = convert_temperature(
            0,
            "celsius",
            "fahrenheit"
        )

        self.assertEqual(result, 32)
        self.assertEqual(unit, "fahrenheit")

    def test_fahrenheit_to_celsius(self):
        result, unit = convert_temperature(
            32,
            "fahrenheit",
            "celsius"
        )

        self.assertEqual(result, 0)
        self.assertEqual(unit, "celsius")


if __name__ == "__main__":
    unittest.main()