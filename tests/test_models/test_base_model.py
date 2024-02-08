#!/usr/bin/python3
""" Test cases for Base Model class """

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    def test_attribute_init(self):
        """ checks if the instance attributes are initialized """
        obj = BaseModel()

        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_save(self):
        """ checks if the created time is not same with updated time"""
        obj = BaseModel()

        first_update_at = obj.updated_at
        present_updated_at = obj.save()
        self.assertNotEqual(first_update_at, present_updated_at)

    def test_string(self):
        """ tests if the instance are printed in desired string format """
        obj = BaseModel()

        self.assertTrue(str(obj).startswith("[BaseModel]"))
        self.assertIn(obj.id, str(obj))
        self.assertIn(str(obj.__dict__), str(obj))

    def test_to_dict(self):
        """ checks if object attributes are serialized into dictionary """
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()

