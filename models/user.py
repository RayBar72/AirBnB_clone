#!/usr/bin/python3
"""Module User that inheritage from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User that has public class atr:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
