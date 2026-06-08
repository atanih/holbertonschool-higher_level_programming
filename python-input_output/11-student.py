#!/usr/bin/python3
"""Module that defines a Student class with disk serialization and reload"""


class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize Student instance.

        Args:
            first_name: The student's first name
            last_name: The student's last name
            age: The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs: A list of strings of attribute names to retrieve.
                   If None, all attributes are retrieved.

        Returns:
            A dictionary representation of the Student
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self._dict_

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.

        Args:
            json: A dictionary with attribute names as keys and values as values
        """
        for key, value in json.items():
            setattr(self, key, value)
