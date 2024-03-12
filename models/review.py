#!/usr/bin/python3
'''
Review class inherit from Base class
'''

from base_model import BaseModel


class Review(BaseModel):
    '''
    A simple class that represent A review.

    Attributes:
        place_id (str): string with the id of the place
        user_id (str): id of the reviewer user
        text (str): review text
    '''
    place_id = ""
    user_id = ""
    text = ""
