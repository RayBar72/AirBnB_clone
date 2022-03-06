#!/usr/bin/python3
"""
Test for state class
"""

from models.state import State
import unittest


class Test_state(unittest.TestCase):
    """
    Test for the correct functioning of state
    """
    def test_valdate(self):
        """ validate arguments save"""
        st = State()
        st.name = "Montevideo"
        self.assertTrue(hasattr(st, "name"))
        self.assertIsInstance(st.name, str)

    if __name__ == '__main__':
        unittest.main()
