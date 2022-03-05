#!/usr/bin/python3
"""Module of tests for state"""
import json
import unittest
from datetime import datetime
from models.state import State


class TestsState(unittest.TestCase):
    """Class for tests State"""
    
    def test_creation(self):
        """Tests for state creation"""
        new_s = State()
        self.assertEqual(type(new_s), State)

        self.assertEqual(type(new_s.id), str)
        self.assertEqual(type(new_s.created_at), datetime)
        self.assertEqual(type(new_s.updated_at), datetime)
        self.assertEqual(type(new_s.__str__()), str)
        self.assertNotEqual(len(new_s.__str__()), 0)
        self.assertEqual(type(new_s.name), str)
        self.assertEqual(str(new_s), f'[State] ({new_s.id}) \
{new_s.__dict__}')            

    def test_methods(self):
        """Tests for user methods"""
        new_s = State()
        self.assertEqual(type(new_s.to_dict()), dict)

