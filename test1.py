import unittest
from starterfile import fibonacci_sequence

class TestFibonacci(unittest.TestCase):
    """A test case for the fibonacci_sequence function."""

    def test_base_cases(self):
        """Tests the base cases of the Fibonacci sequence (n=0 and n=1)."""
        self.assertEqual(fibonacci_sequence(0), 0)
        self.assertEqual(fibonacci_sequence(1), 1)

    def test_small_positive_integers(self):
        """Tests the function with small positive integers."""
        self.assertEqual(fibonacci_sequence(2), 1)
        self.assertEqual(fibonacci_sequence(5), 5)
        self.assertEqual(fibonacci_sequence(7), 13)

    def test_larger_positive_integers(self):
        """Tests the function with a larger integer."""
        self.assertEqual(fibonacci_sequence(10), 55)
        self.assertEqual(fibonacci_sequence(15), 610)

    def test_raises_value_error_for_negative_input(self):
        """Ensures a ValueError is raised for negative input."""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)
            fibonacci_sequence(-5)

    def test_raises_type_error_for_non_integer_input(self):
        """Ensures a TypeError is raised for non-integer input."""
        with self.assertRaises(TypeError):
            fibonacci_sequence(3.5)
            fibonacci_sequence("ten")
            
if __name__ == '__main__':
    unittest.main(verbosity=2)