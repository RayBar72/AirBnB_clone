#!/usr/bin/python3
""" Testing for test base """
import unittest
from models.base_model import BaseModel
import models
from datetime import datetime


class Test_clase_m(unittest.TestCase):
    """ Test for class mode """
    Model = BaseModel()

    def test_none(self):
        """ Test for base if thi os none """
        self.assertIsNone(None, self.Model.__dict__.values())

    def test_BaseM(self):
        """ Test for testModel global """
        model_id = BaseModel()
        id = model_id.id
        self.assertNotEqual(id, self.Model.id)

    def test_save(self):
        """ Test fot method save """
        test_save = BaseModel()
        update = test_save.updated_at
        test_save.save()
        update2 = test_save.updated_at
        self.assertNotEqual(update, update2)

    def test_name_Number(self):
        """ Test for name and number """
        self.Model.name = "The better team"
        self.Model.my_number = 2001
        self.assertEqual(self.Model.name, "The better team")
        self.assertEqual(self.Model.my_number, 2001)

    def test_class(self):
        """ test for class method """
        self.assertEqual(self.Model.__class__.__name__, "BaseModel")

    def test_dataTime(self):
        """ Test for data"""
        self.assertEqual(isinstance(self.Model.created_at, datetime), True)
        self.assertEqual(isinstance(self.Model.updated_at, datetime), True)

    def test_dict(self):
        """ Test for dict"""
        self.assertEqual(type(self.Model.__dict__), dict)

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

if __name__ == '__main__':
    unittest.main()
