#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square."""

    def _init_(self, size):
        """Initializes a new Square.

        Args:
            size: The size of the new square.
        """
        self.__size = size
        