#!/usr/bin/python3
"""
    Contains the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Instantiates a new Place with the given:
        # Public class attributes:
            city_id: string
            user_id: string
            name: string
            description: string
            number_rooms: integer
            number_bathrooms: integer
            max_guest: integer
            price_by_night: integer
            latitude: float
            longitude: float
            amenity_ids: list of string
    """

    city_id = ''
    user_id = ''
    name = string = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest: integer = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
