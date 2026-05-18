#!/usr/bin/python3
"""Module that defines print_sorted_dictionary."""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys.

    Keys are sorted alphabetically (ASCII order). Only first-level keys
    are sorted; nested dictionaries are not sorted.

    Args:
        a_dictionary (dict): the dictionary to print. Keys are strings;
            values can be of any type.
    """
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
