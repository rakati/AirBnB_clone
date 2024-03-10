#!/usr/bin/python3

'''
File Storage Class
'''


import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    '''
    This class manages the serialization and deserialization
    of objects to a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary containing objects
        stored with their keys.
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns the dictionary __objects.
        '''

        return self.__objects

    def new(self, obj):
        '''
        Sets in __objects the obj with key <obj class name>.id.
        '''

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''
        Serializes __objects to the JSON file.
        '''

        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        '''
        Deserializes the JSON file to __objects.
        '''
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    self.__objects[key] = BaseModel(**value)
