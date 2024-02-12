#!/usr/bin/python3
""" This module stores the base model objects create """

import os
import json
from models.base_model import BaseModel


class FileStorage:
    """ serialize & deserializes JSON file """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the __objects dict used to store objects """

        return FileStorage.__objects

    def new(self, obj):
        """ adds objects to the __objects dictionary for storage """
        obj_class = obj.__class__.__name__
        key = f"{obj_class}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to JSON file i.e file.json """
        stored_objects = FileStorage.__objects
        serialized_obj_dicts = {}

        for obj in stored_objects.keys():
            serialized_obj_dicts[obj] = stored_objects[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_obj_dicts, file, indent=2)

    def reload(self):
        """ deserializes JSON file to __objects """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    stored_objects = json.load(file)
                    for key, value in stored_objects.items():

                        obj_class, obj_id = key.split(".")

                        converted_class = eval(obj_class)
                        converted_instance = converted_class(**value)
                        FileStorage.__objects[key] = converted_instance
                except Exception:
                    pass
