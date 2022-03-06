#!/usr/bin/python3
"""
Test for city class


import unittest
from models.city import City


class Test_city(unittest.TestCase):
    Test for the correcty funcionning of city
    
    def test_argtms(self):
        #"""Test arguments of the class"""
        self._city = City()
        self.assertTrue(hasattr(self._city, "state_id"))
        self.assertTrue(hasattr(self._city, "name"))
        self.assertIsInstance(self._city.name, str)
        self.assertIsInstance(self._city.state_id, str)

    def test_ids(self):
        """test for two ids"""
        id1 = City()
        id2 = City()
        self.assertNotEqual(id1.id, id2.id)

    if __name__ == '__main__':
        unittest.main()
"""
