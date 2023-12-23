#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return the string representation of Amenity"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.to_dict()
        )
