#!/user/bin/python3
"""test for review file"""

from models.review import Review
import unittest


class Test_review(unittest.TestCase):
    """test for correct funcioning of review"""
    def test_doc(self):
        """test for documentation"""
        self.assertTrue(len(Review.__doc__) > 0)
