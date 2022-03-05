#!/usr/bin/python3
""" Testing for test base """

import pycodestyle
import unittest
from models.base_model import BaseModel
import models
from datetime import datetime


class Test_clase_m(unittest.TestCase):
    """ Test for class mode """
    Model = BaseModel()

    def test_pep8_base(self):
        """Test pycodestyle for base_model"""
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/base_model.py'])
        self.assertEqual(
                check.total_errors, 0,
                "Pycodestyle errors found in models"
        )

    def test_none(self):
        """ Test for base if thi os none """
        self.assertIsNone(None, self.Model.__dict__.values())

    def test_ID(self):
        """ Test for ID """
        model_id = BaseModel()
        id = model_id.id
        self.assertNotEqual(id, self.Model.id)
        self.assertEqual(type(id), str)

    def test_update(self):
        """ Test fot method save """
        Model = BaseModel()
        self.assertTrue(hasattr(Model, "updated_at"))

    def test_created(self):
        """Test fot created"""
        Model = BaseModel()
        self.assertTrue(hasattr(Model, "created_at"))

    def test_name_Number(self):
        """ Test for name and number """
        self.Model.name = "Holberton"
        self.Model.my_number = 2022
        self.assertEqual(self.Model.name, "Holberton")
        self.assertEqual(self.Model.my_number, 2022)

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

    def test_str(self):
        """test for str method"""
        Model = BaseModel()
        model_str = f'[{BaseModel.__name__}] ({Model.id}) {Model.__dict__}'
        self.assertEqual(model_str, str(Model))
    
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
