#!/usr/bin/python3
"""Module for City Model"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Model for AirBnB"""
    def __init__(self):
        """Initialization ofcity model"""
        super().__init__()
        self.state_id = ""
        self.name = ""
