#!/usr/bin/python3
"""
    Contains test cases for FileStorage objects
"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
        Tests for FileStorage object
    """

    def setUp(self):
        self.fs = FileStorage
        self.fs._FileStorage__objects = {}

    def test_has_private_attribute_file_path(self):
        self.assertTrue(hasattr(self.fs, '_FileStorage__file_path'))

    def test_has_private_attribute_objects(self):
        self.assertTrue(hasattr(self.fs, '_FileStorage__objects'))

    def test_method_all_retrieves_all_the_stored_object(self):
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        self.assertEqual(len(self.fs.all(self.fs).keys()), 3)


if __name__ == '__main__':
    unittest.main()
