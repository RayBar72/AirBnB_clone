#!/usr/bin/python3
"""Test for state file"""

from models.place import Place
import unittest


class Test_Place(unittest.TestCase):
    """Test for state class"""

    def test_doc(self):
        """test for documentation"""
        self.assertTrue(len(Place.__doc__) > 0)

    def setUp(self):
        """ Test for Setsup """
        self.place1 = Place()
        self.place2 = Place()
        self.place3 = Place()

    def tearDown(self):
        """ Test for Delete"""
        del self.place1
        del self.place2
        del self.place3

    def test_str(self):
        """ Test for validate str format"""
        string = "[{}] ({}) {}".format(self.place1.__class__.__name__,
                                       self.place1.id,
                                       self.place1.__dict__)
        self.assertEqual(str(self.place1), string)

    def test_equal(self):
        """ Test for validate two id"""
        user2 = Place()
        self.assertNotEqual(self.place1.id, user2.id)

    def test_validsave(self):
        """ Test to validate argumets save """
        self.place1.name = "Holberton"
        self.assertTrue(hasattr(self.place1, "name"))
        self.assertIsInstance(self.place1.name, str)

    if __name__ == '__main__':
        unittest.main()
