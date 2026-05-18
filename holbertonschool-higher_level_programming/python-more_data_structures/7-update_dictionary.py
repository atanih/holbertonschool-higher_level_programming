#!/usr/bin/python3
"""Module that defines update_dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Replace or add a key/value pair in a dictionary.

    If the key already exists, its value is replaced. If the key does not
    exist, it is created.

    Args:
        a_dictionary (dict): the dictionary to update.
        key (str): the key to add or update.
        value: the new value (can be of any type).

    Returns:
        dict: the updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
