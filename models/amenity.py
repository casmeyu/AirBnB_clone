#!/usr/bin/python3
"""Module for class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity model for the AirBnB app"""
    name = ""
    def __init__(self, *args, **kwargs):
        """Initialization of the amenity model"""
        super().__init__(*args, **kwargs)
