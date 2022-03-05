#!/usr/bin/python3
"""Module of tests for place"""
import json
import unittest
from datetime import datetime
from models.place import Place


class TestsState(unittest.TestCase):
    """Class for tests Place"""
    
    def test_creation(self):
        """Tests for place creation"""
        new_p = Place()
        self.assertEqual(type(new_p), Place)

        self.assertEqual(type(new_p.id), str)
        self.assertEqual(type(new_p.created_at), datetime)
        self.assertEqual(type(new_p.updated_at), datetime)
        self.assertEqual(type(new_p.__str__()), str)
        self.assertNotEqual(len(new_p.__str__()), 0)
        self.assertEqual(type(new_p.city_id), str)
        self.assertEqual(type(new_p.user_id), str)
        self.assertEqual(type(new_p.amenity_ids), list)
        self.assertEqual(type(new_p.name), str)
        self.assertEqual(type(new_p.description), str)
        self.assertEqual(type(new_p.number_rooms), int)
        self.assertEqual(type(new_p.number_bathrooms), int)
        self.assertEqual(type(new_p.max_guest), int)
        self.assertEqual(type(new_p.price_by_night), int)
        self.assertEqual(type(new_p.latitude), float)
        self.assertEqual(type(new_p.longitude), float)
            
        self.assertEqual(str(new_p), f'[Place] ({new_p.id}) \
{new_p.__dict__}')            

    def test_methods(self):
        """Tests for user methods"""
        new_p = Place()
        self.assertEqual(type(new_p.to_dict()), dict)

