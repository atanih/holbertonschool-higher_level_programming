#!/usr/bin/python3
"""Module for returning the dictionary description of
an object for JSON serialization"""


def class_to_json(obj):
    """Return the dictionary description with
    simple data structure for JSON serialization.

    Args:
        obj: An instance of a Class

    Returns:
        A dictionary representation of the object
    """
    return obj.__dict__
