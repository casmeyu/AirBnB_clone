#!/usr/bin/python3
""" Module for Base Model """
import models
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """ Base Class for all the objects in the system"""
    def __init__(self, *args, **kwargs):
        """ initialize the base class with a random id and creation dates """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        formato = '%Y-%m-%dT%H:%M:%S.%f'
                        setattr(self, key, datetime.strptime(value, formato))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """String representiation"""
        return (f'[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>')

    def save(self):
        """ Saves a JSON representation of the object
            using the file_storage engine
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of the object """
        dict_new = {"__class__": type(self).__name__}
        for key in self.__dict__:
            if key == "created_at" or key == "updated_at":
                dict_new[key] = self.__dict__[key].isoformat()
            else:
                dict_new[key] = self.__dict__[key]
        return dict_new
