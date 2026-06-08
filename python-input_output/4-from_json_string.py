#!/usr/bin/python3
"""Module for converting a JSON string to a Python object"""
import json


def from_json_string(my_str):
    """Return a Python object represented by a JSON string.

    Args:
        my_str: The JSON string to deserialize

    Returns:
        The Python data structure represented by my_str
    """
    return json.loads(my_str)
