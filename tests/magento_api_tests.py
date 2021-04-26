import pytest
from src.magento_2_api.magento_api import MagentoApi


class TestApiMethods(TestCase):

    def setUp(self):
        self.api = MagentoApi("YOUR_MAGENTO_WEBSITE",
                              'YOUR_INTEGRATION_KEY')

    def test_product_api_200(self):
        endpoint = '/rest/default/V1/products/'
        assert self.api.product_api('sth').status_code == 200

    def test_product_media_api_200(self):
        sku = 'sth'
        assert self.api.product_media_api('sth').status_code == 200

    def test_categories_api_200(self):
        endpoint = '/rest/default/V1/categories/'
        assert self.api.categories_api().status_code == 200

    def test_categories_media_api_200(self):
        category_id = 30
        assert self.api.categories_products_api(category_id).status_code == 200
