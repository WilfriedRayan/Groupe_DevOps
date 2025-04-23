# test_operations.py

import unittest
from operation import addition, soustraction, multiplication, division

class TestOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 3), 12)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)

    def test_division_par_zero(self):
        with self.assertRaises(ValueError):
            division(10, 0)

if __name__ == "__main__":
    unittest.main()