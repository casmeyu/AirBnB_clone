#!/usr/bin/python3
"""Module of tests for user"""
import json
import unittest
from datetime import datetime
from models.user import User


class TestsUser(unittest.TestCase):
    """Class for tests user"""
    
    def test_creation(self):
        """Tests for user creation"""
        new_u = User()
        self.assertEqual(type(new_u), User)

        self.assertEqual(type(new_u.id), str)
        self.assertEqual(type(new_u.created_at), datetime)
        self.assertEqual(type(new_u.updated_at), datetime)
        self.assertEqual(type(new_u.__str__()), str)
        self.assertNotEqual(len(new_u.__str__()), 0)
        self.assertEqual(type(new_u.first_name), str)
        self.assertEqual(type(new_u.last_name), str)
        self.assertEqual(type(new_u.email), str)
        self.assertEqual(type(new_u.password), str)
        self.assertEqual(str(new_u), f'[User] ({new_u.id}) \
{new_u.__dict__}')            

    def test_methods(self):
        """Tests for user methods"""
        new_u = User()
        self.assertEqual(type(new_u.to_dict()), dict)

