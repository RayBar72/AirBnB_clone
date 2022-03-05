#!/usr/bin/python3
"""
All test for file storage
"""

import os
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
import json
import uuid
from models.state import State
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review


class Test_FileStorage(unittest.TestCase):
    """Test for FileStorage """
    Fs = FileStorage()

    def test_doc_FileStorage(self):
        """test doc for class"""
        self.assertTrue(self.Fs.all.__doc__)
        self.assertIsNotNone(self.Fs.all.__doc__)
        self.assertTrue(self.Fs.new.__doc__)
        self.assertIsNotNone(self.Fs.new.__doc__)
        self.assertTrue(self.Fs.save.__doc__)
        self.assertIsNotNone(self.Fs.save.__doc__)
        self.assertTrue(self.Fs.reload.__doc__)
        self.assertIsNotNone(self.Fs.reload.__doc__)

    def test_FS_all(self):
        """ Test for all method """
        obj = self.Fs.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)

    def test_FS_new(self):
        """ Test for new method"""
        obj = self.Fs.all()
        user = User()
        user.id = "0303456"
        user.name = "Betty"
        self.Fs.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])


    def test_save(self):
        """ Test for save method """
        self.Fs.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_empty(self):
        """test if json is empty or not"""
        new = BaseModel()
        conten = new.to_dict()
        new.save()
        new2 = BaseModel(**conten)
        self.assertNotEqual(os.path.getsize("file.json"), 0)

    def test_reload(self):
        """ Test for reload method """
        self.Fs.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "objects.json")
        with open("file.json", 'r') as f:
            lines = f.readlines()
        try:
            os.remove("file.json")
        except Exception:
            pass
        self.Fs.save()
        with open("file.json", 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove("file.json")
        except Exception:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.Fs.reload(), None) 

    def test_obj(self):
        """ Test for obj """
        self.assertEqual(dict, type(self.Fs._FileStorage__objects))
        with self.assertRaises(AttributeError):
            self.Fs.__objects

    def test_path(self):
        """ Test for path """
        self.assertEqual(str, type(self.Fs._FileStorage__file_path))
        with self.assertRaises(AttributeError):
            self.Fs.__file_path

    if __name__ == '__main__':
        unittest.main()
