#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize City instance"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return the string representation of City"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.to_dict()
        )
