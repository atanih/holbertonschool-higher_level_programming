#!/usr/bin/python3
"""Module 7-base_geometry.

Defines a class ``BaseGeometry`` with an unimplemented area and an
integer validator.
"""


class BaseGeometry:
    """Represent the base geometry of every shape."""

    def area(self):
        """Raise an Exception because area is not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that ``value`` is a positive integer.

        Args:
            name (str): the name of the value, used in the messages.
            value (int): the value to validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
