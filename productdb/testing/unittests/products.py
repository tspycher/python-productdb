import unittest
from flask import current_app


class ProductsTestCase(unittest.TestCase):

    def test_get_all_products(self):
        pass

    def setUp(self):
        # reload DB here
        pass

    @property
    def client(self):
        return current_app.test_client()
