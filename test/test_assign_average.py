import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_a_grade(self):
        self.assertEqual(assign_average.switch_average(entry='A'), 'Welcome to the dean\'s list')

    def test_b_grade(self):
        self.assertEqual(assign_average.switch_average(entry='B'), 'Congratulations om receiving your final grade!')

    def test_c_grade(self):
        self.assertEqual(assign_average.switch_average(entry='C'), 'Congratulations om receiving your final grade!')

    def test_d_grade(self):
        self.assertEqual(assign_average.switch_average(entry='D'), 'Congratulations om receiving your final grade!')

    def test_f_grade(self):
        self.assertEqual(assign_average.switch_average(entry='F'), 'Congratulations om receiving your final grade!')

    def test_not_grade(self):
        self.assertNotEqual(assign_average.switch_average(entry='E'), 'Congratulations om receiving your final grade!')


if __name__ == '__main__':
    unittest.main()
