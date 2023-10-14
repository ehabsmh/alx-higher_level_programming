#!/usr/bin/python3

"""
Testing base module
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Defines tests for Base class"""

    def test_id(self):
        """id test for Base class"""

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b1.id, 1)
        self.assertNotEqual(b1.id, b2.id)
        self.assertIsInstance(b1, Base)
        self.assertIsInstance(b2, Base)

        with self.assertRaises(AttributeError):
            self.assertEqual(b2.__nb_objects, 1)
            self.assertEqual(b2.nb_objects, 1)
