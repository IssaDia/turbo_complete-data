from ebay_rest import API, Error
from app.providers.data.ebay.ebay_rest.utils import strip_html_tags
from app.interfaces.data_provider_interface import DATA_PROVIDER_INTERFACE


class EBAY_REST_PROVIDER(DATA_PROVIDER_INTERFACE):

    def __init__(self, api_client):
        self._api_client = api_client
    def get_product_by_id(self, product_id : str):
        try:
            product = self._api_client._api.buy_browse_get_item(product_id)
            if product:
                return product
        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}.\n')

    def get_products_by_keyword(self, category_name : str, limit : int):
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
    
    def get_products_descriptions(self, keyword : str, limit : int):
        try:
            products_list = self.get_products_by_keyword(keyword, limit)
            products_ids = []
            products_descriptions_clean = []
            if products_list:
                for product in products_list:
                    products_ids.append(product['item_id'])
                
                for id in products_ids:
                    item = self.get_product_by_id(id)
                    if item:
                        temp = []
                        description = strip_html_tags(item['description'])
                        category = item['category_path']
                        temp.append(description)
                        temp.append(category)
                        products_descriptions_clean.append(temp)
                        print(products_descriptions_clean)
            return products_descriptions_clean

        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}.\n')