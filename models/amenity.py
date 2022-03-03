#!/usr/bin/python3
"""Module for class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity model for the AirBnB app"""
    def __init__(self, *args, **kwargs):
        """Initialization of the amenity model"""
        name = ""
        super().__init__(*args, **kwargs)
