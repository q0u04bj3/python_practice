import unittest
from fib import fib

class FibonacciTest(unittest.TestCase):
    
    def test_fid1(self):
        c = fib()
        except_value = 1
        for i in range(1):
            value = c.next()
        self.assertEqual(except_value, value)


    def test_fid5(self):
        c = fib()
        except_value = 8
        for i in range(5):
            value = c.next()
        self.assertEqual(except_value, value)


    def test_fid20(self):
        c = fib()
        except_value = 10946
        for i in range(20):
            value = c.next()
        self.assertEqual(except_value, value)


if __name__ == '__main__':
    unittest.main()