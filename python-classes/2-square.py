#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """A square."""

    def _init_(self, size=0):
        """Init."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        