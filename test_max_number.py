import unittest

class MaxNumber:
    def get_max(self, numbers):
        return max(numbers)


class TestMaxNumber(unittest.TestCase):

    def test_get_max(self):
        m = MaxNumber()
        self.assertEqual(m.get_max([1, 5, 3, 9]), 9)
        self.assertEqual(m.get_max([-1, -5, -3]), -1)


if __name__ == '__main__':
    unittest.main()
