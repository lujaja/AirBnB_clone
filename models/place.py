#!/usr/bin/env python3
"""Represent class place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Define class Place

    Attribute:
        city_id (str): City.id
        user_id (str): User.id
        name (str): string
        description (str): string
        number_rooms (int): numbr of rooms
        number_bathrooms (int): number of bath rooms
        max_guest (int): number of maximum guest
        price_by_night (int): price by night
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (list): list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
