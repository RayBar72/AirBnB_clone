#!/usr/bin/python3
"""Module City that inheritage from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City that has public class atr:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
