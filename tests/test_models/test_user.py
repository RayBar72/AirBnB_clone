#!/usr/bin/python3
"""
Test for class user
"""
from datetime import datetime
from models.user import User
import unittest


class TestUser(unittest.TestCase):

    def setUp(self):
        """ Test for Setsup an instance of a User """
        self.user1 = User()
        self.user2 = User()
        self.user3 = User()

    def tearDown(self):
        """ Test for Delete an instance of a User """
        del self.user1
        del self.user2
        del self.user3

    def test_crateinstance(self):
        """ Test for create new instance """
        new = User()
        self.assertEqual(new.password, "")
        self.assertEqual(new.first_name, "")
        self.assertEqual(new.last_name, "")
        self.assertEqual(new.email, "")

    def test_str(self):
        """ Test for validate str format"""
        string = "[{}] ({}) {}".format(self.user1.__class__.__name__,
                                       self.user1.id,
                                       self.user1.__dict__)
        self.assertEqual(str(self.user1), string)

    def test_equal(self):
        """ Test for validate id between both instances """
        user2 = User()
        self.assertNotEqual(self.user1.id, user2.id)

    if __name__ == '__main__':
        unittest.main()
