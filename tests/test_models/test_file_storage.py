#!/usr/bin/python3

import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInitialiazati(unittest.TestCase):
    """ This test file storage class """

    def test_storageFile_without_args_init(self):
        """ test the file storage without parameter """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_storageFile_with_args_init(self):
        """ test the file storage with parameter"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFilesStorage(unittest.TestCase):
    def setup(self):
        """ create temp file for data storing """
        self.test_file = "test_file.js"

    def remove_testFile(self):
        """ remove the temp test_file after testing """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_return_dict(self):
        """ tests if all methods returns a dictiary """
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """ tests the new method if it can create and store objs """
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new_with_args(self):
        """ expects to see if error will be raised when additial parameter is passed which is actually true"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_none(self):
        """" test creating a new object with none (Should raise AttributeError) """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        """ test saving objects to a file """
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        models.storage.new(obj_1)
        models.storage.new(obj_2)
        models.storage.save()

        # create a new instance to simulate reloading
        new_storage = FileStorage()
        new_storage.reload()

        # check if the reloaded obj mch the original obj
        self.assertTrue((new_storage.all().get(f"BaseModel.{obj_1.id}")) is not None)
        self.assertTrue((new_storage.all().get(f"BaseModel.{obj_2.id}")) is not None)

    def test_saveFile(self):
        """ test saving object to a file and check if the file is created """
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reloaded_emptyFile(self):
        """ checks reloading when file is empty or does not exist """
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()


if __name__ == '__main__':
    unittest.main()

