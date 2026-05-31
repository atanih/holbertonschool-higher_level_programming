#!/usr/bin/python3
"""This module defines a Square class."""
Rectangle = _import_('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle."""

    def _init_(self, size):
        """Initialize a new Square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super()._init_(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def _str_(self):
        """Return a string description of the square."""
        return "[Square] {}/{}".format(self._size, self._size)
