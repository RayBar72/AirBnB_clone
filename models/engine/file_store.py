#!/bin/usr/python3
"""
Class file store:
serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file
        and deserializes JSON file to instances
    """
    __file_path = "ni idea"
    __objects = "ni idea"

    def all(self):
        """return dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

    def reload(self):
        """deserializes the JSON file to __objects"""

