#!/usr/bin/python3
""" Module for Base Model """
from uuid import uuid4
from datetime import datetime


class BaseModel():
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_new = {"__class__": self.__class__.__name__}
        for key in self.__dict__:
            if key == "created_at" or key == "updated_at":
                dict_new[key] = self.__dict__[key].isoformat()
            else:
                dict_new[key] = self.__dict__[key]
        return dict_new
