#!/usr/bin/python3
"""Module that defines simple_delete."""


def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary.

    If the key does not exist, the dictionary is not changed.

    Args:
        a_dictionary (dict): the dictionary to modify.
        key (str): the key to delete (default empty string).

    Returns:
        dict: the (possibly modified) dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
