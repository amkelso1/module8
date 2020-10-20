import unittest
from unittest.mock import patch
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    @patch('more_fun_with_collections.dict_membership.in_dict', return_value=True)
    def test_in_dict_true(self, input):
        self.assertTrue(dict_membership.in_dict(), 'a')

    @patch('more_fun_with_collections.dict_membership.in_dict', return_value=False)
    def test_in_dict_false(self, input):
        self.assertFalse(dict_membership.in_dict(), 'd')


if __name__ == '__main__':
    unittest.main()
