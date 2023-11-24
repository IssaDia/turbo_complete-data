from providers.data.ebay.ebay_rest.ebay_rest_provider import EBAY_REST_PROVIDER

class GET_DESCRIPTIONS_USE_CASE():
    def __init__(self, api : EBAY_REST_PROVIDER):
        self.api = api
    
    def execute(self,category_name : str, limit : int):
        return self.api.fetch_product_descriptions(category_name, limit)

class GET_IMAGES_USE_CASE():
    def __init__(self, api : EBAY_REST_PROVIDER):
        self.api = api
    
    def execute(self,category_name : str, limit : int):
        return self.api.get_images_file(category_name, limit, "images")
