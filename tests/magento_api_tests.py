import unittest
import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from src.magento_2_api.magento_api import MagentoApi


class TestApiMethods(unittest.TestCase):

    def setUp(self):
        self.api = MagentoApi("YOUR_MAGENTO_WEBSITE",
                              'YOUR_INTEGRATION_KEY')

    def test_product_api_200(self):
        assert self.api.product_api('sth').status_code == 200

    def test_product_media_api_200(self):
        sku = 'sth'
        assert self.api.product_media_api(sku).status_code == 200

    def test_categories_api_200(self):
        assert self.api.categories_api().status_code == 200

    def test_categories_media_api_200(self):
        category_id = 30
        assert self.api.categories_products_api(category_id).status_code == 200

    def test_guest_cart_create_200(self):
        assert self.api.guest_cart_create().status_code == 200

    def test_guest_cart_get_200(self):
        guest_cart_id = self.api.guest_cart_create().text.replace('"', '')
        assert self.api.guest_cart_get(guest_cart_id).status_code == 200
