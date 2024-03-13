#!/usr/bin/python3
'''Unittests for FileStorage Class'''

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class."""

    def setUp(self):
        """Setup method to create a FileStorage instance."""
        self.storage = FileStorage()

    def tearDown(self):
        """Teardown method to reset FileStorage after each test."""
        self.storage._FileStorage__objects = {}

    def test_classes(self):
        """Test the classes method."""
        classes = self.storage.classes()
        self.assertEqual(classes, [
            "BaseModel", "User", "Place", "State", "City", "Amenity", "Review"
        ])

    def test_all(self):
        """Test the all method."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """Test the new method."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[key], obj)

    def test_save_reload(self):
        """Test the save and reload methods."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, new_storage._FileStorage__objects)
        self.assertEqual(new_storage._FileStorage__objects[key].to_dict(
                    ), obj.to_dict())


if __name__ == "__main__":
    unittest.main()
