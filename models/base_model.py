#!/usr/bin/python3
"""
    Contains the BaseModel class
"""
import uuid
from datetime import datetime
import models


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

    def __init__(self, *args, **kwargs):
        """
            Initialises a BaseModel instance with id, created_at, updates_at
            attributes
        """
        if self.are_valid_args(kwargs):
            self.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        """
            Returns a custom string representation of a BaseModel instance
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                           self.id,
                                           self.__dict__)
    @staticmethod
    def are_valid_args(args):
        """
            Checks if args is not empty and has at least id, created_at and
            updated_at keys
        """
        if not args or 'id' not in args:
            return False
        if 'created_at' not in args or 'updated_at' not in args:
            return False
        return True

    def save(self):
        """
            Updates public attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def update(self, args):
        for k, v in args.items():
            if k == 'created_at' or k == 'updated_at':
                v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
            if k != '__class__':
                setattr(self, k, v)

    def to_dict(self):
        """
            Custom dictionary representation of a BaseModel Instance
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return (dictionary)

if __name__ == "__main__":
    b = BaseModel()
    b.to_dict()
