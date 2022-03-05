#!/usr/bin/python3
"""Module for testing the Base Model"""
import unittest
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """Class for testing the Base Model"""
    def test_creation(self):
        new_bm = BaseModel()
        self.assertEqual(type(new_bm), BaseModel)
        self.assertEqual(type(new_bm.to_dict()), dict)
