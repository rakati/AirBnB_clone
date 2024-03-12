#!/usr/bin/python3
'''
Place class inherit from Base class
'''

from .base_model import BaseModel


class Place(BaseModel):
    '''
    A simple class that represent A Place.

    Attributes:
        city_id (str): City.id of the place
        user_id (str): empty string: it will be the User.id
        name (str): name of the city.
        description (str): description of the place
        number_rooms (int): number of rooms in the place
        number_bathrooms (int): default 0 - number of bathrooms in the place
        max_guest (int): default 0 - max of guests the place can support
        price_by_night (int): default 0 - price per night
        latitude (float): default 0.0 - place latitude coordinates
        longitude (float): default 0.0 - place longitude coordinates
        amenity_ids (list of str): default empty - list of Amenity.id
    '''

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
