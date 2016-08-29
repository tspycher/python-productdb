import unittest
import json
from productdb.app import create_app

class BasicTestCase(unittest.TestCase):
    app = None

    def setUp(self):
        self.app = create_app('dev')

        # reload DB here
        pass

    def parseJsonResponse(self, rv):
        return json.loads(rv.data)

    @property
    def client(self):
        return self.app.test_client()

from products import ProductsTestCase


def getTestCases():
    return [ProductsTestCase]