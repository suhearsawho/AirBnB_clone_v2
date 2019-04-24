#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary, and if cls is given, return all objects of that
        class type in a list.
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            return self.__objects
        else:
            if type(cls) is str:
                types = {'BaseModel': BaseModel, 'User': User, 'State': State,
                         'City': City, 'Amenity': Amenity, 'Place': Place,
                         'Review': Review}
                cls = types[cls]
            new_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    new_dict[k] = v
            # instance_list = [instance for instance in new_dict.values()]
            return new_dict

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes an object from the __objects dictionary if present"""
        if obj:
            try:
                key = obj.__class__.__name__ + "." + str(obj.id)
                del self.__objects[key]
                self.save()
            except:
                pass

    def close(self):
        """Calls reload method"""
        self.reload()
