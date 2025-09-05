import unittest
from prime_check import function2

class TestPrimeCheck(unittest.TestCase):

    def test_prime_numbers(self):
        """Test that prime numbers return True"""
        self.assertTrue(function2(2))
        self.assertTrue(function2(3))
        self.assertTrue(function2(5))
        self.assertTrue(function2(7))
        self.assertTrue(function2(11))
        self.assertTrue(function2(13))

    def test_non_prime_numbers(self):
        """Test that non-prime numbers return False"""
        self.assertFalse(function2(1))
        self.assertFalse(function2(4))
        self.assertFalse(function2(6))
        self.assertFalse(function2(8))
        self.assertFalse(function2(9))
        self.assertFalse(function2(12))

    def test_negative_and_zero(self):
        """Test that negative numbers and zero are not prime"""
        self.assertFalse(function2(-5))
        self.assertFalse(function2(0))
        self.assertFalse(function2(-11))

    def test_large_prime(self):
        """Test a larger prime number"""
        self.assertTrue(function2(101))

    def test_large_non_prime(self):
        """Test a larger non-prime number"""
        self.assertFalse(function2(100))

if __name__ == "__main__":
    unittest.main()