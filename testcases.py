import unittest
from option1 import findDuplicate, findDuplicateTwo

class TestFindDuplicate(unittest.TestCase):

    def test_single_duplicate(self):
        input_data = [1, 3, 4, 2, 2]
        self.assertEqual(findDuplicate(input_data), 2)

    def test_multiple_duplicates(self):
        input_data = [1, 2, 3, 4, 3]
        # Since the function returns the first duplicate it finds,
        # in this case it will return 3.
        self.assertEqual(findDuplicate(input_data), 3)

    def test_large_input(self):
        input_data = [1, 5, 6, 3, 4, 2, 6]
        self.assertEqual(findDuplicateTwo(input_data), 6)

    def test_duplicate_at_end(self):
        input_data = [1, 2, 3, 4, 5, 5]
        self.assertEqual(findDuplicateTwo(input_data), 5)


if __name__ == '__main__':
    unittest.main()
    