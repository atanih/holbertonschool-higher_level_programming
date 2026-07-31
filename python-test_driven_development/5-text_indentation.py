#!/usr/bin/python3
"""Module 5-text_indentation.

Defines a single function ``text_indentation`` that prints a text with
2 new lines after each of these characters: ``.``, ``?`` and ``:``.
"""


def text_indentation(text):
    """Print ``text`` with 2 new lines after each '.', '?' and ':'.

    ``text`` must be a string, otherwise a TypeError is raised. Printed
    lines have no space at the beginning nor at the end.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
