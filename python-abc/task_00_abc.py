#!/usr/bin/env python3
"""This module defines Animal, Dog, and Cat classes."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """An abstract animal class."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """A dog class that inherits from Animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """A cat class that inherits from Animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
