#!/usr/bin/env python3

from client import GithubOrgClient
import unittest
from unittest import mock
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    ''' Test the GithubOrgClient class'''

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])

    @patch('client.get_json',mock.Mock(return_value={'key':'value'}))
    def test_org(self, org):
        '''test if valid org is returned'''
        cls = GithubOrgClient(org)
        self.assertEqual(cls.org, {'key':'value'})
