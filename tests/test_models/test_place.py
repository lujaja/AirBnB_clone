#!/usr/bin/python3
"""Unittest for Place class."""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test case for the Place class."""
    def setUp(self):
        """Set up method to create instances for each test."""
        self.place_instance = Place()

    def test_city_id_type(self):
        """Test if city_id is a string."""
        self.assertEqual(type(self.place_instance.city_id), str)

    def test_user_id_type(self):
        """Test if user_id is a string."""
        self.assertEqual(type(self.place_instance.user_id), str)

    def test_name_type(self):
        """Test if name is a string."""
        self.assertEqual(type(self.place_instance.name), str)

    def test_description_type(self):
        """Test if description is a string."""
        self.assertEqual(type(self.place_instance.description), str)

    def test_number_rooms_type(self):
        """Test if number_rooms is an integer."""
        self.assertEqual(type(self.place_instance.number_rooms), int)

    def test_number_bathrooms_type(self):
        """Test if number_bathrooms is an integer."""
        self.assertEqual(type(self.place_instance.number_bathrooms), int)

    def test_max_guest_type(self):
        """Test if max_guest is an integer."""
        self.assertEqual(type(self.place_instance.max_guest), int)

    def test_price_by_night_type(self):
        """Test if price_by_night is an integer."""
        self.assertEqual(type(self.place_instance.price_by_night), int)

    def test_latitude_type(self):
        """Test if latitude is a float."""
        self.assertEqual(type(self.place_instance.latitude), float)

    def test_longitude_type(self):
        """Test if longitude is a float."""
        self.assertEqual(type(self.place_instance.longitude), float)

    def test_amenity_ids_type(self):
        """Test if amenity_ids is a list."""
        self.assertEqual(type(self.place_instance.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
