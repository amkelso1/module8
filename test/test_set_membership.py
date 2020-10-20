import unittest
from unittest.mock import patch
from more_fun_with_collections import set_membership


class MyTestCase(unittest.TestCase):
    @patch('more_fun_with_collections.set_membership.in_set', return_value=True)
    def test_in_set_true(self, input):
        self.assertTrue(set_membership.in_set(), 'b')

    @patch('more_fun_with_collections.set_membership.in_set', return_value=False)
    def test_in_set_false(self, input):
        self.assertFalse(set_membership.in_set(), 'a')


if __name__ == '__main__':
    unittest.main()
