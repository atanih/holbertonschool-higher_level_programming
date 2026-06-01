#!/usr/bin/env python3
"""This module defines Shape, Circle, Rectangle classes and shape_info."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """An abstract shape class."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """A circle class that inherits from Shape."""

    def _init_(self, radius):
        """Initialize a new Circle with radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A rectangle class that inherits from Shape."""

    def _init_(self, width, height):
        """Initialize a new Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
