#!/usr/bin/python3
"""Test for state file"""

from models.place import Place
import unittest


class Test_Place(unittest.TestCase):
    """Test for state class"""

    def test_doc(self):
        """test for documentation"""
        self.assertTrue(len(Place.__doc__) > 0)
