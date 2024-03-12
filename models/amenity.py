#!/usr/bin/python3
'''
Amenity class inherit from Base class
'''

from base_model import BaseModel


class Amenity(BaseModel):
    '''
    A simple class that represent amenity.

    Attributes:
        name (str): name of the amenity.
    '''
    name = ""
