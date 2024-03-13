#!/usr/bin/python3
'''
unittests for basemodel
'''

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    '''Unittests for testing instantiation of the BaseModel class'''

    def test_instance_creation(self):
        """Test creating an instance of BaseModel."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id_generation(self):
        """Test generation of unique IDs."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_updated_at(self):
        """Test created_at and updated_at attributes."""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_multiple_instances(self):
        '''Test multiple instances'''
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

    def test_str_representation(self):
        """Test string representation of BaseModel."""
        obj = BaseModel()
        obj_str = str(obj)
        self.assertIn("[BaseModel]", obj_str)
        self.assertIn("'id':", obj_str)
        self.assertIn("'created_at':", obj_str)
        self.assertIn("'updated_at':", obj_str)

    def test_to_dict_method(self):
        """Test to_dict method of BaseModel."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_attributes_assignment(self):
        """Test assignment of attributes."""
        obj = BaseModel()
        obj.my_number = 42
        obj.my_string = "hello"
        obj.my_list = [1, 2, 3]
        self.assertEqual(obj.my_number, 42)
        self.assertEqual(obj.my_string, "hello")
        self.assertEqual(obj.my_list, [1, 2, 3])

    def test_attributes_update(self):
        """Test updating attributes."""
        obj = BaseModel()
        obj.my_number = 42
        obj.my_string = "hello"
        obj.my_list = [1, 2, 3]
        obj.my_number = 100
        obj.my_string = "world"
        obj.my_list = [4, 5, 6]
        self.assertEqual(obj.my_number, 100)
        self.assertEqual(obj.my_string, "world")
        self.assertEqual(obj.my_list, [4, 5, 6])

    def test_from_dict_method(self):
        """Test from_dict method of BaseModel."""

        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(obj.__dict__, new_obj.__dict__)

    def test_attributes(self):
        '''Test the presence of essential attributes in the
            BaseModel instance.'''

        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertEqual(type(obj.id), str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict(self):
        '''Test the to_dict method of the BaseModel class.'''

        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_save(self):
        '''Test the save method of the BaseModel class.'''

        obj = BaseModel()
        obj.save()
        self.assertIsNotNone(obj.updated_at)
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, original_updated_at)

    def test_reload(self):
        '''Test the reload method of the FileStorage class.'''

        storage = FileStorage()
        obj = BaseModel()
        obj.save()
        obj_id = obj.id
        storage.reload()
        reloaded_obj = storage.all()["BaseModel." + obj_id]
        self.assertEqual(reloaded_obj.id, obj_id)

    def test_invalid_attribute_access(self):
        '''Test invalid attribute access'''

        obj = BaseModel()
        with self.assertRaises(AttributeError):
            _ = obj.invalid_attribute


if __name__ == "__main__":
    unittest.main()
