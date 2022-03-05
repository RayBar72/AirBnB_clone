#!/usr/bin/python3
"""
All test for file storage
"""
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


class Test_FS(unittest.TestCase):
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
        self.Fs.all()
        with self.assertRaises(TypeError):
            self.Fs.all("PYTHON")

    def test_FS_new(self):
        """ Test for new method"""
        with self.assertRaises(TypeError):
            self.Fs.new()

    def test_doc_FileStorage_new(self):
        """ Test for new method """
        self.assertIsNotNone(self.Fs.new.__doc__)

    def test_save(self):
        """ Test for save method """
        self.assertIsNotNone(self.Fs.save.__doc__)

    def test_reload(self):
        """ Test for reload method """
        self.assertIsNotNone(self.Fs.reload.__doc__)

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
