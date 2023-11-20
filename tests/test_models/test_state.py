#!/usr/bin/python3
"""Unittest for State class."""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test case for State class."""
    def setUp(self):
        """Set up method to create instances for each test."""
        self.state_instance = State()

    def test_name_type(self):
        """Test if name is a string."""
        self.assertEqual(type(self.state_instance.name), str)

    def test_custom_values(self):
        """Test setting custom values for name."""
        custom_name = "Los Angeles"
        new_state = State(name=custom_name)
        self.assertEqual(new_state.name, custom_name)


if __name__ == '__main__':
    unittest.main()
