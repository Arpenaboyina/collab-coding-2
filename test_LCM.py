import unittest
from starterfile import function1 as lcm

class TestLCM(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(5, 7), 35)
        self.assertEqual(lcm(10, 0), 0)

if __name__ == '__main__':
    unittest.main()
