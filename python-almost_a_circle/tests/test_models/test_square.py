#!/usr/bin/python3
"""
Test for the Square class
"""

import unittest
import json
from models import square
from models.base import Base
Square = square.Square

class TestSquare(unittest.TestCase):
    """
    TestSquare class to test the Square class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to initialize test instances.
        """
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)

    def test_id(self):
        """
        Test the 'id' attribute of Square objects.
        """
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)

    def test_size(self):
        """
        Test the 'size' attribute of Square objects.
        """
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)

    def test_width(self):
        """
        Test the 'width' attribute of Square objects.
        """
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s2.width, 2)

    def test_height(self):
        """
        Test the 'height' attribute of Square objects.
        """
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 2)

    def test_x(self):
        """
        Test the 'x' attribute of Square objects.
        """
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)

    def test_y(self):
        """
        Test the 'y' attribute of Square objects.
        """
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)

    def mandatory_size(self):
        """
        Test for mandatory 'size' argument.
        """
        with self.assertRaises(TypeError):
            s = Square()

    def size_typeerror(self):
        """
        Test for 'size' argument type errors.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True)

    def test_x_typeerror(self):
        """
        Test for 'x' argument type errors.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, True)

    def test_y_typeerror(self):
        """
        Test for 'y' argument type errors.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, True)

    def test_size_valueerror(self):
        """
        Test for 'size' argument value errors.
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_x_valueerror(self):
        """
        Test for 'x' argument value errors.
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

    def test_y_valueerror(self):
        """
        Test for 'y' argument value errors.
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)

    def test_area(self):
        """
        Test the 'area' method of Square objects.
        """
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)

    def test_area_args(self):
        """
        Test for extra arguments in 'area' method.
        """
        with self.assertRaises(TypeError):
            a = self.s1.area(1)

    def test_display_too_many_args(self):
        """
        Test for extra arguments in 'display' method.
        """
        with self.assertRaises(TypeError):
            self.s1.display(1)
