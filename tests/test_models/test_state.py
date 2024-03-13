#!/usr/bin/python3
'''
This Module is for testing the State class

classes:
--------
    - TestState class
'''

import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''A test Class for testing the State class from Models package'''

    def test_name(self):
        """Test public attribute name of the state class."""
        st = State()
        self.assertEqual(st.name, '')


if __name__ == "__main__":
    unittest.main()
