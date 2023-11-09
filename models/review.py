#!/usr/bin/env python3
"""Represent class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Define class Review

    Attribute:
        place_id (str): Place.id
        user_id (str): User.id
        text (str): string
    """
    place_id = ""
    user_id = ""
    text = ""
