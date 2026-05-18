#!/usr/bin/python3
"""Module that defines roman_to_int."""


def roman_to_int(roman_string):
    """Convert a Roman numeral string to an integer.

    Args:
        roman_string (str): a Roman numeral between 1 and 3999.

    Returns:
        int: the integer value of roman_string, or 0 if roman_string
        is not a string or is None.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(roman_string)):
        current = values.get(roman_string[i], 0)
        if i + 1 < len(roman_string) and \
                current < values.get(roman_string[i + 1], 0):
            total -= current
        else:
            total += current
    return total
