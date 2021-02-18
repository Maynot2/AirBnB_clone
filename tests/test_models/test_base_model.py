#!/usr/bin/python3
"""
    Contains test cases for BasicModel objects
"""
import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """
        Tests for BasicModel objects
    """

    def setUp(self):
        self.b1 = BaseModel()

    def test_is_instance_of_BasicModel(self):
        self.assertIsInstance(self.b1, BaseModel)

    def test_saving_BaseModel_object(self):
        self.b1.save()
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)

    def test__str__(self):
        self.assertEqual(self.b1.__str__(),
                         '[{}] ({}) {}'.format(type(self.b1).__name__,
                                               self.b1.id,
                                               self.b1.__dict__))

    def test_has_id(self):
        self.assertIsNotNone(self.b1.id)

    def test_has_uniq_id(self):
        for i in range(100):
            self.assertNotEqual(self.b1.id, BaseModel().id)

    def test_id_is_a_string(self):
        self.assertEqual(type(self.b1.id), str)

    def test_added_key_is_present(self):
        self.b1.name = "Holberton"
        self.assertTrue('name' in self.b1.__dict__)

    def test_to_dict_method_adds_class_key_with_matching_class_name(self):
        self.assertEqual(self.b1.to_dict()['__class__'], 'BaseModel')

    def test_to_dict_method_converts_created_at_attr_to_a_string(self):
        self.assertEqual(type(self.b1.to_dict()['created_at']), str)

    def test_to_dict_method_converts_updated_at_attr_to_a_string(self):
        self.assertEqual(type(self.b1.to_dict()['updated_at']), str)

    def test_passing_empty_dict_as_argument_creates_regular_instance(self):
        args = {}
        b2 = BaseModel(args)
        self.assertEqual(len(b2.__dict__), 3)

    def test_passing_None_as_argument_creates_regular_instance(self):
        args = None
        b2 = BaseModel(args)
        self.assertEqual(len(b2.__dict__), 3)

    def test_passing_dict_with_missing_default_arg_creates_regular_obj(self):
        args = {
            'my_number': 89,
            'id': '38a41f60-4c43-47b5-b74f-738f72afedfd',
            'name': 'Holberton',
            'created_at': '2021-02-10T13:05:42.109437'
        }
        b2 = BaseModel(args)
        self.assertEqual(len(b2.__dict__), 3)

    def test_passing_valid_dict_creates_regular_obj_with_same_id(self):
        args = {
            'id': '38a41f60-4c43-47b5-b74f-738f72afedfd',
            'created_at': '2021-02-10T13:05:42.109437',
            'updated_at': '2021-02-10T16:33:41.743696'
        }
        b2 = BaseModel(**args)
        self.assertEqual(b2.id, '38a41f60-4c43-47b5-b74f-738f72afedfd')

    def test_passing_valid_dict_with_extra_attrs_creates_regular_obj(self):
        args = {
            'my_number': 89,
            'id': '38a41f60-4c43-47b5-b74f-738f72afedfd',
            'name': 'Holberton',
            'created_at': '2021-02-10T13:05:42.109437',
            'updated_at': '2021-02-10T16:33:41.743696'
        }
        b2 = BaseModel(**args)
        self.assertEqual(len(b2.__dict__), 5)


if __name__ == '__main__':
    unittest.main()
