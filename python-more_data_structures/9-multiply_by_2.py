#!/usr/bin/python3
"""Module that defines multiply_by_2."""


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2.

    The original dictionary is not modified.

    Args:
        a_dictionary (dict): the input dictionary with integer values.

    Returns:
        dict: a new dictionary with the same keys and values multiplied by 2.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
