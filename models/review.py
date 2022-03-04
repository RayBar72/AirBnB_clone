#!/usr/bin/python3
"""Module Review that inheritage from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review that has public class atr:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
