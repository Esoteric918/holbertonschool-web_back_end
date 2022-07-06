#!/usr/bin/env python3
'''build out tests for client.py'''

from urllib.error import HTTPError
from client import GithubOrgClient
from unittest import TestCase
from unittest import mock
from parameterized import parameterized, parameterized_class
from unittest.mock import PropertyMock, patch
from fixtures import *


class TestGithubOrgClient(TestCase):
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


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
    )
class TestIntegrationGithubOrgClient(TestCase):
    ''' test the GithubOrgClient.public_repos
        method in an integration test
    '''

    @classmethod
    def setUpClass(cls):
        ''' part of the unittest.TestCase API'''
        cls.get_patcher = patch('requests.get.json', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        ''' part of the unittest.TestCase API'''
        cls.get_patcher.stop()
