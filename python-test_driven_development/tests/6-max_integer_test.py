#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the function max_integer"""

    def test_empty_list(self):
        """An empty list must return None"""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument must return None"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """A list with a single element returns that element"""
        self.assertEqual(max_integer([7]), 7)

    def test_max_at_the_end(self):
        """The biggest number is the last one"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_the_beginning(self):
        """The biggest number is the first one"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_the_middle(self):
        """The biggest number is in the middle"""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_negative_numbers(self):
        """A list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """A list with negative and positive numbers"""
        self.assertEqual(max_integer([-1, 0, 5, -10]), 5)

    def test_floats(self):
        """A list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_ints_and_floats(self):
        """A list mixing integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_duplicated_max(self):
        """The biggest number appears several times"""
        self.assertEqual(max_integer([3, 3, 1, 3]), 3)

    def test_strings(self):
        """A list of strings returns the biggest string"""
        self.assertEqual(max_integer(["ab", "cd", "ef"]), "ef")

    def test_string(self):
        """A string returns its biggest character"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_list_of_lists(self):
        """A list of lists returns the biggest list"""
        self.assertEqual(max_integer([[1, 2], [3]]), [3])

    def test_mixed_types(self):
        """Comparing different types raises a TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

    def test_none(self):
        """None is not iterable"""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
