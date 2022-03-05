#!/usr/bin/python3
"""Module for testing the Base Model"""
import unittest
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """Class for testing the Base Model"""
    def test_creation(self):
        """Test the creation and type of attributes of BaseModel"""
        new_bm = BaseModel()
        self.assertEqual(type(new_bm), BaseModel)
        self.assertEqual(type(new_bm.id), str)
        self.assertEqual(type(new_bm.to_dict()), dict)

    def test_documentation(self):
        """Test the documentation for BaseModel"""
        new_bm = BaseModel()
        self.assertNotEqual(len(new_bm.__doc__), 0)

