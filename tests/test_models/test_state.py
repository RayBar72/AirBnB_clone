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
    def test_validate(self):
        """ validate arguments save"""
        st = State()
        st.name = "Montevideo"
        self.assertTrue(hasattr(st, "name"))
        self.assertIsInstance(st.name, str)
    
    def test_ids(self):
        """ test for two ids"""
        self._state1 = State()
        self._state2 = State()
        self.assertNotEqual(self._state1.id, self._state2.id)

    if __name__ == '__main__':
        unittest.main()
