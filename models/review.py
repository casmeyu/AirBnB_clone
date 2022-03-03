#!/usr/bin/python3
"""Module class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review model for the AirBnB app"""
    def __init__(self, *args, **kwargs):
        """Initialization of review model"""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
