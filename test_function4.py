import unittest
from starterfile import function4

class TestFunction4(unittest.TestCase):
    def test_gcd_positive_numbers(self):
        self.assertEqual(function4(56, 98), 14)
        self.assertEqual(function4(48, 18), 6)
        self.assertEqual(function4(100, 25), 25)

    def test_gcd_with_one_zero(self):
        self.assertEqual(function4(0, 5), 5)
        self.assertEqual(function4(7, 0), 7)

    def test_gcd_both_zero(self):
        # By convention, we treat GCD(0, 0) as 0 in this project
        self.assertEqual(function4(0, 0), 0)

    def test_gcd_same_numbers(self):
        self.assertEqual(function4(25, 25), 25)
        self.assertEqual(function4(7, 7), 7)

    def test_gcd_coprime_numbers(self):
        self.assertEqual(function4(17, 13), 1)
        self.assertEqual(function4(35, 64), 1)

    def test_gcd_with_negative_numbers(self):
        self.assertEqual(function4(-56, 98), 14)
        self.assertEqual(function4(56, -98), 14)
        self.assertEqual(function4(-56, -98), 14)

if __name__ == "__main__":
    unittest.main()
