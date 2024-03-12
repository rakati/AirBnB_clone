#!/usr/bin/python3
'''
State class inherit from Base class
'''

from .base_model import BaseModel


class State(BaseModel):
    '''
    A simple class that represent state.

    Attributes:
        name (str): name of the state.
    '''
    name = ""
