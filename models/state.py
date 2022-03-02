#!/usr/bin/python3
"""Module class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """State model for AirBnB app"""
    def __init__(self):
        """Initialization of state model"""
        super().__init__()
        self.name = ""
