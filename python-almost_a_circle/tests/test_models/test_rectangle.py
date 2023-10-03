#!/usr/bin/python3
"""
Test for the Rectangle class
"""

import unittest
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class and its methods.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up test class with instances of Rectangle.
        """
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(2, 3, 4)

    def test_id(self):
        """
        Test if the IDs of the rectangles are assigned correctly.
        """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)

    def test_width(self):
        """
        Test if the widths of the rectangles are correct.
        """
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)

    def test_height(self):
        """
        Test if the heights of the rectangles are correct.
        """
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 3)

    def test_x(self):
        """
        Test if the x-coordinates of the rectangles are correct.
        """
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)

    def test_y(self):
        """
        Test if the y-coordinates of the rectangles are correct.
        """
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)

    def test_width_typeerror(self):
        """
        Test if width raises TypeError when non-integer values are provided.
        """
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_height_typeerror(self):
        """
        Test if height raises TypeError when non-integer values are provided.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_width_typeerror(self):
        """
        Test if width raises TypeError when non-integer values are provided.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hello", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 1)

    def test_height_typeerror(self):
        """
        Test if height raises TypeError when non-integer values are provided.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, True)

    def test_x_typeerror(self):
        """
        Test if x raises TypeError when non-integer values are provided.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, True)

    def test_y_typeerror(self):
        """
        Test if y raises TypeError when non-integer values are provided.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, True)

    def test_width_valueerror(self):
        """
        Test if width raises ValueError when values less than or equal to 0 are provided.
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_height_valueerror(self):
        """
        Test if height raises ValueError when values less than or equal to 0 are provided.
        """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_x_valueerror(self):
        """
        Test if x raises ValueError when values less than 0 are provided.
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)

    def test_y_valueerror(self):
        """
        Test if y raises ValueError when values less than 0 are provided.
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """
        Test if the area of the rectangles is calculated correctly.
        """
        self.assertEqual(self.r1.area(), 100)
        self.assertEqual(self.r2.area(), 6)

    def test_area_args(self):
        """
        Test if the area method raises TypeError when arguments are provided.
        """
        with self.assertRaises(TypeError):
            r = self.r1.area(1)

    def test_display_too_many_args(self):
        """
        Test if display method raises TypeError when too many arguments are provided.
        """
        with self.assertRaises(TypeError):
            self.r1.display(1)

    def test_str(self):
        """
        Test if the string representation of the rectangles is correct.
        """
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/10")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")

    def test_update_args(self):
        """
        Test if the update method correctly updates attributes using positional arguments.
        """
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_setter(self):
        """
        Test if update method raises TypeError or ValueError when incorrect arguments are provided.
        """
        r = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, 1, -1)

    def test_update_too_many_args(self):
        """
        Test if update method raises an error when too many arguments are provided.
        """
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_no_args(self):
        """
        Test if update method does not change attributes when called with no arguments.
        """
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_mix_args_kwargs(self):
        """
        Test if update method can handle a mix of positional and keyword arguments.
        """
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")
