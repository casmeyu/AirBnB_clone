#!/usr/bin/python3
"""Module for testing the Base Model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class BaseModelTest(unittest.TestCase):
    """Class for testing the Base Model"""
    def test_creation(self):
        """Test the creation and type of attributes of BaseModel"""
        new_bm = BaseModel()
        self.assertEqual(type(new_bm), BaseModel)
        self.assertEqual(type(new_bm.id), str)
        self.assertEqual(type(new_bm.created_at), datetime)
        self.assertEqual(type(new_bm.updated_at), datetime)

        new_bm = BaseModel(**{'name': "Cami"})
        self.assertEqual(new_bm.name, "Cami")

    def test_documentation(self):
        """Test the documentation for BaseModel"""
        new_bm = BaseModel()
        self.assertNotEqual(len(new_bm.__doc__), 0)
        self.assertNotEqual(len(new_bm.save.__doc__), 0)
        self.assertNotEqual(len(new_bm.to_dict.__doc__), 0)

    def test_methods(self):
        """Test the methods of BaseModel"""
        new_bm = BaseModel()
        self.assertEqual(type(new_bm.to_dict()), dict)
        self.assertEqual(type(new_bm.__str__()), str)

        last_update = new_bm.updated_at
        new_bm.save()
        key = f'BaseModel.{new_bm.id}'
        self.assertEqual(new_bm, storage.all()[key])
        self.assertNotEqual(new_bm.updated_at, last_update)

