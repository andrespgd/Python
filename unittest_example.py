import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_addition(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_addition_with_negative_numbers(self):
        result = add(-1, -2)
        self.assertEqual(result, -3)

if __name__ == '__main__':
    unittest.main()

# RUN: python test_add.py
