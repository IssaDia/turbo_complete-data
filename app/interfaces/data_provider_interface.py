from abc import ABC, abstractmethod


class DATA_PROVIDER_INTERFACE():

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def get_product_by_keywords(self, product_id):
        pass

    @abstractmethod
    def search_products(self, keyword, limit):
        pass

    @abstractmethod
    def get_products_descriptions(self, keyword, limit):
        pass
