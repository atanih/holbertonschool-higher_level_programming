#!/usr/bin/python3
"""This module defines a Square class."""
Rectangle = _import_('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return a string description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
