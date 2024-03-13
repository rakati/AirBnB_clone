#!/usr/bin/python3
'''
This Module is for testing the User class

classes:
--------
    - TestUser class
'''

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''A test Class for testing the User class from Models package'''

    def test_first_name(self):
        """Test public attribute firstname of the user class."""
        usr = User()
        self.assertEqual(usr.first_name, '')

    def test_last_name(self):
        """Test public attribute last_name of the user class."""
        usr = User()
        self.assertEqual(usr.last_name, '')

    def test_email(self):
        """Test public attribute email of the user class."""
        usr = User()
        self.assertEqual(usr.email, '')

    def test_password(self):
        """Test public attribute password of the user class."""
        usr = User()
        self.assertEqual(usr.password, '')


if __name__ == "__main__":
    unittest.main()
