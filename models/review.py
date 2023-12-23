#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize Review instance"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return the string representation of Review"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.to_dict()
        )
