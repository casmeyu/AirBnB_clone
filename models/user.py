#!/usr/bin/python3
"""Module for Use Model"""
from models.base_model import BaseModel

class User(BaseModel):
    """User model for the AirBnB application"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
