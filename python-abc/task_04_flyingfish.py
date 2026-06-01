#!/usr/bin/env python3
"""This module defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """A fish class."""

    def swim(self):
        """Print swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat message."""
        print("The fish lives in water")


class Bird:
    """A bird class."""

    def fly(self):
        """Print flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A flying fish class that inherits from Fish and Bird."""

    def swim(self):
        """Print swimming message."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print flying message."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print habitat message."""
        print("The flying fish lives both in water and the sky!")
