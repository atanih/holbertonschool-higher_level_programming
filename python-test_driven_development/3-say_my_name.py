#!/usr/bin/python3
"""Module 3-say_my_name.

Defines a single function ``say_my_name`` that prints a full name.
"""


def say_my_name(first_name, last_name=""):
    """Print ``My name is <first name> <last name>``.

    Both arguments must be strings, otherwise a TypeError is raised.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
