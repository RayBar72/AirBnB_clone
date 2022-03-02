"""Serializes instances to a JSON file and deserializes
    JSON file to instances
"""
from models.base_model import BaseModel
import json
import os

class FileStorage:
    """Class that serializes instances to a JSON
        file and deserializas JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary of __objects"""
        return self.__objects

    def new(self, obj):
        """Sets __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        tmp_dictionary = {}
        for k, v in self.__objects.items():
            tmp_dictionary[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as working_file:
            json.dump(tmp_dictionary, working_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists('file.json'):
            with open(self.__file_path, "r") as x:
                return json.load(x)
