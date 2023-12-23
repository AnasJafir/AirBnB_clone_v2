#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
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

    def __init__(self, *args, **kwargs):
        """Initialize Place instance"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return the string representation of Place"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.to_dict()
        )
