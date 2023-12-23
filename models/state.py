#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize State instance"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return the string representation of State"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.to_dict()
        )
