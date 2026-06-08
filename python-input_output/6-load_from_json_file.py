#!/usr/bin/python3
"""Module for creating a Python object from a JSON file"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename: The name of the JSON file to read from

    Returns:
        The Python object represented by the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
