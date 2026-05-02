import unittest
import os

class FileOps:
    def write_file(self, filename, content):
        with open(filename, "w") as f:
            f.write(content)

    def read_file(self, filename):
        with open(filename, "r") as f:
            return f.read()


class TestFileOps(unittest.TestCase):

    def test_file_ops(self):
        f = FileOps()
        filename = "test.txt"

        f.write_file(filename, "hello")
        data = f.read_file(filename)

        self.assertEqual(data, "hello")

        os.remove(filename)


if __name__ == '__main__':
    unittest.main()