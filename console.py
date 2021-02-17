#!/usr/bin/python3
"""
    Custom command line interface for ARBNB clone
"""
import cmd
import json
import re
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

BaseModel = models.base_model.BaseModel


class HBNBCommand(cmd.Cmd):
    """
        Custom command line interface for ARBNB clone
    """

    prompt = '(hbnb) '
    __models = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
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
        """Instanciate a new object of a given class
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
        """Shows a given instance
        """
        args = args.split()
        if HBNBCommand.has_class(len(args)) and HBNBCommand.has_id(len(args)):
            cls, ID = args
        else:
            return False
        key = '{}.{}'.format(cls, ID)
        if HBNBCommand.is_valid_class(cls) and HBNBCommand.is_valid_idkey(key):
            print(models.storage.all()[key])

    def do_count(self, args=''):
        """Counts instances of a given class
        """
        args = args.split()
        count = 0
        if HBNBCommand.has_class(len(args)):
            cls = args[0]
        if HBNBCommand.is_valid_class(cls):
                json_obj = models.storage.all()
                for key in json_obj:
                    if key.startswith('{}.'.format(cls)):
                        count += 1
        print(count)

    def do_destroy(self, args):
        """Destroys a given instance
        """
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

    def do_all(self, args):
        """Shows all instances of a given class or all instances of all
            classes if no argument given
        """
        args = args.split()
        json_obj = models.storage.all()
        if not args:
            for key in json_obj:
                print(json_obj[key])
        if args and HBNBCommand.is_valid_class(args[0]):
            for key in json_obj:
                if key.startswith('{}.'.format(args[0])):
                    print(json_obj[key])

    def do_update(self, args):
        """Updates a given instance
            Usage:
            update <class name> <id> <attribute name> "<attribute value>"
        """
        if args.startswith('‡'):
            args = args.split('‡')
            args = args[1:]
        else:
            args = args.split()
        size = len(args)
        if size == 0:
            print('** class name missing **')
            return False
        if size >= 1:
            cls = args[0]
            if cls not in HBNBCommand.__models:
                print("** class doesn't exist **")
                return False
            if size == 1:
                print('** instance id missing **')
                return False
        if size >= 2:
            ID = args[1]
            key = '{}.{}'.format(cls, ID)
            if key not in models.storage.all():
                print('** no instance found **')
                return False
            if size == 2:
                print('** attribute name missing **')
                return False
        if size == 3:
            d = args[2]
            if d[0] == '{' and d[-1] == '}':
                obj = models.storage.all()[key]
                BaseModel.update(obj, eval(d))
            else:
                print('** value missing **')
                return False
        if size >= 4:
            attr = args[2]
            val = args[3]
            if val[0] == '"' and val[-1] == '"':
                val = val[1:-1]
            obj = models.storage.all()[key]
            BaseModel.update(obj, {attr: val})
            BaseModel.save(obj)

    def do_quit(self, args):
        """Exits the HRBNB cmd line interpreter
        """
        return True

    def do_EOF(self, args):
        """Exits on CTRL-D
        """
        return self.do_quit(args)

    def default(self, line):
        """overides default behaviour when command not found
        """
        methods = {
            'all': self.do_all,
            'count': self.do_count,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update
        }
        args = line.split('.')
        if len(args) == 2:
            cls, method = args
            meth_name = method[0:method.find('(')]
            meth_args = method[method.find('(') + 1:method.find(')')]
            if meth_args[-1] == '}':
                ID = re.findall(r'\w+-\w+-\w+-\w+-\w+', meth_args)[0]
                d = '{' + re.findall(r'\{(.*?)\}', meth_args)[0] + '}'
                if cls in HBNBCommand.__models and meth_name in methods:
                        do_ = methods[meth_name]
                        do_('‡{}‡{}‡{}'.format(cls, ID, d))
                        return
            else:
                meth_args = meth_args.replace(',', ' ')
                meth_args = meth_args.replace('"', '')
                if cls in HBNBCommand.__models and meth_name in methods:
                        do_ = methods[meth_name]
                        do_('{} {}'.format(cls, meth_args))
                        return
        print('*** Unknown syntax: {}'.format(line))

    def emptyline(self):
        """
            Overides normal behaviour. Doesn't repeat last command when empty
            line is entered
        """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
