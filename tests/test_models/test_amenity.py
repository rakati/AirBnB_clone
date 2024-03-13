#!/usr/bin/python3
'''
This Module is for testing the Amenity class

classes:
--------
    - TestAmenity class
'''

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''A test Class for testing the Amenity class from Models package'''

    def test_name(self):
        """Test public attribute name of the amenity class."""
        st = Amenity()
        self.assertIsInstance(st.name, str)
        self.assertEqual(st.name, '')


if __name__ == "__main__":
    unittest.main()
