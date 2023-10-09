from ebay_rest import API, Error
from ebay_api import EbayAPIClient

class EbayOperations:
    def __init__(self, application : str, user : str, header : str):
        self._api = EbayAPIClient(application, user, header)
        self._connected = False
        try:
            if not self._connected:
                self._api.connect()
                self._connected = True
            print('Connected to Ebay API')
        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}. \n')
    
    def get_product_by_id(self, product_id : str):
        try:
            
             if self._connected:
                    product = self._api.api.buy_browse_get_item(product_id)
                    if product:
                        return product
        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}.\n')
    
    def get_products_by_keyword(self, category_name : str, limit : int):
        products_list = []
        try:
            if self._connected:
                data = self._api.api.buy_browse_search(q=category_name, sort='price', limit=limit)
                for record in data:
                    if 'record' not in record:
                        pass
                    else:
                        item = record['record']
                        products_list.append(item)
            print(products_list)
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
                        description = self.strip_html_tags(item['description'])
                        category = item['category_path']
                        temp.append(description)
                        temp.append(category)
                        products_descriptions_clean.append(temp)
            return products_descriptions_clean

        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}.\n')