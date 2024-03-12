#!/usr/bin/python3
'''
Base class for all models in the application.
'''

import uuid
import models
from datetime import datetime


class BaseModel:
    '''
    Base class for all models in the application.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Date and time when the instance was created.
        updated_at (datetime): Date and time when the instance
                               was last updated.
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        '''
        Saves the current instance to the storage.
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        '''
        Returns a string representation of the BaseModel instance.
        '''
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        '''
        Converts the instance to a dictionary representation.

        Returns:
            dict: Dictionary containing the instance
            attributes and their values.
        '''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
