#!/usr/bin/python3
""" Testing for test base """

import pycodestyle
import unittest
from models.base_model import BaseModel
import models
from datetime import datetime
import uuid


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
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)

    def test_method(self):
        """test correct methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_ID(self):
        """ Test for ID """
        model_id = BaseModel()
        mod_id = model_id.id
        self.assertNotEqual(mod_id, self.Model.id)
        self.assertEqual(type(mod_id), str)
        self.assertTrue(hasattr(model_id, "id"))
        uniqid = uuid.UUID(mod_id)
        self.assertEqual(uniqid.version, 4)

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
        Model = BaseModel()
        self.Model.name = "Holberton"
        self.Model.my_number = 22
        self.assertEqual(self.Model.name, "Holberton")
        self.assertEqual(self.Model.my_number, 22)
        self.assertEqual(type(self.Model.name), str)
        self.assertEqual(type(Model), BaseModel)
        self.assertTrue(hasattr(self.Model, "my_number"))

    def test_class(self):
        """ test for class method """
        self.assertEqual(self.Model.__class__.__name__, "BaseModel")

    def test_dataTime(self):
        """ Test for data"""
        self.assertEqual(isinstance(self.Model.created_at, datetime), True)
        self.assertEqual(isinstance(self.Model.updated_at, datetime), True)
        self.assertEqual(type(self.Model.created_at), datetime)
        self.assertEqual(type(self.Model.updated_at), datetime)

    def test_dict(self):
        """ Test for dict"""
        base_dict = self.Model.to_dict()
        self.assertEqual(type(self.Model.__dict__), dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(self.Model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    def test_creation_dic(self):
        """Test for correct creation dictionary"""
        date = datetime.now()
        dic = {"id": "7734cf23-6c89-4662-8483-284727324c77", "created_at":
               "2022-03-4T16:32:39.023915", "updated_at":
               "2022-03-4T16:32:39.023940", "__class__": "BaseModel"}
        my_base = BaseModel(**dic)
        self.assertEqual(my_base.__class__.__name__, "BaseModel")
        self.assertEqual(my_base.id, "7734cf23-6c89-4662-8483-284727324c77")
        self.assertEqual(type(my_base.created_at), type(date))
        self.assertEqual(type(my_base.updated_at), type(date))

    def test_str(self):
        """test for str method"""
        Model = BaseModel()
        model_str = f'[{BaseModel.__name__}] ({Model.id}) {Model.__dict__}'
        self.assertEqual(model_str, str(Model))

    def test_save(self):
        """Test for save method"""
        self.Model.save()
        self.assertNotEqual(self.Model.created_at, self.Model.updated_at)

    if __name__ == '__main__':
        unittest.main()
