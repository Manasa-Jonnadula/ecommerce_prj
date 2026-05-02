import unittest

class Palindrome:
    def is_palindrome(self, text):
        return text == text[::-1]


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        p = Palindrome()
        self.assertTrue(p.is_palindrome("madam"))
        self.assertFalse(p.is_palindrome("hello"))


if __name__ == '__main__':
    unittest.main()