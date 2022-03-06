#!/usr/bin/python3
"""
Test for amenity class
"""

from models.amenity import Amenity
import unittest
from models.base_model import BaseModel
from datetime import datetime


class Testamenity(unittest.TestCase):
    """Test for the correct funcionamiento of amenity"""

    def test_Amenity(self):
        """ test for correct name, class and subclass"""
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, "Amenity")
        self.assertTrue(issubclass(amenity.__class__, BaseModel))
        self.assertEqual(amenity.__class__, Amenity)
        
    def test_creatupdat(self):
        """created for created and updated"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "created_at"), True)
        self.assertEqual(type(amenity.created_at), datetime)
        self.assertTrue(hasattr(amenity, "updated_at"), True)
        self.assertEqual(type(amenity.updated_at), datetime)


