#!/usr/bin/python3
"""Module for writing a string to a text file"""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters written.

    Args:
        filename: The name of the file to write to
        text: The string to write to the file

    Returns:
        The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
