import unittest

class DivideDigits:
    def divide_digits(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class TestDivideDigits(unittest.TestCase):

    def test_divide_digits(self):
        divide = DivideDigits()

        self.assertEqual(divide.divide_digits(10, 2), 5)
        self.assertEqual(divide.divide_digits(7, -2), -3.5)

        with self.assertRaises(ValueError):
            divide.divide_digits(5, 0)


if __name__ == '__main__':
    unittest.main()