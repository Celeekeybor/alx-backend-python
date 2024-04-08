#!/usr/bin/env python3
"""Parameterize a unit test
"""
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map utils methods
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test that the method returns what it is supposed to.
         """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Exception access nested method
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)

        self.assertEqual(
            f'KeyError({str(error.exception)})', repr(error.exception))


class TestGetJson(unittest.TestCase):
    """ Class to test get_json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Mock HTTP calls
        """
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ Test memoize class """

    def test_memoize(self):
        """ Test memoize """
        class TestClass:
            """ Test Class """

            def a_method(self):
                """ A method that returns 42 """
                return 42

            @memoize
            def a_property(self):
                """ Decorator """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
