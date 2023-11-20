#!/usr/bin/python3
"""Unittest for User class."""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test case for the User class."""
    def setUp(self):
        """Set up method to create instances for each test."""
        self.user_instance = User()

    def test_first_name_type(self):
        """Test if first_name is a string."""
        self.assertEqual(type(self.user_instance.first_name), str)

    def test_last_name_type(self):
        """Test if last_name is a string."""
        self.assertEqual(type(self.user_instance.last_name), str)

    def test_email_type(self):
        """Test if email is a string."""
        self.assertEqual(type(self.user_instance.email), str)

    def test_password_type(self):
        """Test if password is a string."""
        self.assertEqual(type(self.user_instance.password), str)

    def test_custom_values(self):
        """Test setting custom values."""
        custom_first_name = "Eliza"
        custom_last_name = "Doe"
        custom_email = "elizadoe@gmail.com"
        custom_password = "secure_password"

        new_user = User(
                first_name=custom_first_name,
                last_name=custom_last_name,
                email=custom_email,
                password=custom_password
                )

        self.assertEqual(new_user.first_name, custom_first_name)
        self.assertEqual(new_user.last_name, custom_last_name)
        self.assertEqual(new_user.email, custom_email)
        self.assertEqual(new_user.password, custom_password)


if __name__ == '__main__':
    unittest.main()
