#!/usr/bin/python3
"""Module of tests for amenity"""
import json
import unittest
from datetime import datetime
from models.review import Review


class TestsState(unittest.TestCase):
    """Class for tests Review"""
    
    def test_creation(self):
        """Tests for review creation"""
        new_r = Review()
        self.assertEqual(type(new_r), Review)

        self.assertEqual(type(new_r.id), str)
        self.assertEqual(type(new_r.created_at), datetime)
        self.assertEqual(type(new_r.updated_at), datetime)
        self.assertEqual(type(new_r.__str__()), str)
        self.assertNotEqual(len(new_r.__str__()), 0)
        self.assertEqual(type(new_r.place_id), str)
        self.assertEqual(type(new_r.user_id), str)
        self.assertEqual(type(new_r.text), str)
        self.assertEqual(str(new_r), f'[Review] ({new_r.id}) \
{new_r.__dict__}')            

    def test_methods(self):
        """Tests for user methods"""
        new_r = Review()
        self.assertEqual(type(new_r.to_dict()), dict)

