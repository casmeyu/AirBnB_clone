#!/usr/bin/python3
"""Module for testing the Base Model"""
import json
import os
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
        self.assertEqual(str(new_bm), f'[BaseModel] ({new_bm.id}) \
{new_bm.__dict__}')
        self.assertEqual(type(new_bm.created_at), datetime)
        self.assertEqual(type(new_bm.updated_at), datetime)

        u_date = new_bm.updated_at.isoformat()
        c_date = new_bm.created_at.isoformat()
        self.assertEqual(new_bm.to_dict()['updated_at'], u_date)
        self.assertEqual(new_bm.to_dict()['created_at'], c_date)

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
        self.assertNotEqual(len(new_bm.__str__()), 0)

        last_update = new_bm.updated_at
        new_bm.save()
        self.assertTrue(os.path.isfile('file.json'))
        key = f'BaseModel.{new_bm.id}'
        self.assertEqual(new_bm, storage.all()[key])
        self.assertNotEqual(new_bm.updated_at, last_update)
        self.assertNotEqual(new_bm.created_at, new_bm.updated_at)

    def test_save_reload(self):
        """Test save and reload from json file"""
        new_bm = BaseModel()
        new_bm.save()
        try:
            with open('file.json', 'r') as fd:
                objs = json.loads(fd)
                self.assertEqual(new_bm, objs[f'BaseModel.{new_bm.id}'])
        except Exception as ex:
            pass


if __name__ == '__main__':
    unittest.main()
