#!/usr/bin/python3
"""Module for Use Model"""
from models.base_model import BaseModel

class User(BaseModel):
    """User model for the AirBnB application"""
    def __init__(self, *args, **kwargs):
        """Initialization for the user model"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
