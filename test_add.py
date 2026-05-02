import unittest

class AddDigits:
    def add_digits(self, a, b):
        return a + b


class TestAddDigits(unittest.TestCase):

    def test_add_digits(self):
        add = AddDigits()
        result = add.add_digits(2, 3)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()