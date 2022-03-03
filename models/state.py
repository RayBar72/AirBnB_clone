#!/usr/bin/python3
"""Module State that inheritage from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class State that has public class atr:
        name: string - empty string
    """
    name = ""
