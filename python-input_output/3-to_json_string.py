#!/usr/bin/python3
"""Module for converting an object to its JSON string representation"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj: The object to serialize to JSON

    Returns:
        The JSON string representation of my_obj
    """
    return json.dumps(my_obj)
