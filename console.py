#!/usr/bin/python3
"""
    Custom command line interface for ARBNB clone
"""
import cmd
import json
import models
BaseModel = models.base_model.BaseModel


class HBNBCommand(cmd.Cmd):
    """
        Custom command line interface for ARBNB clone
    """

    prompt = '(hbnb) '
    __models = {
        'BaseModel': BaseModel
    }

    @staticmethod
    def is_valid_idkey(key=''):
        """Checks if key is valid"""
        if key not in models.storage.all():
            print('** no instance found **')
            return False
        return True

    @staticmethod
    def has_id(size):
        """Checks if id is present"""
        if size >= 2:
            return True
        else:
            print('** instance id missing **')
            return False

    @staticmethod
    def is_valid_class(cls_name):
        """Checks if class name exists"""
        if cls_name not in HBNBCommand.__models:
            print("** class doesn't exist **")
            return False
        return True

    @staticmethod
    def has_class(size):
        """Checks if class is present"""
        if size > 0:
            return True
        else:
            print('** class name missing **')
            return False

    def do_create(self, args=''):
        """
            Instanciate a new object of a given class
            Takes 2 positional arguments:
                self
               cls: The name of the class of the object to be created
        """
        args = args.split()
        if HBNBCommand.has_class(len(args)):
            cls = args[0]
        else:
            return False
        if HBNBCommand.is_valid_class(cls):
            obj = HBNBCommand.__models[cls]()
            obj.save()
            print(obj.id)

    def do_show(self, args=''):
        """Shows a given instance"""
        args = args.split()
        if HBNBCommand.has_class(len(args)) and HBNBCommand.has_id(len(args)):
            cls, ID = args
        else:
            return False
        key = '{}.{}'.format(cls, ID)
        if HBNBCommand.is_valid_class(cls) and HBNBCommand.is_valid_idkey(key):
            print(models.storage.all()[key])

    def do_destroy(self, args):
        """Destroys a given instance"""
        args = args.split()
        if HBNBCommand.has_class(len(args)) and HBNBCommand.has_id(len(args)):
            cls, ID = args
        else:
            return False
        key = '{}.{}'.format(cls, ID)
        if HBNBCommand.is_valid_class(cls) and HBNBCommand.is_valid_idkey(key):
            json_obj = models.storage.all()
            del json_obj[key]
            models.storage.save()

    def do_quit(self, line):
        """Exits the HRBNB cmd line interpreter"""
        return True

    def do_EOF(self, line):
        """Exits the HRBNB cmd line interpreter"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
