#!/usr/bin/env python3
'''build out the test utils'''

from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map

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
