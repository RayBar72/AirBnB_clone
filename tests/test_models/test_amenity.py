#!/usr/bin/python3
"""
Test for amenity class
"""

from models.amenity import Amenity
import unittest
from models.base_model import BaseModel


class Testamenity(unittest.TestCase):
    """Test for the correct funcionamiento of amenity"""

    def test_Amenity(self):
        """ test for correct name"""
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, "Amenity")
        self.assertTrue(issubclass(amenity.__class__, BaseModel))
