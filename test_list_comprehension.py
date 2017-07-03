import unittest
from list_comprehension import fun

class ListComprehensionTest(unittest.TestCase):
    
    def test_list_comprehension_zero(self):
        expected_value = 0
        value = fun(0,0)
        self.assertEqual(expected_value, value)
    
    def test_list_comprehension_num1(self):
        expected_value = -55
        value = fun(1,11)
        self.assertEqual(expected_value, value)
    
    def test_list_comprehension_num2(self):
        expected_value = 4951
        value = fun(1,20)
        self.assertEqual(expected_value, value)

if __name__ == '__main__':
    unittest.main()