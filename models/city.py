#!/usr/bin/env python3
"""Represent class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Define class City

    Attributes:
        state_id (str): State.id
        name (str): name
    """
    state_id = ""
    name = ""
