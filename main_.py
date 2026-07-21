"""
===============================================================================
Project     : Unit Converter
File        : main.py
Author      : Siddharth Navaneethan
Description :
    Main entry point for the Unit Converter application.

    Supports:
        - Length Conversion
        - Temperature Conversion

Features:
    ✔ Modular Design
    ✔ Input Validation
    ✔ Exception Handling
    ✔ Logging
    ✔ Easy to Extend

Version     : 1.0
===============================================================================
"""

import logging

from length import convert_length
from temperature import convert_temperature

# -----------------------------------------------------------------------------
# Configure Logging
# -----------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
LENGTH = "length"
TEMPERATURE = "temperature"
QUIT = "quit"

CONVERTERS = {
    LENGTH: convert_length,
    TEMPERATURE: convert_temperature
}


def get_numeric_input():
    """
    Prompt the user for a numeric value.

    Returns
    -------
    float
        Valid numeric input entered by the user.
    """

    while True:
        try:
            return float(input("\nEnter the value to convert: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_conversion_type():
    """
    Prompt the user to select a conversion type.

    Returns
    -------
    str
        length, temperature, or quit
    """

    while True:

        conversion_type = input(
            "\nEnter conversion type "
            "(length / temperature / quit): "
        ).strip().lower()

        if conversion_type in CONVERTERS or conversion_type == QUIT:
            return conversion_type

        print("Invalid conversion type.")


def unit_converter():
    """
    Main application loop.
    """

    logger.info("Unit Converter Started")

    while True:

        conversion_type = get_conversion_type()

        if conversion_type == QUIT:
            print("\nThank you for using Unit Converter.")
            logger.info("Application Closed")
            break

        value = get_numeric_input()

        from_unit = input(
            "Enter source unit: "
        ).strip().lower()

        to_unit = input(
            "Enter target unit :  "
        ).strip().lower()

        try:

            converter = CONVERTERS[conversion_type]

            result, unit = converter(
                value,
                from_unit,
                to_unit
            )

            print("\n--------------------------------")
            print(f"Converted Value : {result:.2f} {unit}")
            print("--------------------------------")

            logger.info(
                "%s conversion completed successfully.",
                conversion_type.title()
            )

        except ValueError as error:

            logger.error(error)
            print(f" {error}")

        except Exception as error:

            logger.exception(error)
            print("An unexpected error occurred.")


def main():
    """
    Application entry point.
    """
    unit_converter()


if __name__ == "__main__":
    main()