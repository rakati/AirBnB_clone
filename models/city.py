#!/usr/bin/python3
'''
City class inherit from Base class
'''

from .base_model import BaseModel


class City(BaseModel):
    '''
    A simple class that represent A city.

    Attributes:
        state_id (str): string with the id of city state
        name (str): name of the city.
    '''
    name = ""
    state_id = ""
