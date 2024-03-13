#!/usr/bin/python3
'''
This Module is for testing the Place class

classes:
--------
    - TestPlace class
'''

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''A test Class for testing the Place class from Models package'''

    def test_city_id(self):
        """Test public attribute city_id of the Place class."""
        plc = Place()
        self.assertIsInstance(plc.city_id, str)
        self.assertEqual(plc.city_id, '')

    def test_user_id(self):
        """Test public attribute user_id of the Place class."""
        plc = Place()
        self.assertIsInstance(plc.user_id, str)
        self.assertEqual(plc.user_id, '')

    def test_name(self):
        """Test public attribute name of the Place class."""
        plc = Place()
        self.assertIsInstance(plc.name, str)
        self.assertEqual(plc.name, '')

    def test_description(self):
        """Test public attribute description of the Place class."""
        plc = Place()
        self.assertIsInstance(plc.description, str)
        self.assertEqual(plc.description, '')

    def test_number_rooms(self):
        """Test public attribute number_rooms of the Place class."""
        plc = Place()
        self.assertIsInstance(plc.number_rooms, int)
        self.assertEqual(plc.number_rooms, 0)

    def test_number_bathrooms(self):
        """Test public attribute number_bathrooms of the Place class."""
        plc = Place()
        self.assertIsInstance(plc.number_bathrooms, int)
        self.assertEqual(plc.number_bathrooms, 0)

    def test_max_guest(self):
        """Test public attribute max_guest of the Place class."""
        plc = Place()
        self.assertIsInstance(plc.max_guest, int)
        self.assertEqual(plc.max_guest, 0)

    def test_price_by_night(self):
        """Test public attribute price_by_night of the Place class."""
        plc = Place()
        self.assertIsInstance(plc.price_by_night, int)
        self.assertEqual(plc.price_by_night, 0)

    def test_latitude(self):
        """Test public attribute latitude of the Place class."""
        plc = Place()
        self.assertIsInstance(plc.latitude, float)
        self.assertEqual(plc.latitude, 0.0)

    def test_longitude(self):
        """Test public attribute longitude of the Place class."""
        plc = Place()
        self.assertIsInstance(plc.longitude, float)
        self.assertEqual(plc.longitude, 0.0)

    def test_amenity_ids(self):
        """Test public attribute amenity_ids of the Place class."""
        plc = Place()
        self.assertIsInstance(plc.amenity_ids, list)
        self.assertEqual(plc.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
