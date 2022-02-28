#!/usr/bin/python3
"""
    Module for class BaseModel.
    This class is the base for the Airbnb clone console
    The rest of the classes inheritage from it
"""

from ssl import create_default_context
import uuid
from datetime import datetime


class BaseModel():
    """Base class named BaseModel. Stands for parente class"""
    
    def __init__(self):
        """Initializes attributes for class BaseModel
        Args:
            id: identifier number
            created_at = date of creation
            updated_at = date of update    
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string for class BaseModel"""
        clas = self.__class__.__name__
        return ("[{}] ({}) {}".format(clas, self.id, self.__dict__))

    def save(self):
        """Updates the publict instance attribute updated_at with current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Creates a dictionary"""
        diction = self.__dict__
        diction["__class__"] = "BaseModel"
        diction["created_at"] = self.created_at.isoformat()
        diction["updated_at"] = self.updated_at.isoformat()
        return diction
