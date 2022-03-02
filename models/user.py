#!/usr/bin/python3
"""
CLass User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Create attributes for user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
