#!/usr/bin/env python3
'''build out the test utils'''

from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    '''test the access_nested_map function'''
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
        ({'a': {'b': 2}}, ('a', 'b'), 2, None),
    ])
    def test_access_nested_map(self, map, path, expected, default=None):
        '''test access nested map'''
        self.assertEqual(expected, access_nested_map(map, path))

    @parameterized.expand([
        ({}, ('a'), None),
        ({'a': 1}, ('a', 'b'), None)
    ])
    def test_access_nested_map_exception(self, map, path, default=None):
        '''test access nested map exception'''
        with self.assertRaises(KeyError):
            access_nested_map(map, path)


class TestGetJson(TestCase):
    '''test the get_json function'''
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, url, payload):
        '''test get json'''
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = payload
            self.assertEqual(payload, get_json(url))


class TestMemoize(TestCase):
    '''test memoize exception'''

    def test_memoize(self):
        '''test memoize'''
        class TestClass:

            def a_method(self):
                '''test a method'''
                return 42

            @memoize
            def a_property(self):
                '''test a property'''
                return self.a_method()

        test_object = TestClass()
        test_object.a_method = mock.MagicMock(return_value=42)
        self.assertEqual(42, test_object.a_property)
        test_object.a_method.assert_called_once()

        with mock.patch.object(TestClass,
                               'a_method',
                               return_value=42) as mock_method:
            test_object2 = TestClass()
            self.assertEqual(42, test_object2.a_property)
            mock_method.assert_called_once()
