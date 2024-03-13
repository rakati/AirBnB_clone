#!/usr/bin/python3
'''
This Module is for testing the City class

classes:
--------
    - TestCity class
'''

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    '''A test Class for testing the City class from Models package'''

    def test_state_id(self):
        """Test public attribute state_id of the city class."""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertEqual(city.state_id, '')

    def test_name(self):
        """Test public attribute name of the city class."""
        city = City()
        self.assertIsInstance(city.name, str)
        self.assertEqual(city.name, '')


if __name__ == "__main__":
    unittest.main()
