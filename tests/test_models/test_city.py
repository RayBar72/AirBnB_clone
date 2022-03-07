#!/usr/bin/python3
"""
Test for city class
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class Test_city(unittest.TestCase):
    """
    Test for the correcty funcionning of city
    """
    def test_argtms(self):
        """Test arguments of the class"""
        self._city = City()
        self.assertTrue(hasattr(self._city, "state_id"))
        self.assertTrue(hasattr(self._city, "name"))
        self.assertIsInstance(self._city.name, str)
        self.assertIsInstance(self._city.state_id, str)
        self.assertTrue(issubclass(type(self._city), BaseModel))

    def test_ids(self):
        """test for two ids"""
        id1 = City()
        id2 = City()
        self.assertNotEqual(id1.id, id2.id)

    def test_str(self):
        """ Test for validate str format"""
        self.city = City()
        string = "[{}] ({}) {}".format(self.city.__class__.__name__,
                                       self.city.id,
                                       self.city.__dict__)
        self.assertEqual(str(self.city), string)

    if __name__ == '__main__':
        unittest.main()
