#!/usr/bin/python3
"""
    Contains a FileStorage class to serialize and deserialize objects
"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
        Serialize and deserialize objects
        # Private class attributes:
            __file_path
            __objects
            __models
        # Public instance methods:
            all()
            new()
            save()
            reload()
    """

    __file_path = "file.json"
    __objects = {}
    __models = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self):
        """
            Returns a dictionary containing all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            Sets in __objects the obj with key <obj class name>.id
        """
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
            Serializes __objects to the JSON file
        """
        json_obj = {}
        for key, obj in FileStorage.__objects.items():
            json_obj[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_obj, f, indent=6)

    def reload(self):
        """
            Deserializes the JSON file to __objects
        """
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                json_obj = json.load(f)
            for key in json_obj:
                cls = FileStorage.__models[key.split('.')[0]]
                obj = cls(**json_obj[key])
                self.new(obj)
