#!/usr/bin/python3
"""
    Contains test cases for FileStorage objects
"""
import unittest
import models
from models.engine.file_storage import FileStorage

class TestBase(unittest.TestCase):
    """
        Tests for FileStorage object
    """

    def setUp(self):
        self.fs = FileStorage
        self.fs._FileStorage__objects = {}

    def test_has_private_attribute_file_path(self):
        print(self.fs.__dict__)
        self.assertTrue(hasattr(self.fs, '_FileStorage__file_path'))

if __name__ == '__main__':
    unittest.main()
