"""Serializes instances to a JSON file and deserializes
    JSON file to instances
"""
from models.base_model import BaseModel
from models.user import User
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

    def classes(self):
        """Dictionary with valid classes"""
        classes = {"BaseModel": BaseModel,
                   "User": User}
        return classes

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as x:
            jfiledict = json.load(x)
            jfiledict = {k: self.classes()[v["__class__"]](
                **v) for k, v in jfiledict.items()}
            FileStorage.__objects = jfiledict
