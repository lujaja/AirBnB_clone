#!/usr/bin/python3
"""Unittest for Review class."""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test case for Review class."""
    def setUp(self):
        """Set up method to create instances for each test."""
        self.review_instance = Review()

    def test_place_id_type(self):
        """Test if place_id is a string."""
        self.assertEqual(type(self.review_instance.place_id), str)

    def test_user_id_type(self):
        """Test if user_id is a string."""
        self.assertEqual(type(self.review_instance.user_id), str)

    def test_text_type(self):
        """Test if text is a string."""
        self.assertEqual(type(self.review_instance.text), str)

    def test_custom_values(self):
        """Test setting custom values for place_id, user_id, and text."""
        custom_place_id = "12345"
        custom_user_id = "67890"
        custom_text = "This is a custom review."

        new_review = Review(
                place_id=custom_place_id,
                user_id=custom_user_id,
                text=custom_text
                )

        self.assertEqual(new_review.place_id, custom_place_id)
        self.assertEqual(new_review.user_id, custom_user_id)
        self.assertEqual(new_review.text, custom_text)


if __name__ == '__main__':
    unittest.main()
