import unittest
from more_fun_with_collections import datetime_assignment as datetime


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual(datetime.half_birthday(), ('Half Birthday: ', datetime.datetime(2020, 6, 30, 0, 0)))


if __name__ == '__main__':
    unittest.main()
