"""
===============================================================================
Project     : Unit Converter
File        : length.py
Author      : Siddharth Navaneethan

Description :
    Contains functions for converting length units.

Supported Conversions:
    - Meters to Feet
    - Feet to Meters

Version     : 1.0
===============================================================================
"""

import logging

logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Conversion Constants
# -----------------------------------------------------------------------------
METERS_TO_FEET = 3.28084

SUPPORTED_UNITS = {
    "meters",
    "feet"
}


def convert_length(value: float, from_unit: str, to_unit: str):
    """
    Convert length between supported units.

    Parameters
    ----------
    value : float
        Numeric value to convert.

    from_unit : str
        Source unit.

    to_unit : str
        Target unit.

    Returns
    -------
    tuple
        (converted_value, target_unit)

    Raises
    ------
    ValueError
        If the conversion is not supported.
    """

    from_unit = from_unit.strip().lower()
    to_unit = to_unit.strip().lower()

    if from_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported source unit: {from_unit}")

    if to_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    if from_unit == to_unit:
        logger.info("Source and target units are the same.")
        return value, to_unit

    if from_unit == "meters" and to_unit == "feet":
        logger.info("Converting meters to feet.")
        return value * METERS_TO_FEET, "feet"

    if from_unit == "feet" and to_unit == "meters":
        logger.info("Converting feet to meters.")
        return value / METERS_TO_FEET, "meters"

    raise ValueError(
        f"Conversion from '{from_unit}' to '{to_unit}' is not supported."
    )