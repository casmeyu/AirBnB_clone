#!/usr/bin/python3
"""Module class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """State model for AirBnB app"""
    def __init__(self, *args, **kwargs):
        """Initialization of state model"""
        self.name = ""
        super().__init__(*args, **kwargs)
