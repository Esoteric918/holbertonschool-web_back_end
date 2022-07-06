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
    @patch('client.get_json', mock.Mock(return_value={'key': 'value'}))
    def test_org(self, org):
        '''test if valid org is returned'''
        cls = GithubOrgClient(org)
        self.assertEqual(cls.org, {'key': 'value'})

    def test_public_repos_url(self):
        '''test GithubOrgClient._public_repos_url method'''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock,
                   return_value={'repos_url': 'url'}):
            mockProp = GithubOrgClient('org_prop')
            self.assertEqual(mockProp._public_repos_url, 'url')

    @patch('client.get_json')
    def test_public_repos(self, license):
        '''test GithubOrgClient.public_repos method'''
        with patch('client.GithubOrgClient.public_repos',
                   new_callable=PropertyMock) as mock_pub_repos:
            cls = GithubOrgClient('org_name')
            license.return_value = {'repos_url': 'url'}
            mock_pub_repos.return_value = cls.org.get('repos_url')
            self.assertEqual(cls.public_repos, 'url')
            license.assert_called_once()
            mock_pub_repos.assert_called_once()

    @parameterized.expand([
       ({"license": {"key": "my_license"}}, 'my_license', True),
        ({"license": {"key": "other_license"}}, 'my_license', False),
    ])

    def test_has_license(self, repo, license_key, expected):
        '''test GithubOrgClient.has_license method'''
        cls = GithubOrgClient('org_name')
        self.assertEqual(cls.has_license(repo, license_key), expected)

