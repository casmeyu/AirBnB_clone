#!/usr/bin/python3
"""Module for class File storage"""
import json


class FileStorage():
    """class filestorage"""
    __file_path = "data_base.json"
    __objects = {}

    def all(self):
        """public method all"""
        return __objects

    def new(self, obj):
        """public method new"""
        __objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """public method save"""
        with open(__file_path, "w+") as fi:
            for key, value in __objects.items():
                var = json.dumps({key: value.to_dict()})
                fi.write(f'{var}, ')

    def reload(self):
        """public method reload""" 
        with open(__file_path, 'r') as fi:
            print(json.loads(fi))
