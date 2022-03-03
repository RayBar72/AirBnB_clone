#!usr/bin/python3
"""Testing for BaseModel"""


import imp


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Testing for basemodel.py archive"""

    def setUp(self):
        """Setting casses for testing enviroment"""
        self.b1 = BaseModel()
        self.b2 = BaseModel()
        self.b1 = "Ray"
        self.b2 = "Mati"

    def test_3_00_create(self):
        """Tests the creation of BaseModel"""
        self.assertTrue(self.b1)
        self.assertTrue(self.b2)

    def test_3_01_id(self):
        """Tests ID and compares them"""
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_3_02_attr(self):
        """Tets created attributes"""
        self.assertEqual(self.b1.name, "Ray")
        self.assertEqual(self.b2.name, "Maty")
        self.assertNotEqual(self.b1.name, self.b2.name)

    def test_3_03_toDict(self):
        """Tests output when using to_dict()"""
        self.assertFalse("__class__" in self.b1.__dict__)
        self.assertFalse("__class__" in self.b2.__dict__)
        dict_check = self.b1.to_dict()
        self.assertTrue("__class__" in dict_check)
        self.assertFalse("__class__" in self.b2.__dict__)

    def test_3_04_changing_name(self):
        """Tests changing the name"""
        self.b1.name = "Raymundo"
        self.assertTrue(self.b1.name, "Raymundo")

    def test_3_05_compare_create_and_update(self):
        """Tests update"""
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)

    def test_3_06_update(self):
        """Tests update. Secound"""
        tmp = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(tmp, self.b1.updated_at)

    def test_3_07_id_length(self):
        """Test if id is the right amount of characters"""
        self.assertTrue(len(self.b1.id), 36)
        self.assertTrue(len(self.b2.id), 36)

    def test_3_08_user_attr(self):
        """Checks to see if a user created attribute is updated"""
        self.assertFalse("number" in self.b1.__dict__)
        self.assertFalse("number" in self.b2.__dict__)
        self.b1.number = 22
        self.assertTrue("number" in self.b1.__dict__)
        self.assertFalse("number" in self.b2.__dict__)

    def tearDown(self):
        """Breaks down the testing environment"""

        pass