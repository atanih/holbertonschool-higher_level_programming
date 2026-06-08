#!/usr/bin/env python3
"""Pickling Custom Classes - serialize/deserialize custom objects with pickle"""
import pickle


class CustomObject:
    """A custom Python class with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        """Initialize CustomObject.

        Args:
            name: A string representing the name
            age: An integer representing the age
            is_student: A boolean indicating if the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a formatted way."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle.

        Args:
            filename: The filename to save the serialized object
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject instance from a pickle file.

        Args:
            filename: The filename to load the serialized object from

        Returns:
            A CustomObject instance, or None if an error occurs
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
