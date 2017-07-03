import unittest
from perfect_num import is_perfect

class PerfectNumTest(unittest.TestCase):
    
    def test_is_perfect_zero(self):
        expected_value = False
        value = is_perfect()
        self.assertEqual(expected_value, value)
    
    def test_is_perfect_zero(self):
        expected_value = False
        value = is_perfect(-1)
        self.assertEqual(expected_value, value)
    
    def test_is_perfect_zero(self):
        expected_value = False
        value = is_perfect(0)
        self.assertEqual(expected_value, value)
    
    def test_is_perfect_num1(self):
        expected_value = True
        value = is_perfect(6)
        self.assertEqual(expected_value, value)
    
    def test_is_perfect_num2(self):
        expected_value = True
        value = is_perfect(28)
        self.assertEqual(expected_value, value)

    def test_is_perfect_num3(self):
        expected_value = False
        value = is_perfect(129)
        self.assertEqual(expected_value, value)

if __name__ == '__main__':
    unittest.main()