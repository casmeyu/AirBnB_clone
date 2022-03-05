#!/usr/bin/python3
"""Module of tests for city"""
import json
import unittest
from datetime import datetime
from models.city import City


class TestsCity(unittest.TestCase):
    """Class for tests City"""
    
    def test_creation(self):
        """Tests for city creation"""
        new_c = City()
        self.assertEqual(type(new_c), City)

        self.assertEqual(type(new_c.id), str)
        self.assertEqual(type(new_c.created_at), datetime)
        self.assertEqual(type(new_c.updated_at), datetime)
        self.assertEqual(type(new_c.__str__()), str)
        self.assertNotEqual(len(new_c.__str__()), 0)
        self.assertEqual(type(new_c.name), str)
        self.assertEqual(type(new_c.state_id), str)
        self.assertEqual(str(new_c), f'[City] ({new_c.id}) \
{new_c.__dict__}')            

    def test_methods(self):
        """Tests for user methods"""
        new_c = City()
        self.assertEqual(type(new_c.to_dict()), dict)

