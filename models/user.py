#!/usr/bin/env python3
"""Represent class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Define Class User
    Attributes:
        email (str): user email address
        password (str): user password
        first_name (str): user first name
        last_name (str): user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
