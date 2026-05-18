#!/usr/bin/python3
"""Module that defines only_diff_elements."""


def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set.

    Args:
        set_1 (set): the first set.
        set_2 (set): the second set.

    Returns:
        set: a set containing elements present in only one of the two sets
        (i.e., the symmetric difference).
    """
    return set_1 ^ set_2
