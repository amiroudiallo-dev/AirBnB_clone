#!/usr/bin/python3

""" This contains Airbnb base class upon which other class inherit from"""
import cmd
import uuid
from datetime import datetime

class BaseModel(cmd.Cmd):
    """ This is the command interpreter class"""

    def __init__(self):
        """ initializes both instance and inherited attributes """
        super().__init__()
        self.id = str(uuid.uuid4())  # remember to test for string output
        self.created_at = datetime.utcnow()    # remember to check if datetime when user is created is correct
        self.updated_at = datetime.utcnow()    # remember to confirm that updated_at is not same with created_at field

    def __str__(self):
        """ outputs in the string format. this method is called by either str or print """
        return f"[{__class__.__name__}], ({self.id}), {self.__dict__}"   # check if the output is format is in give project sample

    def save(self):
        """ This method saves the updated_at attribute with the current date """
        self.updated_at = datetime.utcnow()                                        # check that the updated time is correct. this guy failed

    def to_dict(self):
        """ This function returns a contain keys/values of the object instance """
        obj_dict = self.__dict__.copy()                                     # ensures data integrity is maintained
        obj_dict["__class__"] = self.__class__.__name__                     # check for class name
        obj_dict["created_at"] = self.created_at.isoformat()                # check if key created_at exist in obj_dict
        obj_dict["updated_at"] = self.updated_at.isoformat()                # check if key updated_at exist in obj_dict
        return obj_dict


#
# def main():
#     obj = BaseModel()
#     print(obj.created_at)
#     obj.save()
#     print(obj.updated_at)
#     print(obj.to_dict())



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


