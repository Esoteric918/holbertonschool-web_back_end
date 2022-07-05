#!/usr/bin/env python3
'''build out tests for client.py'''

from client import GithubOrgClient
import unittest
from unittest import mock
from parameterized import parameterized
from unittest.mock import PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    ''' Test the GithubOrgClient class'''

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])

    @patch('client.get_json', mock.Mock(return_value={'key':'value'}))
    def test_org(self, org):
        '''test if valid org is returned'''
        cls = GithubOrgClient(org)
        self.assertEqual(cls.org, {'key':'value'})

    def test_public_repos_url(self):
        '''test GithubOrgClient._public_repos_url method'''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock,
                   return_value={'repos_url': 'url'}):
            mockProp = GithubOrgClient('org_prop')
            self.assertEqual(mockProp._public_repos_url, 'url')
