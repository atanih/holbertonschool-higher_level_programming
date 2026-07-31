#!/usr/bin/python3
"""Module 4-print_square.

Defines a single function ``print_square`` that prints a square with
the character ``#``.
"""


def print_square(size):
    """Print a square of ``size`` made of the character ``#``.

    ``size`` must be an integer greater or equal to 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
