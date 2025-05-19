import unittest
from task_04_db import app

class ProductTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_products_json(self):
        response = self.client.get('/?source=json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Laptop', response.data)  # assuming it's in the JSON

    def test_products_csv(self):
        response = self.client.get('/?source=csv')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Coffee Mug', response.data)  # assuming it's in the CSV

    def test_products_sql(self):
        response = self.client.get('/?source=sql')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Laptop', response.data)
        self.assertIn(b'Coffee Mug', response.data)

    def test_invalid_source(self):
        response = self.client.get('/?source=xml')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Wrong source', response.data)

    def test_valid_id_sql(self):
        # Not part of original app, you'd need to add support for ?id=
        response = self.client.get('/?source=sql')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'id', response.data)
        self.assertIn(b'1', response.data)

    def test_invalid_id_sql(self):
        # Optional advanced filter - if you add filtering by ID
        response = self.client.get('/?source=sql&id=999')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Laptop', response.data)
        self.assertNotIn(b'Coffee Mug', response.data)

if __name__ == '__main__':
    unittest.main()

