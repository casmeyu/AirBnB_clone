#!/usr/bin/python3
"""Module of tests for amenity"""
import json
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestsState(unittest.TestCase):
    """Class for tests Amenity"""
    
    def test_creation(self):
        """Tests for state creation"""
        new_a = Amenity()
        self.assertEqual(type(new_a), Amenity)

        self.assertEqual(type(new_a.id), str)
        self.assertEqual(type(new_a.created_at), datetime)
        self.assertEqual(type(new_a.updated_at), datetime)
        self.assertEqual(type(new_a.__str__()), str)
        self.assertNotEqual(len(new_a.__str__()), 0)
        self.assertEqual(type(new_a.name), str)
        self.assertEqual(str(new_a), f'[Amenity] ({new_a.id}) \
{new_a.__dict__}')            

    def test_methods(self):
        """Tests for user methods"""
        new_a = Amenity()
        self.assertEqual(type(new_a.to_dict()), dict)

