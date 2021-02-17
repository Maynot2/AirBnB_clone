#!/usr/bin/python3
"""
    Contains the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        Instantiates a new City  with the given:
        # Public class attributes:
            name: string
    """

    state_id = ''
    name = ''
