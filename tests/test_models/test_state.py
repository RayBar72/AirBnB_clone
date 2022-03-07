#!/usr/bin/python3
"""
Test for state class
"""

from models.state import State
import unittest
from models.base_model import BaseModel


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

    def test_none(self):
        """test for state none"""
        self.state = State()
        self.state.name = None
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(None, self.state.name)

    if __name__ == '__main__':
        unittest.main()
