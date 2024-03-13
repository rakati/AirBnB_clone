#!/usr/bin/python3
'''
This Module is for testing the Review class

classes:
--------
    - TestReview class
'''

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''A test Class for testing the Review class from Models package'''

    def test_place_id(self):
        """Test public attribute place_id of the review class."""
        rev = Review()
        self.assertIsInstance(rev.place_id, str)
        self.assertEqual(rev.place_id, '')

    def test_user_id(self):
        """Test public attribute user_id of the review class."""
        rev = Review()
        self.assertIsInstance(rev.user_id, str)
        self.assertEqual(rev.user_id, '')

    def test_text(self):
        """Test public attribute text of the review class."""
        rev = Review()
        self.assertIsInstance(rev.text, str)
        self.assertEqual(rev.text, '')


if __name__ == "__main__":
    unittest.main()
