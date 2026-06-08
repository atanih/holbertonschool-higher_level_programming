#!/usr/bin/python3
"""Module for appending a string to a text file"""


def append_write(filename="", text=""):
    """Append a string at the end of
    a text file and return the number of characters added.

    Args:
        filename: The name of the file to append to
        text: The string to append to the file

    Returns:
        The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
