#!/usr/bin/python3
"""
Test for amenity class
"""

from models.amenity import Amenity
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class Testamenity(unittest.TestCase):
    """Test for the correct funcionamiento of amenity"""

    def test_Amenity(self):
        """ test for correct name, class and subclass"""
        amenity = Amenity()
        self.assertEqual(type(amenity), Amenity)
        self.assertEqual(amenity.__class__.__name__, "Amenity")
        self.assertTrue(issubclass(amenity.__class__, BaseModel))
        self.assertEqual(amenity.__class__, Amenity)
        self.assertEqual(type(amenity.__str__()), str)
        self.assertNotEqual(len(amenity.__str__()), 0)
        self.assertEqual(type(amenity.to_dict()), dict)

    def test_creatupdat(self):
        """created for created and updated"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "created_at"), True)
        self.assertEqual(type(amenity.created_at), datetime)
        self.assertTrue(hasattr(amenity, "updated_at"), True)
        self.assertEqual(type(amenity.updated_at), datetime)

    def test_str(self):
        """ Test for validate str format"""
        self.amenity = Amenity()
        string = "[{}] ({}) {}".format(self.amenity.__class__.__name__,
                                       self.amenity.id,
                                       self.amenity.__dict__)
        self.assertEqual(str(self.amenity), string)

    def test_equal(self):
        """ Test for validate id between both instances """
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()
        self.assertEqual(type(self.amenity1.id), str)
        self.assertNotEqual(self.amenity1.id, self.amenity2.id)

    def test_validatearg(self):
        """ Test to validate argumets save """
        self.amenity = Amenity()
        self.amenity.name = "Bañera"
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertIsInstance(self.amenity.name, str)

    if __name__ == '__main__':
        unittest.main()
