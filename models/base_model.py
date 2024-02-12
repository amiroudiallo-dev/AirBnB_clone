#!/usr/bin/python3
""" the baseModel module """

import uuid
from datetime import datetime
import models

class BaseModel:
    """ This contains Airbnb base class upon which other classes inherit from """

    def __init__(self, *args, **kwargs):
        """ Initializes both instance and inherited attributes """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        models.storage.new(self)

    def __str__(self):
        """ Outputs in the string format. This method is called by either str or print """
        return f"[{__class__.__name__}], ({self.id}), {self.__dict__}"
    
    def __repr__(self):
        """ returns string representaiton of BaseModel class """
        return f"[{__class__.__name__}], ({self.id}), {self.__dict__}"
    
    def save(self):
        """ This method saves the updated_at attribute with the current date """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """ This function returns a dictionary containing keys/values of the object instance """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict


if __name__ == "__main__":

    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
