import unittest
from name_score import name_score

class NameScoreTest(unittest.TestCase):
    
    def test_name_score1(self):
        file_data = '"CDEF", "ABC", "FIJK"'
        expected_value = [6, 36, 108]
        value = name_score(file_data)
        self.assertEqual(value, expected_value)

    def test_name_score3(self):
        file_data = '"", "AB", "ZOIU"'
        expected_value = [3, 142]
        value = name_score(file_data)
        self.assertEqual(value, expected_value)

    def test_name_score4(self):
        file_data = '"!!!!", "@@=+", "FIJK"'
        expected_value = [36]
        value = name_score(file_data)
        self.assertEqual(value, expected_value)

    def test_name_score5(self):
        file_data = '"CDEF", "ABC", "FIJK", "99678"'
        expected_value = [6, 36, 108]
        value = name_score(file_data)
        self.assertEqual(value, expected_value)

if __name__ == '__main__':
    unittest.main()