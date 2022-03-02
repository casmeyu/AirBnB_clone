#!/usr/bin/python3
"""Module class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review model for the AirBnB app"""
    def __init__(self):
        """Initialization of review model"""
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
