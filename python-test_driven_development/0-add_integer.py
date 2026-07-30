#!/usr/bin/python3
"""Module 0-add_integer.

Defines a single function ``add_integer`` that adds two numbers
and always returns an integer.
"""


def add_integer(a, b=98):
    """Add two integers.

    ``a`` and ``b`` must be integers or floats, floats are casted
    to integers before the addition. Returns an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
