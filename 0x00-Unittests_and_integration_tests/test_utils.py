#!/usr/bin/env python3
'''build out the test utils'''

from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json

class TestAccessNestedMap(TestCase):

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
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, url, payload):
        '''test get json'''
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = payload
            self.assertEqual( payload, get_json(url))

