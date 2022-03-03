#!/usr/bin/python3
"""Module Amenity that inheritage from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class Amenity that has public class atr:
        name: string - empty string
    """
    name = ""
