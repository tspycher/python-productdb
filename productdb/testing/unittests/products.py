from . import BasicTestCase

class ProductsTestCase(BasicTestCase):

    def test_basic(self):
        rv = self.client.get('/')
        assert rv.status_code == 200

        data = self.parseJsonResponse(rv)
        assert '_links' in data


    def test_get_all_products(self):
        rv = self.client.get('/product')
        assert rv.status_code == 200

        data = self.parseJsonResponse(rv)
        assert '_items' in data
        # add further data tests here, load basic data by fixtures

        pass


