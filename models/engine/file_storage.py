#!/usr/bin/python3
"""Module for class File storage"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """class filestorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """public method all"""
        return self.__objects

    def new(self, obj):
        """public method new"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """public method save"""
        aux_dict = {}
        with open(self.__file_path, "w+") as fi:
            for key, value in self.__objects.items():
                aux_dict[key] = value.to_dict()

            fi.write(json.dumps(aux_dict))

    def reload(self):
        """public method reload"""
        try:
            with open(self.__file_path, 'r') as fi:
                x = json.load(fi)
                for key, value in x.items():
                    cls = value['__class__']
                    self.__objects[key] = eval(f'{cls}(**{value})')
        except Exception as ex:
            pass
