#!/usr/bin/python3
"""Unittest for City class."""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test case for City class."""
    def setUp(self):
        """Setup method to create instances for each test."""
        self.city_instance = City()

    def test_state_id(self):
        """Test if state_id is a string"""
        self.assertEqual(type(self.city_instance.state_id), str)

    def test_name(self):
        """Test if name is a string"""
        self.assertEqual(type(self.city_instance.name), str)

    def test_default_values(self):
        """Test default values for a new instance."""
        self.assertEqual(self.city_instance.state_id, "")
        self.assertEqual(self.city_instance.name, "")

    def test_custom_values(self):
        """Test setting custom values for state_id and name."""
        custom_state_id = "NY"
        custom_name = "New York"

        new_city = City(state_id=custom_state_id, name=custom_name)

        self.assertEqual(new_city.state_id, custom_state_id)
        self.assertEqual(new_city.name, custom_name)


if __name__ == '__main__':
    unittest.main()
