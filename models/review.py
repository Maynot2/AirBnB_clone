#!/usr/bin/python3
"""
    Contains the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Instantiates a new Review with the given:
        # Public class attributes:
            place_id: string
            user_id: string
            text: string

    """

    place_id = ''
    user_id = ''
    text = ''
