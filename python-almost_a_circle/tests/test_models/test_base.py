#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
import json
from models import base
Base = base.Base

class TestBase(unittest.TestCase):
    """
    Test cases for the Base class and its methods.
    """

    def test_too_many_args(self):
        """
        Test if a TypeError is raised when too many arguments are provided.
        """
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_no_id(self):
        """
        Test if an object is assigned an ID when no ID is provided.
        """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_set(self):
        """
        Test if an object's ID is correctly set when an ID is provided.
        """
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def test_no_id_after_set(self):
        """
        Test if subsequent objects are assigned incrementing IDs.
        """
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_nb_private(self):
        """
        Test if the '__nb_objects' attribute is private and cannot be accessed directly.
        """
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_to_json_string(self):
        """
        Test the 'to_json_string' method.
        """
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_empty_to_json_string(self):
        """
        Test 'to_json_string' with an empty list.
        """
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_None_to_json_string(self):
        """
        Test 'to_json_string' with None as input.
        """
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """
        Test the 'from_json_string' method.
        """
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_frjs_empty(self):
        """
        Test 'from_json_string' with an empty string.
        """
        self.assertEqual([], Base.from_json_string(""))

    def test_frjs_None(self):
        """
        Test 'from_json_string' with None as input.
        """
        self.assertEqual([], Base.from_json_string(None))
