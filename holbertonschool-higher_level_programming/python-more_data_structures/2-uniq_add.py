#!/usr/bin/python3
"""Module that defines uniq_add."""


def uniq_add(my_list=[]):
    """Add all unique integers in a list (only once for each integer).

    Args:
        my_list (list of int): the input list.

    Returns:
        int: the sum of all unique integers in my_list.
    """
    return sum(set(my_list))
