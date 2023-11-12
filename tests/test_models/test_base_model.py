#!/usr/bin/python3
"""The unittest for the BaseModel class"""

import unittest
from datetime import datetime
import json
import os
import re
import time
import uuid
from models import storage
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ The test cases for the BaseModel class."""

    # Setup and Teardown Methods
    def setUp(self):
        """Set up test method."""
        pass

    def tearDown(self):
        """ Tear down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    # Instantiatiotion Tests
    def  test_instantiation(self):
        """Test instatiation of BaseModel class."""
        b = BaseModel()
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_init_no_args(self):
        """Test __init__ with no arguments."""
        self.restStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
            msg = "__init__() missing 1 required positional argument: 'self'"
            self.assertEqual(str(e.exception), msg)

    def test_init_many_args(self):
        """Test __init__ with many arguments."""
        self.resetStorage()
        args = [j for j in range(1000)]
        obj = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        obj = BaseModel(*args)

    # Attributes Tests
    def test_attributes(self):
        """Tests attributes value for instance of a Basemodel class."""
        attributes_dict = storage.attributes()["BaseModel"]
        obj = BaseModel()
        for attr, exp_type in attributes.items():
            self.assertTrue(hasattr(obj, attr))
            self.assertEqual(type(getattr(obj, attr, None)), exp_type)

    # Datetime Tests
    def test_datetime_created(self):
        """Test if updated_at & created_at are current at creation."""
        date_now = datetime.now()
        obj = BaseModel()
        diff = obj.updated_at - obj.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = obj.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    # ID Tests
    def test_id(self):
        """Tests user IDs."""
        id_list = [BaseModel().id for j in range(1000)]
        self.assertEqual(len(set(id_list)), len(id_list))

    # Save Tests
    def test_save(self):
        """Tests the public instance method save()."""
        obj = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        obj.save()
        diff = obj.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    # __str__Tests
    def test_str(self):
        """Tests for __str__ method."""
        obj = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        result = rex.match(str(obj))
        selfassertIsNotNone(result)
        self.assertEqual(result.group(1), "BaseModel")
        self.assertEqual(result.group(2), obj.id)
        s = result.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        data = json.loads(s.replace("'", '"'))
        data_copy = obj.__dict__.copy()
        data_copy["created_at"] = repr(data_copy["created_at"])
        data_copy["updated_at"] = repr(data_copy["updated_at"])
        self.assertEqual(data, data_copy)

    # to_dict Tests
    def test_to_dict(self):
        """Tests the public instance method to_dict()."""
        obj = BaseModel()
        obj.name = "Laura"
        obj.age = 23
        d = obj.to_dict()
        self.assertEqual(d["id"], obj.id)
        self.assertEqual(d["__class__"], type(obj).__name__)
        self.assertEqual(d["created_at"], obj.created_at.isoformat())
        self.assertEqual(d["updated_at"], obj.updated_at.isoformat())
        self.assertEqual(d["name"], obj.name)
        self.assertEqual(d["age"], obj.age)

    def test_to_dict_no_args(self):
        """Tests to_dict() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_to_dict_excess_args(self):
        """Tests to_dict with too many arguments."""
        self.restStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

if __name__ == '__main__':
    unittest.main()
