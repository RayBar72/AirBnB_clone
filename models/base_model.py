#!/usr/bin/python3
"""
Create a class Basemodel
"""

import uuid
from datetime import datetime


class BaseModel:
    """A base class for console"""

    def __init__(self, *args, **kwargs):
        """initialize attributes"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    self.created_at = datetime.strptime(value,
                            '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    value = datetime.strptime(value,
                        '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())

    def __str__(self):
        """return caracteristics of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance
            attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        newdic = self.__dict__.copy()
        newdic["created_at"] = self.created_at.isoformat()
        newdic["updated_at"] = self.updated_at.isoformat()
        newdic["__class__"] = self.__class__.__name__
        return newdic
