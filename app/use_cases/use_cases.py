from app.providers.data.ebay.ebay_rest.ebay_rest_provider import EBAY_REST_PROVIDER

class GET_PRODUCTS_KEYWORDS_USE_CASE():
    def __init__(self, api : EBAY_REST_PROVIDER):
        self.api = api
    
    def execute(self,category_name : str, limit : int):
        return self.api.get_products_by_keyword(category_name, limit)

class GET_PRODUCTS_DESCRIPTION_USE_CASE():
    def __init__(self, api : EBAY_REST_PROVIDER):
        self.api = api
    
    def execute(self,category_name : str, limit : int):
        return self.api.get_products_descriptions(category_name, limit)
