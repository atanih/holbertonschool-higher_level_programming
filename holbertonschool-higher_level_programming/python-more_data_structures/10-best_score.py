#!/usr/bin/python3
"""Module that defines best_score."""


def best_score(a_dictionary):
    """Return the key with the biggest integer value in a dictionary.

    Args:
        a_dictionary (dict): a dictionary where values are integers.

    Returns:
        The key with the biggest value, or None if no score is found
        (i.e., the dictionary is None or empty).
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
