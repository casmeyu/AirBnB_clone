#!/usr/bin/python3
"""Module for City Model"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Model for AirBnB"""
    def __init__(self, *args, **kwargs):
        """Initialization ofcity model"""
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
