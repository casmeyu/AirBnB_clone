#!/usr/bin/python3
"""Module for class File storage"""
import json
from models.base_model import BaseModel


class FileStorage():
    """class filestorage"""
    __file_path = "data_base.json"
    __objects = {}

    def all(self):
        """public method all"""
        return self.__objects

    def new(self, obj):
        """public method new"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """public method save"""
        with open(self.__file_path, "a+") as fi:
            for key, value in self.__objects.items():
                var = json.dumps({key: value.to_dict()})
                fi.write(f'{var},\n')

    def reload(self):
        """public method reload""" 
        try:
            with open(self.__file_path, 'a') as fi:
                x = json.loads(fi.read())
                for key, value in x.items():
                    value = BaseMode(value)
                    self.__objects[key] = value
        except Exception as ex:
                    pass
