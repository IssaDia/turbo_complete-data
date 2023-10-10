from ebay_rest import API, Error
import csv
from app.providers.data.ebay.ebay_rest.utils import strip_html_tags
from app.interfaces.data_provider_interface import DATA_PROVIDER_INTERFACE
from app.external.ebay_rest_connection import EBAY_REST_CONNECTION


class EBAY_REST_PROVIDER(DATA_PROVIDER_INTERFACE):

    def __init__(self):
        self._api_client = EBAY_REST_CONNECTION()
    def fetch_product_by_id(self, product_id : str):
        try:
            product = self._api_client._api.buy_browse_get_item(product_id)
            if product:
                return product
        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}.\n')

    def fetch_products_by_keyword(self, category_name : str, limit : int):
        products_list = []
        try:
            data = self._api_client._api.buy_browse_search(q=category_name, sort='price', limit=limit)
            for record in data:
                    if 'record' not in record:
                        pass
                    else:
                        item = record['record']
                        products_list.append(item)
            return products_list
        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}.\n')
    
    def fetch_product_descriptions(self, keyword : str, limit : int):
        try:
            products_list = self.fetch_products_by_keyword(keyword, limit)
            products_ids = []
            descriptions_clean = []
            if products_list:
                for product in products_list:
                    products_ids.append(product['item_id'])
                
                for id in products_ids:
                    item = self.fetch_product_by_id(id)
                    if item:
                        temp = []
                        description = strip_html_tags(item['description'])
                        category = item['category_path']
                        temp.append(description)
                        temp.append(category)
                        descriptions_clean.append(temp)
                        print(descriptions_clean)
            return descriptions_clean

        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}.\n')
    
    def transform_descriptions_to_csv(self, descriptions_list : list[str], filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'CATEGORY', 'DESCRIPTION'])
            for i, description in enumerate(descriptions_list, start=1):
                writer.writerow([i, description[1], description[0]])
    
    def get_and_export_product_descriptions(self, category_name : str, limit: int):
        try:
            descriptions = self.fetch_product_descriptions(category_name, limit)
            if descriptions:
                self.transform_descriptions_to_csv(descriptions, 'descriptions.csv')
                print(f'Description list to csv suceed!')
        except :
            print(f'Couldn\'t transform to a CSV file')
    