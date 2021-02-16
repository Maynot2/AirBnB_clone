#!/usr/bin/python3
"""
    Contains the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        Instantiates a new User with the given:
        # Public class attributes:
            email: string
            password: string
            first_name: string
            last_name: string
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
