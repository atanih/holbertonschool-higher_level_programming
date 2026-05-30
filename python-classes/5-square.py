#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class defines a square."""

    def _init_(self, size=0):
        """Initialize a new Square instance with an optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the # character, or an empty line if size is 0."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print("#" * self.__size)
            