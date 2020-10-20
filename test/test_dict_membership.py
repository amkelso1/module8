import unittest
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertEqual(dict_membership.in_dict(), {'a'})

    def test_in_dict_false(self):
        self.assertNotEqual(dict_membership.in_dict(), {'b'})


if __name__ == '__main__':
    unittest.main()