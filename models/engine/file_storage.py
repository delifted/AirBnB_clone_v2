#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        if cls is None:
            return self.__objects
        else:
            return {key: value for key, value in self.__objects.items()
                    if isinstance(value, cls)}

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)  # Converts clas name to a  class
                    self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass

    def close(self):
        '''Calls reload() method for deserializing the JSON file to objects'''
        self.reload()


storage = FileStorage()
storage.reload()
