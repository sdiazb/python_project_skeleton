"""
This module contains tests for dummy module
inside this project
"""
import unittest
from mock import patch
from myproject.dummy import dummy, dummy_caller


class DummyTestCase(unittest.TestCase):
    """
    This class is a TestCase where
    functions inside dummy module
    are tested
    """
    def setUp(self):
        """
        SetUp function executed before tests
        """
        print 'Setting up test case!'

    def tearDown(self):
        """
        TearDown function executed after tests
        """
        print 'Tearing down test case!'

    def test_dummy(self):
        """
        This tests dummy function inside dummy module
        """
        self.assertEqual(dummy(), 'Dummy')

    @patch('myproject.dummy.dummy')
    def test_dummy_with_mock(self, mock_dummy):
        """
        This testsd dummy_caller function mocking
        the dummy function
        """
        mock_dummy.return_value = 'Dummy mocked'
        self.assertEqual(dummy_caller(), 'Dummy mocked')
