from providers.data.ebay.ebay_rest.utils import *
from interfaces.data_provider_interface import DATA_PROVIDER_INTERFACE
from external.ebay_rest_connection import EBAY_REST_CONNECTION

class EBAY_REST_PROVIDER(DATA_PROVIDER_INTERFACE):
    def __init__(self):
        self._api_client = EBAY_REST_CONNECTION()

    def fetch_product_by_id(self, product_id):
        return fetch_product_by_id(self._api_client, product_id)

    def fetch_products_by_keyword(self, category_name, limit):
        return fetch_products_by_keyword(self, category_name, limit)

    def fetch_product_descriptions(self, keyword, limit):
        return fetch_product_descriptions(self._api_client, keyword, limit)

    def transform_descriptions_to_csv(self, descriptions_list, filename):
        return transform_descriptions_to_csv(descriptions_list, filename)

    def get_and_export_product_descriptions(self, category_name, limit):
        try:
            descriptions = self.fetch_product_descriptions(category_name, limit)
            if descriptions:
                self.transform_descriptions_to_csv(descriptions, 'descriptions.csv')
                print(f'Description list to CSV succeeded!')
        except:
            print(f'Couldn\'t transform to a CSV file')

    def fetch_products_images_url(self, keyword, limit):
        return fetch_products_images_url(self._api_client, keyword, limit)

    def get_images_file(self, keyword, limit, folder_target):
        return get_images_file(self._api_client, keyword, limit, folder_target)
