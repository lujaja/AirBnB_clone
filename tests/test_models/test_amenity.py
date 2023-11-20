#!/usr/bin/python3
"""Unittest for Amenity class."""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""
    def __init__(self, *args, **kwargs):
        """Constructor for the TestAmenity class."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_default_values(self):
        """Tests if default values are set correctly."""
        new_amenity = self.value()
        self.assertEqual(new_amenity.name, "")

    def test_initialization_with_values(self):
        """Tests initialization of Amenity with specific values."""
        amenity_name = "Basketball Court"
        new_amenity = self.value(name=amenity_name)
        self.assertEqual(new_amenity.name, amenity_name)

    def test_name_is_string(self):
        """Tests if 'name' attribute of a new Amenity instance is string."""
        new_amenity = self.value()
        self.assertEqual(type(new_amenity.name), str)


if __name__ == '__main__':
    unittest.main()
