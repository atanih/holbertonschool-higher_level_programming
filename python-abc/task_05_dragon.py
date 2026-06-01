#!/usr/bin/env python3
"""This module defines SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """A mixin that provides swimming ability."""

    def swim(self):
        """Print swimming message."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying ability."""

    def fly(self):
        """Print flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon class that inherits from SwimMixin and FlyMixin."""

    def roar(self):
        """Print roaring message."""
        print("The dragon roars!")
