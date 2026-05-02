import unittest

def get_product(product_id):
    products = {
        1: "Laptop",
        2: "Mobile"
    }
    return products.get(product_id, None)

class TestAPI(unittest.TestCase):

    def test_get_product(self):
        self.assertEqual(get_product(1), "Laptop")
        self.assertIsNone(get_product(10))

if __name__ == '__main__':      
    unittest.main()