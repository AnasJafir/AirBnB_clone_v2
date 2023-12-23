#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return the string representation of User"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.to_dict()
        )
