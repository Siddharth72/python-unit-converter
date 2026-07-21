"""
===============================================================================
Project     : Unit Converter
File        : temperature.py
Author      : Siddharth Navaneethan

Description :
    Contains functions for converting temperature units.

Supported Conversions:
    - Celsius to Fahrenheit
    - Fahrenheit to Celsius

Version     : 1.0
===============================================================================
"""
import logging

logger = logging.getLogger(__name__)

SUPPORTED_UNITS = {
    "celsius",
    "fahrenheit"
}

CONVERSIONS = {
    ("celsius", "fahrenheit"): lambda x: (x * 9 / 5) + 32,
    ("fahrenheit", "celsius"): lambda x: (x - 32) * 5 / 9,
}


def convert_temperature(value: float, from_unit: str, to_unit: str):
    """
    Convert temperature between supported units.
    """

    from_unit = from_unit.strip().lower()
    to_unit = to_unit.strip().lower()

    if from_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported source unit: {from_unit}")

    if to_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    if from_unit == to_unit:
        return value, to_unit

    conversion = CONVERSIONS.get((from_unit, to_unit))

    if conversion:
        logger.info(
            "Converting %s to %s",
            from_unit.title(),
            to_unit.title()
        )
        return conversion(value), to_unit

    raise ValueError(
        f"Conversion from '{from_unit}' to '{to_unit}' is not supported."
    )