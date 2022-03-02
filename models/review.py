#!/usr/bin/python3
"""Module class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review model for the AirBnB app"""
    place_id = ""
    user_id = ""
    text = ""
