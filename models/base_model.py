#!/usr/bin/python3
"""
    Contains the BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
        Defines all common attributes/methods for other classes
        # Public instance attributes:
            id
            created_at
            updated_at
        # Public instance methods:
            save()
            to_dict()
    """

    def __init__(self):
        """
            Initialises a BaseModel instance with id, created_at, updates_at
            attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
            Returns a custom string representation of a BaseModel instance
        """
        return "[<{}>] (<{}>) <{}>".format(type(self).__name__,
                                           self.id,
                                           self.__dict__)

    def save(self):
        """
            Updates public attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Custom dictionary representation of a BaseModel Instance
        """
        dictionary = self.__dict__
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return (dictionary)

if __name__ == "__main__":
    b = BaseModel()
    b.to_dict()
