#!/usr/bin/python3
"""Unittest for the BaseModel class."""

import unittest
import datetime
import json
import os
from uuid import UUID
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test case for the BaseModel class."""
    def __init__(self, *args, **kwargs):
        """Constructor for the TestBaseModel class."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up methode for test cases."""
        pass

    def tearDown(self):
        """Tear down method to clean up after each test."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """ Test creation of a BaseModel instance with missing attribute"""
        instance = self.value()
        self.assertEqual(type(instance), self.value)

    def test_kwargs(self):
        """Test creation of a BaseModel instance with attributes."""
        instance = self.value()
        copy = instance.to_dict()
        new_instance = BaseModel(**copy)
        self.assertFalse(new_instance is instance)

    def test_kwargs_int(self):
        """Test the creation of BaseModel instance with invalid int attrs."""
        instance = self.value()
        copy = instance.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new_instance = BaseModel(**copy)

    def test_save(self):
        """Test the save method of the BaseModel class """
        instance = self.value()
        instance.save()
        k = f"{self.name}.{instance.id}"
        with open('file.json', 'r') as f:
            json_data = json.load(f)
            self.assertEqual(json_data[k], instance.to_dict())

    def test_str(self):
        """Test the __str__ method of the BaseModel class"""
        instance = self.value()
        self.assertEqual(str(instance), '[{}] ({}) {}'.format(
            self.name, instance.id, instance.__dict__))

    def test_kwargs_none(self):
        """Tests creation of BaseModel instance with invalid none attrs"""
        invalid_dict = {None: None}
        with self.assertRaises(TypeError):
            new_instance = self.value(**invalid_dict)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class"""
        instance = self.value()
        to_dict_result = instance.to_dict()
        self.assertEqual(instance.to_dict(), to_dict_result)

    def test_id(self):
        """Tests type of the id attribute of the BaseModel class."""
        new_instance = self.value()
        self.assertEqual(type(new_instance.id), str)

    def test_created_at(self):
        """Test the type of the created_at atrribute of  the BaseModel."""
        new_instance = self.value()
        self.assertEqual(type(new_instance.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test that created_at and updated_at attributes are different."""
        new_instance = self.value()
        self.assertEqual(type(new_instance.updated_at), datetime.datetime)
        instance_dict = new_instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertFalse(new_instance.created_at == new_instance.updated_at)


if __name__ == '__main__':
    unittest.main()
