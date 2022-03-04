#!/usr/bin/python3
"""
    Module for class BaseModel.
    This class is the base for the Airbnb clone console
    The rest of the classes inheritage from it
"""
from datetime import datetime
import json
import models
import uuid


class BaseModel():
    """Base class named BaseModel. Stands for parente class"""
    def __init__(self, *args, **kwargs):
        """Initializes attributes for class BaseModel
        Args:
            id: identifier number
            *args - arguments (not used)
            **kwargs - keyword arguments
        """
        if kwargs and kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == "__class__":
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string for class BaseModel"""
        clas = self.__class__.__name__
        return ("[{}] ({}) {}".format(clas, self.id, self.__dict__))

    def save(self):
        """
        Updates the publict instance attribute updated_at
        with current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary"""
        diction = self.__dict__.copy()
        diction["__class__"] = self.__class__.__name__
        diction["created_at"] = self.created_at.isoformat()
        diction["updated_at"] = self.updated_at.isoformat()
        return diction
