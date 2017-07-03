import unittest
from max import read_file, my_3max

class MaxTest(unittest.TestCase):
    
    def test_read_file(self):
        expected_value = ['2134', '3412', '6421', '8723', '9239', '1234', '2345']
        test_file="sample1.dat"
        value = read_file(test_file)
        self.assertEqual(value, expected_value)

    def test_my_3max_num(self):
        expected_value = [8, 9, 10]
        test_value=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        value = my_3max(test_value)
        self.assertEqual(value, expected_value)
    
    def test_my_3max_zero(self):
        expected_value = [0, 0, 0]
        test_value=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        value = my_3max(test_value)
        self.assertEqual(value, expected_value)

    def test_my_3max_none(self):
        expected_value = []
        test_value=[]
        value = my_3max(test_value)
        self.assertEqual(value, expected_value)

if __name__ == '__main__':
    unittest.main()