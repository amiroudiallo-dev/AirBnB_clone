#!/usr/bin/python3
""" This module stores the base model objects create """

import os
import json
from models.base_model import BaseModel


class FileStorage:
    """ serializes instance to a JSON file and deserializes JSON file to instance """
    __file_path = "file.json"               # path to JSON file
    __objects = {}                          # dict that stores all obj by class id

    def all(self):
        """ returns the __objects dict used to store objects """

        return FileStorage.__objects

    def new(self, obj):
        """ adds objects to the __objects dictionary for storage """
        obj_class = obj.__class__.__name__                              # retrieves the object class name
        key = f"{obj_class}.{obj.id}"                                   # concat class name with obj id t
        FileStorage.__objects[key] = obj                                # adds the object to dict using the concat key

    def save(self):
        """ serializes __objects to JSON file i.e file.json """
        stored_objects = FileStorage.__objects
        serialized_obj_dicts = {}                                           # stores serialized objects

        for obj in stored_objects.keys():
            serialized_obj_dicts[obj] = stored_objects[obj].to_dict()       # serializing object to dict

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_obj_dicts, file, indent=2)                           # serializing converted obj dict to JSON

    def reload(self):
        """ deserializes JSON file to __objects only if JSON file exist ie '__file_path'
            otherwise, do nothing. if the file doesn't exist.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    stored_objects = json.load(file)                                    # stored_objects in python
                    for key, value in stored_objects.items():

                        obj_class, obj_id = key.split(".")                              # key = BaseModel.12323

                        converted_class = eval(obj_class)                               # convert to class
                        converted_instance = converted_class(**value)                   # instance created
                        FileStorage.__objects[key] = converted_instance                 # add instance
                except Exception:
                    pass


