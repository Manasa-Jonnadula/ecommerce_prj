import unittest

class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        self.balance += amount


class TestBank(unittest.TestCase):

    def test_deposit(self):
        b = Bank()
        b.deposit(100)
        self.assertEqual(b.balance, 100)

    def test_invalid_deposit(self):
        b = Bank()
        with self.assertRaises(ValueError):
            b.deposit(-10)


if __name__ == '__main__':
    unittest.main()